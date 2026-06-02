#!/usr/bin/env python3
"""
backlog-prioritize.py — recalcula ROI e reordena o backlog Kaizen

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: data/backlog/improvement-backlog.md (tabela sob "## Backlog")
PRODUCES: reescreve a tabela com roi recalculado + rank por prioridade
USAGE:
  python scripts/backlog-prioritize.py            # recalcula e reescreve
  python scripts/backlog-prioritize.py --check    # só mostra o ranking (não escreve)
DEPENDS: stdlib
EXIT: 0 ok · 1 erro de parse · 2 uso
ROI = impact (1-5) * confidence (0-1) / effort (1-5)
"""
from __future__ import annotations
import argparse, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKLOG = os.path.join(ROOT, "data", "backlog", "improvement-backlog.md")
COLS = ["rank", "id", "item", "origem", "impact", "effort", "confidence", "roi", "dono", "status"]


def parse_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    if not os.path.exists(BACKLOG):
        print(f"ERRO: {BACKLOG} inexistente"); sys.exit(1)
    lines = open(BACKLOG, encoding="utf-8").read().split("\n")

    # localizar bloco de tabela (linhas contíguas começando com '|')
    tbl = [i for i, l in enumerate(lines) if l.lstrip().startswith("|")]
    if len(tbl) < 3:
        print("ERRO: tabela de backlog não encontrada"); sys.exit(1)
    start, end = tbl[0], tbl[-1]
    header, sep, data_idx = tbl[0], tbl[1], tbl[2:]

    rows = []
    for i in data_idx:
        cells = parse_row(lines[i])
        if len(cells) != len(COLS):
            print(f"ERRO: linha {i+1} com {len(cells)} colunas (esperado {len(COLS)})"); sys.exit(1)
        r = dict(zip(COLS, cells))
        try:
            imp, eff, conf = int(r["impact"]), int(r["effort"]), float(r["confidence"])
            r["_roi"] = round(imp * conf / eff, 2) if eff else 0.0
        except ValueError:
            print(f"ERRO: impact/effort/confidence inválidos na linha {i+1}"); sys.exit(1)
        rows.append(r)

    # ordenar por roi desc (estável)
    rows.sort(key=lambda r: r["_roi"], reverse=True)
    for rank, r in enumerate(rows, 1):
        r["rank"], r["roi"] = str(rank), f"{r['_roi']:.2f}"

    new_tbl = [lines[header], lines[sep]]
    for r in rows:
        new_tbl.append("| " + " | ".join(r[c] for c in COLS) + " |")

    print("\n=== BACKLOG PRIORITIZADO (por ROI) ===")
    for r in rows:
        flag = "✓" if r["status"] == "done" else "•"
        print(f"  {flag} #{r['rank']:>2} roi={r['roi']:>5} [{r['status']:>4}] {r['id']} — {r['item'][:48]}")

    if a.check:
        print("\n[--check] não escrito.")
        sys.exit(0)

    out = lines[:start] + new_tbl + lines[end + 1:]
    open(BACKLOG, "w", encoding="utf-8").write("\n".join(out))
    print(f"\nOK · {BACKLOG} reordenado ({len(rows)} itens).")
    sys.exit(0)


if __name__ == "__main__":
    main()
