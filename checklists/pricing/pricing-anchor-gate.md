---
id: checklist.pricing.pricing-anchor-gate
title: "Gate — Ancoragem Real (referência alta, crível e verdadeira)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [price-anchoring, pricing/decoy-effect, pricing/value-based-pricing]
registries: [price-test-registry, claim-registry]
tags: [gate, pricing, ancoragem, anchor, decoy, anti-fake, d2]
---

# Gate — Ancoragem Real

## Propósito
Este gate prova que a **âncora de preço é alta, crível e verdadeira**. Preço é mensagem: uma âncora bem-posta faz o ponto-alvo parecer óbvio de barato. Mas uma âncora **fictícia** — um "de R$5.000 por R$497" onde o R$5.000 nunca existiu — é ancoragem falsa, prima da escassez falsa, e o [`compliance-auditor`](../../agents/compliance-auditor.md) a veta. Este gate separa as duas: a âncora pode ser o custo real das alternativas, o valor entregue medido pela value equation, ou um tier superior que de fato existe e se vende. O `decoy` (isca) é legítimo quando é uma opção real que torna o alvo a escolha racional — não um número inventado. Ele protege a margem (ancorar alto defende o prêmio do mecanismo) sem cruzar para a fraude que destrói confiança e expõe a marca.

## Dono & Escopo
- **owner_agent:** `pricing-wtp-strategist` (define a âncora e o decoy). Sem poder de veto — **sinaliza** âncora fictícia ao [`compliance-auditor`](../../agents/compliance-auditor.md), que tem o veto de ancoragem falsa.
- **Artefato inspecionado:** os campos `ancora` e `decoy?` da `pricing-wtp-sheet` no [`price-test-registry`](../../data/registries/price-test-registry.md), e a proveniência da âncora (custo de alternativas, valor entregue, tier real) cruzada com o [`claim-registry`](../../data/registries/claim-registry.md) quando a âncora vira claim.

## Condição de Passagem
A âncora é alta, crível e tem origem verdadeira (alternativa real, valor medido ou tier existente), e qualquer decoy é uma opção real que torna o tier-alvo a escolha óbvia.

## Itens
1. **Âncora declarada.** Verificar: existe uma referência de preço alto explícita antes do ponto-alvo na `pricing-wtp-sheet`.
2. **Origem verdadeira.** Verificar: a âncora vem de fonte real — custo de alternativas, valor entregue (value equation) ou um tier que de fato existe e se vende — não de um número inventado.
3. **Sem "de/por" fictício.** Verificar: nenhum "de R$X por R$Y" onde o R$X jamais foi praticado; se aparece, é flag ao `compliance-auditor`.
4. **Âncora antecede o alvo.** Verificar: a referência alta é apresentada **antes** do preço-alvo (sequência de ancoragem), consistente com o que o [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) usa.
5. **Decoy é opção real.** Verificar: se há `decoy`, é uma opção genuína (ex.: "tier sem 1:1") que torna o alvo a escolha racional — não uma fantasia.
6. **Crível para o avatar.** Verificar: a âncora é alta mas plausível ao avatar (sofisticação do mercado), não absurda a ponto de queimar credibilidade.
7. **Rastreável.** Verificar: a origem da âncora está registrada no `price-test-registry` e, quando vira claim, no `claim-registry`.

## Evidência Exigida
Para marcar ✅: linkar a `pricing-wtp-sheet` mostrando a âncora, sua origem documentada e a posição antes do alvo (itens 1–4, 7), a definição do decoy como opção real (item 5) e a justificativa de credibilidade pela sofisticação (item 6). Âncora que vira claim aponta para o `claim-registry`.

## Protocolo de Falha
Item vermelho → o `pricing-wtp-strategist` troca a âncora fictícia por uma âncora real (custo de alternativas, valor entregue) e re-submete; "de/por" inventado é reprovação e flag ao [`compliance-auditor`](../../agents/compliance-auditor.md). Decoy que não é opção real é removido. Re-entrada: corrige `ancora`/`decoy?` no `price-test-registry`, registra a origem e re-submete. Mudança de âncora ou de tier reabre este gate e o [`pricing-packaging-gate`](pricing-packaging-gate.md).

## Links
- Gates irmãos: [`pricing-value-derived-gate`](pricing-value-derived-gate.md) · [`pricing-method-declared-gate`](pricing-method-declared-gate.md) · [`pricing-packaging-gate`](pricing-packaging-gate.md) · [`pricing-kano-gate`](pricing-kano-gate.md)
- Frameworks: [`price-anchoring`](../../frameworks/price-anchoring.md) · [`decoy-effect`](../../frameworks/pricing/decoy-effect.md) · [`value-based-pricing`](../../frameworks/pricing/value-based-pricing.md)
- Registries: [`price-test-registry`](../../data/registries/price-test-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md)
- Agentes: [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) · [`compliance-auditor`](../../agents/compliance-auditor.md) · [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md)
- Relacionado: [`vsl-value-before-price-gate`](../vsl/vsl-value-before-price-gate.md)
