---
id: project.full-launch-blackbook-project.09-events-logistics
title: "Fase 09 — Eventos & Logística"
type: project-phase
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
tags: [project-phase, ops, eventos, logistica, calendario, inventario, fulfillment, d6]
---

# Fase 09 — Eventos & Logística

## Objetivo da Fase
Operacionalizar cada evento e cada entrega do lançamento: o calendário de eventos (datas, salas, plataformas, ensaios, donos, fallbacks), o asset/inventory tracker (cada ativo, bônus e vaga com status e quantidade) e o plano de fulfillment/redemption (como cada oferta é entregue e resgatada). O estado-pronto é nenhum evento sem logística confirmada, nenhuma oferta vendida sem caminho de entrega, e cada limite de escassez batendo com um número real no tracker — aprovado no events-logistics-checklist. É aqui que a escassez deixa de ser texto e passa a ter lastro físico: "últimas 50 vagas" só existe se houver 50 no tracker.

## Critério de Entrada
A Fase 08 entrega o `artifact.run-of-show` aprovado (datas, horários, donos, fallbacks) e as `artifact.launch-phases` (o que cada fase exige de evento e entrega). A Fase 01 entrega o `artifact.money-model` (cada degrau e seu objeto de entrega) e o `artifact.offer-book` (bônus prometidos, garantias que exigem caminho de reembolso, limites de escassez a rastrear). A Fase 06 entrega o `artifact.funnel-map` (onde cada oferta é vendida e, portanto, onde a entrega precisa estar plugada). Pré-condição: o run-of-show está aprovado e o money model presente — sem saber quais ofertas existem na sequência, não há o que entregar. Oferta sem caminho de entrega não é marcada pronta e volta ao money-model-designer. O [`offer-registry`](../../data/registries/offer-registry.md) é escrito.

## Agentes & Tasks
- **Task [`build-events-logistics`](../../tasks/ops/build-events-logistics.md)** — dono [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md). O quartel-mestre: calendariza, rastreia inventário e garante a entrega. Sem poder de veto, mas recusa declarar pronto o que não fecha.

## Passos
1. Confirme as pré-condições: run-of-show aprovado, money model presente, lista de bônus/limites do Offer Book.
2. Construa o calendário de eventos: para cada evento, plataforma/sala, link canônico, ensaio técnico no dia anterior, dono e fallback (transmissão reserva + gravação de emergência).
3. Monte o asset/inventory tracker: cada ativo, bônus e vaga com tipo, quantidade e status. Vaga limitada registra o número real e cria o gatilho de "esgotado" no limite.
4. Desenhe o fulfillment/redemption com Tree-of-Thoughts (≥3 modelos — automático, agendado, concierge — pontuados por confiabilidade sob volume, carga, experiência e rastreabilidade).
5. Ordene a entrega pela escada com [`money-model-sequence`](../../frameworks/money-model-sequence.md): o acesso ao core pronto antes do upsell ser oferecido.
6. Ancore a escassez no inventário com Tree-of-Thoughts (≥3 mecânicas todas verdadeiras); descarte qualquer mecânica que não se consiga provar no tracker.
7. Plugue a entrega ao funil: confirme que a página de obrigado/área de membros/e-mail de acesso libera cada oferta no ponto certo.
8. Self-verify com red-team (toda oferta com fulfillment? todo evento com sala/link/ensaio/fallback? todo limite batendo com número real?); atualize o `offer-registry` (ofertas active com caminho de entrega e limite).

## Artefatos Produzidos
- `artifact.events-calendar` — cada evento com data/hora, plataforma, ensaio, dono e fallback.
- `artifact.asset-inventory-tracker` — cada item com tipo, quantidade, status e modelo de fulfillment.
- `artifact.fulfillment-plan` — por oferta: entrega, resgate do bônus, ponto no funil.
- Registry escrito: [`offer-registry`](../../data/registries/offer-registry.md).

## Gates
- [`events-logistics-checklist`](../../checklists/events-logistics-checklist.md)

## Critério de Saída
O run-of-show aprovado e o money model presente foram confirmados; cada evento tem sala/plataforma, link canônico, ensaio e fallback; cada oferta do money model tem caminho de fulfillment plugado no funil; a ordem de entrega respeita a escada; todo limite de escassez bate com um número real no tracker (zero limite sem lastro); o events-logistics-checklist está verde e as ofertas estão registradas como active. A próxima fase é a [`10-affiliate-program`](10-affiliate-program.md), que recebe o calendário e o inventário para recrutar e armar o exército de afiliados.
