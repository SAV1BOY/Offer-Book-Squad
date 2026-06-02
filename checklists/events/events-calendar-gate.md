---
id: checklist.events.events-calendar-gate
title: "Gate — Calendário de Eventos (cada evento com data, sala, ensaio e fallback)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: events-logistics-coordinator
frameworks: [money-model-sequence, launch/runway-and-phases]
registries: [offer-registry]
tags: [gate, eventos, calendario, sala, ensaio, fallback, d6]
---

# Gate — Calendário de Eventos

## Propósito
Este gate prova que **cada evento do lançamento tem data, sala/plataforma, ensaio, dono e plano B definidos**. Ele existe porque webinar sem sala, live sem link ou call sem ensaio vira desastre ao vivo, na frente da audiência, sem segunda chance. O `events-logistics-coordinator` herda as datas e horários do run-of-show e adiciona a camada logística: plataforma confirmada, link canônico (do `tech-deliverability-plan`), ensaio técnico no dia anterior e fallback (transmissão reserva + gravação de emergência). A ordem dos eventos segue a sequência da escada via `money-model-sequence` e as Fases I–VIII via `runway-and-phases`. Vale o princípio `decision_before_ornament`: cada evento serve a um degrau do lançamento. Um evento sem fallback não está pronto — se a transmissão cai, a audiência some. Este gate julga **só a operação dos eventos** — o inventário de vagas é do `events-asset-tracker-gate`, e a entrega da oferta vendida é do `events-fulfillment-gate`. Evento agendado sem sala/plataforma viável escala ao `launch-producer`, dono do run-of-show.

## Dono & Escopo
- **owner_agent:** `events-logistics-coordinator` (transforma o run-of-show em logística confirmada de cada evento).
- **Artefato inspecionado:** o `events-calendar`, cruzado com o `run-of-show` (datas/horários/donos) e o `launch-phases`. As ofertas ligadas a eventos ficam no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
Cada evento do calendário tem data, sala/plataforma, link, ensaio, dono e plano B confirmados, na ordem da escada.

## Itens
1. **Data e horário.** Verificar: cada evento (webinar, live, call, abertura/fechamento) tem data e horário do run-of-show.
2. **Sala/plataforma.** Verificar: cada evento tem plataforma confirmada e link canônico definido.
3. **Ensaio agendado.** Verificar: há ensaio técnico antes de cada evento ao vivo (ex.: no dia anterior).
4. **Dono nomeado.** Verificar: cada evento tem um responsável que conduz e decide no dia.
5. **Fallback do evento.** Verificar: cada evento ao vivo tem plano B (transmissão reserva + gravação de emergência).
6. **Ordem da escada.** Verificar: a sequência dos eventos respeita a ordem do money model (atração antes do core).

## Evidência Exigida
Para marcar ✅: linkar o `events-calendar` com, por evento, `{data/hora, plataforma/sala, link, ensaio, dono, fallback}`, mais a confirmação da plataforma e do link canônico. As datas do run-of-show e a ordem da escada que embasaram o calendário ficam citadas.

## Protocolo de Falha
Item vermelho → o `events-logistics-coordinator` **não declara o calendário pronto** até cada evento ter sala, ensaio, dono e fallback. Evento agendado sem sala/plataforma/capacidade viável ele **escala** ao [`launch-producer`](../../agents/launch-producer.md), dono do run-of-show. Capacidade de evento estourada (mais inscritos que a sala) escala ao launch-producer e ao [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) para upgrade ou lista de espera real. O coordenador **não tem veto**, mas recusa declarar pronto o que não fecha. O inventário de vagas do evento é do [`events-asset-tracker-gate`](events-asset-tracker-gate.md). Re-entrada: definir sala/ensaio/dono/fallback de cada evento e re-submeter o calendário.

## Links
- Frameworks: [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) · [`launch-producer`](../../agents/launch-producer.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md)
- Gates irmãos: [`events-asset-tracker-gate`](events-asset-tracker-gate.md) · [`events-fulfillment-gate`](events-fulfillment-gate.md) · [`events-redemption-gate`](events-redemption-gate.md) · [`events-owner-hosting-gate`](events-owner-hosting-gate.md)
