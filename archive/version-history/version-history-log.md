---
id: archive.version-history.version-history-log
title: "Log — Histórico de Versões"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
registries: [data.registry.decision-registry, data.registry.lessons-learned-registry]
tags: [version-history, changelog, log, traceability, memory]
---

# Log — Histórico de Versões

## Propósito

Este é o **log central de versões** dos artefatos do squad. Cada linha registra uma mudança material — um salto de semver — numa oferta, Big Idea, control, money model ou template. O `knowledge-librarian` adiciona uma linha sempre que uma peça muda de comportamento ou estratégia. O resultado é uma linha do tempo auditável: qualquer sessão reconstrói a evolução de um artefato só lendo este arquivo. Sem ele, o time perde o porquê das mudanças e refaz experimentos já feitos.

O log não copia o conteúdo das versões; ele aponta para a decisão que disparou a mudança e para o registry onde a peça vive. Isto cumpre `traceability_before_eloquence`: a rastreabilidade vem antes da beleza. Mudanças cosméticas não entram — só o que altera o comportamento da peça.

## O que arquivar

Uma linha por mudança material. Inclua o `artifact_id`, o salto de versão (`de` → `para`), o tipo de mudança, o motivo em uma frase, o link para a decisão e a data. Não registre typos nem formatação.

## Formato / Template

A tabela abaixo é o log. O schema das colunas: `artifact_id` (slug), `tipo` (offer/big-idea/control/money-model/template), `versão de`, `versão para`, `mudança` (added/changed/deprecated/fixed), `motivo`, `decisão` (id), `data` (ISO). A tabela está **semeada vazia**: a linha abaixo é um exemplo ilustrativo e deve ser apagada quando o log real começar.

| artifact_id | tipo | versão de | versão para | mudança | motivo | decisão | data |
|---|---|---|---|---|---|---|---|
| `core-exemplo-90d` _(EXEMPLO ILUSTRATIVO — apagar)_ | offer | 2.2 | 2.3 | changed | ajuste de preço após teste de WTP | `dec-exemplo-0001` | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo, marcada como (EXEMPLO ILUSTRATIVO). O knowledge-librarian apaga o exemplo e escreve registros reais. -->

## Lições para reuso

Quando o mesmo artefato sobe várias versões pelo mesmo motivo, isso vira lição no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md): o diagnóstico inicial pode ter falhado. Uma versão nova que perde para a antiga liga à autópsia em [`losing-controls/`](../losing-controls/README.md). O log é matéria-prima de padrão, não só registro morto.

## Liga com

- [`decision-registry`](../../data/registries/decision-registry.md) — a decisão por trás de cada salto.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — onde padrões de versão viram lição.
- [`losing-controls/`](../losing-controls/README.md) — quando uma versão nova regrediu.
- [`README.md`](README.md) — visão da pasta.
