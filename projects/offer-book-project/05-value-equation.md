---
id: project.offer-book-project.05-value-equation
title: "Fase 05 — Equação de Valor"
type: project-phase
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
consumes:
  - artifact.mechanism-sheet
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - artifact.offer-registry-state
produces:
  - artifact.value-equation-scorecard
  - decision.lever-assignment
tags: [project-phase, offer-architecture, value-equation, alavancas, sonho, tempo, esforco, veto, d2]
---

# Fase 05 — Equação de Valor

## Objetivo da Fase
Maximizar (Sonho × Probabilidade) / (Tempo × Esforço) provando, para cada componente da oferta, qual alavanca ele move, em que direção e com qual evidência. O estado-pronto é o ponto em que nenhuma das quatro alavancas fica abandonada, nenhum componente órfão sobrevive e o produto da equação é defensável sem inflar o Sonho. Esta fase tem poder de veto sobre componentes e claims — é o HARD STOP do componente. O scorecard que ela entrega diz ao pricing quanto valor cada alavanca carrega e ao money model onde alocar cada peça.

## Critério de Entrada
A Fase 04 entrega o `artifact.mechanism-sheet` provado (as alavancas que o mecanismo já move, para não duplicar e para amplificar). As Fases 02 entregam o avatar e o VOC (o Sonho real na linguagem do avatar, os medos que derrubam a Probabilidade, os sacrifícios temidos). O `artifact.offer-registry-state` traz a lista corrente de componentes a auditar. Pré-condição: o mechanism-sheet está provado, não provisório — o valor se ancora no mecanismo. Se o mecanismo ainda é provisório, marco o scorecard como condicional e bloqueio só os componentes que dependem do elo não-provado. Se a lista vier sem o resultado-alvo de cada componente, devolvo pedindo o "para quê". O [`offer-registry`](../../data/registries/offer-registry.md) é a fonte que esta fase escreve.

## Agentes & Tasks
- **Task [`score-value-equation`](../../tasks/offer-architecture/score-value-equation.md)** — dono [`value-equation-engineer`](../../agents/value-equation-engineer.md). O engenheiro do valor percebido. Tem poder de veto sobre componentes e claims.

## Passos
1. Mapeie e amplifique o Sonho com [`dream-outcome-amplification`](../../frameworks/value-equation-engineer/dream-outcome-amplification.md): amplificado e crível. Sonho inflado sem Probabilidade destrói valor.
2. Suba a Probabilidade percebida com prova, garantia e mecanismo, usando [`value-equation`](../../frameworks/value-equation.md) como fórmula-mestra.
3. Comprima o Tempo com [`time-delay-compression`](../../frameworks/value-equation-engineer/time-delay-compression.md): traga o primeiro resultado para mais cedo.
4. Reduza o Esforço com [`effort-sacrifice-reduction`](../../frameworks/value-equation-engineer/effort-sacrifice-reduction.md): feito-por-você, atalhos, remoção do trabalho temido.
5. Audite cada componente contra as 4 alavancas: declare alavanca-alvo e direção. Delta líquido zero ou negativo vira órfão e recebe veto até reposicionar ou cortar.
6. Resolva ambiguidade com Tree-of-Thoughts: ≥3 enquadramentos pontuados por delta, custo, risco de credibilidade e sinergia.
7. Vete o claim inacreditável: promessa que infla o Sonho mas gera descrença derruba o produto da equação.
8. Reavalie o scorecard inteiro: nenhuma alavanca abandonada, nenhum órfão. Registre no `offer-registry`, marque value_equation_pass e passe o gate.

## Artefatos Produzidos
- `artifact.value-equation-scorecard` — leitura das 4 alavancas, componentes mapeados (id, alavanca, direção, delta, veredito), vetos, value_equation_pass.
- `decision.lever-assignment` — a alavanca dominante e a atribuição por componente.
- Registry escrito: [`offer-registry`](../../data/registries/offer-registry.md).

## Gates
- [`value/value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md) — nenhuma alavanca abandonada, nenhum componente órfão.

## Critério de Saída
Cada componente mapeia ≥1 alavanca com direção declarada; nenhuma das 4 alavancas está abandonada; nenhum componente órfão sobrevive; o produto da equação é defensável; o gate está verde; vetos e overrides estão registrados. A próxima fase é a [`06-money-model`](06-money-model.md), que recebe o scorecard para alocar cada componente ao degrau certo da escada — o acelerador de Tempo vira upsell, o redutor de Esforço entra no núcleo.
