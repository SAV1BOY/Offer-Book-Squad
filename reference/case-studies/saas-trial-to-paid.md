---
id: reference.case.saas-trial-to-paid
title: "Caso — SaaS: do Trial ao Pago (Trial-to-Paid)"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Alex Hormozi, *$100M Money Models* (2025) — papéis de atração e continuidade."
  - "Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016) — preço por valor e empacotamento."
  - "Padrões representativos de mercado SaaS (faixas observadas, não auditadas) — rotulados no texto."
tags: [case-study, saas, trial, freemium, activation, continuity, good-better-best, churn]
---

# Caso — SaaS: do Trial ao Pago (Trial-to-Paid)

## Contexto
Software é o negócio de continuidade por excelência: a receita é recorrente por natureza. Mas o software tem um problema único — o cliente precisa **usar** o produto para perceber o valor. Por isso o degrau de atração do SaaS quase sempre é um **trial** (gratuito ou pago) ou um plano **freemium**. O objetivo do trial não é "deixar testar" — é levar o usuário até o **momento "aha"**, a primeira vez em que o produto resolve o problema dele de verdade. Quem ativa, converte e fica. Quem não ativa, cancela e some. A conversão trial-to-paid é decidida no **onboarding**, não no preço. Este caso disseca o esqueleto. As cifras são **faixas representativas de mercado**, claramente rotuladas.

## A jogada
A jogada é projetar o trial inteiro ao redor da **ativação**. Ver papéis em [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md):

- **Atração:** trial gratuito, trial pago de baixo valor ou freemium. O **trial pago** (pague-menos-agora) qualifica melhor — quem digita o cartão tem mais intenção. O freemium maximiza volume de topo.
- **A ativação (o "aha"):** o onboarding conduz o usuário à primeira vitória o mais rápido possível. Cada passo remove fricção até o momento em que o valor fica óbvio.
- **Núcleo:** o plano pago, vendido por **valor entregue durante o trial** — não por features numa tabela (ver [`../books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../books/offers-and-monetization/ramanujam-monetizing-innovation.md)).
- **Upsell:** planos superiores (good-better-best), assentos extras, add-ons de uso. A escada de planos é o efeito decoy aplicado (ver [`../../frameworks/pricing/decoy-effect.md`](../../frameworks/pricing/decoy-effect.md)).
- **Downsell:** plano mais barato ou extensão de trial para recuperar quem ia cancelar.
- **Continuidade:** a assinatura é o produto; a retenção é a economia (ver [`continuity-retention-wins.md`](continuity-retention-wins.md)).

A **big idea** (UMA, ver `one_big_idea`): *você não vai acreditar até ver funcionando no seu caso — então vamos te levar até lá rápido*. A âncora é o valor vivido no trial, não a lista de recursos.

O **money model** trata o trial como o degrau de atração e a assinatura como onde o LTV se realiza (`money_model_spine`). A economia fecha quando o **LTV supera o CAC com folga** — e o LTV depende inteiramente da **retenção**, que depende da **ativação**. Tudo se encadeia: ativação → retenção → LTV → margem para escalar aquisição.

## Por que funcionou
- **Valor vivido derruba a descrença:** software é difícil de avaliar por descrição. Deixar o usuário **experimentar o resultado** converte melhor que qualquer página de features.
- **O "aha" trava o hábito:** quem atinge a primeira vitória integra o produto à rotina. Hábito é retenção; retenção é LTV.
- **Preço por valor, não por feature:** empacotar planos por valor percebido (e usar um plano-âncora caro) captura WTP diferente sem afastar ninguém (ver [`../books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../books/offers-and-monetization/ramanujam-monetizing-innovation.md)).
- **Good-better-best com decoy:** três planos onde o do meio é o alvo torna a escolha fácil e eleva o ticket médio (ver [`../psychology/cognitive-biases-for-offers.md`](../psychology/cognitive-biases-for-offers.md)).
- **Trial pago qualifica:** pedir o cartão na entrada filtra curiosos e eleva a conversão trial-to-paid, embora reduza o volume de topo. É um trade-off de desenho.

## Números & resultado
Cifras abaixo são **padrão representativo do mercado** (faixas observadas), não números de uma empresa única:
- **Trial gratuito (sem cartão) → pago:** costuma converter em **um dígito a baixo-dois dígitos** percentuais (faixa observada muito ampla; depende de ativação).
- **Trial com cartão / pago → pago:** tende a converter **bem mais alto** que o gratuito sem cartão — menos volume, mais intenção.
- **Ativação manda na conversão:** usuários que atingem o evento de ativação convertem em taxa **muito superior** — a ativação é o preditor número um (padrão amplamente observado).
- **Churn e LTV:** a economia só fecha se a **retenção** sustentar o LTV acima do CAC; cortar churn move o LTV mais que aumentar o topo.
Sempre meça as suas coortes reais; benchmark externo só serve para detectar anomalia.

## Lições reutilizáveis
- **money-model-designer:** projete o trial ao redor da **ativação** ("aha"), não do tempo; escolha entre **trial pago** (qualifica) e **freemium** (volume) por intenção; monte planos **good-better-best com decoy** e ancore a continuidade como o degrau de LTV. A economia fecha em **LTV > CAC**, e o LTV é refém da retenção.
- **big-idea-architect:** ancore a Big Idea no **valor vivido no trial** ("veja funcionar no seu caso"), nunca na lista de features — o software vende-se pelo resultado experimentado.
- **launch-producer:** trate o **onboarding como o lançamento**: cada passo até o "aha" é uma etapa de conversão; instrumente e otimize a ativação antes de escalar aquisição.
- **affiliate-program-architect:** recompense o afiliado por **conversão a pago e retenção**, não por inscrição no trial — alinha o parceiro com a ativação e o LTV real.

## Cross-refs
- [`continuity-retention-wins.md`](continuity-retention-wins.md) — a retenção que sustenta o LTV do SaaS.
- [`ladder-pricing-examples.md`](ladder-pricing-examples.md) — a escada good-better-best de planos.
- [`dtc-subscription-box.md`](dtc-subscription-box.md) — outro modelo de continuidade.
- [`evergreen-webinar.md`](evergreen-webinar.md) — demo/webinar de produto que leva ao trial.
- [`../books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../books/offers-and-monetization/ramanujam-monetizing-innovation.md) — preço e empacotamento por valor.
- [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md) — atração, upsell, continuidade.

## Fontes
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025); Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016). Faixas numéricas marcadas como **padrão representativo do mercado**, não cifras auditadas. Acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
