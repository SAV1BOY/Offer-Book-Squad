---
id: doc.exemplar-project-walkthrough
title: "Walkthrough Exemplar — De Oferta Bruta a Blackbook"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [exemplar, walkthrough, end-to-end, onboarding]
---

# Walkthrough Exemplar — De Oferta Bruta a Blackbook

Um caso fictício, ponta a ponta, para o operador ver o pipeline funcionando: quais agentes entram, qual gate passa e qual registry é alimentado em cada fase. Caso: **Mariana**, mentora de transição de carreira (CLT → tech), oferta bruta "curso de transição", 80 alunos com resultado, meta de escalar. O [offerbook-chief](../agents/offerbook-chief.md) classifica como **full-launch** (oferta provada) e roda o workflow [full-launch-blackbook](../workflows/full-launch-blackbook.md). (Se não houvesse prova, seria [single-promo](../workflows/single-promo.md); se fosse B2B, [enterprise-deal-book](../workflows/enterprise-deal-book.md); se fosse só desenhar a escada, [offer-ladder](../workflows/offer-ladder.md).)

## D0 — Escopo & pipeline
- **Agentes:** offerbook-chief, [offer-squad-architect](../agents/offer-squad-architect.md). **Task:** [intake-and-scope](../tasks/planning/intake-and-scope.md).
- **Escopo (1 frase):** "Escalar a oferta provada de transição CLT→tech da Mariana num lançamento completo."
- **Gate:** [chief-scope-approval-gate](../checklists/chief/chief-scope-approval-gate.md). **Registry:** [decision-registry](../data/registries/decision-registry.md) (project type + escopo).

## D1 — Inteligência
- **market-sophistication-analyst** → sofisticação **4** (mercado cheio de "bootcamps"), consciência **3**. **Gate:** [market-sophistication-gate](../checklists/market/market-sophistication-gate.md).
- **avatar-voc-investigator** → 12 verbatims; emoção dominante: medo de "ser velho demais para mudar". **Gate:** [avatar-voc-verbatim-gate](../checklists/avatar/avatar-voc-verbatim-gate.md). **Registry:** [objection-registry](../data/registries/objection-registry.md).
- **proof-credibility-curator** → 80 casos catalogados. **Registry:** [proof-registry](../data/registries/proof-registry.md). **Agrega:** [intelligence-complete-gate](../checklists/offer-book-stack/intelligence-complete-gate.md).

## D2 — Arquitetura de oferta
- **mechanism-architect** → mecanismo "Portfólio-Primeiro" (vs "estudar teoria"). **Gate:** [mechanism-naming-gate](../checklists/mechanism/mechanism-naming-gate.md).
- **value-equation-engineer** → eleva probabilidade (garantia) e corta tempo (90 dias). **Veto** de componente órfão: [value-no-orphan-lever-gate](../checklists/value/value-no-orphan-lever-gate.md).
- **money-model-designer** → escada: atração (workshop pago R$47) → núcleo (R$1.997) → upsell (mentoria) → continuidade (comunidade). **Veto/Gate:** [money-model-four-parts-gate](../checklists/money-model/money-model-four-parts-gate.md). **Planilha:** [products-and-offers](../templates/offer/products-and-offers-template.csv).
- **pricing-wtp-strategist** + **unit-economics-stack-analyst** → preço por WTP (Van Westendorp); confirma que a atração **liquida o CAC**. **Registry:** [price-test-registry](../data/registries/price-test-registry.md). **Agrega:** [offer-architecture-gate](../checklists/offer-book-stack/offer-architecture-gate.md).

## D3 — Big Idea & posição
- **big-idea-architect** → gera 4 ideias (ToT), trava UMA: "Seu portfólio contrata por você". **Veto:** [big-idea-single-gate](../checklists/big-idea/big-idea-single-gate.md). **Registry:** [big-idea-registry](../data/registries/big-idea-registry.md).
- **positioning-lead-strategist** → lead de Problema-Solução (casa com consciência 3). **Gate:** [positioning-awareness-fit](../checklists/positioning/positioning-awareness-fit.md).

## ★ HARD STOP — Offer Book DoD
- **Task:** [assemble-offer-book](../tasks/assembly/assemble-offer-book.md). **Gate:** [offer-book-dod-gate](../checklists/offer-book-stack/offer-book-dod-gate.md). **Nenhuma copy (D4+) começa até aqui ficar verde.** Verde → o D4 abre.

## D4 — Copy (na voz)
- **vsl-webinar-scriptwriter**, **email-sms-sequence-writer**, **ad-creative-factory**, **direct-mail-insert-writer** produzem; **voice-style-guardian** roda a [voice-pass](../tasks/copy/voice-pass.md) (**veto** de voz). **Gates:** [vsl-value-before-price-gate](../checklists/vsl/vsl-value-before-price-gate.md), [email-step-coverage-gate](../checklists/email-sms/email-step-coverage-gate.md). **Registry:** [control-registry](../data/registries/control-registry.md).

## D5–D6 — Funil, tech, ops, growth
- **funnel-architect** + **tech-links-deliverability-engineer** (sem becos sem saída; UTMs; load test). **launch-producer** (run-of-show), **events-logistics-coordinator**, **affiliate-program-architect**, **pr-brand-strategist**.

## D7 — ★ Compliance, Blackbook & memória
- **compliance-auditor** audita: cada claim com prova, escassez verdadeira, disclaimers. **Veto** se falhar. **Gate:** [blackbook-dod-gate](../checklists/blackbook-stack/blackbook-dod-gate.md).
- **knowledge-librarian** registra winners, swipe e lições. **Registries:** [control-registry](../data/registries/control-registry.md), [lessons-learned-registry](../data/registries/lessons-learned-registry.md), [swipe-registry](../data/registries/swipe-registry.md).

## Resultado
Um **Offer Book** (fundação provada) + um **Launch Blackbook** (máquina executável), com cada claim rastreável, escassez real e a memória pronta para o próximo lançamento começar adiantado. Próximo passo do operador: abrir o [offer-book-master](../templates/core/offer-book-master.md) e preencher com o caso real.
