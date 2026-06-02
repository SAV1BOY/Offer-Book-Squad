#!/usr/bin/env python3
"""
readiness-check.py — avalia go/no-go de um marco contra score_thresholds + readiness_rules

PART OF: Offer Book Squad / scripts
OWNER_AGENT: offerbook-chief
CONSUMES: config.yaml (score_thresholds, readiness_rules) + .qa-report.json (score estrutural) + scorecard vivo (opcional)
PRODUCES: veredito go/no-go no stdout
USAGE:
  python scripts/readiness-check.py --milestone offer_book_ready
  python scripts/readiness-check.py --milestone ship --scorecard data/scorecards/example-launch-scorecard.md
  python scripts/readiness-check.py --milestone blackbook_ready --check
DEPENDS: stdlib (+ pyyaml)
EXIT: 0 GO · 1 NO-GO / gate ausente · 2 uso
"""
from __future__ import annotations
import argparse, json, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MILESTONES = ["offer_book_ready", "blackbook_ready", "ship"]


def gate_path(slug: str) -> str:
    # slug ex.: offer-book-stack/offer-book-dod-gate -> checklists/<slug>.md
    return os.path.join(ROOT, "checklists", slug + ".md")


def parse_scorecard(path: str):
    """Extrai (dimensão, score) da tabela do scorecard; ignora header/separador."""
    rows = []
    for line in open(path, encoding="utf-8"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 2:
            continue
        if cells[0].lower() in ("dimensão", "dimensao") or set(cells[1]) <= set("-: "):
            continue
        m = re.search(r"\d+", cells[1])
        if m:
            rows.append((cells[0], int(m.group())))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--milestone", choices=MILESTONES, required=True)
    ap.add_argument("--scorecard", default=None, help="caminho do scorecard vivo (data/scorecards/...)")
    ap.add_argument("--check", action="store_true", help="dry-run (não falha exit)")
    a = ap.parse_args()

    cfg = yaml.safe_load(open(os.path.join(ROOT, "config.yaml"), encoding="utf-8"))
    thr = cfg.get("score_thresholds", {})
    gold = thr.get("gold", 95)
    rules = cfg.get("readiness_rules", {}).get(a.milestone, {})

    # score estrutural (do último qa-runner)
    score = None
    qa = os.path.join(ROOT, ".qa-report.json")
    if os.path.exists(qa):
        score = json.load(open(qa)).get("score")

    print(f"\n=== READINESS — {a.milestone} (gold={gold}) ===")
    problems = []

    # 1) gates requeridos existem em disco?
    req = rules.get("requires", []) + ([rules["gate"]] if rules.get("gate") else [])
    for slug in req:
        if isinstance(slug, str) and "/" in slug:
            ok = os.path.exists(gate_path(slug))
            print(f"  {'✓' if ok else '✗'} gate {slug}")
            if not ok:
                problems.append(f"gate ausente: {slug}")
        else:
            print(f"  • critério editorial: {slug} (verificar no checklist/compliance)")

    # 2) score estrutural >= gold?
    if score is None:
        print("  ⚠ sem .qa-report.json — rode `python scripts/qa-runner.py` antes")
        problems.append("score estrutural desconhecido")
    else:
        ok = score >= gold
        print(f"  {'✓' if ok else '✗'} score estrutural {score} >= gold {gold}")
        if not ok:
            problems.append(f"score {score} < gold {gold} -> rework")

    # 3) scorecard vivo (editorial) >= gold por dimensão + overall?
    if a.scorecard:
        sc = a.scorecard if os.path.isabs(a.scorecard) else os.path.join(ROOT, a.scorecard)
        if not os.path.exists(sc):
            print(f"  ✗ scorecard inexistente: {a.scorecard}"); problems.append("scorecard ausente")
        else:
            dims = parse_scorecard(sc)
            if not dims:
                print("  ⚠ scorecard sem scores parseáveis"); problems.append("scorecard ilegível")
            else:
                overall = round(sum(s for _, s in dims) / len(dims), 1)
                below = [(d, s) for d, s in dims if s < gold]
                print(f"  {'✓' if overall >= gold and not below else '✗'} scorecard overall {overall} >= gold {gold} ({len(dims)} dimensões)")
                for d, s in below:
                    print(f"    ✗ dimensão < gold: {d} = {s}")
                if overall < gold:
                    problems.append(f"scorecard overall {overall} < gold {gold}")
                if below:
                    problems.append(f"{len(below)} dimensão(ões) < gold")

    no_override = rules.get("no_override")
    if no_override:
        print(f"  ! sem override para: {no_override} (veto terminal do compliance-auditor)")

    go = not problems
    print(f"\nVEREDITO: {'GO ✅' if go else 'NO-GO ❌ — ' + '; '.join(problems)}")
    print("(gates editoriais N4-N5 exigem revisão humana nos checklists; este script cobre N1-N3 + score.)\n")
    sys.exit(0 if (go or a.check) else 1)


if __name__ == "__main__":
    main()
