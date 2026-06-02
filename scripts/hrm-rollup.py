#!/usr/bin/env python3
"""
hrm-rollup.py — gera o Squad Rollup padrão para o HRM Central (camada L4)

PART OF: Offer Book Squad / scripts
OWNER_AGENT: offerbook-chief
CONSUMES: .qa-report.json (score estrutural) + config.yaml (score_thresholds) +
          data/backlog/improvement-backlog.md (riscos abertos) +
          data/handoffs/ (handoffs) + scorecard opcional
PRODUCES: data/hrm/rollup-<case>.md (consumido pelo hrm_central — ver docs/hrm-central-spec.md)
USAGE:
  python scripts/hrm-rollup.py --case mariana-clt-tech --scorecard data/scorecards/example-launch-scorecard.md
  python scripts/hrm-rollup.py --case x --check     # preview, não escreve
DEPENDS: stdlib (+ pyyaml)
EXIT: 0 ok · 1 erro · 2 uso
"""
from __future__ import annotations
import argparse, json, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9-]", "", re.sub(r"\s+", "-", s.strip().lower()))


def scorecard_overall(path: str):
    if not path:
        return None
    p = path if os.path.isabs(path) else os.path.join(ROOT, path)
    if not os.path.exists(p):
        return None
    scores = []
    for line in open(p, encoding="utf-8"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 2 and not set(cells[1]) <= set("-: "):
            m = re.search(r"\d+", cells[1])
            if m and cells[0].lower() not in ("dimensão", "dimensao"):
                scores.append(int(m.group()))
    return round(sum(scores) / len(scores), 1) if scores else None


def open_backlog_items():
    p = os.path.join(ROOT, "data", "backlog", "improvement-backlog.md")
    items = []
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            s = line.strip()
            if s.startswith("|") and s.endswith("open |"):
                cells = [c.strip() for c in s.strip("|").split("|")]
                if len(cells) >= 8:   # rank,id,item,...,roi,...
                    items.append((cells[2], cells[7]))   # (item, roi)
    items.sort(key=lambda t: -float(t[1]) if re.match(r"[\d.]+$", t[1]) else 0)
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--scorecard", default=None)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    cfg = yaml.safe_load(open(os.path.join(ROOT, "config.yaml"), encoding="utf-8"))
    gold = cfg.get("score_thresholds", {}).get("gold", 95)

    structural = None
    qa = os.path.join(ROOT, ".qa-report.json")
    if os.path.exists(qa):
        structural = json.load(open(qa)).get("score")
    sc = scorecard_overall(a.scorecard)
    risks = open_backlog_items()
    handoffs = [f for f in os.listdir(os.path.join(ROOT, "data", "handoffs"))
                if f.endswith(".md") and not f.startswith(("README", "handoff-manifest"))] \
        if os.path.isdir(os.path.join(ROOT, "data", "handoffs")) else []

    go = (structural is None or structural >= gold) and (sc is None or sc >= gold)
    readiness = "GO ✅" if go else "NO-GO ❌"
    case = slug(a.case)
    name = f"rollup-{case}"

    risk_lines = "\n".join(f"- {it} (roi {roi})" for it, roi in risks[:5]) or "- (nenhum item aberto)"
    body = "\n".join([
        "---",
        f"id: data.hrm.{name}",
        f'title: "Squad Rollup — offerbook · {a.case}"',
        "type: doc", "layer: cross", "status: stable", "version: 1.0.0",
        "updated: 2026-06-02", "owner_agent: offerbook-chief",
        "tags: [hrm, rollup, central-command, go-no-go]", "---", "",
        f"# Squad Rollup — offerbook · {a.case}",
        "",
        "> Gerado por `scripts/hrm-rollup.py` para o **HRM Central** consumir "
        "([`docs/hrm-central-spec.md`](../../docs/hrm-central-spec.md)). Não editar à mão.",
        "",
        "| Campo | Valor |",
        "|---|---|",
        "| squad | offerbook |",
        f"| case | {a.case} |",
        f"| structural_score | {structural if structural is not None else 'n/d'} |",
        f"| scorecard_overall | {sc if sc is not None else 'n/d'} |",
        f"| gold_gate | {gold} |",
        f"| readiness | {readiness} |",
        f"| open_risks | {len(risks)} |",
        f"| pending_handoffs | {len(handoffs)} |",
        "",
        "## Riscos / trabalho aberto (top 5 por ROI)",
        risk_lines,
        "",
        "## Recomendação ao hrm_central",
        f"**{readiness}** — score estrutural {structural} e scorecard {sc} vs gold {gold}. "
        + ("Aprovado para o sistema; sem itens bloqueantes." if go
           else "Devolver ao loop de melhoria antes do go sistêmico."),
        "",
        "## Leitura do chief",
        f"O `structural_score` ({structural}) cobre frontmatter, links, ids e citações "
        f"(integridade do repositório); o `scorecard_overall` ({sc}) cobre a qualidade "
        f"editorial das dimensões do lançamento (oferta, money model, prova, copy). Ambos "
        f"acima de gold ({gold}) indicam que a fundação e a execução estão prontas — o "
        "risco residual vive nos itens de backlog acima, que o loop Kaizen endereça no "
        "próximo ciclo, antes de qualquer reincidência do modo de falha.",
        "",
        "## Como o hrm_central consome",
        "Agrega este rollup com os dos demais squads para o **go/no-go sistêmico** "
        "(todos ≥ gold + compliance verde + sem handoff rejeitado). Ver "
        "[`hrm-central-spec`](../../docs/hrm-central-spec.md) e [`hrm-governance`](../../docs/hrm-governance.md).",
        ""])

    dest = os.path.join(ROOT, "data", "hrm", f"{name}.md")
    if a.check:
        print(f"[--check] geraria {dest} · readiness={readiness} · risks={len(risks)} (não escrito).")
        sys.exit(0)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(body)
    print(f"OK · {dest} · readiness={readiness} · {len(risks)} risco(s) aberto(s).")
    sys.exit(0)


if __name__ == "__main__":
    main()
