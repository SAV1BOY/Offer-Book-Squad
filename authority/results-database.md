---
id: authority.results-database
title: "Banco de Resultados Verificáveis"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
tags: [authority, results, proof, verifiable, tracker, evidence]
---

# Banco de Resultados Verificáveis

## Propósito

Este é o banco central dos **números de resultado** que o squad pode usar como prova — receita gerada, peso perdido, leads captados, ROI de cliente, tempo economizado. Cada linha existe para sustentar um claim com lastro. O princípio é direto: nenhum resultado entra aqui sem fonte verificável. Sem isso, o [`compliance-auditor`](../agents/compliance-auditor.md) veta o uso na copy.

O dono é o [`proof-credibility-curator`](../agents/proof-credibility-curator.md). Ele cataloga cada resultado, mede a força da evidência e marca o status de verificação. O banco serve a todos os escritores de copy (VSL, e-mail, mailer, anúncio) que precisam de um número concreto para vencer ceticismo. Um número forte e checável move a alavanca de prova mais que qualquer adjetivo.

Este banco é a camada de números do [`proof-registry`](../data/registries/proof-registry.md). Onde o registro guarda toda prova (depoimento, caso, print), este arquivo isola os **dados numéricos de resultado** e exige a fonte que os torna defensáveis.

## Estrutura / Schema

Registre cada resultado como uma linha no tracker. Colunas obrigatórias:

| Coluna | Tipo | O que registrar |
|---|---|---|
| `result_id` | slug | id único, ex.: `result-cliente-ana-3x-roi` |
| `metric` | string | a métrica medida (receita, kg, leads, %) |
| `value` | número + unidade | o valor exato, ex.: `R$ 142.000` ou `12 kg` |
| `timeframe` | string | janela do resultado, ex.: `90 dias` |
| `subject` | string | quem obteve (cliente, conta, coorte) |
| `baseline` | string | ponto de partida (de onde saiu) |
| `source_type` | enum | `print-painel` \| `nota-fiscal` \| `estudo` \| `relato-assinado` \| `dado-plataforma` |
| `source_link` | path/URL | onde a fonte vive (checável) |
| `verifiable` | bool | há como um terceiro conferir? |
| `is_atypical` | bool | resultado fora da média? (exige disclaimer) |
| `consent_status` | enum | `pending` \| `granted` \| `revoked` |
| `proof_id` | ref | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |
| `updated` | data | `YYYY-MM-DD` |

### Tracker (semeado vazio)

| result_id | metric | value | timeframe | subject | source_type | verifiable | is_atypical | consent_status | proof_id | updated |
|---|---|---|---|---|---|---|---|---|---|---|
| `result-exemplo-0001` _(EXEMPLO — apagar)_ | receita | R$ 142.000 | 90 dias | Cliente Ana (amostra) | print-painel | true | true | granted | `proof-exemplo-0001` | 2026-06-02 |

## Como coletar & verificar

1. Peça a fonte primária ao cliente: print do painel, nota, extrato, relato assinado.
2. Anexe o arquivo em `source_link` e confirme que um terceiro consegue conferir.
3. Marque `is_atypical: true` se o número está acima da média — isso obriga disclaimer "resultados variam".
4. Registre `consent_status` e só use na copy quando for `granted`.
5. Espelhe a linha no [`proof-registry`](../data/registries/proof-registry.md) com `proof_type: data` e o `strength` (forte = específico + checável).

## Regras de uso & compliance

- Todo resultado usado em copy aponta para uma linha aqui com `verifiable: true` (princípio `evidence_before_opinion`).
- Resultado atípico **sempre** acompanha disclaimer, conforme [`../docs/compliance-policy.md`](../docs/compliance-policy.md) (seção Disclaimers).
- Sem `consent_status: granted`, o resultado não vai para peça pública.
- Número sem fonte = **veto** do [`compliance-auditor`](../agents/compliance-auditor.md). Não há override para claim sem lastro.
- Setores regulados (saúde, finanças): sem promessa de cura ou de ganho garantido, mesmo com fonte.

## Liga com

- [`proof-asset-index.md`](proof-asset-index.md) — índice-mestre que aponta para este banco.
- [`case-study-library.md`](case-study-library.md) — o caso narra o resultado que aqui é número.
- [`data-points-bank.md`](data-points-bank.md) — estatísticas de mercado vs. resultados próprios.
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (dono), [`compliance-auditor`](../agents/compliance-auditor.md) (veto), [`pr-brand-strategist`](../agents/pr-brand-strategist.md) (usa em pauta).
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md).
- Framework: [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md).
