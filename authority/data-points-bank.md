---
id: authority.data-points-bank
title: "Banco de Dados e Estatísticas"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
tags: [authority, data, statistics, market, proof, sources, evidence]
---

# Banco de Dados e Estatísticas

## Propósito

Este é o banco de **estatísticas e pontos de dados** que o squad usa para sustentar argumentos — tanto dados **próprios** (gerados pela operação) quanto dados de **mercado** (estudos, institutos, relatórios setoriais). Um número certo no lugar certo cria autoridade e dimensiona o problema: "73% das pessoas com X falham por Y" justifica o mecanismo antes do pitch. A regra de ouro: todo dado aqui tem fonte citável.

O dono é o [`proof-credibility-curator`](../agents/proof-credibility-curator.md). Ele separa o que é dado próprio (resultado agregado da base, pesquisa interna) do que é dado de terceiro (estudo, IBGE, relatório). Cada categoria exige fonte: a interna aponta para o painel ou a metodologia; a externa aponta para a publicação original com autor, ano e URL. Dado sem fonte vira veto do [`compliance-auditor`](../agents/compliance-auditor.md).

O banco serve a copy (estatística de abertura, dimensionamento do problema), o [`media-kit.md`](media-kit.md) e o pitch de PR. Ele se distingue do [`results-database.md`](results-database.md): aquele guarda resultados de cliente; este guarda estatísticas que enquadram o problema e o mercado.

## Estrutura / Schema

Registre cada ponto de dado como uma linha. Colunas obrigatórias:

| Coluna | Tipo | O que registrar |
|---|---|---|
| `data_id` | slug | id único, ex.: `data-mercado-falha-73pct` |
| `statement` | string | o dado em uma frase (ex.: `73% abandonam no 1º mês`) |
| `value` | número + unidade | o número exato com unidade |
| `data_origin` | enum | `próprio` \| `mercado` |
| `source_full` | string | autor, título, ano (bloco de citação) |
| `source_url` | URL | link para a fonte primária |
| `access_date` | data | quando a fonte foi acessada |
| `methodology` | string | como o dado foi obtido (amostra, período) — obrigatório se `próprio` |
| `verifiable` | bool | terceiro consegue conferir? |
| `proof_id` | ref | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |

### Tracker (semeado vazio)

| data_id | statement | value | data_origin | source_full | source_url | verifiable | proof_id |
|---|---|---|---|---|---|---|---|
| `data-exemplo-0001` _(EXEMPLO — apagar)_ | 73% abandonam no 1º mês (amostra) | 73% | mercado | Instituto X, *Relatório* (2025) | https://exemplo | true | `proof-exemplo-0001` |

## Como coletar & verificar

1. Para dado de mercado, vá à fonte primária — não cite a citação. Registre `source_full`, `source_url` e `access_date` no formato do bloco de citação do [`../docs/style-guide.md`](../docs/style-guide.md).
2. Para dado próprio, documente a `methodology`: tamanho da amostra, período, como foi medido. Sem método, o número não é defensável.
3. Confirme que o número não foi tirado de contexto — verifique o que a fonte realmente mede.
4. Marque `verifiable: false` em dado sem fonte sólida; ele não entra na copy.
5. Espelhe no [`proof-registry`](../data/registries/proof-registry.md) com `proof_type: data` e o `strength`.

## Regras de uso & compliance

- Todo dado usado em copy tem fonte citável e `verifiable: true` (princípio `evidence_before_opinion`).
- Dado de mercado citado fora de contexto, ou número sem fonte = **veto** do [`compliance-auditor`](../agents/compliance-auditor.md).
- Dado próprio exige metodologia declarada; "nossa pesquisa mostra" sem método é frágil.
- Citação literal de relatório ≤ 25 palavras, atribuída, conforme [`../docs/compliance-policy.md`](../docs/compliance-policy.md) (anti-plágio).
- Setores regulados: estatística não vira promessa implícita de resultado individual.

## Liga com

- [`results-database.md`](results-database.md) — resultados de cliente (não confundir com estatística de mercado).
- [`social-proof-inventory.md`](social-proof-inventory.md), [`credibility-builders.md`](credibility-builders.md), [`media-kit.md`](media-kit.md).
- [`proof-asset-index.md`](proof-asset-index.md) — índice-mestre.
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (dono), [`pr-brand-strategist`](../agents/pr-brand-strategist.md) (usa em pauta), [`compliance-auditor`](../agents/compliance-auditor.md) (veto). Consumido pelos escritores do D4.
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md).
- Framework: [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md).
