---
id: checklist.events.events-owner-hosting-gate
title: "Gate — Dono & Hosting (cada evento tem host confirmado e hospedagem técnica viável)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: events-logistics-coordinator
frameworks: [money-model-sequence, launch/runway-and-phases]
registries: [offer-registry]
tags: [gate, eventos, dono, host, hosting, plataforma, capacidade, d6]
---

# Gate — Dono & Hosting

## Propósito
Este gate prova que **cada evento tem um host confirmado e uma hospedagem técnica que aguenta o público esperado**. Ele existe porque um evento sem dono no comando trava no primeiro imprevisto, e uma plataforma que não suporta a audiência derruba a transmissão no pico. O `events-logistics-coordinator` confirma, para cada evento, quem apresenta e conduz (o host), quem opera a parte técnica, e que a plataforma/sala comporta o número de inscritos. A capacidade do evento herda do inventory tracker (quantos confirmaram) e do load test do `tech-links-deliverability-engineer` (a plataforma aguenta?). Vale o princípio `decision_before_ornament`: cada evento tem um responsável que decide ao vivo, não um vácuo de comando. Este gate é o complemento de papéis do `events-calendar-gate`: o calendário define data/sala/ensaio/fallback, este garante que há **gente no comando e plataforma viável**. Quando a sala não comporta o público (mais inscritos que capacidade), o coordenador escala ao launch-producer e ao tech para upgrade ou lista de espera real. Este gate julga **só o comando e a hospedagem** — a entrega da oferta vendida no evento é do `events-fulfillment-gate`.

## Dono & Escopo
- **owner_agent:** `events-logistics-coordinator` (confirma host, operador técnico e capacidade da plataforma por evento).
- **Artefato inspecionado:** o `events-calendar` na parte de donos/hosting, cruzado com o `run-of-show` (papéis), o `asset-inventory-tracker` (público confirmado) e a capacidade técnica do `tech-deliverability-plan`. As ofertas dos eventos ficam no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
Cada evento tem host confirmado, operador técnico e plataforma com capacidade para o público esperado.

## Itens
1. **Host confirmado.** Verificar: cada evento tem quem apresenta e conduz, nomeado e ciente.
2. **Operador técnico.** Verificar: cada evento ao vivo tem quem opera a transmissão e os controles.
3. **Capacidade da plataforma.** Verificar: a plataforma/sala comporta o número de inscritos confirmados.
4. **Backup de host.** Verificar: há quem assuma se o host principal cair (par do fallback do evento).
5. **Público vs capacidade.** Verificar: o público esperado (do tracker) não estoura a capacidade da plataforma.
6. **Hosting alinhado ao tech.** Verificar: a capacidade técnica foi confirmada com o `tech-links-deliverability-engineer`.

## Evidência Exigida
Para marcar ✅: linkar o `events-calendar` mostrando, por evento, `{host, operador técnico, capacidade da plataforma}`, mais a confirmação de capacidade cruzada com o público do `asset-inventory-tracker` e o `tech-deliverability-plan`. Os papéis do `run-of-show` que embasaram os donos ficam citados.

## Protocolo de Falha
Item vermelho → o `events-logistics-coordinator` **não declara o evento pronto** até ter host, operador e plataforma com capacidade. Evento sem sala/plataforma/capacidade viável ele **escala** ao [`launch-producer`](../../agents/launch-producer.md), dono do run-of-show. Capacidade de plataforma estourada (mais inscritos que a sala comporta) escala ao launch-producer e ao [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) para upgrade ou lista de espera real. O coordenador **não tem veto**, mas recusa declarar pronto o evento sem comando ou sem hospedagem viável. A operação geral do calendário é do [`events-calendar-gate`](events-calendar-gate.md). Re-entrada: confirmar host, operador e capacidade, e re-submeter o evento.

## Links
- Frameworks: [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) · [`launch-producer`](../../agents/launch-producer.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md)
- Gates irmãos: [`events-calendar-gate`](events-calendar-gate.md) · [`events-asset-tracker-gate`](events-asset-tracker-gate.md) · [`events-fulfillment-gate`](events-fulfillment-gate.md) · [`events-redemption-gate`](events-redemption-gate.md)
