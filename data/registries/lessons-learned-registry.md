---
id: data.registry.lessons-learned-registry
title: "Registro de Lições Aprendidas"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [knowledge-librarian, offerbook-chief, compliance-auditor]
read_agents: [offerbook-chief, offer-squad-architect, money-model-designer, big-idea-architect, vsl-webinar-scriptwriter, positioning-lead-strategist, knowledge-librarian]
tags: [lessons, retrospective, launch, blackbook, memory, registry]
---

# Registro de Lições Aprendidas

## Propósito

Esta é a **memória das lições por lançamento** — o que funcionou, o que falhou e **o que mudar na próxima vez**. É o coração do **Blackbook**: cada promoção encerrada deixa lições rastreáveis, ligadas à decisão ([`decision-registry`](decision-registry.md)) ou ao control ([`control-registry`](control-registry.md)) que as gerou.

O registro cumpre `memory_before_repetition` no nível mais alto: o squad não repete o erro de um lançamento no seguinte, e promove o que ganhou a padrão reutilizável (swipe, framework, default). Cada lição vira ação — não fica só na observação. Alimenta o KPI `lessons-learned-frequency`.

## Schema

A `category` mapeia a fase do pipeline ([`ARCHITECTURE.md`](../../ARCHITECTURE.md) §3). `impact` mede o peso da lição.

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `lesson_id` | string (slug) | `kebab-case` único, ex.: `ll-2025-q2-cart-timing` | Sim |
| `launch_id` | string | lançamento/promoção de origem, ex.: `metodo-x-2025-q2` | Sim |
| `category` | enum | `market` \| `avatar` \| `offer` \| `pricing` \| `money-model` \| `big-idea` \| `copy` \| `funnel` \| `ops` \| `affiliate` \| `compliance` | Sim |
| `observation` | string | o que aconteceu (fato observado) | Sim |
| `what_worked` | string | o que deu certo | Não |
| `what_failed` | string | o que deu errado | Não |
| `root_cause` | string | a causa raiz (não o sintoma) | Não |
| `action` | string | o que mudar na próxima vez (a lição acionável) | Sim |
| `impact` | enum | `low` \| `medium` \| `high` \| `critical` | Sim |
| `promoted_to` | ref | virou swipe/framework/default? (ex.: `swipe-registry`, `framework.copy.pas`) | Não |
| `source_ref` | ref | id em [`decision-registry`](decision-registry.md) ou [`control-registry`](control-registry.md) | Não |
| `status` | enum | `open` \| `applied` \| `archived` | Sim |
| `owner_agent` | agent-id | id real de [`config.yaml`](../../config.yaml) | Sim |
| `updated` | ISO date | `YYYY-MM-DD` | Sim |

## Quem escreve / Quem lê

**Escrevem**:
- `knowledge-librarian` — dono do registro; conduz a retrospectiva pós-lançamento e registra cada lição com sua `action` (tarefa `memory-update`, gate `final-delivery-checklist`). Promove lições a swipe/framework via `promoted_to`.
- `offerbook-chief` — registra lições de escopo, prioridade e processo.
- `compliance-auditor` — registra lições de claim/escassez/LGPD que devem virar default.

**Leem**: todo o comando e a arquitetura de oferta (`offerbook-chief`, `offer-squad-architect`, `money-model-designer`, `big-idea-architect`) consultam antes do próximo lançamento; os escritores de copy veem o que converteu e o que queimou; `positioning-lead-strategist` ajusta lead/posição com base no histórico.

## Registros

| lesson_id | launch_id | category | observation | what_worked | what_failed | root_cause | action | impact | promoted_to | source_ref | status | owner_agent | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `ll-exemplo-2025q2-cart` _(EXEMPLO ILUSTRATIVO — apagar)_ | `metodo-x-exemplo-2025-q2` | copy | E-mail de fechamento de carrinho às 20h converteu mais (amostra) | janela final de urgência | timing cedo demais no 1º teste | fadiga de inbox de manhã | mover o e-mail de fechamento para a noite | high | `swipe-registry` | `dec-exemplo-0001` | applied | knowledge-librarian | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo, marcada como (EXEMPLO ILUSTRATIVO). Os agentes apagam o exemplo e escrevem registros reais. -->
