---
id: data.conversion-data.funnel-metrics-template
title: "Snapshot de Funil (EXEMPLO ILUSTRATIVO / Template)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [conversion, funnel, template, example, illustrative]
---

# Snapshot de Funil (EXEMPLO ILUSTRATIVO / Template)

> **AVISO:** Este arquivo é um **template ilustrativo (seed)**. Os volumes e taxas são **fictícios**, só para mostrar o formato. Não use como fato. Cada lançamento real copia este snapshot e preenche com dados de plataforma.

## Propósito

Mostrar como o squad registra o **funil etapa por etapa**, do clique ao upsell. O snapshot responde: onde o lançamento vaza? A coluna de taxa expõe o gargalo. O `funnel-architect` usa isso para corrigir becos sem saída (gate `funnel/funnel-no-dead-end-gate`).

## Identificação

| Campo | Valor (exemplo) |
|---|---|
| caso | Método X (amostra) |
| período | 2026-Q2 |
| canal | vsl-funnel |
| fonte | dashboard da plataforma _(ilustrativo)_ |

## Funil — volume e conversão por etapa (ilustrativo)

| etapa | volume | conversão p/ próxima | meta | observação |
|---|---|---|---|---|
| Cliques no anúncio | 50.000 | 30% | 30% | CTR de mídia (amostra) |
| Visitantes da landing | 15.000 | 38% | 40% | abaixo da meta de optin |
| Optins (lead) | 5.700 | 60% | 65% | comparecimento à VSL |
| Espectadores da VSL | 3.420 | 4,1% | 4% | acima do benchmark de VSL |
| Compras do core | 140 | 22% | 25% | take rate do upsell |
| Aceites de upsell | 31 | — | — | fim do funil de front-end |

> Compare cada taxa com [`benchmarks/conversion-benchmarks-by-industry.md`](../benchmarks/conversion-benchmarks-by-industry.md). Aqui o **gargalo** é optin (38% vs meta 40%) e take rate de upsell (22% vs 25%).

## Coorte (amostra) — por origem de tráfego

| origem | optin | conversão VSL | observação |
|---|---|---|---|
| Tráfego frio (paid social) | 35% | 3,8% | maior volume, menor taxa |
| Lista quente (e-mail) | 55% | 6,2% | menor volume, maior taxa |

## Derivados (alimenta KPIs)

- `opt_in_rate` = optins ÷ visitantes = 38% _(ex.)_.
- `vsl_conversion_rate` = compras ÷ espectadores = 4,1% _(ex.)_.
- `upsell_take_rate` = aceites ÷ compras = 22% _(ex.)_.
- Estes números sobem para o painel em [`metrics/kpi-dashboard-template.md`](../metrics/kpi-dashboard-template.md).

## Ação / decisão disparada

Gargalo de optin e de upsell. Ação: testar nova headline da landing e novo ângulo de upsell. Vira linha em [`decision-registry`](../registries/decision-registry.md) e a peça testada entra em [`control-registry`](../registries/control-registry.md).

## DoD do snapshot

Pronto quando: todas as etapas com volume e taxa medidos, fonte citada, gargalo identificado, derivados calculados e a ação disparada nomeada.
