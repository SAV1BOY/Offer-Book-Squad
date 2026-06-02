---
id: checklist.proof.proof-objection-coverage-gate
title: "Gate — Toda Objeção de Alta Severidade Desarmada pela Prova Certa"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
frameworks: [proof-to-claim-chain]
registries: [proof-registry, objection-registry]
tags: [gate, proof, objection-coverage, d1, dmu, severidade, emocao]
---

# Gate — Toda Objeção de Alta Severidade Desarmada pela Prova Certa

## Propósito
Este gate prova que **cada objeção que o comprador levantará** — sobretudo as de alta severidade — tem prova que a desarma, e que essa prova **ressoa com a emoção dominante** do avatar. Ele existe porque a prova certa não é a tecnicamente mais forte, mas a que fala com o medo certo: uma objeção `belief-self` ("a culpa é minha") pede um caso-espelho de alguém igual ao avatar, não uma estatística agregada. Ele complementa o `proof-coverage-gate` (que olha os claims) cobrindo o **outro lado da corrente**: as objeções e falsas crenças herdadas do `avatar-voc-investigator`. Em B2B, a cobertura é **roteada por papel da DMU** — o CFO quer ROI, o risco quer compliance, o TI quer mecanismo. Sem este gate, uma objeção fatal pode passar sem desarme e derrubar a conversão na hora da decisão. É o gate que garante que toda dúvida que mata a venda já tem uma resposta provada e ressonante esperando por ela.

## Dono & Escopo
- **owner_agent:** `proof-credibility-curator` (cura prova contra as objeções, não no vácuo; sem veto, sinaliza).
- **Artefato inspecionado:** a **matriz prova × objeção** (em B2B, por papel da DMU), com as objeções no [`objection-registry`](../../data/registries/objection-registry.md) e as provas no [`proof-registry`](../../data/registries/proof-registry.md).

## Condição de Passagem
Cada objeção de alta severidade tem prova que a desarma, a prova ressoa com a emoção dominante, e em B2B a cobertura está roteada por papel da DMU.

## Itens
1. **Objeções de alta severidade cobertas.** Verificar: cada objeção `high` do [`objection-registry`](../../data/registries/objection-registry.md) tem uma prova principal que a desarma — nenhuma objeção fatal sem resposta.
2. **Prova ressoa com a emoção dominante.** Verificar: a munição principal de cada objeção fala com o medo/desejo dominante do avatar (caso-espelho para `belief-self`, ROI para `price`).
3. **Tipo de prova casa com a falsa crença.** Verificar: aplicado [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md), o tipo de prova corresponde à crença a derrubar (mecanismo para `belief-mechanism`, identidade para `belief-self`).
4. **Cobertura por papel da DMU (B2B).** Verificar: em venda a comitê, cada papel (CFO, risco, TI, jurídico) tem a prova que desarma a objeção dele; cobertura segmentada, não única.
5. **Objeções de média severidade endereçadas.** Verificar: objeções `med` têm ao menos uma prova ou um plano de resposta, mesmo que não-principal.
6. **Objeções sem desarme sinalizadas.** Verificar: toda objeção de alta severidade que nenhuma prova atual vence está no proof-gap-report como bloqueio sinalizado.
7. **Cobertura cruzada com o mapa.** Verificar: a matriz cobre o mapa de objeções entregue pelo avatar (via [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md)), sem objeção do mapa fora dela.

## Evidência Exigida
Para marcar cada item ✅, linkar a matriz prova × objeção (cada objeção com sua prova principal e severidade), o [`objection-registry`](../../data/registries/objection-registry.md) (objeções, falsas crenças, severidade) cruzado contra a matriz, e — em B2B — o agrupamento por papel da DMU. O proof-gap-report listando objeções fatais sem desarme é a evidência-resumo do risco residual de conversão.

## Protocolo de Falha
Item vermelho → não declara verde. Objeção fatal sem prova → abre proof-gap de alta severidade e **bloqueio sinalizado**; não deixa a copy enfrentar a objeção sem munição. Prova que ignora a emoção dominante (forte mas fria) → reordena a matriz para que a munição principal ressoe com o medo certo. Tipo de prova errado para a crença → troca por prova do tipo correto (mecanismo vs identidade). Cobertura B2B não-segmentada → roteia por papel da DMU. Mapa de objeções incompleto → cobre o que dá e sinaliza ao [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md). O curador **não tem veto**: sinaliza ao [`offerbook-chief`](../../agents/offerbook-chief.md) e ao [`compliance-auditor`](../../agents/compliance-auditor.md). Re-entrada: desarmada a objeção, o gate é re-submetido.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`proof-registry`](../../data/registries/proof-registry.md) · [`objection-registry`](../../data/registries/objection-registry.md)
- Agentes: [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gate de entrada (montante): [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md)
- Gates irmãos: [`proof-claim-backing-gate`](proof-claim-backing-gate.md) · [`proof-coverage-gate`](proof-coverage-gate.md) · [`proof-source-credibility-gate`](proof-source-credibility-gate.md) · [`proof-permission-gate`](proof-permission-gate.md)
