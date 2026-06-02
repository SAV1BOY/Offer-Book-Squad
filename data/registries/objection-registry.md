---
id: data.registry.objection-registry
title: "Registro de Objeções"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [avatar-voc-investigator, mechanism-architect, vsl-webinar-scriptwriter, email-sms-sequence-writer, compliance-auditor]
read_agents: [vsl-webinar-scriptwriter, email-sms-sequence-writer, direct-mail-insert-writer, ad-creative-factory, pricing-wtp-strategist, offerbook-chief]
tags: [objection, voc, rebuttal, proof, registry, memory]
---

# Registro de Objeções

## Propósito

Esta é a **memória de toda objeção** que trava a compra — e da **resposta** que a desarma. Toda objeção sai da voz do cliente (VOC), minerada pelo `avatar-voc-investigator`, não do palpite. Cada uma recebe um id, uma categoria, a emoção por trás, a resposta que a vence e o link para a **prova** ([`proof-registry`](proof-registry.md)) ou o **mecanismo** ([`unique-mechanism`](../../frameworks/unique-mechanism.md)) que a sustenta.

O registro cumpre `evidence_before_opinion` e `contradiction_before_conclusion`: o squad busca o "não" **antes** de escrever a copy, mapeia prova a cada objeção e nunca deixa um medo do comprador sem resposta. Sem ele, a VSL e os e-mails ignorariam o que de fato segura a venda.

## Schema

A categoria mapeia a crença por trás da objeção (mineração de VOC do `avatar-voc-investigator`); a resposta liga prova ao claim via [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md). O nível de consciência vem de [`awareness-levels`](../../lib/taxonomies/awareness-levels.md).

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `objection_id` | string (slug) | `kebab-case` único, ex.: `caro-demais` | Sim |
| `objection_text` | string | a objeção na voz do cliente (verbatim quando possível) | Sim |
| `category` | enum | `price` \| `time` \| `trust` \| `belief-self` \| `belief-mechanism` \| `fit` \| `risk` \| `priority` | Sim |
| `underlying_emotion` | string | medo/crença por trás (ex.: "medo de fracassar de novo") | Sim |
| `awareness_level` | int 1-5 | nível de [consciência](../../lib/taxonomies/awareness-levels.md) onde aparece | Não |
| `rebuttal` | string | a resposta que desarma, na voz do squad | Sim |
| `rebuttal_type` | enum | `proof` \| `reframe` \| `guarantee` \| `mechanism` \| `bonus` \| `scarcity` \| `urgency` | Sim |
| `proof_id` | ref | prova que sustenta a resposta em [`proof-registry`](proof-registry.md) | Não |
| `offer_id` | ref | id em [`offer-registry`](offer-registry.md) | Não |
| `severity` | enum | `low` \| `medium` \| `high` (quanto trava a venda) | Sim |
| `status` | enum | `open` \| `addressed` \| `recurring` | Sim |
| `owner_agent` | agent-id | id real de [`config.yaml`](../../config.yaml) | Sim |
| `decided_in` | ref | id em [`decision-registry`](decision-registry.md) | Não |
| `updated` | ISO date | `YYYY-MM-DD` | Sim |

## Quem escreve / Quem lê

**Escrevem**:
- `avatar-voc-investigator` — dono da fonte; minera cada objeção na pesquisa de VOC e registra `objection_text` + `underlying_emotion` (tarefa `build-avatar-voc`, gate `avatar/avatar-objection-map-gate`).
- `mechanism-architect` — registra a resposta de mecanismo para objeções de descrença ("por que vai funcionar pra mim?").
- `vsl-webinar-scriptwriter` e `email-sms-sequence-writer` — marcam `status: addressed` quando a peça vence a objeção e ligam o `proof_id` usado.
- `compliance-auditor` — confere que a resposta não cria claim sem lastro.

**Leem**: todos os escritores de copy (`vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `direct-mail-insert-writer`, `ad-creative-factory`) escrevem rebatendo objeção por objeção; `pricing-wtp-strategist` usa objeções de preço para calibrar WTP; `offerbook-chief` confere cobertura no DoD.

## Registros

| objection_id | objection_text | category | underlying_emotion | awareness_level | rebuttal | rebuttal_type | proof_id | offer_id | severity | status | owner_agent | decided_in | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `caro-demais-exemplo` _(EXEMPLO ILUSTRATIVO — apagar)_ | "É caro demais pra mim agora" (amostra) | price | medo de desperdiçar dinheiro de novo | 4 | Mostra o custo de não agir e ancora no resultado, não no preço (amostra) | reframe | `proof-exemplo-0001` | `core-exemplo-90d` | high | addressed | avatar-voc-investigator | `dec-exemplo-0001` | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo, marcada como (EXEMPLO ILUSTRATIVO). Os agentes apagam o exemplo e escrevem registros reais. -->
