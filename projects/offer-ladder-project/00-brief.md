---
id: project.offer-ladder-project.00-brief
title: "Fase 00 — Brief & Escopo da Escada de Ofertas"
type: project-phase
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes:
  - briefing.raw-offer
  - template.offer.products-and-offers
produces:
  - decision.project-type
  - decision.scope-one-sentence
  - artifact.ladder-pipeline
  - artifact.current-offer-inventory
  - artifact.handoff-contracts
tags: [project-phase, offer-ladder, brief, escopo, money-model, ascension, d0]
---

# Fase 00 — Brief & Escopo da Escada de Ofertas

## Objetivo da Fase
Enquadrar um caso de escada de ofertas e travar o que ele vai resolver. Diferente de uma promo, este caso não nasce para vender uma oferta — nasce para desenhar a **sequência** de ofertas que extrai o máximo de valor de cada cliente ao longo do tempo. É a espinha do Money Model. O alvo é uma escada deliberada: atração, núcleo, upsell, downsell e continuidade, na ordem certa, com a economia que sustenta cada degrau. O estado-pronto é o tipo classificado como offer-ladder, UMA frase de escopo, o inventário das ofertas que já existem e o pipeline curto desenhado. Esta trilha vive no centro de arquitetura de oferta (D2): valor, preço, unit economics e money model. Não escreve copy nem monta funil — entrega a escada economicamente válida que as outras trilhas vão usar.

## Critério de Entrada
A entrada é o `briefing.raw-offer` com os campos mínimos: quem compra, qual o produto-núcleo, qual a meta de receita e qual a economia atual (preço, custo, CAC se conhecido). Falta um? A fase devolve com perguntas objetivas. Pré-condição: existe ao menos uma oferta-núcleo real e um público recortado. Se o pedido é só "qual preço cobrar" numa oferta única, o tipo pode ser outro — esta trilha existe para múltiplos degraus. O [`offer-registry`](../../data/registries/offer-registry.md) e o [`price-test-registry`](../../data/registries/price-test-registry.md) são lidos para reusar ofertas e testes de preço já validados.

## Agentes & Tasks
- **Task [`intake-and-scope`](../../tasks/planning/intake-and-scope.md)** — dono [`offerbook-chief`](../../agents/offerbook-chief.md). Classifica o tipo, trava o escopo.
- **Task [`design-pipeline`](../../tasks/planning/design-pipeline.md)** — dono [`offer-squad-architect`](../../agents/offer-squad-architect.md). Desenha a sequência de arquitetura.

## Passos
1. Leia o briefing e confirme os campos mínimos. Falta um? Devolva.
2. Reescreva o pedido em UMA frase de escopo com [`power-of-one`](../../frameworks/power-of-one.md): qual jornada de valor a escada vai cobrir.
3. Levante o inventário das ofertas atuais: o que já existe, qual preço, qual papel cada uma cumpre.
4. Confirme o fit da trilha: há um núcleo real e espaço para degraus acima e abaixo. Caso contrário, reencaminhe.
5. Passe os gates de comando [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md).
6. Desenhe o pipeline `offer-ladder`: valor → preço → unit economics → money model → produtos e ofertas. Cada nó com dono, cada aresta com contrato.
7. Nomeie o caminho crítico e a meta de liquidação de CAC. Registre a topologia no [`decision-registry`](../../data/registries/decision-registry.md).

## Artefatos Produzidos
- `decision.project-type` — offer-ladder, com motivo e alternativas podadas.
- `decision.scope-one-sentence` — a frase de escopo travada.
- `artifact.ladder-pipeline` — o pipeline de arquitetura com gates e caminho crítico.
- `artifact.current-offer-inventory` — o inventário das ofertas atuais com papel e preço.
- `artifact.handoff-contracts` — o contrato de cada aresta.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) — existe UM tipo classificado com motivo.
- [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) — a frase de escopo é única e não bifurca.

## Critério de Saída
O tipo está classificado como offer-ladder, a frase de escopo não admite duas leituras, o inventário das ofertas atuais está mapeado, o pipeline de arquitetura é acíclico com o caminho crítico nomeado e a meta de liquidação de CAC declarada. Os dois gates de comando estão verdes. A próxima fase é a [`01-value-and-pricing`](01-value-and-pricing.md), que recebe o inventário e o escopo para derivar o valor percebido e o preço de cada degrau. Se a frase ainda bifurca, esta fase não fecha.
