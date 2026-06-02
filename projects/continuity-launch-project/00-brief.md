---
id: project.continuity-launch-project.00-brief
title: "Fase 00 — Brief & Escopo do Lançamento de Continuidade"
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
  - artifact.continuity-pipeline
  - artifact.recurring-value-hypothesis
  - artifact.handoff-contracts
tags: [project-phase, continuity, brief, escopo, recorrente, ltv, churn, d0]
---

# Fase 00 — Brief & Escopo do Lançamento de Continuidade

## Objetivo da Fase
Enquadrar um lançamento de continuidade e travar o valor recorrente que ele vai entregar. Continuidade é onde mora o LTV e a previsibilidade — a receita que paga mês após mês: assinatura, comunidade, consumível, manutenção. Mas ela só funciona com valor recorrente real, não com acesso passivo a um arquivo. Esta fase classifica o tipo como continuity-launch, trava UMA frase de escopo (o que o cliente recebe de novo a cada ciclo) e levanta a hipótese de valor recorrente. O estado-pronto é o tipo classificado, a frase de escopo única, a hipótese de valor recorrente declarada e o pipeline desenhado. A pergunta-mãe desta trilha: o que o cliente precisa de novo a cada ciclo? Se a resposta é "nada — ele já recebeu tudo na primeira entrega", não há continuidade verdadeira. Como toda trilha, termina em compliance e ship.

## Critério de Entrada
A entrada é o `briefing.raw-offer` com os campos mínimos mais o contexto de recorrência: o que se quer cobrar de forma recorrente, sobre qual base (produto-núcleo já vendido?) e qual a meta de LTV ou de churn. Falta um? A fase devolve com perguntas objetivas. Pré-condição: existe um produto ou serviço que permite valor contínuo, e um público que já compra ou compraria o núcleo. Se o produto se resolve numa única entrega, cobrar recorrente gera churn e reembolso — o tipo pode não ser continuity. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para reusar a oferta-núcleo; o [`decision-registry`](../../data/registries/decision-registry.md) checa decisões anteriores.

## Agentes & Tasks
- **Task [`intake-and-scope`](../../tasks/planning/intake-and-scope.md)** — dono [`offerbook-chief`](../../agents/offerbook-chief.md). Classifica o tipo, trava o escopo.
- **Task [`design-pipeline`](../../tasks/planning/design-pipeline.md)** — dono [`offer-squad-architect`](../../agents/offer-squad-architect.md). Desenha o pipeline de continuidade.

## Passos
1. Leia o briefing e confirme os campos mínimos mais o contexto de recorrência. Falta um? Devolva.
2. Reescreva o pedido em UMA frase de escopo com [`power-of-one`](../../frameworks/power-of-one.md): o que o cliente recebe de novo a cada ciclo.
3. Levante a hipótese de valor recorrente: o que recorre de fato — acompanhamento, atualização, comunidade, insumo, suporte.
4. Confirme o fit da trilha: há valor que recorre e uma base de clientes do núcleo. Caso contrário, reencaminhe.
5. Passe os gates de comando [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md).
6. Desenhe o pipeline de continuidade: desenho da oferta recorrente → retenção e onboarding → copy e sequência → compliance e ship. Cada nó com dono.
7. Posicione o HARD STOP [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) antes da copy. Registre a topologia no [`decision-registry`](../../data/registries/decision-registry.md).

## Artefatos Produzidos
- `decision.project-type` — continuity-launch, com motivo e alternativas podadas.
- `decision.scope-one-sentence` — a frase de escopo travada.
- `artifact.continuity-pipeline` — o pipeline com gates e caminho crítico.
- `artifact.recurring-value-hypothesis` — a hipótese do que recorre a cada ciclo.
- `artifact.handoff-contracts` — o contrato de cada aresta.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) — existe UM tipo classificado com motivo.
- [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) — a frase de escopo é única e não bifurca.

## Critério de Saída
O tipo está classificado como continuity-launch, a frase de escopo não admite duas leituras, a hipótese de valor recorrente está declarada, o pipeline é acíclico com o HARD STOP posicionado e o caminho crítico nomeado. Os dois gates de comando estão verdes. A próxima fase é a [`01-continuity-offer-design`](01-continuity-offer-design.md), que recebe a hipótese para desenhar a oferta recorrente, a economia e o controle de churn. Se a frase ainda bifurca, esta fase não fecha.
