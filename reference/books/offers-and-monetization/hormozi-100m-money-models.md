---
id: reference.book.hormozi-100m-money-models
title: "$100M Money Models — Alex Hormozi (2025)"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Alex Hormozi, *$100M Money Models: How To Make Money* (Acquisition.com $100M Series, 2025), ISBN 978-1-7374757-8-1."
tags: [money-model, offer-sequence, upsell, downsell, continuity, cfa, payback, hormozi]
---

# $100M Money Models — Alex Hormozi (2025)

## Citação
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025), Acquisition.com $100M Series, ISBN 978-1-7374757-8-1.
> **Anti-verbatim:** princípios em redação original; citação literal ≤25 palavras, atribuída.

## Tese central
Os dois primeiros livros da série resolvem duas peças soltas: a oferta e o fluxo de leads. Este terceiro livro junta tudo numa máquina. A tese é que dinheiro não vem de **uma** oferta, vem da **ordem** das ofertas. Hormozi chama isso de **Money Model**: a sequência desenhada de propostas que um cliente atravessa, da primeira compra ao pagamento recorrente. O objetivo central muda o jogo. Em vez de só baixar o custo de adquirir um cliente (CAC), você desenha a sequência para que **um cliente pague pela aquisição de dois ou mais — em menos de 30 dias**. Quando o caixa gerado por cliente novo cobre o custo de trazer os próximos, o crescimento deixa de depender de capital externo e passa a se autofinanciar. O lançamento do livro foi a própria demonstração: vendeu cerca de 2,9 milhões de cópias num dia (17 de agosto de 2025, Las Vegas) e entrou para o Guinness como o livro de não-ficção mais vendido em 24 horas, com a oferta do livro encadeada a um upsell de continuidade de alto valor ao vivo.

## Frameworks/Modelos

### Money Model Sequence (A Sequência de Ofertas)
A espinha do squad. Quatro tipos de oferta em ordem: **atração** (a oferta de entrada que liquida o CAC), **upsell** (sobe o ticket logo após o "sim"), **downsell** (recupera quem disse não, com versão menor/mais barata) e **continuidade** (receita recorrente que sustenta o LTV). Cada passo tem o seu próprio CTA. Operacionalizamos a sequência inteira em [`../../frameworks/money-model-sequence.md`](../../../frameworks/money-model-sequence.md), com os sub-frameworks de [desenho da oferta de atração](../../../frameworks/money-model-designer/attraction-offer-design.md), [lógica de upsell/downsell](../../../frameworks/money-model-designer/upsell-downsell-logic.md) e [continuidade](../../../frameworks/money-model-designer/continuity-design.md).

### Client-Financed Acquisition / CFA (Aquisição Financiada pelo Cliente)
O coração econômico. A meta operacional: o lucro bruto da primeira janela (≤30 dias) de um cliente novo deve ser **maior** que o custo de adquiri-lo, com folga para financiar os próximos. Isso troca "quanto custa um cliente?" por "em quanto tempo o cliente devolve o dobro?". O `unit-economics-stack-analyst` calcula a janela de payback e a liquidação de CAC no front-end. Ver [`../../frameworks/money-model-designer/offer-ladder-sequencing.md`](../../../frameworks/money-model-designer/offer-ladder-sequencing.md).

### A Escada de Ofertas (Offer Ladder)
As ofertas não são avulsas; cada uma prepara a próxima. A atração resolve um problema estreito e revela o seguinte; o upsell vende a solução completa; a continuidade vende o resultado mantido no tempo. O `money-model-designer` desenha a escada **antes** de qualquer copy — é o `money_model_spine` do config, e o `value-equation-engineer` reprova qualquer degrau que não mova uma alavanca de valor.

## Princípios
- O centro do negócio é a **sequência**, não a oferta isolada; quem vende uma oferta só deixa dinheiro na mesa.
- Desenhe para que **um cliente financie a aquisição de dois** em menos de 30 dias; aí o crescimento se autofinancia.
- Toda oferta da escada tem CTA próprio e prepara a porta da próxima — atração revela o problema que o upsell resolve.
- Upsell logo após o "sim" aproveita o pico de compromisso; o downsell recupera o "não" sem queimar a lista.
- Continuidade é onde mora o lucro de verdade; o front-end existe para comprar clientes baratos, não para lucrar.
- Caixa rápido vence margem teórica: prefira o modelo que devolve o CAC primeiro, mesmo com ticket de entrada menor.

## Como o squad usa
- `money-model-designer`: dono da espinha — desenha as 4 partes em sequência e bloqueia D4+ até a escada existir.
- `unit-economics-stack-analyst`: calcula LTV:CAC, janela de payback e liquidação de CAC no front-end (`unit_economics_known`).
- `pricing-wtp-strategist`: define o ticket de cada degrau para sustentar o CFA sem matar a conversão de entrada.
- `value-equation-engineer`: audita cada oferta da escada contra as quatro alavancas e reprova degraus órfãos.
- `funnel-architect`: traduz a escada em funil sem becos sem saída, com upsell/downsell mapeados após o checkout.
- `launch-producer`: encadeia a sequência no run-of-show do evento, como no próprio lançamento-recorde do livro.

## Cross-refs
- [`hormozi-100m-offers.md`](hormozi-100m-offers.md) — a Grand Slam Offer que vira a oferta de **atração** da escada.
- [`hormozi-100m-leads.md`](hormozi-100m-leads.md) — o fluxo de leads que entra no topo da sequência.
- [`ramanujam-monetizing-innovation.md`](ramanujam-monetizing-innovation.md) — WTP e empacotamento que definem o ticket de cada degrau.
- [`nagle-strategy-tactics-pricing.md`](nagle-strategy-tactics-pricing.md) — preço por valor que sustenta o LTV da continuidade.
- [`../../lib/taxonomies/offer-types.md`](../../../lib/taxonomies/offer-types.md) — tipologia de atração, upsell, downsell e continuidade.
