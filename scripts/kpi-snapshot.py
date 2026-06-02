#!/usr/bin/env python3
"""
kpi-snapshot.py — scaffolda um KPI snapshot vivo a partir do template

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: data/metrics/kpi-dashboard-template.md + config.yaml (kpis)
PRODUCES: data/metrics/kpi-snapshot-<case>-<period>.md (a preencher com dados reais)
USAGE:
  python scripts/kpi-snapshot.py --case mariana-clt-tech --period q2
  python scripts/kpi-snapshot.py --case x --period q3 --check   # preview, não escreve
DEPENDS: stdlib (+ pyyaml)
EXIT: 0 ok · 1 erro · 2 uso
"""
from __future__ import annotations
import argparse, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9-]", "", re.sub(r"\s+", "-", s.strip().lower()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True, help="identificador do lançamento")
    ap.add_argument("--period", required=True, help="período (ex.: q2, 2026-06)")
    ap.add_argument("--check", action="store_true", help="preview, não escreve")
    a = ap.parse_args()

    cfg = yaml.safe_load(open(os.path.join(ROOT, "config.yaml"), encoding="utf-8"))
    kpis = cfg.get("kpis", {})
    case, period = slug(a.case), slug(a.period)
    name = f"kpi-snapshot-{case}-{period}"
    dest = os.path.join(ROOT, "data", "metrics", f"{name}.md")

    rows = []
    for family, ids in kpis.items():
        for k in ids:
            rows.append(f"| {family} | {k} | _(preencher)_ | _(meta)_ | — | _(registry)_ |")

    body = "\n".join([
        "---",
        f"id: data.metrics.{name}",
        f'title: "KPI Snapshot — {a.case} · {a.period}"',
        "type: doc", "layer: cross", "status: draft", "version: 1.0.0",
        "updated: 2026-06-02", "owner_agent: knowledge-librarian",
        "tags: [kpi, snapshot, metrics, live]", "---", "",
        f"# KPI Snapshot — {a.case} (período: {a.period})", "",
        "Instância viva do [`kpi-dashboard-template`](kpi-dashboard-template.md). "
        "Preencha os valores a partir dos registries + `conversion-data/`. "
        "Veja um exemplo completo em [`kpi-snapshot-example.md`](kpi-snapshot-example.md).", "",
        "| Família | KPI | Valor | Meta | vs Meta | Fonte |",
        "|---|---|---|---|---|---|",
        *rows, "",
        "> Ao fechar o snapshot, gere o [scorecard](../scorecards/launch-scorecard-template.md) "
        "e rode `python scripts/readiness-check.py --milestone ship --scorecard <scorecard>`. "
        "KPIs abaixo da meta viram item no [backlog Kaizen](../backlog/improvement-backlog.md).", ""])

    if a.check:
        print(f"[--check] geraria {dest} com {len(rows)} KPIs (não escrito).")
        sys.exit(0)
    if os.path.exists(dest):
        print(f"ERRO: {dest} já existe (não sobrescrevo)."); sys.exit(1)
    open(dest, "w", encoding="utf-8").write(body)
    print(f"OK · {dest} criado com {len(rows)} KPIs. Preencha os valores.")
    sys.exit(0)


if __name__ == "__main__":
    main()
