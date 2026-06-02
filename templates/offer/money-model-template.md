---
id: template.offer.money-model
title: "Money Model — A Espinha da Escada de Ofertas"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes: [template.offer.products-and-offers, template.strategy.pricing-wtp, template.strategy.unit-economics, template.offer.offer-stack]
produces: [template.core.offer-book-master]
frameworks: [money-model-sequence, offer-stack-builder, value-equation, unit-economics-stack, offer-to-funnel-mapping]
checklists: [money-model/money-model-four-parts-gate, money-model/money-model-cac-liquidation]
registries: [offer-registry, decision-registry]
tags: [template, money-model, sequence, spine, ladder, cac-liquidation]
---

# Money Model — A Espinha da Escada de Ofertas

O Money Model é o **centro do squad**: a *sequência* deliberada de ofertas (atração → núcleo → upsell → downsell → continuidade), não uma oferta avulsa. A meta clássica do [`money-model-sequence`](../../frameworks/money-model-sequence.md): ganhar de **um** cliente o bastante para adquirir e atender **dois** outros em menos de 30 dias. Este template documenta a escada em prosa e amarra cada linha à planilha-mãe [`products-and-offers`](products-and-offers-template.csv). Sem este desenho verde, ninguém escreve copy (`money_model_spine`).

## Como usar
- **Agente dono:** `money-model-designer` — dono da espinha. Validado pelo `unit-economics-stack-analyst` (CAC) e pelo `pricing-wtp-strategist` (preço).
- **Task:** `design-money-model`. Abre depois do mecanismo, do valor e do preço; fecha quando a escada tem ≥2 partes (alvo 4) e a atração liquida o CAC.
- **Quando:** D2, antes do Big Idea. Preencha a planilha [`products-and-offers`](products-and-offers-template.csv) **primeiro** (uma linha por oferta), depois destile aqui a lógica da sequência: por que esta ordem, o que cada degrau resolve, como o dinheiro flui.
- Use número em todo campo econômico (preço, valor ancorado, CAC, LTV). Use a voz do avatar no resultado de cada oferta. Campo `{{...}}` solto = escada incompleta = gate vermelho.

## Campos & Instruções
- **{{NOME_MODELO}}** — o nome de trabalho da escada (ex.: "Escada do Lucro Recuperado").
- **{{META_30_DIAS}}** — a meta de payback: quanto um cliente precisa gerar para financiar a aquisição de N novos em <30 dias.
- **{{OFERTA_ATRACAO}}** / **{{TIPO_ATRACAO}}** — a oferta de entrada e seu tipo ([`offer-types`](../../lib/taxonomies/offer-types.md): tripwire, free+frete, BOGO…). O papel dela é **liquidar o CAC**, não lucrar.
- **{{LIQUIDA_CAC}}** — sim/não: a receita da atração cobre o custo de adquirir o cliente no front-end? É o gate `money-model-cac-liquidation`.
- **{{OFERTA_NUCLEO}}** — a oferta principal que entrega a transformação (a Grand Slam Offer; ver [`offer-stack`](offer-stack-template.md)).
- **{{OFERTA_UPSELL}}** — o que se vende **no pico da compra** (upgrade, feito-para-você, mais velocidade). Sobe o AOV.
- **{{OFERTA_DOWNSELL}}** — como o "não" é recuperado (versão menor, parcelado). Salva margem.
- **{{OFERTA_CONTINUIDADE}}** — a receita recorrente (assinatura, comunidade). Onde mora o LTV.
- **{{LTV}}** / **{{CAC}}** / **{{RAZAO_LTV_CAC}}** / **{{PAYBACK}}** — os números de unit economics da escada inteira (vêm do `unit-economics`). Alvo: LTV:CAC ≥ 3, payback < 30d.
- **{{FLUXO_DO_DINHEIRO}}** — a frase que explica como um cliente financia o próximo: "o tripwire de R$X paga o CAC; o núcleo é lucro; o upsell e a continuidade compõem o LTV".
- **{{PARTES_PREENCHIDAS}}** — quantas das 4 partes existem (mín. 2, alvo 4). É o gate `money-model-four-parts-gate`.

## O Template
```
# MONEY MODEL — {{NOME_MODELO}}
Owner: money-model-designer · Data: {{DATA}} · Planilha: products-and-offers.csv
Meta (<30 dias): {{META_30_DIAS}}

## 1. A ESCADA (a sequência)
[Atração]   {{OFERTA_ATRACAO}} — tipo {{TIPO_ATRACAO}} — R$ {{PRECO_ATRACAO}}
              → liquida o CAC? {{LIQUIDA_CAC}}
[Núcleo]    {{OFERTA_NUCLEO}} — R$ {{PRECO_NUCLEO}}  (entrega a transformação)
[Upsell]    {{OFERTA_UPSELL}} — R$ {{PRECO_UPSELL}}  (no pico da compra)
[Downsell]  {{OFERTA_DOWNSELL}} — R$ {{PRECO_DOWNSELL}}  (recupera o "não")
[Continui.] {{OFERTA_CONTINUIDADE}} — R$ {{PRECO_CONTINUIDADE}}/mês  (LTV)
Partes preenchidas: {{PARTES_PREENCHIDAS}}/4

## 2. POR QUE ESTA ORDEM
{{LOGICA_DA_SEQUENCIA}}  (o que cada degrau resolve e por que vem aqui)

## 3. O FLUXO DO DINHEIRO
{{FLUXO_DO_DINHEIRO}}

## 4. UNIT ECONOMICS DA ESCADA
LTV: R$ {{LTV}} · CAC: R$ {{CAC}} · LTV:CAC: {{RAZAO_LTV_CAC}} · Payback: {{PAYBACK}}

## 5. GATES
Quatro partes (money-model-four-parts-gate): {{STATUS_4P}}
Atração liquida CAC (money-model-cac-liquidation): {{STATUS_CAC}}
```

## Exemplo preenchido
> **# MONEY MODEL — Escada do Lucro Recuperado**
> Owner: money-model-designer · Data: 2026-06-02 · Planilha: products-and-offers.csv
> Meta (<30 dias): cada cliente do núcleo financia a aquisição de 2 novos clientes.
>
> **1. A ESCADA**
> [Atração] Diagnóstico Lucro em 7 Dias — tripwire — R$ 27 → liquida o CAC? **SIM**
> [Núcleo] Motor de Recuperação 72h — R$ 497 (entrega +18% de receita recuperada)
> [Upsell] Implementação Feita-para-Você — R$ 1.497 (no pico da compra)
> [Downsell] Motor 72h parcelado 3x de R$ 197 — recupera o "não" do preço cheio
> [Continui.] Otimização Recorrente — R$ 197/mês (LTV)
> Partes preenchidas: **4/4** (atração, núcleo, upsell, continuidade) + downsell.
>
> **2. POR QUE ESTA ORDEM** — O tripwire de R$27 converte estranho em comprador e paga o anúncio. O núcleo entrega o resultado e gera o lucro. O upsell entra no pico de intenção (logo após o "sim" do núcleo). A continuidade transforma um resultado pontual em receita previsível.
> **3. O FLUXO DO DINHEIRO** — O Diagnóstico de R$27 cobre o CAC de R$24. O Motor (R$497) é lucro quase puro. Implementação (R$1.497) e a mensalidade (R$197) empilham o LTV até R$1.840.
> **4. UNIT ECONOMICS** — LTV R$ 1.840 · CAC R$ 210 · LTV:CAC **8,8** · Payback **<30d**.
> **5. GATES** — Quatro partes: **VERDE** (4/4). Atração liquida CAC: **VERDE** (R$27 > R$24 de CAC).

## DoD do entregável
O Money Model está pronto quando: (1) a escada tem ≥2 partes preenchidas (alvo 4) e bate com a planilha [`products-and-offers`](products-and-offers-template.csv) linha a linha; (2) existe uma oferta de **atração** e o `unit-economics-stack-analyst` confirma que ela **liquida o CAC** no front-end (`money-model-cac-liquidation` verde); (3) a oferta núcleo entrega o mecanismo e a transformação; (4) cada preço deriva de WTP, nunca de custo; (5) o fluxo do dinheiro está descrito (quem financia quem) e LTV, CAC, razão e payback são conhecidos, com LTV:CAC ≥ 3 ou justificativa; (6) a lógica da sequência explica por que cada degrau vem onde vem; (7) o `money-model-four-parts-gate` está verde; (8) a decisão de desenho é registrada no [`decision-registry`](../../data/registries/decision-registry.md). Só então a espinha libera o restante do Offer Book ([`offer-book-master`](../core/offer-book-master.md)).
