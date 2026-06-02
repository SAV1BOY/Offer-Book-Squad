---
id: data.metrics.readme
title: "Data Store — Métricas & KPIs"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [metrics, kpi, dashboard, offer-quality, conversion, economics, data-store]
---

# Data Store — Métricas & KPIs

## Propósito

Este diretório guarda os **KPIs vivos do squad** — os números que dizem se a oferta é forte e se o lançamento converte. As cinco famílias de KPI vêm de [`config.yaml`](../../config.yaml) (`kpis:`): qualidade de oferta, conversão, economia, eficiência e operação. Aqui ficam os **dashboards e snapshots** que rastreiam esses números ao longo do tempo.

A pasta serve `decision_before_ornament`: cada métrica existe para sustentar uma decisão. O `offerbook-chief` lê estes painéis para aprovar o DoD e priorizar. O `unit-economics-stack-analyst` cruza os números de economia com o preço. Sem métrica, não há prova de que a máquina funciona.

## O que guardar

- **Snapshots de KPI** por lançamento ou período (ex.: `kpi-snapshot-metodo-x-2026q2.md`).
- **Dashboards** que agregam os KPIs das cinco famílias do config.
- **Definições de métrica** (como cada número é calculado, qual a fórmula, qual a fonte).
- **Metas vs realizado** por KPI.

Não guardar aqui: dados de funil crus (vão para [`conversion-data/`](../conversion-data/)) nem benchmarks de indústria (vão para [`benchmarks/`](../benchmarks/)). Esta pasta é sobre **os nossos números**.

## Formato / Schema

Dashboards usam tabela com colunas fixas: `kpi`, `família`, `definição/fórmula`, `meta`, `realizado`, `fonte`, `período`, `updated`. As cinco famílias e seus KPIs seguem `config.yaml`:

- `offer_quality`: value_equation_score, money_model_completeness, proof_coverage_rate, big_idea_strength
- `conversion`: opt_in_rate, vsl_conversion_rate, upsell_take_rate, aov, cart_close_lift
- `economics`: cac, ltv_cac_ratio, payback_period, front_end_cac_liquidation
- `efficiency`: time_to_offer_book, time_to_blackbook, copy_throughput
- `operational`: registry_currency, swipe_reuse_rate, compliance_pass_rate, lessons_learned_frequency

## Como alimenta os agentes

- **Escrevem**: `knowledge-librarian` (consolida o dashboard na memória/Blackbook), `unit-economics-stack-analyst` (KPIs de economia), `offerbook-chief` (metas e qualidade de oferta).
- **Leem**: `offerbook-chief` (priorização e DoD), `money-model-designer` (saúde da sequência), `funnel-architect` e os escritores de copy (conversão por etapa).
- **Ligações a registries**: `registry_currency` audita a atualidade de [`data/registries/`](../registries/); `swipe_reuse_rate` puxa de [`swipe-registry`](../registries/swipe-registry.md); `compliance_pass_rate` puxa de [`decision-registry`](../registries/decision-registry.md).

## Exemplo

Ver [`kpi-dashboard-template.md`](kpi-dashboard-template.md) — um painel ilustrativo com as cinco famílias de KPI, metas de amostra e a nota de que os valores são exemplos.
