---
id: checklist.avatar.avatar-dmu-gate
title: "Gate — DMU/Comitê de Compra Mapeado por Papel em B2B (medo e critério de cada decisor)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
frameworks: [avatar-voc-investigator/dmu-mapping-b2b, avatar-voc-investigator/objection-belief-mapping]
registries: [objection-registry]
tags: [gate, avatar, dmu, b2b, d1, comite-de-compra, bloqueador]
---

# Gate — DMU/Comitê de Compra Mapeado por Papel

## Propósito
Este gate prova que, em B2B, o `avatar-voc-investigator` mapeou a **DMU** (Decision-Making Unit / comitê de compra) papel a papel, em vez de tratar a venda complexa como se fosse uma pessoa só. Existe porque numa conta corporativa o "cliente" é um comitê: o CFO teme gastar sem ROI, o jurídico teme cláusula mal resolvida, o técnico teme mais um sistema para manter, e qualquer um deles pode ser um **bloqueador**. Mapear só o usuário deixa um decisor sem resposta — e um único bloqueador derruba o negócio. A prova precisa ser **roteada por papel** (ROI para o CFO, compliance para o risco), e este gate garante que cada papel, com seu medo e seu critério, está no mapa. Em B2C puro, o gate é marcado **não-aplicável** com justificativa.

## Dono & Escopo
- **owner_agent:** `avatar-voc-investigator` (aplica [`dmu-mapping-b2b`](../../frameworks/avatar-voc-investigator/dmu-mapping-b2b.md) quando o escopo é B2B).
- **Artefato inspecionado:** o **mapa da DMU** do ICP da conta (papéis, medo, objeção e critério de cada decisor), com as objeções no [`objection-registry`](../../data/registries/objection-registry.md).

## Condição de Passagem
Em B2B, cada papel do comitê de compra está mapeado com seu medo, sua objeção e o que precisa ouvir; em B2C, o gate está marcado não-aplicável com justificativa.

## Itens
1. **Aplicabilidade declarada.** Verificar: o brief diz se o caso é B2B (gate ativo) ou B2C (não-aplicável com justificativa).
2. **Papéis cobertos.** Verificar: o mapa cobre os papéis relevantes — comprador econômico, técnico, usuário, influenciador e **bloqueador** — sem deixar nenhum decisor de fora.
3. **Medo por papel.** Verificar: cada papel tem o medo nomeado (CFO = gastar sem ver ROI; risco = auditoria/multa; técnico = mais sistema para manter).
4. **Objeção por papel.** Verificar: cada papel tem a objeção categorizada (`price`, `risk`, `belief-mechanism`, `trust`...).
5. **O que precisa ouvir.** Verificar: cada papel tem nomeado o que o convence (payback para o CFO, prova de conformidade para o risco).
6. **Bloqueador avaliado.** Verificar: se há um bloqueador (ex.: jurídico) com objeção que nenhuma prova atual resolve, isso está sinalizado.
7. **Verbatims segmentados por papel.** Verificar: há verbatims do conjunto atribuídos por papel ("preciso justificar isso pro board" = CFO), não uma voz única.

## Evidência Exigida
Para marcar cada item ✅, linkar o mapa da DMU com a tabela papel → medo → objeção → critério e os verbatims segmentados por papel. As objeções de cada papel são registradas no [`objection-registry`](../../data/registries/objection-registry.md) com a categoria correspondente. O roteamento da prova por papel linka o handoff ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). Em B2C, a justificativa de "não-aplicável" conta como evidência. O permalink do mapa conta como evidência.

## Protocolo de Falha
Item vermelho → o `avatar-voc-investigator` reconstrói a DMU papel a papel, com o medo e o critério de cada decisor, e roteia a prova por papel. B2B tratado como B2C (só o usuário mapeado) → reabre e completa o comitê. Bloqueador intransponível (papel com objeção que nenhuma prova resolve) → o agente **sinaliza ao `offerbook-chief`** o risco de inviabilidade. Re-entrada: completado o mapa por papel, o gate é re-submetido. O agente não tem veto; a decisão sobre um bloqueador fatal é do comando.

## Links
- Frameworks: [`dmu-mapping-b2b`](../../frameworks/avatar-voc-investigator/dmu-mapping-b2b.md) · [`objection-belief-mapping`](../../frameworks/avatar-voc-investigator/objection-belief-mapping.md)
- Registries: [`objection-registry`](../../data/registries/objection-registry.md)
- Agentes: [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md)
- Gate de objeções (par): [`avatar-objection-map-gate`](avatar-objection-map-gate.md)
- Escopo (B2B detectado): [`chief-project-type-gate`](../chief/chief-project-type-gate.md)
