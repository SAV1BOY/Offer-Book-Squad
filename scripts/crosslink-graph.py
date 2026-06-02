#!/usr/bin/env python3
"""
crosslink-graph.py — grafo de cross-links relativos; links quebrados + órfãos

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: todos os .md do repo (links markdown relativos em prosa)
PRODUCES: relatório no stdout + .crosslink-graph.json (na raiz; em .gitignore)
USAGE:
  python scripts/crosslink-graph.py            # repo inteiro
  python scripts/crosslink-graph.py --dir frameworks
  python scripts/crosslink-graph.py --check    # dry-run read-only (não escreve json)
DEPENDS: stdlib
EXIT: 0 sem links quebrados · 1 há link(s) quebrado(s) · 2 erro de uso
"""
from __future__ import annotations
import argparse, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env", "fixtures"}
# .md "raiz/entrada" que não precisam ser apontados por ninguém (não contam como órfãos):
ENTRYPOINTS = {"README.md", "ARCHITECTURE.md", "BUILD-PROGRESS.md"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")


def iter_md(target_dir: str):
    for dp, dns, fns in os.walk(target_dir):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if fn.endswith(".md"):
                yield os.path.join(dp, fn)


def extract_links(path: str):
    """Retorna alvos .md relativos (sem âncora) citados no corpo (fora de blocos de código)."""
    text = open(path, encoding="utf-8").read()
    text = FENCE_RE.sub(" ", text)
    text = INLINE_CODE_RE.sub(" ", text)
    out = []
    for tgt in LINK_RE.findall(text):
        tgt = tgt.split("#")[0].strip()
        if not tgt or tgt.startswith(("http://", "https://", "mailto:", "tel:")):
            continue
        if not tgt.endswith(".md"):
            continue
        out.append(tgt)
    return out


def main():
    ap = argparse.ArgumentParser(description="Grafo de cross-links relativos: quebrados + órfãos.")
    ap.add_argument("--dir", default=".", help="subdiretório a analisar (default: repo)")
    ap.add_argument("--check", action="store_true", help="dry-run read-only (não escreve json)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    target = os.path.normpath(os.path.join(ROOT, a.dir))
    if not os.path.isdir(target):
        print(f"ERRO: diretório inexistente: {a.dir}"); sys.exit(2)

    all_files = sorted(iter_md(target))
    rels = {os.path.relpath(p, ROOT).replace(os.sep, "/") for p in all_files}

    edges = {}            # rel -> [rel alvo resolvido]
    broken = []           # (origem, alvo bruto)
    incoming = {r: 0 for r in rels}

    for p in all_files:
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        edges[rel] = []
        for raw in extract_links(p):
            abs_t = os.path.normpath(os.path.join(os.path.dirname(p), raw))
            rel_t = os.path.relpath(abs_t, ROOT).replace(os.sep, "/")
            if os.path.exists(abs_t):
                edges[rel].append(rel_t)
                if rel_t in incoming:
                    incoming[rel_t] += 1
            else:
                broken.append((rel, raw))

    # órfãos: nenhum link de entrada, não é entrypoint, não é index de pasta.
    orphans = []
    for r in sorted(rels):
        base = os.path.basename(r)
        if base in ENTRYPOINTS or base == "index.md":
            continue
        if incoming.get(r, 0) == 0:
            orphans.append(r)

    n = len(rels)
    total_edges = sum(len(v) for v in edges.values())

    label = f" — {a.dir}" if a.dir != "." else ""
    print(f"\n=== CROSSLINK-GRAPH{label} ===")
    print(f"arquivos: {n} · links resolvidos: {total_edges} · quebrados: {len(broken)} · órfãos: {len(orphans)}")
    if not a.quiet:
        for src, tgt in broken[:50]:
            print(f"  ✗ QUEBRADO  {src} -> {tgt}")
        if len(broken) > 50:
            print(f"  … (+{len(broken) - 50} link(s) quebrado(s))")
        for r in orphans[:50]:
            print(f"  ⚠ ÓRFÃO     {r}")
        if len(orphans) > 50:
            print(f"  … (+{len(orphans) - 50} órfão(s))")

    if not a.check:
        json.dump({"dir": a.dir, "files": n, "edges": total_edges,
                   "broken": [{"from": s, "to": t} for s, t in broken],
                   "orphans": orphans, "graph": edges},
                  open(os.path.join(ROOT, ".crosslink-graph.json"), "w"),
                  ensure_ascii=False, indent=1)

    ok = not broken
    note = "" if ok else f" ({len(broken)} quebrado(s))"
    print(f"\nRESULTADO: {'GRAFO OK ✅' if ok else 'LINKS QUEBRADOS ❌'}{note}"
          f" · órfãos (informativo): {len(orphans)}\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
