---
id: framework.launch.cart-open-close
title: "Cart Open / Close — Abertura e Fechamento de Carrinho"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [product-launch-formula, perfect-webinar, runway-and-phases, abandoned-cart-recovery, scarcity-urgency-engine]
sources:
  - "Jeff Walker, *Launch* (2014; ed. atualizada, 2023), Open Cart / Close Cart."
  - "Alex Hormozi, *$100M Offers* (2021), seção 'Scarcity & Urgency'."
tags: [open-cart, close-cart, deadline, scarcity, urgency, launch-sequence, walker]
---

# Cart Open / Close — Abertura e Fechamento de Carrinho

## TL;DR
A janela em que se pode comprar é o motor da urgência. Você **abre o carrinho** com um evento, sustenta a abertura com prova e quebra de objeção, e **fecha o carrinho** com um deadline 100% real que faz a venda acontecer. A maior parte do faturamento de um lançamento chega no **último dia** — por isso o fechamento merece tanto cuidado quanto a abertura. O `launch-producer` é dono da janela; o `email-sms-sequence-writer` escreve a sequência que a sustenta. Sem escassez verdadeira, isto vira manipulação e é veto (`truthful_scarcity`).

## Quando usar / Quando não
**Use** quando há um evento de venda (webinar, série de vídeos, página) e você quer concentrar a decisão numa janela curta com deadline real.
**Use mais** em mercado de sofisticação 3-5: o público já viu promessas; a escassez verdadeira (vagas, bônus, preço que somem de fato) é o que tira do "depois eu vejo".
**Não use** com deadline falso ou que "volta amanhã" — queima a lista, derruba entregabilidade e é veto de compliance.
**Não use** num funil evergreen de baixo ticket sem evento; ali pareie com [`../money-model-designer/offer-ladder-sequencing.md`](../money-model-designer/offer-ladder-sequencing.md).

## Inputs
- Offer Book aprovado: núcleo, mecanismo, garantia e prova prontos (pós HARD STOP).
- O evento de abertura definido ([`perfect-webinar.md`](perfect-webinar.md) ou página/VSL).
- A forma de escassez **real** declarada: vagas limitadas, bônus que expira, preço de lançamento, turma com data.
- Calendário com data e hora exatas de abertura e fechamento.
- Capacidade de e-mail/SMS verificada e lista segmentada (compraram x não compraram x clicaram).

## Procedimento
1. **Declare a escassez real antes de abrir.** Defina o que limita de fato (nº de vagas, expiração do bônus, data da turma). Registre o motivo honesto — ele entra na copy.
2. **Abra com o evento** (Open Cart). Webinar, aula ao vivo, VSL ou página de vendas. Aqui o valor é construído antes do preço.
3. **Mande o e-mail de abertura** no minuto da abertura: link direto, recap do valor, deadline visível.
4. **Sustente o meio da janela** com prova: depoimentos, respostas a objeções, demonstração do mecanismo. Um ângulo por contato.
5. **Segmente.** Quem comprou sai da sequência de venda e entra no onboarding. Quem clicou e não comprou recebe a recuperação de [`abandoned-cart-recovery.md`](abandoned-cart-recovery.md).
6. **Anuncie o fechamento** 48h e 24h antes: o que some, quando some, por quê.
7. **Rode o dia do fechamento (Close Cart)** com 3-4 contatos: "últimas horas", "última chamada", "fecha à meia-noite". Conte o deadline real.
8. **Feche de verdade.** Remova o botão de compra na hora marcada. Honrar o deadline preserva a confiança e sustenta o próximo lançamento.
9. **Pós-fechamento**: confirme a entrega, abra a sequência de onboarding e ofereça o downsell/continuidade da escada.

## Outputs
- **Mapa da janela**: data/hora de abertura e fechamento, com a forma de escassez declarada.
- **Sequência de carrinho** (briefs): abertura, meio (prova), aviso 48h/24h, dia final (3-4 contatos).
- Regras de segmentação (compraram / clicaram / silenciaram).
- Handoff para [`abandoned-cart-recovery.md`](abandoned-cart-recovery.md) e para o onboarding.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Escassez real**: turma com início fixo (15 do mês) + bônus "50 frases de entrevista" que expira no fechamento.
- **Open Cart (terça 10h)**: webinar com o pitch; e-mail de abertura no fim do webinar.
- **Meio (quarta-sexta)**: 3 e-mails de prova (aprovados reais), 1 SMS com objeção "não tenho tempo".
- **Aviso (sexta)**: e-mail "o bônus some sábado à meia-noite — e a turma fecha".
- **Close Cart (sábado)**: 09h "últimas horas", 18h "última chamada", 23h "fecha em 1h". CTA único.
- **Resultado**: ~55% das vendas chegam no sábado; o botão some à meia-noite de verdade e a lista confia no próximo ciclo.

## Armadilhas
- **Deadline falso.** Reabrir "por demanda" treina a lista a ignorar todo prazo futuro. Veto (`truthful_scarcity`).
- **Fechamento fraco.** Um único e-mail no último dia deixa dinheiro na mesa — a maioria compra nas últimas horas.
- **Não segmentar.** Mandar "compre" para quem já comprou irrita e aumenta descadastro.
- **Escassez vaga.** "Vagas limitadas" sem número nem motivo soa falso. Diga o que limita e por quê.
- **Esquecer o carrinho abandonado.** Quem chegou ao checkout e não pagou é a maior fonte de recuperação — encaminhe sempre.

## Interações
- **Agentes**: `launch-producer` (dono da janela e do run-of-show); `email-sms-sequence-writer` (escreve a sequência de abertura/fechamento); `value-equation-engineer` (a escassez cria custo de adiar, movendo a decisão); `money-model-designer` (o downsell/continuidade no pós-fechamento); `affiliate-program-architect` (parceiros respeitam a mesma janela e deadline).
- **Frameworks que pareiam**: [`product-launch-formula.md`](product-launch-formula.md) (a fase de Open/Close Cart), [`perfect-webinar.md`](perfect-webinar.md) (o evento de abertura), [`abandoned-cart-recovery.md`](abandoned-cart-recovery.md), [`runway-and-phases.md`](runway-and-phases.md), [`../../frameworks/scarcity-urgency-engine.md`](../../frameworks/scarcity-urgency-engine.md).

## Fontes
> **Fonte:** Jeff Walker, *Launch* (2014; ed. atualizada, 2023) — Open/Close Cart — via [`../../reference/books/launches-and-funnels/walker-launch.md`](../../reference/books/launches-and-funnels/walker-launch.md), acesso 2026-06-02.
> **Fonte:** Alex Hormozi, *$100M Offers* (2021), seção "Scarcity & Urgency" — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
