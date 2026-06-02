---
id: swipe.email-sms.launch-cart-sequence
title: "Padrão: Sequência de Carrinho Aberto"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [copy.email-sequence-architecture, scarcity-urgency-engine, copy.close-frameworks]
sources:
  - "Jeff Walker, *Launch* (2014/2023) — open/close cart, via reference/swipe-breakdowns/info-product-launch-email-sequence.md."
  - "Robert Cialdini, *Influence* — reciprocidade, escassez, compromisso/coerência."
tags: [swipe, email, sequence, open-cart, close-cart, objection-handling, urgency]
---

# Padrão: Sequência de Carrinho Aberto

## O que é
Arquétipo: **a sequência de e-mails que converte uma lista aquecida durante uma janela de carrinho aberto.** É o trilho de conversão de um lançamento: depois do aquecimento, o carrinho abre, e uma série de mensagens apresenta a oferta, trata as objeções uma a uma, e fecha com urgência verdadeira quando a janela expira. Cada e-mail tem um trabalho — não é "mais um e-mail", é um beat com objetivo. Estudamos a **ordem e a função** de cada mensagem, não o texto literal de ninguém. Ver o teardown [`info-product-launch-email-sequence`](../../reference/swipe-breakdowns/info-product-launch-email-sequence.md).

## Anatomia
O arco do carrinho aberto, na nossa leitura:
1. **"Está aberto" (a oferta).** Anuncia a abertura, apresenta a oferta completa, o stack e a **janela real** de fechamento.
2. **Aprofundamento de benefício/mecanismo.** Detalha o que o produto faz e o mecanismo único — o "como/porquê funciona". Ver [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md).
3. **Objeção "vai funcionar para mim?".** Casos de perfis variados; quebra a crença externa.
4. **Objeção "eu consigo?".** Mostra simplicidade e suporte; quebra a crença interna.
5. **Objeção preço/risco.** Ancora valor, reforça garantia e reversão de risco. Ver [`anchoring`](../../reference/psychology/anchoring.md).
6. **FAQ + bônus.** Responde dúvidas práticas e reforça com bônus que inclinam a decisão.
7. **"Último dia" (urgência verdadeira).** A janela está fechando — razão real, não inventada (`truthful_scarcity`).
8. **"Últimas horas" + recapitulação.** Reembala oferta, resultado e o que se perde ao não agir; CTA final repetido.

## Por que funciona
- **Cada objeção tem seu e-mail.** Tratar uma crença por mensagem é mais limpo que amontoar tudo — `clarity_before_volume`.
- **Persuasão distribuída no tempo.** Múltiplos contatos constroem crença gradualmente — espinha de [Walker](../../reference/books/launches-and-funnels) e de [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md).
- **Escassez verdadeira do carrinho.** A janela real é o motor do fechamento — `truthful_scarcity`, sob veto do [compliance-auditor](../../agents/compliance-auditor.md). Ver [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md).
- **Compromisso e coerência.** Quem consumiu o aquecimento já deu micro-sins; o "sim" é coerente — Cialdini. Ver [`commitment-consistency`](../../reference/psychology/commitment-consistency.md).
- **Ancoragem antes do preço.** O valor empilhado fixa a referência antes do número. Ver [`price-anchoring`](../../frameworks/price-anchoring.md).

## Padrão reutilizável
Esqueleto do carrinho aberto, abstraído e original:
```
E-MAIL 1 — ABERTURA: "{{Está aberto}}" + oferta + stack + janela real ({{data/hora}}).
E-MAIL 2 — MECANISMO: como/porquê {{produto}} funciona ({{mecanismo único}}).
E-MAIL 3 — OBJEÇÃO externa: "{{funciona pra mim?}}" → casos de perfis variados.
E-MAIL 4 — OBJEÇÃO interna: "{{eu consigo?}}" → simplicidade + suporte.
E-MAIL 5 — OBJEÇÃO preço/risco: ancora valor + {{garantia}}.
E-MAIL 6 — FAQ + BÔNUS: dúvidas práticas + {{bônus que inclina}}.
E-MAIL 7 — ÚLTIMO DIA: a janela fecha em {{prazo}} (urgência verdadeira).
E-MAIL 8 — ÚLTIMAS HORAS: recapitulação + o que se perde + CTA final.

Regras:
  - cada e-mail tem UM trabalho; se não move alavanca, corta.
  - toda urgência aponta para a janela REAL ({{data/hora de fechamento}}).
  - subject line = gancho honrado pelo corpo.
```
Regra de ouro: a urgência da fase final só vale se o carrinho **realmente** fecha. Janela falsa queima a lista e é veto de compliance.

## Adaptação por sofisticação
Ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md).
- **Estágio 2-3:** os e-mails de mecanismo e abertura carregam o **"como" novo**; o mecanismo puxa a sequência.
- **Estágio 4:** os e-mails de objeção posicionam o mecanismo como **superior** (comparação direta, menos esforço/risco).
- **Estágio 5:** ancore em **identidade e comunidade** — uma turma entrando junta; pertencimento e prova social pesada conduzem o fechamento.

## Fonte
> **Fonte:** Jeff Walker, *Launch* (2014/2023), e Robert Cialdini, *Influence* — via [`source-catalog`](../../swipe-sources/source-catalog.md) e [`info-product-launch-email-sequence`](../../reference/swipe-breakdowns/info-product-launch-email-sequence.md). Acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Nenhum e-mail reproduzido; nenhuma citação literal acima.
