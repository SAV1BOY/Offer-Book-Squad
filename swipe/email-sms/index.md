---
id: swipe.email-sms.index
title: "Swipe: Sequências & Subject Lines (índice)"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [copy.email-sequence-architecture, copy.hook-frameworks, scarcity-urgency-engine]
sources:
  - "Jeff Walker, *Launch* (2014/2023)."
  - "Robert Cialdini, *Influence*."
tags: [swipe, email, sms, sequence, subject-line, open-cart, welcome, nurture]
---

# Swipe: Sequências & Subject Lines (índice)

## O que é
Esta categoria reúne **padrões estruturais de sequências de e-mail e SMS** — os arcos de mensagens que conduzem uma lista do primeiro contato à compra. Um e-mail isolado raramente vende; o que vende é a **sequência**: uma série de mensagens, cada uma com um trabalho, encadeadas no tempo. Aqui guardamos a **anatomia** desses arcos — a função de cada mensagem, a ordem, a cadência — em redação original com `{{placeholders}}`, nunca a copy literal de campanha alheia.

A sequência certa depende do momento: uma **sequência de boas-vindas** aquece um lead novo e constrói relação; uma **sequência de carrinho** converte uma lista aquecida numa janela de venda. Ambas obedecem a regras comuns: cada mensagem tem UM trabalho; toda urgência aponta para uma janela **real**; e o subject line é o gancho que decide a abertura. Ver [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md).

## Quando usar
- Quando o `email-sms-sequence-writer` precisa do **esqueleto de uma sequência** — boas-vindas, nutrição, lançamento ou recuperação.
- Quando uma lista tem tráfego mas converte mal: muitas vezes falta o **arco**, não o conteúdo de cada e-mail.
- Quando um lançamento precisa de aquecimento (pré-carrinho) **e** de conversão (carrinho aberto) com mensagens distintas.
- Antes de escrever: a sequência define quantas mensagens, em que ordem e com que cadência.

Evite mandar e-mails sem função clara — se a mensagem não move uma alavanca, corte. Evite também urgência inventada ("últimas vagas" sem vagas reais): é veto do [compliance-auditor](../../agents/compliance-auditor.md). E nunca encadeie subject lines de clickbait que o corpo não honra.

## Padrões nesta categoria
- [`launch-cart-sequence.md`](launch-cart-sequence.md) — o arco de **carrinho aberto**: abertura, aprofundamento, tratamento de objeções e fechamento com urgência verdadeira. Calibrado para lista aquecida numa janela de venda.
- [`soap-opera-welcome-sequence.md`](soap-opera-welcome-sequence.md) — a **sequência de boas-vindas** que aquece um lead novo com história em capítulos e constrói relação antes de vender. Calibrada para lead frio recém-capturado.

Cada padrão marca o momento do funil, o número de mensagens e a função de cada uma, alimentando a matriz de sequências e o `control-registry`.

## Liga com
- **Frameworks**: [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md) (a arquitetura das sequências), [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md) (subject lines), [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) (a urgência verdadeira do carrinho), [`pas`](../../frameworks/copy/pas.md) e [`aida`](../../frameworks/copy/aida.md) (estrutura de cada e-mail), [`close-frameworks`](../../frameworks/copy/close-frameworks.md) (o CTA).
- **Agentes**: [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) (dono), [`launch-producer`](../../agents/launch-producer.md) (cadência do lançamento), [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) (o lead que abre cada mensagem), [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) (verbatim e objeções), [`compliance-auditor`](../../agents/compliance-auditor.md) (veta urgência falsa).
- **Taxonomias**: [`awareness-levels`](../../lib/taxonomies/awareness-levels.md), [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md), [`offer-types`](../../lib/taxonomies/offer-types.md).
- **Teardowns**: [`info-product-launch-email-sequence`](../../reference/swipe-breakdowns/info-product-launch-email-sequence.md).
