---
id: checklist.unit-econ.unit-econ-breakeven-gate
title: "Gate — Ponto de Equilíbrio e AOV Conhecidos por Degrau"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [offer-stack-builder, guarantee-design, scarcity-urgency-engine, magic-naming, risk-reversal-ladder]
registries: [offer-registry]
tags: [gate, unit-econ, breakeven, aov, ponto-de-equilibrio, d2]
---

# Gate — Ponto de Equilíbrio e AOV Conhecidos por Degrau

## Propósito
Este gate prova que o **ponto de equilíbrio** da oferta e o **AOV** (valor médio de pedido) por degrau estão calculados — quantas vendas, ou que AOV, fazem a operação cobrir custos fixos e variáveis. Ele existe porque uma oferta pode liquidar o CAC no front e ainda assim não pagar a estrutura: sem saber o break-even, o negócio não sabe a que volume começa a lucrar nem qual AOV sustenta a escada. O gate conecta o AOV de front e o AOV total (ao longo do money model) ao custo de entrega de cada degrau, expondo o volume mínimo viável. Diferente do gate de margem (que olha a margem unitária) e do de liquidação (a atração cobre o CAC), este olha o **limiar de viabilidade do conjunto**: a partir de que ponto a oferta deixa de queimar caixa. É o gate que dá ao `money-model-designer` e ao chief o número que separa "vende" de "lucra".

## Dono & Escopo
- **owner_agent:** `unit-economics-stack-analyst` (calcula break-even e AOV; sem veto, sinaliza).
- **Artefato inspecionado:** o **ponto de equilíbrio**, o `aov_front` e o `aov_total` na `unit-economics-sheet` no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O AOV de front e total estão calculados por degrau, o ponto de equilíbrio (volume ou AOV mínimo) está conhecido, e os custos fixos e variáveis estão declarados.

## Itens
1. **AOV de front conhecido.** Verificar: o `aov_front` (atração + take-rate dos upsells de front) está calculado.
2. **AOV total conhecido.** Verificar: o `aov_total` ao longo da escada (até continuidade) está calculado com take-rates declarados.
3. **Custos mapeados.** Verificar: custos fixos (estrutura) e variáveis (entrega por degrau) estão declarados e separados.
4. **Ponto de equilíbrio calculado.** Verificar: o break-even (volume de vendas ou AOV mínimo que cobre custos) está computado.
5. **Break-even confrontado com a meta.** Verificar: o volume de break-even é alcançável pela demanda projetada (não exige um volume irreal).
6. **AOV por degrau coerente com o stack.** Verificar: o AOV reflete o offer-stack e os preços reais por degrau (sem inflar o take-rate).
7. **Equilíbrio registrado.** Verificar: AOV (front/total), custos e break-even estão no [`offer-registry`](../../data/registries/offer-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar a `unit-economics-sheet` no [`offer-registry`](../../data/registries/offer-registry.md) (`aov_front`, `aov_total`, custos fixos/variáveis), o cálculo do ponto de equilíbrio (volume ou AOV mínimo), e os take-rates usados. O confronto do volume de break-even com a demanda projetada é a evidência-resumo de que o equilíbrio é alcançável.

## Protocolo de Falha
Item vermelho → não fecha o cálculo. AOV usando take-rate otimista → ajusta para pressuposto defensável. Custos não separados (fixo vs variável) → separa antes de calcular o break-even. Break-even exige volume irreal → testa ≥3 alavancas (subir AOV via stack/upsell, reduzir custo de entrega, ajustar preço) e devolve ao [`money-model-designer`](../../agents/money-model-designer.md) a de menor dano. AOV inflado vs stack real → recalcula com os preços e take-rates reais. O analista **não tem veto**: se o break-even é inalcançável, **sinaliza** ao [`money-model-designer`](../../agents/money-model-designer.md) e ao [`offerbook-chief`](../../agents/offerbook-chief.md) — a espinha ou o preço precisam mudar. Re-entrada: recalculado o equilíbrio, o gate é re-submetido.

## Links
- Frameworks: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`guarantee-design`](../../frameworks/guarantee-design.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`magic-naming`](../../frameworks/magic-naming.md) · [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md)
- Template: [`unit-economics-template`](../../templates/strategy/unit-economics-template.md)
- Gates irmãos: [`unit-econ-ltv-cac-gate`](unit-econ-ltv-cac-gate.md) · [`unit-econ-payback-gate`](unit-econ-payback-gate.md) · [`unit-econ-cac-liquidation-gate`](unit-econ-cac-liquidation-gate.md) · [`unit-econ-margin-gate`](unit-econ-margin-gate.md)
