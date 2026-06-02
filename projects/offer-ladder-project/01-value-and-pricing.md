---
id: project.offer-ladder-project.01-value-and-pricing
title: "Fase 01 — Valor & Precificação"
type: project-phase
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
consumes:
  - decision.scope-one-sentence
  - artifact.current-offer-inventory
  - template.strategy.value-equation
  - template.strategy.pricing-wtp
produces:
  - artifact.value-equation-score
  - artifact.pricing-wtp
  - decision.price-per-rung
tags: [project-phase, offer-ladder, valor, value-equation, pricing, wtp, packaging, d2]
---

# Fase 01 — Valor & Precificação

## Objetivo da Fase
Derivar o valor percebido de cada degrau e fixar o preço a partir do valor, nunca do custo. A escada só funciona se cada degrau vale mais do que custa na cabeça do cliente, e se o preço sobe junto com o valor entregue. Esta fase pontua a equação de valor de cada oferta — resultado dos sonhos, probabilidade de alcance, tempo até o resultado e esforço/sacrifício — e fixa o preço com um método declarado de WTP. O estado-pronto é cada degrau com sua equação de valor sem alavanca órfã e um preço derivado de valor, com o método explícito (Van Westendorp, Gabor-Granger, conjoint ou value-based) e o empacotamento good-better-best onde fizer sentido. Preço sem método é palpite. Aqui o palpite morre.

## Critério de Entrada
A [`00-brief`](00-brief.md) entrega a frase de escopo e o `artifact.current-offer-inventory` com os degraus candidatos e seus preços atuais. Pré-condição: existe um inventário de ofertas com papéis definidos (atração, núcleo, upsell, downsell, continuidade) e dados mínimos de demanda ou VOC para sustentar a WTP. Se um degrau não tem clareza de resultado, a fase devolve para defini-lo antes de precificar. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para puxar a equação de valor já registrada; o [`price-test-registry`](../../data/registries/price-test-registry.md) guarda os testes de preço.

## Agentes & Tasks
- **Task [`score-value-equation`](../../tasks/offer-architecture/score-value-equation.md)** — dono [`value-equation-engineer`](../../agents/value-equation-engineer.md), que pode vetar degrau que não move alavanca.
- **Task [`set-pricing-wtp`](../../tasks/offer-architecture/set-pricing-wtp.md)** — dono [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md).

## Passos
1. Para cada degrau, pontue a equação de valor com [`value-equation`](../../frameworks/value-equation.md): as quatro alavancas, cada uma com ação concreta.
2. Amplifique o resultado dos sonhos com [`value-equation-engineer/dream-outcome-amplification`](../../frameworks/value-equation-engineer/dream-outcome-amplification.md).
3. Comprima o tempo até o resultado com [`value-equation-engineer/time-delay-compression`](../../frameworks/value-equation-engineer/time-delay-compression.md) e reduza o esforço com [`value-equation-engineer/effort-sacrifice-reduction`](../../frameworks/value-equation-engineer/effort-sacrifice-reduction.md).
4. Reprove qualquer degrau cujo valor não justifique a existência. Sem alavanca movida, o degrau sai.
5. Escolha o método de WTP por degrau: [`pricing/van-westendorp`](../../frameworks/pricing/van-westendorp.md), [`pricing/gabor-granger`](../../frameworks/pricing/gabor-granger.md), [`pricing/conjoint-cbc`](../../frameworks/pricing/conjoint-cbc.md) ou [`pricing/value-based-pricing`](../../frameworks/pricing/value-based-pricing.md).
6. Empacote em good-better-best onde couber com [`pricing/packaging-good-better-best`](../../frameworks/pricing/packaging-good-better-best.md).
7. Ancore o preço com [`price-anchoring`](../../frameworks/price-anchoring.md): o degrau de cima ancora o de baixo.
8. Fixe o preço de cada degrau e declare o método. Atualize o `offer-registry` e o `price-test-registry`.

## Artefatos Produzidos
- `artifact.value-equation-score` — a equação de valor de cada degrau, sem alavanca órfã.
- `artifact.pricing-wtp` — o preço de cada degrau, o método declarado e o empacotamento.
- `decision.price-per-rung` — o preço travado por degrau.
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md), [`price-test-registry`](../../data/registries/price-test-registry.md).

## Gates
- [`value/value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md) — nenhuma alavanca sem ação concreta.
- [`pricing/pricing-value-derived-gate`](../../checklists/pricing/pricing-value-derived-gate.md) — o preço deriva de valor.
- [`pricing/pricing-method-declared-gate`](../../checklists/pricing/pricing-method-declared-gate.md) e [`pricing/pricing-packaging-gate`](../../checklists/pricing/pricing-packaging-gate.md).

## Critério de Saída
Cada degrau tem equação de valor sem alavanca órfã; cada preço deriva de valor com um método declarado; o empacotamento good-better-best está definido onde cabe; a ancoragem entre degraus está clara. Os gates de valor e preço estão verdes; os registries estão atualizados. A próxima fase é a [`02-unit-economics`](02-unit-economics.md), que recebe os preços por degrau para modelar a economia real — CAC, LTV, margem e payback — e checar se a escada se paga.
