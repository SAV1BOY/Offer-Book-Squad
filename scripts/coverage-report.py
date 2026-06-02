#!/usr/bin/env python3
"""
coverage-report.py — contagem de arquivos por diretório vs meta do plano

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: a árvore de arquivos do repo
PRODUCES: tabela no stdout + .coverage-report.json
USAGE: python scripts/coverage-report.py [--phase N]
DEPENDS: stdlib
EXIT: 0 sempre (informativo)
"""
from __future__ import annotations
import argparse, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {".git", "__pycache__", ".venv", "venv", "node_modules"}

# Metas por diretório de topo (do plano / BUILD-PROGRESS)
TARGETS = {
    "agents": 25, "archive": 20, "authority": 22, "checklists": 120,
    "data": 55, "docs": 18, "frameworks": 95, "lib": 38, "phrases": 18,
    "projects": 55, "reference": 90, "scripts": 14, "swipe": 42,
    "swipe-sources": 4, "tasks": 55, "templates": 45, "voice": 22,
    "workflows": 20,
}
ROOT_FILES_TARGET = 8  # README, ARCHITECTURE, config.yaml, swipe.config, .gitignore, BUILD-PROGRESS, etc.


def count_files(d: str) -> int:
    total = 0
    for dp, dns, fns in os.walk(d):
        dns[:] = [x for x in dns if x not in SKIP]
        total += sum(1 for f in fns if f.endswith((".md", ".csv", ".py", ".yaml")))
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", default="")
    a = ap.parse_args()

    rows, done, target_total = [], 0, 0
    for name, tgt in sorted(TARGETS.items()):
        p = os.path.join(ROOT, name)
        actual = count_files(p) if os.path.isdir(p) else 0
        done += actual
        target_total += tgt
        pct = round(100 * actual / tgt) if tgt else 0
        flag = "✅" if actual >= tgt else ("🟨" if actual > 0 else "⬜")
        rows.append((name, actual, tgt, pct, flag))

    # root files
    root_files = sum(1 for f in os.listdir(ROOT)
                     if os.path.isfile(os.path.join(ROOT, f)) and not f.startswith("."))
    done += root_files
    target_total += ROOT_FILES_TARGET

    label = f" (Fase {a.phase})" if a.phase else ""
    print(f"\n=== COVERAGE{label} ===")
    print(f"{'dir':<16}{'tem':>5}{'meta':>6}{'%':>6}  status")
    for name, actual, tgt, pct, flag in rows:
        print(f"{name:<16}{actual:>5}{tgt:>6}{pct:>5}%  {flag}")
    print(f"{'(root files)':<16}{root_files:>5}{ROOT_FILES_TARGET:>6}")
    print("-" * 40)
    pct_total = round(100 * done / target_total)
    print(f"{'TOTAL':<16}{done:>5}{target_total:>6}{pct_total:>5}%")

    json.dump({"phase": a.phase, "total": done, "target": target_total,
               "pct": pct_total, "dirs": {r[0]: {"actual": r[1], "target": r[2]} for r in rows}},
              open(os.path.join(ROOT, ".coverage-report.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
