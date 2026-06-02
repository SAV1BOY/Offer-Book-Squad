---
id: project.full-launch-blackbook-project.01-offer-book
title: "Fase 01 — Offer Book Completo (★ HARD STOP de Entrada)"
type: project-phase
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes:
  - decision.project-type
  - decision.scope-one-sentence
  - artifact.offer-book-master-skeleton
  - artifact.case-pipeline
produces:
  - artifact.offer-book
  - decision.hard-stop-status
tags: [project-phase, full-launch, offer-book, hard-stop, dod-gate, d1, d2, d3]
---

# Fase 01 — Offer Book Completo (★ HARD STOP de Entrada)

## Objetivo da Fase
Produzir o Offer Book inteiro e cruzar o **★ HARD STOP de entrada**. Esta fase **incorpora o projeto [`offer-book-project`](../offer-book-project/00-brief.md) por completo** — as dez fases de mercado, avatar, prova, mecanismo, valor, money model, pricing/unit economics, Big Idea/posicionamento e a montagem com o `offer-book-stack/offer-book-dod-gate`. O estado-pronto é o Offer Book aprovado (gate VERDE): a fonte de verdade estratégica sobre a qual toda a copy, todo o funil e toda a logística do lançamento serão construídos. Nada de D4+ começa antes deste verde. É a fase mais longa e mais decisiva do lançamento — ~50-60% do esforço total mora aqui.

## Critério de Entrada
A Fase 00 entrega o `decision.project-type` (full-launch), a `decision.scope-one-sentence` travada, o `artifact.offer-book-master-skeleton` aberto e o `artifact.case-pipeline` com a posição desta trilha no DAG e o HARD STOP posicionado entre D3 e D4. Pré-condição: a frase de escopo não bifurca e o esqueleto está aberto. Esta fase executa internamente o composite `run-offer-book` — `intake-and-scope`, `run-market-intel`, `build-avatar-voc`, `curate-proof`, `define-mechanism`, `score-value-equation`, `set-pricing-wtp`, `model-unit-economics`, `design-money-model`, `generate-big-ideas`, `lock-positioning-lead` e `assemble-offer-book`. Os registries [`offer-registry`](../../data/registries/offer-registry.md) e [`decision-registry`](../../data/registries/decision-registry.md) são escritos ao longo das sub-fases.

## Agentes & Tasks
- Toda a cadeia D1-D3 do squad, fase a fase do [`offer-book-project`](../offer-book-project/00-brief.md): [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md), [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md), [`proof-credibility-curator`](../../agents/proof-credibility-curator.md), [`mechanism-architect`](../../agents/mechanism-architect.md), [`value-equation-engineer`](../../agents/value-equation-engineer.md), [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md), [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md), [`money-model-designer`](../../agents/money-model-designer.md), [`big-idea-architect`](../../agents/big-idea-architect.md), [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md).
- **Task de fechamento [`assemble-offer-book`](../../tasks/assembly/assemble-offer-book.md)** — dono [`offerbook-chief`](../../agents/offerbook-chief.md), com o [`compliance-auditor`](../../agents/compliance-auditor.md). Roda o ★ HARD STOP.

## Passos
1. Execute o projeto Offer Book de ponta a ponta, seguindo suas dez fases. Cada fase passa seus próprios gates antes de liberar a seguinte.
2. Diagnostique o mercado (sofisticação + consciência + starving-crowd) e minere a voz do cliente com ≥10 verbatims por segmento.
3. Cure a prova contra cada claim e cada objeção; reporte os proof-gaps.
4. Nomeie o mecanismo único provado; pontue a equação de valor sem alavanca órfã.
5. Derive o preço do valor, prove a liquidação do CAC e desenhe a espinha do money model com ≥2 partes (alvo 4).
6. Destile UMA Big Idea e trave a posição e o lead casados com a consciência.
7. Transcreva os 10 blocos do Offer Book Master e rode o `offer-book-stack/offer-book-dod-gate` item a item, com evidência linkada.
8. Decida VERDE (libera D4) ou VERMELHO (barra D4, devolve ao dono do bloco). Registre `decision.hard-stop-status`.

## Artefatos Produzidos
- `artifact.offer-book` — o mapa-mestre com os 10 blocos preenchidos e validados; a fonte de verdade de todo o lançamento. (Mais todos os artefatos intermediários das dez fases do offer-book: market-brief, avatar, proof-bank, mechanism-sheet, value-scorecard, money-model, pricing/unit-economics, big-idea, positioning.)
- `decision.hard-stop-status` — verde ou vermelho + bloco que falhou + pendências.
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md) e [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) — **★ HARD STOP de entrada** (bloqueia D4+).
- [`chief/chief-offer-book-readiness-gate`](../../checklists/chief/chief-offer-book-readiness-gate.md)
- Mais todos os gates internos das dez fases do Offer Book (mercado, avatar, prova, mecanismo, valor, pricing, unit-econ, money-model, big-idea, positioning).

## Critério de Saída
O Offer Book está VERDE: os 10 blocos preenchidos sem placeholder, cada critério do DoD atendido com evidência, o compliance sem achado aberto e o readiness gate verde. Só com este verde o lançamento cruza o HARD STOP. A próxima fase é a [`02-copy-vsl`](02-copy-vsl.md), que recebe o Offer Book aprovado como fonte de verdade para a primeira palavra de copy. Vermelho devolve ao agente dono do bloco que falhou e a copy permanece barrada.
