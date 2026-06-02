---
id: framework.money-model-sequence
title: "Money Model Sequence — A Espinha (Atração → Upsell → Downsell → Continuidade)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [offer-stack-builder, value-equation, offer-to-funnel-mapping, price-anchoring, risk-reversal-ladder, grand-slam-offer]
sources:
  - "Alex Hormozi, *$100M Money Models* (2025)."
  - "Alex Hormozi, *$100M Offers* (2021)."
tags: [money-model, sequence, attraction, upsell, downsell, continuity, cac, ltv]
---

# Money Model Sequence — A Espinha

## TL;DR
Você não vende **uma** oferta. Você vende uma **sequência**: o quê, quando e em que ordem oferecer para tirar o máximo de dinheiro o mais rápido possível. As quatro partes são **Atração → Upsell → Downsell → Continuidade**. A meta clássica: ganhar de **um** cliente o bastante para adquirir e atender **dois** outros em menos de 30 dias. Esta é a espinha do squad (`money_model_spine`): sem a escada montada, nada de copy, funil ou logística nasce. É o `money-model-designer` quem a constrói e protege.

## Quando usar / Quando não
**Use** sempre que houver mais de um produto possível, ou quando o CAC pago exige liquidação rápida no front-end. É o esqueleto de qualquer lançamento ou funil com tráfego pago.
**Use mais** quando o LTV mora na recompra/recorrência — a sequência é o que transforma uma venda em fluxo.
**Não use** como desculpa para empilhar produtos sem fôlego: cada degrau precisa de uma oferta real (passa na [Value Equation](value-equation.md)).
**Mínimo aceitável** = 2 partes (`money_model_min_parts: 2`); **alvo** = as 4. Uma oferta avulsa (só o núcleo) **não** é money model — viola `money_model_spine`.

## Inputs
- O **núcleo** já desenhado (a [Grand Slam Offer](offer/grand-slam-offer.md) ou produto principal).
- Unit economics: CAC pretendido, margem, LTV alvo (do `unit-economics-stack-analyst`).
- A taxonomia de papéis das ofertas — ver [`../lib/taxonomies/offer-types.md`](../lib/taxonomies/offer-types.md).
- Preço e WTP por degrau (do `pricing-wtp-strategist`).
- O avatar e a dor dominante (banco de VOC).

## Procedimento
1. **Fixe a meta econômica**: defina o "CAC a liquidar" e a janela (ex.: front-end paga o tráfego em ≤30 dias). Esse número guia toda a escada.
2. **Desenhe a Atração**: escolha o tipo que **liquida o CAC** (tripwire, free+frete, win-your-money-back, BOGO — ver taxonomia). Pergunta-teste: "esta oferta paga a aquisição do próximo cliente?".
3. **Encaixe o Núcleo**: a oferta que entrega o [mecanismo](unique-mechanism.md) e a transformação. É o centro de gravidade; tudo aponta para ela.
4. **Projete o Upsell** no **momento da compra** (pico de intenção): upgrade, feito-para-você, mais volume, mais velocidade, proximidade. Regra: ofereça **antes** que a empolgação esfrie.
5. **Projete o Downsell** para o "não": versão menor, parcelamento, escopo reduzido. Salva a margem que sumiria no abandono.
6. **Projete a Continuidade**: assinatura, comunidade, consumível recorrente. É onde o LTV e a previsibilidade vivem.
7. **Sequencie e cronometre**: defina a **ordem** e o **gatilho** de cada oferta (na página, no e-mail D+1, no carrinho). Um CTA por degrau — sem bifurcar a decisão.
8. **Cheque a continuidade econômica**: some a contribuição de cada degrau; confirme que a Atração + Upsell cobrem o CAC e que a Continuidade ergue o LTV:CAC.
9. **Registre** a escada na planilha `products-and-offers` e no `offer-registry`; rode o gate `money-model/money-model-four-parts-gate`.

## Outputs
- **Mapa da escada**: 4 papéis preenchidos, cada um com oferta, preço, gatilho e CTA.
- **Tabela de contribuição** por degrau (quanto cada um adiciona ao caixa).
- Veredito de liquidação de CAC (passa / não passa) e leitura de LTV:CAC.
- Handoff pronto para [`offer-to-funnel-mapping.md`](offer-to-funnel-mapping.md) (cada degrau vira páginas + sequências).

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Atração**: e-book "50 frases de entrevista técnica" por R$27 (free+frete na versão impressa). Captura cartão e **liquida o CAC** do anúncio.
- **Núcleo**: programa "Aprovado em Inglês" (R$1.997) — entrega o mecanismo "Shadowing Técnico".
- **Upsell** (no checkout): "Simulador de Entrevista 1:1" (R$897) — done-with-you no pico de intenção.
- **Downsell** (no "não" do núcleo): mesmo programa em 12× sem o 1:1 (R$1.997 parcelado) — recupera quem travou no preço à vista.
- **Continuidade**: "Clube de Conversação" (R$97/mês) — recorrência que ergue o LTV.
- **Leitura**: Atração + Upsell cobrem o CAC no D+1; a Continuidade leva o LTV:CAC de 1,8 para 4,3. A escada está completa e sequenciada.

## Armadilhas
- **Chamar uma oferta avulsa de money model.** Sem sequência não há espinha — reprovação automática.
- **Atração que não liquida o CAC.** Se o front-end não paga a aquisição, a escada sangra caixa.
- **Upsell tarde demais.** Oferecido depois que a empolgação esfria, a taxa despenca. Ofereça no pico.
- **Pular o downsell.** Você descarta a margem de todo "não" que era recuperável.
- **Continuidade sem entrega contínua.** Recorrência que não entrega valor mês a mês vira churn e dano de marca.
- **Bifurcar o CTA.** Dois pedidos no mesmo degrau dividem a decisão e derrubam a conversão.

## Interações
- **Agentes**: `money-model-designer` (dono — pode **vetar** copy/funil/logística antes da escada existir); `unit-economics-stack-analyst` (valida liquidação de CAC e LTV:CAC); `pricing-wtp-strategist` (preço por degrau); `value-equation-engineer` (cada degrau precisa mover alavanca); `funnel-architect` (traduz a escada em páginas); `events-logistics-coordinator` (sequencia ofertas no calendário).
- **Frameworks que pareiam**: [`value-equation.md`](value-equation.md), [`offer-stack-builder.md`](offer-stack-builder.md), [`price-anchoring.md`](price-anchoring.md), [`risk-reversal-ladder.md`](risk-reversal-ladder.md), [`offer-to-funnel-mapping.md`](offer-to-funnel-mapping.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025) e *$100M Offers* (2021) — via [`../reference/books/offers-and-monetization/hormozi-100m-money-models.md`](../reference/books/offers-and-monetization/hormozi-100m-money-models.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
