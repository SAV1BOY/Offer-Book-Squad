---
id: project.single-promo-project.04-funnel-and-links
title: "Fase 04 — Funil & Links"
type: project-phase
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
consumes:
  - artifact.offer-book-master
  - artifact.vsl-script
  - artifact.email-sequence
produces:
  - artifact.funnel-map
  - artifact.page-specs
  - artifact.links-urls
  - artifact.tech-deliverability-plan
tags: [project-phase, single-promo, funnel, tech, links, deliverability, d5]
---

# Fase 04 — Funil & Links

## Objetivo da Fase
Montar o funil que entrega a oferta sem nenhum beco sem saída e armar os links e a entregabilidade que fazem tudo funcionar no dia. Na promo enxuta, o funil é curto: captura ou página de oferta, checkout, um upsell ou order bump se o money model pedir, e a página de obrigado. Cada página tem um próximo passo. O estado-pronto é o mapa do funil sem dead-end, as specs de cada página, a planilha de URLs com todos os links rastreáveis e o plano de tech/entregabilidade que garante e-mail na caixa de entrada e checkout no ar sob carga. O funil reflete o money model: se há upsell, ele aparece; se há continuidade, o checkout a oferece. Nada de página solta sem destino.

## Critério de Entrada
A [`02-vsl-or-sales-letter`](02-vsl-or-sales-letter.md) entrega a peça-âncora e a copy da página de oferta; a [`03-email-sequence`](03-email-sequence.md) entrega a sequência com seus CTAs; a [`01-offer-book-core`](01-offer-book-core.md) entrega o money model. Pré-condição: a copy das páginas existe (não se monta funil sem destino) e o money model define os degraus. Se há um upsell no money model sem copy correspondente, a fase sinaliza a lacuna. O [`decision-registry`](../../data/registries/decision-registry.md) é lido para alinhar com a topologia do pipeline.

## Agentes & Tasks
- **Task [`map-funnel`](../../tasks/funnel-tech/map-funnel.md)** — dono [`funnel-architect`](../../agents/funnel-architect.md). Desenha o funil e as specs de página.
- **Task [`plan-tech-deliverability`](../../tasks/funnel-tech/plan-tech-deliverability.md)** — dono [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md). Arma links, URLs e entregabilidade.

## Passos
1. Mapeie o funil com [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md): cada degrau do money model vira uma página com destino.
2. Confirme zero dead-end: toda página leva à próxima ou à de obrigado. Nenhum beco sem saída.
3. Posicione o order bump ou upsell no checkout, se o money model pedir.
4. Escreva as specs de cada página: objetivo, blocos, CTA, elementos de prova.
5. Monte a janela de carrinho com [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md): redirecionamento ao abrir e ao fechar.
6. Crie a planilha de URLs: todos os links rastreáveis, com UTM e redirecionamentos de abre/fecha.
7. Arme a entregabilidade: SPF, DKIM, DMARC, aquecimento, lista limpa, para o e-mail cair na caixa de entrada.
8. Planeje o pico de carga com [`launch/surge-ops`](../../frameworks/launch/surge-ops.md): checkout e páginas aguentam o tráfego.
9. Teste cada link e cada caminho. Atualize o `decision-registry`.

## Artefatos Produzidos
- `artifact.funnel-map` — o mapa do funil sem dead-end, refletindo o money model.
- `artifact.page-specs` — as specs de cada página (objetivo, blocos, CTA, prova).
- `artifact.links-urls` — a planilha de URLs rastreáveis com redirecionamentos.
- `artifact.tech-deliverability-plan` — o plano de entregabilidade e de carga.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`funnel/funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) — nenhuma página sem destino.
- [`funnel/funnel-backend-gate`](../../checklists/funnel/funnel-backend-gate.md) — o backend (upsell/continuidade) está no funil.
- [`tech-deliverability-checklist`](../../checklists/tech-deliverability-checklist.md) e [`launch/launch-fallback-gate`](../../checklists/launch/launch-fallback-gate.md).

## Critério de Saída
O funil não tem dead-end; cada degrau do money model está representado; o order bump ou upsell está no checkout se aplicável; as specs de página estão escritas; a planilha de URLs tem todos os links rastreáveis com redirecionamentos de abre/fecha; a entregabilidade está configurada; o plano de carga existe; cada caminho foi testado. Os gates de funil e tech estão verdes. A próxima fase é a [`05-compliance-and-ship`](05-compliance-and-ship.md), que audita tudo antes de a promo ir ao ar.
