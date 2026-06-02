---
id: project.offer-book-project.00-brief
title: "Fase 00 — Brief, Escopo & Desenho do Pipeline"
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
  - artifact.offer-book-master-skeleton
  - artifact.case-pipeline
  - artifact.handoff-contracts
tags: [project-phase, offer-book, brief, escopo, pipeline, hard-stop, d0]
---

# Fase 00 — Brief, Escopo & Desenho do Pipeline

## Objetivo da Fase
Transformar um briefing bruto de oferta em um caso pronto para executar. Esta fase recebe o pedido cru, classifica UM project type, trava UMA frase de escopo e desenha o grafo de execução do caso. O estado-pronto é simples: existe um tipo de projeto com motivo, uma frase de escopo que não admite duas leituras, o esqueleto do Offer Book Master aberto e um DAG onde cada nó tem dono e cada aresta tem contrato. Aqui também nasce o HARD STOP: nenhuma copy começa antes do Offer Book passar no Definition of Done na Fase 09.

## Critério de Entrada
Esta é a primeira fase do projeto. A entrada é o `briefing.raw-offer` — o pedido cru do solicitante com o mínimo de três campos: quem compra, qual a dor, qual a meta. Se faltar qualquer um, a fase não prossegue e devolve ao solicitante com três perguntas objetivas. O [`decision-registry`](../../data/registries/decision-registry.md) é lido para checar se já existe decisão sobre este caso (memória antes de repetição).

## Agentes & Tasks
- **Task [`intake-and-scope`](../../tasks/planning/intake-and-scope.md)** — dono [`offerbook-chief`](../../agents/offerbook-chief.md). Classifica o tipo, trava o escopo, abre o esqueleto.
- **Task [`design-pipeline`](../../tasks/planning/design-pipeline.md)** — dono [`offer-squad-architect`](../../agents/offer-squad-architect.md). Desenha o DAG, posiciona os gates, contrata os handoffs.

## Passos
1. Leia o briefing e confirme os três campos mínimos. Falta um? Devolva ao solicitante.
2. Reescreva o pedido em UMA frase de escopo com [`power-of-one`](../../frameworks/power-of-one.md): um avatar, uma promessa, um próximo passo.
3. Leia o terreno em alto nível com [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) para calibrar o tipo.
4. Gere ≥3 project types candidatos e pode até UM, com motivo e alternativas podadas.
5. Abra o esqueleto do Offer Book Master, preenchendo só tipo, nome de trabalho e data.
6. Passe os gates de comando [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md).
7. Monte o DAG do composite `run-offer-book`: cada task com dono, cada aresta com contrato, gates posicionados nas junções.
8. Posicione o ★ HARD STOP [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) entre D3 e D4. Nenhuma aresta de copy o contorna.
9. Nomeie o caminho crítico e confronte com o prazo. Registre a topologia e as decisões no `decision-registry`.

## Artefatos Produzidos
- `decision.project-type` — um dos 7 tipos, com motivo e alternativas podadas.
- `decision.scope-one-sentence` — a frase de escopo travada.
- `artifact.offer-book-master-skeleton` — o mapa-mestre aberto com os 10 blocos reservados.
- `artifact.case-pipeline` — o DAG do caso com gates e caminho crítico.
- `artifact.handoff-contracts` — o contrato de cada aresta (campos + qualidade mínima + dono).
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) — existe UM tipo classificado com motivo.
- [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) — a frase de escopo é única e não bifurca.

## Critério de Saída
O tipo está classificado, a frase de escopo não admite duas leituras, o esqueleto do Offer Book Master está aberto, o DAG é acíclico com todos os gates posicionados, o HARD STOP é intransponível e o caminho crítico cabe no prazo. Os dois gates de comando estão verdes. A próxima fase é a [`01-market-intel`](01-market-intel.md), que recebe o mercado-alvo recortado e a posição no DAG. Se a frase ainda bifurca, esta fase não fecha.
