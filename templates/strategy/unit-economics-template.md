---
id: template.strategy.unit-economics
title: "Unit Economics Stack — CAC, LTV, AOV e Payback da Escada"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
consumes: [template.strategy.pricing-wtp, template.offer.products-and-offers, template.offer.money-model, template.strategy.market-brief]
produces: [template.core.offer-book-master, template.offer.money-model]
frameworks: [unit-economics-stack, money-model-sequence, pricing.value-based-pricing, value-equation]
checklists: [unit-economics-checklist, money-model/money-model-cac-liquidation]
registries: [offer-registry, decision-registry, price-test-registry]
tags: [template, unit-economics, cac, ltv, aov, payback, strategy]
---

# Unit Economics Stack — CAC, LTV, AOV e Payback da Escada

Esta planilha prova que a oferta **fecha em dinheiro real**: quanto custa adquirir um cliente (CAC), quanto ele vale na vida toda (LTV), quanto gasta por pedido (AOV) e em quantos dias o caixa volta (payback). É a calculadora que sustenta o Money Model: a meta clássica do [`money-model-sequence`](../../frameworks/money-model-sequence.md) é ganhar de **um** cliente o bastante para adquirir e atender **dois** outros em menos de 30 dias. Sem esses números, a escada é torcida, não plano. É o documento que o `unit-economics-stack-analyst` usa para aprovar ou reprovar a viabilidade da sequência. Toda copy e todo funil dependem dele.

## Como usar
- **Agente dono:** `unit-economics-stack-analyst` (camada D2). Trabalha colado ao `money-model-designer` (a sequência) e ao `pricing-wtp-strategist` (os preços que viram receita).
- **Task:** `analyze-unit-economics`. Consome o [`pricing-wtp`](pricing-wtp-template.md), a planilha [`products-and-offers`](../offer/products-and-offers-template.csv) e o [`money-model`](../offer/money-model-template.md).
- **Quando:** depois do preço, junto do Money Model. Confirma se a oferta de atração **liquida o CAC** (gate `money-model-cac-liquidation`) e se a escada bate LTV:CAC ≥ 3 e payback < 30 dias. Alimenta o [`offer-book-master`](../core/offer-book-master.md).
- Regra: use número em todo campo. Separe **CAC blended** (média de todos os canais) de **CAC pago** (só mídia). Cada premissa (conversão, recompra, churn) é uma estimativa rastreável, não um chute. Campo `{{...}}` vazio = conta incompleta.

## Campos & Instruções
- **{{AOV}}** — Average Order Value: ticket médio do **primeiro** pedido (a oferta de entrada/núcleo). Base de tudo.
- **{{CAC}}** — Custo de Aquisição de Cliente: gasto total de marketing/vendas ÷ clientes novos. Separe blended de pago.
- **{{LTV}}** — Lifetime Value: receita total que um cliente gera ao longo da relação (núcleo + upsell + downsell + continuidade), líquida de custo de entrega. Onde mora a continuidade.
- **{{PAYBACK}}** — em quantos dias a receita acumulada de um cliente cobre o CAC. Alvo: < 30 dias (a meta dos "dois novos clientes").
- **{{RAZAO_LTV_CAC}}** — LTV ÷ CAC. Alvo: ≥ 3. Abaixo de 3, a escada não escala; acima de 5, talvez você esteja subinvestindo em aquisição.
- **{{LIQUIDA_CAC}}** — sim/não: a receita da oferta de **atração** sozinha cobre o CAC no front-end? É o gate `money-model-cac-liquidation` e o coração do Money Model.
- **{{MARGEM_CONTRIBUICAO}}** — preço menos custo variável por unidade; o que sobra para cobrir CAC e fixos.
- **{{PREMISSAS}}** — as taxas que sustentam a conta: conversão de atração→núcleo, take-rate de upsell, churn da continuidade. Cada uma rastreável.
- **{{GARGALO}}** — o número que mais limita a escala hoje (CAC alto? payback longo? churn?) e a alavanca para corrigi-lo.
- **{{VEREDITO}}** — a escada fecha (verde) ou não (vermelho), com o porquê.

## O Template
```
# UNIT ECONOMICS STACK — {{NOME_DA_OFERTA}}
Owner: unit-economics-stack-analyst · Data: {{DATA}} · Planilha: products-and-offers.csv
Alvos: LTV:CAC ≥ 3 · Payback < 30d · Atração liquida o CAC

## 1. POR PEDIDO (front-end)
AOV (1º pedido): R$ {{AOV}}
Margem de contribuição: R$ {{MARGEM_CONTRIBUICAO}} ({{PCT_MARGEM}}%)

## 2. AQUISIÇÃO
CAC blended: R$ {{CAC_BLENDED}}  · CAC pago: R$ {{CAC_PAGO}}
Atração liquida o CAC? {{LIQUIDA_CAC}}  (receita da atração R$ {{RECEITA_ATRACAO}} vs CAC)

## 3. VIDA DO CLIENTE
LTV (líquido): R$ {{LTV}}
Composição: núcleo R$ {{V_NUCLEO}} + upsell R$ {{V_UPSELL}} + continuidade R$ {{V_CONT}}/mês × {{MESES}}

## 4. SAÚDE DA ESCADA
LTV:CAC: {{RAZAO_LTV_CAC}}  · Payback: {{PAYBACK}} dias

## 5. PREMISSAS (rastreáveis)
{{PREMISSAS}}

## 6. GARGALO & VEREDITO
Gargalo atual: {{GARGALO}}
Veredito: {{VEREDITO}}

## 7. GATES
LTV:CAC ≥ 3 e payback < 30d: {{STATUS_SAUDE}}
Atração liquida CAC (money-model-cac-liquidation): {{STATUS_CAC}}
```

## Exemplo preenchido
> **# UNIT ECONOMICS STACK — Escada do Lucro Recuperado**
> Owner: unit-economics-stack-analyst · Data: 2026-06-02 · Planilha: products-and-offers.csv
>
> **1. POR PEDIDO** — AOV (1º pedido = Diagnóstico tripwire): R$27. Margem de contribuição: R$25 (93%).
> **2. AQUISIÇÃO** — CAC blended: R$24. CAC pago: R$31. Atração liquida o CAC? **SIM** — o Diagnóstico de R$27 cobre o CAC blended de R$24 no front-end.
> **3. VIDA DO CLIENTE** — LTV líquido: R$1.840. Composição: núcleo R$497 + upsell (implementação) R$1.497 a 22% de take + continuidade R$197/mês × ~6 meses.
> **4. SAÚDE DA ESCADA** — LTV:CAC: **8,8**. Payback: **<30 dias** (o núcleo cobre o CAC já na primeira compra após o tripwire).
> **5. PREMISSAS** — Conversão atração→núcleo: 18%. Take-rate upsell: 22%. Churn da continuidade: ~15%/mês (≈6 meses de vida). Fonte: benchmark do nicho + 142 lojas piloto.
> **6. GARGALO & VEREDITO** — Gargalo: o churn da continuidade limita o LTV; alavanca = onboarding melhor nos 30 primeiros dias. Veredito: **escada fecha com folga** — financia 2+ clientes novos por cliente em <30 dias.
> **7. GATES** — LTV:CAC ≥3 e payback <30d: **VERDE**. Atração liquida CAC: **VERDE** (R$27 > R$24).

## DoD do entregável
A Unit Economics Stack está pronta quando: (1) AOV, CAC (blended **e** pago), LTV e payback têm número, sem campo solto; (2) a margem de contribuição está calculada e é positiva; (3) está provado se a oferta de **atração** liquida o CAC no front-end (`money-model-cac-liquidation` verde) — o coração do Money Model; (4) a razão LTV:CAC é ≥ 3 ou há justificativa explícita, e o payback é < 30 dias ou há plano para chegar lá; (5) a composição do LTV mostra cada degrau (núcleo, upsell, continuidade) batendo com a planilha [`products-and-offers`](../offer/products-and-offers-template.csv); (6) cada premissa (conversão, take-rate, churn) é uma estimativa **rastreável** com fonte, não um chute; (7) o gargalo de escala está nomeado com a alavanca de correção; (8) há um veredito claro (fecha/não fecha) e os números estão registrados no [`offer-registry`](../../data/registries/offer-registry.md) e a decisão no [`decision-registry`](../../data/registries/decision-registry.md). Só então a viabilidade libera o [`money-model`](../offer/money-model-template.md) e o restante do [`offer-book-master`](../core/offer-book-master.md).
