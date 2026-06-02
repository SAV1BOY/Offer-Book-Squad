---
id: authority.proof-asset-index
title: "Índice de Ativos de Prova"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
tags: [authority, proof, index, master, registry, evidence, traceability]
---

# Índice de Ativos de Prova

## Propósito

Este é o **índice-mestre de todos os ativos de prova** do squad. Ele não guarda a prova em si — ele aponta para onde cada ativo vive (depoimento, caso, número, sinal de mídia, parceria, prêmio) e como cada um se liga ao [`proof-registry`](../data/registries/proof-registry.md). É o mapa único que responde "que prova temos, de que força, e onde está?" sem abrir dez arquivos.

O dono é o [`proof-credibility-curator`](../agents/proof-credibility-curator.md). Quando um escritor de copy precisa de munição para uma objeção, ou o [`compliance-auditor`](../agents/compliance-auditor.md) precisa conferir o lastro de um claim, este índice é o ponto de entrada. Ele garante `traceability_before_eloquence`: toda prova é rastreável da copy até a fonte primária, passando por aqui.

O índice cobre os bancos de autoridade — [`results-database.md`](results-database.md), [`case-study-library.md`](case-study-library.md), [`testimonial-vault.md`](testimonial-vault.md), [`credibility-builders.md`](credibility-builders.md), [`pr-placements.md`](pr-placements.md), [`social-proof-inventory.md`](social-proof-inventory.md), [`data-points-bank.md`](data-points-bank.md), [`awards-certifications.md`](awards-certifications.md) e [`partnerships-endorsements.md`](partnerships-endorsements.md) — e mapeia cada um ao registro central.

## Estrutura / Schema

Cada ativo é uma linha no índice. Colunas obrigatórias:

| Coluna | Tipo | O que registrar |
|---|---|---|
| `asset_id` | slug | id único do ativo, ex.: `asset-depo-carla-video` |
| `asset_type` | enum | `testimonial` \| `case-study` \| `data` \| `screenshot` \| `demo` \| `endorsement` \| `media-mention` |
| `home_file` | path | banco onde o ativo vive (ex.: `testimonial-vault.md`) |
| `home_record_id` | ref | id do registro dentro do banco |
| `proof_id` | ref | linha no [`proof-registry`](../data/registries/proof-registry.md) |
| `claim_ids` | list ref | claims que o ativo sustenta no [`claim-registry`](../data/registries/claim-registry.md) |
| `strength` | enum | `weak` \| `moderate` \| `strong` |
| `consent_status` | enum | `pending` \| `granted` \| `revoked` |
| `verifiable` | bool | há fonte checável? |
| `updated` | data | `YYYY-MM-DD` |

### Tracker (semeado vazio)

| asset_id | asset_type | home_file | proof_id | strength | consent_status | verifiable | updated |
|---|---|---|---|---|---|---|---|
| `asset-exemplo-0001` _(EXEMPLO — apagar)_ | testimonial | testimonial-vault.md | `proof-exemplo-0001` | strong | granted | true | 2026-06-02 |

## Como coletar & verificar

1. Sempre que um ativo entra em qualquer banco de autoridade, crie a linha-espelho aqui no mesmo momento.
2. Preencha `home_file` + `home_record_id` para que o caminho de volta à fonte seja um clique.
3. Confirme que `proof_id` resolve em uma linha real do [`proof-registry`](../data/registries/proof-registry.md) — o índice exige bijeção, sem ativo órfão.
4. Reflita aqui o `strength`, `consent_status` e `verifiable` que vivem no banco de origem; em divergência, a fonte primária manda.
5. Rode a conferência periódica: todo ativo do índice aponta para um arquivo e um registro existentes; todo registro de prova tem entrada aqui.

## Regras de uso & compliance

- O índice é a fonte de verdade para "que prova existe"; copy só usa ativo que tem linha aqui com `verifiable: true`.
- Ativo sem `proof_id` válido = órfão = não usável até ser ligado ao registro.
- `consent_status: revoked` aqui retira o ativo de toda peça, em cascata para os bancos.
- O índice não duplica conteúdo — ele aponta. Editar o ativo é feito no banco de origem, nunca aqui.
- Conformidade com [`../docs/compliance-policy.md`](../docs/compliance-policy.md): rastreabilidade de claim↔prova é pré-requisito do DoD.

## Liga com

- Todos os bancos de autoridade: [`results-database.md`](results-database.md), [`case-study-library.md`](case-study-library.md), [`testimonial-vault.md`](testimonial-vault.md), [`credibility-builders.md`](credibility-builders.md), [`pr-placements.md`](pr-placements.md), [`social-proof-inventory.md`](social-proof-inventory.md), [`data-points-bank.md`](data-points-bank.md), [`awards-certifications.md`](awards-certifications.md), [`partnerships-endorsements.md`](partnerships-endorsements.md).
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (dono), [`compliance-auditor`](../agents/compliance-auditor.md) (confere lastro), [`pr-brand-strategist`](../agents/pr-brand-strategist.md).
- Registries: [`proof-registry`](../data/registries/proof-registry.md) (espelho central), [`claim-registry`](../data/registries/claim-registry.md).
- Framework: [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md).
