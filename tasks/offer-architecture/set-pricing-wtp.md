---
id: task.offer-architecture.set-pricing-wtp
title: "Set Pricing & WTP — Derivar o Preço do Valor e da Disposição a Pagar, com Método Declarado"
type: task
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
produces:
  - artifact.pricing-wtp-sheet
  - decision.price-points
  - decision.packaging-tiers
frameworks:
  - pricing/van-westendorp
  - pricing/gabor-granger
  - pricing/conjoint-cbc
  - pricing/kano-model
  - pricing/value-based-pricing
  - price-anchoring
  - pricing/packaging-good-better-best
  - pricing/decoy-effect
checklists:
  - pricing/pricing-value-derived-gate
  - pricing/pricing-method-declared-gate
  - pricing/pricing-packaging-gate
registries: [price-test-registry]
metrics: [aov, ltv_cac_ratio, front_end_cac_liquidation]
tags: [offer-architecture, pricing, wtp, van-westendorp, gabor-granger, conjoint, ancoragem, packaging, d2]
---

# Set Pricing & WTP — derivar o preço do valor e da disposição a pagar, com método declarado

## Objetivo
Fixar pontos de preço derivados de valor/WTP — nunca de custo — com a âncora e o packaging good-better-best, no estado em que ≥2 métodos de WTP convergem na faixa, o método está declarado e registrado, e o "sim" é fácil com margem saudável.

## Agente dono
[`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md). Produz os pontos de preço, a ancoragem e o packaging. Não escreve copy, não desenha a escada. Sem poder de veto — sinaliza margem ao unit-econ e ancoragem falsa ao compliance.

## Gatilho / Quando
Roda em D2, quando: (a) o value scorecard está fechado (valor por alavanca disponível); (b) o chief ou o money-model pede pontos de preço, packaging ou ancoragem; (c) há um relançamento que pede reprecificação. **Pré-condição:** o [`value-equation-scorecard`](score-value-equation.md) existe — eu **derivo do valor**; sem ele estaria chutando custo+margem (o que recuso). Se me pedem "cobrir custo + X%", recuso o método e proponho preço por valor, escalando ao chief se houver insistência em cost-plus — viola `price_value_derived`.

## Inputs (Consome)
- **`artifact.value-equation-scorecard`** (do value-engineer) — o valor percebido por alavanca: a âncora superior do preço.
- **`artifact.mechanism-sheet`** — o mecanismo (quanto mais único, maior o WTP defensável).
- **`artifact.avatar-icp`** — poder de compra, alternativas que o avatar considera (o "preço de referência" mental), sensibilidade a preço.
- **`artifact.market-brief`** — sofisticação (mercados maduros toleram premium com mecanismo) e faixas de preço dos concorrentes para ancorar.
- **Registry escrito:** [`price-test-registry`](../../data/registries/price-test-registry.md).

## Procedimento
1. **Estime a faixa de WTP (piso/teto).** Aplique [`van-westendorp`](../../frameworks/pricing/van-westendorp.md) (as 4 perguntas) — barato demais / caro demais / caro mas justo / muito caro → ponto de indiferença.
2. **Trace a curva de aceitação.** Aplique [`gabor-granger`](../../frameworks/pricing/gabor-granger.md) em pontos discretos — onde a aceitação despenca define o ponto que maximiza receita.
3. **Identifique as features que movem WTP.** Aplique [`conjoint-cbc`](../../frameworks/pricing/conjoint-cbc.md) (part-worth) e [`kano-model`](../../frameworks/pricing/kano-model.md) (básicas/lineares/encantadoras). As encantadoras (ex.: "acompanhamento 1:1") viram o tier alto.
4. **Cruze ≥3 métodos (Tree-of-Thoughts — central).** Nenhum método isolado decide; a **convergência** decide. Pontue cada método por *robustez do sinal* (×3), *custo/velocidade do teste* (×2), *fit com o estágio* (×2), *convergência com os outros* (×3). Se dois métodos divergem muito, **não fixe** — rode um teste-desempate antes.
5. **Fixe a âncora.** Aplique [`price-anchoring`](../../frameworks/price-anchoring.md): preço de referência alto e **crível** (custo de alternativas, valor entregue) — nunca um "de R$5000" que jamais existiu.
6. **Desenhe o packaging.** Aplique [`packaging-good-better-best`](../../frameworks/pricing/packaging-good-better-best.md): três tiers com um **tier-alvo** claro; ancore o tier alto primeiro. Use [`decoy-effect`](../../frameworks/pricing/decoy-effect.md) para tornar o alvo óbvio. [`value-based-pricing`](../../frameworks/pricing/value-based-pricing.md) costura valor→preço.
7. **Self-verify (Bloom + red-team).** Cada ponto tem método e faixa por trás? Os métodos convergem? O preço deriva do valor, ou escorreguei para custo+margem? *"O que o `unit-economics-stack-analyst` reprovaria?"* (preço que não deixa margem para liquidar o CAC). *"O que o `compliance-auditor` rejeitaria?"* (âncora fictícia). Corrija.
8. **Registre e passe os gates.** Logue cada ponto e teste no `price-test-registry` (`price_test_id`, método, faixa, indiferença, ótimo, tiers, âncora, decoy, convergência, `status: testado|inferido`). Registre a decisão e as alternativas podadas.

## Frameworks
[`van-westendorp`](../../frameworks/pricing/van-westendorp.md) · [`gabor-granger`](../../frameworks/pricing/gabor-granger.md) · [`conjoint-cbc`](../../frameworks/pricing/conjoint-cbc.md) · [`kano-model`](../../frameworks/pricing/kano-model.md) · [`value-based-pricing`](../../frameworks/pricing/value-based-pricing.md) · [`price-anchoring`](../../frameworks/price-anchoring.md) · [`packaging-good-better-best`](../../frameworks/pricing/packaging-good-better-best.md) · [`decoy-effect`](../../frameworks/pricing/decoy-effect.md).

## Outputs (Produz)
- **`artifact.pricing-wtp-sheet`** ([`template`](../../templates/strategy/pricing-wtp-template.md)) — métodos rodados, faixa de WTP (piso/indiferença/teto), convergência, packaging (good/better/best com tier-alvo), decoy, âncora de referência, status.
- **`decision.price-points`** e **`decision.packaging-tiers`** — os pontos e os tiers travados.
- **Registry escrito:** [`price-test-registry`](../../data/registries/price-test-registry.md).

## Definition of Done
Cada ponto de preço tem método e faixa por trás; ≥2 métodos convergem na faixa (ou o desempate está documentado quando a convergência é baixa); o preço **deriva do valor** medido, não de custo+margem; o packaging tem um tier-alvo claro com âncora; os três gates de pricing estão verdes; a decisão está no registry. Máximo de 3 ciclos antes de escalar.

## Gates
- [`pricing/pricing-value-derived-gate`](../../checklists/pricing/pricing-value-derived-gate.md)
- [`pricing/pricing-method-declared-gate`](../../checklists/pricing/pricing-method-declared-gate.md)
- [`pricing/pricing-packaging-gate`](../../checklists/pricing/pricing-packaging-gate.md)

## Métricas
Move KPIs da família **economics** ([`config.yaml`](../../config.yaml) `kpis:`), por fixar os pontos de preço de que toda a economia deriva:
- **`aov`** — os pontos de preço por tier/degrau e o packaging good-better-best determinam diretamente a receita por pedido.
- **`ltv_cac_ratio`** — preço derivado de valor (não cost-plus) é o que mantém a margem que sustenta um LTV:CAC saudável; preço fraco quebra a razão a jusante.
- **`front_end_cac_liquidation`** — o ponto de preço da atração define quanto do CAC a oferta de front-end consegue liquidar.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (família economics), com cada ponto/teste em [`price-test-registry`](../../data/registries/price-test-registry.md).

## Handoff
**Próxima task:** [`model-unit-economics`](model-unit-economics.md) — dono [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md), que recebe o preço/margem para o cálculo de CAC/LTV e a liquidação do CAC. Adiante, o [`money-model-designer`](../../agents/money-model-designer.md) recebe os **pontos de preço por degrau** (insumo direto da escada); o [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md), a âncora e o packaging para a apresentação do preço (valor antes do preço). **Garantia:** todo downstream recebe pontos derivados de valor, com método declarado e packaging com tier-alvo — nunca um número avulso "porque sim".
