---
id: checklist.proof.proof-claim-backing-gate
title: "Gate — Nenhum Claim Sem Lastro e Nenhuma Prova Órfã"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
frameworks: [proof-to-claim-chain]
registries: [proof-registry, claim-registry]
tags: [gate, proof, claim-backing, proof-to-claim, d1, compliance, lastro]
---

# Gate — Nenhum Claim Sem Lastro e Nenhuma Prova Órfã

## Propósito
Este é o gate central do `proof-credibility-curator` — a antecâmara do compliance. Ele prova que **toda afirmação que a oferta fará tem uma prova catalogada por trás** e que **nenhuma prova é órfã** (sem um claim ou objeção que ela sustente). Existe porque copy que afirma o que não pode provar é exatamente o que o `compliance-auditor` veta lá em D7 — então o curador pega o problema aqui, no D1, antes de virar copy mentirosa. Ele materializa a corrente [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md): toda prova existe **para** sustentar um claim, e todo claim forte **precisa** de prova de força adequada ao estágio de sofisticação (resultado nos estágios baixos; mecanismo nos estágios 3–4; identidade no 5). O gate também exige proveniência resolvida — consentimento e fonte checável — porque um depoimento sem autorização ou um número sem base amostral é não usável. É a primeira linha de defesa do squad contra o veto de claim sem lastro: alinha-se diretamente com o [`compliance-claim-backing-gate`](../compliance/compliance-claim-backing-gate.md).

## Dono & Escopo
- **owner_agent:** `proof-credibility-curator` (guardião da credibilidade; sem veto formal, sinaliza ao chief e ao compliance).
- **Artefato inspecionado:** a **matriz prova × claim/objeção** e o **proof-gap-report**, com cada prova no [`proof-registry`](../../data/registries/proof-registry.md) e cada claim no [`claim-registry`](../../data/registries/claim-registry.md).

## Condição de Passagem
Cada claim que a oferta fará tem ≥1 prova de força adequada ao estágio, nenhuma prova é órfã, toda prova tem proveniência resolvida, e os proof-gaps estão reportados com recomendação.

## Itens
1. **Nenhum claim órfão.** Verificar: na matriz, cada claim forte da oferta tem ≥1 prova casada no [`claim-registry`](../../data/registries/claim-registry.md) — nenhum claim sem lastro.
2. **Nenhuma prova órfã.** Verificar: toda prova no [`proof-registry`](../../data/registries/proof-registry.md) aponta para ≥1 `claim_id` ou objeção — nenhuma prova solta sem destino.
3. **Força casa com o estágio.** Verificar: aplicado [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md), o estágio 3–4 tem prova de **mecanismo** (não só de resultado) e o estágio 5 tem prova de **identidade/comunidade**.
4. **Classificação honesta de força.** Verificar: nenhuma prova vaga ou infalsificável está marcada `strong`; força = especificidade + verificabilidade (número, nome, data, fonte checável).
5. **Proveniência resolvida.** Verificar: cada prova tem `consent_status` (granted, não pending/revoked) e `verifiable: true` quando usada; prova sem autorização está fora de uso.
6. **Número com base.** Verificar: todo dado/estatística tem n e metodologia documentados — sem "87% melhoram" sem base amostral.
7. **Objeções de alta severidade cobertas.** Verificar: cada objeção `high` do mapa tem a melhor prova disponível como munição principal (em B2B, roteada por papel da DMU).
8. **Proof-gaps reportados.** Verificar: claims/objeções sem prova suficiente estão no proof-gap-report com severidade e recomendação (obter prova ou suavizar/remover o claim).

## Evidência Exigida
Para marcar cada item ✅, linkar a matriz prova × claim/objeção (cada claim/objeção com prova principal + reforços), o [`proof-registry`](../../data/registries/proof-registry.md) (com `proof_type`, `strength`, `consent_status`, `verifiable`, `claim_ids`) e o [`claim-registry`](../../data/registries/claim-registry.md) (cada claim com a prova que o sustenta). O proof-gap-report com `{claim, objeção associada, prova faltante, severidade, recomendação}` é a evidência-resumo do que **não** se pode afirmar.

## Protocolo de Falha
Item vermelho → não declara verde. Claim órfão → abre proof-gap e **bloqueio sinalizado**; não deixa passar para a copy. Prova órfã → descarta ou arquiva a que não serve a nenhum claim. Prova inflada (vaga marcada `strong`) → rebaixa a força exigindo especificidade + verificabilidade. Número sem base → marca não usável até a metodologia ser documentada. Prova sem consentimento → `consent_status: pending`, fora de uso até liberar. Descompasso de estágio (sofisticação 4 só com prova de resultado) → busca prova de mecanismo ou abre gap para o [`mechanism-architect`](../../agents/mechanism-architect.md). O curador **não tem veto**: sinaliza ao [`offerbook-chief`](../../agents/offerbook-chief.md) e ao [`compliance-auditor`](../../agents/compliance-auditor.md) (que tem o veto em D7). Re-entrada: obtida a prova ou suavizado o claim, o gate é re-submetido.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`proof-registry`](../../data/registries/proof-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md)
- Agentes: [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`compliance-auditor`](../../agents/compliance-auditor.md) · [`mechanism-architect`](../../agents/mechanism-architect.md)
- Alinhamento com compliance: [`compliance-claim-backing-gate`](../compliance/compliance-claim-backing-gate.md) · [`compliance-disclaimers-gate`](../compliance/compliance-disclaimers-gate.md)
- Gates irmãos: [`proof-coverage-gate`](proof-coverage-gate.md) · [`proof-objection-coverage-gate`](proof-objection-coverage-gate.md) · [`proof-source-credibility-gate`](proof-source-credibility-gate.md) · [`proof-permission-gate`](proof-permission-gate.md)
