---
id: data.registry.claim-registry
title: "Registro de Claims"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [proof-credibility-curator, mechanism-architect, vsl-webinar-scriptwriter, ad-creative-factory, compliance-auditor]
read_agents: [compliance-auditor, vsl-webinar-scriptwriter, email-sms-sequence-writer, direct-mail-insert-writer, ad-creative-factory, offerbook-chief]
tags: [claim, proof, compliance, traceability, registry]
---

# Registro de Claims

## Propósito

Esta é a **memória de todo claim** que o squad faz — e do **lastro** que o sustenta. O princípio `evidence_before_opinion` exige que **toda afirmação aponte para evidência**; o `compliance-auditor` pode **vetar** qualquer claim sem prova. Este registro é a corrente prova→claim ([`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)) tornada tabela: cada claim recebe um id, um tipo, um status de lastro e um link para o registro de prova.

Sem ele, a copy poderia repetir promessas que ninguém consegue defender. Com ele, cada frase forte da VSL, do e-mail ou do ad tem um `claim_id` rastreável até um depoimento, caso ou dado em [`proof-registry`](proof-registry.md).

## Schema

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `claim_id` | string (slug) | `kebab-case` único, ex.: `perde-5kg-30d` | Sim |
| `claim_text` | string | a afirmação, na voz do squad | Sim |
| `claim_type` | enum | `outcome` \| `mechanism` \| `speed` \| `scarcity` \| `authority` \| `comparison` | Sim |
| `offer_id` | ref | id em [`offer-registry`](offer-registry.md) | Não |
| `proof_id` | ref | id em [`proof-registry`](proof-registry.md) | Não |
| `backing_status` | enum | `unbacked` \| `partial` \| `backed` \| `vetoed` | Sim |
| `risk_level` | enum | `low` \| `medium` \| `high` (sensibilidade regulatória) | Sim |
| `used_in` | list ref | ids de peças/controls em [`control-registry`](control-registry.md) | Não |
| `disclaimer_required` | bool | `true` \| `false` | Sim |
| `owner_agent` | agent-id | id real de [`config.yaml`](../../config.yaml) | Sim |
| `decided_in` | ref | id em [`decision-registry`](decision-registry.md) | Não |
| `updated` | ISO date | `YYYY-MM-DD` | Sim |

## Quem escreve / Quem lê

**Escrevem**:
- `proof-credibility-curator` — registra o claim e o liga ao `proof_id` (tarefa `curate-proof`).
- `mechanism-architect` — registra claims de mecanismo (o *porquê funciona*).
- `vsl-webinar-scriptwriter` e `ad-creative-factory` — declaram cada claim usado na copy, com `used_in`.
- `compliance-auditor` — atualiza `backing_status` para `vetoed` e marca `disclaimer_required`.

**Leem**: `compliance-auditor` (última barreira — gate `compliance/compliance-claim-backing-gate`), todos os escritores de copy (`vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `direct-mail-insert-writer`, `ad-creative-factory`) e `offerbook-chief` (DoD).

## Registros

| claim_id | claim_text | claim_type | offer_id | proof_id | backing_status | risk_level | used_in | disclaimer_required | owner_agent | decided_in | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `exemplo-resultado-30d` _(EXEMPLO ILUSTRATIVO — apagar)_ | Clientes relatam o primeiro resultado em 30 dias (amostra) | outcome | `core-exemplo-90d` | `proof-exemplo-0001` | backed | medium | `ctrl-exemplo-vsl-01` | true | proof-credibility-curator | `dec-exemplo-0001` | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo. Apagar antes de uso real. -->
