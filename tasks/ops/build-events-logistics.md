---
id: task.ops.build-events-logistics
title: "Task — Construir o Calendário de Eventos & a Logística"
type: task
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: events-logistics-coordinator
consumes:
  - artifact.run-of-show
  - artifact.launch-phases
  - artifact.money-model
  - artifact.offer-book
  - artifact.funnel-map
produces:
  - artifact.events-calendar
  - artifact.asset-inventory-tracker
  - artifact.fulfillment-plan
frameworks: [money-model-sequence]
checklists:
  - events-logistics-checklist
registries: [offer-registry]
metrics: [compliance_pass_rate, upsell_take_rate, time_to_blackbook]
tags: [ops, eventos, logistica, calendario, inventario, fulfillment, redemption, d6]
---

# Task — Construir o calendário de eventos & a logística: nenhum evento sem sala, nenhuma oferta sem fulfillment

## Objetivo
Operacionalizar cada evento e cada entrega do lançamento: o **calendário de eventos** (datas, salas, plataformas, ensaios, donos, fallbacks), o **asset/inventory tracker** (cada ativo, bônus e vaga com status e quantidade) e o **plano de fulfillment/redemption** (como cada oferta é entregue e resgatada). O estado-pronto: nenhum evento sem logística confirmada, nenhuma oferta vendida sem caminho de entrega, e cada limite de escassez batendo com um número real no tracker — aprovado no events-logistics-checklist.

## Agente dono
[`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md). O quartel-mestre: calendariza, rastreia inventário e garante a entrega. Sem poder de veto, mas recusa declarar pronto o que não fecha.

## Gatilho / Quando
Roda em D6, **depois** do run-of-show: ativa quando o run-of-show do [`launch-producer`](../../agents/launch-producer.md) está aprovado e precisa virar operação concreta. Demais gatilhos: pedido de calendário + tracker + plano de fulfillment, ou mudança de data/capacidade/entrega que exige re-coordenação. **Sem money model não monta fulfillment** — sem saber quais ofertas existem na sequência, não há o que entregar. Oferta sem caminho de entrega → **não marcar como pronta** e devolver ao [`money-model-designer`](../../agents/money-model-designer.md).

## Inputs (Consome)
- `artifact.run-of-show` — as datas e horários de cada evento (webinar, live, call, abertura/fechamento), donos e fallbacks já definidos, a transformar em logística confirmada.
- `artifact.launch-phases` — as Fases I–VIII e o que cada uma exige de evento e de entrega.
- `artifact.money-model` — cada degrau da escada e o **objeto de entrega** (curso, acesso, bônus, comunidade, DFY).
- `artifact.offer-book` — os bônus prometidos, as garantias (que exigem caminho de reembolso), os **limites de escassez** (vagas, lotes) a rastrear, e os ativos de prova a exibir nos eventos.
- `artifact.funnel-map` — onde cada oferta é vendida e, portanto, onde a entrega/resgate precisa estar plugado (página de obrigado, área de membros, e-mail de acesso).

## Procedimento
1. **Confirmar as pré-condições.** Run-of-show aprovado; money model presente; lista de bônus/limites do Offer Book. Sem isso, parar.
2. **Construir o calendário de eventos.** Para cada evento do run-of-show: plataforma/sala, link canônico (do tech-plan via run-of-show), ensaio técnico no dia anterior, dono e **fallback** (transmissão reserva + gravação de emergência).
3. **Montar o asset/inventory tracker.** Cada ativo, bônus e vaga com tipo, quantidade e status. Vaga limitada → registrar o número real e criar o gatilho de "esgotado" no limite (escassez real, não inventada).
4. **Desenhar o fulfillment/redemption (ToT).** Para cada oferta/bônus, gerar ≥3 modelos de entrega — automático, agendado, concierge — e pontuar por confiabilidade sob volume, carga operacional, experiência percebida e rastreabilidade. Baixo-ticket tende a automático; high-ticket a concierge.
5. **Ordenar a entrega pela escada.** Aplicar [`money-model-sequence`](../../frameworks/money-model-sequence.md): o acesso ao core pronto **antes** de o upsell ser oferecido (o cliente não compra upgrade de algo que ainda não recebeu); o upsell entrega logo após a compra.
6. **Ancorar a escassez no inventário (ToT).** Gerar ≥3 mecânicas **todas verdadeiras** (vagas fixas, lotes por data, capacidade de atendimento) e pontuar por veracidade verificável, clareza e sustentabilidade. **Descartar qualquer mecânica que não se consiga provar no tracker** — escassez que não bate com o inventário é falsa.
7. **Plugar a entrega ao funil.** Confirmar que a página de obrigado/área de membros/e-mail de acesso libera cada oferta no ponto certo.
8. **Self-verify (Bloom + red-team).** **Toda** oferta tem caminho de fulfillment? **Todo** evento tem sala/link/ensaio/fallback? **Todo** limite prometido bate com um número real no tracker? Antecipar o veto de escassez falsa do [`compliance-auditor`](../../agents/compliance-auditor.md) ("últimas 50 vagas" sem 50 no tracker) e corrigir antes.
9. **Registrar e entregar.** Atualizar o `offer-registry` (cada oferta `active` quando a entrega está pronta, com o caminho de fulfillment e o limite). Decisões de modelo de fulfillment/escassez vão ao decision-registry via chief; lições logísticas ao [`knowledge-librarian`](../../agents/knowledge-librarian.md). Máximo de 2 ciclos antes de escalar.

## Frameworks
[`money-model-sequence`](../../frameworks/money-model-sequence.md) · (herdado) [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md) via o run-of-show.

## Outputs (Produz)
- `artifact.events-calendar` (template em [`ops/events-calendar-template`](../../templates/ops/events-calendar-template.md)) — cada evento com data/hora, plataforma, ensaio, dono e fallback.
- `artifact.asset-inventory-tracker` (template em [`ops/asset-inventory-tracker-template`](../../templates/ops/asset-inventory-tracker-template.md)) — cada item com tipo, quantidade, status e modelo de fulfillment.
- `artifact.fulfillment-plan` — por oferta: entrega, resgate do bônus, ponto no funil.
- [`offer-registry`](../../data/registries/offer-registry.md) atualizado (`offer_id`, fulfillment, delivery_point, inventory_limit, inventory_status, redemption, event_ref).

## Definition of Done
- Run-of-show aprovado e money model presente confirmados antes de operacionalizar.
- Cada evento com sala/plataforma, link canônico, ensaio e **fallback**.
- Cada oferta do money model com caminho de fulfillment plugado no funil; ordem de entrega respeita a escada.
- **Todo** limite de escassez bate com um número real no inventory tracker (zero limite sem lastro).
- O events-logistics-checklist verde; ofertas registradas como `active` no `offer-registry` com caminho de entrega.

## Gates
[`events-logistics-checklist`](../../checklists/events-logistics-checklist.md).

## Métricas
Move KPIs de **operational**, **conversion** e **efficiency** ([`config.yaml`](../../config.yaml) `kpis:`), por operacionalizar eventos e entrega sem furos:
- **`compliance_pass_rate`** — ancorar **todo** limite de escassez a um número real no inventory tracker é o que sustenta a escassez no veto do `compliance-auditor` ("últimas 50 vagas" só com 50 no tracker).
- **`upsell_take_rate`** — entregar o core **antes** de oferecer o upsell (ordem da escada) é pré-condição para a take rate do upsell acontecer.
- **`time_to_blackbook`** — logística confirmada e fulfillment plugado evitam o retrabalho que atrasa o Blackbook.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md), com ofertas `active` e limites em [`offer-registry`](../../data/registries/offer-registry.md).

## Handoff
**Próximas tasks:** [`build-affiliate-program`](../growth/build-affiliate-program.md) — recebe o calendário de eventos onde afiliados podem participar e o inventário disponível para promoções; [`build-pr-plan`](../growth/build-pr-plan.md) — recebe os eventos que geram pauta de PR. Também entrega ao [`compliance-auditor`](../qa-memory/compliance-audit.md) o inventory tracker para auditoria de escassez real e ao [`knowledge-librarian`](../../agents/knowledge-librarian.md) o que vira memória. **Garantia:** um calendário com logística confirmada, um tracker onde cada limite é um número real, e um plano de fulfillment onde cada oferta vendida tem como ser entregue e resgatada.
