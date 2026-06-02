---
id: project.offer-book-project.07-pricing-unit-economics
title: "Fase 07 — Pricing & Unit Economics"
type: project-phase
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
consumes:
  - artifact.value-equation-scorecard
  - artifact.mechanism-sheet
  - artifact.avatar-icp
  - artifact.market-brief
  - artifact.money-model
produces:
  - artifact.pricing-wtp-sheet
  - artifact.unit-economics-sheet
  - artifact.offer-stack
  - artifact.guarantee
  - decision.price-points
  - decision.cac-liquidation-status
tags: [project-phase, offer-architecture, pricing, wtp, unit-economics, cac, ltv, offer-stack, garantia, d2]
---

# Fase 07 — Pricing & Unit Economics

## Objetivo da Fase
Derivar o preço do valor e da disposição a pagar — nunca do custo — e provar com números que a oferta de atração liquida o CAC no front-end. Esta fase entrega os pontos de preço (com âncora e packaging good-better-best), o cálculo de CAC/LTV/AOV/payback, o offer stack com valor maior que o preço, a garantia exequível e a escassez 100% real com nome MAGIC. O estado-pronto é a matemática fechada e a embalagem de valor pronta. Esta fase fecha a camada D2 em laço com a Fase 06: ela fixa o preço e valida a conta, o money model fecha a forma.

## Critério de Entrada
A Fase 05 entrega o `artifact.value-equation-scorecard` (o valor percebido por alavanca, a âncora superior do preço, o custo × delta de cada componente). A Fase 04 entrega o `artifact.mechanism-sheet` (quanto mais único, maior o WTP defensável; matéria do naming MAGIC e da escassez honesta). A Fase 02 entrega o avatar (poder de compra, alternativas, sensibilidade) e a Fase 01 o market-brief (sofisticação, faixas dos concorrentes). A Fase 06 entrega a forma da escada (`artifact.money-model`) para somar o AOV ao longo dos degraus e localizar onde o CAC é liquidado. Pré-condição: o scorecard de valor existe — derivo do valor; cost-plus é recusado e escala ao chief. Os registries [`price-test-registry`](../../data/registries/price-test-registry.md) e [`offer-registry`](../../data/registries/offer-registry.md) são escritos.

## Agentes & Tasks
- **Task [`set-pricing-wtp`](../../tasks/offer-architecture/set-pricing-wtp.md)** — dono [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md). Produz os pontos de preço, a ancoragem e o packaging. Sem poder de veto.
- **Task [`model-unit-economics`](../../tasks/offer-architecture/model-unit-economics.md)** — dono [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md). Calcula a economia, monta o stack/garantia/escassez e valida a liquidação do CAC. Sem veto — suas flags acionam os vetos do compliance e do value-engineer.

## Passos
1. Estime a faixa de WTP com [`van-westendorp`](../../frameworks/pricing/van-westendorp.md) e [`gabor-granger`](../../frameworks/pricing/gabor-granger.md); identifique as features que movem WTP com [`conjoint-cbc`](../../frameworks/pricing/conjoint-cbc.md) e [`kano-model`](../../frameworks/pricing/kano-model.md).
2. Cruze ≥3 métodos com Tree-of-Thoughts — a convergência decide, não um método isolado. Métodos que divergem muito pedem teste-desempate.
3. Fixe a âncora com [`price-anchoring`](../../frameworks/price-anchoring.md) (referência alta e crível) e o packaging com [`packaging-good-better-best`](../../frameworks/pricing/packaging-good-better-best.md) mais [`decoy-effect`](../../frameworks/pricing/decoy-effect.md).
4. Calcule a unidade: CAC, AOV (front e total), margem, LTV, payback, razão LTV:CAC — com margem, não receita bruta.
5. Verifique a liquidação do CAC: some a receita do front-end e localize onde na escada o cliente paga a aquisição. Abaixo do CAC, teste ≥3 alavancas de correção; qualquer uma que dependa de escassez falsa é podada.
6. Monte o offer stack com [`offer-stack-builder`](../../frameworks/offer-stack-builder.md), escolha a garantia com [`guarantee-design`](../../frameworks/guarantee-design.md) e [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md), desenhe a escassez real com [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) e dê o nome com [`magic-naming`](../../frameworks/magic-naming.md).
7. Self-verify com red-team: "o que o compliance rejeitaria?" (âncora fictícia, escassez sem motivo, garantia inexequível).
8. Registre os pontos no `price-test-registry`, a economia e o stack no `offer-registry`, e passe os seis gates das duas tasks.

## Artefatos Produzidos
- `artifact.pricing-wtp-sheet` — métodos, faixa de WTP, convergência, packaging com tier-alvo, decoy, âncora, status.
- `artifact.unit-economics-sheet` — CAC/AOV/margem/LTV/payback/LTV:CAC e a liquidação do CAC com seu ponto na escada.
- `artifact.offer-stack` + `artifact.guarantee` — itens com valor ancorado vs preço; tipo de garantia e exequibilidade.
- `decision.price-points` e `decision.cac-liquidation-status` — pontos travados e veredito de liquidação (sim/não/estimado).
- Registries escritos: [`price-test-registry`](../../data/registries/price-test-registry.md) e [`offer-registry`](../../data/registries/offer-registry.md).

## Gates
- [`pricing/pricing-value-derived-gate`](../../checklists/pricing/pricing-value-derived-gate.md) · [`pricing/pricing-method-declared-gate`](../../checklists/pricing/pricing-method-declared-gate.md) · [`pricing/pricing-packaging-gate`](../../checklists/pricing/pricing-packaging-gate.md)
- [`unit-economics-checklist`](../../checklists/unit-economics-checklist.md) · [`offer-stack-checklist`](../../checklists/offer-stack-checklist.md) · [`guarantee-checklist`](../../checklists/guarantee-checklist.md)

## Critério de Saída
Cada ponto de preço tem método e faixa por trás; ≥2 métodos convergem; o preço deriva do valor, não de custo+margem; o packaging tem tier-alvo com âncora; CAC/AOV/margem/LTV/payback/LTV:CAC estão calculados; a liquidação do CAC está confirmada (ou reportada como não-fechada com alavancas propostas); o stack tem valor > preço sem órfãos; a garantia é exequível; a escassez é 100% real com motivo documentado; a oferta tem nome MAGIC; os seis gates estão verdes. Fecha a camada D2. A próxima fase é a [`08-big-idea-positioning`](08-big-idea-positioning.md), que recebe a oferta completa e precificada para destilar a tese e travar a posição.
