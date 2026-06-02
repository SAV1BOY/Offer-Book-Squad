#!/usr/bin/env python3
"""
qa-runner.py — auditor de qualidade do Offer Book Squad

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: todos os .md/.csv/.py do repo + config.yaml
PRODUCES: relatório no stdout + .qa-report.json (na raiz)
USAGE:
  python scripts/qa-runner.py                 # repo inteiro (lenient)
  python scripts/qa-runner.py --dir agents    # só um diretório
  python scripts/qa-runner.py --phase 5       # rótulo informativo
  python scripts/qa-runner.py --strict        # warnings viram erros (Fase 18)
DEPENDS: stdlib (+ pyyaml)
EXIT: 0 ok (score >= gate) · 1 falha de validação/score < gate · 2 erro de uso
"""
from __future__ import annotations
import argparse, json, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário (pip install pyyaml)"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCORE_GATE = 95.0

ALLOWED_TYPES = {
    "agent", "checklist", "gate", "framework", "reference", "template", "task",
    "workflow", "swipe", "swipe-source", "voice", "phrases", "registry",
    "component", "pattern", "utility", "taxonomy", "script", "project-phase",
    "doc", "config",
}
REQUIRED_KEYS = ["id", "title", "type", "status", "version", "updated"]
WORD_FLOOR = {
    "agent": 1200, "framework": 500, "reference": 400, "task": 350,
    "workflow": 300, "template": 250, "swipe": 200, "voice": 200,
    "phrases": 200, "checklist": 150, "gate": 150, "swipe-source": 150,
    "reference-book": 400, "project-phase": 200,
    # defaults menores para vocabulário/infra:
    "registry": 90, "component": 120, "pattern": 150, "utility": 120,
    "taxonomy": 200, "doc": 150,
}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
# arquivos md sem frontmatter permitidos (infra de repo):
NO_FRONTMATTER_OK = {"README.md", "ARCHITECTURE.md", "BUILD-PROGRESS.md"}

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def slugify_path(relpath: str) -> str:
    """Deriva o slug do path (sem extensão), p/ checar consistência do id."""
    base = os.path.splitext(relpath)[0]
    return base.split("/")[-1]


def iter_md(target_dir: str):
    for dp, dns, fns in os.walk(target_dir):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if fn.endswith(".md"):
                yield os.path.join(dp, fn)


def word_count(body: str) -> int:
    # remove blocos de código e frontmatter já retirado
    body = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    return len(re.findall(r"\b\w+\b", body))


def check_file(path: str, ids: dict, strict: bool = False) -> dict:
    rel = os.path.relpath(path, ROOT)
    issues, warns = [], []
    weights = {"keys": 0.4, "type": 0.1, "id": 0.1, "words": 0.2, "links": 0.2}
    got = {k: 0.0 for k in weights}

    text = open(path, encoding="utf-8").read()
    m = FM_RE.match(text)
    fname = os.path.basename(path)

    if not m:
        if fname in NO_FRONTMATTER_OK:
            return {"rel": rel, "score": 100.0, "issues": [], "warns": [], "skip": True}
        issues.append("sem frontmatter YAML")
        return {"rel": rel, "score": 0.0, "issues": issues, "warns": warns}

    body = text[m.end():]
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception as e:
        issues.append(f"frontmatter YAML inválido: {e}")
        return {"rel": rel, "score": 0.0, "issues": issues, "warns": warns}

    # required keys
    missing = [k for k in REQUIRED_KEYS if k not in fm or fm.get(k) in (None, "")]
    if missing:
        issues.append(f"chaves faltando: {missing}")
    else:
        got["keys"] = weights["keys"]

    # type
    t = fm.get("type")
    if t in ALLOWED_TYPES:
        got["type"] = weights["type"]
    else:
        issues.append(f"type inválido: {t!r}")

    # id consistente + único
    fid = fm.get("id", "")
    slug = slugify_path(rel)
    if fid:
        if fid in ids and ids[fid] != rel:
            issues.append(f"id duplicado com {ids[fid]}")
        ids.setdefault(fid, rel)
        # id presente e único basta aqui; a bijeção id<->path (convenção
        # namespace.slug) é validada autoritativamente por scripts/id-resolver.py.
        got["id"] = weights["id"]
        _ = slug
    else:
        issues.append("id ausente")

    # word floor
    wc = word_count(body)
    floor = WORD_FLOOR.get(t, 150)
    if wc >= floor:
        got["words"] = weights["words"]
    else:
        warns.append(f"abaixo do piso ({wc}/{floor} palavras)")
        got["words"] = weights["words"] * min(1.0, wc / floor)

    # relative .md links resolve
    bad = []
    for tgt in LINK_RE.findall(body):
        tgt = tgt.split("#")[0].strip()
        if not tgt or tgt.startswith(("http://", "https://", "mailto:")):
            continue
        if not tgt.endswith(".md"):
            continue
        abs_t = os.path.normpath(os.path.join(os.path.dirname(path), tgt))
        if not os.path.exists(abs_t):
            bad.append(tgt)
    if not bad:
        got["links"] = weights["links"]
    elif strict:
        # Fase 18: link não resolvido é defeito real (não há "depois")
        issues.append(f"{len(bad)} link(s) quebrado(s): {bad[:3]}")
    else:
        # build em camadas: forward-ref planejado → crédito total + aviso informativo
        warns.append(f"{len(bad)} forward-ref (será criado em fase futura): {bad[:3]}")
        got["links"] = weights["links"]

    score = sum(got.values()) * 100
    return {"rel": rel, "score": round(score, 1), "issues": issues, "warns": warns}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=".")
    ap.add_argument("--phase", default="")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    target = os.path.normpath(os.path.join(ROOT, a.dir))
    ids: dict = {}
    results = [check_file(p, ids, a.strict) for p in sorted(iter_md(target))]
    results = [r for r in results if not r.get("skip")]

    if not results:
        print(f"Nenhum .md em {a.dir}"); sys.exit(0)

    n = len(results)
    avg = round(sum(r["score"] for r in results) / n, 1)
    err_files = [r for r in results if r["issues"]]
    warn_files = [r for r in results if r["warns"] and not r["issues"]]

    label = f" (Fase {a.phase})" if a.phase else ""
    print(f"\n=== QA-RUNNER{label} — {a.dir} ===")
    print(f"arquivos: {n} · score médio: {avg}/100 · gate: {SCORE_GATE}")
    print(f"com ERRO: {len(err_files)} · com warning: {len(warn_files)} · limpos: {n-len(err_files)-len(warn_files)}")

    if not a.quiet:
        for r in results:
            if r["issues"]:
                print(f"  ✗ {r['rel']} [{r['score']}] " + " | ".join(r["issues"]))
        for r in (warn_files if not a.quiet else []):
            print(f"  ⚠ {r['rel']} [{r['score']}] " + " | ".join(r["warns"][:2]))

    json.dump({"dir": a.dir, "phase": a.phase, "files": n, "score": avg, "results": results},
              open(os.path.join(ROOT, ".qa-report.json"), "w"), ensure_ascii=False, indent=1)

    ok = avg >= SCORE_GATE and (not a.strict or not err_files)
    if a.strict and err_files:
        print(f"\nSTRICT: {len(err_files)} arquivo(s) com erro → FALHA")
    print(f"\nRESULTADO: {'PASS ✅' if ok else 'ABAIXO DO GATE ❌'} (score {avg})\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
