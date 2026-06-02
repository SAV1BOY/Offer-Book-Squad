---
id: framework.readme
title: "frameworks/ — Índice e Hierarquia"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
tags: [frameworks, index, hierarchy, navigation]
---

# frameworks/ — Índice e Hierarquia

Como o squad **pensa**. Cada framework é um arquivo executável (quando usar, inputs, procedimento, outputs, exemplo, armadilhas, interações, fontes). Comece pelos **universais**; os de subpasta são especializações.

## Universais (raiz)
A espinha do raciocínio de oferta: [value-equation](value-equation.md) · [money-model-sequence](money-model-sequence.md) · [offer-stack-builder](offer-stack-builder.md) · [awareness-x-sophistication](awareness-x-sophistication.md) · [starving-crowd](starving-crowd.md) · [magic-naming](magic-naming.md) · [guarantee-design](guarantee-design.md) · [scarcity-urgency-engine](scarcity-urgency-engine.md) · [power-of-one](power-of-one.md) · [big-idea-generator](big-idea-generator.md) · [lead-types](lead-types.md) · [unique-mechanism](unique-mechanism.md) · [meta-launch-principle](meta-launch-principle.md) · [price-anchoring](price-anchoring.md) · [risk-reversal-ladder](risk-reversal-ladder.md) · [offer-to-funnel-mapping](offer-to-funnel-mapping.md) · [proof-to-claim-chain](proof-to-claim-chain.md).

## Por domínio
- **[offer/](offer/)** — grand-slam-offer, offer-diagnosis, value-stacking.
- **[copy/](copy/)** — aida, pas, pastor, 4ps, vsl-structure, fascination-bullets, hook-frameworks, close-frameworks, slippery-slide, one-sentence-persuasion, email-sequence-architecture.
- **[pricing/](pricing/)** — van-westendorp, gabor-granger, conjoint-cbc, maxdiff, kano-model, value-based-pricing, price-elasticity, packaging-good-better-best, decoy-effect.
- **[positioning/](positioning/)** — dunford-positioning, moore-positioning-formula, ries-trout-positioning, category-design, blue-ocean-strategy, jtbd, 4-monetization-failures, perceived-value-stack.
- **[launch/](launch/)** — product-launch-formula, perfect-webinar, cart-open-close, runway-and-phases, affiliate-army, surge-ops, abandoned-cart-recovery, pr-brand-maximization.

## Hierarquia por-agente (parent universal → especializações)
Leia o **parent** primeiro; entre na subpasta quando precisar do procedimento detalhado.
- [money-model-sequence](money-model-sequence.md) → **[money-model-designer/](money-model-designer/)**: attraction-offer-design, upsell-downsell-logic, continuity-design, offer-ladder-sequencing.
- [value-equation](value-equation.md) → **[value-equation-engineer/](value-equation-engineer/)**: dream-outcome-amplification, likelihood-of-achievement, time-delay-compression, effort-sacrifice-reduction (uma por alavanca).
- [big-idea-generator](big-idea-generator.md) → **[big-idea-architect/](big-idea-architect/)**: big-idea-ideation-tot, big-idea-scoring, promise-hook-villain.
- (avatar) → **[avatar-voc-investigator/](avatar-voc-investigator/)**: voc-mining, objection-belief-mapping, dmu-mapping-b2b.

## Referência intelectual (doutrina)
**[reference-intellectual/](reference-intellectual/)** — os métodos nomeados (Hormozi, Schwartz, Cialdini, Halbert, Sugarman, Kennedy, Ogilvy, Caples, Ramanujam, Voss, Kahneman) + [hrm-hierarchical-reasoning](reference-intellectual/hrm-hierarchical-reasoning.md) (a base metodológica dos prompts). Operacionalizados nos agentes; aqui ficam como fundamento citável.

## Como escolher um framework
1. Veja a §4 do agente dono (ele lista quais frameworks aplica e quando).
2. Ou ache sua task no [config.yaml](../config.yaml) `routing` — o campo `frameworks:` lista os ids.
3. Universais resolvem 80% dos casos; subpastas são para profundidade.
