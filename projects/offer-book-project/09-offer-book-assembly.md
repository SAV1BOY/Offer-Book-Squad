---
id: project.offer-book-project.09-offer-book-assembly
title: "Fase 09 — Montagem do Offer Book (★ HARD STOP / DoD)"
type: project-phase
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes:
  - artifact.offer-book-master-skeleton
  - artifact.market-brief
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - artifact.mechanism-sheet
  - artifact.proof-bank
  - artifact.value-equation-scorecard
  - artifact.money-model
  - artifact.pricing-wtp-sheet
  - artifact.unit-economics-sheet
  - artifact.offer-stack
  - artifact.guarantee
  - artifact.big-idea
  - artifact.positioning
  - decision.lead-type-locked
produces:
  - artifact.offer-book
  - decision.hard-stop-status
tags: [project-phase, assembly, offer-book, hard-stop, dod-gate, compliance, readiness, d3]
---

# Fase 09 — Montagem do Offer Book (★ HARD STOP / DoD)

## Objetivo da Fase
Transcrever os destilados de D1-D3 nos 10 blocos do Offer Book Master, auditar a verdade da oferta e rodar o **★ HARD STOP** — o `offer-book-stack/offer-book-dod-gate`. Verde libera a primeira palavra de copy (D4); vermelho barra o D4 e devolve ao agente dono do bloco que falhou. Esta é a fase-marco do projeto: o portão entre estratégia e copy. O estado terminal é binário — VERDE (a copy nasce) ou VERMELHO (a copy fica barrada). Não existe "parcial liberado". É aqui que o princípio Agora se materializa: ~50-60% do trabalho de pesquisa e estratégia precede a primeira palavra.

## Critério de Entrada
A Fase 08 fecha a camada D3: Big Idea travada (`artifact.big-idea`), posição e lead travados (`artifact.positioning`, `decision.lead-type-locked`), sobre uma D2 completa. Todos os blocos D1-D3 chegam com seu artefato-fonte: o market-brief (Fase 01), o avatar/VOC (Fase 02), o proof-bank (Fase 03), o mechanism-sheet (Fase 04), o value-equation-scorecard (Fase 05), o money-model (Fase 06), o pricing-wtp-sheet/unit-economics-sheet/offer-stack/guarantee (Fase 07) e a big-idea/positioning (Fase 08). O esqueleto vem aberto desde a Fase 00. Pré-condição: nenhum bloco vazio, nenhum gate a montante vermelho. Conforme `config.yaml: defaults.hard_stop_before_copy: true`, nenhuma palavra de copy nasce antes deste gate passar. Os registries [`offer-registry`](../../data/registries/offer-registry.md) e [`decision-registry`](../../data/registries/decision-registry.md) são escritos.

## Agentes & Tasks
- **Task [`assemble-offer-book`](../../tasks/assembly/assemble-offer-book.md)** — dono [`offerbook-chief`](../../agents/offerbook-chief.md), com o [`compliance-auditor`](../../agents/compliance-auditor.md) como auditor de verdade do pacote. Ambos detêm poder de veto: o chief sobre cruzar o HARD STOP; o compliance sobre claim sem lastro ou escassez falsa.

## Passos
1. Confirme a completude: cada um dos 10 blocos tem seu artefato-fonte? Falta algum, devolva ao agente dono antes de transcrever.
2. Transcreva os destilados nos 10 blocos do Offer Book Master (Mercado, Avatar, Mecanismo, Prova, Valor, Money Model, Pricing & Unit Economics, Big Idea & Posição, Reversão & Escassez, Status). Resuma e linke os templates-fonte; nenhum placeholder solto.
3. Verifique a cadeia prova→claim com [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md): nenhum claim grande órfão; cada objeção top com resposta provada.
4. Auditoria de verdade: o compliance inspeciona claim sem lastro, escassez sem motivo, garantia inexequível, âncora fictícia. Achado marca o bloco pendente.
5. Confira o mapeamento oferta→funil com [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md): cada degrau com próximo passo claro.
6. **★ Rode o HARD STOP** — verifique os 10 critérios do DoD item a item, com evidência linkada (não opinião).
7. Decida: VERDE marca o bloco 10 e passa o [`chief/chief-offer-book-readiness-gate`](../../checklists/chief/chief-offer-book-readiness-gate.md); só então o caso cruza para o blackbook e a copy. VERMELHO barra o D4, nomeia o bloco que falhou e devolve ao dono.
8. Self-verify e registre `decision.hard-stop-status` no `decision-registry`. Override do HARD STOP só com decisão explícita e registrada do chief.

## Artefatos Produzidos
- `artifact.offer-book` — o mapa-mestre com os 10 blocos preenchidos e validados; a fonte de verdade de todo o D4+.
- `decision.hard-stop-status` — verde (D4 liberado) ou vermelho (D4 barrado) + bloco que falhou + pendências.
- Registries escritos: [`decision-registry`](../../data/registries/decision-registry.md) e [`offer-registry`](../../data/registries/offer-registry.md).

## Gates
- [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) — **★ HARD STOP** (bloqueia D4+).
- [`chief/chief-offer-book-readiness-gate`](../../checklists/chief/chief-offer-book-readiness-gate.md)

## Critério de Saída
Os 10 blocos estão preenchidos sem placeholder solto; cada critério do `offer-book-dod-gate` está atendido com evidência linkada; o compliance não tem achado aberto; o `chief-offer-book-readiness-gate` está verde; o status do HARD STOP está registrado. Estado terminal: VERDE (o lançamento cruza para D4) ou VERMELHO (D4 barrado, bloco devolvido ao dono). Com VERDE, o Offer Book aprovado é entregue como fonte de verdade — em um caso `run-offer-book`, este é o entregável final; em um lançamento completo, ele se torna a Fase 01 do projeto [`full-launch-blackbook`](../full-launch-blackbook-project/01-offer-book.md), que incorpora o Offer Book inteiro antes de qualquer copy.
