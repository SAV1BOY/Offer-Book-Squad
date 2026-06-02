---
id: data.metrics.kpi-dashboard-template
title: "Painel de KPIs (EXEMPLO ILUSTRATIVO / Template)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [metrics, kpi, dashboard, template, example, illustrative]
---

# Painel de KPIs (EXEMPLO ILUSTRATIVO / Template)

> **AVISO:** Este arquivo é um **template ilustrativo (seed)**. Os valores de "meta" e "realizado" são **fictícios**, só para mostrar o formato. Não use como fato. Cada lançamento real copia este painel e preenche com números medidos e fonte.

## Propósito

Este painel agrega as **cinco famílias de KPI** definidas em [`config.yaml`](../../config.yaml) (`kpis:`) num só lugar. Ele responde a uma pergunta simples: a máquina de oferta está forte e o lançamento converte? O `offerbook-chief` lê o painel para aprovar o DoD e priorizar. O `unit-economics-stack-analyst` cruza a família de economia com o preço. Cada número aqui sustenta uma decisão — nunca enfeite.

## O que guardar

- Um painel por lançamento ou período (ex.: `kpi-snapshot-metodo-x-2026q2.md`, copiado deste template).
- Para cada KPI: a **definição/fórmula**, a **meta**, o **realizado**, a **fonte** e o **período**.
- A coluna `fonte` aponta para o registro ou o dado cru de origem (ex.: [`conversion-data/`](../conversion-data/), [`data/registries/`](../registries/)).

## Formato / Schema

Tabela com colunas fixas: `kpi`, `família`, `definição/fórmula`, `meta`, `realizado`, `fonte`, `período`, `updated`. As famílias e KPIs seguem `config.yaml`.

| kpi | família | definição/fórmula | meta | realizado | fonte | período | updated |
|---|---|---|---|---|---|---|---|
| value_equation_score | offer_quality | nota 0-100 da Value Equation | ≥80 | 82 _(ex.)_ | [`offer-registry`](../registries/offer-registry.md) | 2026-Q2 | 2026-06-02 |
| money_model_completeness | offer_quality | nº de partes da escada (alvo 4) | 4 | 3 _(ex.)_ | [`offer-registry`](../registries/offer-registry.md) | 2026-Q2 | 2026-06-02 |
| proof_coverage_rate | offer_quality | % de claims com prova ligada | 100% | 90% _(ex.)_ | [`claim-registry`](../registries/claim-registry.md) | 2026-Q2 | 2026-06-02 |
| big_idea_strength | offer_quality | nota dos 5 critérios da Big Idea | ≥4/5 | 4/5 _(ex.)_ | [`big-idea-registry`](../registries/big-idea-registry.md) | 2026-Q2 | 2026-06-02 |
| opt_in_rate | conversion | optins / visitantes | ≥40% | 38% _(ex.)_ | [`conversion-data/`](../conversion-data/) | 2026-Q2 | 2026-06-02 |
| vsl_conversion_rate | conversion | vendas / espectadores VSL | ≥4% | 4.1% _(ex.)_ | [`control-registry`](../registries/control-registry.md) | 2026-Q2 | 2026-06-02 |
| upsell_take_rate | conversion | aceites / ofertas de upsell | ≥25% | 22% _(ex.)_ | [`conversion-data/`](../conversion-data/) | 2026-Q2 | 2026-06-02 |
| aov | conversion | receita / nº de pedidos | R$ 3000 | R$ 2890 _(ex.)_ | [`conversion-data/`](../conversion-data/) | 2026-Q2 | 2026-06-02 |
| cart_close_lift | conversion | lift na janela de fechamento | +30% | +28% _(ex.)_ | [`control-registry`](../registries/control-registry.md) | 2026-Q2 | 2026-06-02 |
| cac | economics | gasto de mídia / clientes novos | ≤R$ 600 | R$ 640 _(ex.)_ | [`conversion-data/`](../conversion-data/) | 2026-Q2 | 2026-06-02 |
| ltv_cac_ratio | economics | LTV ÷ CAC | ≥3:1 | 2.8:1 _(ex.)_ | [`conversion-data/`](../conversion-data/) | 2026-Q2 | 2026-06-02 |
| payback_period | economics | meses para recuperar o CAC | ≤2 meses | 2.3 meses _(ex.)_ | [`conversion-data/`](../conversion-data/) | 2026-Q2 | 2026-06-02 |
| front_end_cac_liquidation | economics | % do CAC pago pela atração | ≥100% | 95% _(ex.)_ | [`offer-registry`](../registries/offer-registry.md) | 2026-Q2 | 2026-06-02 |
| time_to_offer_book | efficiency | dias até o Offer Book passar no DoD | ≤10 dias | 12 dias _(ex.)_ | [`decision-registry`](../registries/decision-registry.md) | 2026-Q2 | 2026-06-02 |
| time_to_blackbook | efficiency | dias até o Blackbook completo | ≤25 dias | 27 dias _(ex.)_ | [`decision-registry`](../registries/decision-registry.md) | 2026-Q2 | 2026-06-02 |
| copy_throughput | efficiency | peças de copy aprovadas / semana | ≥12 | 10 _(ex.)_ | [`control-registry`](../registries/control-registry.md) | 2026-Q2 | 2026-06-02 |
| registry_currency | operational | % de registros atualizados ≤7 dias | 100% | 92% _(ex.)_ | [`data/registries/`](../registries/) | 2026-Q2 | 2026-06-02 |
| swipe_reuse_rate | operational | % de peças que reusam um swipe | ≥50% | 45% _(ex.)_ | [`swipe-registry`](../registries/swipe-registry.md) | 2026-Q2 | 2026-06-02 |
| compliance_pass_rate | operational | % de peças aprovadas sem veto | ≥95% | 97% _(ex.)_ | [`decision-registry`](../registries/decision-registry.md) | 2026-Q2 | 2026-06-02 |
| lessons_learned_frequency | operational | lições registradas / lançamento | ≥5 | 6 _(ex.)_ | [`lessons-learned-registry`](../registries/lessons-learned-registry.md) | 2026-Q2 | 2026-06-02 |

## Como alimenta os agentes

- **Escrevem**: `knowledge-librarian` (consolida o painel no Blackbook), `unit-economics-stack-analyst` (família economics), `offerbook-chief` (metas e offer_quality).
- **Leem**: `offerbook-chief` (priorização e DoD), `money-model-designer` (saúde da escada via take rate e AOV), `funnel-architect` e os escritores de copy (conversão por etapa).
- **Ligações a registries**: cada KPI puxa de um registro nomeado na coluna `fonte` — o painel é a leitura agregada de [`data/registries/`](../registries/) e [`conversion-data/`](../conversion-data/).

## Exemplo

A tabela acima já é o exemplo preenchido. Para um lançamento real, copie o arquivo, renomeie para `kpi-snapshot-<caso>-<periodo>.md`, apague o aviso e substitua cada `_(ex.)_` por um número medido com fonte. Compare meta vs realizado e marque em vermelho o que não bateu — esse é o gatilho de decisão do `offerbook-chief`.
