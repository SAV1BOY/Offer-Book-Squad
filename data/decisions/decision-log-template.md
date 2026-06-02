---
id: data.decisions.decision-log-template
title: "Log de Decisão (EXEMPLO ILUSTRATIVO / Template)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [decisions, adr, template, example, illustrative]
---

# Log de Decisão (EXEMPLO ILUSTRATIVO / Template)

> **AVISO:** Este arquivo é um **template ilustrativo (seed)**. A decisão e os números são **fictícios**, só para mostrar o formato. Não use como fato. Cada decisão real copia este log e preenche.

## Propósito

Mostrar o **log narrativo** de uma decisão grande — a versão longa da linha que vive em [`decision-registry`](../registries/decision-registry.md). O log existe para que qualquer sessão futura entenda **por que** o squad escolheu o que escolheu, qual caminho rejeitou e o que aceitou de risco.

## Identificação

| Campo | Valor (exemplo) |
|---|---|
| `decision_id` | `dec-exemplo-0001` |
| `title` | Preço do core em R$ 2497 (amostra) |
| `decision_type` | pricing |
| `made_by` | money-model-designer |
| `vetoed_by` | — |
| `reversible` | true |
| `status` | decided |

## Contexto

O estudo Van Westendorp (ver [`pricing-tests/van-westendorp-example.md`](../pricing-tests/van-westendorp-example.md)) deu faixa aceitável de ~R$ 1750 a ~R$ 2400. Precisávamos travar o preço do core para liberar copy e funil. A pergunta: volume ou margem?

## Opção escolhida

**R$ 2497 com bônus empilhados** — no topo da faixa, com valor empilhado para sustentar o WTP alto.

## Alternativas (o caminho não tomado)

- **R$ 1997 sem bônus** — mais volume, menos margem por venda.
- **R$ 1750 (piso PMC)** — maximiza volume, mas corrói margem e sinaliza "barato demais".

## Racional / evidência

WTP no topo da faixa do PSM, somado ao valor empilhado e à prova social com o avatar (mulheres 40+). A [Value Equation](../../frameworks/value-equation.md) sustenta o preço: o resultado dos sonhos é alto e a probabilidade percebida sobe com a prova.

## Trade-off (risco aceito)

Menos volume de vendas, mais margem por venda. Aceita-se converter um pouco menos para liquidar o CAC com folga. Risco: se o comparecimento cair, o volume menor pesa — mitigado pela recuperação de carrinho.

## Reversibilidade & status

Reversível: dá para testar R$ 1997 num split de preço (`ab-price-split`) sem custo de produto. Status: `decided`; revisitar se a conversão ficar abaixo do benchmark (ver [`benchmarks/`](../benchmarks/)).

## Ligação ao índice e aos registros

- Linha-resumo em [`decision-registry`](../registries/decision-registry.md) (`dec-exemplo-0001`).
- `linked_registry`: [`offer-registry`](../registries/offer-registry.md) (`core-exemplo-90d`), [`price-test-registry`](../registries/price-test-registry.md) (`vw-core-exemplo-2026q2`).

## DoD do log

Pronto quando: contexto, opção escolhida, ≥2 alternativas, evidência citada, trade-off explícito, quem decidiu/vetou, e ligação à linha do registro.
