---
id: swipe.offers.attraction-offer-cac-liquidator
title: "Padrão: Oferta de Atração que Liquida o CAC"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [money-model-sequence, value-equation, offer-stack-builder]
sources:
  - "Alex Hormozi, *$100M Money Models* (2025)."
  - "Alex Hormozi, *$100M Offers* (2021)."
tags: [swipe, offers, attraction, tripwire, cac-liquidation, front-end, money-model]
---

# Padrão: Oferta de Atração que Liquida o CAC

## O que é
Arquétipo: **a oferta de front-end barata cujo trabalho é comprar clientes, não lucrar** — a entrada da escada do Money Model. Ela existe para converter um estranho em comprador ao menor atrito possível e, idealmente, para que o caixa do dia **pague a mídia do dia** (aquisição financiada pelo cliente). Não é a oferta que entrega a grande transformação; é a porta que cria a relação e libera o upsell no pico de compromisso. Estudamos a **estrutura econômica e de conversão** da oferta de atração, não a copy de campanha alheia. Ver a [taxonomia de tipos de oferta](../../lib/taxonomies/offer-types.md).

## Anatomia
Os beats da oferta de atração, na nossa leitura:
1. **Isca de valor desproporcional.** Uma promessa pequena, específica e rápida que vale muito mais que o preço de entrada — atrito de compra mínimo.
2. **Preço-âncora baixo (ou grátis + frete).** O número baixa a barreira do primeiro "sim" e captura o meio de pagamento. Ver [`offer-types`](../../lib/taxonomies/offer-types.md).
3. **Resultado rápido prometido.** A atração entrega uma vitória rápida — sobe a probabilidade percebida e prepara a próxima compra.
4. **Razão honesta para o preço baixo.** Um motivo crível ("amostra", "primeira dose", "para conhecer o método") que evita parecer barato demais.
5. **Upsell imediato no mesmo checkout.** Logo após o "sim", uma oferta que multiplica o ticket — o pico de compromisso. Ver o teardown [`hormozi-100m-money-models-launch`](../../reference/swipe-breakdowns/hormozi-100m-money-models-launch.md).
6. **Ponte para a continuidade.** O fluxo aponta para a recorrência onde mora o LTV.
7. **Cálculo de payback embutido.** A oferta só existe se a conta fecha: o lucro bruto da janela liquida o CAC. Ver [`money-model-sequence`](../../frameworks/money-model-sequence.md).

## Por que funciona
- **Money Model Spine.** O valor está na *sequência* (atração→upsell→continuidade), não na oferta isolada — princípio `money_model_spine`. Ver [`money-model-sequence`](../../frameworks/money-model-sequence.md).
- **Aquisição financiada pelo cliente.** O caixa do front-end paga a aquisição do próximo cliente; o crescimento se autofinancia. Ver o teardown [`hormozi-100m-money-models-launch`](../../reference/swipe-breakdowns/hormozi-100m-money-models-launch.md).
- **Atrito baixo = mais "sins".** Preço baixo e promessa específica maximizam a taxa de primeira compra — alavanca de esforço/sacrifício da [Value Equation](../../frameworks/value-equation.md).
- **Pico de compromisso.** O upsell chega no instante do "sim", quando a coerência interna empurra a próxima decisão — ver [`commitment-consistency`](../../reference/psychology/commitment-consistency.md).
- **Decisão de economia, não de ego.** A oferta vive ou morre pela unidade econômica — `evidence_before_opinion`, validada pelo [unit-economics-stack-analyst](../../agents/unit-economics-stack-analyst.md).

## Padrão reutilizável
Esqueleto da oferta de atração, abstraído e original:
```
ISCA: Por {{preço-baixo-ou-grátis+frete}}, você leva {{vitória-rápida-específica}}.
POR QUE TÃO BARATO: {{razão-honesta}} (amostra / primeira dose / conhecer o método).
RESULTADO RÁPIDO: Em {{prazo-curto}}, você já {{micro-resultado}}.
NO CHECKOUT (upsell imediato):
  - {{upsell}} → multiplica o ticket, ligado por {{motivo-honesto}}.
DEPOIS (continuidade):
  - {{oferta-recorrente}} → mantém o resultado vivo, vira LTV.
CONTA QUE PRECISA FECHAR:
  - CAC alvo: {{R$}} · Lucro bruto da janela: {{R$}} · Payback: {{dias}}.
AÇÃO: {{CTA-de-baixo-atrito}}.
```
Regra de ouro: a atração não precisa lucrar — precisa **liquidar o CAC** dentro da janela definida. Se não fecha, é só barulho.

## Adaptação por sofisticação
Ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md).
- **Estágio 1-2:** a isca lidera pela **promessa** simples e pelo preço; pouca explicação.
- **Estágio 3:** a isca nomeia um **mecanismo** ("o método que financia a aquisição") — o "como" novo justifica a entrada.
- **Estágio 4:** posicione a entrada como **rota superior** (mais rápida, menos risco) para o resultado.
- **Estágio 5:** ancore em **identidade** — "torne-se o tipo de operador que pensa em sequências"; a tribo e o recorde viram o argumento.

## Fonte
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025) e *$100M Offers* (2021) — via [`source-catalog`](../../swipe-sources/source-catalog.md); estrutura econômica detalhada em [`hormozi-100m-money-models-launch`](../../reference/swipe-breakdowns/hormozi-100m-money-models-launch.md). Acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Nenhuma copy de oferta reproduzida; nenhuma citação literal acima.
