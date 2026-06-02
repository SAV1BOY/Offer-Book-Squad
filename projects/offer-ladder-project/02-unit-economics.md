---
id: project.offer-ladder-project.02-unit-economics
title: "Fase 02 — Unit Economics"
type: project-phase
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
consumes:
  - decision.price-per-rung
  - artifact.value-equation-score
  - template.strategy.unit-economics
produces:
  - artifact.unit-economics
  - decision.ltv-cac-target
  - decision.payback-window
tags: [project-phase, offer-ladder, unit-economics, ltv, cac, payback, margem, d2]
---

# Fase 02 — Unit Economics

## Objetivo da Fase
Modelar a economia real da escada e provar que ela se paga. Preço sem economia é número solto. Esta fase pega os preços por degrau e calcula a margem, o custo de aquisição (CAC), o valor do cliente no tempo (LTV), o índice LTV:CAC e a janela de payback. O alvo clássico de Hormozi orienta o desenho: ganhar de um cliente, cedo, o bastante para adquirir e atender o próximo. O estado-pronto é a economia conhecida — LTV:CAC com base de cálculo explícita, payback dentro de uma janela viável e a confirmação de quanto do CAC o front-end liquida. Se a escada não se paga no prazo definido, esta fase volta à precificação ou ao desenho da oferta. Economia escondida é risco; aqui ela vira número defensável.

## Critério de Entrada
A [`01-value-and-pricing`](01-value-and-pricing.md) entrega o `decision.price-per-rung` e a equação de valor de cada degrau. Pré-condição: cada degrau tem preço travado e um método de WTP declarado, e existem custos mínimos conhecidos (entrega, suporte, processamento) e uma estimativa de CAC por canal. Se faltam custos para calcular a margem, a fase sinaliza a lacuna e pede os dados. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para puxar os preços e papéis; o [`price-test-registry`](../../data/registries/price-test-registry.md) guarda as faixas de preço testadas.

## Agentes & Tasks
- **Task [`model-unit-economics`](../../tasks/offer-architecture/model-unit-economics.md)** — dono [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md), com apoio do [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) nas faixas de preço.

## Passos
1. Calcule a margem de contribuição de cada degrau: preço menos custo variável direto.
2. Estime o CAC por canal com base de cálculo explícita. Sem base, marque como hipótese e sinalize.
3. Modele o LTV com o ferramental de cálculo de ROI ([`lib/utilities/roi-calculator.md`](../../lib/utilities/roi-calculator.md)): valor médio, frequência, tempo de vida.
4. Compute o índice LTV:CAC e a janela de payback. Confronte com o alvo declarado na [`00-brief`](00-brief.md).
5. Verifique a liquidação de CAC no front-end com [`money-model-sequence`](../../frameworks/money-model-sequence.md): atração + upsell cobrem o custo cedo?
6. Rode cenários: pessimista, base e otimista, variando CAC e take rate dos degraus.
7. Se a escada não se paga na janela, devolva à [`01-value-and-pricing`](01-value-and-pricing.md) para reprecificar ou repensar degraus.
8. Trave o LTV:CAC-alvo e a janela de payback. Atualize o `price-test-registry` e o `offer-registry`.

## Artefatos Produzidos
- `artifact.unit-economics` — margem por degrau, CAC, LTV, LTV:CAC, payback e os três cenários.
- `decision.ltv-cac-target` — o índice-alvo travado.
- `decision.payback-window` — a janela de payback viável.
- Registries escritos: [`price-test-registry`](../../data/registries/price-test-registry.md), [`offer-registry`](../../data/registries/offer-registry.md).

## Gates
- [`unit-economics-checklist`](../../checklists/unit-economics-checklist.md) — LTV:CAC e payback conhecidos com base de cálculo.
- [`money-model/money-model-cac-liquidation-gate`](../../checklists/money-model/money-model-cac-liquidation-gate.md) — o front-end liquida o CAC.

## Critério de Saída
A margem de cada degrau está calculada; o CAC tem base de cálculo; o LTV e o índice LTV:CAC estão modelados; a janela de payback é viável e bate com o alvo; a liquidação de CAC no front-end está confirmada; os três cenários estão rodados. Os gates de unit economics estão verdes; os registries estão atualizados. A próxima fase é a [`03-money-model`](03-money-model.md), que recebe a economia provada para sequenciar os degraus em um Money Model com as quatro partes e CTA por passo.
