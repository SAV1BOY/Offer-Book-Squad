---
id: data.conversion-data.readme
title: "Data Store — Dados de Conversão (Funil)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [conversion, funnel, raw-data, metrics, data-store]
---

# Data Store — Dados de Conversão (Funil)

## Propósito

Este diretório guarda os **dados crus do funil** — o número medido em cada etapa, do clique à compra ao upsell. É a matéria-prima dos KPIs de conversão. Diferente de [`metrics/`](../metrics/) (que **agrega** os KPIs num painel) e de [`benchmarks/`](../benchmarks/) (que guarda **padrões externos**), aqui ficam os **números brutos do nosso funil**, etapa por etapa, por lançamento.

A pasta serve `decision_before_ornament`: o funil mostra **onde** o lançamento vaza, e isso dispara a decisão de corrigir. O `funnel-architect` lê para achar o gargalo. Os escritores de copy leem para saber qual etapa melhorar. O `unit-economics-stack-analyst` cruza com o CAC.

## O que guardar

- **Snapshots de funil** por lançamento (ex.: `funnel-metodo-x-2026q2.md`): volume e taxa por etapa.
- **Dados por etapa**: visitantes, optins, espectadores de VSL, compras, upsells, taxa de fechamento de carrinho.
- **Dados de coorte** (conversão por origem de tráfego, por dia da janela de carrinho).
- Cada número com **período**, **fonte** (plataforma/dashboard) e nota se é parcial.

Não guardar aqui: o painel agregado de KPIs (vai para [`metrics/`](../metrics/)) nem os benchmarks de indústria (vão para [`benchmarks/`](../benchmarks/)). Aqui é o **dado bruto** que alimenta os dois.

## Formato / Schema

Cada snapshot é um `.md` com frontmatter (`type: doc`) e uma tabela de funil com colunas fixas: `etapa`, `volume`, `taxa de conversão` (para a próxima etapa), `meta`, `fonte`, `período`. As etapas seguem o pipeline de funil ([`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md)). Todo número cita a fonte (plataforma) ou é marcado como `ilustrativo`.

## Como alimenta os agentes

- **Escrevem**: `funnel-architect` (mapeia e registra o funil), `knowledge-librarian` (consolida), com aporte de dados de plataforma do cliente.
- **Leem**: `funnel-architect` (gargalo e becos sem saída — gate `funnel/funnel-no-dead-end-gate`), `vsl-webinar-scriptwriter` e `email-sms-sequence-writer` (etapa a melhorar), `unit-economics-stack-analyst` (CAC, payback, take rate de upsell), `offerbook-chief` (saúde do lançamento).
- **Ligações a registries**: alimenta os KPIs de conversão em [`metrics/`](../metrics/); o `metric_value` de [`control-registry`](../registries/control-registry.md) vem destes dados; gargalos viram decisão em [`decision-registry`](../registries/decision-registry.md).

## Exemplo

Ver [`funnel-metrics-template.md`](funnel-metrics-template.md) — um snapshot de funil ilustrativo, do clique ao upsell, com taxas de amostra e a nota de que os valores são exemplos.
