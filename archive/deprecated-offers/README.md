---
id: archive.deprecated-offers.readme
title: "Arquivo — Ofertas Descontinuadas"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [archive, deprecated-offers, sunset, money-model, memory]
---

# Arquivo — Ofertas Descontinuadas

## Propósito

Esta pasta guarda o registro de **toda oferta que saiu de circulação**. Uma oferta pode ser aposentada por mil motivos: a unit economics quebrou, o mercado ficou sofisticado demais, o mecanismo perdeu o frescor, ou uma versão melhor a substituiu. Aqui o `knowledge-librarian` documenta **por que** ela saiu e **o que aprender** com isso.

O objetivo é evitar dois erros caros: ressuscitar uma oferta morta sem lembrar por que morreu, e perder o aprendizado de uma boa ideia que só faltou timing. Cada registro liga a oferta arquivada à decisão que a aposentou e à versão que a substituiu. Isto cumpre `memory_before_repetition` e `traceability_before_eloquence`.

## O que arquivar

- Um registro de descontinuação por oferta aposentada (use o template).
- O `offer_id` real e a versão final que rodou.
- O motivo da descontinuação e a métrica que o comprova.
- A oferta substituta, se houver (`replaced_by`).
- A decisão que selou o fim ([`decision-registry`](../../data/registries/decision-registry.md)).

Não arquive a oferta inteira de novo — ela já vive no [`offer-registry`](../../data/registries/offer-registry.md). Arquive só o motivo do fim e a lição.

## Formato / Template

Use [`deprecation-record-template.md`](deprecation-record-template.md). Ele captura contexto, motivo, evidência, substituta e lição. Cada arquivo final nomeia a oferta (`deprecation-<offer_id>.md`) e marca exemplos como ilustrativos.

## Lições para reuso

Toda descontinuação carrega uma lição: o que sinaliza que uma oferta está morrendo, e quando aposentar antes de queimar caixa. Essa lição vira linha no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), categoria `offer` ou `money-model`. Um padrão de morte recorrente sobe a default ou framework via `promoted_to`.

## Liga com

- [`offer-registry`](../../data/registries/offer-registry.md) — onde a oferta viva está catalogada.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — onde a lição vira registro.
- [`decision-registry`](../../data/registries/decision-registry.md) — a decisão que aposentou.
- [`version-history/`](../version-history/README.md) — o histórico de versões da oferta.
- [`ARCHITECTURE.md`](../../ARCHITECTURE.md) — o pipeline e o Money Model (camada D2).
