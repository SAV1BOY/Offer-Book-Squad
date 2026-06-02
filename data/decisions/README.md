---
id: data.decisions.readme
title: "Data Store — Decisões (Decision Log)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [decisions, adr, rationale, trade-off, advisory, data-store]
---

# Data Store — Decisões (Decision Log)

## Propósito

Este diretório guarda os **logs de decisão narrativos** — o "porquê" por trás de cada escolha do lançamento, em prosa. Enquanto [`data/registries/decision-registry.md`](../registries/decision-registry.md) é a **tabela-índice** (uma linha por decisão), esta pasta guarda o **documento completo** quando a decisão é grande demais para uma linha: o contexto, as alternativas pesadas, a evidência, o trade-off e quem decidiu. É o estilo ADR (Architecture Decision Record) aplicado a oferta e lançamento.

A pasta cumpre `decision_before_ornament` e `contradiction_before_conclusion`: a alternativa rejeitada fica registrada, não esquecida. Também recebe a **crítica do squad Advisory Board** (`cross_squad.advisory_board_squad`, ver [`config.yaml`](../../config.yaml)): risco e contraponto estratégico aterrissam aqui.

## O que guardar

- **Logs de decisão** grandes (ex.: `dec-log-preco-core.md`): a decisão em prosa, com alternativas e trade-off.
- **Críticas e flags de risco** do Advisory Board (handoff `handoff_from_advisory`).
- **Decisões revisitadas/revertidas** com o motivo da mudança.

Não guardar aqui: a tabela-índice (fica no [`decision-registry`](../registries/decision-registry.md)). Aqui fica o **detalhe** que a linha resume; a linha aponta de volta para o log.

## Formato / Schema

Cada log é um `.md` com frontmatter (`type: doc`) e seções: contexto, opção escolhida, alternativas, racional/evidência, trade-off, quem decidiu (e quem vetou), reversibilidade e status. Os campos espelham o [`decision-registry`](../registries/decision-registry.md): `decision_id`, `decision_type`, `made_by`, `vetoed_by`, `reversible`, `status`, `linked_registry`.

## Como alimenta os agentes

- **Escrevem**: qualquer agente que toma decisão material — `offerbook-chief` (escopo), `money-model-designer` (espinha), `value-equation-engineer`/`big-idea-architect`/`compliance-auditor` (registram **vetos** com motivo), `positioning-lead-strategist`, `funnel-architect`; o `knowledge-librarian` consolida.
- **Leem**: todos consultam para não recriar uma decisão já tomada; `offerbook-chief` audita coerência no DoD; `knowledge-librarian` leva ao Blackbook.
- **Ligações a registries**: cada log é a versão longa de uma linha em [`decision-registry`](../registries/decision-registry.md); `linked_registry` aponta para os registros afetados ([`offer-registry`](../registries/offer-registry.md), [`price-test-registry`](../registries/price-test-registry.md), etc.).

## Exemplo

Ver [`decision-log-template.md`](decision-log-template.md) — um log de decisão ilustrativo (preço do core), com alternativas, evidência e trade-off, claramente marcado como exemplo.
