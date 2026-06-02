---
id: data.scorecards.example-launch-scorecard
title: "Launch Scorecard (exemplo) — Mariana CLT→Tech"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [scorecard, quality, launch, example, go-no-go]
---

# Launch Scorecard — exemplo (Mariana CLT→Tech)

Instância **viva** preenchida do [`launch-scorecard-template`](launch-scorecard-template.md), ligada ao [KPI snapshot](../metrics/kpi-snapshot-example.md). Lido por `python scripts/readiness-check.py --milestone ship --scorecard data/scorecards/example-launch-scorecard.md`. Regra: **GOLD ≥ 95, SOTA ≥ 98**; qualquer dimensão `< gold` → rework antes do go.

| Dimensão | Score | Gate | Evidência | Verdict |
|---|---|---|---|---|
| Offer quality (value equation) | 95 | value-no-orphan-lever-gate | KPI value_equation_score 4.4/5 | GOLD |
| Money model (espinha) | 96 | money-model-four-parts-gate | 4 partes; CAC liquidation 118% | GOLD |
| Proof & compliance | 100 | compliance-claim-backing-gate | 100% claims com prova; escassez real | SOTA |
| Big idea & positioning | 96 | big-idea-single-gate | big_idea_strength 4.6/5; UMA tese | GOLD |
| Copy & conversion | 95 | vsl-value-before-price-gate | vsl_conversion 4.1%; voz aprovada | GOLD |
| Funnel / tech / ops | 95 | funnel-no-dead-end-gate | sem becos; load test ok; run-of-show | GOLD |

**Overall: 96 / 100 — GOLD.** Verdict: **GO** para ship (todas as dimensões ≥ gold; HARD STOPs verdes). Lições → [backlog Kaizen](../backlog/improvement-backlog.md); KPIs → [snapshot](../metrics/kpi-snapshot-example.md).
