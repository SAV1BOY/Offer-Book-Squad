---
id: data.registry.price-test-registry
title: "Registro de Testes de Preço"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [pricing-wtp-strategist, unit-economics-stack-analyst, money-model-designer]
read_agents: [money-model-designer, value-equation-engineer, offerbook-chief, compliance-auditor, vsl-webinar-scriptwriter]
tags: [price, wtp, pricing-test, van-westendorp, economics, registry]
---

# Registro de Testes de Preço

## Propósito

Esta é a **memória de todo teste de preço** — o método usado, o ponto medido e o resultado. O preço **deriva de valor/WTP, nunca de custo** (`value_equation_test` + princípio de preço). Cada teste registra **qual método** ([Van Westendorp](../../frameworks/pricing/van-westendorp.md), [Gabor-Granger](../../frameworks/pricing/gabor-granger.md), [conjoint](../../frameworks/pricing/conjoint-cbc.md), [Kano](../../frameworks/pricing/kano-model.md)), **o número que saiu** e **a decisão de preço** que ele sustenta.

O registro garante `traceability_before_eloquence`: todo preço de uma oferta aponta para um método declarado e um resultado, não para um chute. Alimenta o [`offer-registry`](offer-registry.md) (`price` + `price_basis`) e fecha o gate `pricing/pricing-method-declared-gate`.

## Schema

O método vem dos frameworks de [`pricing/`](../../frameworks/pricing/). O `offer_id` referencia [`offer-registry`](offer-registry.md).

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `test_id` | string (slug) | `kebab-case` único, ex.: `vw-core-2025q2` | Sim |
| `offer_id` | ref | id em [`offer-registry`](offer-registry.md) | Sim |
| `method` | enum | `van-westendorp` \| `gabor-granger` \| `conjoint-cbc` \| `maxdiff` \| `kano` \| `price-elasticity` \| `ab-price-split` \| `value-based` | Sim |
| `price_point_tested` | money | número + moeda, ex.: `R$ 1997` | Sim |
| `sample_size` | int | n de respondentes/sessões | Não |
| `result_metric` | enum | `opt-in-rate` \| `conversion-rate` \| `aov` \| `take-rate` \| `psm-range` \| `revenue-per-visitor` | Sim |
| `result_value` | number/string | valor medido (ex.: `3.2%`, `R$ 1750-2100`) | Sim |
| `optimal_price` | money | preço recomendado pelo teste | Não |
| `wtp_basis` | enum | `value-based` \| `wtp-survey` \| `anchor` \| `competitive` | Sim |
| `confidence` | enum | `low` \| `medium` \| `high` (robustez da amostra) | Sim |
| `status` | enum | `planned` \| `running` \| `complete` \| `inconclusive` \| `adopted` | Sim |
| `owner_agent` | agent-id | id real de [`config.yaml`](../../config.yaml) | Sim |
| `decided_in` | ref | id em [`decision-registry`](decision-registry.md) | Não |
| `updated` | ISO date | `YYYY-MM-DD` | Sim |

## Quem escreve / Quem lê

**Escrevem**:
- `pricing-wtp-strategist` — dono do registro; declara `method`, roda o teste e registra `result_value` + `optimal_price` (tarefa `set-pricing-wtp`, gate `pricing/pricing-method-declared-gate`).
- `unit-economics-stack-analyst` — cruza o preço com LTV:CAC e payback; marca `status: adopted` quando o número fecha a economia.
- `money-model-designer` — registra testes de preço por degrau da escada (atração vs core vs upsell).

**Leem**: `money-model-designer` e `value-equation-engineer` (preço por papel na sequência), `vsl-webinar-scriptwriter` (ancora o preço com o resultado do teste), `compliance-auditor` (preço anunciado bate com o testado) e `offerbook-chief` no DoD.

## Registros

| test_id | offer_id | method | price_point_tested | sample_size | result_metric | result_value | optimal_price | wtp_basis | confidence | status | owner_agent | decided_in | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `vw-exemplo-2025q2` _(EXEMPLO ILUSTRATIVO — apagar)_ | `core-exemplo-90d` | van-westendorp | R$ 1997 | 120 | psm-range | R$ 1750-2400 | R$ 2200 | wtp-survey | medium | complete | pricing-wtp-strategist | `dec-exemplo-0001` | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo, marcada como (EXEMPLO ILUSTRATIVO). Os agentes apagam o exemplo e escrevem registros reais. -->
