---
id: project.continuity-launch-project.02-retention-and-onboarding
title: "Fase 02 — Retenção & Onboarding"
type: project-phase
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes:
  - artifact.continuity-offer
  - artifact.unit-economics
  - artifact.offer-book-master
produces:
  - artifact.onboarding-flow
  - artifact.retention-system
  - artifact.churn-playbook
tags: [project-phase, continuity, retencao, onboarding, churn, ltv, ops, d6]
---

# Fase 02 — Retenção & Onboarding

## Objetivo da Fase
Desenhar o onboarding que entrega a primeira vitória rápido e o sistema que mantém o cliente pagando. A continuidade não se ganha na venda — se ganha na retenção. Um cliente que não vê valor no primeiro ciclo cancela, e o churn devora o LTV que a Fase 01 modelou. Esta fase desenha o fluxo de onboarding (a primeira vitória nos primeiros dias), o sistema de retenção (o ritmo de valor que justifica a próxima cobrança) e o playbook de churn (como prevenir, detectar e recuperar cancelamentos). O estado-pronto é o fluxo de onboarding mapeado com o momento "aha" definido, o sistema de retenção com os marcos de valor por ciclo e o playbook de churn com os gatilhos de risco e as ações de salvamento. Onboarding fraco é churn garantido. Aqui o primeiro ciclo é desenhado para provar o valor antes de a primeira renovação chegar.

## Critério de Entrada
A [`01-continuity-offer-design`](01-continuity-offer-design.md) entrega a `artifact.continuity-offer` e o `artifact.unit-economics` com o churn-alvo. Pré-condição: a oferta recorrente está desenhada com o motivo de ficar definido e o churn-alvo travado. Se o motivo de ficar é vago, o sistema de retenção não tem o que reforçar — a fase devolve à Fase 01. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para a oferta recorrente; o [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) traz lições de retenção de lançamentos anteriores.

## Agentes & Tasks
- **Task [`design-money-model`](../../tasks/offer-architecture/design-money-model.md)** — dono [`money-model-designer`](../../agents/money-model-designer.md), responsável pelo desenho de churn da continuidade.
- **Task [`build-events-logistics`](../../tasks/ops/build-events-logistics.md)** — dono [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md), para o calendário de valor recorrente e a logística de onboarding.

## Passos
1. Defina o momento "aha" do primeiro ciclo: a primeira vitória que prova o valor, e quão rápido o cliente chega nela.
2. Mapeie o fluxo de onboarding com os padrões de [`lib/patterns/continuity-patterns.md`](../../lib/patterns/continuity-patterns.md): os passos dos primeiros dias até o "aha".
3. Desenhe o sistema de retenção com [`money-model-designer/continuity-design`](../../frameworks/money-model-designer/continuity-design.md): os marcos de valor que justificam cada renovação.
4. Monte o calendário de valor recorrente: o que o cliente recebe de novo a cada ciclo, na cadência da cobrança.
5. Construa o playbook de churn: os gatilhos de risco (uso caindo, ciclo sem login), a detecção e as ações de salvamento.
6. Desenhe a recuperação de cobrança falha (dunning): cartão recusado não pode virar churn silencioso.
7. Ancore o anti-churn no valor que se acumula — rede, progresso, biblioteca viva — para a saída doer mais que a permanência.
8. Cruze tudo com o churn-alvo da Fase 01. Atualize o `offer-registry` e as lições.

## Artefatos Produzidos
- `artifact.onboarding-flow` — o fluxo dos primeiros dias com o momento "aha" definido.
- `artifact.retention-system` — os marcos de valor por ciclo e o calendário de valor recorrente.
- `artifact.churn-playbook` — os gatilhos de risco, a detecção, as ações de salvamento e o dunning.
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md), [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md).

## Gates
- [`events-logistics-checklist`](../../checklists/events-logistics-checklist.md) — o calendário de valor recorrente está completo.
- [`money-model/money-model-sequence-gate`](../../checklists/money-model/money-model-sequence-gate.md) — o valor por ciclo segue a cadência da cobrança.

## Critério de Saída
O momento "aha" está definido e o onboarding leva o cliente até ele rápido; o sistema de retenção tem marcos de valor por ciclo; o playbook de churn cobre prevenção, detecção, salvamento e dunning; o anti-churn está ancorado no valor que se acumula; tudo bate com o churn-alvo. Os gates estão verdes; os registries estão atualizados. A próxima fase é a [`03-copy-and-sequence`](03-copy-and-sequence.md), que recebe a oferta recorrente, o onboarding e a retenção para escrever a copy de venda e as sequências de boas-vindas e de retenção.
