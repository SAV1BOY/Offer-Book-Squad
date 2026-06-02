---
id: project.enterprise-deal-book-project.00-brief
title: "Fase 00 — Brief & Escopo do Deal Book Enterprise"
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
  - artifact.account-icp-sketch
  - artifact.deal-book-pipeline
  - artifact.handoff-contracts
tags: [project-phase, enterprise, deal-book, b2b, escopo, meddic, dmu, d0]
---

# Fase 00 — Brief & Escopo do Deal Book Enterprise

## Objetivo da Fase
Enquadrar um caso de venda enterprise e travar o que o deal book vai provar. B2B não é B2C com gravata. Aqui ninguém compra sozinho: decide um comitê, o ciclo é longo, o ticket é alto e o risco não é falar pouco — é investir meses num negócio que nunca ia fechar. Esta fase classifica o tipo como enterprise-deal-book, trava UMA frase de escopo (qual conta ou segmento, qual transformação, qual próximo passo de venda) e esboça o ICP da conta. O estado-pronto é o tipo classificado, a frase de escopo única, o esboço de ICP da conta-alvo e o pipeline B2B desenhado. A malha de qualificação MEDDPICC já começa a guiar: qual a métrica que justifica a compra, quem assina o cheque, como o comitê decide. Este caso usa o fluxo B2B inteiro — DMU, business case e battle cards — e termina em compliance e handoff de vendas.

## Critério de Entrada
A entrada é o `briefing.raw-offer` com os campos mínimos do contexto enterprise: qual conta ou segmento, qual a dor de negócio, qual a meta (tamanho do contrato, ciclo-alvo) e o que se sabe do comitê comprador. Falta um? A fase devolve com perguntas objetivas. Pré-condição: existe uma solução real para vender a empresas e um recorte de conta ou vertical, não "qualquer empresa". Se o caso é uma venda transacional de decisor único, o tipo não é enterprise — esta trilha existe para comitês. O [`decision-registry`](../../data/registries/decision-registry.md) é lido para reusar decisões de contas semelhantes.

## Agentes & Tasks
- **Task [`intake-and-scope`](../../tasks/planning/intake-and-scope.md)** — dono [`offerbook-chief`](../../agents/offerbook-chief.md). Classifica o tipo, trava o escopo.
- **Task [`design-pipeline`](../../tasks/planning/design-pipeline.md)** — dono [`offer-squad-architect`](../../agents/offer-squad-architect.md). Desenha o pipeline B2B.

## Passos
1. Leia o briefing e confirme os campos mínimos do contexto enterprise. Falta um? Devolva.
2. Reescreva o pedido em UMA frase de escopo com [`power-of-one`](../../frameworks/power-of-one.md): conta/segmento, transformação, próximo passo de venda.
3. Esboce o ICP da conta-alvo: porte, vertical, gatilho de compra, sinais de comitê (orçamento, segurança, jurídico).
4. Confirme o fit B2B: há comitê, ticket alto e ciclo longo. Caso contrário, reencaminhe.
5. Passe os gates de comando [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md).
6. Desenhe o pipeline `run-enterprise-deal-book`: inteligência → arquitetura de valor → posicionamento → deal deck → compliance. Cada nó com dono.
7. Posicione o HARD STOP [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) antes do deal deck. Registre a topologia no [`decision-registry`](../../data/registries/decision-registry.md).

## Artefatos Produzidos
- `decision.project-type` — enterprise-deal-book, com motivo e alternativas podadas.
- `decision.scope-one-sentence` — a frase de escopo travada.
- `artifact.account-icp-sketch` — o esboço de ICP da conta com sinais de comitê.
- `artifact.deal-book-pipeline` — o pipeline B2B com gates e caminho crítico.
- `artifact.handoff-contracts` — o contrato de cada aresta.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) — existe UM tipo classificado com motivo.
- [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) — a frase de escopo é única e não bifurca.

## Critério de Saída
O tipo está classificado como enterprise-deal-book, a frase de escopo não admite duas leituras, o ICP da conta está esboçado com sinais de comitê, o pipeline B2B é acíclico com o HARD STOP posicionado e o caminho crítico nomeado. Os dois gates de comando estão verdes. A próxima fase é a [`01-icp-and-dmu`](01-icp-and-dmu.md), que recebe o esboço de ICP para mapear a unidade de decisão de compra papel por papel. Se a frase ainda bifurca, esta fase não fecha.
