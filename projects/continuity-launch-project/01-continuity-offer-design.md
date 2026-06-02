---
id: project.continuity-launch-project.01-continuity-offer-design
title: "Fase 01 — Desenho da Oferta de Continuidade (HARD STOP)"
type: project-phase
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes:
  - artifact.recurring-value-hypothesis
  - decision.scope-one-sentence
  - template.offer.money-model
produces:
  - artifact.offer-book-master
  - artifact.continuity-offer
  - artifact.unit-economics
  - decision.big-idea-locked
tags: [project-phase, continuity, oferta, recorrente, ltv, churn, hard-stop, money-model, d3]
---

# Fase 01 — Desenho da Oferta de Continuidade (HARD STOP)

## Objetivo da Fase
Desenhar a oferta recorrente, provar a economia e fechar o HARD STOP. Esta fase é o coração da trilha: define o formato da continuidade (assinatura, comunidade, software, consumível, manutenção), o gancho de entrada de baixo atrito, o motivo de ficar que se acumula com o tempo, o ciclo de cobrança e o desenho de churn. Modela o LTV e o payback que tornam a aquisição lucrativa, e trava UMA Big Idea para o lançamento. O estado-pronto é o Offer Book Master da continuidade completo, a oferta recorrente desenhada com valor que recorre de fato, a economia provada (LTV, churn-alvo, payback) e a Big Idea travada — tudo no Definition of Done. Nenhuma copy nasce antes deste verde. A régua de continuidade manda: nada de "depósito de conteúdo" pago; acesso passivo sem valor novo não retém. Cada ciclo precisa entregar valor real, ou o churn devora o LTV.

## Critério de Entrada
A [`00-brief`](00-brief.md) entrega a `artifact.recurring-value-hypothesis` e a frase de escopo. Pré-condição: existe uma hipótese clara do que recorre a cada ciclo e uma base de clientes do núcleo. Se a hipótese de valor recorrente é fraca (nada novo a cada ciclo), a fase devolve — sem valor que recorre, não há continuidade que retém. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para a oferta-núcleo; o [`price-test-registry`](../../data/registries/price-test-registry.md) guarda os testes de preço; o [`big-idea-registry`](../../data/registries/big-idea-registry.md) recebe a tese.

## Agentes & Tasks
- **Task [`design-money-model`](../../tasks/offer-architecture/design-money-model.md)** — dono [`money-model-designer`](../../agents/money-model-designer.md), com [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) modelando LTV e [`value-equation-engineer`](../../agents/value-equation-engineer.md) conferindo cada ciclo.
- **Task [`set-pricing-wtp`](../../tasks/offer-architecture/set-pricing-wtp.md)** — dono [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md).
- **Task [`generate-big-ideas`](../../tasks/big-idea/generate-big-ideas.md)** e [`assemble-offer-book`](../../tasks/assembly/assemble-offer-book.md) — donos [`big-idea-architect`](../../agents/big-idea-architect.md), [`offerbook-chief`](../../agents/offerbook-chief.md) e [`compliance-auditor`](../../agents/compliance-auditor.md).

## Passos
1. Identifique o valor recorrente real com [`money-model-designer/continuity-design`](../../frameworks/money-model-designer/continuity-design.md): o que o cliente precisa de novo a cada ciclo.
2. Escolha o formato: assinatura de conteúdo vivo, comunidade/clube, software, consumível, manutenção. Use os padrões de [`lib/patterns/continuity-patterns.md`](../../lib/patterns/continuity-patterns.md).
3. Desenhe o gancho de entrada de baixo atrito: o primeiro ciclo como upsell do núcleo ou bônus que vira pago.
4. Defina o motivo de ficar — o valor que se acumula (rede, progresso, biblioteca viva, resultado contínuo). É o anti-churn.
5. Escolha o ciclo de cobrança: mensal (mais entradas) ou anual (mais caixa, menos churn). Ofereça os dois quando der.
6. Confira a equação de valor de cada ciclo com [`value-equation`](../../frameworks/value-equation.md): cada cobrança entrega valor, ou sai.
7. Modele LTV, churn-alvo e payback com [`lib/utilities/roi-calculator.md`](../../lib/utilities/roi-calculator.md) e [`money-model-sequence`](../../frameworks/money-model-sequence.md).
8. Trave UMA Big Idea com [`power-of-one`](../../frameworks/power-of-one.md), monte o Offer Book Master e passe o ★ HARD STOP. Atualize o `offer-registry` e o `big-idea-registry`.

## Artefatos Produzidos
- `artifact.offer-book-master` — o mapa-mestre da continuidade, aprovado no HARD STOP.
- `artifact.continuity-offer` — formato, gancho, motivo de ficar, ciclo de cobrança e desenho de churn.
- `artifact.unit-economics` — LTV, churn-alvo, payback e os cenários.
- `decision.big-idea-locked` — a tese do lançamento de continuidade.
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md), [`price-test-registry`](../../data/registries/price-test-registry.md), [`big-idea-registry`](../../data/registries/big-idea-registry.md).

## Gates
- ★ [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) — o HARD STOP. Bloqueia a copy.
- [`money-model/money-model-four-parts-gate`](../../checklists/money-model/money-model-four-parts-gate.md) — a continuidade ocupa o seu degrau na sequência.
- [`value/value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md) e [`unit-economics-checklist`](../../checklists/unit-economics-checklist.md).

## Critério de Saída
O Offer Book Master está completo; a oferta recorrente entrega valor que recorre de fato; o gancho, o motivo de ficar e o ciclo de cobrança estão definidos; a equação de valor de cada ciclo move alavanca; LTV, churn-alvo e payback estão modelados; UMA Big Idea está travada. O HARD STOP está verde. Só agora a copy pode nascer. A próxima fase é a [`02-retention-and-onboarding`](02-retention-and-onboarding.md), que recebe a oferta recorrente para desenhar o onboarding e o sistema de retenção que combatem o churn.
