---
id: data.registry.control-registry
title: "Registro de Controls"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [vsl-webinar-scriptwriter, email-sms-sequence-writer, direct-mail-insert-writer, ad-creative-factory, knowledge-librarian]
read_agents: [vsl-webinar-scriptwriter, email-sms-sequence-writer, ad-creative-factory, big-idea-architect, positioning-lead-strategist, offerbook-chief]
tags: [control, winner, loser, copy, ab-test, registry, memory]
---

# Registro de Controls

## Propósito

Esta é a **memória dos controls** — as peças de copy que **venceram** (e as que **perderam**) em teste. Um *control* é a versão campeã que toda nova peça precisa bater. Aqui registramos cada VSL, e-mail, ad ou mailer testado, sua **métrica de conversão**, se virou control ou foi batido, e a **Big Idea** ([`big-idea-registry`](big-idea-registry.md)) e oferta ([`offer-registry`](offer-registry.md)) que carregava.

O registro cumpre `memory_before_repetition`: o squad reusa o que ganhou antes de recriar, e aprende com o que perdeu. Vence também `traceability_before_eloquence` — cada control aponta para os claims ([`claim-registry`](claim-registry.md)) que usou, então um vencedor é auditável até a prova.

## Schema

A peça referencia [`big-idea-registry`](big-idea-registry.md), [`offer-registry`](offer-registry.md) e [`claim-registry`](claim-registry.md).

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `control_id` | string (slug) | `kebab-case` único, ex.: `ctrl-vsl-metodo-x-v3` | Sim |
| `asset_type` | enum | `vsl` \| `webinar` \| `email` \| `sms` \| `ad` \| `sales-page` \| `mailer` \| `insert` \| `vsl-recap` | Sim |
| `title` | string | nome humano da peça | Sim |
| `offer_id` | ref | id em [`offer-registry`](offer-registry.md) | Não |
| `big_idea_id` | ref | id em [`big-idea-registry`](big-idea-registry.md) | Não |
| `claim_ids` | list ref | claims usados em [`claim-registry`](claim-registry.md) | Não |
| `metric` | enum | `conversion-rate` \| `opt-in-rate` \| `ctr` \| `aov` \| `epc` \| `roas` \| `cart-close-lift` | Sim |
| `metric_value` | number/string | valor medido (ex.: `4.1%`, `R$ 3.20 EPC`) | Sim |
| `result` | enum | `winner` \| `loser` \| `control` \| `beaten` \| `inconclusive` | Sim |
| `beat_control_id` | ref | control que esta peça superou (se houver) | Não |
| `channel` | enum | `vsl-funnel` \| `email` \| `paid-social` \| `paid-search` \| `direct-mail` \| `webinar` \| `affiliate` | Não |
| `status` | enum | `live` \| `paused` \| `archived` | Sim |
| `owner_agent` | agent-id | id real de [`config.yaml`](../../config.yaml) | Sim |
| `decided_in` | ref | id em [`decision-registry`](decision-registry.md) | Não |
| `updated` | ISO date | `YYYY-MM-DD` | Sim |

## Quem escreve / Quem lê

**Escrevem**:
- `vsl-webinar-scriptwriter` — registra a VSL/webinar testado e seu resultado (tarefa `write-vsl-webinar`).
- `email-sms-sequence-writer` — registra sequências de e-mail/SMS e o `cart-close-lift` (tarefa `write-email-sms-sequences`).
- `direct-mail-insert-writer` e `ad-creative-factory` — registram mailers e ads, com `metric_value`.
- `knowledge-librarian` — promove a peça vencedora a `control` e arquiva os perdedores (tarefa `memory-update`).

**Leem**: todos os escritores de copy buscam o control vigente para bater; `big-idea-architect` e `positioning-lead-strategist` veem qual tese converteu; `offerbook-chief` acompanha o KPI `winning-controls`.

## Registros

| control_id | asset_type | title | offer_id | big_idea_id | claim_ids | metric | metric_value | result | beat_control_id | channel | status | owner_agent | decided_in | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `ctrl-exemplo-vsl-01` _(EXEMPLO ILUSTRATIVO — apagar)_ | vsl | VSL Método X v3 (amostra) | `core-exemplo-90d` | `metodo-x-exemplo` | `exemplo-resultado-30d` | conversion-rate | 4.1% | control | `ctrl-exemplo-vsl-00` | vsl-funnel | live | vsl-webinar-scriptwriter | `dec-exemplo-0001` | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo, marcada como (EXEMPLO ILUSTRATIVO). Os agentes apagam o exemplo e escrevem registros reais. -->
