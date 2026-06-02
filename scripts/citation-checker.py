#!/usr/bin/env python3
"""
citation-checker.py — fiscaliza anti-plágio: citação literal e bloco de fonte

PART OF: Offer Book Squad / scripts
OWNER_AGENT: compliance-auditor
CONSUMES: reference/, frameworks/reference-intellectual/, swipe/, swipe-sources/ (+ regras de swipe.config)
PRODUCES: relatório no stdout + .citation-report.json (na raiz)
USAGE:
  python scripts/citation-checker.py                 # varre os dirs citáveis
  python scripts/citation-checker.py --dir reference
  python scripts/citation-checker.py --max-words 25  # piso de citação literal
  python scripts/citation-checker.py --check         # dry-run read-only (não escreve json)
DEPENDS: stdlib (+ pyyaml; swipe.config opcional p/ ler o limite)
EXIT: 0 sem violação · 1 citação > limite ou bloco de fonte ausente · 2 erro de uso
"""
from __future__ import annotations
import argparse, json, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário (pip install pyyaml)"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env", "fixtures"}

# Dirs que exigem proveniência (ARCHITECTURE §7; style-guide §3).
CITABLE_PREFIXES = ("reference/", "frameworks/reference-intellectual/", "swipe/", "swipe-sources/")
DEFAULT_MAX_WORDS = 25

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
# Linhas de citação em bloco markdown: começam com ">".
QUOTE_LINE_RE = re.compile(r"^\s*>\s?(.*)$")
WORD_RE = re.compile(r"\b[\wÀ-ÿ]+\b", re.UNICODE)
# Sinais de um bloco de Fonte/citação conforme style-guide §3.
SOURCE_MARKERS = ("**fonte:**", "**source:**", "## fonte", "## citação", "## sources")


def load_max_words(cli_value: int | None) -> int:
    if cli_value is not None:
        return cli_value
    cfg = os.path.join(ROOT, "swipe.config")
    if os.path.exists(cfg):
        try:
            data = yaml.safe_load(open(cfg, encoding="utf-8").read()) or {}
            rules = data.get("rules", {}) or {}
            v = rules.get("verbatim_quote_max_words")
            if isinstance(v, int):
                return v
        except Exception:
            pass
    return DEFAULT_MAX_WORDS


def iter_md(target_dir: str):
    for dp, dns, fns in os.walk(target_dir):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if fn.endswith(".md"):
                yield os.path.join(dp, fn)


def is_citable(rel: str) -> bool:
    return rel.startswith(CITABLE_PREFIXES)


def split_frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    return fm, text[m.end():]


def collect_quote_blocks(body: str):
    """Agrupa linhas '>' contíguas num bloco; retorna lista de (linha_inicial, texto)."""
    blocks, cur, start = [], [], None
    for i, line in enumerate(body.splitlines(), 1):
        m = QUOTE_LINE_RE.match(line)
        if m:
            if start is None:
                start = i
            cur.append(m.group(1))
        else:
            if cur:
                blocks.append((start, " ".join(cur).strip()))
                cur, start = [], None
    if cur:
        blocks.append((start, " ".join(cur).strip()))
    return blocks


def check_file(path: str, max_words: int) -> dict:
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    issues, warns = [], []
    text = open(path, encoding="utf-8").read()
    fm, body = split_frontmatter(text)
    no_fence = FENCE_RE.sub(" ", body)
    low = no_fence.lower()

    # 1) bloco de fonte/citação presente? (frontmatter `sources` OU marcador no corpo)
    has_sources_fm = bool(fm.get("sources"))
    has_source_block = any(mk in low for mk in SOURCE_MARKERS)
    is_index = os.path.basename(rel) == "index.md"
    if not (has_sources_fm or has_source_block):
        # índices podem herdar proveniência dos itens — vira aviso, não erro
        (warns if is_index else issues).append("bloco de fonte/citação ausente (sem `sources` nem '> **Fonte:**')")

    # 2) citação literal > max_words em qualquer bloco '>'
    long_quotes = []
    for ln, qtext in collect_quote_blocks(no_fence):
        # ignora as linhas meta do bloco anti-verbatim (Fonte:/Anti-verbatim:)
        meta = qtext.lower().lstrip("* ").startswith(("fonte:", "source:", "anti-verbatim", "**fonte", "**anti"))
        wc = len(WORD_RE.findall(qtext))
        if wc > max_words and not meta:
            long_quotes.append((ln, wc, qtext[:60]))
    if long_quotes:
        issues.append(f"{len(long_quotes)} citação(ões) literal(is) > {max_words} palavras "
                      f"(1ª na linha {long_quotes[0][0]}: {long_quotes[0][1]} palavras)")

    ok = not issues
    return {"rel": rel, "ok": ok, "issues": issues, "warns": warns,
            "long_quotes": [{"line": ln, "words": wc, "snippet": sn} for ln, wc, sn in long_quotes]}


def main():
    ap = argparse.ArgumentParser(description="Checa citação literal (>25 palavras) e bloco de fonte.")
    ap.add_argument("--dir", default="", help="restringe a um subdiretório (default: todos os dirs citáveis)")
    ap.add_argument("--max-words", type=int, default=None, help="piso de citação literal (default: swipe.config ou 25)")
    ap.add_argument("--check", action="store_true", help="dry-run read-only (não escreve json)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    max_words = load_max_words(a.max_words)

    if a.dir:
        target = os.path.normpath(os.path.join(ROOT, a.dir))
        if not os.path.isdir(target):
            print(f"ERRO: diretório inexistente: {a.dir}"); sys.exit(2)
        paths = [p for p in sorted(iter_md(target))]
    else:
        paths = []
        for pref in ("reference", "frameworks/reference-intellectual", "swipe", "swipe-sources"):
            d = os.path.join(ROOT, pref)
            if os.path.isdir(d):
                paths.extend(sorted(iter_md(d)))

    # filtra só os citáveis (se --dir apontar p/ algo não-citável, ainda checamos o que estiver lá)
    results = [check_file(p, max_words) for p in paths]

    n = len(results)
    bad = [r for r in results if r["issues"]]
    warn_only = [r for r in results if r["warns"] and not r["issues"]]

    print("\n=== CITATION-CHECKER ===")
    print(f"arquivos: {n} · limite de citação literal: {max_words} palavras")
    print(f"com violação: {len(bad)} · com aviso: {len(warn_only)} · limpos: {n - len(bad) - len(warn_only)}")
    if not a.quiet:
        for r in bad:
            print(f"  ✗ {r['rel']}: " + " | ".join(r["issues"]))
        for r in warn_only:
            print(f"  ⚠ {r['rel']}: " + " | ".join(r["warns"]))

    if not a.check:
        json.dump({"files": n, "max_words": max_words,
                   "violations": [r for r in results if r["issues"]],
                   "results": results},
                  open(os.path.join(ROOT, ".citation-report.json"), "w"),
                  ensure_ascii=False, indent=1)

    ok = not bad
    print(f"\nRESULTADO: {'CITAÇÃO OK ✅' if ok else 'VIOLAÇÃO ❌'} ({len(bad)} arquivo(s))\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
