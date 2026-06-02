---
id: swipe.affiliate.sequencia-de-lancamento-do-afiliado
title: "Padrão: Sequência de Lançamento do Afiliado"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [launch.affiliate-army, launch.cart-open-close, copy.email-sequence-architecture, scarcity-urgency-engine]
sources:
  - "Jeff Walker, *Launch* (2014; ed. atualizada, 2023), JV Launch."
  - "Russell Brunson, *DotCom Secrets* (2015; ed. atualizada, 2020), Dream 100."
tags: [swipe, affiliate, sequence, cart-window, deadline, launch, jv]
---

# Padrão: Sequência de Lançamento do Afiliado

## O que é
Este é o **padrão estrutural da sequência de envios** que o afiliado dispara durante a janela de carrinho — tipicamente 3 a 4 mensagens: abertura, prova/aprofundamento e fechamento. O arquétipo-fonte é a sequência de JV launch alinhada ao calendário comum: **todos os parceiros enviam na mesma janela** e respeitam o **mesmo deadline real** ([`../../frameworks/launch/cart-open-close.md`](../../frameworks/launch/cart-open-close.md)). Aqui guardamos só a **anatomia** — o papel de cada envio na janela — em redação original, nunca copy literal de campanha alheia.

É a peça que sustenta o material de abertura ([e-mail de indicação](email-de-indicacao-do-parceiro.md)) ao longo dos dias de carrinho, entregue pronta no blackbook do afiliado ([`../../frameworks/launch/affiliate-army.md`](../../frameworks/launch/affiliate-army.md)). O efeito coordenado — todo mundo falando ao mesmo tempo — amplifica a prova social e a urgência **verdadeira** do fechamento comum.

## Anatomia
A sequência de envios que sustenta o padrão (alinhada ao calendário comum):
1. **Envio 1 — Abertura (carrinho abre)** — o parceiro endossa e apresenta a Big Idea única; abre o carrinho com o link rastreado. (Ver [e-mail de indicação](email-de-indicacao-do-parceiro.md).)
2. **Envio 2 — Prova/Aprofundamento (meio da janela)** — aprofunda o mecanismo, traz um caso de resultado e responde a objeção dominante da audiência do parceiro.
3. **Envio 3 — Lembrete de fechamento (D-1)** — recapitula a oferta e avisa que o carrinho/bônus fecha de verdade na data comum.
4. **Envio 4 — Últimas horas (dia do fechamento)** — o empurrão final com a urgência real do deadline compartilhado por todos os parceiros.

Cada envio carrega **um** CTA único com o link rastreado, e todos compartilham a **mesma Big Idea** e o **mesmo deadline real**.

## Por que funciona
A sequência respeita a **arquitetura de e-mail de lançamento** ([`../../frameworks/copy/email-sequence-architecture.md`](../../frameworks/copy/email-sequence-architecture.md)): cada mensagem tem um papel e entrega o leitor ao próximo passo, em vez de repetir o mesmo apelo. O **deadline comum** cria urgência **verdadeira** ([`../../frameworks/scarcity-urgency-engine.md`](../../frameworks/scarcity-urgency-engine.md)): a oferta de fato muda quando o carrinho fecha, e todos os parceiros reforçam o mesmo prazo — o que multiplica a **prova social** do "todo mundo falando ao mesmo tempo" (ver [`../../reference/psychology/social-proof.md`](../../reference/psychology/social-proof.md)) e a **aversão à perda** da janela que termina (ver [`../../reference/psychology/loss-aversion.md`](../../reference/psychology/loss-aversion.md)). Walker mostra que o efeito de evento coordenado, com abertura e fechamento datados, supera o envio avulso e perpétuo. Deadlines desalinhados diluiriam o pico e a escassez.

## Padrão reutilizável
Esqueleto em redação original, com placeholders por envio (o parceiro adapta à voz dele):

```
[ENVIO 1 — ABRE] {{endosso_curto}} + {{big_idea_única}}. Abriu hoje: {{link_rastreado}}.
[ENVIO 2 — PROVA] Como {{mecanismo}} funciona + caso de {{cliente_com_resultado}}. Responde: {{objeção_dominante}}. {{link_rastreado}}.
[ENVIO 3 — D-1] Recap de {{oferta}}. Fecha amanhã em {{data_e_hora_reais}} — {{bônus_que_sai}}. {{link_rastreado}}.
[ENVIO 4 — ÚLTIMAS HORAS] Faltam {{tempo_real}}. {{empurrão_final}}. {{link_rastreado}}.
```

O `affiliate-program-architect` entrega a sequência completa no blackbook com o link rastreado por parceiro e o calendário comum; o `launch-producer` garante que todos enviam na mesma janela; o `compliance-auditor` confirma que o deadline e a urgência são reais.

## Adaptação por sofisticação
Conforme [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md):
- **Sofisticação 1-2** — uma sequência curta basta (abertura + fechamento); o mercado age sem muito aprofundamento.
- **Sofisticação 3** — o envio 2 carrega o **mecanismo** com força: o público cético precisa do "por que funciona" antes do fechamento.
- **Sofisticação 4** — adense a **prova** (mais casos, mais demonstração) e o motivo real do deadline; a audiência viu sequências de lançamento demais e a credibilidade diferencia.
- **Sofisticação 5** — a sequência vira **narrativa de evento e pertencimento**: cada envio convida a audiência do parceiro a entrar numa experiência/tribo, não só a comprar antes do prazo.

## Fonte
> **Fonte:** Sequência de JV launch e janela de carrinho derivada de Jeff Walker, *Launch* (2014; ed. atualizada, 2023) e do Dream 100 de Russell Brunson, *DotCom Secrets* (2015; ed. atualizada, 2020) — via [`../../reference/books/launches-and-funnels/walker-launch.md`](../../reference/books/launches-and-funnels/walker-launch.md) e [`../../reference/books/launches-and-funnels/brunson-dotcom-secrets.md`](../../reference/books/launches-and-funnels/brunson-dotcom-secrets.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída. Todo deadline redigido por este padrão precisa ser real e cumprido (`truthful_scarcity`).
