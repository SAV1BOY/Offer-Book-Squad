---
id: data.winners.readme
title: "Data Store — Winners (Padrões de Ouro)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [winners, gold-standard, swipe, control, data-store]
---

# Data Store — Winners (Padrões de Ouro)

## Propósito

Este diretório guarda os **padrões de ouro do squad** — os vencedores que provaram valor mais de uma vez e viraram referência reutilizável. Se [`controls/`](../controls/) é a lista de campeões do teste corrente, **winners** é o **hall da fama**: as ofertas, Big Ideas e peças que o squad reusa por padrão porque ganharam de forma consistente. É a expressão máxima de `memory_before_repetition`.

A pasta existe para acelerar o próximo lançamento: antes de criar do zero, o squad consulta o que já é ouro. O `knowledge-librarian` cura esta lista; os escritores de copy e o `big-idea-architect` puxam daqui o ponto de partida.

## O que guardar

- **Índice de winners** (`winners-index.md`): a tabela-mestre dos padrões de ouro, ranqueada.
- **Ofertas vencedoras** (Money Models que liquidaram CAC com folga).
- **Big Ideas vencedoras** (teses que converteram em mais de um canal).
- **Padrões de copy** vencedores (sem copy literal — ver [`swipe/`](../../swipe/) para o padrão abstraído).

Não guardar aqui: o campeão do teste corrente (fica em [`controls/`](../controls/)) nem copy literal de terceiros (proibido — ver [`docs/compliance-policy.md`](../../docs/compliance-policy.md)).

## Formato / Schema

`winners-index.md` é uma tabela com: `winner_id`, `tipo` (oferta/big-idea/control/swipe), `título`, `métrica de prova`, `reusos`, `fonte` (link ao control/registro de origem), `status`, `updated`. Vencedores de copy ligam ao padrão original em [`swipe-registry`](../registries/swipe-registry.md), nunca à cópia literal.

## Como alimenta os agentes

- **Escrevem**: `knowledge-librarian` (promove e mantém o ranking na tarefa `memory-update`).
- **Leem**: `vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `ad-creative-factory` (ponto de partida de copy), `big-idea-architect` (teses que já ganharam), `money-model-designer` (escadas que liquidaram CAC), `offerbook-chief` (o que escalar).
- **Ligações a registries**: cruza [`control-registry`](../registries/control-registry.md) (origem do vencedor), [`offer-registry`](../registries/offer-registry.md) (ofertas de ouro), [`big-idea-registry`](../registries/big-idea-registry.md) e [`swipe-registry`](../registries/swipe-registry.md) (padrões reutilizáveis).

## Exemplo

Ver [`winners-index.md`](winners-index.md) — o índice-mestre ilustrativo de padrões de ouro, com uma linha de exemplo marcada como amostra.
