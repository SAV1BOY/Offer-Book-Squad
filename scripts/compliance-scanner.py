#!/usr/bin/env python3
"""
compliance-scanner.py — heurística de claims sem prova + escassez/urgência suspeita

PART OF: Offer Book Squad / scripts
OWNER_AGENT: compliance-auditor
CONSUMES: os .md do repo (copy/oferta); aplica princípios claim_backing + truthful_scarcity
PRODUCES: relatório no stdout + .compliance-report.json (na raiz)
USAGE:
  python scripts/compliance-scanner.py             # repo inteiro (heurístico, informativo)
  python scripts/compliance-scanner.py --dir templates/copy
  python scripts/compliance-scanner.py --strict    # qualquer flag vira FALHA (exit 1)
  python scripts/compliance-scanner.py --check      # dry-run read-only (não escreve json)
DEPENDS: stdlib (+ pyyaml p/ pular frontmatter)
EXIT: 0 ok (sem flags, ou flags só em --check informativo) · 1 flags em --strict · 2 erro de uso

NOTA: heurístico por design. Sinaliza padrões para revisão humana do compliance-auditor;
não substitui o gate. Falsos positivos são esperados (ex.: prosa que ensina a NÃO mentir).
"""
from __future__ import annotations
import argparse, json, os, re, sys

try:
    import yaml  # noqa: F401  (usado só p/ detectar/pular frontmatter)
    HAVE_YAML = True
except Exception:
    HAVE_YAML = False

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env"}

FM_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)

# Números/percentuais/dinheiro que normalmente exigem fonte (claim factual).
NUMERIC_CLAIM_RE = re.compile(
    r"(?<![\w/])(?:R\$\s?\d|US\$\s?\d|\$\s?\d|\d[\d.,]*\s?%|\d[\d.,]*\s?x\b|"
    r"\d[\d.,]*\s?(?:mil|milh[õo]es|clientes|alunos|vendas|dias))",
    re.IGNORECASE,
)
# Marcadores de prova/atribuição na MESMA linha que abonam um número.
PROOF_NEARBY_RE = re.compile(
    r"(fonte|source|via |segundo |conforme |estudo|pesquisa|registry|proof|"
    r"\bcf\.|\[|depoimento|caso|case|evid[êe]ncia|m[ée]dia de|exemplo)",
    re.IGNORECASE,
)
# Escassez/urgência: termos que pedem lastro real (truthful_scarcity).
SCARCITY_RE = re.compile(
    r"\b(?:[uú]ltim[ao]s?|s[oó]\s+hoje|agora\s+ou\s+nunca|vagas?\s+limitad|"
    r"acaba\s+(?:hoje|amanh[ãa])|encerra|expira|fecha\s+(?:hoje|amanh[ãa])|"
    r"corre|n[aã]o\s+perca|tempo\s+esgotando|restam?\s+\d|apenas\s+\d|"
    r"limited|last\s+chance|expires|ending\s+soon|hurry|don'?t\s+miss)\b",
    re.IGNORECASE,
)
# Quando a escassez vem qualificada como REAL/verdadeira, é o uso correto -> não sinaliza.
TRUTH_QUALIFIER_RE = re.compile(
    r"\b(?:verdadeir|real|reais|genu[íi]n|honest|leg[íi]tim|de\s+verdade|"
    r"capacidade|lote|janela|por\s+capacidade|sem\s+inventar|nunca\s+inventad|"
    r"100%\s+reais?|truthful|true\s+scarcity)\b",
    re.IGNORECASE,
)


def iter_md(target_dir: str):
    for dp, dns, fns in os.walk(target_dir):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if fn.endswith(".md"):
                yield os.path.join(dp, fn)


def strip_noise(text: str) -> str:
    text = FM_RE.sub("", text, count=1)
    text = FENCE_RE.sub("\n", text)
    return text


def scan_file(path: str) -> dict:
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    text = strip_noise(open(path, encoding="utf-8").read())
    unproven, scarcity = [], []
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith(("#", "|", ">", "<!--")):
            # tabelas, headings, citações em bloco e comentários: fora do escopo de copy
            continue
        if NUMERIC_CLAIM_RE.search(s) and not PROOF_NEARBY_RE.search(s):
            unproven.append({"line": i, "text": s[:90]})
        if SCARCITY_RE.search(s) and not TRUTH_QUALIFIER_RE.search(s):
            scarcity.append({"line": i, "text": s[:90]})
    flags = len(unproven) + len(scarcity)
    return {"rel": rel, "flags": flags, "unproven_claims": unproven, "scarcity": scarcity}


def main():
    ap = argparse.ArgumentParser(description="Heurística: claims sem prova + escassez suspeita.")
    ap.add_argument("--dir", default=".", help="subdiretório (default: repo)")
    ap.add_argument("--strict", action="store_true", help="qualquer flag => exit 1")
    ap.add_argument("--check", action="store_true", help="dry-run read-only (não escreve json)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    target = os.path.normpath(os.path.join(ROOT, a.dir))
    if not os.path.isdir(target):
        print(f"ERRO: diretório inexistente: {a.dir}"); sys.exit(2)

    results = [scan_file(p) for p in sorted(iter_md(target))]
    flagged = [r for r in results if r["flags"]]
    total_claims = sum(len(r["unproven_claims"]) for r in results)
    total_scarcity = sum(len(r["scarcity"]) for r in results)

    label = f" — {a.dir}" if a.dir != "." else ""
    print(f"\n=== COMPLIANCE-SCANNER{label} (heurístico) ===")
    print(f"arquivos: {len(results)} · arquivos sinalizados: {len(flagged)}")
    print(f"claims sem prova (suspeitos): {total_claims} · escassez/urgência suspeita: {total_scarcity}")
    if not a.quiet:
        for r in flagged[:60]:
            print(f"  ⚠ {r['rel']} — claims:{len(r['unproven_claims'])} escassez:{len(r['scarcity'])}")
            for c in r["unproven_claims"][:2]:
                print(f"      claim   L{c['line']}: {c['text']}")
            for c in r["scarcity"][:2]:
                print(f"      escassez L{c['line']}: {c['text']}")
        if len(flagged) > 60:
            print(f"  … (+{len(flagged) - 60} arquivo(s) sinalizado(s))")

    if not a.check:
        json.dump({"dir": a.dir, "files": len(results), "flagged": len(flagged),
                   "total_unproven": total_claims, "total_scarcity": total_scarcity,
                   "results": flagged},
                  open(os.path.join(ROOT, ".compliance-report.json"), "w"),
                  ensure_ascii=False, indent=1)

    # Informativo por padrão; --strict transforma flags em falha.
    ok = (not a.strict) or (len(flagged) == 0)
    verdict = "OK ✅" if not flagged else ("REVISAR ⚠ (informativo)" if not a.strict else "FALHA ❌")
    print(f"\nRESULTADO: {verdict} · {len(flagged)} arquivo(s) sinalizado(s)\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
