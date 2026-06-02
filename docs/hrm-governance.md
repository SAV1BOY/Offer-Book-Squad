---
id: doc.hrm-governance
title: "Governança HRM — Camadas, Escalonamento e Comando Central"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [hrm, governance, escalation, central-command, multi-squad, go-no-go]
---

# Governança HRM — Camadas, Escalonamento e Comando Central

Este squad opera como **setor de uma multinacional de squads** sob arquitetura **HRM multi-camadas**. Este documento define **quem decide o quê**, **quando o output sobe**, **quando volta em loop** e **como o squad se conecta ao comando central**. Regras vivem em [`config.yaml`](../config.yaml) (`escalation_rules`, `readiness_rules`, `delegation_rules`, `improvement_loop`).

## As 4 camadas
```
L4  HRM Central Command (hrm_central)   ← multi-squad: prioridade, conflito entre squads, go/no-go sistêmico
L3  Squad Chief (offerbook-chief)        ← orquestra, aprova, veta, resolve conflito interno
L2  Teams / Swarms (9 grupos funcionais) ← coordenam execução (ver team-coordination.md)
L1  Agentes (L-module)                   ← executam a task, auto-verificam, escrevem registry
```
Espelha o HRM (Sapient, arXiv 2506.21734): **H-module** (planejador lento) dirige o **L-module** (executor rápido). Aqui: L3/L4 planejam e aprovam; L1/L2 executam; o output **converge nos gates**.

## Quando o output SOBE de camada
- **L1 → L2:** o agente passa no seu gate + auto-verificação (Bloom até Avaliar) → entrega ao team lead.
- **L2 → L3:** o team passa no gate intermediário do grupo → o chief recebe para o gate de domínio/readiness.
- **L3 → L4 (sobe ao comando central):** somente quando (`escalation_rules`):
  1. risco estratégico ou task fora do escopo do squad;
  2. `score < gold` após **2 loops** de rework;
  3. conflito que cruza squads (handoff rejeitado por outro squad);
  4. decisão que muda metas de receita/prioridade (vem do `c_level_squad`).

## Quando o output VOLTA em loop (loop-to-improve)
- Gate vermelho → volta ao **agente dono** do bloco (não ao início) — ver [`failure-paths-and-gate-recovery`](failure-paths-and-gate-recovery.md).
- `score < gold` (`score_thresholds.rework_below`) → rework obrigatório.
- 2 loops sem atingir gold → escala ao chief; chief sem solução → `hrm_central`.
- **Sem volta, sem override:** claim sem lastro e escassez falsa (veto terminal do `compliance-auditor`).

## Go/No-Go (readiness)
Três marcos, cada um = gate + `min_score: gold` (`readiness_rules`):
| Marco | Exige | Gate | Decide |
|---|---|---|---|
| **offer_book_ready** | intelligence + offer-architecture + big-idea gates | [offer-book-dod-gate](../checklists/offer-book-stack/offer-book-dod-gate.md) ★ HARD STOP | offerbook-chief |
| **blackbook_ready** | copy + funnel-tech + ops + growth gates | [blackbook-dod-gate](../checklists/blackbook-stack/blackbook-dod-gate.md) | compliance-auditor + chief |
| **ship** | truthful_scarcity + claim_backing + compliance | (os dois acima verdes) | chief; **sem override** p/ claim/escassez falsa |

## Como o squad pluga na multinacional (cross-squad)
- **Upstream (entrega PARA o offer book):** [deepresearch_squad](../checklists/cross-squad/cross-squad-research-request-quality.md) (mercado/VOC), advisory_board_squad (stress-test).
- **Downstream (offer book entrega PARA):** copy_squad, traffic_squad, design_squad, brand_squad, data_squad, c_level_squad.
- Toda transição usa um **contrato** ([`templates/cross-squad/handoff-contract-template`](../templates/cross-squad/handoff-contract-template.md)), passa pelo [handoff-quality gate](../checklists/cross-squad/cross-squad-handoff-quality.md) na saída e pelo [asset-validation gate](../checklists/cross-squad/cross-squad-asset-validation.md) na entrada, e é logada em [`data/handoffs/`](../data/handoffs/README.md) + `decision-registry`.

## HRM Central Command (`hrm_central`) — o que faz
- Aprova ou devolve o output do squad para o **sistema maior** (go/no-go sistêmico).
- Resolve conflitos **entre** squads (quando o handoff-quality gate de dois squads diverge).
- Distribui prioridade/metas (recebe do `c_level_squad`) e decide se um lançamento entra na fila.
- Aciona o **Kaizen** entre squads (ver [`improvement-loop-kaizen`](improvement-loop-kaizen.md)).

> Princípio: o sistema falha **fechado** (bloqueia entrega ruim) e **aprende em loop** (memória → próximo intake). Nenhuma camada aprova sozinha algo abaixo de `gold`.
