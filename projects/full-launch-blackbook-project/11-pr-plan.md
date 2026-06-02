---
id: project.full-launch-blackbook-project.11-pr-plan
title: "Fase 11 — Plano de PR"
type: project-phase
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
consumes:
  - artifact.offer-book
  - artifact.big-idea
  - artifact.run-of-show
  - artifact.events-calendar
  - artifact.affiliate-program
produces:
  - artifact.pr-plan
  - decision.brand-angle
tags: [project-phase, growth, pr, marca, autoridade, buzz, angulo, kpis, d6]
---

# Fase 11 — Plano de PR

## Objetivo da Fase
Transformar o resultado do lançamento em capital de marca duradouro, através de um ângulo memorável e verdadeiro, e medi-lo com KPIs de marca. O estado-pronto é o plano de PR com ângulo memorável lastreado em fato verificável + mapa de canais + ativos + KPIs de marca, onde o ângulo estende a Big Idea (não cria tese paralela) e a prova social é consentida — aprovado no pr-plan-checklist. A regra eliminatória: sem um fato lastreado não se cria ângulo — PR sobre conquista inventada destrói a marca e cai no veto de compliance. Esta fase fecha a camada D6 e prepara o material para a barreira final de compliance.

## Critério de Entrada
A Fase 01 entrega o `artifact.offer-book` e a `artifact.big-idea` (a tese que o ângulo estende, sem contradizer). A Fase 08 entrega o `artifact.run-of-show` e a Fase 09 o `artifact.events-calendar` (o que aconteceu e quando — a matéria cronológica). A Fase 10 entrega o `artifact.affiliate-program` (os parceiros de topo, que são multiplicadores de PR). As provas e resultados vêm via offer-book e registries (os fatos lastreados). Pré-condição: existe pelo menos um fato lastreado digno de pauta — número de resultado, caso com consentimento, marco verificável. Sem nenhum, a fase diz isso e recomenda construir o ativo primeiro. O [`decision-registry`](../../data/registries/decision-registry.md) é escrito.

## Agentes & Tasks
- **Task [`build-pr-plan`](../../tasks/growth/build-pr-plan.md)** — dono [`pr-brand-strategist`](../../agents/pr-brand-strategist.md). O guardião do halo do lançamento. Sem poder de veto, mas recusa publicar narrativa sobre conquista inventada.

## Passos
1. Inventarie os fatos lastreados: números de resultado, casos com consentimento, endossos com permissão, marcos verificáveis. Sem nenhum, pare e recomende construir o ativo.
2. Gere o ângulo memorável com Tree-of-Thoughts (≥3 ângulos de fontes de prova diferentes) via [`launch/pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md); a veracidade/lastro é critério eliminatório.
3. Confirme o fit com a Big Idea: o ângulo estende a tese travada; ângulo que cria tese paralela é realinhado.
4. Mapeie os canais com Tree-of-Thoughts (≥3 focos — mídia ganha, autoridade do fundador, prova social interna); inclua os parceiros do Dream 100 como canal.
5. Defina os ativos de PR: press angle, estudo de caso (com consentimento), conteúdo de autoridade, depoimento de terceiro — cada um lastreado e consentido.
6. Defina os KPIs de marca: menções ganhas, share of voice, crescimento de audiência, lift de prova social, sentimento — halo mensurável, nunca vaidade pura.
7. Self-verify com red-team: cada ângulo tem fato verificável + consentimento? Um jornalista checaria e o fato se sustenta? Antecipe o veto do compliance (caso sem consentimento, número inflado, endosso sem permissão).
8. Registre o ângulo escolhido (e os podados, com o fato que os lastreava), os canais e os KPIs no `decision-registry`.

## Artefatos Produzidos
- `artifact.pr-plan` — ângulo memorável + fato que o lastreia + como estende a Big Idea + canais/cadência + ativos + KPIs de marca.
- `decision.brand-angle` — o ângulo escolhido, os podados e o foco de canal.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`pr-plan-checklist`](../../checklists/pr-plan-checklist.md)

## Critério de Saída
Existe pelo menos um fato lastreado por trás do ângulo (zero PR sobre conquista inventada); o ângulo é verificável e consentido e estende a Big Idea travada; o mapa de canais e a cadência pós-cart estão definidos; os ativos de PR estão cada um lastreado e consentido; os KPIs de marca são mensuráveis; o pr-plan-checklist está verde e o ângulo está registrado. Fecha a camada D6. A próxima fase é a [`12-compliance-and-blackbook-assembly`](12-compliance-and-blackbook-assembly.md), que roda a auditoria final de compliance e monta o Blackbook no ★ HARD STOP de saída.
