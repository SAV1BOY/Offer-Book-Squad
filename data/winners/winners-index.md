---
id: data.winners.winners-index
title: "Índice de Winners (EXEMPLO ILUSTRATIVO / Padrões de Ouro)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [winners, gold-standard, index, example, illustrative]
---

# Índice de Winners (EXEMPLO ILUSTRATIVO / Padrões de Ouro)

> **AVISO:** Este arquivo é um **índice ilustrativo (seed)**. A linha de exemplo é **fictícia**, só para mostrar o formato. Não use como fato. O `knowledge-librarian` apaga o exemplo e ranqueia vencedores reais.

## Propósito

Esta é a **tabela-mestre dos padrões de ouro** — o hall da fama do squad. Lista, ranqueado por prova, o que ganhou de forma consistente e vira ponto de partida do próximo lançamento. Um winner só entra aqui depois de provar valor em teste (origem em [`controls/`](../controls/)) e, de preferência, em mais de um canal ou caso.

## O que guardar

Uma linha por padrão de ouro. Tipos aceitos: `oferta`, `big-idea`, `control` (peça de copy), `swipe` (padrão de copy abstraído). Cada linha liga à origem (control/registro) e conta quantas vezes foi reusada.

## Critério de entrada (para virar "ouro")

1. Venceu em teste com métrica medida e fonte.
2. Bateu um control anterior (lift positivo) **ou** liquidou CAC com folga.
3. Reusado com sucesso ≥1 vez **ou** validado em ≥2 canais/casos.
4. Rastreável: claims ligados à prova, sem copy literal de terceiros.

## Índice

| winner_id | tipo | título | métrica de prova | reusos | fonte | status | updated |
|---|---|---|---|---|---|---|---|
| `win-exemplo-vsl-01` _(EXEMPLO ILUSTRATIVO — apagar)_ | control | VSL Método X v3 (amostra) | conversão 4,1% (bateu 3,2%) | 2 | [`controls/control-template.md`](../controls/control-template.md) | gold | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo, marcada como (EXEMPLO ILUSTRATIVO). O knowledge-librarian apaga o exemplo e ranqueia vencedores reais. -->

## Como alimenta os agentes

- **Escreve**: `knowledge-librarian` (promove e ranqueia na tarefa `memory-update`).
- **Leem**: os escritores de copy (ponto de partida), `big-idea-architect` (teses que ganharam), `money-model-designer` (escadas de ouro), `offerbook-chief` (o que escalar primeiro).

## Cross-refs

- Origem dos vencedores: [`controls/`](../controls/) e [`control-registry`](../registries/control-registry.md).
- Ofertas de ouro: [`offer-registry`](../registries/offer-registry.md). Teses: [`big-idea-registry`](../registries/big-idea-registry.md).
- Padrões de copy abstraídos (sem cópia literal): [`swipe-registry`](../registries/swipe-registry.md).
