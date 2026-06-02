---
id: archive.past-launches.readme
title: "Arquivo — Lançamentos Passados"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [archive, past-launches, postmortem, blackbook, memory]
---

# Arquivo — Lançamentos Passados

## Propósito

Esta pasta guarda a **memória viva de cada lançamento encerrado**. Quando uma promoção termina — ganhou ou perdeu — o `knowledge-librarian` conduz a retrospectiva e deposita aqui o postmortem completo. O objetivo é simples: o squad nunca repete um erro já pago, e sempre reusa o que já venceu. Isto cumpre o princípio `memory_before_repetition` no nível mais alto do pipeline.

Um postmortem não é um diário. É um documento de decisão. Ele mostra o número, a causa raiz e a ação para a próxima vez. Cada lançamento vira um caso auditável: da Big Idea ao resultado financeiro, com link para a decisão que o originou.

## O que arquivar

- Um postmortem por lançamento encerrado (use o template).
- O `launch_id` real, as datas de início e fim, e o resultado financeiro.
- A Big Idea que carregou a promoção e os controls que rodaram.
- O que funcionou, o que falhou e a causa raiz de cada falha.
- As lições já gravadas no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md).

Não arquive copy bruta nem rascunhos. Só o aprendizado destilado e seus links.

## Formato / Template

Use [`launch-postmortem-template.md`](launch-postmortem-template.md). Ele segue o esqueleto de retrospectiva: contexto, números, o que funcionou, o que falhou, causa raiz e ações. Cada arquivo final nomeia o lançamento (`postmortem-<launch_id>.md`) e marca exemplos como ilustrativos.

## Lições para reuso

Toda lição extraída aqui deve virar uma linha no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), com `action` acionável e `impact`. Lições que viram padrão sobem para swipe, framework ou default via o campo `promoted_to`. O postmortem é a fonte; o registry é o índice consultável. Os dois andam juntos.

## Liga com

- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — onde cada lição vira registro.
- [`control-registry`](../../data/registries/control-registry.md) — os controls que o lançamento rodou.
- [`losing-controls/`](../losing-controls/README.md) — autópsias dos controls que perderam.
- [`version-history/`](../version-history/README.md) — o histórico de versões da oferta.
- [`ARCHITECTURE.md`](../../ARCHITECTURE.md) — o pipeline e a camada D7 (memória).
