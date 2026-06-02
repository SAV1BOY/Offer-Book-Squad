---
id: task.offer-architecture.model-unit-economics
title: "Model Unit Economics — Calcular CAC/LTV/AOV/Payback, Montar o Stack/Garantia/Escassez e Validar a Liquidação do CAC"
type: task
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
consumes:
  - artifact.pricing-wtp-sheet
  - artifact.money-model
  - artifact.value-equation-scorecard
  - artifact.mechanism-sheet
produces:
  - artifact.unit-economics-sheet
  - artifact.offer-stack
  - artifact.guarantee
  - decision.cac-liquidation-status
frameworks:
  - offer-stack-builder
  - guarantee-design
  - scarcity-urgency-engine
  - magic-naming
  - risk-reversal-ladder
checklists:
  - unit-economics-checklist
  - offer-stack-checklist
  - guarantee-checklist
registries: [offer-registry]
metrics: [cac, ltv_cac_ratio, payback_period, front_end_cac_liquidation, aov]
tags: [offer-architecture, unit-economics, cac, ltv, aov, payback, offer-stack, garantia, escassez, magic-naming, d2]
---

# Model Unit Economics — calcular CAC/LTV/AOV/payback, montar o stack/garantia/escassez e validar a liquidação do CAC

## Objetivo
Provar, com números, que a oferta de atração liquida o CAC no front-end e empilhar o valor (stack + garantia + escassez verdadeira + nome MAGIC) de modo que o preço pareça uma pechincha — sem nenhuma escassez falsa — no estado em que a matemática fecha e a embalagem de valor está pronta.

## Agente dono
[`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md). O alarme aritmético do squad e montador da embalagem de valor. Não escreve copy, não fixa o preço. Sem poder de veto — suas flags acionam os vetos do `compliance-auditor` (escassez falsa) e do `value-equation-engineer` (item órfão).

## Gatilho / Quando
Roda em D2, quando: (a) há preço por valor e um esboço de escada; (b) pedem o cálculo de CAC/LTV/AOV/margem/payback; (c) pedem para montar o offer stack, a garantia, a escassez e o naming. **Pré-condição:** os **pontos de preço** do [`pricing-wtp-strategist`](set-pricing-wtp.md) e a **forma da escada** do [`money-model-designer`](design-money-model.md) — sem eles não há o que somar nem o que liquidar; do value scorecard tiro o custo×delta de cada componente. Se faltam os custos de aquisição/entrega, calculo o que dá e marco **estimado**, declarando as suposições. Se a margem não comporta nenhum CAC plausível, **sinalizo** ao money-model e ao chief — a oferta não fecha.

## Inputs (Consome)
- **`artifact.pricing-wtp-sheet`** (do pricing) — os pontos de preço por tier/degrau e a margem implícita.
- **`artifact.money-model`** (do money-model-designer; pode entrar em iteração) — a sequência, para somar AOV ao longo da escada e localizar **onde** o CAC é liquidado.
- **`artifact.value-equation-scorecard`** — o custo de entrega × delta de cada componente, para empilhar só o que paga seu lugar.
- **`artifact.mechanism-sheet`** — o mecanismo (matéria-prima do naming MAGIC e da escassez honesta — por que é limitado de verdade).
- **Registry escrito:** [`offer-registry`](../../data/registries/offer-registry.md).

## Procedimento
1. **Calcule a unidade.** CAC, AOV (front e total), margem de contribuição, LTV, payback, razão LTV:CAC. Use LTV com margem e payback, não receita bruta — LTV:CAC bonito que estoura o caixa é falso positivo.
2. **Verifique a liquidação do CAC.** Some a receita do front-end (atração + take-rate dos upsells imediatos). Localize **onde** na escada o cliente paga a aquisição. Abaixo do CAC → ainda não liquida.
3. **Corrija quando não fecha (Tree-of-Thoughts).** Gere ≥3 alavancas de correção e pontue por *recupera liquidação?* (×3), *dano à conversão* (×2, penaliza), *esforço operacional* (×2, penaliza), *verdade/compliance* (×3). Qualquer alavanca que dependa de **escassez falsa** é podada de saída — prefiro reportar que a oferta não fecha a mentir.
4. **Monte o offer stack.** Aplique [`offer-stack-builder`](../../frameworks/offer-stack-builder.md): liste cada item com valor ancorado **real** até a soma percebida superar o preço. Sem item órfão (que o value-engineer vetaria) e sem âncora fictícia.
5. **Escolha a garantia.** Aplique [`guarantee-design`](../../frameworks/guarantee-design.md) + [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md): a reversão que a operação **sustenta**. Garantia que a operação não honra → desça a escada de reversão até um nível exequível.
6. **Desenhe a escassez/urgência verdadeira.** Aplique [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md): só limite **real** (turma de 100 por capacidade de mentoria, janela de matrícula datada). Documente o motivo para o compliance.
7. **Dê o nome MAGIC.** Aplique [`magic-naming`](../../frameworks/magic-naming.md): nome que faz a oferta saltar, ancorado no mecanismo.
8. **Self-verify (Bloom + red-team).** Todos os números calculados (ou estimados com suposição)? Localizei onde o CAC é liquidado? Se não liquida, testei ≥3 alavancas? O stack tem valor > preço sem órfãos? A garantia é exequível? *"O que o `compliance-auditor` rejeitaria?"* (escassez sem motivo, garantia inexequível, âncora fictícia). Corrija.
9. **Registre e passe os gates.** Logue a economia e o stack no `offer-registry` (CAC, AOV, margem, LTV, payback, LTV:CAC, `cac_liquidado`, ponto de liquidação, stack, valor percebido, garantia, escassez+motivo, nome MAGIC). Registre a decisão de liquidação e as suposições quando estimado.

## Frameworks
- [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) — empilhar valor item a item > preço.
- [`guarantee-design`](../../frameworks/guarantee-design.md) + [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md) — reversão de risco exequível.
- [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) — limite real documentado.
- [`magic-naming`](../../frameworks/magic-naming.md) — nome MAGIC da oferta.

## Outputs (Produz)
- **`artifact.unit-economics-sheet`** ([`template`](../../templates/strategy/unit-economics-template.md)) — CAC/AOV/margem/LTV/payback/LTV:CAC + liquidação do CAC e seu ponto na escada.
- **`artifact.offer-stack`** ([`template`](../../templates/offer/offer-stack-template.md)) — itens com valor ancorado vs preço.
- **`artifact.guarantee`** ([`template`](../../templates/offer/guarantee-template.md)) — tipo + exequibilidade.
- **`decision.cac-liquidation-status`** — sim / não / estimado, com o ponto de liquidação.
- **Registry escrito:** [`offer-registry`](../../data/registries/offer-registry.md).

## Definition of Done
CAC, AOV, margem, LTV, payback e LTV:CAC estão calculados (ou estimados com suposição explícita); a liquidação do CAC está **confirmada** (ou reportada como não-fechada com as alavancas propostas); o stack tem valor percebido > preço sem itens órfãos; a garantia é exequível; a escassez é 100% real com motivo documentado; a oferta tem nome MAGIC; os três gates estão verdes. Máximo de 3 ciclos antes de escalar.

## Gates
- [`unit-economics-checklist`](../../checklists/unit-economics-checklist.md)
- [`offer-stack-checklist`](../../checklists/offer-stack-checklist.md)
- [`guarantee-checklist`](../../checklists/guarantee-checklist.md)

## Métricas
Move KPIs da família **economics** ([`config.yaml`](../../config.yaml) `kpis:`), por ser quem calcula a unidade e valida a liquidação do CAC:
- **`cac`**, **`ltv_cac_ratio`** e **`payback_period`** — esta task **calcula** os três (CAC, LTV:CAC e payback); o veredito aritmético aqui é a fonte direta da família.
- **`front_end_cac_liquidation`** — confirma onde na escada a atração+upsell liquidam o CAC, o KPI central de "% do CAC pago pela atração".
- **`aov`** — soma o AOV de front e total ao longo do stack/escada.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (família economics), com a economia gravada em [`offer-registry`](../../data/registries/offer-registry.md).

## Handoff
**Próxima task:** [`design-money-model`](design-money-model.md) — dono [`money-model-designer`](../../agents/money-model-designer.md), que recebe o **veredito de liquidação do CAC** e a economia por degrau para **fechar a espinha** (relação iterativa: ele desenha a forma, eu valido a conta, ele fecha). Adiante, o [`offerbook-chief`](../../agents/offerbook-chief.md) recebe os números para o gate `unit_economics_known`; o [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) e o [`funnel-architect`](../../agents/funnel-architect.md) recebem o offer stack, a garantia, a escassez verdadeira e o nome MAGIC prontos para apresentar. **Garantia:** todo downstream recebe economia conhecida (ou estimada com suposição), liquidação de CAC declarada, stack com valor > preço, garantia exequível e escassez 100% real.
