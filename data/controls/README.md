---
id: data.controls.readme
title: "Data Store — Controls (Peças Campeãs)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [controls, winner, ab-test, copy, data-store]
---

# Data Store — Controls (Peças Campeãs)

## Propósito

Este diretório guarda os **dossiês de control** — o detalhe vivo de cada peça campeã que toda nova copy precisa **bater**. Um *control* é a versão que venceu o teste e vira a meta a superar. Enquanto [`data/registries/control-registry.md`](../registries/control-registry.md) é a **tabela-índice** (uma linha por peça), esta pasta guarda o **dossiê completo**: o ângulo, a Big Idea, os claims, a métrica e por que ganhou.

A pasta cumpre `memory_before_repetition`: o squad reusa o que ganhou antes de recriar. Cumpre também `traceability_before_eloquence` — cada control aponta para os claims que usou, então um vencedor é auditável até a prova.

## O que guardar

- **Dossiê por control** (ex.: `ctrl-vsl-metodo-x-v3.md`): a peça campeã com contexto completo.
- O **ângulo e a Big Idea** que carregava ([`big-idea-registry`](../registries/big-idea-registry.md)).
- A **métrica de conversão** e contra quem ganhou (`beat_control_id`).
- Os **claims usados** ([`claim-registry`](../registries/claim-registry.md)) e a oferta ([`offer-registry`](../registries/offer-registry.md)).

Não guardar aqui: a tabela-índice (fica no [`control-registry`](../registries/control-registry.md)) nem os números de funil crus (vão para [`conversion-data/`](../conversion-data/)). Vencedores promovidos a "padrão de ouro" do squad ganham destaque em [`winners/`](../winners/).

## Formato / Schema

Cada dossiê é um `.md` com frontmatter (`type: doc`) e seções: identificação, ângulo/Big Idea, oferta e claims, métrica e resultado, contra quem ganhou, e por que funcionou. Os campos espelham o [`control-registry`](../registries/control-registry.md): `control_id`, `asset_type`, `metric`, `metric_value`, `result`, `beat_control_id`, `channel`.

## Como alimenta os agentes

- **Escrevem**: `vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `direct-mail-insert-writer`, `ad-creative-factory` (registram a peça testada); `knowledge-librarian` (promove a vencedora a control e arquiva perdedores na tarefa `memory-update`).
- **Leem**: todos os escritores de copy buscam o control vigente para bater; `big-idea-architect` e `positioning-lead-strategist` veem qual tese converteu; `offerbook-chief` acompanha o KPI de controls vencedores.
- **Ligações a registries**: índice em [`control-registry`](../registries/control-registry.md); claims em [`claim-registry`](../registries/claim-registry.md); oferta em [`offer-registry`](../registries/offer-registry.md); Big Idea em [`big-idea-registry`](../registries/big-idea-registry.md).

## Exemplo

Ver [`control-template.md`](control-template.md) — um dossiê de control ilustrativo (VSL campeã), com ângulo, claims, métrica e a razão da vitória, claramente marcado como exemplo.
