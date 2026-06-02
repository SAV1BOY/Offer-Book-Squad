---
id: authority.pr-placements
title: "Colocações de Imprensa"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
tags: [authority, pr, media, press, placement, credibility]
---

# Colocações de Imprensa

## Propósito

Este arquivo cataloga cada **colocação de imprensa** que a marca ou o fundador conquistou — matéria, entrevista, citação, participação em podcast, coluna assinada, prêmio noticiado. A colocação de imprensa é um sinal de autoridade emprestada: quando um veículo respeitado cita a marca, parte da confiança dele se transfere para nós. O avatar baixa a guarda antes do pitch.

O dono é o [`pr-brand-strategist`](../agents/pr-brand-strategist.md), que prospecta veículos, faz o pitch e registra cada conquista. A regra inegociável: cada colocação aqui é **real e verificável** por um link vivo. "Visto na Forbes" sem matéria que o sustente é enganoso e vira veto do [`compliance-auditor`](../agents/compliance-auditor.md). Logo de veículo só entra na copy quando há cobertura real por trás dele.

Estas colocações alimentam os [`credibility-builders.md`](credibility-builders.md), o [`media-kit.md`](media-kit.md) e a faixa de "como visto em" no topo da VSL e da página. Elas não substituem prova de resultado; elas abrem a porta de confiança para que a prova entre.

## Estrutura / Schema

Registre cada colocação como uma linha no tracker. Colunas obrigatórias:

| Coluna | Tipo | O que registrar |
|---|---|---|
| `placement_id` | slug | id único, ex.: `pr-forbes-coluna-2026` |
| `outlet` | string | veículo (Forbes, Exame, podcast X) |
| `outlet_tier` | enum | `tier-1` \| `tier-2` \| `nicho` (alcance/prestígio) |
| `format` | enum | `matéria` \| `entrevista` \| `citação` \| `podcast` \| `coluna` \| `menção` |
| `headline` | string | título ou ângulo da peça |
| `spokesperson` | string | quem representou a marca |
| `publish_date` | data | `YYYY-MM-DD` |
| `live_url` | URL | link vivo da peça (checável) |
| `archive_link` | URL/path | print ou cópia arquivada (caso saia do ar) |
| `reuse_rights` | enum | `livre` \| `com-crédito` \| `restrito` (uso do logo/trecho) |
| `proof_id` | ref | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |

### Tracker (semeado vazio)

| placement_id | outlet | outlet_tier | format | publish_date | live_url | reuse_rights | proof_id |
|---|---|---|---|---|---|---|---|
| `pr-exemplo-0001` _(EXEMPLO — apagar)_ | Exame (amostra) | tier-1 | entrevista | 2026-06-02 | https://exemplo | com-crédito | `proof-exemplo-0001` |

## Como coletar & verificar

1. Registre cada conquista no momento em que sai — capture o `live_url` e um `archive_link` (print da página completa).
2. Confirme que o link está vivo e que a marca aparece de fato; matéria que sumiu sem arquivo perde o lastro.
3. Classifique o `outlet_tier` por alcance e prestígio — tier-1 brilha no topo da página.
4. Verifique os `reuse_rights` do veículo antes de usar logo ou trecho; alguns exigem crédito ou proíbem reuso comercial.
5. Espelhe a linha no [`proof-registry`](../data/registries/proof-registry.md) com `proof_type: media-mention` e o `strength`.

## Regras de uso & compliance

- Toda colocação usada em copy tem `live_url` ativo ou `archive_link` que prova a cobertura.
- Faixa "como visto em" só lista veículos com peça real; logo sem matéria = enganoso = **veto** do [`compliance-auditor`](../agents/compliance-auditor.md).
- Respeite os `reuse_rights`: usar logo de veículo sem direito viola marca de terceiro.
- Não distorça o tom da peça — citação crítica não pode virar elogio recortado.
- Conformidade com [`../docs/compliance-policy.md`](../docs/compliance-policy.md): publicidade não enganosa (CDC) e endorsements honestos (FTC).

## Liga com

- [`credibility-builders.md`](credibility-builders.md) — a colocação vira sinal de autoridade na copy.
- [`media-kit.md`](media-kit.md) — kit que facilita novas colocações e reúne as antigas.
- [`awards-certifications.md`](awards-certifications.md) e [`proof-asset-index.md`](proof-asset-index.md).
- Agentes: [`pr-brand-strategist`](../agents/pr-brand-strategist.md) (dono), [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (cataloga prova), [`compliance-auditor`](../agents/compliance-auditor.md) (veto).
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md).
