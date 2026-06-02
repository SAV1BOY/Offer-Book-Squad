---
id: checklist.proof-checklist
title: "Checklist — Prova & Credibilidade (cada claim e objeção com prova ou plano de coleta)"
type: checklist
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
frameworks: [proof-to-claim-chain]
registries: [proof-registry, claim-registry, objection-registry]
tags: [checklist, prova, credibilidade, claim, objecao, proof-gap, d1]
---

# Checklist — Prova & Credibilidade

## Propósito
Este checklist prova que **nenhum claim forte vive sem prova catalogada** por trás, e que cada objeção do comprador tem uma prova que a desarma. Existe porque copy que afirma o que não pode provar é mentira que o `compliance-auditor` veta lá na frente — então a prova é caçada aqui, na inteligência. Cada claim e cada objeção recebe ou uma prova classificada por força (especificidade + verificabilidade) ou um **plano de coleta** explícito quando a prova ainda não existe. Sem este checklist verde, a oferta promete no escuro. Ele encarna `evidence_before_opinion` e é a primeira linha de defesa do compliance: o que não se prova aqui, não entra na copy.

## Dono & Escopo
- **owner_agent:** `proof-credibility-curator` (inventaria e classifica a prova, casa prova a claim/objeção, reporta proof-gaps).
- **Artefato inspecionado:** o `artifact.proof-bank`, a `artifact.proof-claim-matrix` e o `artifact.proof-gap-report`, com prova e claims registrados no [`proof-registry`](../data/registries/proof-registry.md) e no [`claim-registry`](../data/registries/claim-registry.md).

## Condição de Passagem
Cada claim tem prova catalogada ou plano de coleta, cada objeção dominante tem prova que a desarma, e cada proof-gap está reportado em vez de escondido.

## Itens
1. **Inventário de prova montado.** Como verificar: o `proof-registry` lista depoimentos, casos, dados, prints, demos e autoridade com fonte por item, conforme `proof-to-claim-chain`.
2. **Força classificada por prova.** Como verificar: cada prova tem nota de força (fraca/média/forte) por especificidade + verificabilidade; depoimento vago = fraco, caso com número auditável = forte.
3. **Claim ↔ prova casados.** Como verificar: cada `claim_id` no `claim-registry` aponta para ≥1 `proof_id` no `proof-registry`, ou para um plano de coleta datado.
4. **Objeção ↔ prova casadas.** Como verificar: cada objeção dominante do `objection-registry` tem a prova que a neutraliza identificada.
5. **Proof-gaps reportados.** Como verificar: todo claim sem prova aparece no proof-gap-report como gap explícito — nunca silenciado nem assumido como verdadeiro.
6. **Plano de coleta para gaps.** Como verificar: cada gap tem um plano (que prova coletar, de quem, até quando) ou o claim é cortado.
7. **Fonte checável por prova.** Como verificar: cada prova forte tem origem verificável (link, documento, contato), não "ouvi dizer".
8. **Sem claim inflado.** Como verificar: nenhum número está arredondado para cima sem lastro; a prova sustenta o número exato usado.

## Evidência Exigida
Para marcar ✅: linkar o `proof-registry` com a classificação de força (itens 1–2), a matriz claim→proof sem órfãos no `claim-registry` (item 3), a tabela objeção→prova (item 4) e o proof-gap-report com planos de coleta datados (itens 5–6). Cada prova forte exige a fonte checável anexada (item 7).

## Protocolo de Falha
Item vermelho → o banco de prova volta ao `proof-credibility-curator` com o gap nomeado e **bloqueia o uso do claim** em D4. Claim sem prova e sem plano de coleta é cortado, não maquiado. Re-entrada: coletar a prova ou cortar o claim, atualizar `proof-registry` e `claim-registry`, re-submeter. O `compliance-auditor` herda esta tabela: qualquer órfão que escape aqui é vetado na auditoria final.

## Links
- Frameworks: [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md)
- Registries: [`proof-registry`](../data/registries/proof-registry.md) · [`claim-registry`](../data/registries/claim-registry.md) · [`objection-registry`](../data/registries/objection-registry.md)
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md) · [`avatar-voc-investigator`](../agents/avatar-voc-investigator.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Gate por agente: [`proof/proof-claim-backing-gate`](proof/proof-claim-backing-gate.md)
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate relacionado: [`offer-book-stack/intelligence-complete-gate`](offer-book-stack/intelligence-complete-gate.md)
