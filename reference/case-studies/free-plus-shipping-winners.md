---
id: reference.case.free-plus-shipping-winners
title: "Caso — Ofertas Vencedoras de Free + Frete"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Alex Hormozi, *$100M Money Models* (Acquisition.com $100M Series, 2025) e *$100M Offers* (2021)."
  - "Dan Ariely, *Predictably Irrational* (2008) — o poder do 'grátis'."
  - "Padrões representativos de mercado de e-commerce/DTC (faixas observadas, não auditadas) — rotulados no texto."
tags: [case-study, free-plus-shipping, tripwire, attraction, aov, upsell, cac-liquidation]
---

# Caso — Ofertas Vencedoras de Free + Frete

## Contexto
"Grátis, você só paga o frete." Essa frase move bilhões em e-commerce e infoprodutos. A oferta de **free + frete** entrega um produto físico ou digital de baixo custo "de graça", cobrando apenas o envio. Parece ilógico — onde está o lucro? O lucro nunca esteve no item grátis. Ele está em **três lugares**: o cartão capturado, o upsell no checkout e a escada que vem depois. O item grátis é a **oferta de atração** mais barata que existe para transformar um estranho em comprador. Quem usa free + frete bem não vende um produto — compra um cliente. Este caso disseca o esqueleto vencedor. As cifras são **faixas representativas de mercado**, claramente rotuladas.

## A jogada
A jogada é usar "grátis" como gatilho de ação e o checkout como o verdadeiro ponto de lucro. Ver o tipo "free + frete" em [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md):

- **Atração:** um produto irresistível e de baixo custo (livro, amostra, ferramenta, kit) oferecido grátis; o cliente paga só o envio. A fricção de compra despenca porque "grátis" desliga o cálculo de risco.
- **Captura do cartão:** o passo decisivo. Ao inserir o cartão para pagar o frete, o cliente vira comprador — e abre a porta para upsells de um clique.
- **Upsell imediato (bump + OTO):** no checkout, um *order bump* ("adicione X por um pouco mais") e uma *one-time offer* (OTO) na página seguinte. É aqui que a margem aparece.
- **Downsell:** se recusa a OTO, uma versão menor recupera parte do "não".
- **Continuidade:** o comprador entra numa escada — assinatura, recompra ou núcleo caro depois.

A **big idea** (UMA, ver `one_big_idea`): *o item não custa nada — o risco de não tê-lo, sim*. A âncora é a ação fácil agora, não o produto.

O **money model** trata o item grátis como **degrau de liquidação de CAC** (`money_model_spine`): o frete cobre parte do custo, o order bump e a OTO liquidam o resto, e a escada captura o lucro. A oferta de atração não precisa lucrar — precisa **pagar a própria aquisição** para que o upsell e a continuidade sejam puro ganho.

## Por que funcionou
- **O poder do "grátis":** "grátis" não é só um preço baixo — é um botão emocional. As pessoas reagem a "grátis" de forma desproporcional (ver [`../books/persuasion-psychology/ariely-predictably-irrational.md`](../books/persuasion-psychology/ariely-predictably-irrational.md)). Cobrar R$ 0 pelo item e só o frete vence "barato".
- **Fricção mínima de entrada:** sem decisão de preço, o estranho age. O primeiro "sim" é o mais caro de conseguir; "grátis" o torna barato.
- **Pico de compra para o upsell:** o cartão já está digitado e a intenção no auge. O order bump e a OTO entram no instante certo (Cialdini — compromisso e coerência).
- **Liquidação de CAC:** quando o frete + bump + OTO cobrem o custo de aquisição, cada cliente novo entra de graça e a escada vira lucro líquido.
- **Escassez verdadeira:** "estoque limitado do brinde" só se for real (`truthful_scarcity`) — caso contrário, veto.

## Números & resultado
Cifras abaixo são **padrão representativo do mercado** (faixas observadas), não números de uma campanha única:
- **Conversão da página free + frete:** tende a ser **mais alta** que a de um tripwire pago equivalente, porque "grátis" reduz a fricção (faixa observada ampla).
- **Take-rate de order bump:** uma fração relevante dos compradores aceita o bump quando ele é barato e relevante (padrão comum; varia muito).
- **Take-rate de OTO:** menor que o bump, mas com ticket maior — soma decisiva ao AOV.
- **Economia da liquidação:** o sucesso é medido por **CAC liquidado no checkout**, não por lucro no item. Se frete + bump + OTO ≥ custo de aquisição, a escada inteira vira margem.
Sempre meça o seu funil real; benchmark externo só serve para detectar anomalia.

## Lições reutilizáveis
- **money-model-designer:** trate o item grátis como **degrau de liquidação de CAC**, nunca como fonte de lucro. Empilhe **order bump + OTO** no checkout para que frete + upsells cubram a aquisição; só então a continuidade é ganho puro. Confira a liquidação antes de escalar mídia.
- **big-idea-architect:** ancore a oferta na **ação fácil agora** ("não custa nada tê-lo"), não no produto — "grátis" é gatilho emocional, não só preço baixo.
- **launch-producer:** posicione bump e OTO **no pico de compra** (cartão digitado), com escassez do brinde **verdadeira**; nunca empurre o upsell para depois do checkout.
- **affiliate-program-architect:** o free + frete é uma **oferta de afiliado** poderosa — a baixa fricção eleva a conversão do parceiro; pague comissão sobre o **valor total do funil**, não só sobre o item.

## Cross-refs
- [`book-funnel-launch.md`](book-funnel-launch.md) — o livro como item de atração (frete cobre o custo).
- [`agora-empiricus-front-to-back.md`](agora-empiricus-front-to-back.md) — front-end barato que financia o back-end.
- [`ladder-pricing-examples.md`](ladder-pricing-examples.md) — a escada que captura o lucro depois.
- [`dtc-subscription-box.md`](dtc-subscription-box.md) — quando a amostra grátis vira assinatura.
- [`../books/persuasion-psychology/ariely-predictably-irrational.md`](../books/persuasion-psychology/ariely-predictably-irrational.md) — o poder do "grátis".
- [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md) — o tipo free + frete.

## Fontes
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025) e *$100M Offers* (2021); Dan Ariely, *Predictably Irrational* (2008). Faixas numéricas marcadas como **padrão representativo do mercado**, não cifras auditadas. Acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
