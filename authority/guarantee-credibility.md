---
id: authority.guarantee-credibility
title: "A Garantia como Construtora de Confiança"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
tags: [authority, guarantee, risk-reversal, trust, credibility, proof]
---

# A Garantia como Construtora de Confiança

## Propósito

Este arquivo explica **como a garantia constrói confiança e autoridade** — não como ela reverte risco no funil (isso vive na taxonomia), mas como ela funciona como sinal de prova. Uma garantia forte diz ao avatar algo que nenhuma promessa diz: "estou tão certo do resultado que assumo o risco por você". A garantia honrada vira ativo de credibilidade; a garantia exagerada que a operação não cumpre vira passivo de marca.

O dono aqui é o [`proof-credibility-curator`](../agents/proof-credibility-curator.md), que trata a garantia como prova de confiança e cataloga o histórico de cumprimento. A escolha do tipo de garantia pertence ao desenho da oferta — ver os 13 tipos em [`../lib/taxonomies/guarantee-types.md`](../lib/taxonomies/guarantee-types.md). A regra inegociável: a garantia precisa ser **real e exequível**. Garantia que a operação não honra vira veto do [`compliance-auditor`](../agents/compliance-auditor.md).

A credibilidade da garantia depende de duas provas: a clareza dos termos (sem letra miúda que esvazia a promessa) e o histórico de cumprimento (taxa de reembolso honrado, casos de garantia acionada e paga). Esse histórico é, ele próprio, prova de autoridade.

## Estrutura / Schema

Registre como cada garantia constrói (ou arrisca) confiança. Campos:

| Campo | O que registrar |
|---|---|
| `guarantee_cred_id` | slug único, ex.: `gar-cred-reembolso-30d` |
| `guarantee_type` | ref a um dos 13 tipos em [`../lib/taxonomies/guarantee-types.md`](../lib/taxonomies/guarantee-types.md) |
| `terms_clarity` | os termos exatos, em linguagem simples (sem pegadinha) |
| `is_operable` | a operação consegue honrar? (`true`/`false`) |
| `fulfillment_history` | histórico: pedidos de garantia recebidos e honrados |
| `redemption_rate` | taxa de acionamento (prova de honestidade dos termos) |
| `trust_signal` | a frase que comunica a garantia como confiança |
| `proof_link` | evidência de cumprimento (registros, prints) |
| `proof_id` | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |

### Tracker (semeado vazio)

| guarantee_cred_id | guarantee_type | is_operable | redemption_rate | proof_id |
|---|---|---|---|---|
| `gar-cred-exemplo-0001` _(EXEMPLO — apagar)_ | reembolso-sem-perguntas | true | 4% | `proof-exemplo-0001` |

## Como coletar & verificar

1. Confirme com a operação que a garantia é **exequível** — quem processa, em quanto tempo, com que custo absorvido. Sem isso, `is_operable: false` e a garantia não sai.
2. Escreva os `terms_clarity` em linguagem simples; letra miúda que esvazia a promessa destrói confiança quando descoberta.
3. Acompanhe o `fulfillment_history` e a `redemption_rate` — uma taxa saudável e honrada é prova de que a garantia é real.
4. Guarde evidência de cumprimento (registros de reembolso, casos honrados) como prova de autoridade.
5. Espelhe no [`proof-registry`](../data/registries/proof-registry.md) e ligue ao claim de garantia no [`claim-registry`](../data/registries/claim-registry.md).

## Regras de uso & compliance

- Garantia comunicada na copy é **real e exequível**; promessa que a operação não honra = **veto** do [`compliance-auditor`](../agents/compliance-auditor.md).
- Os termos não podem ter pegadinha que esvazie a promessa — isso é enganoso (CDC), conforme [`../docs/compliance-policy.md`](../docs/compliance-policy.md).
- Em setores regulados, garantia não vira promessa de cura ou de ganho (Anvisa, CVM, códigos de ética).
- "Todas as vendas são finais" só com motivo verdadeiro e claro (ver tipo 12 da taxonomia).
- Histórico de cumprimento usado como prova segue as mesmas regras de consentimento e verificabilidade dos demais ativos.

## Liga com

- [`../lib/taxonomies/guarantee-types.md`](../lib/taxonomies/guarantee-types.md) — os 13 tipos de garantia (a escolha do tipo).
- [`results-database.md`](results-database.md) — resultados que dão segurança para garantir.
- [`credibility-builders.md`](credibility-builders.md) e [`proof-asset-index.md`](proof-asset-index.md).
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (dono), [`compliance-auditor`](../agents/compliance-auditor.md) (exequibilidade + veto), [`unit-economics-stack-analyst`](../agents/unit-economics-stack-analyst.md) (escolhe o tipo no stack), [`pr-brand-strategist`](../agents/pr-brand-strategist.md).
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md).
- Frameworks: [`risk-reversal-ladder`](../frameworks/risk-reversal-ladder.md), [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md).
