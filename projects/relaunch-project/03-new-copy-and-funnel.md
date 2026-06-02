---
id: project.relaunch-project.03-new-copy-and-funnel
title: "Fase 03 — Nova Copy & Funil"
type: project-phase
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes:
  - artifact.offer-book-master
  - decision.big-idea-locked
  - artifact.failure-diagnosis
produces:
  - artifact.vsl-script
  - artifact.email-sequence
  - artifact.funnel-map
  - artifact.links-urls
tags: [project-phase, relaunch, copy, vsl, email, funnel, d4]
---

# Fase 03 — Nova Copy & Funil

## Objetivo da Fase
Reescrever a copy e remontar o funil sobre a oferta renovada — corrigindo exatamente onde o anterior sangrou. Esta fase usa duas fontes ao mesmo tempo: o Offer Book renovado (o que vender) e o diagnóstico de falha (onde o anterior perdeu). Se a VSL anterior perdia na primeira virada, a nova ataca essa virada. Se o funil tinha um beco sem saída no upsell, o novo o fecha. O estado-pronto é a nova peça-âncora na voz da marca conduzida pela nova Big Idea, a sequência de e-mail que corrige o timing e os ângulos que cansaram, e o funil remontado sem os pontos de sangramento do anterior, com os links rastreáveis. O que ganhou na autópsia é reusado do [`control-registry`](../../data/registries/control-registry.md); o que perdeu é reescrito. Nada de repetir o ângulo aposentado.

## Critério de Entrada
A [`02-offer-and-bigidea-refresh`](02-offer-and-bigidea-refresh.md) entrega o `artifact.offer-book-master` renovado e a Big Idea; a [`01-previous-launch-autopsy`](01-previous-launch-autopsy.md) entrega o diagnóstico de onde o anterior sangrou. Pré-condição absoluta: o ★ [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) está verde — `offer_before_persuasion`. Pré-condição de conteúdo: o diagnóstico aponta os pontos de queda do funil anterior. Se o diagnóstico está vago sobre onde sangrou, a nova copy corre o risco de repetir o erro — a fase sinaliza. O [`control-registry`](../../data/registries/control-registry.md) é lido para reusar o que ganhou.

## Agentes & Tasks
- **Task [`write-vsl-webinar`](../../tasks/copy/write-vsl-webinar.md)** — dono [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md), com passe de voz do [`voice-style-guardian`](../../agents/voice-style-guardian.md).
- **Task [`write-email-sms-sequences`](../../tasks/copy/write-email-sms-sequences.md)** — dono [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md).
- **Task [`map-funnel`](../../tasks/funnel-tech/map-funnel.md)** e [`plan-tech-deliverability`](../../tasks/funnel-tech/plan-tech-deliverability.md) — donos [`funnel-architect`](../../agents/funnel-architect.md) e [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md).

## Passos
1. Reescreva a peça-âncora com a nova Big Idea no lead, calibrada à sofisticação atual com [`lead-types`](../../frameworks/lead-types.md).
2. Ataque o ponto de queda da VSL anterior: se a virada falhava, reconstrua a virada com [`copy/vsl-structure`](../../frameworks/copy/vsl-structure.md) ou [`copy/pastor`](../../frameworks/copy/pastor.md).
3. Empilhe o valor antes do preço e revele o mecanismo renovado; trate cada objeção do mapa.
4. Reescreva a sequência de e-mail com [`copy/email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md): corrija o timing e troque os ângulos que cansaram.
5. Reuse do [`control-registry`](../../data/registries/control-registry.md) os e-mails e ganchos que ganharam; reescreva os que perderam.
6. Remonte o funil com [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md): feche o beco sem saída do anterior, sem nenhum dead-end novo.
7. Crie a planilha de URLs rastreáveis e configure a entregabilidade (SPF, DKIM, DMARC, lista limpa).
8. Rode o passe de voz e teste cada caminho do funil. Atualize o `control-registry` e o `decision-registry`.

## Artefatos Produzidos
- `artifact.vsl-script` — a nova peça-âncora na voz da marca, atacando o ponto de queda anterior.
- `artifact.email-sequence` — a sequência reescrita com timing e ângulos corrigidos.
- `artifact.funnel-map` — o funil remontado sem os pontos de sangramento, sem dead-end.
- `artifact.links-urls` — a planilha de URLs rastreáveis com a entregabilidade configurada.
- Registries escritos: [`control-registry`](../../data/registries/control-registry.md), [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`vsl/vsl-value-before-price-gate`](../../checklists/vsl/vsl-value-before-price-gate.md) e [`vsl/vsl-cta-strength-gate`](../../checklists/vsl/vsl-cta-strength-gate.md) — o valor antecede o preço e o CTA é forte.
- [`email-sms/email-step-coverage-gate`](../../checklists/email-sms/email-step-coverage-gate.md) — todas as fases da sequência cobertas.
- [`funnel/funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) — nenhuma página sem destino.

## Critério de Saída
A nova peça-âncora está na voz da marca, conduzida pela nova Big Idea, atacando o ponto de queda anterior; a sequência reescrita corrigiu timing e ângulos; o funil remontado fechou o beco sem saída e não tem dead-end novo; a planilha de URLs e a entregabilidade estão prontas; cada caminho foi testado. Os gates de copy e funil estão verdes; o guardião de voz aprovou. A próxima fase é a [`04-compliance-and-ship`](04-compliance-and-ship.md), que audita tudo antes de o relançamento ir ao ar.
