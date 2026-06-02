---
id: checklist.pricing.pricing-packaging-gate
title: "Gate — Packaging com Tier-Alvo (good-better-best, não preço nu)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [pricing/packaging-good-better-best, pricing/decoy-effect, price-anchoring, pricing/value-based-pricing]
registries: [price-test-registry, offer-registry]
tags: [gate, pricing, packaging, good-better-best, tier-alvo, d2]
---

# Gate — Packaging com Tier-Alvo

## Propósito
Este gate prova que a oferta vem em **tiers (good-better-best) com um tier-alvo claro** — não como um preço único e nu. O packaging muda a pergunta do cliente de "compro ou não?" para "qual eu escolho?", e isso eleva conversão e ticket. Três preços soltos sem hierarquia confundem e derrubam a decisão; três tiers com um alvo desenhado (ancorado pelo "best", empurrado por um decoy) tornam a escolha óbvia. Este gate força a disciplina: cada tier tem uma alavanca dominante, um papel (entrada, alvo, âncora) e uma razão de existir. Ele costura com a [`pricing-anchor-gate`](pricing-anchor-gate.md) (a âncora é o tier alto) e com a [`pricing-kano-gate`](pricing-kano-gate.md) (a feature encantadora sobe para o "best"). O resultado alimenta a espinha: os pontos por degrau que o [`money-model-designer`](../../agents/money-model-designer.md) recebe.

## Dono & Escopo
- **owner_agent:** `pricing-wtp-strategist` (desenha os tiers e o tier-alvo). Sem poder de veto.
- **Artefato inspecionado:** o bloco `tiers{good, better, best}`, o `decoy?` e a marcação de tier-alvo da `pricing-wtp-sheet` no [`price-test-registry`](../../data/registries/price-test-registry.md), que vira insumo de preço por degrau no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
A oferta tem ao menos dois tiers com hierarquia clara, um tier-alvo explícito, e cada tier declara o que inclui e a alavanca dominante que o diferencia.

## Itens
1. **Tiers presentes.** Verificar: há ao menos dois tiers (alvo: good-better-best) na `pricing-wtp-sheet` — não um preço único nu.
2. **Tier-alvo explícito.** Verificar: um tier está marcado como ALVO (geralmente o "better") — a oferta sabe qual quer vender.
3. **Diferença clara entre tiers.** Verificar: cada tier lista o que inclui e a alavanca dominante (Sonho/Probabilidade/Tempo/Esforço) que o distingue do anterior.
4. **Âncora pelo tier alto.** Verificar: o "best" ancora a percepção (consistente com [`pricing-anchor-gate`](pricing-anchor-gate.md)) e é uma opção real.
5. **Decoy empurra o alvo (se usado).** Verificar: havendo decoy, ele torna o tier-alvo a escolha racional — não confunde.
6. **Hierarquia de preço coerente.** Verificar: os preços sobem com o valor entregue; nenhum tier custa mais e entrega menos.
7. **Pontos prontos para a espinha.** Verificar: os preços de cada tier estão disponíveis como insumo por degrau ao `money-model-designer` (no `offer-registry`/`price-test-registry`).

## Evidência Exigida
Para marcar ✅: linkar o bloco de packaging da `pricing-wtp-sheet` com os tiers, o tier-alvo marcado e a alavanca dominante de cada um (itens 1–3, 6), a âncora pelo "best" e o decoy quando houver (itens 4–5), e a passagem dos pontos por degrau ao `offer-registry`/`price-test-registry` (item 7).

## Protocolo de Falha
Item vermelho → o `pricing-wtp-strategist` redesenha o packaging com tier-alvo claro mais âncora e, se útil, decoy; três preços sem hierarquia ou preço único nu é reprovação. Re-entrada: atualiza `tiers{}` e a marcação de alvo no `price-test-registry` e re-submete. Mudança de tier reabre este gate e a [`pricing-anchor-gate`](pricing-anchor-gate.md); mudança de preço por degrau sinaliza ao `money-model-designer` para revalidar a espinha.

## Links
- Gates irmãos: [`pricing-value-derived-gate`](pricing-value-derived-gate.md) · [`pricing-method-declared-gate`](pricing-method-declared-gate.md) · [`pricing-anchor-gate`](pricing-anchor-gate.md) · [`pricing-kano-gate`](pricing-kano-gate.md)
- Frameworks: [`packaging-good-better-best`](../../frameworks/pricing/packaging-good-better-best.md) · [`decoy-effect`](../../frameworks/pricing/decoy-effect.md) · [`price-anchoring`](../../frameworks/price-anchoring.md) · [`value-based-pricing`](../../frameworks/pricing/value-based-pricing.md)
- Registries: [`price-test-registry`](../../data/registries/price-test-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) · [`money-model-designer`](../../agents/money-model-designer.md)
- Relacionado: [`money-model-four-parts-gate`](../money-model/money-model-four-parts-gate.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
