---
id: project.single-promo-project.00-brief
title: "Fase 00 — Brief & Escopo da Promo Enxuta"
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
  - artifact.promo-pipeline
  - artifact.handoff-contracts
tags: [project-phase, single-promo, brief, escopo, pipeline, tier-1, hard-stop, d0]
---

# Fase 00 — Brief & Escopo da Promo Enxuta

## Objetivo da Fase
Transformar um pedido de promoção rápida num caso enxuto pronto para executar. Esta é a Tier 1 do squad: um caminho curto que vai do briefing à promoção no ar com o mínimo de peso. O alvo é UMA oferta, UM público, UM canal principal. A fase recebe o pedido cru, confirma que cabe na trilha enxuta e trava UMA frase de escopo. O estado-pronto é simples: o tipo está classificado como single-promo, a frase de escopo não admite duas leituras, o esqueleto do Offer Book Master está aberto e o pipeline curto está desenhado. Aqui nasce o HARD STOP do caso: nenhuma copy começa antes do Offer Book passar no Definition of Done na [`01-offer-book-core`](01-offer-book-core.md). A promo é rápida, mas a oferta vem antes da persuasão. Single-promo não significa pular a oferta — significa montá-la enxuta, sem ops pesada, sem afiliados, sem PR.

## Critério de Entrada
Esta é a primeira fase do caso. A entrada é o `briefing.raw-offer` — o pedido cru com três campos mínimos: quem compra, qual a dor, qual a meta de receita e prazo. Falta um? A fase devolve ao solicitante com três perguntas objetivas. Pré-condição da trilha enxuta: existe uma oferta-base e um público recortado, e o prazo é curto. Se o briefing pede um lançamento completo com evento, afiliados e PR, o tipo não é single-promo e a fase reencaminha para a trilha cheia. O [`decision-registry`](../../data/registries/decision-registry.md) é lido para checar se já há decisão sobre este caso (memória antes de repetição).

## Agentes & Tasks
- **Task [`intake-and-scope`](../../tasks/planning/intake-and-scope.md)** — dono [`offerbook-chief`](../../agents/offerbook-chief.md). Classifica o tipo, trava o escopo, abre o esqueleto.
- **Task [`design-pipeline`](../../tasks/planning/design-pipeline.md)** — dono [`offer-squad-architect`](../../agents/offer-squad-architect.md). Desenha o pipeline curto e os handoffs.

## Passos
1. Leia o briefing e confirme os três campos mínimos. Falta um? Devolva.
2. Reescreva o pedido em UMA frase de escopo com [`power-of-one`](../../frameworks/power-of-one.md): um avatar, uma promessa, um próximo passo.
3. Leia o terreno em alto nível com [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) para calibrar o tipo.
4. Confirme o fit da trilha enxuta: oferta-base existe, público recortado, prazo curto, sem ops pesada. Caso contrário, reencaminhe.
5. Abra o esqueleto do Offer Book Master, preenchendo tipo, nome de trabalho e data.
6. Passe os gates de comando [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md).
7. Desenhe o pipeline curto do composite `run-single-promo`: offer book → VSL → e-mail → funil → tech → compliance → memória. Cada nó com dono, cada aresta com contrato.
8. Posicione o ★ HARD STOP [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) antes da copy. Nenhuma aresta o contorna.
9. Nomeie o caminho crítico e confronte com o prazo. Registre a topologia e as decisões no `decision-registry`.

## Artefatos Produzidos
- `decision.project-type` — single-promo, com motivo e alternativas podadas.
- `decision.scope-one-sentence` — a frase de escopo travada.
- `artifact.offer-book-master-skeleton` — o mapa-mestre aberto.
- `artifact.promo-pipeline` — o pipeline curto com gates e caminho crítico.
- `artifact.handoff-contracts` — o contrato de cada aresta (campos + qualidade mínima + dono).
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) — existe UM tipo classificado com motivo.
- [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) — a frase de escopo é única e não bifurca.

## Critério de Saída
O tipo está classificado como single-promo, a frase de escopo não admite duas leituras, o esqueleto está aberto, o pipeline curto é acíclico com o HARD STOP posicionado e o caminho crítico cabe no prazo. Os dois gates de comando estão verdes. A próxima fase é a [`01-offer-book-core`](01-offer-book-core.md), que recebe o escopo travado e monta o núcleo do Offer Book enxuto. Se a frase ainda bifurca, esta fase não fecha.
