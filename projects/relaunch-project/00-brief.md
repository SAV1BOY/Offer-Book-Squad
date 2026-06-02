---
id: project.relaunch-project.00-brief
title: "Fase 00 — Brief & Escopo do Relançamento"
type: project-phase
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes:
  - briefing.raw-offer
  - template.core.offer-book-master
produces:
  - decision.project-type
  - decision.scope-one-sentence
  - artifact.relaunch-pipeline
  - artifact.prior-launch-inventory
  - artifact.handoff-contracts
tags: [project-phase, relaunch, brief, escopo, autopsia, pipeline, d0]
---

# Fase 00 — Brief & Escopo do Relançamento

## Objetivo da Fase
Enquadrar um relançamento e travar o que ele vai consertar. Um relançamento não começa do zero — começa de um histórico. Houve um lançamento antes, e ele teve resultado: vendeu menos do que devia, o controle cansou, a Big Idea perdeu força, ou a oferta envelheceu. Esta fase classifica o tipo como relaunch, trava UMA frase de escopo (o que vamos relançar e para quem) e inventaria o material do lançamento anterior — o que existe em archive, quais controles perderam, quais lições foram gravadas. O estado-pronto é o tipo classificado, a frase de escopo única, o inventário do lançamento anterior localizado e o pipeline de relançamento desenhado. A diferença desta trilha: ela começa com uma autópsia. Antes de refazer, entendemos por que o anterior não voou. Memória antes de repetição. E, como toda trilha, termina em compliance e ship.

## Critério de Entrada
A entrada é o `briefing.raw-offer` com os campos mínimos mais o contexto do histórico: qual oferta ou lançamento estamos relançando, qual foi o resultado anterior e qual a meta agora. Falta o histórico? A fase devolve pedindo o material do lançamento anterior — sem ele, não há autópsia, e sem autópsia o relançamento repete o erro. Pré-condição: existe um lançamento anterior com algum dado de resultado e ativos arquivados. O [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) e o [`control-registry`](../../data/registries/control-registry.md) são lidos para localizar as lições e os controles do passado.

## Agentes & Tasks
- **Task [`intake-and-scope`](../../tasks/planning/intake-and-scope.md)** — dono [`offerbook-chief`](../../agents/offerbook-chief.md). Classifica o tipo, trava o escopo.
- **Task [`design-pipeline`](../../tasks/planning/design-pipeline.md)** — dono [`offer-squad-architect`](../../agents/offer-squad-architect.md). Desenha o pipeline de relançamento.

## Passos
1. Leia o briefing e confirme os campos mínimos mais o histórico. Falta o histórico? Devolva.
2. Reescreva o pedido em UMA frase de escopo com [`power-of-one`](../../frameworks/power-of-one.md): o que relançar, para quem, com qual próximo passo.
3. Localize o inventário do lançamento anterior: ativos em [`archive/losing-controls`](../../archive/losing-controls), [`archive/past-launches`](../../archive/past-launches) e [`archive/retired-big-ideas`](../../archive/retired-big-ideas).
4. Confirme o fit da trilha: há um lançamento anterior com dados e ativos. Caso contrário, pode ser um lançamento novo, não um relançamento.
5. Passe os gates de comando [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md).
6. Desenhe o pipeline de relançamento: autópsia → refresh de oferta/Big Idea → nova copy e funil → compliance e ship. Cada nó com dono.
7. Posicione o HARD STOP [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) antes da nova copy. Registre a topologia no [`decision-registry`](../../data/registries/decision-registry.md).

## Artefatos Produzidos
- `decision.project-type` — relaunch, com motivo e alternativas podadas.
- `decision.scope-one-sentence` — a frase de escopo travada.
- `artifact.relaunch-pipeline` — o pipeline de relançamento com gates e caminho crítico.
- `artifact.prior-launch-inventory` — o inventário dos ativos e dados do lançamento anterior.
- `artifact.handoff-contracts` — o contrato de cada aresta.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) — existe UM tipo classificado com motivo.
- [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) — a frase de escopo é única e não bifurca.

## Critério de Saída
O tipo está classificado como relaunch, a frase de escopo não admite duas leituras, o inventário do lançamento anterior está localizado, o pipeline é acíclico com o HARD STOP posicionado e o caminho crítico nomeado. Os dois gates de comando estão verdes. A próxima fase é a [`01-previous-launch-autopsy`](01-previous-launch-autopsy.md), que recebe o inventário para dissecar por que o lançamento anterior não atingiu a meta. Se a frase ainda bifurca, esta fase não fecha.
