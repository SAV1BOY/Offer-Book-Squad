---
id: doc.handoff-matrix
title: "Matriz de Handoffs — Intra-Squad + Cross-Squad"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
tags: [handoff, matrix, upstream, downstream, cross-squad, contracts]
---

# Matriz de Handoffs — Intra-Squad + Cross-Squad

A tabela única que torna **todo handoff explícito** (quem entrega o quê para quem, com qual gate). No frontmatter dos agentes, **`upstream` = handoff_from** e **`downstream` = handoff_to**. Cross-squad usa o [contrato](../templates/cross-squad/handoff-contract-template.md) + gates de saída/entrada + log em [`data/handoffs/`](../data/handoffs/README.md).

## 1. Intra-squad (agente → agente, por camada)

| Camada | Agente | handoff_from (upstream) | handoff_to (downstream) | Gate na transição |
|---|---|---|---|---|
| D0 | offerbook-chief | briefing (raw offer) | offer-squad-architect + todos | [chief-scope-approval-gate](../checklists/chief/chief-scope-approval-gate.md) |
| D0 | offer-squad-architect | offerbook-chief | market-sophistication-analyst | [handoff-contract-gate](../checklists/architect/handoff-contract-gate.md) |
| D1 | market-sophistication-analyst | architect / deepresearch_squad | avatar-voc-investigator, mechanism-architect | [market-sophistication-gate](../checklists/market/market-sophistication-gate.md) |
| D1 | avatar-voc-investigator | market | proof-credibility-curator, mechanism-architect | [avatar-voc-verbatim-gate](../checklists/avatar/avatar-voc-verbatim-gate.md) |
| D1 | proof-credibility-curator | avatar | value-equation-engineer, compliance-auditor | [proof-claim-backing-gate](../checklists/proof/proof-claim-backing-gate.md) |
| D2 | mechanism-architect | market, avatar | value-equation-engineer | [mechanism-naming-gate](../checklists/mechanism/mechanism-naming-gate.md) |
| D2 | value-equation-engineer ⛔ | mechanism, proof | money-model-designer | [value-no-orphan-lever-gate](../checklists/value/value-no-orphan-lever-gate.md) |
| D2 | pricing-wtp-strategist | value, market | unit-economics-stack-analyst, money-model-designer | [pricing-value-derived-gate](../checklists/pricing/pricing-value-derived-gate.md) |
| D2 | unit-economics-stack-analyst | pricing, value | money-model-designer | [unit-econ-cac-liquidation-gate](../checklists/unit-econ/unit-econ-cac-liquidation-gate.md) |
| D2 | money-model-designer ⛔ | mechanism, value, pricing, unit-econ | big-idea-architect, vsl, funnel, events, chief | [money-model-four-parts-gate](../checklists/money-model/money-model-four-parts-gate.md) |
| D3 | big-idea-architect ⛔ | money-model, mechanism, avatar | positioning-lead-strategist, vsl | [big-idea-single-gate](../checklists/big-idea/big-idea-single-gate.md) |
| D3 | positioning-lead-strategist | big-idea, market | vsl, ad-creative-factory, chief | [positioning-awareness-fit](../checklists/positioning/positioning-awareness-fit.md) |
| **★** | **HARD STOP** | (D1–D3 verdes) | **libera D4** | [offer-book-dod-gate](../checklists/offer-book-stack/offer-book-dod-gate.md) |
| D4 | vsl-webinar-scriptwriter | offer book completo | voice-style-guardian, funnel, launch | [vsl-value-before-price-gate](../checklists/vsl/vsl-value-before-price-gate.md) |
| D4 | email-sms-sequence-writer | offer book | voice-style-guardian, funnel | [email-step-coverage-gate](../checklists/email-sms/email-step-coverage-gate.md) |
| D4 | direct-mail-insert-writer | offer book | voice-style-guardian, events | [mailer-spec-gate](../checklists/mailer/mailer-spec-gate.md) |
| D4 | ad-creative-factory | offer book, positioning | voice-style-guardian, traffic_squad | [ads-claim-backing-gate](../checklists/ads/ads-claim-backing-gate.md) |
| D4 | voice-style-guardian ⛔ | todos os agentes de copy | funnel, chief | [voice-approval-gate](../checklists/voice/voice-approval-gate.md) |
| D5 | funnel-architect | copy, money-model | tech, launch | [funnel-no-dead-end-gate](../checklists/funnel/funnel-no-dead-end-gate.md) |
| D5 | tech-links-deliverability-engineer | funnel | launch | [tech-deliverability-gate](../checklists/tech/tech-deliverability-gate.md) |
| D6 | launch-producer | funnel, copy | events, affiliate, compliance | [launch-phase-readiness-gate](../checklists/launch/launch-phase-readiness-gate.md) |
| D6 | events-logistics-coordinator | launch, money-model | compliance | [events-fulfillment-gate](../checklists/events/events-fulfillment-gate.md) |
| D6 | affiliate-program-architect | launch, money-model | compliance | [affiliate-referral-tracking-gate](../checklists/affiliate/affiliate-referral-tracking-gate.md) |
| D6 | pr-brand-strategist | big-idea | compliance | [pr-memorable-angle-gate](../checklists/pr/pr-memorable-angle-gate.md) |
| D7 | compliance-auditor ⛔ | todos D4–D6 | knowledge-librarian, chief | [blackbook-dod-gate](../checklists/blackbook-stack/blackbook-dod-gate.md) |
| D7 | knowledge-librarian | compliance | registries + próximo intake | [final-delivery-checklist](../checklists/final-delivery-checklist.md) |

⛔ = agente com poder de veto. Recuperação de cada gate em [`failure-paths-and-gate-recovery`](failure-paths-and-gate-recovery.md).

## 2. Cross-squad (os 12 squads do ecossistema MMOS)

> Este repo é **single-squad**; os vizinhos são **integração-por-design** (contratos prontos). Todo handoff cross-squad usa o [contrato reutilizável](../templates/cross-squad/handoff-contract-template.md), passa pela gate de saída [`cross-squad-handoff-quality`](../checklists/cross-squad/cross-squad-handoff-quality.md) e pela de entrada [`cross-squad-asset-validation`](../checklists/cross-squad/cross-squad-asset-validation.md), e é logado em [`data/handoffs/`](../data/handoffs/README.md).

| Squad | Direção | handoff (o quê) | Assets compartilhados |
|---|---|---|---|
| deepresearch | **upstream →** | recebe: market sizing, VOC, competitor intel | market-theses, audience-insights |
| advisory-board | **upstream →** | recebe: crítica estratégica, risk flags; envia: oferta+big idea p/ stress-test | strategic-review, risk-assessment |
| storytelling | **upstream →** | recebe: arcos narrativos, hero-journey, epiphany-bridge | narrative-arcs, proof-points |
| movement | **upstream →** | recebe: sinais de comunidade/identidade coletiva | identity-belonging, community-language |
| pre-programming | **upstream →** | recebe: prontidão de produto, escopo, viabilidade de entrega | scope, readiness-review |
| copy | **← downstream** | envia: offer book + big idea + prova; recebe: copy longa polida, swipe | market-language, winning-controls |
| brand | **← downstream** | envia: positioning + big idea; recebe: brand voice, category analysis | positioning, brand-voice |
| traffic-masters | **← downstream** | envia: ad matrix + oferta + funnel map; recebe: performance, winning hooks | ad-creative, channel-intelligence |
| design | **← downstream** | envia: page/ad/mailer specs; recebe: visuais, brand assets | landing-pages, creative-assets |
| data | **← downstream** | envia: pricing test design, conversion data; recebe: WTP, cohort/LTV | pricing-science, cohort-analysis |
| cybersecurity | **← downstream** | envia: deliverability + coleta de dados p/ review; recebe: assessment LGPD/GDPR | deliverability, data-privacy |
| c-level | **↕ ambos** | envia: business case + projeções; recebe: metas de receita + prioridade | revenue-models, launch-objectives |

## 3. Quando uma task sai do escopo
Regra em [`config.yaml`](../config.yaml) `delegation_rules`: o [offerbook-chief](../agents/offerbook-chief.md) detecta o fora-de-escopo, escolhe o squad destino, exige o contrato e roda a gate de saída. Conflito entre squads → escala ao `hrm_central` (ver [`hrm-governance`](hrm-governance.md)).
