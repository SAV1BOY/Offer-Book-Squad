---
id: data.backlog.improvement-backlog
title: "Improvement Backlog (Kaizen) — vivo, com ROI numérico"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [backlog, kaizen, roi, prioritization, learning]
---

# Improvement Backlog (Kaizen) — vivo

Backlog **vivo** de melhorias do squad (alimenta o [loop Kaizen](../../docs/improvement-loop-kaizen.md) → próximo intake). Cada item tem **ROI numérico** = `impact (1-5) × confidence (0-1) ÷ effort (1-5)`, e é **ranqueado** por `scripts/backlog-prioritize.py` (recalcula `roi` e `rank`; não editar `roi`/`rank` à mão). Template em [`improvement-backlog-template.md`](improvement-backlog-template.md).

## Backlog
| rank | id | item | origem | impact | effort | confidence | roi | dono | status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | bk-05 | ROI numérico no backlog Kaizen | audit §11 | 3 | 1 | 0.95 | 2.85 | knowledge-librarian | done |
| 2 | bk-01 | Hook pre-commit (qa-strict + regenerar matrizes) | audit §11 | 4 | 2 | 0.9 | 1.80 | knowledge-librarian | done |
| 3 | bk-02 | readiness-check com scorecard vivo | audit §11 | 3 | 2 | 0.9 | 1.35 | offerbook-chief | done |
| 4 | bk-06 | Autópsia real em archive/losing-controls | audit §10 | 3 | 2 | 0.8 | 1.20 | knowledge-librarian | done |
| 5 | bk-10 | compliance-scanner --strict no CI | audit §11 | 3 | 2 | 0.8 | 1.20 | compliance-auditor | done |
| 6 | bk-03 | 1º handoff executável com deepresearch | audit §11 | 5 | 3 | 0.7 | 1.17 | offer-squad-architect | done |
| 7 | bk-04 | KPI snapshots vivos por lançamento | audit §11 | 4 | 3 | 0.8 | 1.07 | knowledge-librarian | done |
| 8 | bk-07 | Fixtures de cenário de falha (gate/veto) | audit §11 | 3 | 3 | 0.7 | 0.70 | offerbook-chief | done |
| 9 | bk-08 | Variante B2B do offer-book-master + battle cards | audit §11 | 4 | 4 | 0.6 | 0.60 | offer-squad-architect | done |
| 10 | bk-09 | Governança multi-squad executável (hrm_central) | audit §11 | 5 | 5 | 0.5 | 0.50 | offerbook-chief | done |

## Como usar
1. Adicione um item com `impact`, `effort`, `confidence` (deixe `roi` e `rank` em branco ou `0`).
2. Rode `python scripts/backlog-prioritize.py` → recalcula `roi` e reordena por prioridade.
3. O [offerbook-chief](../../agents/offerbook-chief.md) promove os itens do topo `open` para o próximo ciclo ([intake-and-scope](../../tasks/planning/intake-and-scope.md)); melhorias que cruzam squads sobem ao `hrm_central`.

## Definição de ROI
`roi = impact × confidence ÷ effort` (RICE simplificado). Maior = primeiro. `confidence` reflete a certeza do impacto (0–1). Itens `done` permanecem para histórico/rastreabilidade.
