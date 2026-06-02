---
id: checklist.affiliate.affiliate-swipe-kit-gate
title: "Gate — Swipe Kit (cada peça é original, lastreada e carrega a disclosure de afiliação)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
frameworks: [launch/affiliate-army, launch/cart-open-close]
registries: [decision-registry]
tags: [gate, afiliados, swipe, disclosure, claim, lastro, d6]
---

# Gate — Swipe Kit

## Propósito
Este gate prova que **cada peça de swipe do afiliado é original, restrita ao que o Offer Book prova, e carrega a disclosure de afiliação**. Ele existe porque o que o afiliado promete em nome da marca também precisa de lastro e de divulgação: a relação de afiliação deve ser declarada (FTC/CDC), e nenhum parceiro pode fazer claim de resultado sem a prova catalogada. O `affiliate-program-architect` monta o swipe a partir dos ângulos do Offer Book em **redação original** (sem copiar terceiros), restringe cada claim ao que a prova sustenta, e adiciona a disclosure obrigatória em cada peça. O swipe de fechamento usa a escassez **verdadeira** do `cart-open-close`. Vale o princípio `truthful_scarcity` somado a `evidence_before_opinion`: claim sem lastro e escassez inventada são veto. Este gate julga **só o conteúdo do swipe, o lastro e a disclosure** — o fit econômico é do `affiliate-prizes-aligned-gate`, e a prontidão do funil é do `affiliate-funnel-gate`. Swipe com claim sem prova, sem disclosure, ou com escassez falsa é corrigido antes de liberar e sinalizado ao compliance, dono do veto.

## Dono & Escopo
- **owner_agent:** `affiliate-program-architect` (monta o swipe original, restringe o claim e exige a disclosure).
- **Artefato inspecionado:** o swipe do `affiliate-blackbook`, cruzado com os ângulos e a prova do `offer-book`. O swipe referencia o [`swipe-registry`](../../data/registries/swipe-registry.md); a prova de cada claim aponta ao [`proof-registry`](../../data/registries/proof-registry.md) e ao [`claim-registry`](../../data/registries/claim-registry.md). As decisões vão ao [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
Cada peça de swipe é redação original, com todo claim lastreado, escassez verdadeira e a disclosure de afiliação presente.

## Itens
1. **Redação original.** Verificar: o swipe é escrito em redação original, sem copiar copy de terceiros.
2. **Claim lastreado.** Verificar: cada afirmação do swipe se restringe ao que o Offer Book prova.
3. **Disclosure presente.** Verificar: a divulgação de afiliação aparece em **toda** peça (FTC/CDC).
4. **Escassez verdadeira.** Verificar: o swipe de fechamento usa o cart-close real, não urgência inventada.
5. **Ligado ao swipe-registry.** Verificar: o swipe referencia o `swipe-registry` e cada claim aponta ao `proof-registry`/`claim-registry`.
6. **Sem promessa de ROI sem prova.** Verificar: nenhum número de resultado sem o lastro do Offer Book.

## Evidência Exigida
Para marcar ✅: linkar o swipe do `affiliate-blackbook` com a disclosure visível em cada peça, mais a prova de cada claim no [`proof-registry`](../../data/registries/proof-registry.md)/[`claim-registry`](../../data/registries/claim-registry.md) e a referência ao [`swipe-registry`](../../data/registries/swipe-registry.md). O `offer-book` que limita os claims e a escassez de fechamento verdadeira ficam citados. As decisões ficam no [`decision-registry`](../../data/registries/decision-registry.md).

## Protocolo de Falha
Item vermelho → o `affiliate-program-architect` **não libera** o swipe até cada peça ter disclosure e cada claim ter lastro. Swipe sem disclosure ele completa antes (exigência FTC/CDC). Claim de afiliado sem lastro ele restringe ao que o Offer Book prova. Escassez de fechamento inventada vira a escassez real do `cart-open-close`. O arquiteto **não tem veto**, mas recusa publicar swipe sem lastro/disclosure e **sinaliza** ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto sobre claim sem prova e escassez falsa. A prontidão do funil que distribui o swipe é do [`affiliate-funnel-gate`](affiliate-funnel-gate.md). Re-entrada: tornar o swipe original, lastrear cada claim, adicionar a disclosure e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md) · [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`swipe-registry`](../../data/registries/swipe-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md)
- Agentes: [`affiliate-program-architect`](../../agents/affiliate-program-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`affiliate-prizes-aligned-gate`](affiliate-prizes-aligned-gate.md) · [`affiliate-leaderboard-gate`](affiliate-leaderboard-gate.md) · [`affiliate-referral-tracking-gate`](affiliate-referral-tracking-gate.md) · [`affiliate-funnel-gate`](affiliate-funnel-gate.md)
