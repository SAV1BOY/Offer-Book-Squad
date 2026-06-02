---
id: project.offer-book-project.03-proof
title: "Fase 03 — Prova & Credibilidade"
type: project-phase
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
consumes:
  - artifact.objection-belief-map
  - artifact.market-brief
  - template.strategy.proof-bank
produces:
  - artifact.proof-bank
  - artifact.proof-claim-matrix
  - artifact.proof-gap-report
tags: [project-phase, intelligence, prova, credibilidade, claim, proof-to-claim, gap, d1]
---

# Fase 03 — Prova & Credibilidade

## Objetivo da Fase
Montar o arsenal de prova e casar cada prova a um claim e a uma objeção. Esta fase devolve o banco de prova classificado por força e proveniência, a matriz prova × claim/objeção com a melhor munição em cada linha, e o relatório de proof-gaps — o que a oferta ainda não pode afirmar. O estado-pronto é simples: a copy nunca afirmará o que não consegue provar, e cada objeção de alta severidade já tem sua munição escolhida. Esta fase fecha a camada D1 e libera a arquitetura de oferta. Sem prova catalogada, o mecanismo da Fase 04 não nasce com lastro.

## Critério de Entrada
A Fase 02 entrega o `artifact.objection-belief-map` (a lista do que a prova precisa desarmar, com falsa crença e severidade) e o `artifact.market-brief` da Fase 01 (o estágio de sofisticação — 3 a 5 exige prova de mecanismo, não só de resultado). Pré-condição: o mapa de objeções está verde, porque curo prova contra as objeções e claims, nunca no vácuo. Sem inventário de prova acessível, o banco fica abaixo do piso e sinalizado — prova fabricada é falha grave. O [`proof-registry`](../../data/registries/proof-registry.md) e o [`claim-registry`](../../data/registries/claim-registry.md) são as fontes que esta fase escreve.

## Agentes & Tasks
- **Task [`curate-proof`](../../tasks/intelligence/curate-proof.md)** — dono [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). Inventaria, classifica, casa prova a claim/objeção e reporta os gaps. Sem poder de veto — sinaliza.

## Passos
1. Enumere os claims que a oferta fará e as objeções que pedem prova, as de alta severidade primeiro.
2. Inventarie cada peça de prova com tipo, resumo e fonte (depoimento, caso, dado, print, demo, endosso, menção de mídia).
3. Classifique a força com [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md): especificidade mais verificabilidade definem fraca, moderada ou forte. Classifique honesto — não infle.
4. Verifique a proveniência: consentimento, fonte checável, direito de uso. Sem autorização vira pendente e não usável.
5. Monte a matriz prova × claim/objeção; em B2B, agrupe por papel da DMU.
6. Escolha a munição principal com Tree-of-Thoughts: ≥3 candidatas pontuadas por especificidade, verificabilidade, ressonância com a emoção dominante e risco de compliance.
7. Identifique os proof-gaps: claim sem prova vira gap com severidade e recomendação (obter caso datado ou suavizar o claim).
8. Faça o self-verify com a pergunta central "o que o compliance rejeitaria?". Escreva o `proof-registry` e o `claim-registry` e passe o gate.

## Artefatos Produzidos
- `artifact.proof-bank` — inventário classificado por força e proveniência.
- `artifact.proof-claim-matrix` — cada claim/objeção com a melhor prova disponível (por papel da DMU, se B2B).
- `artifact.proof-gap-report` — o que não se pode afirmar, com objeção associada, prova faltante, severidade e recomendação.
- Registries escritos: [`proof-registry`](../../data/registries/proof-registry.md) e [`claim-registry`](../../data/registries/claim-registry.md).

## Gates
- [`proof/proof-claim-backing-gate`](../../checklists/proof/proof-claim-backing-gate.md) — cada claim grande com prova de força adequada ao estágio; cada objeção alta desarmada.

## Critério de Saída
Cada claim que a oferta fará tem ≥1 prova de força adequada (mecanismo provado nos estágios 3-4); cada objeção de alta severidade tem prova que a desarma; toda prova tem consentimento resolvido; os proof-gaps estão listados e priorizados; o gate está verde. Se um claim central permanece sem prova, esta fase não declara verde — entrega o gap como bloqueio sinalizado. A próxima fase é a [`04-mechanism`](04-mechanism.md), que recebe a prova de mecanismo disponível para nomear um mecanismo com lastro.
