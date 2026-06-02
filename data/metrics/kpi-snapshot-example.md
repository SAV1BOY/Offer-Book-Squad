---
id: data.metrics.kpi-snapshot-example
title: "KPI Snapshot (exemplo) — Mariana CLT→Tech, lançamento Q2"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [kpi, snapshot, metrics, example, live]
---

# KPI Snapshot — exemplo (Mariana CLT→Tech · período: lançamento Q2)

Instância **viva** preenchida do [`kpi-dashboard-template`](kpi-dashboard-template.md), para o caso do [walkthrough](../../docs/exemplar-project-walkthrough.md). Gerada por `scripts/kpi-snapshot.py --case mariana-clt-tech --period q2`. **Números ilustrativos** (rotulados) — num lançamento real vêm dos registries + `conversion-data/`. Alimenta o [scorecard](../scorecards/example-launch-scorecard.md) e o `readiness-check`.

| Família | KPI | Valor (ilustrativo) | Meta | vs Meta | Fonte |
|---|---|---|---|---|---|
| offer_quality | value_equation_score | 4.4 / 5 | ≥ 4 | ✅ | offer-registry |
| offer_quality | money_model_completeness | 4 / 4 partes | ≥ 2 (alvo 4) | ✅ | offer-registry |
| offer_quality | proof_coverage_rate | 100% | 100% | ✅ | claim+proof-registry |
| offer_quality | big_idea_strength | 4.6 / 5 | ≥ 4 | ✅ | big-idea-registry |
| conversion | opt_in_rate | 38% | ≥ 30% | ✅ | conversion-data |
| conversion | vsl_conversion_rate | 4.1% | ≥ 3% | ✅ | conversion-data |
| conversion | upsell_take_rate | 22% | ≥ 15% | ✅ | conversion-data |
| conversion | aov | R$ 2.480 | ≥ R$ 2.000 | ✅ | offer-registry |
| conversion | cart_close_lift | +31% | ≥ +20% | ✅ | conversion-data |
| economics | cac | R$ 540 | ≤ R$ 700 | ✅ | conversion-data |
| economics | ltv_cac_ratio | 4.2 : 1 | ≥ 3 : 1 | ✅ | conversion-data |
| economics | payback_period | 26 dias | ≤ 30 dias | ✅ | conversion-data |
| economics | front_end_cac_liquidation | 118% | ≥ 100% | ✅ | price-test-registry |
| efficiency | time_to_offer_book | 6 dias | — | — | decision-registry |
| efficiency | time_to_blackbook | 11 dias | — | — | decision-registry |
| efficiency | copy_throughput | 7 peças/dia | — | — | control-registry |
| operational | registry_currency | 100% atualizados | 100% | ✅ | (auditoria) |
| operational | swipe_reuse_rate | 41% | ≥ 30% | ✅ | swipe-registry |
| operational | compliance_pass_rate | 100% | 100% | ✅ | claim-registry |
| operational | lessons_learned_frequency | 5 lições | ≥ 3 | ✅ | lessons-learned-registry |

**Leitura:** 17/20 KPIs com meta batem; 3 de eficiência são informativos (sem meta fixa). `front_end_cac_liquidation 118%` → a oferta de atração financia +1 cliente em <30 dias (espinha do money model saudável). → vira [scorecard](../scorecards/example-launch-scorecard.md) e entra no [backlog Kaizen](../backlog/improvement-backlog.md) se algo < meta.
