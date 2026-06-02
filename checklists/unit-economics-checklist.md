---
id: checklist.unit-economics-checklist
title: "Checklist — Unit Economics (LTV:CAC, payback e break-even conhecidos)"
type: checklist
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [offer-stack-builder, guarantee-design, scarcity-urgency-engine, magic-naming, risk-reversal-ladder]
registries: [offer-registry, price-test-registry]
tags: [checklist, unit-economics, ltv, cac, payback, break-even, d2]
---

# Checklist — Unit Economics

## Propósito
Este checklist prova que a **economia por cliente é conhecida**: LTV, CAC, razão LTV:CAC, payback e break-even estão calculados com números rastreáveis. Existe porque um lançamento que não sabe quanto pode pagar para adquirir um cliente quebra na escala — gasta mais para vender do que ganha. Cada número precisa de origem (preço testado, custo real, take-rate estimado), não de estimativa solta. Sem este checklist verde, o money model fica sem viabilidade e o funil sem teto de CAC. Ele encarna `evidence_before_opinion` aplicado ao caixa: a oferta só avança quando a matemática fecha. É o sinal verde econômico antes da copy custar dinheiro.

## Dono & Escopo
- **owner_agent:** `unit-economics-stack-analyst` (calcula CAC/LTV/AOV/margem/payback e monta o offer stack, a garantia e a escassez).
- **Artefato inspecionado:** o `artifact.unit-economics-sheet`, o `artifact.offer-stack` e a `decision.cac-liquidation-status`, com os números no [`offer-registry`](../data/registries/offer-registry.md) e os preços no [`price-test-registry`](../data/registries/price-test-registry.md).

## Condição de Passagem
LTV, CAC, razão LTV:CAC, payback e break-even estão calculados com números rastreáveis, e a liquidação de CAC no front-end está classificada — sem número solto.

## Itens
1. **CAC conhecido.** Como verificar: o custo de aquisição por cliente está calculado no `unit-economics-sheet`, com a base de cálculo declarada.
2. **LTV conhecido.** Como verificar: o valor do cliente ao longo do tempo está calculado, somando os degraus do money model com take-rate declarado.
3. **Razão LTV:CAC.** Como verificar: a razão está computada e comparada a um piso aceitável; abaixo do piso reprova.
4. **Payback declarado.** Como verificar: o tempo (ou número de transações) até recuperar o CAC está calculado e rastreável.
5. **Break-even conhecido.** Como verificar: o ponto de equilíbrio (unidades ou receita) está calculado para a oferta.
6. **Liquidação de CAC no front-end.** Como verificar: a `decision.cac-liquidation-status` declara se a oferta de atração liquida (ou não) o CAC, conforme a espinha do money model.
7. **Números rastreáveis.** Como verificar: cada número aponta para origem — preço no `price-test-registry`, custo real, take-rate estimado com base; nada é "achei que fosse".
8. **Offer stack e garantia coerentes.** Como verificar: o custo da garantia e dos bônus do `offer-stack` entra no cálculo de margem, conforme `guarantee-design` e `offer-stack-builder`.

## Evidência Exigida
Para marcar ✅: linkar o `unit-economics-sheet` com CAC, LTV, razão, payback e break-even (itens 1–5), a `decision.cac-liquidation-status` no `offer-registry` (item 6) e a origem de cada número — preço no `price-test-registry`, custos e take-rates (item 7). O custo de garantia/bônus aparece embutido na margem (item 8).

## Protocolo de Falha
Item vermelho → os números voltam ao `unit-economics-stack-analyst` com o defeito nomeado e **bloqueiam o money model** (sem viabilidade não há escada). Razão LTV:CAC abaixo do piso reabre preço (`pricing-wtp-strategist`) ou a escada (`money-model-designer`). Re-entrada: recalcular com origem rastreável, atualizar o `offer-registry`, re-submeter. Mudança de preço ou de take-rate reabre este checklist por inteiro.

## Links
- Frameworks: [`offer-stack-builder`](../frameworks/offer-stack-builder.md) · [`guarantee-design`](../frameworks/guarantee-design.md) · [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md) · [`magic-naming`](../frameworks/magic-naming.md) · [`risk-reversal-ladder`](../frameworks/risk-reversal-ladder.md)
- Registries: [`offer-registry`](../data/registries/offer-registry.md) · [`price-test-registry`](../data/registries/price-test-registry.md)
- Agentes: [`unit-economics-stack-analyst`](../agents/unit-economics-stack-analyst.md) · [`pricing-wtp-strategist`](../agents/pricing-wtp-strategist.md) · [`money-model-designer`](../agents/money-model-designer.md)
- Checklists vizinhos: [`offer-stack-checklist`](offer-stack-checklist.md) · [`guarantee-checklist`](guarantee-checklist.md)
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate relacionado: [`offer-book-stack/offer-architecture-gate`](offer-book-stack/offer-architecture-gate.md)
