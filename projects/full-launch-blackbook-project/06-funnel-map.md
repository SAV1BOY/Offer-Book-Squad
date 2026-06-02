---
id: project.full-launch-blackbook-project.06-funnel-map
title: "Fase 06 — Mapa de Funil"
type: project-phase
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
consumes:
  - artifact.offer-book
  - artifact.money-model
  - artifact.vsl-script
  - artifact.email-sms-sequences
  - artifact.ad-matrix
  - decision.voice-verdict
produces:
  - artifact.funnel-map
  - artifact.page-specs
  - decision.funnel-routes
tags: [project-phase, funnel, funil, money-model, paginas, checkout, sem-becos, d5]
---

# Fase 06 — Mapa de Funil

## Objetivo da Fase
Traduzir o money model travado e a copy aprovada num mapa de funil com uma trilha por degrau (atração, núcleo, upsell, downsell, continuidade), sem nenhum beco sem saída, cobrindo o "não" do comprador e o pós-compra, e especificando cada página, checkout e order bump de forma executável. O estado-pronto é o funnel-map mais as page-specs onde toda página/estado tem próximo passo, as quatro partes do money model viram trilhas reais, e a recuperação do abandono/recusa existe — aprovado nos dois gates de funil. O funil espelha a escada: é a regra de ouro desta camada.

## Critério de Entrada
A Fase 01 entrega o `artifact.money-model` travado com as quatro partes sequenciadas (passou no four-parts-gate) e o `artifact.offer-book` (oferta de núcleo, garantia, preço ancorado, bônus). As Fases 02, 03 e 05 entregam o `artifact.vsl-script`, as `artifact.email-sms-sequences` e a `artifact.ad-matrix` — todos com `decision.voice-verdict` APROVADO. Pré-condição: a copy de núcleo está aprovada na voz (não se mapeia sobre texto que pode mudar) e o money model tem as quatro partes (sem backend o CAC não liquida). Copy sem aprovação volta ao guardião; money model abaixo das partes mínimas volta ao designer via chief. O [`decision-registry`](../../data/registries/decision-registry.md) é escrito.

## Agentes & Tasks
- **Task [`map-funnel`](../../tasks/funnel-tech/map-funnel.md)** — dono [`funnel-architect`](../../agents/funnel-architect.md). Arquiteta o caminho do tráfego. Sem poder de veto.

## Passos
1. Confirme as pré-condições: voice-verdict APROVADO e money model com quatro partes.
2. Desenhe a trilha principal (entrada → VSL/oferta → checkout → TY) com [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md); cada página com um CTA único.
3. Insira o order bump no checkout: complemento de alta margem em 1-clique, sem roubar o foco do núcleo.
4. Sequencie upsell → downsell pós-compra: o "sim" sobe, o "não" cai no downsell, nunca em página morta.
5. Desenhe a recuperação com [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md): ligue o gatilho de abandono à sequência de e-mail/SMS; o "não" final cai numa oferta de backend.
6. Ligue a continuidade: o backend de recorrência ganha trilha própria; a TY convida à continuidade.
7. Especifique cada página (objetivo, seções, CTA único, garantia/T&C visível, consciência-alvo, dependência de copy). Escolha a topologia com Tree-of-Thoughts (≥3 configurações pontuadas por sem-beco, fidelidade ao money model, cobertura do "não", atrito e consciência).
8. Calibre o destino por temperatura (frio → educativa/VSL; retarget → oferta; quente → checkout); self-verify seguindo cada seta; registre as rotas no `decision-registry` e entregue specs executáveis ao tech.

## Artefatos Produzidos
- `artifact.funnel-map` — entrada por temperatura, trilha principal, pós-compra, recuperação, regra "sem beco sem saída".
- `artifact.page-specs` — por página: objetivo, seções, CTA único, garantia/T&C, consciência-alvo, dependência de copy.
- `decision.funnel-routes` — trilha, páginas, bifurcações, order bump, destino por temperatura, alternativas podadas.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`funnel/funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) — nenhuma página/estado sem próximo passo.
- [`funnel/funnel-backend-gate`](../../checklists/funnel/funnel-backend-gate.md) — o backend (upsell/downsell/continuidade) está ligado.

## Critério de Saída
O voice-verdict APROVADO e o money model com quatro partes foram confirmados; todas as quatro partes aparecem como trilha; o backend está ligado; nenhuma página/estado fica sem próximo passo (TY, "não" do upsell, abandono têm rota); o abandono está ligado à recuperação; cada página está especificada; o destino casa por temperatura; os dois gates de funil estão verdes e as rotas estão registradas. A próxima fase é a [`07-tech-deliverability`](07-tech-deliverability.md), que torna o funil executável, resiliente e entregável na caixa de entrada.
