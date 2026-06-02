---
id: data.handoffs.readme
title: "Data Store — Handoffs Cross-Squad (Manifesto & Log)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [handoff, cross-squad, manifest, log, contract, rejection, data-store]
---

# Data Store — Handoffs Cross-Squad (Manifesto & Log)

## Propósito

Este diretório guarda o **manifesto e o log dos handoffs cross-squad** — toda entrega que sai deste squad para outro e toda que entra de outro. É a memória da fronteira: o que foi entregue, sob qual contrato, se foi aceito ou rejeitado, e por qual defeito quando voltou. Um handoff só é válido quando o destinatário pode agir sem voltar a perguntar; este log prova isso ou registra a falha.

A pasta serve `traceability_before_eloquence` na fronteira entre squads. Cada linha do log aponta para o contrato que a rege ([`handoff-contract-template`](../../templates/cross-squad/handoff-contract-template.md)) e para a decisão que a aprovou. As rejeições e reentradas ficam aqui, não escondidas: um pacote devolvido com defeito nomeado é dado de memória, não vergonha.

## O que guardar

- **Manifesto de handoffs** (`handoff-manifest-<periodo>.md`, copiado do template): uma linha por handoff, de entrada ou de saída.
- **Rejeições e reentradas**: o pacote devolvido com o defeito nomeado e o re-envio corrigido, com a nova data.
- **Os contratos preenchidos** que regem cada handoff (referenciados em `contract_ref`).

Não guardar aqui: o ativo recebido em si depois de validado (entra nos registries via [`cross-squad-asset-validation`](../../checklists/cross-squad/cross-squad-asset-validation.md)) nem o pedido de pesquisa que abre o fluxo (esse nasce no [`decision-registry`](../registries/decision-registry.md)). Esta pasta é sobre **o trânsito na fronteira**: quem passou o quê para quem, com qual veredito.

## Formato / Schema

O manifesto é um `.md` com tabela de colunas fixas: `handoff_id`, `de_squad`, `para_squad`, `artefato`, `contract_ref`, `status` (enviado/aceito/rejeitado), `defeito`, `data`, `decided_in`. Os squads de origem/destino usam os nomes de [`config.yaml`](../../config.yaml) (`cross_squad`): deepresearch, copy, brand, traffic, design, data, c-level, advisory. Cada handoff é regido pelos três gates de fronteira em [`checklists/cross-squad/`](../../checklists/cross-squad/).

## Como alimenta os agentes

- **Escrevem**: `offerbook-chief` (controla as transições de fronteira e libera ou segura o handoff), `compliance-auditor` (co-assina quando o pacote leva claims; rejeita ativo de entrada sem lastro), `knowledge-librarian` (consolida o log na memória).
- **Leem**: `offerbook-chief` (audita a fronteira no DoD), `offer-squad-architect` (desenho dos handoffs e contratos), todos os agentes-dono dos artefatos entregues (para corrigir o que voltou).
- **Ligações a registries**: cada handoff aponta para um `decided_in` no [`decision-registry`](../registries/decision-registry.md); o ativo de entrada aceito é gravado nos registries de prova/claim/swipe pelo `knowledge-librarian`.

## Exemplo

Ver [`handoff-manifest-template.md`](handoff-manifest-template.md) — um manifesto ilustrativo com handoffs de entrada e de saída, uma rejeição com defeito nomeado e a reentrada, marcado como exemplo.
