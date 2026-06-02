---
id: doc.principles-enforcement-map
title: "Mapa de Enforcement dos 11 Princípios"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [principles, enforcement, gates, veto, traceability]
---

# Mapa de Enforcement dos 11 Princípios

Os 11 princípios não são decorativos — cada um tem um **dono** (agente), um **gate** que o testa e/ou um **framework** que o operacionaliza. Esta tabela é o atalho: princípio → onde ele é enforçado.

| # | Princípio | Agente campeão | Gate / Checklist | Framework | Veto? |
|---|---|---|---|---|---|
| 1 | `evidence_before_opinion` | [proof-credibility-curator](../agents/proof-credibility-curator.md) | [proof/proof-claim-backing-gate](../checklists/proof/proof-claim-backing-gate.md) | [proof-to-claim-chain](../frameworks/proof-to-claim-chain.md) | via compliance |
| 2 | `contradiction_before_conclusion` | [big-idea-architect](../agents/big-idea-architect.md) | [big-idea/big-idea-new-big-credible-gate](../checklists/big-idea/big-idea-new-big-credible-gate.md) | [big-idea-architect/big-idea-ideation-tot](../frameworks/big-idea-architect/big-idea-ideation-tot.md) | — |
| 3 | `traceability_before_eloquence` | [knowledge-librarian](../agents/knowledge-librarian.md) | [final-delivery-checklist](../checklists/final-delivery-checklist.md) | [proof-to-claim-chain](../frameworks/proof-to-claim-chain.md) | — |
| 4 | `decision_before_ornament` | [offerbook-chief](../agents/offerbook-chief.md) | [chief/chief-scope-approval-gate](../checklists/chief/chief-scope-approval-gate.md) | [power-of-one](../frameworks/power-of-one.md) | chief |
| 5 | `memory_before_repetition` | [knowledge-librarian](../agents/knowledge-librarian.md) | [final-delivery-checklist](../checklists/final-delivery-checklist.md) | — | — |
| 6 | `clarity_before_volume` | [voice-style-guardian](../agents/voice-style-guardian.md) | [voice/voice-approval-gate](../checklists/voice/voice-approval-gate.md) | — | **sim** |
| 7 | **`offer_before_persuasion`** | [offerbook-chief](../agents/offerbook-chief.md) | [offer-book-stack/offer-book-dod-gate](../checklists/offer-book-stack/offer-book-dod-gate.md) (★ HARD STOP) | [starving-crowd](../frameworks/starving-crowd.md) | **sim** |
| 8 | **`one_big_idea`** | [big-idea-architect](../agents/big-idea-architect.md) | [big-idea/big-idea-single-gate](../checklists/big-idea/big-idea-single-gate.md) | [power-of-one](../frameworks/power-of-one.md) | **sim** |
| 9 | **`truthful_scarcity`** | [compliance-auditor](../agents/compliance-auditor.md) | [compliance/compliance-scarcity-truth-gate](../checklists/compliance/compliance-scarcity-truth-gate.md) | [scarcity-urgency-engine](../frameworks/scarcity-urgency-engine.md) | **sim** |
| 10 | **`value_equation_test`** | [value-equation-engineer](../agents/value-equation-engineer.md) | [value/value-no-orphan-lever-gate](../checklists/value/value-no-orphan-lever-gate.md) | [value-equation](../frameworks/value-equation.md) | **sim** |
| 11 | **`money_model_spine`** | [money-model-designer](../agents/money-model-designer.md) | [money-model/money-model-four-parts-gate](../checklists/money-model/money-model-four-parts-gate.md) | [money-model-sequence](../frameworks/money-model-sequence.md) | **sim** |

## Os 6 agentes com poder de veto
| Agente | Camada | Bloqueia |
|---|---|---|
| [offerbook-chief](../agents/offerbook-chief.md) | D0 | copy antes do Offer Book DoD; pular gate; scope creep |
| [value-equation-engineer](../agents/value-equation-engineer.md) | D2 | componente que não move ≥1 alavanca |
| [money-model-designer](../agents/money-model-designer.md) | D2 | copy/funil/logística antes da escada existir |
| [big-idea-architect](../agents/big-idea-architect.md) | D3 | múltiplas Big Ideas (Power of One) |
| [voice-style-guardian](../agents/voice-style-guardian.md) | D4 | copy fora do padrão de voz |
| [compliance-auditor](../agents/compliance-auditor.md) | D7 | claim sem lastro; escassez falsa; garantia inexequível; violação setorial/privacidade |

## Enforcement multicamada
- **D0** segura o HARD STOP e o escopo.
- **D2** tem dois vetos (valor + money model) — fundação da oferta.
- **D3** trava UMA Big Idea.
- **D4** veta voz fora do padrão.
- **D7** é a última barreira (compliance) + memória.
- **Agregação:** `offer-book-dod-gate` reúne os gates D1–D3; `blackbook-dod-gate` reúne D4–D7 + compliance. Override só com decisão gravada no [decision-registry](../data/registries/decision-registry.md) — **exceto** claim falso e escassez falsa, que **não têm override**.
