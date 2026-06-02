---
id: checklist.unit-econ.unit-econ-payback-gate
title: "Gate — Período de Payback Conhecido e Dentro do Aceitável"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [offer-stack-builder, guarantee-design, scarcity-urgency-engine, magic-naming, risk-reversal-ladder]
registries: [offer-registry]
tags: [gate, unit-econ, payback, caixa, d2, recuperacao-cac]
---

# Gate — Período de Payback Conhecido e Dentro do Aceitável

## Propósito
Este gate prova que o **período de payback** — o tempo até a margem acumulada de um cliente recuperar o CAC — foi calculado e cabe na realidade de caixa do negócio. Ele existe porque a razão LTV:CAC pode ser bonita e o negócio ainda quebrar por falta de caixa: se o CAC só volta em 12 meses mas o negócio precisa reinvestir em aquisição todo mês, o caixa seca antes de o LTV se realizar. O gate materializa o KPI `payback_period` do `config.yaml` e a verdade de que **velocidade de recuperação do CAC financia o crescimento**. Diferente do gate LTV:CAC (proporção de longo prazo) e do de liquidação (a atração cobre o CAC no front), este mede **o tempo**: em quantos dias/meses o cliente paga o próprio custo de aquisição? Um payback curto permite reinvestir rápido; um longo trava o crescimento mesmo com unidade lucrativa. É o gate que protege o fluxo de caixa, não só a lucratividade no papel.

## Dono & Escopo
- **owner_agent:** `unit-economics-stack-analyst` (calcula o payback; sem veto, sinaliza ao money-model e ao chief).
- **Artefato inspecionado:** o **`payback`** e a curva de recuperação do CAC na `unit-economics-sheet` no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O período de payback está calculado a partir da margem acumulada por degrau, cabe na realidade de caixa do negócio, e os pressupostos de take-rate estão declarados.

## Itens
1. **Payback calculado.** Verificar: o `payback` está computado como o tempo até a margem acumulada do cliente igualar o CAC.
2. **Usa margem, não receita.** Verificar: a curva de recuperação usa margem de contribuição por degrau, não faturamento.
3. **Take-rate declarado.** Verificar: os pressupostos de conversão de upsell/continuidade que alimentam a curva estão explícitos (não otimistas sem base).
4. **Dentro do aceitável.** Verificar: o payback está dentro da janela de caixa do caso (alvo típico < 30–90 dias conforme o modelo) ou o desvio está justificado.
5. **Curva por degrau.** Verificar: a recuperação está mapeada ao longo da escada (front-end → upsell → continuidade), mostrando **quando** o CAC é coberto.
6. **Sensibilidade quando estimado.** Verificar: se há inputs estimados, a sensibilidade mostra como o payback muda com CAC/take-rate diferentes.
7. **Payback registrado.** Verificar: o `payback` e a curva estão no [`offer-registry`](../../data/registries/offer-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar a `unit-economics-sheet` no [`offer-registry`](../../data/registries/offer-registry.md) (campo `payback`), a curva de margem acumulada por degrau, e os pressupostos de take-rate declarados. A janela de caixa do caso (com a comparação payback × janela aceitável) e a sensibilidade quando há estimativas são a evidência-resumo de que o caixa não seca antes da recuperação.

## Protocolo de Falha
Item vermelho → não fecha o cálculo. Payback usando receita bruta → recalcula com margem. Take-rate otimista sem base → ajusta para um pressuposto defensável e declara. Payback longo demais (estoura a janela de caixa) → testa ≥3 alavancas (upsell mais cedo, continuidade no checkout, bump de velocidade) e devolve ao [`money-model-designer`](../../agents/money-model-designer.md) a que encurta a recuperação com menor dano. Inputs estimados sem sensibilidade → adiciona a curva. O analista **não tem veto**: se nenhum arranjo honesto encurta o payback ao aceitável, **sinaliza** ao [`money-model-designer`](../../agents/money-model-designer.md) e ao [`offerbook-chief`](../../agents/offerbook-chief.md). Re-entrada: recalculado o payback, o gate é re-submetido.

## Links
- Frameworks: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`guarantee-design`](../../frameworks/guarantee-design.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`magic-naming`](../../frameworks/magic-naming.md) · [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Template: [`unit-economics-template`](../../templates/strategy/unit-economics-template.md)
- Gates irmãos: [`unit-econ-ltv-cac-gate`](unit-econ-ltv-cac-gate.md) · [`unit-econ-breakeven-gate`](unit-econ-breakeven-gate.md) · [`unit-econ-cac-liquidation-gate`](unit-econ-cac-liquidation-gate.md) · [`unit-econ-margin-gate`](unit-econ-margin-gate.md)
