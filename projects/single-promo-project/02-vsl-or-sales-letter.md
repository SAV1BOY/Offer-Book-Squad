---
id: project.single-promo-project.02-vsl-or-sales-letter
title: "Fase 02 — VSL ou Carta de Vendas"
type: project-phase
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes:
  - artifact.offer-book-master
  - decision.big-idea-locked
  - artifact.objection-belief-map
produces:
  - artifact.vsl-script
  - artifact.sales-letter
  - artifact.offer-page-copy
tags: [project-phase, single-promo, copy, vsl, sales-letter, offer-page, d4]
---

# Fase 02 — VSL ou Carta de Vendas

## Objetivo da Fase
Converter o Offer Book numa peça de venda longa que faz uma pessoa comprar. Na promo enxuta, esta é a peça-âncora: uma VSL ou uma carta de vendas que carrega a Big Idea do começo ao fim, abre o mecanismo único, empilha o valor antes do preço e fecha com reversão de risco e escassez verdadeira. A escolha entre vídeo e carta segue o canal e o avatar — vídeo para tráfego frio e mobile, carta para leitores que querem profundidade. O estado-pronto é o roteiro completo, na voz da marca, com cada claim lastreado e a estrutura de venda inteira: lead, problema, agitação, mecanismo, prova, oferta, garantia, escassez, CTA. A peça soa como a cabeça do cliente porque nasceu do VOC, não de suposição.

## Critério de Entrada
A [`01-offer-book-core`](01-offer-book-core.md) entrega o `artifact.offer-book-master`, a Big Idea travada e o mapa de objeções. Pré-condição absoluta: o ★ [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) está verde. Sem o HARD STOP fechado, esta fase não abre — é a regra `offer_before_persuasion`. Pré-condição de conteúdo: existe UMA Big Idea, o mecanismo está nomeado e a oferta tem garantia e escassez reais. Se a escassez ainda é vaga, a fase para e devolve à arquitetura. O [`control-registry`](../../data/registries/control-registry.md) é lido para reusar estruturas vencedoras.

## Agentes & Tasks
- **Task [`write-vsl-webinar`](../../tasks/copy/write-vsl-webinar.md)** — dono [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md), com passe obrigatório de voz do [`voice-style-guardian`](../../agents/voice-style-guardian.md).
- **Task [`voice-pass`](../../tasks/copy/voice-pass.md)** — dono [`voice-style-guardian`](../../agents/voice-style-guardian.md), que pode vetar copy fora da voz.

## Passos
1. Escolha o formato: VSL para frio/mobile, carta para leitores de profundidade. Registre o motivo.
2. Abra com a Big Idea no lead, calibrada ao nível de consciência com [`lead-types`](../../frameworks/lead-types.md).
3. Construa o arco com [`copy/vsl-structure`](../../frameworks/copy/vsl-structure.md) ou [`copy/pastor`](../../frameworks/copy/pastor.md): problema, agitação, virada.
4. Revele o mecanismo único como a razão pela qual desta vez funciona.
5. Empilhe o valor antes de mostrar o preço; cada bônus move uma alavanca da equação de valor.
6. Trate cada objeção do mapa dentro do corpo, na ordem em que ela surge na cabeça do leitor.
7. Apresente a oferta, a garantia e a escassez verdadeira; ancore o preço contra o valor empilhado.
8. Feche com um CTA forte e único usando [`copy/close-frameworks`](../../frameworks/copy/close-frameworks.md).
9. Rode o passe de voz: ativa, presente, frases curtas, sem jargão. Atualize o `control-registry`.

## Artefatos Produzidos
- `artifact.vsl-script` — o roteiro de vídeo completo (ou `artifact.sales-letter` se carta).
- `artifact.offer-page-copy` — a copy da página de oferta que envolve o player ou a carta.
- Registry escrito: [`control-registry`](../../data/registries/control-registry.md) com a estrutura vencedora.

## Gates
- [`vsl/vsl-value-before-price-gate`](../../checklists/vsl/vsl-value-before-price-gate.md) — o valor vem antes do preço.
- [`vsl/vsl-risk-reversal-gate`](../../checklists/vsl/vsl-risk-reversal-gate.md) — a reversão de risco está presente.
- [`vsl/vsl-cta-strength-gate`](../../checklists/vsl/vsl-cta-strength-gate.md) e a voz aprovada pelo guardião.

## Critério de Saída
O roteiro ou a carta está completo, na voz da marca, com a Big Idea conduzindo do lead ao CTA; o mecanismo está revelado; o valor antecede o preço; cada objeção foi tratada; a garantia e a escassez são reais; o CTA é único e forte. Os três gates de VSL estão verdes e o guardião de voz aprovou. A próxima fase é a [`03-email-sequence`](03-email-sequence.md), que recebe a peça-âncora e a Big Idea para orquestrar a sequência que leva tráfego até ela.
