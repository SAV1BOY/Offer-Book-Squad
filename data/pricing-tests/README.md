---
id: data.pricing-tests.readme
title: "Data Store — Testes de Preço (Pricing Tests)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
tags: [pricing, wtp, van-westendorp, gabor-granger, conjoint, data-store]
---

# Data Store — Testes de Preço (Pricing Tests)

## Propósito

Este diretório guarda os **estudos de disposição a pagar (WTP)** que derivam preço de **valor**, nunca de custo. É a base de prova do princípio `price_value_derived` ([`config.yaml`](../../config.yaml) `quality_gates.mandatory`). Cada preço travado numa oferta precisa apontar para um teste aqui — Van Westendorp, Gabor-Granger, conjoint (CBC) ou Kano. Sem método declarado, o gate `pricing/pricing-method-declared-gate` não passa.

A pasta serve `evidence_before_opinion` e `traceability_before_eloquence`: o `pricing-wtp-strategist` mostra a faixa de aceitação, e o `money-model-designer` escolhe o ponto na escada com rastro até o dado.

## O que guardar

- **Estudos de WTP** por oferta (Van Westendorp PSM, Gabor-Granger, conjoint, Kano).
- **Faixa de preço aceitável**, ponto ótimo (OPP), ponto de indiferença (IPP) e os limites (PMC/PME).
- **Amostra e método** (n, como foi perguntado, fonte do painel).
- **Cenários de pacote** (good-better-best) e o efeito decoy testado.

Não guardar aqui: o preço final travado (vai para [`offer-registry`](../registries/offer-registry.md)) nem a decisão de preço (vai para [`decision-registry`](../registries/decision-registry.md)). Aqui fica **a evidência que sustenta** essas duas.

## Formato / Schema

Cada estudo é um `.md` com frontmatter (`type: doc`, `owner_agent: pricing-wtp-strategist`) e seções: método, amostra, dados/curvas, faixa aceitável, ponto recomendado e ligação à decisão. Valores reais citam a fonte do painel; exemplos são marcados como `ilustrativo`. Campos-chave alinham com [`price-test-registry`](../registries/price-test-registry.md): `test_id`, `method`, `price_point`, `acceptance_range`, `sample_size`, `recommended_price`.

## Como alimenta os agentes

- **Escrevem**: `pricing-wtp-strategist` (dono; roda os estudos na tarefa `set-pricing-wtp`).
- **Leem**: `money-model-designer` (escolhe preço por papel na escada), `unit-economics-stack-analyst` (cruza preço com CAC e margem), `value-equation-engineer` (confere que o preço respeita o valor entregue), `offerbook-chief` (DoD de preço derivado).
- **Ligações a registries**: alimenta [`price-test-registry`](../registries/price-test-registry.md) (o registro do teste) e justifica o `price` em [`offer-registry`](../registries/offer-registry.md); a escolha final vira linha em [`decision-registry`](../registries/decision-registry.md).

## Exemplo

Ver [`van-westendorp-example.md`](van-westendorp-example.md) — um estudo Van Westendorp ilustrativo com as quatro perguntas clássicas, curvas de amostra e a faixa de preço aceitável, claramente marcado como exemplo.
