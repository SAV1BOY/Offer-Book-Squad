---
id: checklist.pricing.pricing-value-derived-gate
title: "Gate — Preço Derivado de Valor (nunca de custo)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [pricing/value-based-pricing, value-equation, pricing/van-westendorp, pricing/gabor-granger]
registries: [price-test-registry, offer-registry]
tags: [gate, pricing, valor, wtp, anti-cost-plus, d2]
---

# Gate — Preço Derivado de Valor

## Propósito
Este gate prova que cada ponto de preço **deriva do valor percebido e da disposição a pagar (WTP)** do avatar — jamais de custo mais margem. Ele protege o princípio `price_value_derived` e a disciplina de Ramanujam de conversar sobre preço antes de construir o produto. A maioria erra **barateando**: subprecifica por medo e joga fora a margem que pagaria a aquisição. O preço é a única alavanca que multiplica receita sem custo de entrega; ancorá-lo no custo desperdiça-a. Este gate liga o preço ao trabalho do [`value-equation-engineer`](../../agents/value-equation-engineer.md): nenhum número é defensável sem o valor por alavanca (Sonho, Probabilidade, Tempo, Esforço) por trás dele. É também o ponto onde o preço encontra os unit economics — um preço derivado de valor precisa deixar margem para a atração liquidar o CAC.

## Dono & Escopo
- **owner_agent:** `pricing-wtp-strategist` (deriva o preço do valor; recusa cost-plus). Sem poder de veto — **sinaliza** ao [`offerbook-chief`](../../agents/offerbook-chief.md) se houver imposição de custo mais margem.
- **Artefato inspecionado:** a `pricing-wtp-sheet` e cada ponto no [`price-test-registry`](../../data/registries/price-test-registry.md), cruzados com o `value-equation-scorecard` (valor por alavanca) e com a faixa de WTP estimada.

## Condição de Passagem
Cada ponto de preço aponta para o valor percebido por alavanca que o sustenta e para uma faixa de WTP, sem que o custo tenha servido de base do número.

## Itens
1. **Valor por alavanca mapeado.** Verificar: existe o `value-equation-scorecard` com valor percebido por alavanca; sem ele, o gate reprova e devolve ao `value-equation-engineer`.
2. **Preço ancorado no valor.** Verificar: cada ponto referencia a(s) alavanca(s) dominante(s) que o justifica, não uma planilha de custo.
3. **Faixa de WTP presente.** Verificar: há piso/teto de WTP por trás do ponto (de método, §[`pricing-method-declared-gate`](pricing-method-declared-gate.md)), não um número solto.
4. **Custo só como piso de margem.** Verificar: o custo aparece, no máximo, como piso que protege a margem — nunca como a base que define o preço.
5. **Sem subprecificação por medo.** Verificar: se a WTP comporta mais, o ponto não foi rebaixado sem motivo; a margem perdida está justificada ou corrigida.
6. **Margem para liquidar o CAC.** Verificar: o preço deixa margem de contribuição suficiente para a atração liquidar o CAC (insumo ao [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md)).
7. **Rastreável ao registry.** Verificar: o vínculo preço→valor→WTP está gravado no `price-test-registry` (`traceability_before_eloquence`).

## Evidência Exigida
Para marcar ✅: linkar a `pricing-wtp-sheet` mostrando, por ponto, a alavanca de valor que o sustenta e a faixa de WTP (itens 1–3, 7), a nota de que o custo entra só como piso (item 4), a justificativa de margem versus WTP (item 5) e a margem de contribuição passada ao unit-econ (item 6).

## Protocolo de Falha
Item vermelho → o `pricing-wtp-strategist` re-deriva o ponto a partir do valor mapeado; cost-plus disfarçado é reprovação. Sem valor por alavanca, devolve ao [`value-equation-engineer`](../../agents/value-equation-engineer.md). Se alguém impõe custo mais margem, escalona ao [`offerbook-chief`](../../agents/offerbook-chief.md) (viola `price_value_derived`). Re-entrada: atualiza a `pricing-wtp-sheet` e o `price-test-registry` e re-submete. Mudança de valor mapeado ou de ponto de preço reabre este gate.

## Links
- Gates irmãos: [`pricing-method-declared-gate`](pricing-method-declared-gate.md) · [`pricing-anchor-gate`](pricing-anchor-gate.md) · [`pricing-packaging-gate`](pricing-packaging-gate.md) · [`pricing-kano-gate`](pricing-kano-gate.md)
- Frameworks: [`value-based-pricing`](../../frameworks/pricing/value-based-pricing.md) · [`value-equation`](../../frameworks/value-equation.md) · [`van-westendorp`](../../frameworks/pricing/van-westendorp.md) · [`gabor-granger`](../../frameworks/pricing/gabor-granger.md)
- Registries: [`price-test-registry`](../../data/registries/price-test-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) · [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Relacionado: [`money-model-cac-liquidation-gate`](../money-model/money-model-cac-liquidation-gate.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
