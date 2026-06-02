---
id: authority.social-proof-inventory
title: "Inventário de Prova Social"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
tags: [authority, social-proof, reviews, ugc, numbers, evidence]
---

# Inventário de Prova Social

## Propósito

Este arquivo inventaria toda a **prova social** do squad — avaliações, notas, comentários, conteúdo gerado por usuário (UGC), números de seguidores, volume de vendas, selos de "milhares de clientes". A prova social ativa o gatilho do consenso: o avatar confia mais quando vê que muitos como ele já confiaram. É o "se todos estão fazendo, deve ser certo".

O dono é o [`proof-credibility-curator`](../agents/proof-credibility-curator.md). Diferente do [`testimonial-vault.md`](testimonial-vault.md), que guarda a fala individual com permissão formal, este inventário cataloga o **volume e a média** — a nota 4,8 de 1.200 avaliações, o print da seção de comentários, o número de membros da comunidade. A regra: cada número é real e verificável; nota inflada ou contagem inventada vira veto do [`compliance-auditor`](../agents/compliance-auditor.md).

O inventário alimenta as faixas de prova social na página, no anúncio e na VSL, e abastece os [`credibility-builders.md`](credibility-builders.md). Ele complementa a prova de resultado: o número mostra escala, o caso mostra profundidade.

## Estrutura / Schema

Catalogue cada ativo de prova social. Campos:

| Campo | O que registrar |
|---|---|
| `social_id` | slug único, ex.: `social-nota-google-48` |
| `proof_kind` | `avaliação` \| `nota-média` \| `comentário` \| `ugc` \| `seguidores` \| `volume-vendas` \| `selo-comunidade` |
| `platform` | onde vive (Google, Instagram, marketplace, app) |
| `metric_value` | o número exato (ex.: `4,8 de 5` · `1.200 avaliações`) |
| `sample_size` | base do número (quantas avaliações, quantos clientes) |
| `capture_link` | print ou URL que prova o número |
| `verifiable` | há como conferir publicamente? |
| `consent_needed` | UGC de pessoa identificável exige permissão? |
| `proof_id` | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |
| `updated` | `YYYY-MM-DD` |

### Tracker (semeado vazio)

| social_id | proof_kind | platform | metric_value | sample_size | verifiable | proof_id |
|---|---|---|---|---|---|---|
| `social-exemplo-0001` _(EXEMPLO — apagar)_ | nota-média | Google (amostra) | 4,8 de 5 | 1.200 | true | `proof-exemplo-0001` |

## Como coletar & verificar

1. Capture o número na fonte pública e guarde o `capture_link` (print com data e contexto visível).
2. Registre o `sample_size` — nota sem base é frágil; "4,8 de 1.200" é forte, "4,8" sozinho é fraco.
3. Para UGC com pessoa identificável (rosto, @ visível), trate como depoimento e colha permissão via [`testimonial-vault.md`](testimonial-vault.md).
4. Confirme que o número é o atual; nota e contagem mudam, então datar a captura é obrigatório.
5. Espelhe no [`proof-registry`](../data/registries/proof-registry.md) com o `proof_type` adequado (`screenshot`, `data` ou `testimonial`).

## Regras de uso & compliance

- Todo número de prova social usado em copy tem `verifiable: true` e captura datada.
- Nota e contagem não podem ser arredondadas para cima nem destacadas sem o `sample_size`.
- UGC de pessoa identificável sem permissão não vai para peça paga — vira veto.
- Comentário recortado não pode mudar de sentido; contexto crítico não vira elogio.
- Conformidade com [`../docs/compliance-policy.md`](../docs/compliance-policy.md): endorsements honestos (FTC) e publicidade não enganosa (CDC).

## Liga com

- [`testimonial-vault.md`](testimonial-vault.md) — a fala individual com permissão formal.
- [`credibility-builders.md`](credibility-builders.md) e [`data-points-bank.md`](data-points-bank.md).
- [`proof-asset-index.md`](proof-asset-index.md) — índice-mestre que reúne tudo.
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (dono), [`avatar-voc-investigator`](../agents/avatar-voc-investigator.md) (colhe UGC), [`compliance-auditor`](../agents/compliance-auditor.md) (veto).
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md), [`objection-registry`](../data/registries/objection-registry.md).
