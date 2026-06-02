---
id: archive.losing-controls.autopsy-orphan-bonus-stack
title: "Autópsia — offer stack inchado com bônus órfãos"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
registries: [data.registry.control-registry, data.registry.lessons-learned-registry, data.registry.offer-registry]
tags: [autopsy, losing-control, value-equation, offer-stack, sales-page]
---

# Autópsia — stack de 9 bônus "R$ 12k" (órfãos)

- **control_id:** offer-stack-bonus-padding-v1
- **asset_type:** sales-page
- **Perdeu para:** offer-stack-lean-levers-v2
- **Métrica:** conversion — 2,0% vs 3,1% (+ reembolso e valor percebido pior)
- **Lançamento:** consultoria-y-2026-q1 (representativo)

## Hipótese
Empilhar **9 bônus** somando "R$ 12.000 em valor" aumentaria o valor percebido e a conversão — quanto mais bônus, melhor.

## O que falhou
A maioria dos bônus era **órfã**: não movia **nenhuma alavanca** da [Value Equation](../../frameworks/value-equation.md) (Sonho × Probabilidade ÷ Tempo × Esforço). O stack inchado **diluiu o foco**, aumentou a carga cognitiva e cheirou a "encheção" → desconfiança. Viola `value_equation_test` — reprovação do [`value-equation-engineer`](../../agents/value-equation-engineer.md) no [`value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md). O vencedor cortou para **3 bônus**, cada um movendo uma alavanca (probabilidade↑, tempo↓).

## Evidência
| Sinal | Perdedor | Vencedor | Delta |
|---|---|---|---|
| conversion | 2,0% | 3,1% | −1,1 p.p. |
| valor percebido (survey 1-7) | 4,1 | 5,8 | −1,7 |
| taxa de reembolso | 7% | 4% | +3 p.p. |

## Lição
**Cada bônus move ≥1 alavanca ou sai.** Stack enxuto > stack longo. Use [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) com o filtro de alavanca antes de empilhar. → lição `ll-2026q1-no-orphan-bonus`.

## Links
- vencedor: offer-stack-lean-levers-v2 · lição: `ll-2026q1-no-orphan-bonus` · swipe: [`swipe/offers`](../../swipe/offers/index.md)
- princípio violado: `value_equation_test` · gate: [`value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md)
