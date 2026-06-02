---
id: checklist.pricing.pricing-kano-gate
title: "Gate — Classificação Kano das Features (básica, linear, encantadora)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [pricing/kano-model, pricing/conjoint-cbc, pricing/packaging-good-better-best, pricing/value-based-pricing]
registries: [price-test-registry, offer-registry]
tags: [gate, pricing, kano, features, conjoint, wtp, d2]
---

# Gate — Classificação Kano das Features

## Propósito
Este gate prova que as features da oferta foram **classificadas por Kano** — básicas, lineares e encantadoras — e que essa classificação guiou o packaging e o preço. Nem toda feature move WTP do mesmo jeito: as **básicas** são esperadas (sua ausência irrita, sua presença não encanta), as **lineares** somam satisfação proporcional, e as **encantadoras** surpreendem e justificam o prêmio. Subir o preço empilhando básicas não funciona; subir empilhando encantadoras, sim. O gate exige que a feature que mais move WTP (corroborada por conjoint quando disponível) seja alocada ao tier que precisa dela — tipicamente a encantadora sobe para o "best" e ancora. Sem essa disciplina, o packaging vira uma lista de itens de peso igual, o tier-alvo perde força e a margem fica na mesa. Ele alimenta diretamente a [`pricing-packaging-gate`](pricing-packaging-gate.md).

## Dono & Escopo
- **owner_agent:** `pricing-wtp-strategist` (classifica as features e aloca por tier). Sem poder de veto.
- **Artefato inspecionado:** a classificação Kano por feature na `pricing-wtp-sheet` e o `metodo` correspondente no [`price-test-registry`](../../data/registries/price-test-registry.md), cruzados com os part-worths do conjoint quando houver, e a alocação por tier que chega ao [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
Cada feature relevante está classificada como básica, linear ou encantadora, e a alocação por tier reflete essa classificação, com a encantadora sustentando o tier-alvo ou a âncora.

## Itens
1. **Features listadas.** Verificar: as features da oferta estão enumeradas na `pricing-wtp-sheet` antes de classificar.
2. **Classificação Kano por feature.** Verificar: cada feature recebe um rótulo — básica, linear ou encantadora — não fica sem classificação.
3. **Corroboração por conjoint (quando viável).** Verificar: a feature de maior part-worth no conjoint bate com a marcada encantadora; divergência forte é investigada.
4. **Básicas cobertas no tier de entrada.** Verificar: o "good" já inclui as básicas — faltar uma básica irrita e derruba conversão de todos os tiers.
5. **Encantadora sustenta alvo/âncora.** Verificar: a feature encantadora sobe para o tier-alvo ou para o "best" (âncora), justificando o prêmio.
6. **Sem inflar preço com básicas.** Verificar: nenhum tier sobe de preço empilhando só básicas/lineares sem uma encantadora real.
7. **Rastreável ao registry.** Verificar: a classificação e a alocação por tier estão gravadas no `price-test-registry` e refletidas no `offer-registry`.

## Evidência Exigida
Para marcar ✅: linkar a tabela Kano por feature na `pricing-wtp-sheet` (itens 1–2, 7), o cruzamento com part-worths do conjoint quando houver (item 3), a presença das básicas no "good" (item 4) e a alocação da encantadora ao tier-alvo/âncora com a justificativa de prêmio (itens 5–6).

## Protocolo de Falha
Item vermelho → o `pricing-wtp-strategist` reclassifica as features e realoca por tier; preço inflado só com básicas é reprovação. Se o conjoint contradiz a classificação Kano, roda a corroboração antes de fixar (consistente com [`pricing-method-declared-gate`](pricing-method-declared-gate.md)). Re-entrada: atualiza a classificação no `price-test-registry`, ajusta o packaging e re-submete. Mudança de feature ou de tier reabre este gate e a [`pricing-packaging-gate`](pricing-packaging-gate.md).

## Links
- Gates irmãos: [`pricing-value-derived-gate`](pricing-value-derived-gate.md) · [`pricing-method-declared-gate`](pricing-method-declared-gate.md) · [`pricing-anchor-gate`](pricing-anchor-gate.md) · [`pricing-packaging-gate`](pricing-packaging-gate.md)
- Frameworks: [`kano-model`](../../frameworks/pricing/kano-model.md) · [`conjoint-cbc`](../../frameworks/pricing/conjoint-cbc.md) · [`packaging-good-better-best`](../../frameworks/pricing/packaging-good-better-best.md) · [`value-based-pricing`](../../frameworks/pricing/value-based-pricing.md)
- Registries: [`price-test-registry`](../../data/registries/price-test-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) · [`value-equation-engineer`](../../agents/value-equation-engineer.md)
- Relacionado: [`value-no-orphan-lever-gate`](../value/value-no-orphan-lever-gate.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
