---
id: project.single-promo-project.01-offer-book-core
title: "Fase 01 — Núcleo do Offer Book (HARD STOP)"
type: project-phase
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes:
  - decision.scope-one-sentence
  - artifact.promo-pipeline
  - template.core.offer-book-master
produces:
  - artifact.offer-book-master
  - decision.sophistication-stage
  - decision.awareness-level
  - artifact.mechanism-sheet
  - artifact.value-equation-score
  - artifact.money-model
  - decision.big-idea-locked
tags: [project-phase, single-promo, offer-book, hard-stop, mecanismo, valor, money-model, big-idea, d3]
---

# Fase 01 — Núcleo do Offer Book (HARD STOP)

## Objetivo da Fase
Montar, enxuto e completo, o coração do Offer Book — e fechar o HARD STOP que destrava a copy. Esta fase comprime o pipeline de inteligência e arquitetura de oferta numa única passada disciplinada: mercado, avatar, prova, mecanismo, valor, preço, money model, Big Idea e posicionamento. Enxuto não é incompleto. O estado-pronto é o Offer Book Master preenchido nos blocos essenciais, com o mecanismo único nomeado e provado, a equação de valor sem alavanca órfã, o money model com no mínimo 2 partes sequenciadas, UMA Big Idea travada e o posicionamento ajustado à célula de sofisticação e consciência. Sem isso, nenhuma palavra de copy nasce. É o princípio Agora aplicado à Tier 1: mesmo na promo rápida, a maior parte do trabalho é estratégia antes da primeira frase.

## Critério de Entrada
A [`00-brief`](00-brief.md) entrega a frase de escopo travada, o `artifact.promo-pipeline` com a posição desta trilha e os contratos de handoff. Pré-condição: existe um público-alvo definido, não "todo mundo", e uma oferta-base sobre a qual trabalhar. Se o escopo aponta para dois mercados ou duas ofertas, a fase devolve ao chief pedindo poda. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para reusar oferta validada antes de recriar. O [`objection-registry`](../../data/registries/objection-registry.md) e o [`proof-registry`](../../data/registries/proof-registry.md) são lidos para puxar objeções e provas já mapeadas.

## Agentes & Tasks
- **Tasks de inteligência** — [`run-market-intel`](../../tasks/intelligence/run-market-intel.md), [`build-avatar-voc`](../../tasks/intelligence/build-avatar-voc.md), [`curate-proof`](../../tasks/intelligence/curate-proof.md). Donos: [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md), [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md), [`proof-credibility-curator`](../../agents/proof-credibility-curator.md).
- **Tasks de arquitetura** — [`define-mechanism`](../../tasks/offer-architecture/define-mechanism.md), [`score-value-equation`](../../tasks/offer-architecture/score-value-equation.md), [`set-pricing-wtp`](../../tasks/offer-architecture/set-pricing-wtp.md), [`design-money-model`](../../tasks/offer-architecture/design-money-model.md). Donos: [`mechanism-architect`](../../agents/mechanism-architect.md), [`value-equation-engineer`](../../agents/value-equation-engineer.md), [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md), [`money-model-designer`](../../agents/money-model-designer.md).
- **Tasks de Big Idea & posição** — [`generate-big-ideas`](../../tasks/big-idea/generate-big-ideas.md), [`lock-positioning-lead`](../../tasks/big-idea/lock-positioning-lead.md). Donos: [`big-idea-architect`](../../agents/big-idea-architect.md), [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md).
- **Task de fechamento** — [`assemble-offer-book`](../../tasks/assembly/assemble-offer-book.md). Donos: [`offerbook-chief`](../../agents/offerbook-chief.md) e [`compliance-auditor`](../../agents/compliance-auditor.md).

## Passos
1. Diagnostique o mercado: sofisticação (1-5) e consciência (1-5), cada um com ≥2 evidências, e o veredito [`starving-crowd`](../../frameworks/starving-crowd.md).
2. Minere o avatar com [`voc-mining`](../../frameworks/avatar-voc-investigator/voc-mining.md): ≥10 verbatims, emoção dominante, mapa de objeções via [`objection-belief-mapping`](../../frameworks/avatar-voc-investigator/objection-belief-mapping.md).
3. Case prova a cada claim e a cada objeção com [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md).
4. Nomeie o mecanismo único com [`unique-mechanism.md`](../../frameworks/unique-mechanism.md) e prove-o numa frase.
5. Pontue a equação de valor com [`value-equation`](../../frameworks/value-equation.md): nenhuma alavanca fica sem ação concreta.
6. Derive o preço do valor com método declarado ([`pricing/value-based-pricing`](../../frameworks/pricing/value-based-pricing.md)); ancore com [`price-anchoring`](../../frameworks/price-anchoring.md).
7. Desenhe o money model enxuto com [`money-model-sequence`](../../frameworks/money-model-sequence.md): mínimo 2 partes, alvo 4, com CTA por degrau.
8. Gere candidatas a Big Idea e trave UMA com [`big-idea-generator`](../../frameworks/big-idea-generator.md) e [`power-of-one`](../../frameworks/power-of-one.md). Múltiplas ideias = reprovação.
9. Trave o posicionamento ajustado à célula de sofisticação/consciência com [`positioning/dunford-positioning`](../../frameworks/positioning/dunford-positioning.md).
10. Monte o Offer Book Master e passe o ★ HARD STOP. Atualize o `offer-registry` e o `big-idea-registry`.

## Artefatos Produzidos
- `artifact.offer-book-master` — o mapa-mestre preenchido nos blocos essenciais.
- `decision.sophistication-stage` e `decision.awareness-level` — os dois números travados.
- `artifact.mechanism-sheet`, `artifact.value-equation-score`, `artifact.money-model`, `decision.big-idea-locked`.
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md), [`big-idea-registry`](../../data/registries/big-idea-registry.md), [`claim-registry`](../../data/registries/claim-registry.md).

## Gates
- ★ [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) — o HARD STOP. Bloqueia a copy.
- [`chief/chief-offer-book-readiness-gate`](../../checklists/chief/chief-offer-book-readiness-gate.md) — o chief confirma que o núcleo está pronto.
- [`value/value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md) e [`money-model/money-model-four-parts-gate`](../../checklists/money-model/money-model-four-parts-gate.md).

## Critério de Saída
O Offer Book Master está preenchido; os dois números de mercado têm evidência; o mecanismo está nomeado e provado; a equação de valor não tem alavanca órfã; o money model tem no mínimo 2 partes com CTA por degrau; UMA Big Idea está travada nos cinco critérios; o posicionamento bate com a célula. O HARD STOP está verde. Só agora a copy pode nascer. A próxima fase é a [`02-vsl-or-sales-letter`](02-vsl-or-sales-letter.md), que recebe o Offer Book como contrato de entrada.
