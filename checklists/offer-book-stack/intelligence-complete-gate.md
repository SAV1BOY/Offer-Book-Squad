---
id: checklist.offer-book-stack.intelligence-complete-gate
title: "Gate — Inteligência Completa (Mercado + Avatar + Prova)"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [awareness-x-sophistication, starving-crowd, proof-to-claim-chain]
registries: [offer-registry, objection-registry, proof-registry, claim-registry]
tags: [gate, intelligence, market, avatar, voc, proof, d1, dod-input]
---

# Gate — Inteligência Completa

## Propósito
Este gate prova que a **fundação de inteligência (D1)** está pronta antes de qualquer desenho de oferta. Ele existe porque, no princípio Agora, ~50–60% do trabalho é pesquisa antes da primeira palavra. Sem mercado diagnosticado, avatar pela voz real e prova mapeada, todo o resto vira suposição cara. Este gate é o primeiro dos três insumos que alimentam o [`offer-book-dod-gate`](offer-book-dod-gate.md): a estratégia só pode começar quando a inteligência fecha.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (libera a transição D1→D2).
- **Artefato inspecionado:** o pacote de inteligência produzido por `market-sophistication-analyst`, `avatar-voc-investigator` e `proof-credibility-curator` — gravado em [`offer-registry`](../../data/registries/offer-registry.md), [`objection-registry`](../../data/registries/objection-registry.md) e [`proof-registry`](../../data/registries/proof-registry.md).

## Condição de Passagem
Mercado (sofisticação + consciência) está declarado, o avatar está descrito pela voz real do cliente, e cada claim tem prova mapeada.

## Itens
1. **Sofisticação declarada (1–5).** Verificar: campo de sofisticação preenchido no `offer-registry` com 1 frase de justificativa citando o concorrente de referência.
2. **Consciência declarada (1–5).** Verificar: nível de consciência (Schwartz) gravado, com a implicação para o lead.
3. **Starving crowd confirmada.** Verificar: dor/desejo + poder de compra + facilidade de alcance descritos em 3 bullets.
4. **≥10 verbatims de VOC.** Verificar: contar entradas literais com fonte (URL/contexto) no banco de VOC.
5. **Emoção dominante nomeada.** Verificar: uma emoção primária declarada e ligada a ≥3 verbatims.
6. **Mapa de objeções.** Verificar: cada objeção no `objection-registry` tem um contra-argumento e um ativo de prova candidato.
7. **Cadeia prova→claim sem órfãos.** Verificar: nenhum claim no `claim-registry` sem `proof_id` correspondente no `proof-registry`.

## Evidência Exigida
Para marcar cada item ✅, linkar: a linha do `offer-registry` (itens 1–3), o banco de VOC com contagem de verbatims (itens 4–5), e a tabela cruzada objeção→prova e claim→prova (itens 6–7). Print ou permalink da linha do registry conta como evidência.

## Protocolo de Falha
Item vermelho → o `offerbook-chief` devolve ao agente dono nomeado (mercado/avatar/prova) com o defeito específico e **não libera D2**. Re-entrada: o agente corrige, atualiza o registry e re-submete. Falta de dado de origem (ex.: sem acesso a VOC) escalona ao solicitante com perguntas objetivas, conforme `intake-and-scope`.

## Links
- Frameworks: [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`starving-crowd`](../../frameworks/starving-crowd.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`objection-registry`](../../data/registries/objection-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md)
- Agentes: [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Agrega para: [`offer-book-dod-gate`](offer-book-dod-gate.md)
