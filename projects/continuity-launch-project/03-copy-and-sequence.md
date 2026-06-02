---
id: project.continuity-launch-project.03-copy-and-sequence
title: "Fase 03 — Copy & Sequência"
type: project-phase
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes:
  - artifact.offer-book-master
  - artifact.continuity-offer
  - artifact.onboarding-flow
  - artifact.retention-system
produces:
  - artifact.vsl-script
  - artifact.welcome-sequence
  - artifact.retention-sequence
  - artifact.funnel-map
tags: [project-phase, continuity, copy, vsl, welcome, retencao, sequence, funnel, d4]
---

# Fase 03 — Copy & Sequência

## Objetivo da Fase
Escrever a copy que vende a continuidade e as sequências que retêm o assinante. A continuidade tem dois momentos de copy: a venda (por que assinar) e a permanência (por que ficar). Esta fase produz a peça-âncora que vende a recorrência empilhando o valor de cada ciclo, a sequência de boas-vindas que conduz ao momento "aha" do onboarding, e a sequência de retenção que reforça o valor antes de cada renovação e recupera quem está em risco de churn. O estado-pronto é a peça-âncora na voz da marca, a sequência de boas-vindas ligada ao onboarding, a sequência de retenção ligada ao playbook de churn e o funil curto que entrega a assinatura. A régua aqui: a copy de venda promete só o valor recorrente que a Fase 01 desenhou, e a copy de retenção mostra o valor já entregue para justificar a próxima cobrança.

## Critério de Entrada
A [`01-continuity-offer-design`](01-continuity-offer-design.md) entrega o Offer Book Master e a oferta recorrente; a [`02-retention-and-onboarding`](02-retention-and-onboarding.md) entrega o onboarding e o sistema de retenção. Pré-condição absoluta: o ★ [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) está verde — `offer_before_persuasion`. Pré-condição de conteúdo: o momento "aha" e os marcos de valor por ciclo estão definidos, porque as sequências os reforçam. Se o onboarding não tem "aha" claro, a sequência de boas-vindas não tem destino — a fase sinaliza. O [`control-registry`](../../data/registries/control-registry.md) é lido para reusar sequências de retenção vencedoras.

## Agentes & Tasks
- **Task [`write-vsl-webinar`](../../tasks/copy/write-vsl-webinar.md)** — dono [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md), com passe de voz do [`voice-style-guardian`](../../agents/voice-style-guardian.md).
- **Task [`write-email-sms-sequences`](../../tasks/copy/write-email-sms-sequences.md)** — dono [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md).
- **Task [`map-funnel`](../../tasks/funnel-tech/map-funnel.md)** — dono [`funnel-architect`](../../agents/funnel-architect.md).

## Passos
1. Escreva a peça-âncora de venda com a Big Idea no lead, empilhando o valor de cada ciclo antes do preço, com [`copy/vsl-structure`](../../frameworks/copy/vsl-structure.md).
2. Mostre o motivo de ficar como parte da promessa: o valor que se acumula no tempo, não só o do primeiro mês.
3. Escreva a sequência de boas-vindas com [`copy/email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md): conduza o novo assinante ao momento "aha" do onboarding.
4. Escreva a sequência de retenção: cada e-mail antes da renovação mostra o valor já entregue e o que vem no próximo ciclo.
5. Escreva os e-mails de salvamento ligados ao playbook de churn: uso caindo, risco de cancelamento, cartão recusado (dunning).
6. Use os padrões de continuidade de [`lib/patterns/continuity-patterns.md`](../../lib/patterns/continuity-patterns.md) para as mensagens de permanência.
7. Mapeie o funil curto com [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md): página de venda → checkout recorrente → boas-vindas, sem dead-end.
8. Rode o passe de voz e teste os gatilhos das sequências. Atualize o `control-registry`.

## Artefatos Produzidos
- `artifact.vsl-script` — a peça-âncora que vende a recorrência, na voz da marca.
- `artifact.welcome-sequence` — a sequência de boas-vindas ligada ao onboarding.
- `artifact.retention-sequence` — a sequência de retenção e de salvamento ligada ao churn.
- `artifact.funnel-map` — o funil curto da assinatura, sem dead-end.
- Registry escrito: [`control-registry`](../../data/registries/control-registry.md).

## Gates
- [`vsl/vsl-value-before-price-gate`](../../checklists/vsl/vsl-value-before-price-gate.md) — o valor recorrente vem antes do preço.
- [`email-sms/email-step-coverage-gate`](../../checklists/email-sms/email-step-coverage-gate.md) — boas-vindas, retenção e salvamento cobertos.
- [`funnel/funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) e a voz aprovada pelo guardião.

## Critério de Saída
A peça-âncora vende a recorrência com o valor de cada ciclo antes do preço; a sequência de boas-vindas conduz ao "aha"; a sequência de retenção reforça o valor antes de cada renovação; os e-mails de salvamento cobrem os gatilhos de churn e o dunning; o funil curto não tem dead-end. Os gates de copy e funil estão verdes; o guardião de voz aprovou. A próxima fase é a [`04-compliance-and-ship`](04-compliance-and-ship.md), que audita os claims de recorrência e as regras de cobrança antes de o lançamento ir ao ar.
