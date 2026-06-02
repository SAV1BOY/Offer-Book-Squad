---
id: data.registry.proof-registry
title: "Registro de Provas"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [proof-credibility-curator, avatar-voc-investigator, compliance-auditor]
read_agents: [vsl-webinar-scriptwriter, email-sms-sequence-writer, direct-mail-insert-writer, ad-creative-factory, mechanism-architect, compliance-auditor, offerbook-chief]
tags: [proof, testimonial, case-study, data, credibility, registry]
---

# Registro de Provas

## Propósito

Esta é a **memória das provas** que o squad pode usar — depoimentos, casos, dados, prints, números e demonstrações. Cada prova vira munição rastreável para sustentar um claim ([`claim-registry`](claim-registry.md)) via a corrente [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md). O `proof-credibility-curator` é o dono; o `compliance-auditor` confere a **proveniência** (consentimento, veracidade, direito de uso).

O registro garante `evidence_before_opinion`: nenhuma promessa forte sai sem uma prova catalogada por trás. Também acelera reuso — uma prova forte de um lançamento serve a outro, sem recriar.

## Schema

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `proof_id` | string (slug) | `kebab-case` único, ex.: `depo-maria-5kg` | Sim |
| `proof_type` | enum | `testimonial` \| `case-study` \| `data` \| `screenshot` \| `demo` \| `endorsement` \| `media-mention` | Sim |
| `summary` | string | o que a prova mostra, em uma frase | Sim |
| `source_name` | string | quem deu (cliente, estudo, veículo) | Sim |
| `strength` | enum | `weak` \| `moderate` \| `strong` (especificidade + verificabilidade) | Sim |
| `claim_ids` | list ref | claims que esta prova sustenta em [`claim-registry`](claim-registry.md) | Não |
| `consent_status` | enum | `pending` \| `granted` \| `revoked` | Sim |
| `verifiable` | bool | `true` \| `false` (há fonte checável?) | Sim |
| `asset_link` | path/URL | caminho do arquivo ou URL da prova | Não |
| `owner_agent` | agent-id | id real de [`config.yaml`](../../config.yaml) | Sim |
| `decided_in` | ref | id em [`decision-registry`](decision-registry.md) | Não |
| `updated` | ISO date | `YYYY-MM-DD` | Sim |

## Quem escreve / Quem lê

**Escrevem**:
- `proof-credibility-curator` — dono do registro; cataloga cada prova e seu `strength` (tarefa `curate-proof`, gate `proof/proof-claim-backing-gate`).
- `avatar-voc-investigator` — alimenta depoimentos e verbatims colhidos na mineração de VOC.
- `compliance-auditor` — atualiza `consent_status` e pode marcar uma prova como não usável.

**Leem**: todos os escritores de copy (`vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `direct-mail-insert-writer`, `ad-creative-factory`) escolhem provas por objeção; `mechanism-architect` busca prova do mecanismo; `compliance-auditor` e `offerbook-chief` no DoD.

## Registros

| proof_id | proof_type | summary | source_name | strength | claim_ids | consent_status | verifiable | asset_link | owner_agent | decided_in | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `proof-exemplo-0001` _(EXEMPLO ILUSTRATIVO — apagar)_ | testimonial | Cliente perdeu 5kg em 30 dias com fotos antes/depois (amostra) | Maria S. (amostra) | strong | `exemplo-resultado-30d` | granted | true | `data/case-studies/maria-s.md` | proof-credibility-curator | `dec-exemplo-0001` | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo. Apagar antes de uso real. -->
