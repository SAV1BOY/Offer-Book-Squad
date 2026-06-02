---
id: task.offer-architecture.design-money-model
title: "Design Money Model — Desenhar a Espinha (Atração → Núcleo → Upsell → Downsell → Continuidade) Antes de Qualquer Copy"
type: task
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes:
  - artifact.mechanism-sheet
  - artifact.value-equation-scorecard
  - artifact.unit-economics-sheet
  - artifact.pricing-wtp-sheet
produces:
  - artifact.money-model
  - artifact.products-and-offers
  - decision.ladder-configuration
frameworks:
  - money-model-sequence
  - money-model-designer/attraction-offer-design
  - money-model-designer/upsell-downsell-logic
  - money-model-designer/continuity-design
  - money-model-designer/offer-ladder-sequencing
checklists:
  - money-model/money-model-four-parts-gate
  - money-model/money-model-sequence-gate
  - money-model/money-model-cta-per-step-gate
registries: [offer-registry, price-test-registry]
tags: [offer-architecture, money-model, espinha, escada, atracao, upsell, continuidade, veto, hard-stop, d2]
---

# Design Money Model — desenhar a espinha (atração → núcleo → upsell → downsell → continuidade) antes de qualquer copy

## Objetivo
Desenhar a sequência mínima de ofertas (alvo 4 partes) que faz um cliente liquidar o CAC e financiar a aquisição de mais clientes, com um CTA por degrau — a estrutura econômica que existe e passa no Definition of Done **antes** de qualquer copy, funil ou logística.

## Agente dono
[`money-model-designer`](../../agents/money-model-designer.md), o **dono da espinha**, com os colaboradores de D2: [`value-equation-engineer`](../../agents/value-equation-engineer.md) (o que pertence a cada degrau), [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) (o preço de cada degrau) e [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) (a liquidação do CAC). Não escreve copy, não desenha página. **Tem o poder de veto mais estrutural do squad** — sem espinha, nada a jusante começa (HARD STOP da espinha).

## Gatilho / Quando
Roda em D2, quando: (a) mecanismo provado, value scorecard e unit economics estão disponíveis; (b) o chief pede para desenhar/refazer a espinha; (c) **qualquer** agente de copy/funil/logística tenta começar antes de a escada existir — aí acordo para **barrar**. **Pré-condição:** mecanismo provado, scorecard de valor (o que pertence a cada degrau) e unit economics preliminares (CAC/AOV/margem) para validar que a atração **liquida o CAC**; o preço por valor entra para fixar os pontos de cada degrau. Sem unit economics, desenho a **forma** marcada `não-validada` e bloqueio o avanço para copy.

## Inputs (Consome)
- **`artifact.mechanism-sheet`** — o mecanismo e a frase única (o núcleo entrega isto; cada degrau orbita isto).
- **`artifact.value-equation-scorecard`** — quais componentes movem quais alavancas, para alocar cada um ao degrau certo (ex.: acelerador de Tempo↓ vira upsell de velocidade).
- **`artifact.unit-economics-sheet`** — CAC, AOV-alvo, margem, payback, para garantir que a atração liquida o CAC no front-end.
- **`artifact.pricing-wtp-sheet`** — o preço derivado de valor/WTP de cada peça e o packaging good-better-best.
- **Registries escritos:** [`offer-registry`](../../data/registries/offer-registry.md) (a espinha) e [`price-test-registry`](../../data/registries/price-test-registry.md) (os pontos de preço por degrau).

## Procedimento
1. **Desenhe a oferta de atração.** Aplique [`attraction-offer-design`](../../frameworks/money-model-designer/attraction-offer-design.md): teste tripwire vs free+frete vs challenge vs win-your-money-back. Ela precisa converter estranho em comprador e **cobrir o CAC**.
2. **Defina o núcleo.** A oferta que entrega o mecanismo — o centro da escada.
3. **Projete o upsell.** Aplique [`upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md): no pico de compra, pegue do value scorecard o componente de aceleração (Tempo↓) — sobe o AOV sem inflar o CAC.
4. **Projete o downsell.** Para quem disse "não" ao upsell: versão menor/parcelada que recupera margem que sumiria.
5. **Desenhe a continuidade.** Aplique [`continuity-design`](../../frameworks/money-model-designer/continuity-design.md): recorrência com **valor contínuo real** (comunidade/assinatura), não só cobrança — senão o LTV infla no papel e perde na prática.
6. **Gere ≥3 configurações completas de escada (Tree-of-Thoughts — central).** Cada uma especifica os 4-5 degraus, tipos de oferta e preços. Pontue por *liquidação de CAC* (×3), *AOV/upside* (×2), *LTV/continuidade* (×2), *atrito de execução* (×2, penaliza), *fit com mecanismo+valor* (×1). Configuração que **não liquida o CAC** é podada de saída — é o critério eliminatório. Sequencie a vencedora com [`offer-ladder-sequencing`](../../frameworks/money-model-designer/offer-ladder-sequencing.md), um CTA por degrau.
7. **Valide a liquidação com o unit-econ.** Confirme com o [`unit-economics-stack-analyst`](model-unit-economics.md) que a atração+upsell cobrem o CAC em <30 dias. Não cobre → itere a forma (mover upsell para mais cedo, trocar o tipo de atração).
8. **Self-verify (Bloom + red-team).** A escada tem todos os papéis? Cada degrau usa o tipo certo? Comparei ≥3 configurações? *"O que o `unit-economics-stack-analyst` reprovaria?"* (atração que não cobre o CAC). *"O que o `compliance-auditor` rejeitaria?"* (continuidade obrigatória sem cancelamento claro). Corrija.
9. **Registre e passe os gates.** Logue a espinha no `offer-registry` e os pontos por degrau no `price-test-registry` (`ladder_id`, degraus, config vencedora, configs podadas, AOV, LTV, payback, `four_parts_pass`, `status: validada|não-validada`). Registre a decisão de configuração e cada veto/override.

## Frameworks
- [`money-model-sequence`](../../frameworks/money-model-sequence.md) — ordem e meta dos 30 dias; sequência mínima de 2 (alvo 4).
- [`attraction-offer-design`](../../frameworks/money-model-designer/attraction-offer-design.md) — oferta que liquida o CAC.
- [`upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md) — pico de compra e recuperação do "não".
- [`continuity-design`](../../frameworks/money-model-designer/continuity-design.md) — mecânica de LTV.
- [`offer-ladder-sequencing`](../../frameworks/money-model-designer/offer-ladder-sequencing.md) — ordenação/timing com CTAs.

## Outputs (Produz)
- **`artifact.money-model`** ([`template`](../../templates/offer/money-model-template.md)) — a espinha sequenciada (papel/tipo/preço/CTA/alavanca/liquida-CAC por degrau), AOV/LTV/payback, config vencedora e podadas, `four_parts_pass`, status.
- **`artifact.products-and-offers`** ([`template`](../../templates/offer/products-and-offers-template.csv)) — a planilha de produtos e ofertas.
- **`decision.ladder-configuration`** — a configuração de escada travada.
- **Registries escritos:** [`offer-registry`](../../data/registries/offer-registry.md) e [`price-test-registry`](../../data/registries/price-test-registry.md).

## Definition of Done
A escada cobre os papéis (atração, núcleo, upsell, downsell, continuidade) com ≥2 partes (alvo 4); a atração **liquida o CAC** (validado pelo unit-econ) e o ponto de liquidação está nomeado; cada degrau tem **um** CTA/próximo passo; ≥3 configurações foram comparadas e a vencedora é defensável; os três gates de money-model estão verdes; a decisão está registrada. Máximo de 3 ciclos antes de escalar ao chief. Se a espinha não fecha, fica `não-validada` e a copy permanece **barrada**.

## Gates
- [`money-model/money-model-four-parts-gate`](../../checklists/money-model/money-model-four-parts-gate.md)
- [`money-model/money-model-sequence-gate`](../../checklists/money-model/money-model-sequence-gate.md)
- [`money-model/money-model-cta-per-step-gate`](../../checklists/money-model/money-model-cta-per-step-gate.md)

## Handoff
**Próxima task:** [`generate-big-ideas`](../big-idea/generate-big-ideas.md) — dono [`big-idea-architect`](../../agents/big-idea-architect.md), que recebe a oferta-núcleo já posicionada na escada. Adiante, o [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) e o [`funnel-architect`](../../agents/funnel-architect.md) recebem a sequência completa com CTAs por degrau (o funil **espelha** a escada); o [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md), o que cada degrau exige operar; o [`offerbook-chief`](../../agents/offerbook-chief.md), o sinal de que a espinha passou no DoD. **Garantia:** todo downstream recebe uma sequência completa, sequenciada, com um CTA por degrau e a atração validada como liquidante do CAC — nunca uma oferta avulsa. Fecha a camada D2.
