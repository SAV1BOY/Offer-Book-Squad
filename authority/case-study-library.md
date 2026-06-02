---
id: authority.case-study-library
title: "Biblioteca de Estudos de Caso"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
tags: [authority, case-study, proof, narrative, before-after, evidence]
---

# Biblioteca de Estudos de Caso

## Propósito

Esta biblioteca guarda os **estudos de caso** do squad — a história completa de um cliente que saiu de um ponto A doloroso para um ponto B desejado, com o mecanismo no meio e o número no fim. O caso é a prova mais persuasiva que existe: ele mostra o resultado dentro de um contexto humano que o avatar reconhece como o seu.

O dono é o [`proof-credibility-curator`](../agents/proof-credibility-curator.md). Cada caso aqui precisa de um resultado verificável por trás (ver [`results-database.md`](results-database.md)) e de permissão de uso do protagonista. Um caso sem número checável é história bonita, não prova — e o [`compliance-auditor`](../agents/compliance-auditor.md) trata assim.

A biblioteca serve os escritores de copy que constroem a VSL, a sequência de e-mail e o mailer. Eles puxam o caso certo para a objeção certa: o caso de quem "não tinha tempo" desarma a objeção de tempo; o de quem "já tinha tentado tudo" desarma o ceticismo.

## Estrutura / Schema

Cada caso é um registro com a narrativa estruturada em beats. Campos a registrar:

| Campo | O que registrar |
|---|---|
| `case_id` | slug único, ex.: `caso-joao-agencia-2x` |
| `protagonist` | nome/perfil do cliente (com consentimento) |
| `avatar_match` | qual segmento de avatar ele representa |
| `before_state` | a dor concreta no ponto A (números, sensação) |
| `obstacle` | o que ele já tentou e por que falhou |
| `mechanism_used` | o mecanismo único aplicado |
| `after_state` | o resultado no ponto B |
| `result_id` | ref ao número em [`results-database.md`](results-database.md) |
| `objections_addressed` | quais objeções este caso desarma |
| `consent_status` | `pending` \| `granted` \| `revoked` |
| `media_assets` | fotos, vídeo, prints (links) |
| `proof_id` | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |

### Esqueleto de um caso

```
## Caso: {{case_id}}
- Quem: {{protagonist}} — representa {{avatar_match}}
- Antes: {{before_state}}
- Tentou e falhou: {{obstacle}}
- Mecanismo: {{mechanism_used}}
- Depois: {{after_state}} (fonte: {{result_id}})
- Desarma: {{objections_addressed}}
- Permissão: {{consent_status}} · Mídia: {{media_assets}}
```

## Como coletar & verificar

1. Selecione clientes com resultado forte e jornada clara (ponto A→B nítido).
2. Entreviste para extrair os beats — foque na dor inicial e no momento de virada.
3. Vincule o número final a uma linha verificável em [`results-database.md`](results-database.md).
4. Colha permissão de uso escrita (imagem, nome, dados) antes de publicar.
5. Marque quais objeções o caso desarma — isso guia o reuso na copy.
6. Espelhe no [`proof-registry`](../data/registries/proof-registry.md) com `proof_type: case-study`.

## Regras de uso & compliance

- Todo caso publicável tem `consent_status: granted` e `result_id` verificável.
- Resultado atípico no caso exige disclaimer "resultados variam", conforme [`../docs/compliance-policy.md`](../docs/compliance-policy.md).
- Não invente, não exagere, não componha caso "representativo" sem marcar como ilustrativo.
- Setor de saúde: sem alegação de cura; setor financeiro: sem promessa de ganho.
- Caso sem prova numérica por trás = **veto** do [`compliance-auditor`](../agents/compliance-auditor.md).

## Liga com

- [`results-database.md`](results-database.md) — o número que sustenta o caso.
- [`testimonial-vault.md`](testimonial-vault.md) — a fala do cliente dentro do caso.
- [`social-proof-inventory.md`](social-proof-inventory.md) e [`proof-asset-index.md`](proof-asset-index.md).
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md), [`compliance-auditor`](../agents/compliance-auditor.md), escritores de copy do D4.
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`objection-registry`](../data/registries/objection-registry.md).
- Framework: [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md).
