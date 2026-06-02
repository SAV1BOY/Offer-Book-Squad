---
id: project.offer-book-project.08-big-idea-positioning
title: "Fase 08 — Big Idea & Posicionamento"
type: project-phase
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
consumes:
  - artifact.market-brief
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - artifact.mechanism-sheet
  - artifact.value-equation-scorecard
  - artifact.money-model
  - data.registry.objection
  - data.registry.proof
produces:
  - decision.big-idea-locked
  - artifact.big-idea
  - decision.positioning-locked
  - decision.lead-type-locked
  - artifact.positioning
tags: [project-phase, big-idea, power-of-one, positioning, lead, awareness-fit, veto, d3]
---

# Fase 08 — Big Idea & Posicionamento

## Objetivo da Fase
Destilar tudo em UMA Big Idea — e apenas uma — e travar a posição competitiva e o tipo de lead que abre a copy. A Big Idea passa nos cinco critérios (nova, grande, crível, relevante, proprietária), casa com a consciência dominante e fica cravada com promessa, gancho e vilão. A posição define qual categoria a oferta ocupa e contra o que compete; o lead define a abertura, casado com a consciência. O estado-pronto é a moldura completa dentro da qual toda copy de D4 nasce — sem que nenhum agente de copy precise "escolher entre ideias". Esta fase fecha a camada D3 e entrega o último insumo do Offer Book.

## Critério de Entrada
A camada D2 fecha: a Fase 04 entrega o `artifact.mechanism-sheet` (o coração proprietário da ideia, em uma frase), a Fase 05 o `artifact.value-equation-scorecard` (o sonho, a probabilidade, a alavanca dominante), a Fase 06 o `artifact.money-model` (a espinha que a tese precisa honrar). A Fase 01 entrega o market-brief (consciência dominante, claims gastos), a Fase 02 o avatar/VOC (emoção, desejo no idioma do avatar) e os registries [`objection-registry`](../../data/registries/objection-registry.md) e [`proof-registry`](../../data/registries/proof-registry.md). Pré-condição: mecanismo nomeado e provado, value equation aprovada, money model com ≥2 partes, preço por valor. Sem mecanismo nomeado não gero ideia. Se me pressionam a travar duas teses, veto e escalono. O [`big-idea-registry`](../../data/registries/big-idea-registry.md) e o [`decision-registry`](../../data/registries/decision-registry.md) são escritos.

## Agentes & Tasks
- **Task [`generate-big-ideas`](../../tasks/big-idea/generate-big-ideas.md)** — dono [`big-idea-architect`](../../agents/big-idea-architect.md). Abre o leque de candidatas, pontua e poda até UMA. Tem poder de veto: múltiplas ideias é reprovação.
- **Task [`lock-positioning-lead`](../../tasks/big-idea/lock-positioning-lead.md)** — dono [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md). Trava a posição e o lead. Decisor vinculante.

## Passos
1. Extraia o desejo e o vilão com [`promise-hook-villain`](../../frameworks/big-idea-architect/promise-hook-villain.md): o vilão é uma causa externa que o mecanismo revela.
2. Divirja com [`big-idea-ideation-tot`](../../frameworks/big-idea-architect/big-idea-ideation-tot.md): 3 a 5 candidatas de ângulos distintos, ancoradas no mecanismo.
3. Pontue nos 5 critérios com [`big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md) e os critérios de [`big-idea-generator`](../../frameworks/big-idea-generator.md).
4. Pode para UMA: descarte qualquer candidata com critério ≤ 2; vence a maior soma; desempate por Proprietária. Comprima com [`power-of-one`](../../frameworks/power-of-one.md) e cheque o fit de consciência com [`meta-launch-principle`](../../frameworks/meta-launch-principle.md).
5. Inventarie as alternativas competitivas com [`dunford-positioning`](../../frameworks/positioning/dunford-positioning.md) e crave o atributo único.
6. Decida a categoria com [`category-design`](../../frameworks/positioning/category-design.md) e monte a fórmula de [`moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md), sem campo vazio.
7. Selecione o lead cruzando a consciência com [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) e [`lead-types`](../../frameworks/lead-types.md): descarte o lead que contradiz a consciência.
8. Self-verify com red-team e registre a Big Idea (locked e pruned) no `big-idea-registry` e a posição/lead no `decision-registry`. Passe os quatro gates.

## Artefatos Produzidos
- `decision.big-idea-locked` + `artifact.big-idea` — a UMA tese travada com promessa, gancho, vilão, mecanismo amarrado, consciência-alvo, scores e ramos podados.
- `decision.positioning-locked` + `decision.lead-type-locked` + `artifact.positioning` — categoria, atributo único, fórmula de Moore, lead travado com justificativa.
- Registries escritos: [`big-idea-registry`](../../data/registries/big-idea-registry.md) e [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`big-idea/big-idea-single-gate`](../../checklists/big-idea/big-idea-single-gate.md) · [`big-idea/big-idea-new-big-credible-gate`](../../checklists/big-idea/big-idea-new-big-credible-gate.md) · [`big-idea/big-idea-awareness-fit-gate`](../../checklists/big-idea/big-idea-awareness-fit-gate.md)
- [`positioning/positioning-awareness-fit`](../../checklists/positioning/positioning-awareness-fit.md)

## Critério de Saída
Existe UMA Big Idea (não duas) com soma alta e nenhum critério ≤ 2; o fit de consciência está confirmado; o gancho faz parar e o vilão culpa algo externo; a posição está travada (categoria, atributo único, fórmula de Moore completa); o lead está travado com justificativa de consciência e carrega o gancho da tese; os quatro gates estão verdes; tudo está registrado. Fecha a camada D3. A próxima fase é a [`09-offer-book-assembly`](09-offer-book-assembly.md), que recebe a tese e a posição para fechar o mapa-mestre e rodar o ★ HARD STOP.
