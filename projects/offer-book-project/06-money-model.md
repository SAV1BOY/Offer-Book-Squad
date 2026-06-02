---
id: project.offer-book-project.06-money-model
title: "Fase 06 — Money Model (a Espinha)"
type: project-phase
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes:
  - artifact.mechanism-sheet
  - artifact.value-equation-scorecard
  - artifact.pricing-wtp-sheet
  - artifact.unit-economics-sheet
produces:
  - artifact.money-model
  - artifact.products-and-offers
  - decision.ladder-configuration
tags: [project-phase, offer-architecture, money-model, espinha, escada, upsell, continuidade, veto, d2]
---

# Fase 06 — Money Model (a Espinha)

## Objetivo da Fase
Desenhar a sequência mínima de ofertas (alvo 4 partes: atração, núcleo, upsell, downsell, continuidade) que faz um cliente liquidar o CAC e financiar a aquisição de mais clientes, com um CTA por degrau. O estado-pronto é a estrutura econômica que existe e passará no Definition of Done antes de qualquer copy, funil ou logística. Esta fase é o coração da camada D2 e detém o veto mais estrutural do squad: sem espinha, nada a jusante começa. O funil de D5 espelha esta escada; a Big Idea da Fase 08 nasce sobre a oferta-núcleo já posicionada.

## Critério de Entrada
A Fase 04 entrega o `artifact.mechanism-sheet` (o núcleo orbita o mecanismo). A Fase 05 entrega o `artifact.value-equation-scorecard` (quais componentes movem quais alavancas, para alocar cada um). A Fase 07 entrega, em relação iterativa, o `artifact.pricing-wtp-sheet` (preço por degrau) e o `artifact.unit-economics-sheet` (CAC, AOV, margem, para validar que a atração liquida o CAC). Pré-condição: mecanismo provado e scorecard de valor fechados. Esta fase e a 07 trabalham em laço: desenho a forma da escada, o unit-econ valida a conta, eu fecho. Sem unit economics, desenho a forma marcada não-validada e bloqueio o avanço para copy. Os registries [`offer-registry`](../../data/registries/offer-registry.md) e [`price-test-registry`](../../data/registries/price-test-registry.md) são escritos aqui.

## Agentes & Tasks
- **Task [`design-money-model`](../../tasks/offer-architecture/design-money-model.md)** — dono [`money-model-designer`](../../agents/money-model-designer.md), o dono da espinha, com os colaboradores de D2: [`value-equation-engineer`](../../agents/value-equation-engineer.md), [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) e [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md). Tem poder de veto (HARD STOP da espinha).

## Passos
1. Desenhe a oferta de atração com [`attraction-offer-design`](../../frameworks/money-model-designer/attraction-offer-design.md): tripwire, free+frete, challenge ou win-your-money-back. Ela converte estranho em comprador e cobre o CAC.
2. Defina o núcleo: a oferta que entrega o mecanismo.
3. Projete o upsell com [`upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md): no pico de compra, o componente de aceleração (Tempo↓) sobe o AOV.
4. Projete o downsell: versão menor/parcelada que recupera a margem do "não".
5. Desenhe a continuidade com [`continuity-design`](../../frameworks/money-model-designer/continuity-design.md): recorrência com valor contínuo real, não só cobrança.
6. Gere ≥3 configurações de escada com Tree-of-Thoughts, pontuadas por liquidação de CAC, AOV, LTV, atrito e fit. A que não liquida o CAC é podada de saída. Sequencie a vencedora com [`offer-ladder-sequencing`](../../frameworks/money-model-designer/offer-ladder-sequencing.md), um CTA por degrau.
7. Valide a liquidação com o unit-econ da Fase 07: atração+upsell cobrem o CAC em <30 dias. Não cobre, itere a forma.
8. Self-verify com red-team e registre a espinha no `offer-registry`, os pontos no `price-test-registry`. Passe os três gates.

## Artefatos Produzidos
- `artifact.money-model` — a espinha sequenciada (papel, tipo, preço, CTA, alavanca, liquida-CAC por degrau), AOV/LTV/payback, config vencedora e podadas, four_parts_pass, status.
- `artifact.products-and-offers` — a planilha de produtos e ofertas.
- `decision.ladder-configuration` — a configuração de escada travada.
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md) e [`price-test-registry`](../../data/registries/price-test-registry.md).

## Gates
- [`money-model/money-model-four-parts-gate`](../../checklists/money-model/money-model-four-parts-gate.md)
- [`money-model/money-model-sequence-gate`](../../checklists/money-model/money-model-sequence-gate.md)
- [`money-model/money-model-cta-per-step-gate`](../../checklists/money-model/money-model-cta-per-step-gate.md)

## Critério de Saída
A escada cobre os papéis com ≥2 partes (alvo 4); a atração liquida o CAC (validado pelo unit-econ) e o ponto de liquidação está nomeado; cada degrau tem um CTA; ≥3 configurações foram comparadas e a vencedora é defensável; os três gates de money-model estão verdes; a decisão está registrada. Se a espinha não fecha, fica não-validada e a copy permanece barrada. A próxima fase é a [`07-pricing-unit-economics`](07-pricing-unit-economics.md), que fecha o laço derivando o preço por valor e provando a liquidação do CAC com números.
