---
id: checklist.money-model.money-model-cac-liquidation-gate
title: "Gate — Liquidação de CAC (a atração paga a aquisição)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, money-model-designer/attraction-offer-design, money-model-designer/upsell-downsell-logic]
registries: [offer-registry, price-test-registry]
tags: [gate, money-model, cac, liquidacao, unit-economics, d2]
---

# Gate — Liquidação de CAC

## Propósito
Este gate prova o critério eliminatório da espinha: a **oferta de atração (mais o upsell imediato) liquida o custo de aquisição** no front-end. É a tese central de Hormozi de que um money model forte faz o cliente pagar a própria aquisição — e idealmente a de mais clientes — em menos de 30 dias. Uma escada bonita que não cobre o CAC é um buraco que escala prejuízo. Por isso, no Tree-of-Thoughts do designer, qualquer configuração que **não liquida o CAC** é podada de saída. Este gate é o ponto onde a espinha encontra os unit economics: sem CAC conhecido e coberto, a escada é marcada `não-validada` e o avanço para copy fica bloqueado.

## Dono & Escopo
- **owner_agent:** `money-model-designer` (valida a liquidação com o insumo do `unit-economics-stack-analyst`).
- **Artefato inspecionado:** a coluna `liquida_cac?` e os pontos de preço da espinha no [`offer-registry`](../../data/registries/offer-registry.md) e no [`price-test-registry`](../../data/registries/price-test-registry.md), cruzados com o `unit-economics-sheet` (CAC, AOV, margem, payback).

## Condição de Passagem
A receita de margem da atração mais o upsell imediato cobre o CAC dentro da janela alvo (meta <30 dias), com o ponto de liquidação nomeado na sequência.

## Itens
1. **CAC conhecido.** Verificar: existe um CAC (ou faixa) vindo do `unit-economics-sheet`; se ausente, o gate reprova e a espinha vira `não-validada`.
2. **Margem da atração calculada.** Verificar: a margem de contribuição do degrau de atração está no `price-test-registry`, não só o preço bruto.
3. **Ponto de liquidação nomeado.** Verificar: a sequência aponta **onde** o cliente paga a aquisição (ex.: no upsell #1), com `liquida_cac?` marcado nessa linha.
4. **Cobertura dentro da janela.** Verificar: atração+upsell imediato cobrem o CAC dentro da janela alvo (meta <30 dias); fora disso, reprova.
5. **Payback declarado.** Verificar: o payback estimado da escada está registrado e é coerente com o AOV e a margem.
6. **Configurações que não liquidam foram podadas.** Verificar: a decisão de configuração mostra que toda variante sem liquidação de CAC foi descartada.
7. **Status de validação coerente.** Verificar: a linha do `offer-registry` está `validada` apenas se o CAC é conhecido e coberto; senão, `não-validada`.

## Evidência Exigida
Para marcar ✅: linkar o cruzamento espinha × `unit-economics-sheet` com CAC, margem da atração e payback (itens 1–2, 5), a linha com `liquida_cac?` marcada (itens 3–4), a decisão de poda das configs que não liquidavam (item 6) e o `status` da escada no `offer-registry` (item 7).

## Protocolo de Falha
Item vermelho → o `money-model-designer` troca o tipo de oferta de atração (tripwire→challenge), antecipa o upsell, ou reprecifica com o [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) até o front-end cobrir o CAC. Sem CAC, escalona ao [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) e mantém a espinha `não-validada` com a copy bloqueada. Re-entrada: atualiza o `price-test-registry` e o `offer-registry` e re-submete. Mudança de preço ou de CAC reabre este gate.

## Links
- Sibling gates: [`money-model-four-parts-gate`](money-model-four-parts-gate.md) · [`money-model-sequence-gate`](money-model-sequence-gate.md) · [`money-model-cta-per-step-gate`](money-model-cta-per-step-gate.md) · [`money-model-propagation-gate`](money-model-propagation-gate.md)
- Frameworks: [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`attraction-offer-design`](../../frameworks/money-model-designer/attraction-offer-design.md) · [`upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`price-test-registry`](../../data/registries/price-test-registry.md)
- Agentes: [`money-model-designer`](../../agents/money-model-designer.md) · [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md)
- Relacionado: [`pricing-value-derived-gate`](../pricing/pricing-value-derived-gate.md)
