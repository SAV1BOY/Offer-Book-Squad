---
id: archive.version-history.readme
title: "Arquivo — Histórico de Versões"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [archive, version-history, changelog, traceability, memory]
---

# Arquivo — Histórico de Versões

## Propósito

Esta pasta guarda o **histórico de versões dos artefatos do squad** — ofertas, Big Ideas, controls, money models e templates. Cada vez que uma peça muda de forma material, a mudança ganha uma linha datada aqui. O objetivo é responder a uma pergunta a qualquer momento: o que mudou, quando, por quê, e quem decidiu? Sem isto, o time perde o fio da evolução e repete experimentos já feitos.

O `knowledge-librarian` mantém o log. Ele não duplica o conteúdo das versões — esse vive nos registries e nos arquivos próprios. Ele registra o **salto de versão** (semver), o motivo e o link para a decisão ou o control que disparou a mudança. Assim qualquer sessão futura reconstrói a linha do tempo de uma oferta só lendo este log. Isto cumpre `traceability_before_eloquence` e `memory_before_repetition`: a rastreabilidade vem antes da beleza, e a memória vem antes da repetição.

## O que arquivar

- Uma linha por mudança material de versão (oferta, Big Idea, control, money model, template).
- O `artifact_id` real e o salto de versão (`de` → `para`, em semver).
- O motivo da mudança em uma frase.
- O link para a decisão ([`decision-registry`](../../data/registries/decision-registry.md)) ou o control que a disparou.
- A data ISO e o agente que registrou.

Não arquive mudanças cosméticas (typo, formatação). Só o que muda o comportamento ou a estratégia da peça.

## Formato / Template

Use [`version-history-log.md`](version-history-log.md). É um log em tabela, semeado vazio, com uma linha de exemplo marcada como ilustrativa. Cada entrada segue o schema: artefato, versão de/para, tipo de mudança, motivo, link e data.

## Lições para reuso

O log de versões é a fonte para detectar padrões de evolução. Quando uma oferta sobe três versões pelo mesmo motivo (ex.: ajuste de preço), isso vira lição no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md): talvez o diagnóstico inicial de WTP estivesse errado. Padrões de regressão (uma versão nova que perdeu para a antiga) ligam direto às autópsias em [`losing-controls/`](../losing-controls/README.md). O histórico não é só registro; é matéria-prima de aprendizado.

## Liga com

- [`decision-registry`](../../data/registries/decision-registry.md) — a decisão por trás de cada salto de versão.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — onde padrões de versão viram lição.
- [`deprecated-offers/`](../deprecated-offers/README.md) — quando a última versão é a aposentadoria.
- [`losing-controls/`](../losing-controls/README.md) — quando uma versão nova perdeu para a antiga.
- [`ARCHITECTURE.md`](../../ARCHITECTURE.md) — convenções de semver no frontmatter (§5.1).
