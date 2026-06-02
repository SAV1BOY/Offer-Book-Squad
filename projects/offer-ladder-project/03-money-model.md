---
id: project.offer-ladder-project.03-money-model
title: "Fase 03 — Money Model"
type: project-phase
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes:
  - artifact.unit-economics
  - decision.ltv-cac-target
  - artifact.value-equation-score
  - template.offer.money-model
produces:
  - artifact.money-model
  - decision.sequence-and-triggers
  - decision.continuity-design
tags: [project-phase, offer-ladder, money-model, sequence, upsell, downsell, continuity, spine, d2]
---

# Fase 03 — Money Model

## Objetivo da Fase
Sequenciar os degraus numa espinha que extrai o máximo de valor o mais rápido possível. Este é o coração da trilha: o Money Model não é uma oferta, é a ordem deliberada em que o cliente sobe — atração, núcleo, upsell, downsell e continuidade — com um gatilho de transição em cada degrau e um CTA por passo. O estado-pronto é a sequência com as quatro partes (alvo), no mínimo duas (piso), cada degrau com seu gatilho — compra, recusa, conclusão de marco, passagem de tempo — e a continuidade desenhada com valor recorrente real. A régua de Hormozi guia: ganhar de um cliente o bastante para adquirir e atender dois, cedo. Sem essa espinha, não há centro — é o princípio `money_model_spine`. Copy, funil e logística de qualquer trilha futura dependem da escada existir aqui.

## Critério de Entrada
A [`02-unit-economics`](02-unit-economics.md) entrega o `artifact.unit-economics` e o LTV:CAC-alvo; a [`01-value-and-pricing`](01-value-and-pricing.md) entrega a equação de valor por degrau. Pré-condição: a economia se paga na janela definida e cada degrau tem preço e valor travados. Se a economia não fecha, a fase não sequencia — devolve à fase anterior. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para puxar todos os degraus; o [`price-test-registry`](../../data/registries/price-test-registry.md) confirma os preços travados.

## Agentes & Tasks
- **Task [`design-money-model`](../../tasks/offer-architecture/design-money-model.md)** — dono [`money-model-designer`](../../agents/money-model-designer.md), que é dono da espinha, com [`value-equation-engineer`](../../agents/value-equation-engineer.md), [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) e [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) no apoio.

## Passos
1. Liste cada oferta com seu papel usando [`money-model-designer/offer-ladder-sequencing`](../../frameworks/money-model-designer/offer-ladder-sequencing.md): mínimo 2 partes, alvo 4.
2. Desenhe a oferta de atração com [`money-model-designer/attraction-offer-design`](../../frameworks/money-model-designer/attraction-offer-design.md): entrada de baixo atrito que liquida o CAC.
3. Posicione os upsells e downsells com [`money-model-designer/upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md): mais no pico, recuperação no "não".
4. Desenhe a continuidade com [`money-model-designer/continuity-design`](../../frameworks/money-model-designer/continuity-design.md): valor recorrente real, gancho de entrada, motivo de ficar, controle de churn.
5. Defina o gatilho de cada transição: compra, recusa, conclusão de marco, passagem de tempo.
6. Garanta um CTA por degrau — cada oferta termina apontando o próximo passo claro.
7. Confirme a liquidação de CAC: atração + upsell recuperam o custo no front-end.
8. Ordene a sequência completa pela jornada de valor com [`money-model-sequence`](../../frameworks/money-model-sequence.md). Atualize o `offer-registry`.

## Artefatos Produzidos
- `artifact.money-model` — a sequência completa com papéis, gatilhos e CTA por degrau.
- `decision.sequence-and-triggers` — a ordem e os gatilhos travados.
- `decision.continuity-design` — o desenho da continuidade com o controle de churn.
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md), [`price-test-registry`](../../data/registries/price-test-registry.md).

## Gates
- [`money-model/money-model-four-parts-gate`](../../checklists/money-model/money-model-four-parts-gate.md) — quatro partes (alvo) ou duas (piso) sequenciadas.
- [`money-model/money-model-sequence-gate`](../../checklists/money-model/money-model-sequence-gate.md) — a ordem segue a jornada de valor.
- [`money-model/money-model-cta-per-step-gate`](../../checklists/money-model/money-model-cta-per-step-gate.md) — CTA em cada degrau.

## Critério de Saída
A sequência tem as quatro partes (ou no mínimo duas) na ordem da jornada de valor; cada transição tem gatilho; cada degrau tem CTA; a continuidade entrega valor recorrente real com controle de churn; a liquidação de CAC no front-end está confirmada. Os três gates de money model estão verdes; o registry está atualizado. A próxima fase é a [`04-products-and-offers`](04-products-and-offers.md), que recebe a espinha sequenciada para detalhar cada produto e oferta numa planilha pronta para o operacional.
