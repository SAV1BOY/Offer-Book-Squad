---
id: swipe.guarantees.reembolso-incondicional
title: "Padrão: Garantia de Reembolso Incondicional"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [guarantee-design, risk-reversal-ladder, value-equation, proof-to-claim-chain]
sources:
  - "Alex Hormozi, *$100M Offers* (2021), capítulo de Garantias."
tags: [swipe, guarantee, unconditional, refund, risk-reversal, conversion]
---

# Padrão: Garantia de Reembolso Incondicional

## O que é
Este é o **padrão estrutural da garantia incondicional** — a devolução total dentro de um prazo, sem o cliente precisar justificar nada. Corresponde ao **tipo 1** da taxonomia ([`../../lib/taxonomies/guarantee-types.md`](../../lib/taxonomies/guarantee-types.md)) e à família **incondicional**. É a reversão de risco máxima: o comprador não arrisca nada, pois pode desistir e recuperar o dinheiro. Aqui guardamos só a **anatomia** da redação — como declarar o prazo, o gesto e a ausência de fricção — em redação original, nunca copy literal de oferta alheia.

Cabe quando **você controla a entrega** e a **margem absorve** o pior caso (uma fatia pede reembolso). Exige produto sólido. Em mercado de altíssimo churn de oportunistas, a incondicional convida ao abuso — aí o `unit-economics-stack-analyst` filtra antes ou troca pela [condicional](condicional-baseada-em-resultado.md).

## Anatomia
A sequência de elementos que sustenta o padrão:
1. **Declaração da reversão** — "experimente sem risco": a garantia assume o risco pelo comprador, de forma explícita.
2. **Prazo claro** — a janela exata (ex.: 30 dias). Prazo definido fecha disputa e dá segurança operacional.
3. **Gesto de devolução** — "devolvo cada centavo": total, não parcial. Específico, não "satisfação garantida".
4. **Ausência de fricção** — "sem perguntas, sem formulário": quanto menos passos para pedir, mais forte a reversão percebida.
5. **Reancoragem de confiança** — uma frase que mostra **por que** você pode oferecer isso (a confiança no resultado), conectando a garantia à prova.

A garantia entra na copy **depois** do valor e **antes** do preço — reverter risco antes de construir desejo enfraquece o efeito.

## Por que funciona
A incondicional sobe a **Probabilidade percebida** da [Value Equation](../../frameworks/value-equation.md) ao seu teto: se não há risco de perder dinheiro, a barreira de decisão cai. É o degrau 2 da [escada de reversão de risco](../../frameworks/risk-reversal-ladder.md). Apoia-se na **aversão à perda** — o comprador teme perder o que paga, e a devolução total remove exatamente esse medo (ver [`../../reference/psychology/loss-aversion.md`](../../reference/psychology/loss-aversion.md) e [`../../reference/psychology/status-quo-bias.md`](../../reference/psychology/status-quo-bias.md)). O desenho e o teste de sustentabilidade seguem [`../../frameworks/guarantee-design.md`](../../frameworks/guarantee-design.md): cada promessa da garantia aponta para evidência ([`../../frameworks/proof-to-claim-chain.md`](../../frameworks/proof-to-claim-chain.md)). A força vem da ousadia honrável — uma garantia específica e total reverte risco que a genérica não reverte.

## Padrão reutilizável
Esqueleto em redação original, com placeholders para preencher:

```
[REVERSÃO] Experimente {{produto}} sem risco por {{prazo}}.
[GESTO] Se {{condição_de_satisfação_subjetiva}}, devolvo {{valor_total}} — cada centavo.
[SEM FRICÇÃO] Sem perguntas, sem {{passo_burocrático_removido}}. Basta {{ação_simples_de_pedido}}.
[CONFIANÇA] Posso oferecer isso porque {{prova_da_confiança_no_resultado}}.
```

Antes de publicar: o `unit-economics-stack-analyst` simula o pior caso (X% aciona) contra a margem; o `compliance-auditor` confirma exequibilidade e conformidade. Se quebra o LTV, suba uma condição ou troque para a [condicional](condicional-baseada-em-resultado.md).

## Adaptação por sofisticação
Conforme [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md):
- **Sofisticação 1-2** — a incondicional simples já basta; o mercado ainda confia no claim. "30 dias ou seu dinheiro de volta" converte sozinho.
- **Sofisticação 3** — ligue a garantia ao **mecanismo**: "tão certo é o {{mecanismo}} que devolvo tudo se não funcionar". A garantia vira prova do mecanismo.
- **Sofisticação 4** — eleve o degrau: o público viu garantias demais. Suba para o "melhor que grátis" (devolvo + você fica com o bônus) — ver a [escada](../../frameworks/risk-reversal-ladder.md). A ousadia diferencia.
- **Sofisticação 5** — a garantia migra para **prova social e reputação**: "milhares confiaram; veja por que quase ninguém pede de volta". O peso sai do gesto e vai para a evidência acumulada.

## Fonte
> **Fonte:** Estrutura da garantia incondicional derivada do capítulo de Garantias de Alex Hormozi, *$100M Offers* (2021) — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
