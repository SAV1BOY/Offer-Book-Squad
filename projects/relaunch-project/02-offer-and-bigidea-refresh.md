---
id: project.relaunch-project.02-offer-and-bigidea-refresh
title: "Fase 02 — Refresh de Oferta & Big Idea (HARD STOP)"
type: project-phase
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes:
  - artifact.failure-diagnosis
  - decision.what-to-keep-kill-change
  - template.core.offer-book-master
produces:
  - artifact.offer-book-master
  - artifact.refreshed-mechanism
  - artifact.refreshed-money-model
  - decision.big-idea-locked
tags: [project-phase, relaunch, offer-refresh, big-idea, hard-stop, mecanismo, money-model, d3]
---

# Fase 02 — Refresh de Oferta & Big Idea (HARD STOP)

## Objetivo da Fase
Renovar a oferta e a Big Idea sobre o que sobreviveu à autópsia, e fechar o HARD STOP. Esta fase não recomeça do zero nem repete o passado — ela conserta com precisão. O diagnóstico apontou a causa-raiz; agora agimos sobre ela. Se a oferta era fraca, fortalecemos o stack e a garantia. Se a Big Idea cansou, geramos UMA nova, calibrada à sofisticação que subiu. Se o mecanismo virou genérico, renomeamos e reprovamos. O estado-pronto é o Offer Book Master atualizado, o mecanismo renovado, o money model revisado e UMA Big Idea travada — tudo passando no Definition of Done. Nenhuma nova copy nasce antes deste verde. É a mesma regra Agora aplicada ao relançamento: a oferta nova vem antes da persuasão nova. O que ganhou antes é reusado; o que perdeu é substituído com motivo.

## Critério de Entrada
A [`01-previous-launch-autopsy`](01-previous-launch-autopsy.md) entrega o `artifact.failure-diagnosis` e a decisão do que manter, matar e mudar. Pré-condição: a causa-raiz da falha anterior está nomeada com evidência. Se a autópsia não isolou a causa, esta fase não age no escuro — devolve para fechar o diagnóstico. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para reusar a oferta que sobreviveu; o [`big-idea-registry`](../../data/registries/big-idea-registry.md) recebe a nova tese; o [`control-registry`](../../data/registries/control-registry.md) traz o que ganhou antes.

## Agentes & Tasks
- **Tasks de arquitetura** — [`define-mechanism`](../../tasks/offer-architecture/define-mechanism.md), [`score-value-equation`](../../tasks/offer-architecture/score-value-equation.md), [`design-money-model`](../../tasks/offer-architecture/design-money-model.md). Donos: [`mechanism-architect`](../../agents/mechanism-architect.md), [`value-equation-engineer`](../../agents/value-equation-engineer.md), [`money-model-designer`](../../agents/money-model-designer.md).
- **Task [`generate-big-ideas`](../../tasks/big-idea/generate-big-ideas.md)** — dono [`big-idea-architect`](../../agents/big-idea-architect.md).
- **Task [`assemble-offer-book`](../../tasks/assembly/assemble-offer-book.md)** — donos [`offerbook-chief`](../../agents/offerbook-chief.md) e [`compliance-auditor`](../../agents/compliance-auditor.md). Fecha o HARD STOP.

## Passos
1. Aja sobre a causa-raiz do diagnóstico, não sobre tudo: conserte o que quebrou, mantenha o que ganhou.
2. Se a oferta era fraca, refaça o stack com [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) e fortaleça a garantia com [`guarantee-design`](../../frameworks/guarantee-design.md).
3. Se o mecanismo virou genérico, renomeie e reprove com [`unique-mechanism.md`](../../frameworks/unique-mechanism.md): por que desta vez é diferente.
4. Repontue a equação de valor com [`value-equation`](../../frameworks/value-equation.md): nenhuma alavanca órfã na oferta renovada.
5. Revise o money model com [`money-model-sequence`](../../frameworks/money-model-sequence.md): a sequência que falhou ganha o degrau que faltava.
6. Se a Big Idea cansou, gere UMA nova com [`big-idea-generator`](../../frameworks/big-idea-generator.md) e [`power-of-one`](../../frameworks/power-of-one.md), calibrada à nova sofisticação. Múltiplas ideias = reprovação.
7. Confira que a nova tese é nova, grande e crível — e que não repete o ângulo aposentado.
8. Monte o Offer Book Master atualizado e passe o ★ HARD STOP. Atualize o `offer-registry` e o `big-idea-registry`.

## Artefatos Produzidos
- `artifact.offer-book-master` — o mapa-mestre atualizado, aprovado no HARD STOP.
- `artifact.refreshed-mechanism` — o mecanismo renomeado ou reforçado.
- `artifact.refreshed-money-model` — a sequência revisada.
- `decision.big-idea-locked` — a nova tese travada (ou a anterior confirmada com motivo).
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md), [`big-idea-registry`](../../data/registries/big-idea-registry.md).

## Gates
- ★ [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) — o HARD STOP. Bloqueia a nova copy.
- [`big-idea/big-idea-new-big-credible-gate`](../../checklists/big-idea/big-idea-new-big-credible-gate.md) — a tese é nova, grande e crível.
- [`value/value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md) e [`chief/chief-offer-book-readiness-gate`](../../checklists/chief/chief-offer-book-readiness-gate.md).

## Critério de Saída
O Offer Book Master está atualizado; a ação atacou a causa-raiz; o mecanismo está renovado se preciso; a equação de valor não tem alavanca órfã; o money model ganhou o que faltava; UMA Big Idea está travada e não repete o ângulo aposentado. O HARD STOP está verde. Só agora a nova copy pode nascer. A próxima fase é a [`03-new-copy-and-funnel`](03-new-copy-and-funnel.md), que recebe o Offer Book renovado para reescrever a copy e remontar o funil sem os pontos de sangramento do anterior.
