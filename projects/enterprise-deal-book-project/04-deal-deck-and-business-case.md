---
id: project.enterprise-deal-book-project.04-deal-deck-and-business-case
title: "Fase 04 — Deal Deck & Business Case"
type: project-phase
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes:
  - artifact.positioning-statement
  - artifact.commercial-insight
  - artifact.business-case-metrics
  - artifact.dmu-map
  - template.core.offer-book-master
produces:
  - artifact.offer-book-master
  - artifact.deal-deck
  - artifact.business-case-doc
  - artifact.champion-kit
tags: [project-phase, enterprise, b2b, deal-deck, business-case, champion-kit, hard-stop, challenger, d4]
---

# Fase 04 — Deal Deck & Business Case

## Objetivo da Fase
Montar o deal book — o deck de venda e o business case que o comitê aprova — e dar ao campeão a munição para vender por dentro. Esta fase fecha o HARD STOP do caso (o Offer Book Master deve passar no Definition of Done antes da peça de venda) e depois escreve a narrativa enterprise no arco Challenger: Teach, Tailor, Take Control. O estado-pronto é o Offer Book Master completo, o deal deck que abre com o insight comercial e conduz à força única, o documento de business case com as métricas defensáveis que o comprador econômico leva ao comitê, e o champion kit — os one-pagers por papel que o campeão usa para convencer o CFO, o técnico e o usuário. A régua MEDDIC e Challenger guia: o campeão é o seu vendedor interno; sem o kit, ele perde a venda interna. A narrativa é personalizada por stakeholder, porque cada papel teme e deseja coisas diferentes.

## Critério de Entrada
A [`03-positioning-and-battle-cards`](03-positioning-and-battle-cards.md) entrega o posicionamento, o insight comercial e as battle cards; a [`02-value-and-pricing-packaging`](02-value-and-pricing-packaging.md) entrega o business case e o preço; a [`01-icp-and-dmu`](01-icp-and-dmu.md) entrega a DMU. Pré-condição absoluta: o ★ [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) está verde antes de a peça de venda nascer — é a regra `offer_before_persuasion`. Se o Offer Book ainda tem bloco vazio, esta fase monta o Offer Book primeiro e só então escreve o deck. O [`control-registry`](../../data/registries/control-registry.md) é lido para reusar estruturas de deck vencedoras.

## Agentes & Tasks
- **Task [`assemble-offer-book`](../../tasks/assembly/assemble-offer-book.md)** — donos [`offerbook-chief`](../../agents/offerbook-chief.md) e [`compliance-auditor`](../../agents/compliance-auditor.md). Fecha o HARD STOP.
- **Task [`write-vsl-webinar`](../../tasks/copy/write-vsl-webinar.md)** — dono [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md), que adapta a narrativa para o comitê, com passe de voz do [`voice-style-guardian`](../../agents/voice-style-guardian.md).

## Passos
1. Monte o Offer Book Master e passe o ★ HARD STOP. Bloco vazio bloqueia o deck.
2. Estruture o deal deck no arco Teach→Tailor→Take Control com [`copy/pastor`](../../frameworks/copy/pastor.md) e [`copy/vsl-structure`](../../frameworks/copy/vsl-structure.md): abre com o insight, dimensiona o custo do status quo, revela a força única.
3. Escreva o business case doc: a economia, o ROI e o payback das métricas da fase anterior em uma página que o CFO leva ao comitê.
4. Personalize a narrativa por papel (Tailor): o slide do CFO fala ROI, o do técnico fala segurança e integração, o do usuário fala facilidade.
5. Assuma o controle do processo (Take Control): inclua o próximo passo, o cronograma de decisão e o tratamento de preço com [`copy/close-frameworks`](../../frameworks/copy/close-frameworks.md).
6. Monte o champion kit: one-pager de ROI para o CFO, FAQ de segurança para o técnico, prova de adoção para o usuário — a munição do campeão.
7. Embuta as battle cards no deck para a refutação de cada alternativa e do status quo.
8. Rode o passe de voz: clara, direta, ativa. Atualize o `control-registry`.

## Artefatos Produzidos
- `artifact.offer-book-master` — o mapa-mestre completo, aprovado no HARD STOP.
- `artifact.deal-deck` — o deck de venda no arco Challenger, personalizado por papel.
- `artifact.business-case-doc` — o caso de negócio de uma página para o comitê.
- `artifact.champion-kit` — os one-pagers por papel para a venda interna.
- Registry escrito: [`control-registry`](../../data/registries/control-registry.md).

## Gates
- ★ [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) — o HARD STOP. Bloqueia a peça de venda.
- [`chief/chief-offer-book-readiness-gate`](../../checklists/chief/chief-offer-book-readiness-gate.md) — o chief confirma o Offer Book pronto.
- [`vsl/vsl-value-before-price-gate`](../../checklists/vsl/vsl-value-before-price-gate.md) e [`vsl/vsl-cta-strength-gate`](../../checklists/vsl/vsl-cta-strength-gate.md).

## Critério de Saída
O Offer Book Master está completo e aprovado no HARD STOP; o deal deck segue Teach→Tailor→Take Control e é personalizado por papel; o business case doc dá um número defensável ao comitê; o champion kit arma o campeão com munição por papel; as battle cards estão embutidas. Os gates de Offer Book e de deck estão verdes; o guardião de voz aprovou. A próxima fase é a [`05-compliance-and-handoff`](05-compliance-and-handoff.md), que audita cada claim do caso de negócio e entrega o deal book para o time de vendas.
