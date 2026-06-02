---
id: data.scorecards.readme
title: "Data Store — Scorecards de Qualidade por Lançamento"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [scorecard, quality, gold, sota, gating, offer-quality, data-store]
---

# Data Store — Scorecards de Qualidade por Lançamento

## Propósito

Este diretório guarda os **scorecards de qualidade por lançamento** — o placar que transforma "a oferta está boa?" num número auditável de 0 a 100 e num veredito (WEAK/GOOD/GOLD/SOTA). Cada lançamento ganha o seu scorecard, copiado do template, com a nota por dimensão e a evidência que sustenta a nota. É o registro vivo de quão forte é a fundação antes de virar copy.

A pasta serve `decision_before_ornament`: cada nota existe para sustentar uma decisão de seguir ou voltar para a oficina. O scorecard **não substitui** os checklists específicos — ele os resume num placar de decisão. A régua de cálculo, os pesos por dimensão e a porteira de escassez vêm do [`offer-quality-scorecard-checklist`](../../checklists/offer-quality-scorecard-checklist.md), que é a autoridade da pontuação. As famílias de KPI que o placar agrega vêm de [`config.yaml`](../../config.yaml) (`kpis: offer_quality` e `quality_gates`).

## O que guardar

- **Scorecards por lançamento** (ex.: `scorecard-metodo-x-2026q2.md`, copiado do template): a nota por dimensão, a evidência e o veredito.
- **Reentradas**: quando uma dimensão volta para a oficina e é repontuada, a nova nota fica aqui, com a data.
- **O veredito final** (WEAK/GOOD/GOLD/SOTA) que o `offerbook-chief` assina e leva ao DoD.

Não guardar aqui: os números brutos de funil (vão para [`conversion-data/`](../conversion-data/)) nem o painel de KPIs por período (vai para [`metrics/`](../metrics/)). Esta pasta é sobre **o placar de qualidade da oferta**, não sobre a telemetria do lançamento.

## Formato / Schema

Cada scorecard é um `.md` com frontmatter (`type: template` no seed; o lançamento real copia e mantém o tipo) e uma tabela com colunas fixas: `dimensão`, `score 0-100`, `gate`, `evidência`, `verdict`. Os pesos por dimensão (equação de valor 30, money model 25, prova 20, Big Idea 15, escassez verdadeira 10) e a régua de gating (total ≥ 80, nenhuma dimensão < 60% do peso, escassez verdadeira sem penalidade) seguem o [`offer-quality-scorecard-checklist`](../../checklists/offer-quality-scorecard-checklist.md). Os limiares de veredito: **GOLD ≥ 95, SOTA ≥ 98** (abaixo de 80 = WEAK; 80–94 = GOOD).

## Como alimenta os agentes

- **Escrevem**: `offerbook-chief` (calcula e assina o veredito, tarefa `assemble-offer-book`), `knowledge-librarian` (consolida o scorecard na memória/Blackbook), com co-assinatura do `value-equation-engineer` e do `compliance-auditor` nas dimensões de valor e de escassez/prova.
- **Leem**: `offerbook-chief` (libera ou segura a copy no DoD), `money-model-designer` (saúde da espinha), `big-idea-architect` (força da tese), os escritores de copy (só começam com a fundação aprovada).
- **Ligações a registries**: a nota final é gravada como decisão no [`decision-registry`](../registries/decision-registry.md); as dimensões puxam de [`offer-registry`](../registries/offer-registry.md), [`big-idea-registry`](../registries/big-idea-registry.md), [`claim-registry`](../registries/claim-registry.md) e [`proof-registry`](../registries/proof-registry.md).

## Exemplo

Ver [`launch-scorecard-template.md`](launch-scorecard-template.md) — um scorecard ilustrativo por lançamento, com a tabela de dimensões pontuadas, a evidência por linha e o veredito de amostra, marcado como exemplo.
