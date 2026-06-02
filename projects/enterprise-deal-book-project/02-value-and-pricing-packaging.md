---
id: project.enterprise-deal-book-project.02-value-and-pricing-packaging
title: "Fase 02 — Valor, Precificação & Empacotamento"
type: project-phase
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
consumes:
  - artifact.dmu-map
  - artifact.proof-bank
  - template.strategy.value-equation
  - template.strategy.pricing-wtp
produces:
  - artifact.value-equation-score
  - artifact.business-case-metrics
  - artifact.pricing-packaging
  - artifact.unit-economics
tags: [project-phase, enterprise, b2b, valor, roi, business-case, pricing, packaging, meddic, d2]
---

# Fase 02 — Valor, Precificação & Empacotamento

## Objetivo da Fase
Quantificar o valor que o comprador econômico precisa aprovar e empacotar a oferta enterprise. Em vendas grandes, "vai melhorar muito" não fecha orçamento — toda métrica precisa de número. Esta fase pontua a equação de valor da solução, transforma a dor mapeada na DMU em métricas de business case (a perda escondida que o insight revela, o ROI, o payback) e fixa o preço e o empacotamento por valor. O estado-pronto é a equação de valor sem alavanca órfã, o conjunto de métricas do caso de negócio — números defensáveis que o CFO pode levar ao comitê — o preço derivado de valor com método declarado e os pacotes good-better-best ajustados aos papéis. A régua MEDDIC manda: existe um número que justifica a compra? Aqui esse número nasce com base de cálculo.

## Critério de Entrada
A [`01-icp-and-dmu`](01-icp-and-dmu.md) entrega o `artifact.dmu-map` e o `artifact.proof-bank`. Pré-condição: o comprador econômico está mapeado e a Dor de negócio está identificada com a métrica que importa a ele. Se a dor não tem uma métrica quantificável (custo atual, horas, receita perdida), a fase volta à DMU para levantá-la — sem número, não há caso. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para a equação de valor; o [`price-test-registry`](../../data/registries/price-test-registry.md) guarda os testes de preço.

## Agentes & Tasks
- **Task [`score-value-equation`](../../tasks/offer-architecture/score-value-equation.md)** — dono [`value-equation-engineer`](../../agents/value-equation-engineer.md), que pode vetar componente sem alavanca.
- **Task [`set-pricing-wtp`](../../tasks/offer-architecture/set-pricing-wtp.md)** — dono [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md).
- **Task [`model-unit-economics`](../../tasks/offer-architecture/model-unit-economics.md)** — dono [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md), para o caso de ROI da conta.

## Passos
1. Pontue a equação de valor com [`value-equation`](../../frameworks/value-equation.md): cada alavanca com ação concreta para o contexto enterprise.
2. Quantifique a perda escondida que o insight comercial revela com [`value-equation-engineer/dream-outcome-amplification`](../../frameworks/value-equation-engineer/dream-outcome-amplification.md): custo atual do status quo.
3. Modele o ROI e o payback da conta com [`lib/utilities/roi-calculator.md`](../../lib/utilities/roi-calculator.md): o número que o comprador econômico aprova.
4. Monte as métricas do business case: economia anual, payback em meses, ROI percentual — cada uma com base de cálculo.
5. Derive o preço de valor com método declarado: [`pricing/value-based-pricing`](../../frameworks/pricing/value-based-pricing.md), apoiado em WTP do comitê via [`pricing/conjoint-cbc`](../../frameworks/pricing/conjoint-cbc.md) quando houver dados.
6. Empacote em good-better-best com [`pricing/packaging-good-better-best`](../../frameworks/pricing/packaging-good-better-best.md): pacotes que servem papéis e níveis de orçamento diferentes.
7. Ancore o preço contra o valor entregue com [`price-anchoring`](../../frameworks/price-anchoring.md): o custo do status quo ancora o investimento.
8. Trave preço, pacotes e métricas. Atualize o `offer-registry` e o `price-test-registry`.

## Artefatos Produzidos
- `artifact.value-equation-score` — a equação de valor da solução, sem alavanca órfã.
- `artifact.business-case-metrics` — economia, ROI e payback, cada um com base de cálculo.
- `artifact.pricing-packaging` — preço por valor, método declarado e pacotes good-better-best.
- `artifact.unit-economics` — o modelo de ROI da conta com cenários.
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md), [`price-test-registry`](../../data/registries/price-test-registry.md).

## Gates
- [`value/value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md) — nenhuma alavanca sem ação concreta.
- [`pricing/pricing-value-derived-gate`](../../checklists/pricing/pricing-value-derived-gate.md) — o preço deriva de valor.
- [`pricing/pricing-method-declared-gate`](../../checklists/pricing/pricing-method-declared-gate.md) e [`pricing/pricing-packaging-gate`](../../checklists/pricing/pricing-packaging-gate.md).

## Critério de Saída
A equação de valor não tem alavanca órfã; as métricas do business case têm base de cálculo e dão um número que justifica a compra; o preço deriva de valor com método declarado; os pacotes good-better-best servem papéis e orçamentos distintos; a ancoragem usa o custo do status quo. Os gates de valor e preço estão verdes; os registries estão atualizados. A próxima fase é a [`03-positioning-and-battle-cards`](03-positioning-and-battle-cards.md), que recebe o caso de valor e a DMU para fixar o posicionamento contra a concorrência e o status quo, e armar as battle cards do comitê.
