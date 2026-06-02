---
id: data.registry.decision-registry
title: "Registro de Decisões"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [offerbook-chief, offer-squad-architect, money-model-designer, value-equation-engineer, positioning-lead-strategist, big-idea-architect, funnel-architect, compliance-auditor]
read_agents: [offerbook-chief, offer-squad-architect, money-model-designer, vsl-webinar-scriptwriter, funnel-architect, compliance-auditor, knowledge-librarian]
tags: [decision, trade-off, rationale, traceability, registry, memory]
---

# Registro de Decisões

## Propósito

Esta é a **memória de toda decisão** do lançamento — o que foi escolhido, **por quê**, qual o **trade-off** e quem decidiu. É o registro que **todos os outros referenciam**: cada oferta, claim, preço, Big Idea e control aponta de volta para um `decided_in` aqui. Sem decisão rastreável, não há `traceability_before_eloquence`.

O registro existe para que qualquer sessão futura entenda **por que** o squad fez o que fez — o caminho não tomado, a evidência que pesou, o risco aceito. Cumpre `decision_before_ornament` (cada peça serve a uma decisão) e `contradiction_before_conclusion` (a alternativa rejeitada fica registrada, não esquecida).

## Schema

O campo `decision_type` cobre as etapas do pipeline; `made_by` e `vetoed_by` usam ids de [`config.yaml`](../../config.yaml) (só agentes com `veto: true` aparecem em `vetoed_by`).

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `decision_id` | string (slug) | `kebab-case` único, ex.: `dec-0001-preco-core` | Sim |
| `title` | string | a decisão em uma frase | Sim |
| `decision_type` | enum | `scope` \| `mechanism` \| `pricing` \| `money-model` \| `big-idea` \| `positioning` \| `funnel` \| `compliance` \| `offer` | Sim |
| `context` | string | situação/pergunta que exigiu a escolha | Sim |
| `chosen_option` | string | o que foi decidido | Sim |
| `alternatives` | string | opções rejeitadas (o caminho não tomado) | Sim |
| `rationale` | string | por quê — a evidência que pesou | Sim |
| `trade_off` | string | o que se abriu mão / o risco aceito | Sim |
| `made_by` | agent-id | quem decidiu (id de [`config.yaml`](../../config.yaml)) | Sim |
| `vetoed_by` | agent-id | agente que vetou, se houve (só `veto: true`) | Não |
| `reversible` | bool | `true` \| `false` (decisão de uma via?) | Não |
| `status` | enum | `proposed` \| `decided` \| `revisited` \| `reversed` | Sim |
| `linked_registry` | list ref | registros afetados (ex.: `offer-registry`, `price-test-registry`) | Não |
| `updated` | ISO date | `YYYY-MM-DD` | Sim |

## Quem escreve / Quem lê

**Escrevem** (qualquer agente que toma uma decisão material; donos por etapa):
- `offerbook-chief` — decisões de escopo, prioridade e DoD (tarefa `intake-and-scope`).
- `offer-squad-architect` — desenho do pipeline e handoffs.
- `money-model-designer` — decisões da espinha (ordem da escada, papéis).
- `value-equation-engineer`, `big-idea-architect`, `compliance-auditor` — registram seus **vetos** em `vetoed_by` com o motivo no `rationale`.
- `positioning-lead-strategist`, `funnel-architect` — lead/posicionamento e arquitetura de funil.

**Leem**: todos os agentes consultam para não recriar uma decisão já tomada; `knowledge-librarian` consolida no Blackbook; `offerbook-chief` audita coerência no DoD.

## Registros

| decision_id | title | decision_type | context | chosen_option | alternatives | rationale | trade_off | made_by | vetoed_by | reversible | status | linked_registry | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `dec-exemplo-0001` _(EXEMPLO ILUSTRATIVO — apagar)_ | Preço do core em R$ 2497 (amostra) | pricing | Van Westendorp deu faixa R$ 1750-2400 | R$ 2497 com bônus | R$ 1997 sem bônus | WTP no topo da faixa + valor empilhado (amostra) | menos volume, mais margem por venda | money-model-designer | — | true | decided | `offer-registry`, `price-test-registry` | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo, marcada como (EXEMPLO ILUSTRATIVO). Os agentes apagam o exemplo e escrevem registros reais. -->
