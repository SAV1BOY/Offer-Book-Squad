---
id: reference.case.ladder-pricing-examples
title: "Caso — Escadas de Preço (Ladder Pricing) na Prática"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Alex Hormozi, *$100M Money Models* (Acquisition.com $100M Series, 2025)."
  - "Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016)."
  - "Padrões representativos de mercado (faixas observadas, não cifras auditadas) — rotulados no texto."
tags: [case-study, pricing, offer-ladder, ascension, tripwire, continuity, money-model]
---

# Caso — Escadas de Preço (Ladder Pricing) na Prática

## Contexto
Quase todo negócio digital começa com **um** preço e **um** produto. O fundador escolhe um número, publica e espera. O problema aparece rápido. Alguns clientes achariam o preço barato e pagariam muito mais. Outros nunca vão pagar aquele valor, mas comprariam algo menor. Um preço único deixa dinheiro dos dois lados na mesa. A **escada de preço** resolve isso. Ela oferece degraus — do mais barato ao mais caro — para que cada cliente entre no nível que cabe no seu bolso e na sua confiança. Este caso reúne o padrão estrutural de como as escadas mais fortes do mercado de educação, software e DTC são montadas. Os números aqui são **faixas representativas de mercado**, claramente rotuladas — servem de gabarito de proporção, não de promessa.

## A jogada
A jogada é tratar preço como **sequência de papéis**, não como um número. Ver os papéis em [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md). Uma escada madura tem quatro a cinco degraus:

- **Degrau de atração (isca):** um tripwire barato, free + frete ou aula paga simbólica. O objetivo não é lucrar — é converter estranho em comprador e liquidar o CAC. Faixa típica observada: de grátis-mais-frete a um ticket de baixo valor.
- **Núcleo (oferta principal):** a *grand slam offer* com mecanismo nomeado e value stack. É o coração da margem. O preço deriva de **valor percebido**, não de custo (ver [`../books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../books/offers-and-monetization/ramanujam-monetizing-innovation.md)).
- **Upsell de velocidade/proximidade:** acesso a mentoria, "feito-para-você" ou turma acelerada. Vendido **no pico de compra**, multiplica o ticket médio (AOV).
- **Downsell:** versão menor ou parcelamento, para recuperar o "não" sem queimar o lead.
- **Continuidade:** assinatura ou comunidade no topo, onde mora o LTV.

A **big idea** (UMA, ver `one_big_idea`) que sustenta a escada é simples: *cada cliente compra o quanto de transformação está pronto a comprar hoje*. A escada não empurra — ela revela o próximo degrau no momento certo.

O **money model** aqui é a própria espinha (`money_model_spine`): a razão entre os degraus importa mais que cada preço isolado. Um salto de preço grande demais entre dois degraus quebra a subida; um salto pequeno demais não cria âncora. O **efeito decoy** (ver [`../../frameworks/pricing/decoy-effect.md`](../../frameworks/pricing/decoy-effect.md)) é usado de propósito: uma opção intermediária pior faz a opção-alvo parecer óbvia.

## Por que funcionou
- **Captura de disposição a pagar (WTP):** clientes têm WTP diferente. A escada segmenta sem perguntar — quem pode mais, sobe; quem pode menos, entra embaixo. Nenhum dinheiro fica nos extremos.
- **Âncora de preço:** o degrau caro torna o do meio "razoável". Sem o topo, o meio parece caro. Ancoragem é um viés robusto (ver [`../psychology/cognitive-biases-for-offers.md`](../psychology/cognitive-biases-for-offers.md)).
- **Escada de confiança:** o cliente compra barato, confia, e sobe. Cada degrau pago reduz a descrença do próximo. Compra gera coerência (Cialdini).
- **Pico de compromisso:** o upsell entra no instante do "sim", quando a intenção é máxima. Adiar o upsell mata a conversão.
- **LTV na continuidade:** a escada sem topo recorrente é um lançamento, não um negócio. A continuidade transforma compra única em relação.

## Números & resultado
Cifras abaixo são **padrão representativo do mercado** (faixas observadas), não números auditados de uma campanha única — use como proporção de referência:
- **Razão entre degraus:** saltos de 3x a 10x entre níveis adjacentes são uma faixa comum em escadas de info/coaching. Saltos maiores costumam exigir um degrau intermediário.
- **Conversão do degrau de atração:** 1–5% do tráfego de página é uma faixa plausível para tripwire/front-end (ilustrativo, varia muito).
- **Take-rate de upsell no pico:** ofertas de upsell imediato bem casadas captam uma fração relevante dos compradores do núcleo (faixa observada ampla; depende de fit e preço).
- **Peso da continuidade no LTV:** em modelos maduros, a receita recorrente costuma responder pela maior parte do valor do cliente ao longo do tempo — é onde o lucro real se acumula.
Sempre meça a sua escada real. Benchmark externo serve só para detectar anomalia, nunca como meta.

## Lições reutilizáveis
- **money-model-designer:** desenhe a escada como **sequência de papéis** (atração → núcleo → upsell → downsell → continuidade), não como lista de produtos. Calibre a **razão entre degraus** antes de fixar qualquer número; teste o salto de preço como hipótese. Use um degrau decoy de propósito para tornar o alvo óbvio.
- **pricing-wtp-strategist:** derive cada degrau de **WTP/valor**, nunca de custo. Posicione a âncora cara primeiro para tornar o meio razoável.
- **big-idea-architect:** ancore a escada numa ideia que **convida a subir** sem empurrar — "compre o quanto de resultado você está pronto a comprar hoje".
- **launch-producer:** encadeie os CTAs no **pico de compromisso**; nunca adie o upsell para depois do checkout.

## Cross-refs
- [`100m-money-models-records.md`](100m-money-models-records.md) — uma escada inteira rodando ao vivo num só evento.
- [`coaching-ascension-mastermind.md`](coaching-ascension-mastermind.md) — a escada de ascensão até o topo high-ticket.
- [`saas-trial-to-paid.md`](saas-trial-to-paid.md) — escada de planos em software (good-better-best).
- [`continuity-retention-wins.md`](continuity-retention-wins.md) — o degrau de continuidade que sustenta o LTV.
- [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md) — os papéis de cada degrau.
- [`../books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../books/offers-and-monetization/ramanujam-monetizing-innovation.md) — preço a partir de valor.

## Fontes
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025); Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016). Faixas numéricas marcadas como **padrão representativo do mercado**, não cifras auditadas. Acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
