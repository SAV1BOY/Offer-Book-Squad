---
id: archive.retired-big-ideas.readme
title: "Arquivo — Grandes Ideias Aposentadas"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [archive, retired-big-ideas, big-idea, positioning, memory]
---

# Arquivo — Grandes Ideias Aposentadas

## Propósito

Esta pasta guarda o registro de **toda Big Idea que saiu de uso**. O princípio `one_big_idea` diz que cada lançamento carrega UMA tese central. Quando uma tese para de converter, vira clichê de mercado ou é substituída por um ângulo mais forte, ela é aposentada — mas não apagada. Aqui o `knowledge-librarian` documenta **por que** a ideia foi retirada e **o que aprender** com sua trajetória.

O objetivo é proteger o squad de dois erros caros: reciclar uma tese gasta achando que é nova, e perder o aprendizado de um ângulo que só faltou timing ou mercado certo. Uma Big Idea aposentada por saturação hoje pode renascer em outro avatar amanhã — desde que o time lembre por que ela cansou. Cada registro liga a tese arquivada à decisão que a aposentou, aos controls que ela carregou e à ideia que a substituiu. Isto cumpre `memory_before_repetition` e `traceability_before_eloquence`.

## O que arquivar

- Um registro de aposentadoria por Big Idea retirada (use o template).
- O `big_idea_id` real e a versão final da tese.
- O motivo da retirada e a evidência que o comprova.
- A Big Idea substituta, se houver (`replaced_by`).
- Os controls que a tese carregou e o melhor resultado que ela já deu.
- A decisão que selou a retirada ([`decision-registry`](../../data/registries/decision-registry.md)).

Não duplique a tese inteira — ela já vive no [`big-idea-registry`](../../data/registries/big-idea-registry.md). Arquive só o motivo do fim, a trajetória e a lição.

## Formato / Template

Use [`retired-big-idea-record-template.md`](retired-big-idea-record-template.md). Ele captura contexto, motivo da retirada, evidência, substituta e lição. Cada arquivo final nomeia a tese (`retired-<big_idea_id>.md`) e marca exemplos como ilustrativos.

## Lições para reuso

Toda aposentadoria carrega uma lição: o que sinaliza que uma tese está cansando, e quando trocar antes que a conversão despenque. Essa lição vira linha no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), categoria `big-idea` ou `copy`. Um padrão de fadiga recorrente — por exemplo, queda de conversão após N meses no mesmo ângulo — sobe a default ou framework via `promoted_to`, virando gatilho de revisão.

## Liga com

- [`big-idea-registry`](../../data/registries/big-idea-registry.md) — onde a tese viva está catalogada.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — onde a lição vira registro.
- [`decision-registry`](../../data/registries/decision-registry.md) — a decisão que aposentou.
- [`losing-controls/`](../losing-controls/README.md) — autópsias dos controls que a tese carregou.
- [`ARCHITECTURE.md`](../../ARCHITECTURE.md) — o pipeline e a Big Idea (camada D3).
