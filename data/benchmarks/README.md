---
id: data.benchmarks.readme
title: "Data Store — Benchmarks de Indústria"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [benchmarks, conversion, industry, reference, data-store]
---

# Data Store — Benchmarks de Indústria

## Propósito

Este diretório guarda os **números de referência do mercado** — as médias de conversão, abertura, comparecimento e abandono por indústria que dizem se o nosso resultado está acima, na média ou abaixo. Diferente de [`metrics/`](../metrics/) (que rastreia **os nossos** números) e de [`conversion-data/`](../conversion-data/) (que guarda **dados crus do nosso funil**), aqui ficam os **padrões externos** contra os quais comparamos. Um benchmark transforma "4,1% de conversão" de número solto em "acima da média da indústria".

A pasta serve `evidence_before_opinion`: a meta de um KPI não nasce de palpite, nasce de um piso de mercado. O `pricing-wtp-strategist` e o `unit-economics-stack-analyst` calibram metas com estes números. O `offerbook-chief` usa o benchmark para julgar se um control é forte o bastante.

## O que guardar

- **Benchmarks de conversão por indústria** (landing page, VSL, webinar, e-mail, checkout).
- **Benchmarks de economia** (LTV:CAC, payback) por modelo de negócio, quando houver fonte.
- **Benchmarks de canal** (CTR de mídia paga, EPC de afiliados).
- Cada benchmark com **faixa**, **fonte (URL + data de acesso)** e nota sobre a metodologia (n, amostra, ano).

Não guardar aqui: metas internas (vão para [`metrics/`](../metrics/)) nem resultados de teste do squad (vão para [`controls/`](../controls/) e [`winners/`](../winners/)).

## Formato / Schema

Cada arquivo é um `.md` com frontmatter (`type: doc`) e tabelas por categoria. Toda linha de número **cita fonte** (bloco de citação ou link inline) ou é marcada como `aproximado/ilustrativo`. Colunas típicas: `categoria`, `métrica`, `faixa típica`, `mediana/média`, `fonte`, `ano`, `observação`. Regra dura: **não inventar cifra precisa como fato** — citar ou marcar como estimativa.

## Como alimenta os agentes

- **Escrevem**: `knowledge-librarian` (cura e cita fontes), com aporte do squad **DeepResearch** (`cross_squad.deepresearch_squad`, ver [`config.yaml`](../../config.yaml)).
- **Leem**: `pricing-wtp-strategist` (sanidade de preço/conversão), `unit-economics-stack-analyst` (pisos de LTV:CAC e payback), `funnel-architect` (metas de etapa), `vsl-webinar-scriptwriter` e `email-sms-sequence-writer` (metas de conversão e abertura), `offerbook-chief` (força de control).
- **Ligações a registries**: o benchmark contextualiza o `metric_value` de [`control-registry`](../registries/control-registry.md) e as metas espelhadas em [`metrics/`](../metrics/).

## Exemplo

Ver [`conversion-benchmarks-by-industry.md`](conversion-benchmarks-by-industry.md) — uma tabela de benchmarks de conversão por indústria com **fontes reais citadas** (Baymard, ON24, MailerLite, First Page Sage e outros), mostrando o padrão de citação esperado.
