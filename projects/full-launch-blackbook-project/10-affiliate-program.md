---
id: project.full-launch-blackbook-project.10-affiliate-program
title: "Fase 10 — Programa de Afiliados"
type: project-phase
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
consumes:
  - artifact.offer-book
  - artifact.money-model
  - artifact.unit-economics-sheet
  - artifact.run-of-show
  - artifact.events-calendar
produces:
  - artifact.affiliate-program
  - artifact.affiliate-prizes
  - artifact.affiliate-blackbook
tags: [project-phase, growth, afiliados, jv, dream-100, leaderboard, prizes, disclosure, d6]
---

# Fase 10 — Programa de Afiliados

## Objetivo da Fase
Desenhar um programa de afiliados onde a economia fecha, os parceiros certos são recrutados, e cada um recebe um funil pronto para promover sem fricção. O estado-pronto é cohorts + estrutura de prêmios dentro do teto da unit economics + funil de afiliado + leaderboard + affiliate blackbook, com disclosure de afiliação em toda peça de swipe e escassez de fechamento verdadeira — aprovado no affiliate-program-checklist. A regra inegociável: a comissão sai do que a unit economics permite, nunca de uma margem que não existe; comissão que inverte o LTV:CAC não é publicada.

## Critério de Entrada
A Fase 07 do offer-book (incorporada na Fase 01) entrega o `artifact.unit-economics-sheet` — LTV, CAC, payback, margem por venda — que define o teto de comissão. A Fase 01 entrega o `artifact.money-model` (sobre o que a comissão incide) e o `artifact.offer-book` (a Big Idea, a prova e os ângulos — a matéria do swipe). A Fase 08 entrega o `artifact.run-of-show` e a Fase 09 o `artifact.events-calendar` (as janelas em que afiliados entram e os eventos que ancoram a competição). Pré-condição: a unit economics está conhecida — sem saber quanto vale um cliente, qualquer percentual é chute que pode quebrar a margem. Comissão que inverte a economia volta ao unit-economics-stack-analyst e ao money-model-designer. O [`decision-registry`](../../data/registries/decision-registry.md) é escrito.

## Agentes & Tasks
- **Task [`build-affiliate-program`](../../tasks/growth/build-affiliate-program.md)** — dono [`affiliate-program-architect`](../../agents/affiliate-program-architect.md). O general do exército de afiliados. Sem poder de veto, mas recusa publicar o que quebra a economia.

## Passos
1. Confirme o teto econômico: leia LTV/CAC/payback. Unit economics não fechada, pare.
2. Defina as cohorts: Dream 100 de topo (bônus + co-marketing), lista média (comissão padrão + prêmios), micro/embaixadores (comissão + reconhecimento).
3. Estruture comissão e prêmios com Tree-of-Thoughts (≥3 modelos — linear, tiered, flat + leaderboard) via [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md); pode os que estouram o teto.
4. Foque o recrutamento com Tree-of-Thoughts (≥3 estratégias — poucos gigantes, médios, enxame de micro); pode a de risco de concentração alto.
5. Construa o funil de afiliado: recrutamento → onboarding com as datas das fases → área com links rastreáveis + swipe (dos ângulos do Offer Book, em redação original) + e-mails por fase → reporte.
6. Desenhe o leaderboard: competição ao vivo com prêmios por ranking, com critério de qualidade/reembolso para não incentivar promessa enganosa.
7. Garanta a disclosure de afiliação (FTC/CDC) em cada peça de swipe; a escassez de fechamento segue [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md) e tem de ser verdadeira.
8. Empacote o affiliate blackbook (datas, links, swipe original, regras, disclosure, FAQ); self-verify com red-team (após pagar afiliados, o LTV:CAC continua saudável?); registre no `decision-registry`.

## Artefatos Produzidos
- `artifact.affiliate-program` — comissão por degrau, cohorts, funil de afiliado.
- `artifact.affiliate-prizes` — estrutura de prêmios e regras do leaderboard.
- `artifact.affiliate-blackbook` — datas, links, swipe original, regras, disclosure, FAQ.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md) (o blackbook referencia o [`swipe-registry`](../../data/registries/swipe-registry.md)).

## Gates
- [`affiliate-program-checklist`](../../checklists/affiliate-program-checklist.md)

## Critério de Saída
A unit economics foi usada como teto antes de definir percentuais; comissão + prêmios cabem no teto (LTV:CAC saudável após pagar afiliados); as cohorts estão definidas; o funil de afiliado está pronto para promover (links, swipe, datas, disclosure); a disclosure está presente em toda peça; o swipe de fechamento usa escassez verdadeira; o leaderboard motiva volume sem incentivar engano; o affiliate-program-checklist está verde. A próxima fase é a [`11-pr-plan`](11-pr-plan.md), que recebe os parceiros de topo que também geram PR e co-marketing.
