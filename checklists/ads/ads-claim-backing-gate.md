---
id: checklist.ads.ads-claim-backing-gate
title: "Gate — Lastro de Claim em Ads (nenhum gancho sem prova)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
frameworks: [proof-to-claim-chain, copy/hook-frameworks, lead-types]
registries: [control-registry, claim-registry, proof-registry]
tags: [gate, ads, claim, lastro, prova, blocker, d4]
---

# Gate — Lastro de Claim em Ads

## Propósito
Este gate prova que **nenhum gancho ou corpo de ad promete o que a oferta não entrega sem prova**. Ele existe porque atenção sem verdade queima o pixel, atrai o veto do compliance e destrói a confiança que o funil precisa converter. Vale o princípio `evidence_before_opinion`: toda promessa de resultado, prazo ou número aponta para um `proof_id` real. Este é um gate de **bloqueio**: um ad com claim órfão **não vai ao ar** — o ângulo fica marcado `pendente_de_prova` até o lastro chegar. O `ad-creative-factory` não fabrica prova; ele bloqueia o ângulo e aciona o curador. É o espelho, em D4, do veto de claim que o `compliance-auditor` aplica na barreira final.

## Dono & Escopo
- **owner_agent:** `ad-creative-factory` (verifica o lastro antes de emitir; bloqueia o que não tem). O `compliance-auditor` detém o **veto** final de claim sem lastro na auditoria; o `proof-credibility-curator` fornece a prova.
- **Artefato inspecionado:** os claims de cada peça da `ad-matrix` no [`control-registry`](../../data/registries/control-registry.md), cruzados com o [`claim-registry`](../../data/registries/claim-registry.md) e o [`proof-registry`](../../data/registries/proof-registry.md) via [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md).

## Condição de Passagem
Todo claim de resultado, prazo ou número em qualquer ad tem um `proof_id` correspondente no proof-registry, e nenhum ad com claim órfão está liberado para ir ao ar.

## Itens
1. **Claims extraídos.** Verificar: cada ad lista seus `claim_refs[]` no `control-registry` — promessa, número, prazo, comparação.
2. **Cadeia claim→prova.** Verificar: cada `claim_id` tem `proof_id` no `proof-registry`, sem órfão (`proof-to-claim-chain`).
3. **Promessa de prazo verificável.** Verificar: nenhum gancho promete prazo/resultado infalsificável ("destrave em 7 dias garantido" sem evidência → reescrito).
4. **Comparação sustentada.** Verificar: todo "melhor que / mais rápido que" tem base; sem base, vira afirmação verificável.
5. **Garantia honesta.** Verificar: a garantia citada no ad bate com a do `offer-book`, sem inflar termos.
6. **Bloqueio do órfão.** Verificar: todo ad sem lastro está marcado `pendente_de_prova` e **fora do ar**, com flag ao `proof-credibility-curator`.
7. **Pré-auditoria de compliance.** Verificar: nenhum ad carrega escassez falsa ou promessa de cura/ganho garantido que o `compliance-auditor` vetaria.

## Evidência Exigida
Para marcar ✅: linkar a tabela claim→proof sem órfãos do `claim-registry`/`proof-registry` (itens 1–2), as reescritas de promessas infalsificáveis (itens 3–4), a paridade de garantia com o `offer-book` (item 5) e a lista de ângulos `pendente_de_prova` bloqueados (item 6).

## Protocolo de Falha
Claim órfão → o ad é **bloqueado** (não vai ao ar), marcado `pendente_de_prova`, e a lacuna é encaminhada ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). O `ad-creative-factory` substitui por uma promessa verificável até a prova chegar. O **veto** definitivo de claim sem lastro pertence ao [`compliance-auditor`](../../agents/compliance-auditor.md) na barreira final, espelhado aqui em [`compliance/compliance-claim-backing-gate`](../compliance/compliance-claim-backing-gate.md); **override** só com decisão humana explícita gravada no `decision-registry`, nunca por pressa. Re-entrada: anexar o `proof_id`, atualizar os registries e re-submeter.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`lead-types`](../../lib/taxonomies/lead-types.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md)
- Agentes: [`ad-creative-factory`](../../agents/ad-creative-factory.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Espelho de compliance: [`compliance/compliance-claim-backing-gate`](../compliance/compliance-claim-backing-gate.md)
- Gates irmãos: [`ads-angle-coverage-gate`](ads-angle-coverage-gate.md) · [`ads-hook-strength-gate`](ads-hook-strength-gate.md) · [`ads-variation-gate`](ads-variation-gate.md) · [`ads-test-hypothesis-gate`](ads-test-hypothesis-gate.md)
