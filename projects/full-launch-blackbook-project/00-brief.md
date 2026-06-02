---
id: project.full-launch-blackbook-project.00-brief
title: "Fase 00 — Brief, Escopo & Desenho do Pipeline (Full Launch)"
type: project-phase
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes:
  - briefing.raw-offer
  - template.core.offer-book-master
  - template.core.launch-blackbook-skeleton
produces:
  - decision.project-type
  - decision.scope-one-sentence
  - artifact.offer-book-master-skeleton
  - artifact.case-pipeline
  - artifact.handoff-contracts
tags: [project-phase, full-launch, blackbook, brief, escopo, pipeline, hard-stop, d0]
---

# Fase 00 — Brief, Escopo & Desenho do Pipeline (Full Launch)

## Objetivo da Fase
Transformar um briefing bruto num lançamento completo pronto para executar. Esta fase classifica o project type como full-launch, trava UMA frase de escopo e desenha o grafo de execução do composite `run-full-launch` — que encadeia o `run-offer-book` inteiro mais copy, funil, ops, eventos, afiliados, PR, compliance, blackbook e memória. O estado-pronto é o caso com tipo classificado, escopo único, esqueleto do Offer Book Master aberto e um DAG onde cada nó tem dono e cada aresta tem contrato. Aqui nascem os dois HARD STOPs do lançamento: o de entrada (Offer Book DoD, antes da copy) e o de saída (Blackbook DoD, antes da entrega).

## Critério de Entrada
Esta é a primeira fase do projeto. A entrada é o `briefing.raw-offer` com o mínimo de três campos: quem compra, qual a dor, qual a meta — mais, para um full-launch, a janela pretendida e a prova existente. Falta um campo mínimo, a fase devolve ao solicitante com perguntas objetivas. Pré-condição implícita do full-launch: a oferta tende a estar provada ou o mercado quente o bastante para justificar o lançamento completo (do contrário o chief recomenda um tier menor, como single-promo ou offer-book). O [`decision-registry`](../../data/registries/decision-registry.md) é lido para reusar decisões e o `lessons-learned-registry` para herdar lições de lançamentos passados.

## Agentes & Tasks
- **Task [`intake-and-scope`](../../tasks/planning/intake-and-scope.md)** — dono [`offerbook-chief`](../../agents/offerbook-chief.md). Classifica o tipo, trava o escopo, abre o esqueleto.
- **Task [`design-pipeline`](../../tasks/planning/design-pipeline.md)** — dono [`offer-squad-architect`](../../agents/offer-squad-architect.md). Desenha o DAG do `run-full-launch`, posiciona os gates e contrata os handoffs.

## Passos
1. Leia o briefing e confirme os campos mínimos. Falta um, devolva ao solicitante.
2. Reescreva o pedido em UMA frase de escopo com [`power-of-one`](../../frameworks/power-of-one.md): um avatar, uma promessa, um próximo passo.
3. Leia o terreno em alto nível com [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) para calibrar o tipo.
4. Gere ≥3 project types candidatos e pode até full-launch, com motivo e alternativas podadas — confirmando que a maturidade da oferta e o prazo comportam o lançamento completo.
5. Abra o esqueleto do Offer Book Master, preenchendo só tipo, nome de trabalho e data.
6. Passe os gates de comando [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md).
7. Monte o DAG do `run-full-launch`: as 12 tasks do offer-book seguidas das 14 do lançamento, cada uma com dono e contrato.
8. Posicione os dois ★ HARD STOPs: o `offer-book-stack/offer-book-dod-gate` entre D3 e D4 e o `blackbook-stack/blackbook-dod-gate` na saída. Nomeie o caminho crítico, confronte com a janela e registre a topologia no `decision-registry`.

## Artefatos Produzidos
- `decision.project-type` — full-launch, com motivo e alternativas podadas.
- `decision.scope-one-sentence` — a frase de escopo travada.
- `artifact.offer-book-master-skeleton` — o mapa-mestre aberto com os 10 blocos reservados.
- `artifact.case-pipeline` — o DAG do caso com os dois HARD STOPs e o caminho crítico.
- `artifact.handoff-contracts` — o contrato de cada aresta (campos + qualidade mínima + dono).
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) — existe UM tipo classificado com motivo.
- [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) — a frase de escopo é única e não bifurca.

## Critério de Saída
O tipo é full-launch, a frase de escopo não admite duas leituras, o esqueleto está aberto, o DAG é acíclico com os dois HARD STOPs posicionados e intransponíveis, e o caminho crítico cabe na janela. Os dois gates de comando estão verdes. A próxima fase é a [`01-offer-book`](01-offer-book.md), que incorpora o projeto Offer Book inteiro e roda o HARD STOP de entrada antes de qualquer copy.
