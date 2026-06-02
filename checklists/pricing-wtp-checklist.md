---
id: checklist.pricing-wtp-checklist
title: "Checklist — Preço & WTP (preço deriva de valor com método declarado)"
type: checklist
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [pricing/value-based-pricing, pricing/van-westendorp, pricing/gabor-granger, pricing/conjoint-cbc, pricing/kano-model, price-anchoring, pricing/packaging-good-better-best, pricing/decoy-effect]
registries: [price-test-registry]
tags: [checklist, pricing, wtp, value-based, packaging, ancoragem, d2]
---

# Checklist — Preço & WTP

## Propósito
Este checklist prova que o preço **deriva de valor e da disposição a pagar (WTP)**, com um método declarado — nunca de custo nem de chute. Existe porque preço fixado por custo deixa dinheiro na mesa e preço chutado destrói margem ou afasta o comprador certo. Cada ponto de preço precisa rastrear a um método nomeado (van Westendorp, Gabor-Granger, conjoint, value-based) e a um número de WTP medido ou estimado com rigor. Sem este checklist verde, o money model e o unit economics herdam um número sem lastro. Ele encarna a disciplina de Ramanujam: converse sobre preço antes de construir, e ancore o valor antes do número. É o que transforma "quanto cobrar" em decisão rastreável.

## Dono & Escopo
- **owner_agent:** `pricing-wtp-strategist` (fixa preço, packaging e ancoragem a partir do valor percebido).
- **Artefato inspecionado:** o `artifact.pricing-wtp-sheet`, a `decision.price-points` e a `decision.packaging-tiers`, com os testes registrados no [`price-test-registry`](../data/registries/price-test-registry.md).

## Condição de Passagem
Cada preço deriva do valor por um método nomeado, o número de WTP está registrado, o packaging tem ancoragem coerente, e nenhum preço foi fixado por custo ou chute.

## Itens
1. **Método declarado.** Como verificar: cada ponto de preço nomeia o método que o gerou (van Westendorp, Gabor-Granger, conjoint, value-based) no `price-test-registry`.
2. **WTP registrado.** Como verificar: o número de disposição a pagar (faixa ou ponto) está gravado com a fonte do dado, conforme `value-based-pricing`.
3. **Preço deriva de valor.** Como verificar: o preço aponta para o valor percebido do scorecard, não para o custo de produção; a ligação valor→preço está explícita.
4. **Ancoragem coerente.** Como verificar: o preço-âncora e o desconto (se houver) são reais e justificados, conforme `price-anchoring` — sem âncora inventada.
5. **Packaging good-better-best.** Como verificar: se há níveis, eles seguem uma escada clara de valor crescente, conforme `packaging-good-better-best`.
6. **Decoy intencional (se usado).** Como verificar: qualquer opção-isca existe para guiar a escolha ao plano-alvo, com lógica declarada, conforme `decoy-effect` — ou ausente.
7. **Preço por degrau do money model.** Como verificar: cada degrau da escada tem seu ponto de preço rastreável ao `price-test-registry`.
8. **Sem preço por custo.** Como verificar: nenhum preço foi calculado como custo + margem fixa; a justificativa é sempre valor/WTP.

## Evidência Exigida
Para marcar ✅: linkar a entrada do `price-test-registry` com o método nomeado e o número de WTP (itens 1–2), a ligação valor→preço no pricing-wtp-sheet (item 3), a justificativa da âncora (item 4) e a escada de packaging com valor crescente (item 5). O preço por degrau aparece rastreável à escada do money model (item 7).

## Protocolo de Falha
Item vermelho → o preço volta ao `pricing-wtp-strategist` com o defeito nomeado e **bloqueia o money model e o unit economics** (que herdam o número). Preço sem método ou sem WTP reabre o teste. Re-entrada: declarar método, medir/estimar WTP, atualizar o `price-test-registry`, re-submeter. Mudança no valor (scorecard) ou no packaging reabre este checklist e os cálculos de unit economics.

## Links
- Frameworks: [`value-based-pricing`](../frameworks/pricing/value-based-pricing.md) · [`van-westendorp`](../frameworks/pricing/van-westendorp.md) · [`gabor-granger`](../frameworks/pricing/gabor-granger.md) · [`conjoint-cbc`](../frameworks/pricing/conjoint-cbc.md) · [`kano-model`](../frameworks/pricing/kano-model.md) · [`price-anchoring`](../frameworks/price-anchoring.md) · [`packaging-good-better-best`](../frameworks/pricing/packaging-good-better-best.md) · [`decoy-effect`](../frameworks/pricing/decoy-effect.md)
- Registries: [`price-test-registry`](../data/registries/price-test-registry.md)
- Agentes: [`pricing-wtp-strategist`](../agents/pricing-wtp-strategist.md) · [`value-equation-engineer`](../agents/value-equation-engineer.md) · [`money-model-designer`](../agents/money-model-designer.md) · [`unit-economics-stack-analyst`](../agents/unit-economics-stack-analyst.md)
- Gates por agente: [`pricing/pricing-value-derived-gate`](pricing/pricing-value-derived-gate.md) · [`pricing/pricing-method-declared-gate`](pricing/pricing-method-declared-gate.md) · [`pricing/pricing-packaging-gate`](pricing/pricing-packaging-gate.md)
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate relacionado: [`offer-book-stack/offer-architecture-gate`](offer-book-stack/offer-architecture-gate.md)
