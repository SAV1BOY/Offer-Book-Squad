---
id: data.hrm.rollup-example
title: "Squad Rollup — offerbook · example"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [hrm, rollup, central-command, go-no-go]
---

# Squad Rollup — offerbook · example

> Gerado por `scripts/hrm-rollup.py` para o **HRM Central** consumir ([`docs/hrm-central-spec.md`](../../docs/hrm-central-spec.md)). Não editar à mão.

| Campo | Valor |
|---|---|
| squad | offerbook |
| case | example |
| structural_score | 100.0 |
| scorecard_overall | 96.2 |
| gold_gate | 95 |
| readiness | GO ✅ |
| open_risks | 1 |
| pending_handoffs | 1 |

## Riscos / trabalho aberto (top 5 por ROI)
- Governança multi-squad executável (hrm_central) (roi 0.50)

## Recomendação ao hrm_central
**GO ✅** — score estrutural 100.0 e scorecard 96.2 vs gold 95. Aprovado para o sistema; sem itens bloqueantes.

## Leitura do chief
O `structural_score` (100.0) cobre frontmatter, links, ids e citações (integridade do repositório); o `scorecard_overall` (96.2) cobre a qualidade editorial das dimensões do lançamento (oferta, money model, prova, copy). Ambos acima de gold (95) indicam que a fundação e a execução estão prontas — o risco residual vive nos itens de backlog acima, que o loop Kaizen endereça no próximo ciclo, antes de qualquer reincidência do modo de falha.

## Como o hrm_central consome
Agrega este rollup com os dos demais squads para o **go/no-go sistêmico** (todos ≥ gold + compliance verde + sem handoff rejeitado). Ver [`hrm-central-spec`](../../docs/hrm-central-spec.md) e [`hrm-governance`](../../docs/hrm-governance.md).
