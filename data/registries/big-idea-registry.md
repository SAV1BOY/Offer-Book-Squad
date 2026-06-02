---
id: data.registry.big-idea-registry
title: "Registro de Big Ideas"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [big-idea-architect, positioning-lead-strategist, market-sophistication-analyst]
read_agents: [vsl-webinar-scriptwriter, email-sms-sequence-writer, ad-creative-factory, positioning-lead-strategist, offerbook-chief, compliance-auditor]
tags: [big-idea, power-of-one, hook, positioning, registry, memory]
---

# Registro de Big Ideas

## Propósito

Esta é a **memória das Big Ideas testadas** — cada tese candidata e a que venceu o lançamento. O princípio `one_big_idea` (Power of One) exige **UMA tese por lançamento**; múltiplas ideias = reprovação do `big-idea-architect`. Aqui registramos cada candidata gerada na ideação ([ToT](../../frameworks/big-idea-architect/big-idea-ideation-tot.md)), sua nota nos 5 critérios ([scoring](../../frameworks/big-idea-architect/big-idea-scoring.md)) e qual foi **travada**.

O registro cumpre `memory_before_repetition` e `clarity_before_volume`: ideias que ganharam (ou queimaram) viram memória, e o lançamento sai com uma única promessa central. Toda Big Idea aponta para o nível de [sofisticação](../../lib/taxonomies/sophistication-levels.md) que a justifica e para a decisão que a escolheu.

## Schema

A nota usa os 5 critérios de [`big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md). O estágio vem de [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md).

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `idea_id` | string (slug) | `kebab-case` único, ex.: `metodo-x-90d` | Sim |
| `idea_statement` | string | a Big Idea em uma frase (a tese) | Sim |
| `promise` | string | a promessa central (o resultado prometido) | Sim |
| `hook` | string | o gancho/ângulo de entrada | Não |
| `villain` | string | o inimigo comum (o que o cliente culpa) | Não |
| `sophistication_stage` | int 1-5 | estágio que a ideia ataca | Sim |
| `new` | int 0-5 | nota "Nova" (ineditismo) | Não |
| `big` | int 0-5 | nota "Grande" (tamanho da promessa) | Não |
| `credible` | int 0-5 | nota "Crível" (sustentável por prova) | Não |
| `total_score` | int 0-100 | nota composta dos 5 critérios | Não |
| `status` | enum | `candidate` \| `tested` \| `locked` \| `rejected` \| `retired` | Sim |
| `offer_id` | ref | id em [`offer-registry`](offer-registry.md) | Não |
| `owner_agent` | agent-id | id real de [`config.yaml`](../../config.yaml) | Sim |
| `decided_in` | ref | id em [`decision-registry`](decision-registry.md) | Sim |
| `updated` | ISO date | `YYYY-MM-DD` | Sim |

## Quem escreve / Quem lê

**Escrevem**:
- `big-idea-architect` — dono do registro; gera as candidatas, pontua e marca **uma** como `locked` (tarefa `generate-big-idea`, gate `big-idea/big-idea-single-gate`). Múltiplas `locked` no mesmo lançamento = falha.
- `positioning-lead-strategist` — alinha a ideia travada ao posicionamento e ao lead (gate `positioning/positioning-awareness-fit`).
- `market-sophistication-analyst` — valida o `sophistication_stage` que justifica a ideia.

**Leem**: `vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `ad-creative-factory` (toda copy nasce da mesma tese travada); `offerbook-chief` (DoD do Offer Book) e `compliance-auditor` (a promessa tem lastro?).

## Registros

| idea_id | idea_statement | promise | hook | villain | sophistication_stage | new | big | credible | total_score | status | offer_id | owner_agent | decided_in | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `metodo-x-exemplo` _(EXEMPLO ILUSTRATIVO — apagar)_ | Não é força de vontade, é o seu metabolismo X (amostra) | Primeiro resultado em 30 dias sem dieta | "O motivo real por que dietas falham" | a indústria das dietas | 3 | 4 | 4 | 3 | 78 | locked | `core-exemplo-90d` | big-idea-architect | `dec-exemplo-0001` | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo, marcada como (EXEMPLO ILUSTRATIVO). Os agentes apagam o exemplo e escrevem registros reais. -->
