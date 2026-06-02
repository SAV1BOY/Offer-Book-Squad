---
id: doc.hrm-central-spec
title: "Especificação do HRM Central Command (interface executável)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [reference-intellectual/hrm-hierarchical-reasoning]
tags: [hrm, central-command, multi-squad, rollup, go-no-go, interface]
---

# Especificação do HRM Central Command (`hrm_central`)

A camada **L4** de [`hrm-governance`](hrm-governance.md). Este repo é **single-squad** — o `hrm_central` ainda não existe como squad. Esta spec define a **interface executável** para que o Offer Book Squad já seja **hrm_central-ready**: ele emite um **rollup padrão** que o comando central consumiria, sem depender dos outros 11 squads existirem.

## O que o `hrm_central` recebe de cada chief
Um **Squad Rollup** padronizado (gerado por [`scripts/hrm-rollup.py`](../scripts/hrm-rollup.py) → [`data/hrm/`](../data/hrm/README.md)):
| Campo | Significado |
|---|---|
| `squad` | id do squad (ex.: offerbook) |
| `case` | lançamento/engajamento |
| `structural_score` | qa-runner --strict (0–100) |
| `scorecard_overall` | scorecard editorial do lançamento (0–100) |
| `readiness` | GO / NO-GO (vs `score_thresholds.gold`) |
| `open_risks` | itens `open` de maior ROI no [backlog](../data/backlog/improvement-backlog.md) |
| `pending_handoffs` | handoffs em aberto ([`data/handoffs/`](../data/handoffs/README.md)) |
| `recommendation` | recomendação do chief ao comando central |

## Protocolo Go/No-Go sistêmico
1. Cada chief emite seu rollup. **Go sistêmico** exige: todos os squads contribuintes ≥ `gold` **e** compliance verde **e** nenhum handoff cross-squad rejeitado pendente.
2. Se um squad está NO-GO → o `hrm_central` devolve **só aquele squad** ao loop de melhoria (não trava o sistema todo desnecessariamente).
3. Claim falso / escassez falsa em qualquer squad → **veto terminal** (sem override), conforme `readiness_rules.ship.no_override`.

## Resolução de conflito entre squads
Quando o `cross-squad-handoff-quality` (saída) de um squad diverge do `cross-squad-asset-validation` (entrada) de outro, o `hrm_central` arbitra: lê os dois rollups + o contrato ([`handoff-contract-template`](../templates/cross-squad/handoff-contract-template.md)), decide, e grava no `decision-registry` de ambos. Prioridade vem do `c_level_squad` (metas de receita).

## Scorecard de sistema
O `hrm_central` agrega os `scorecard_overall` dos squads num **scorecard de sistema** (média ponderada por criticidade do squad no lançamento). Abaixo de `gold` → loop; ≥ `sota` → referência.

## Como o Offer Book Squad pluga hoje
Roda `python scripts/hrm-rollup.py --case <id>` ao fim do D7 (junto do `memory-update`). O rollup vai para [`data/hrm/`](../data/hrm/README.md) e fica pronto para o `hrm_central` consumir assim que a multinacional de squads existir. Até lá, é a **prova de interface** — o squad fala a língua do comando central.
