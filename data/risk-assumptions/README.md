---
id: data.risk-assumptions.readme
title: "Data Store — Riscos & Premissas"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [risk, assumptions, mitigation, advisory, trade-off, data-store]
---

# Data Store — Riscos & Premissas

## Propósito

Este diretório guarda os **riscos e as premissas** do lançamento — o que pode dar errado e o que estamos assumindo como verdade sem ter provado ainda. É a memória do que ameaça o resultado e do que sustenta o plano por baixo. Risco sem dono é risco esquecido; premissa não validada é uma aposta disfarçada de fato. Esta pasta torna os dois visíveis.

A pasta serve `contradiction_before_conclusion` e `evidence_before_opinion`: o contraponto e a aposta ficam registrados, não varridos para debaixo do tapete. Recebe também as **flags de risco do Advisory Board** (`cross_squad.advisory_board_squad.handoff_from_advisory` em [`config.yaml`](../../config.yaml)): risco estratégico e premissa frágil aterrissam aqui antes de virar decisão.

## O que guardar

- **Log de riscos** (`risk-log-<caso>.md`, copiado do template): cada risco com probabilidade, impacto, mitigação, dono e status.
- **Log de premissas** (`assumptions-log-<caso>.md`, copiado do template): cada premissa com a base, a confiança, se foi validada e o dono.
- **Flags do Advisory Board**: riscos e premissas levantados na crítica estratégica de entrada.

Não guardar aqui: a decisão que aceita o risco (essa vive em [`decisions/`](../decisions/) e no [`decision-registry`](../registries/decision-registry.md)) nem o número medido que valida a premissa (esse vive em [`metrics/`](../metrics/) ou [`conversion-data/`](../conversion-data/)). Esta pasta é sobre **o que ainda não é certo**: a ameaça e a aposta.

## Formato / Schema

Dois `.md`, cada um com tabela de colunas fixas. O **log de riscos**: `risco`, `probabilidade`, `impacto`, `mitigação`, `dono`, `status`. O **log de premissas**: `premissa`, `base`, `confiança`, `validada?`, `dono`. O `dono` usa ids de agente de [`config.yaml`](../../config.yaml). O risco que é aceito como trade-off liga à decisão correspondente no [`decision-registry`](../registries/decision-registry.md).

## Como alimenta os agentes

- **Escrevem**: `offerbook-chief` (riscos de escopo e prioridade), `offer-squad-architect` (riscos de pipeline e handoff), `money-model-designer` e `unit-economics-stack-analyst` (premissas de economia), `compliance-auditor` (riscos de claim e escassez), `knowledge-librarian` (consolida na memória). As flags de entrada vêm do Advisory Board.
- **Leem**: `offerbook-chief` (prioriza a mitigação no DoD), todos os agentes-dono (executam a mitigação e validam a premissa), `knowledge-librarian` (leva ao Blackbook).
- **Ligações a registries**: cada risco aceito como trade-off aponta para a decisão no [`decision-registry`](../registries/decision-registry.md); premissa validada por número liga à fonte em [`metrics/`](../metrics/) ou [`conversion-data/`](../conversion-data/).

## Exemplo

Ver [`risk-log-template.md`](risk-log-template.md) e [`assumptions-log-template.md`](assumptions-log-template.md) — um log de riscos e um log de premissas ilustrativos, cada um com uma linha de amostra marcada como exemplo.
