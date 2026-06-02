---
id: data.pricing-tests.van-westendorp-example
title: "Van Westendorp PSM (EXEMPLO ILUSTRATIVO) — Mentoria 90 Dias"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
tags: [pricing, van-westendorp, psm, wtp, example, illustrative]
---

# Van Westendorp PSM (EXEMPLO ILUSTRATIVO) — Mentoria 90 Dias

> **AVISO:** Este arquivo é um **exemplo ilustrativo (seed)**. Os números são **fictícios**, só para mostrar o método e o formato. Não use como fato. Um estudo real cita a fonte do painel, o n e a data.

## Propósito

Mostrar como o squad registra um estudo de **Van Westendorp (Price Sensitivity Meter / PSM)** para derivar preço de WTP. O PSM faz **quatro perguntas** de preço e cruza as curvas para achar a faixa aceitável e o ponto ótimo. Liga ao framework [`pricing/van-westendorp`](../../frameworks/pricing/van-westendorp.md).

## Método — as quatro perguntas (clássicas)

Pergunta-se, sobre a oferta descrita, a partir de que preço ela seria:

1. **Barata demais** (a ponto de duvidar da qualidade) — "Barato demais".
2. **Uma pechincha** (bom valor) — "Barato".
3. **Começando a ficar cara** (mas ainda consideraria) — "Caro".
4. **Cara demais** (não compraria) — "Caro demais".

## Amostra (ilustrativa)

- **n = 180** respondentes do avatar (mulheres 40+, intenção de compra) — _fonte do painel: ilustrativa_.
- Oferta descrita: Mentoria 90 Dias com mecanismo "equilíbrio hormonal pós-40".
- Período: 2026-Q2 (amostra).

## Dados / pontos de cruzamento (ilustrativos)

| Indicador (PSM) | Definição | Valor (amostra) |
|---|---|---|
| PMC (Point of Marginal Cheapness) | cruzamento "barato demais" × "caro" — piso | ~R$ 1750 |
| OPP (Optimal Price Point) | cruzamento "barato demais" × "caro demais" | ~R$ 2100 |
| IPP (Indifference Price Point) | cruzamento "barato" × "caro" | ~R$ 1950 |
| PME (Point of Marginal Expensiveness) | cruzamento "barato" × "caro demais" — teto | ~R$ 2400 |

> As curvas reais seriam plotadas (% acumulado vs preço). Aqui só listamos os pontos de cruzamento para o seed.

## Faixa de preço aceitável (amostra)

**Faixa de Aceitação (Range of Acceptable Prices):** ~R$ 1750 a ~R$ 2400 (entre PMC e PME).

## Ponto recomendado (amostra)

Recomendação: **R$ 2497** com bônus empilhados, no topo da faixa, porque o valor empilhado e a prova social sustentam o WTP alto. Decisão sobre volume vs margem é do `money-model-designer`.

## Ligação à decisão e ao registro

- Vira linha em [`price-test-registry`](../registries/price-test-registry.md): `test_id: vw-core-exemplo-2026q2`, `method: van-westendorp`, `result_metric: psm-range`, `result_value: R$ 1750-2400`, `optimal_price: R$ 2497`, `confidence: medium`, `status: complete`.
- A escolha do ponto vira [`decision-registry`](../registries/decision-registry.md) (`dec-exemplo-0001`).
- Justifica o `price` em [`offer-registry`](../registries/offer-registry.md) (`core-exemplo-90d`).

## Cross-refs

- Framework: [`pricing/van-westendorp`](../../frameworks/pricing/van-westendorp.md), [`pricing/gabor-granger`](../../frameworks/pricing/gabor-granger.md).
- README da pasta: [`README.md`](README.md).
