---
id: project.full-launch-blackbook-project.05-ad-matrix
title: "Fase 05 — Matriz de Ads"
type: project-phase
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
consumes:
  - artifact.offer-book
  - artifact.mechanism-sheet
  - artifact.big-idea
  - artifact.voc-verbatim-bank
  - data.registry.objection
  - data.registry.proof
produces:
  - artifact.ad-matrix
  - decision.ad-angles
  - decision.voice-verdict
tags: [project-phase, copy, ads, matriz, angulos, retargeting, continuidade, hard-stop, d4]
---

# Fase 05 — Matriz de Ads

## Objetivo da Fase
Transformar UMA Big Idea e UM mecanismo numa matriz de ads onde cada dor do avatar é atacada por ≥3 ângulos distintos, o retargeting cobre cada objeção dominante, e a continuidade estende a recorrência — todos rastreáveis à tese e com claim lastreado. O estado-pronto é a matriz com as três camadas (frio, retarget, continuidade), cada gancho com prova linkada, ângulos realmente diferentes (não cosméticos), aprovada nos três gates de ads e no veredito de voz. Esta fase fecha a camada D4 de copy: multiplica a tese estratégica em criativos sem inventar promessa que a oferta não entrega.

## Critério de Entrada
A Fase 01 entrega o `artifact.offer-book` aprovado (HARD STOP VERDE), a `artifact.big-idea` travada (UMA, via single-gate), o `artifact.mechanism-sheet` e o `artifact.voc-verbatim-bank` (as dores na linguagem literal). Os registries [`objection-registry`](../../data/registries/objection-registry.md) (cada objeção vira um ângulo de retarget) e [`proof-registry`](../../data/registries/proof-registry.md) (define qual gancho vai ao ar) vêm junto. Pré-condição: o `offer-book-dod-gate` está APROVADO e a Big Idea é única — múltiplas teses geram ads que competem e confundem o pixel. Os registries [`control-registry`](../../data/registries/control-registry.md) e [`swipe-registry`](../../data/registries/swipe-registry.md) são escritos.

## Agentes & Tasks
- **Task [`generate-ad-matrix`](../../tasks/copy/generate-ad-matrix.md)** — dono [`ad-creative-factory`](../../agents/ad-creative-factory.md). Sem poder de veto; submete ao guardião.
- **Task [`voice-pass`](../../tasks/copy/voice-pass.md)** — dono [`voice-style-guardian`](../../agents/voice-style-guardian.md). Passe obrigatório de voz.

## Passos
1. Verifique o HARD STOP: confirme o `offer-book-dod-gate` verde e a Big Idea única.
2. Mapeie as dores em eixos de ângulo (dor, mecanismo, prova, identidade, medo/ganho) — diferença real, não troca de cor de botão.
3. Gere ganchos por dor com Tree-of-Thoughts via [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md): ≥3 por dor, pontuados por scroll-stop, fidelidade à Big Idea, lastro, diferença de ângulo e consciência.
4. Escreva a camada de retargeting: um ad por objeção dominante, revertendo-a com o mecanismo + a garantia.
5. Escreva a camada de continuidade: ângulos de retenção/recompra para quem já teve o primeiro resultado.
6. Case lead e consciência com [`lead-types`](../../lib/taxonomies/lead-types.md): frio = História/Segredo; quente = Oferta direta. Gere os corpos com [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md).
7. Valide o lastro: gancho sem prova é bloqueado e substituído por promessa verificável até a prova chegar.
8. Self-verify com red-team (cada dor com ≥3 ângulos? cada objeção com retarget? variações são ângulos diferentes?); registre no `control-registry`, os ganchos no `swipe-registry`, e encaminhe ao voice-pass.

## Artefatos Produzidos
- `artifact.ad-matrix` — as três camadas: frio (≥3 ângulos por dor), retargeting (1 por objeção), continuidade.
- `decision.ad-angles` — eixos escolhidos por dor, candidatos podados, motivo.
- `decision.voice-verdict` — APROVADO por peça.
- Registries escritos: [`control-registry`](../../data/registries/control-registry.md) e [`swipe-registry`](../../data/registries/swipe-registry.md).

## Gates
- [`ads/ads-angle-coverage-gate`](../../checklists/ads/ads-angle-coverage-gate.md) · [`ads/ads-claim-backing-gate`](../../checklists/ads/ads-claim-backing-gate.md) · [`ads/ads-variation-gate`](../../checklists/ads/ads-variation-gate.md)
- Os quatro gates de voz via [`voice/voice-checklist`](../../voice/voice-checklist.md).
- Gate de entrada (HARD STOP): [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).

## Critério de Saída
Cada dor dominante é coberta por ≥3 ângulos distintos; o retargeting cobre cada objeção; a continuidade está presente; cada ad é rastreável à UMA Big Idea; cada gancho tem claim lastreado; as variações são ângulos diferentes; o lead casa com a temperatura do destino; os três gates de ads estão verdes e o veredito de voz é APROVADO. Fecha a camada D4. A próxima fase é a [`06-funnel-map`](06-funnel-map.md), que traduz a copy aprovada e o money model em trilhas de funil sem becos sem saída.
