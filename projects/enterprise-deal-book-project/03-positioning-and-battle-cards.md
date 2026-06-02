---
id: project.enterprise-deal-book-project.03-positioning-and-battle-cards
title: "Fase 03 — Posicionamento & Battle Cards"
type: project-phase
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
consumes:
  - artifact.business-case-metrics
  - artifact.dmu-map
  - artifact.proof-bank
  - template.strategy.positioning
produces:
  - artifact.positioning-statement
  - artifact.commercial-insight
  - artifact.battle-cards
  - decision.big-idea-locked
tags: [project-phase, enterprise, b2b, posicionamento, battle-cards, challenger, reframe, competition, d3]
---

# Fase 03 — Posicionamento & Battle Cards

## Objetivo da Fase
Fixar o posicionamento contra a concorrência e o status quo, e armar o comitê para a disputa. Em vendas complexas, desafiar vence relacionar — o cliente paga por um ponto de vista, não por simpatia. Esta fase transforma o caso de valor num insight comercial que reformula como o comitê vê o próprio problema, trava o posicionamento contra os concorrentes e o "não fazer nada", e produz as battle cards: a munição que o campeão e o vendedor usam contra cada alternativa. O estado-pronto é o statement de posicionamento ajustado aos critérios de decisão, UMA tese de reframe (o insight comercial como Big Idea do deal), e uma battle card por concorrente e pelo status quo, cada uma com a objeção, a refutação e a prova. A régua Challenger manda: o insight deve levar, por lógica, à sua força única — não a uma vantagem genérica.

## Critério de Entrada
A [`02-value-and-pricing-packaging`](02-value-and-pricing-packaging.md) entrega o `artifact.business-case-metrics` e o preço; a [`01-icp-and-dmu`](01-icp-and-dmu.md) entrega a DMU e a prova por papel. Pré-condição: existe um número que justifica a compra e a Concorrência (o "C" de MEDDPICC) está identificada, incluindo o status quo. Se a concorrência não foi mapeada, a fase devolve para levantá-la — sem saber contra quem, não há battle card. O [`decision-registry`](../../data/registries/decision-registry.md) é lido para alinhar com decisões de posicionamento anteriores; o [`big-idea-registry`](../../data/registries/big-idea-registry.md) recebe a tese.

## Agentes & Tasks
- **Task [`lock-positioning-lead`](../../tasks/big-idea/lock-positioning-lead.md)** — dono [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md). Trava o posicionamento e as battle cards.
- **Task [`generate-big-ideas`](../../tasks/big-idea/generate-big-ideas.md)** — dono [`big-idea-architect`](../../agents/big-idea-architect.md). Destila o insight comercial em UMA tese de reframe.

## Passos
1. Fixe o posicionamento com [`positioning/dunford-positioning`](../../frameworks/positioning/dunford-positioning.md): contra qual alternativa você vence e por quê, ajustado aos critérios de decisão.
2. Construa o insight comercial — o reframe — no arco Challenger: provocação, custo escondido do status quo, sentir o problema, revelar a força única. Ref [`reference/books/b2b-enterprise/dixon-adamson-challenger-sale`](../../reference/books/b2b-enterprise/dixon-adamson-challenger-sale.md).
3. Conecte o insight à força única com o mecanismo de [`unique-mechanism.md`](../../frameworks/unique-mechanism.md): o reframe leva, por lógica, à sua solução.
4. Destile UMA tese de reframe com [`big-idea-generator`](../../frameworks/big-idea-generator.md) e [`power-of-one`](../../frameworks/power-of-one.md). Múltiplas teses = reprovação.
5. Mapeie a categoria e o "não fazer nada" como concorrente com [`positioning/category-design`](../../frameworks/positioning/category-design.md): o status quo derruba mais negócios que o rival direto.
6. Monte uma battle card por concorrente e pelo status quo: a objeção típica, a refutação, a prova diferenciadora de [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md).
7. Personalize a munição por papel da DMU: o que o CFO, o técnico e o usuário precisam ouvir contra cada alternativa.
8. Trave o posicionamento e as battle cards. Atualize o `big-idea-registry` e o `decision-registry`.

## Artefatos Produzidos
- `artifact.positioning-statement` — o posicionamento contra a concorrência e o status quo.
- `artifact.commercial-insight` — o reframe Challenger, ancorado em dados.
- `artifact.battle-cards` — uma card por concorrente e pelo status quo, com objeção, refutação e prova.
- `decision.big-idea-locked` — a tese de reframe travada.
- Registries escritos: [`big-idea-registry`](../../data/registries/big-idea-registry.md), [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`big-idea/big-idea-single-gate`](../../checklists/big-idea/big-idea-single-gate.md) — UMA tese de reframe, não várias.
- [`positioning-checklist`](../../checklists/positioning-checklist.md) — o posicionamento bate com a sofisticação do comprador e cobre as battle cards por alternativa.
- [`big-idea/big-idea-new-big-credible-gate`](../../checklists/big-idea/big-idea-new-big-credible-gate.md) — o insight é novo, grande e crível.

## Critério de Saída
O posicionamento está fixado contra a concorrência e o status quo; o insight comercial leva por lógica à força única; UMA tese de reframe está travada; há uma battle card por concorrente e pelo status quo, personalizada por papel. Os gates de big idea e posicionamento estão verdes; os registries estão atualizados. A próxima fase é a [`04-deal-deck-and-business-case`](04-deal-deck-and-business-case.md), que recebe o posicionamento, o insight e as métricas para montar o deck de venda e o business case do comitê.
