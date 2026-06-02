---
id: data.backlog.readme
title: "Data Store — Backlog de Melhoria (Kaizen)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [backlog, kaizen, improvement, lessons-learned, roi, intake, data-store]
---

# Data Store — Backlog de Melhoria (Kaizen)

## Propósito

Este diretório guarda o **backlog de melhoria contínua (Kaizen)** — a fila priorizada de tudo que o squad aprendeu e quer melhorar no próximo ciclo. Cada item nasce de uma lição de um lançamento e morre quando vira melhoria entregue. É a ponte entre "o que deu errado desta vez" e "o que fazemos diferente da próxima": o backlog **alimenta o próximo intake**.

A pasta serve `memory_before_repetition`: a lição registrada não fica num relatório morto, vira item acionável com ROI e dono. O `knowledge-librarian` cura o backlog a partir do [`lessons-learned-registry`](../registries/lessons-learned-registry.md); o `offerbook-chief` puxa daqui as melhorias prioritárias quando abre o próximo lançamento.

## O que guardar

- **Backlog de melhoria** (`improvement-backlog-<periodo>.md`, copiado do template): uma linha por item, priorizada.
- **A origem de cada item**: qual lição ou lançamento o gerou (link ao [`lessons-learned-registry`](../registries/lessons-learned-registry.md)).
- **O estado de cada item**: da ideia ao entregue, com o dono.

Não guardar aqui: a lição crua em si (essa vive no [`lessons-learned-registry`](../registries/lessons-learned-registry.md)) nem a decisão que adota a melhoria (essa vive no [`decision-registry`](../registries/decision-registry.md)). Esta pasta é sobre **a fila de melhorias priorizada**: o que mexer no próximo ciclo, em que ordem e por que.

## Formato / Schema

O backlog é um `.md` com tabela de colunas fixas: `item`, `origem`, `ROI estimado`, `prioridade`, `dono`, `status`. A coluna `origem` aponta para a lição ou o lançamento que gerou o item (link ao [`lessons-learned-registry`](../registries/lessons-learned-registry.md)). O `dono` usa ids de agente de [`config.yaml`](../../config.yaml). A prioridade ordena a fila; o ROI estimado a justifica.

## Como alimenta os agentes

- **Escrevem**: `knowledge-librarian` (cura e prioriza o backlog na tarefa `memory-update`), `offerbook-chief` (prioridade e adoção no próximo intake); qualquer agente que registra uma lição propõe o item de melhoria.
- **Leem**: `offerbook-chief` (puxa as melhorias prioritárias no `intake-and-scope`), todos os agentes-dono (executam a melhoria que lhes cabe), `knowledge-librarian` (consolida no Blackbook).
- **Ligações a registries**: cada item liga à sua origem no [`lessons-learned-registry`](../registries/lessons-learned-registry.md); a melhoria adotada vira decisão no [`decision-registry`](../registries/decision-registry.md) e pode promover um padrão para [`winners/`](../winners/).

## Exemplo

Ver [`improvement-backlog-template.md`](improvement-backlog-template.md) — um backlog ilustrativo com itens de melhoria, a lição de origem, o ROI estimado e a prioridade, marcado como exemplo.
