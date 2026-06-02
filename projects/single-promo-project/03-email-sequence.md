---
id: project.single-promo-project.03-email-sequence
title: "Fase 03 — Sequência de E-mail & SMS"
type: project-phase
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
consumes:
  - artifact.offer-book-master
  - artifact.vsl-script
  - decision.big-idea-locked
produces:
  - artifact.email-sequence
  - artifact.sms-sequence
  - artifact.sequence-matrix
tags: [project-phase, single-promo, copy, email, sms, sequence, cart-open-close, d4]
---

# Fase 03 — Sequência de E-mail & SMS

## Objetivo da Fase
Construir a sequência que leva a lista até a peça-âncora e fecha o carrinho. Na promo enxuta, o e-mail é o motor de tráfego e de urgência: leva o leitor à VSL ou à carta, repete a Big Idea por ângulos diferentes e empurra a decisão no fim da janela. O estado-pronto é uma sequência completa por fase — pré-abertura, abertura de carrinho, meio, fechamento e recuperação de quem não comprou — cada e-mail com um ângulo, uma objeção tratada e um CTA único. O SMS reforça os momentos de pico, sem ruído. A sequência cobre os segmentos certos: quem abriu e não comprou, quem clicou e parou, quem ignorou. A urgência é 100% real, ancorada na escassez verdadeira da oferta.

## Critério de Entrada
A [`02-vsl-or-sales-letter`](02-vsl-or-sales-letter.md) entrega a peça-âncora pronta e a copy da página de oferta. A [`01-offer-book-core`](01-offer-book-core.md) entrega a Big Idea e o mapa de objeções. Pré-condição: existe uma peça-âncora aprovada para onde mandar o tráfego, e a janela de carrinho (abre/fecha) está definida com datas reais. Se a escassez é fabricada, a fase para — urgência falsa é veto de compliance. O [`control-registry`](../../data/registries/control-registry.md) é lido para reusar sequências vencedoras.

## Agentes & Tasks
- **Task [`write-email-sms-sequences`](../../tasks/copy/write-email-sms-sequences.md)** — dono [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md), com passe de voz do [`voice-style-guardian`](../../agents/voice-style-guardian.md).
- **Task [`voice-pass`](../../tasks/copy/voice-pass.md)** — dono [`voice-style-guardian`](../../agents/voice-style-guardian.md).

## Passos
1. Desenhe a matriz da sequência com [`copy/email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md): fases, número de e-mails, segmentos, gatilhos.
2. Mapeie a janela de carrinho com [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md): abre, meio, fecha, com datas reais.
3. Escreva os e-mails de pré-abertura que aquecem com a Big Idea e abrem loops.
4. Escreva os e-mails de abertura e meio: cada um com um ângulo e uma objeção do mapa.
5. Escreva os e-mails de fechamento, ancorados na escassez verdadeira e na contagem real da janela.
6. Adicione a recuperação de carrinho com [`launch/abandoned-cart-recovery`](../../frameworks/launch/abandoned-cart-recovery.md) para quem clicou e parou.
7. Acrescente o SMS nos picos: abertura e últimas horas, curto e direto.
8. Segmente: comprou (sai), abriu e não comprou, clicou e parou, ignorou.
9. Rode o passe de voz e confira o timing. Atualize o `control-registry`.

## Artefatos Produzidos
- `artifact.email-sequence` — a sequência completa por fase, com assunto, corpo, ângulo, objeção e CTA por e-mail.
- `artifact.sms-sequence` — os disparos de SMS nos picos.
- `artifact.sequence-matrix` — a matriz fase × segmento × gatilho × CTA.
- Registry escrito: [`control-registry`](../../data/registries/control-registry.md).

## Gates
- [`email-sms/email-step-coverage-gate`](../../checklists/email-sms/email-step-coverage-gate.md) — todas as fases cobertas.
- [`email-sms/email-segmentation-gate`](../../checklists/email-sms/email-segmentation-gate.md) — os segmentos certos.
- [`email-sms/email-timing-gate`](../../checklists/email-sms/email-timing-gate.md) e a voz aprovada.

## Critério de Saída
A sequência cobre pré-abertura, abertura, meio, fechamento e recuperação; cada e-mail tem ângulo, objeção e CTA único; o SMS reforça os picos; a segmentação está correta; o timing bate com a janela real; a urgência é verdadeira. Os três gates de e-mail/SMS estão verdes e o guardião aprovou. A próxima fase é a [`04-funnel-and-links`](04-funnel-and-links.md), que recebe a peça-âncora e a sequência para montar o funil e as URLs que entregam tudo.
