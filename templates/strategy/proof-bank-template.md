---
id: template.strategy.proof-bank
title: "Proof Bank — Banco de Prova por Claim"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
consumes: [template.strategy.market-brief, template.strategy.avatar-icp]
produces: [template.core.offer-book-master]
frameworks: [proof-to-claim-chain]
checklists: [proof/proof-claim-backing-gate]
registries: [proof-registry, claim-registry]
tags: [template, proof, claim-backing, credibility, strategy]
---

# Proof Bank — Banco de Prova por Claim

Este template amarra **cada afirmação** da oferta a uma **evidência** que a sustenta. A regra do squad é dura: nenhum claim sem lastro (`evidence_before_opinion`). Um claim sozinho é opinião e vira passivo de compliance; um claim com prova é argumento. O banco cataloga toda a prova disponível, casa cada uma a um claim, mede a força e expõe os órfãos — claims grandes sem nada por trás.

## Como usar
- **Agente dono:** `proof-credibility-curator` (camada D1).
- **Task:** `curate-proof`. Consome o [`market-brief`](market-brief-template.md), o [`avatar-icp`](avatar-icp-template.md) e os ativos de prova (depoimentos, dados, estudos, demos).
- **Quando:** depois do avatar, antes/durante a arquitetura de oferta. Alimenta o bloco 4 ("PROVA") do [`offer-book-master`](../core/offer-book-master.md). Validado pelo [`proof-claim-backing-gate`](../../checklists/proof/proof-claim-backing-gate.md). Usa o [`proof-block`](../../lib/components/proof-block.md) como unidade.
- Regra: prova **específica** casa com claim específico — se o claim diz "30 dias", a prova mostra "30 dias". Cada par vai para o [`proof-registry`](../../data/registries/proof-registry.md) e o [`claim-registry`](../../data/registries/claim-registry.md).

## Campos & Instruções
- **{{CLAIM}}** — a afirmação exata, como aparece (ou aparecerá) na copy. Vem do `claim-registry`.
- **{{TIPO_PROVA}}** — o tipo: DEPOIMENTO, NÚMERO, DEMONSTRAÇÃO, ESTUDO, ANTES_DEPOIS, AUTORIDADE. Via [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md).
- **{{A_PROVA}}** — a evidência concreta e específica (não "muita gente gostou" — "+21% em 142 lojas").
- **{{FONTE_RASTRO}}** — onde verificar: id do `proof-registry`, print, link, nome do cliente.
- **{{FORCA}}** — FRACA / MÉDIA / FORTE, com a justificativa (amostra, especificidade, se é mediana ou cereja).
- **{{LASTRO_OK}}** — SIM/NÃO: o claim tem prova suficiente para ir à copy.
- **{{N_CLAIMS_TOTAL}}** / **{{N_CLAIMS_OK}}** — quantos claims existem e quantos têm lastro.
- **{{FORCA_MEDIA}}** — a força média da cobertura (a "saúde" da prova do projeto).
- **{{ORFAOS}}** — os claims grandes **sem** prova suficiente. Nenhum claim grande pode ficar órfão.
- **{{ACAO_PARA_ORFAOS}}** — o que fazer com cada órfão: coletar prova, suavizar o claim, ou cortar.

## O Template
```
# PROOF BANK — {{NOME_DA_OFERTA}}
Owner: proof-credibility-curator · Data: {{DATA}}

## TABELA CLAIM → PROVA  (component: proof-block · framework: proof-to-claim-chain)
| # | Claim (exato) | Tipo | A prova (específica) | Fonte/rastro | Força | Lastro OK? |
|---|---|---|---|---|---|---|
| 1 | "{{CLAIM_1}}" | {{TIPO_1}} | {{PROVA_1}} | {{FONTE_1}} | {{FORCA_1}} | {{OK_1}} |
| 2 | "{{CLAIM_2}}" | {{TIPO_2}} | {{PROVA_2}} | {{FONTE_2}} | {{FORCA_2}} | {{OK_2}} |
| 3 | "{{CLAIM_3}}" | {{TIPO_3}} | {{PROVA_3}} | {{FONTE_3}} | {{FORCA_3}} | {{OK_3}} |
| ... | ... | ... | ... | ... | ... | ... |

## COBERTURA
Claims com lastro: {{N_CLAIMS_OK}} / {{N_CLAIMS_TOTAL}}
Força média: {{FORCA_MEDIA}}
Claims órfãos (sem prova suficiente): {{ORFAOS_OU_NENHUM}}

## PLANO PARA ÓRFÃOS
{{CLAIM_ORFAO}} → ação: {{COLETAR_PROVA | SUAVIZAR_CLAIM | CORTAR}}
```

## Exemplo preenchido
> **# PROOF BANK — Motor de Recuperação 72h**
> Owner: proof-credibility-curator · Data: 2026-06-02
>
> | # | Claim | Tipo | A prova | Fonte/rastro | Força | Lastro OK? |
> |---|---|---|---|---|---|---|
> | 1 | "recupera +15% da receita perdida" | NÚMERO + ANTES_DEPOIS | 142 lojas, mediana +21% em 30 dias | proof-registry #PR-031; painel em anexo | FORTE | SIM |
> | 2 | "funciona em qualquer nicho" | DEPOIMENTO | casos em 9 nichos distintos | proof-registry #PR-033; 9 depoimentos | MÉDIA | SIM |
> | 3 | "setup feito-para-você em 72h" | DEMONSTRAÇÃO | vídeo de onboarding real cronometrado | proof-registry #PR-022 | FORTE | SIM |
> | 4 | "primeiro resultado em 7 dias" | ANTES_DEPOIS | 6 lojas com print do dia 7 | proof-registry #PR-035 | MÉDIA | SIM |
> | 5 | "o maior salto de lucro do mercado" | — | sem dado comparativo | — | — | NÃO |
> | 6 | "garantia dobro do dinheiro" | AUTORIDADE | termo de garantia público + margem | proof-registry #PR-031 | FORTE | SIM |
>
> **COBERTURA** — Claims com lastro: **5/6** · Força média: **forte**. Órfão: claim 5 ("o maior salto de lucro do mercado").
> **PLANO PARA ÓRFÃOS** — Claim 5 → ação: **suavizar o claim** para "um dos maiores saltos que medimos", pois não há benchmark de mercado verificável.

## DoD do entregável
O Proof Bank está pronto quando: (1) **todo** claim grande da oferta aparece na tabela com seu par de prova; (2) cada prova é específica e **casa** com o claim (mesmo número, mesmo prazo) — prova genérica para claim específico não conta; (3) cada linha tem tipo, fonte/rastro verificável e força justificada (gate `proof-claim-backing-gate`); (4) a cobertura está calculada (quantos OK de quantos) e a força média declarada; (5) **nenhum** claim grande fica órfão no estado final — todo órfão tem ação registrada (coletar, suavizar ou cortar); (6) cada par claim→prova está espelhado no [`claim-registry`](../../data/registries/claim-registry.md) e [`proof-registry`](../../data/registries/proof-registry.md). Só então alimenta o bloco "PROVA" do [`offer-book-master`](../core/offer-book-master.md). O `compliance-auditor` **veta** qualquer claim sem lastro que vaze para a copy.
