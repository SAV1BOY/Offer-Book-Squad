---
id: checklist.chief.chief-offer-book-readiness-gate
title: "Gate — Offer Book Pronto para Consolidação (chief co-assina o HARD STOP)"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [power-of-one, money-model-sequence, proof-to-claim-chain, offer-to-funnel-mapping]
registries: [offer-registry, big-idea-registry, decision-registry, claim-registry, proof-registry]
tags: [gate, chief, offer-book, readiness, d0, hard-stop, co-assinatura]
---

# Gate — Offer Book Pronto para Consolidação

## Propósito
Este gate é a verificação do `offerbook-chief` de que todos os insumos do Offer Book chegaram completos antes de ele co-assinar o HARD STOP do squad. Existe porque o chief é quem libera (ou recusa) a abertura de D4: ele não delega essa decisão. Enquanto o agregador [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) soma os gates de D1–D3, este gate é a checagem de comando — o chief confirma que recebeu mercado, avatar, prova, mecanismo, valor, money model, preço, unit econ, Big Idea e posicionamento, e que a oferta tem espinha. É o ponto onde a estratégia vira fundação travada.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (co-assina, junto do `compliance-auditor`, a liberação para a montagem do Offer Book).
- **Artefato inspecionado:** o **pacote de Offer Book** consolidado a partir de [`offer-registry`](../../data/registries/offer-registry.md), [`big-idea-registry`](../../data/registries/big-idea-registry.md), [`claim-registry`](../../data/registries/claim-registry.md) e [`proof-registry`](../../data/registries/proof-registry.md), via a task `assemble-offer-book`.

## Condição de Passagem
Todos os insumos estratégicos (D1–D3) chegaram completos ao chief, a oferta tem espinha de money model, e o chief confirma que pode co-assinar o HARD STOP.

## Itens
1. **Inteligência recebida.** Verificar: market-brief (sofisticação + consciência), avatar/ICP, banco de VOC e prova chegaram e estão linkados no [`offer-registry`](../../data/registries/offer-registry.md).
2. **Arquitetura recebida.** Verificar: mecanismo nomeado e provado, scorecard de valor sem alavanca órfã, money model, preço e unit econ presentes no registry.
3. **Big Idea travada.** Verificar: o [`big-idea-registry`](../../data/registries/big-idea-registry.md) contém exatamente UMA tese com status `locked`, conforme `power-of-one`.
4. **Espinha presente.** Verificar: o money model tem ≥2 partes sequenciadas (alvo 4), conforme `money_model_spine` do `config.yaml`.
5. **Sem claim órfão.** Verificar: cada `claim_id` no [`claim-registry`](../../data/registries/claim-registry.md) tem `proof_id` correspondente.
6. **Escopo ainda intacto.** Verificar: o entregável montado bate com a frase de escopo travada no [`chief-scope-approval-gate`](chief-scope-approval-gate.md), sem creep.
7. **Pronto para o agregador.** Verificar: o chief confirma que os três gates D1–D3 estão verdes para o [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) virar.

## Evidência Exigida
Para marcar cada item ✅, linkar as linhas dos registries (mercado/avatar/prova/mecanismo/valor/money model nos itens 1–2 e 4–5), a linha `locked` do [`big-idea-registry`](../../data/registries/big-idea-registry.md) (item 3), a frase de escopo do gate anterior (item 6) e o estado dos três gates D1–D3 (item 7). A co-assinatura `offerbook-chief` + `compliance-auditor` é gravada no [`decision-registry`](../../data/registries/decision-registry.md).

## Protocolo de Falha
Item vermelho → o chief **não co-assina** o HARD STOP e devolve ao agente dono do insumo faltante (mercado/avatar/prova/mecanismo/valor/money model/big-idea) com o defeito nomeado, conforme o roteamento do `config.yaml`. Sem espinha de money model → bloqueia até existirem ≥2 partes. Claim órfão → devolve ao `proof-credibility-curator`. Re-entrada: corrigido o insumo e atualizado o registry, o gate é re-submetido e, com tudo verde, o chief co-assina o [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md). Override só por decisão humana registrada.

## Links
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`big-idea-registry`](../../data/registries/big-idea-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`offerbook-chief`](../../agents/offerbook-chief.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- HARD STOP agregador: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
- Gate seguinte (memória): [`chief-blackbook-readiness-gate`](chief-blackbook-readiness-gate.md)
