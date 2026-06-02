---
id: taxonomy.offer-types
title: "Tipos de Oferta (por papel no Money Model)"
type: taxonomy
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
sources:
  - "Alex Hormozi, *$100M Money Models* (2025)"
  - "Alex Hormozi, *$100M Offers* (2021)"
tags: [offer, money-model, attraction, upsell, downsell, continuity]
---

# Tipos de Oferta (por papel no Money Model)

> **Fonte:** Alex Hormozi, *$100M Money Models* (2025) e *$100M Offers* (2021). **Anti-verbatim:** estrutura e princípios em redação original.

Um **Money Model** é uma **sequência** deliberada de ofertas — o quê, quando e como você oferece para fazer o máximo de dinheiro o mais rápido possível. A meta clássica: ganhar de **um** cliente o bastante para adquirir e atender **dois** outros em menos de 30 dias. Ver [`frameworks/money-model-sequence`](../../frameworks/money-model-sequence.md). Esta taxonomia classifica as ofertas pelo **papel** que cumprem na escada.

| Papel | Função | Exemplos de tipo | Objetivo econômico |
|---|---|---|---|
| **Atração** | Adquirir cliente barato/lucrativo | tripwire, free+frete, BOGO, giveaway, win-your-money-back, decoy, trial pago | **Liquidar o CAC** no front-end |
| **Núcleo (Core)** | A oferta principal | grand slam offer, programa, produto | Entregar a transformação |
| **Upsell** | Vender mais no pico de compra | upgrade, done-for-you, volume, velocidade | Subir o AOV |
| **Downsell** | Recuperar o "não" | versão menor, parcelado, payment plan | Converter quem recusou |
| **Continuidade** | Receita recorrente | assinatura, comunidade, recompra | Maximizar o LTV |

## Tipos de oferta de Atração (liquidam o CAC)
- **Tripwire / low-ticket:** entrada barata que converte estranho em comprador.
- **Free + frete:** "grátis, só paga o envio" — remove fricção, captura cartão.
- **BOGO (compre-um-leve-outro):** aumenta valor percebido sem cortar preço de tabela.
- **Giveaway / sorteio:** topo de funil; capta lead com baixo atrito.
- **Win-your-money-back:** o cliente recupera o valor ao atingir um marco — alinha incentivo e resultado.
- **Decoy (isca):** uma opção propositalmente pior que faz a opção-alvo parecer óbvia (ver [`frameworks/pricing/decoy-effect`](../../frameworks/pricing/decoy-effect.md)).
- **Trial pago / pay-less-now:** baixa barreira de entrada, cobra cheio depois.

## Núcleo, Upsell, Downsell, Continuidade
- **Núcleo:** a oferta que entrega o [mecanismo](../../frameworks/unique-mechanism.md) e a transformação; empilhada via [offer stack](../../frameworks/offer-stack-builder.md) + [garantia](guarantee-types.md).
- **Upsell:** ofertado **no momento da compra** (maior intenção). Tipos: upgrade, "feito-para-você", mais volume, mais velocidade, acesso/proximidade.
- **Downsell:** acionado no "não" — reduz preço/escopo ou parcela. Salva margem que sumiria.
- **Continuidade:** assinatura, comunidade, consumível recorrente — onde mora o LTV e a previsibilidade.

## Como o squad usa
- `money-model-designer`: monta a escada (mín. 2 partes, alvo 4) na planilha [`products-and-offers`](../../templates/offer/products-and-offers-template.csv); o gate `money-model/money-model-four-parts-gate` confere as 4 partes.
- `unit-economics-stack-analyst`: valida que a oferta de atração **liquida o CAC** (gate `money-model-cac-liquidation`).

**Armadilha:** desenhar uma oferta avulsa (só o núcleo) e chamar de "money model". Sem sequência, não há espinha — viola `money_model_spine`.
