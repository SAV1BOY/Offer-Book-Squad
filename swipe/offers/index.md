---
id: swipe.offers.index
title: "Swipe: Ofertas Irresistíveis (índice)"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [offer-stack-builder, value-equation, money-model-sequence]
sources:
  - "Alex Hormozi, *$100M Offers* (2021)."
  - "Alex Hormozi, *$100M Money Models* (2025)."
tags: [swipe, offers, grand-slam, value-equation, money-model, cac-liquidation]
---

# Swipe: Ofertas Irresistíveis (índice)

## O que é
Esta categoria reúne **padrões estruturais de oferta** — o esqueleto que torna uma proposta tão boa que dizer não parece burrice. Aqui não guardamos a copy de nenhuma oferta famosa; guardamos a **anatomia**: como empilhar valor, como nomear o mecanismo, como reverter risco e como encaixar a oferta numa sequência de dinheiro. Cada padrão é um esqueleto reutilizável em redação original, com `{{placeholders}}` que qualquer nicho preenche.

Uma oferta de verdade não é "produto + preço". Ela move as alavancas da [Value Equation](../../frameworks/value-equation.md) — sobe sonho e probabilidade percebida, baixa tempo e esforço — e ocupa um **papel** dentro do Money Model (atração, núcleo, upsell, downsell, continuidade). Por isso os padrões aqui são lidos junto da [taxonomia de tipos de oferta](../../lib/taxonomies/offer-types.md): um esqueleto de oferta-âncora é diferente de um esqueleto de oferta de atração que existe para liquidar o CAC.

## Quando usar
- Quando o `value-equation-engineer` ou o `money-model-designer` precisa de um **gabarito estrutural** para montar a oferta-núcleo ou a escada.
- Quando uma oferta existente converte mal e você quer diagnosticar **qual bloco** está faltando (mecanismo? prova? reversão de risco? continuidade?).
- Quando o front-end precisa de uma **oferta de atração** que compre clientes baratos antes da oferta cara.
- Antes de escrever qualquer copy: a oferta vem **antes** da persuasão (princípio `offer_before_persuasion`).

Evite tratar estes esqueletos como preenchimento mecânico. Cada `{{placeholder}}` exige pesquisa real (avatar, prova, WTP) por trás. Evite também empilhar bônus genéricos só para "engordar" a oferta — cada item precisa mover uma alavanca de valor ou sai.

## Padrões nesta categoria
- [`grand-slam-offer-stack.md`](grand-slam-offer-stack.md) — o esqueleto da **oferta-núcleo empilhada**: mecanismo nomeado, value stack item a item, reversão de risco e escassez verdadeira. Calibrado para a oferta principal que entrega a transformação.
- [`attraction-offer-cac-liquidator.md`](attraction-offer-cac-liquidator.md) — o esqueleto da **oferta de atração** que existe para liquidar o CAC no front-end e financiar a aquisição do próximo cliente. Calibrado para o topo da escada do Money Model.

Cada padrão marca o papel na escada, a alavanca de valor que prioriza e a objeção que ataca, alimentando o `offer-registry` e o desenho do Money Model.

## Liga com
- **Frameworks**: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) (como empilhar valor), [`value-equation`](../../frameworks/value-equation.md) (as 4 alavancas), [`unique-mechanism`](../../frameworks/unique-mechanism.md) (o "como" único), [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md) e [`guarantee-design`](../../frameworks/guarantee-design.md) (reversão de risco), [`money-model-sequence`](../../frameworks/money-model-sequence.md) (a escada), [`grand-slam-offer`](../../frameworks/offer/grand-slam-offer.md) e [`value-stacking`](../../frameworks/offer/value-stacking.md).
- **Agentes**: [`value-equation-engineer`](../../agents/value-equation-engineer.md) (dono do valor), [`money-model-designer`](../../agents/money-model-designer.md) (dono da espinha), [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) (valida liquidação do CAC), [`mechanism-architect`](../../agents/mechanism-architect.md) (nomeia o mecanismo), [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) (ancora o preço).
- **Taxonomias**: [`offer-types`](../../lib/taxonomies/offer-types.md), [`guarantee-types`](../../lib/taxonomies/guarantee-types.md), [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md).
- **Teardowns**: [`hormozi-100m-money-models-launch`](../../reference/swipe-breakdowns/hormozi-100m-money-models-launch.md).
