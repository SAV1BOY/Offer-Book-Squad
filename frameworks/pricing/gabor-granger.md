---
id: framework.pricing.gabor-granger
title: "Gabor-Granger — Curva de Demanda e Receita por Preço"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [van-westendorp, value-based-pricing, price-elasticity, conjoint-cbc, packaging-good-better-best]
sources:
  - "André Gabor & Clive Granger, *On the Price Consciousness of Consumers*, Applied Statistics, vol. 10 (1961)."
tags: [pricing, wtp, demand-curve, revenue-curve, gabor-granger, survey, elasticity]
---

# Gabor-Granger — Curva de Demanda e Receita por Preço

## TL;DR
Gabor-Granger transforma WTP em **demanda**. Você mostra um preço e pergunta "compraria?". Repete subindo e descendo o preço. A cada nível, conta quantos diriam "sim". Isso desenha a **curva de demanda** (% que compra × preço) e a **curva de receita** (preço × % que compra). Você lê direto o preço que **maximiza receita** e o que maximiza take-rate. É o passo seguinte ao Van Westendorp: este diz quanto cobrar para ganhar mais, não só a faixa. É a segunda ferramenta de WTP do `pricing-wtp-strategist`.

## Quando usar / Quando não
**Use** quando já tem uma faixa de preço (do [`van-westendorp.md`](van-westendorp.md) ou do valor) e quer escolher o **número** dentro dela com base em demanda projetada.
**Use mais** quando o produto é único (sem trade-off de features a testar) e você precisa da curva de receita para decidir preço de tabela ou de um degrau da escada.
**Não use** quando o cliente precisa **comparar features** para decidir — aí o preço não existe sozinho; vá para [`conjoint-cbc.md`](conjoint-cbc.md).
**Não use** como verdade absoluta de volume real: respostas de pesquisa superestimam a compra. Trate a curva como **relativa** (qual preço vence qual), não como previsão de unidades.

## Inputs
- Uma faixa de preços plausível para testar (5 a 8 pontos cobrindo piso e teto da faixa).
- Descrição clara da oferta, com valor já comunicado (senão o "sim" despenca).
- Amostra do avatar-alvo, segmentável — mínimo prático ~100-200 por segmento.
- Sua margem por unidade, para cruzar a curva de receita com lucro depois.

## Procedimento
1. **Defina os pontos de preço** a testar dentro da faixa (ex.: R$990, R$1.290, R$1.490, R$1.790, R$1.990). Use intervalos regulares ou ancorados em números psicológicos.
2. **Escreva a pergunta de compra**: "A R$X, você compraria [oferta]?" — resposta binária (sim/não) ou escala de intenção (1-5, onde 4-5 conta como "compraria").
3. **Apresente os preços em ordem aleatória** por respondente, ou use a escada clássica: comece num preço, suba se "sim", desça se "não", até achar o ponto de virada de cada pessoa. A ordem aleatória reduz viés de âncora; a escada acha o WTP individual.
4. **Colete e limpe**: descarte quem aceita o preço mais alto e rejeita o mais baixo (incoerente).
5. **Monte a curva de demanda**: para cada preço, calcule o **% que compraria** (a esse preço ou menos). A curva cai conforme o preço sobe.
6. **Monte a curva de receita**: multiplique cada preço pelo % que compra. Essa curva sobe, atinge um pico e desce. O **pico é o preço que maximiza receita**.
7. **Leia os três números**: preço de **receita máxima** (topo da curva de receita), preço de **take-rate alvo** (onde X% compra) e a **inclinação** (quão sensível é a demanda — entrada para [`price-elasticity.md`](price-elasticity.md)).
8. **Cruze com margem**: o pico de receita não é o pico de **lucro**. Recalcule com (preço − custo) × % que compra para achar o preço de lucro máximo.
9. **Corte por segmento**: a curva muda por avatar. Segmentos com curva mais alta justificam um pacote premium ([`packaging-good-better-best.md`](packaging-good-better-best.md)).
10. **Registre** a curva, o preço de receita/lucro máximo e o método no `price-test-registry`; declare o método no gate `pricing/pricing-method-declared-gate`.

## Outputs
- **Curva de demanda** (% compra × preço) e **curva de receita** (R$ × preço) por segmento.
- Preço de **receita máxima**, preço de **lucro máximo** e take-rate por preço.
- Estimativa de **elasticidade** local (insumo para [`price-elasticity.md`](price-elasticity.md)).
- Recomendação de preço de tabela ou de degrau, pronta para cruzar com unit economics.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI (núcleo).
- Testamos R$990 / R$1.290 / R$1.490 / R$1.790 / R$1.990 com 160 respostas do ICP "dev pleno".
- Take-rate: 62% / 51% / 44% / 33% / 24%.
- Receita relativa (preço × take): 614 / 658 / 656 / 591 / 478 → **pico em R$1.290-R$1.490**.
- Margem: com custo de entrega R$300, o lucro relativo vira (preço−300)×take → pico desloca para **R$1.490** (lucro máximo um pouco acima do de receita).
- Decisão: tabela do núcleo em **R$1.490**. O segmento "dev sênior" mostrou take-rate 40% a R$1.990 → sustenta um pacote "Pro" mais caro.

## Armadilhas
- **Confiar no volume absoluto.** Pesquisa infla o "sim". Use a curva para **comparar** preços, não para prever unidades vendidas.
- **Não comunicar valor antes de perguntar o preço.** Sem valor na mente, todo preço parece caro e a curva afunda.
- **Viés de âncora pela ordem.** Mostrar do barato ao caro (ou o contrário) distorce. Aleatorize ou use a escada.
- **Parar no pico de receita.** O pico de **lucro** costuma ser mais alto. Sempre cruze com a margem.
- **Faixa de teste estreita.** Se todos os preços têm take-rate alto, você não achou o teto. Amplie a faixa para cima.
- **Ignorar a segmentação.** Uma curva única esconde dois mercados com WTP distinta.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — roda o estudo e lê as curvas de demanda e receita); `unit-economics-stack-analyst` (converte a curva de receita em curva de **lucro** com a margem e valida payback); `money-model-designer` (usa o preço de receita/lucro máximo para fixar o ticket de cada degrau da escada); `positioning-lead-strategist` (a resistência da curva sinaliza se a posição precisa enquadrar melhor o valor antes do preço).
- **Frameworks que pareiam**: [`van-westendorp.md`](van-westendorp.md) (dá a faixa que vira os pontos de teste), [`price-elasticity.md`](price-elasticity.md) (a inclinação da curva é a elasticidade), [`value-based-pricing.md`](value-based-pricing.md) (o teto de valor limita a faixa), [`conjoint-cbc.md`](conjoint-cbc.md) (quando há trade-off de features), [`packaging-good-better-best.md`](packaging-good-better-best.md), [`price-anchoring.md`](../price-anchoring.md).

## Fontes
> **Fonte:** André Gabor & Clive Granger, "On the Price Consciousness of Consumers", *Applied Statistics* vol. 10 (1961) — via [`../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
