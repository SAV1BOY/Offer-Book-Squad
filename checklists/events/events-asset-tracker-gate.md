---
id: checklist.events.events-asset-tracker-gate
title: "Gate — Asset & Inventory Tracker (cada ativo e cada vaga com status e número real)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: events-logistics-coordinator
frameworks: [money-model-sequence, launch/runway-and-phases]
registries: [offer-registry]
tags: [gate, eventos, inventario, ativos, escassez-real, vagas, d6]
---

# Gate — Asset & Inventory Tracker

## Propósito
Este gate prova que **cada ativo, bônus e vaga tem status conhecido e que todo limite de escassez bate com um número real no tracker**. Ele existe porque a escassez falsa é veto: se a oferta diz "100 vagas" ou "últimas 50", o tracker tem que provar que são 100 ou 50 de verdade. O `events-logistics-coordinator` monta o inventory tracker com cada item — core, bônus, vaga, ativo de prova — e sua quantidade, status (disponível/N restantes/esgotado) e gatilho de esgotado. Vale o princípio `truthful_scarcity`: escassez inventada não tem override. Quando a oferta promete um limite, o coordenador gera mecânicas **todas verdadeiras** (vagas fixas, lotes por data, capacidade de atendimento) e descarta qualquer uma que não consiga provar no tracker. A escassez ancorada em capacidade real (ex.: 10 mentorados = capacidade do mentor) é honesta; a inventada vai ao veto do compliance. Este gate julga **só o inventário e a veracidade do limite** — a operação do evento é do `events-calendar-gate`, e como o item é entregue é do `events-fulfillment-gate`. Um "últimas N vagas" sem N real trava aqui.

## Dono & Escopo
- **owner_agent:** `events-logistics-coordinator` (rastreia cada ativo e ancora a escassez no número real).
- **Artefato inspecionado:** o `asset-inventory-tracker`, cruzado com os limites prometidos no `offer-book` (vagas, lotes) e o `money-model`. O status de cada oferta é confirmado no [`offer-registry`](../../data/registries/offer-registry.md). O tracker é entregue ao [`compliance-auditor`](../../agents/compliance-auditor.md) para auditoria de escassez.

## Condição de Passagem
Cada ativo, bônus e vaga tem quantidade e status no tracker, e todo limite de escassez prometido bate com um número real e verificável.

## Itens
1. **Cada ativo listado.** Verificar: core, bônus, vagas e ativos de prova estão no tracker com tipo e quantidade.
2. **Status conhecido.** Verificar: cada item tem status (disponível / N restantes / esgotado).
3. **Limite = número real.** Verificar: todo "N vagas" ou "últimas N" prometido bate com N de verdade no tracker.
4. **Gatilho de esgotado.** Verificar: há gatilho que marca "esgotado" ao atingir o limite real (ex.: aos 200).
5. **Mecânica verdadeira.** Verificar: a mecânica de escassez (vagas fixas/lotes/capacidade) é provável no tracker.
6. **Ancorada em capacidade.** Verificar: limites de atendimento batem com a capacidade real (ex.: 10 vagas = capacidade do mentor).

## Evidência Exigida
Para marcar ✅: linkar o `asset-inventory-tracker` com, por item, `{tipo, quantidade, status}`, mais a prova de que cada limite prometido = número real (ex.: "200 vagas" = 200 no tracker ✓). O status `active` de cada oferta no [`offer-registry`](../../data/registries/offer-registry.md) e os limites do `offer-book` que embasaram o tracker ficam citados.

## Protocolo de Falha
Item vermelho → o `events-logistics-coordinator` **trava no inventory tracker**: só publica limite que bate com a capacidade real. "Últimas N vagas" sem N real ele corrige antes e **sinaliza** ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto de escassez falsa — escassez de inventário tem que bater com a realidade. O coordenador **não tem veto**, mas recusa declarar pronto um limite sem lastro. Bônus prometido que não existe ainda volta ao [`money-model-designer`](../../agents/money-model-designer.md) para criar o ativo. A operação do evento é do [`events-calendar-gate`](events-calendar-gate.md). Re-entrada: ancorar cada limite num número real, corrigir o tracker e re-submeter ao compliance.

## Links
- Frameworks: [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) · [`compliance-auditor`](../../agents/compliance-auditor.md) · [`money-model-designer`](../../agents/money-model-designer.md)
- Gates irmãos: [`events-calendar-gate`](events-calendar-gate.md) · [`events-fulfillment-gate`](events-fulfillment-gate.md) · [`events-redemption-gate`](events-redemption-gate.md) · [`events-owner-hosting-gate`](events-owner-hosting-gate.md)
