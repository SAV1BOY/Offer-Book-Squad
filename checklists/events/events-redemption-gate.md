---
id: checklist.events.events-redemption-gate
title: "Gate — Redemption (cada bônus e garantia tem como ser resgatado e rastreado)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: events-logistics-coordinator
frameworks: [money-model-sequence, launch/runway-and-phases]
registries: [offer-registry]
tags: [gate, eventos, redemption, resgate, bonus, garantia, d6]
---

# Gate — Redemption

## Propósito
Este gate prova que **cada bônus prometido tem como ser resgatado, cada garantia tem caminho de reembolso e o resgate é rastreável**. Ele existe porque um bônus que o cliente não consegue resgatar é uma promessa quebrada, e uma garantia sem caminho de reembolso vira reclamação e estorno. O `events-logistics-coordinator` define, para cada bônus, como o cliente o resgata (link, convite, agendamento) e, para cada garantia, o caminho de devolução. Ele garante que dá para saber quem recebeu e quem resgatou — rastreabilidade do resgate. Vale o princípio `traceability_before_eloquence`: cada entrega tem status conhecido. Este gate é o par do `events-fulfillment-gate`: o fulfillment desenha **como a oferta chega**, este desenha **como o cliente aciona o bônus e a garantia**. Para high-ticket, o resgate concierge (1:1) é rastreado call a call; para baixo-ticket, o resgate automático libera na hora. A garantia exige um caminho de reembolso honesto — sem isso, o risk-reversal prometido no offer-book não se sustenta. Este gate julga **só o resgate e o reembolso** — o número de vagas é do `events-asset-tracker-gate`, e o caminho de entrega da oferta é do `events-fulfillment-gate`.

## Dono & Escopo
- **owner_agent:** `events-logistics-coordinator` (define o resgate de cada bônus e o caminho de reembolso de cada garantia).
- **Artefato inspecionado:** a parte de redemption do `fulfillment-plan`, cruzada com os bônus e garantias do `offer-book`. O caminho de resgate de cada oferta fica anotado no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
Cada bônus tem caminho de resgate, cada garantia tem caminho de reembolso, e ambos são rastreáveis por cliente.

## Itens
1. **Resgate por bônus.** Verificar: cada bônus prometido tem como ser resgatado (link, convite, agendamento).
2. **Reembolso da garantia.** Verificar: cada garantia do offer-book tem caminho de devolução definido.
3. **Resgate rastreável.** Verificar: dá para saber quem recebeu e quem resgatou cada bônus.
4. **Resgate na ordem certa.** Verificar: o resgate fica disponível quando o cliente tem direito (após a compra/acesso).
5. **Concierge rastreado.** Verificar: resgates 1:1 (high-ticket) têm cada call/slot registrado.
6. **Garantia honesta.** Verificar: o caminho de reembolso cumpre o risk-reversal prometido, sem fricção indevida.

## Evidência Exigida
Para marcar ✅: linkar o `fulfillment-plan` na parte de redemption com, por item, `{redemption: como o bônus é resgatado, reembolso: caminho da garantia}`, mais a evidência de rastreabilidade (quem resgatou). Os bônus e garantias do `offer-book` e o caminho anotado no [`offer-registry`](../../data/registries/offer-registry.md) ficam citados.

## Protocolo de Falha
Item vermelho → o `events-logistics-coordinator` **não declara a oferta pronta** até o bônus ter resgate e a garantia ter caminho de reembolso. Bônus que não existe ainda volta ao [`money-model-designer`](../../agents/money-model-designer.md) para criar o ativo. Garantia sem caminho de reembolso honesto ele sinaliza, pois fere o risk-reversal prometido. O coordenador **não tem veto**, mas recusa declarar pronto o resgate que não fecha. Resgate que não pode ser rastreado ele corrige antes do dia. O caminho de entrega da oferta é do [`events-fulfillment-gate`](events-fulfillment-gate.md). Re-entrada: definir o resgate de cada bônus, o reembolso de cada garantia e atualizar o `offer-registry`.

## Links
- Frameworks: [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`events-calendar-gate`](events-calendar-gate.md) · [`events-asset-tracker-gate`](events-asset-tracker-gate.md) · [`events-fulfillment-gate`](events-fulfillment-gate.md) · [`events-owner-hosting-gate`](events-owner-hosting-gate.md)
