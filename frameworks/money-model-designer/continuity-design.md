---
id: framework.money-model-designer.continuity-design
title: "Continuity Design — Desenho de Continuidade"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, attraction-offer-design, upsell-downsell-logic, offer-ladder-sequencing, value-equation]
sources:
  - "Alex Hormozi, *$100M Money Models* (2025), continuidade e recorrência."
  - "Alex Hormozi, *$100M Offers* (2021), maximização de LTV."
tags: [continuity, subscription, recurring, ltv, churn, community, membership, money-model, hormozi]
---

# Continuity Design — Desenho de Continuidade

## TL;DR
A continuidade é onde mora o **LTV** e a **previsibilidade**. É a receita recorrente — assinatura, comunidade, consumível, manutenção — que transforma uma venda única numa relação que paga mês após mês. Ela só funciona quando o cliente recebe **valor recorrente real**, não acesso passivo a um arquivo. O desenho cuida do gancho de entrada, do motivo de ficar e do controle de churn. O `money-model-designer` é dono; o `unit-economics-stack-analyst` modela LTV e payback; o `value-equation-engineer` confere que cada ciclo entrega valor.

## Quando usar / Quando não
**Use** sempre que o produto permite valor contínuo — educação, software, comunidade, consumível, serviço de manutenção.
**Use mais** quando o CAC é alto e a venda única não liquida: a continuidade é o que torna a aquisição lucrativa no tempo.
**Não use** continuidade forçada sobre algo que se resolve numa única entrega — cobrar recorrente por valor que não recorre gera churn e reembolso.
**Não use** como "depósito de conteúdo" pago: acesso passivo sem valor novo não retém (`value_equation_test`).

## Inputs
- O núcleo entregue e o resultado que ele gera (a base sobre a qual a continuidade soma).
- Unit economics: margem recorrente, CAC, LTV-alvo, payback ([`../../frameworks/money-model-sequence.md`](../../frameworks/money-model-sequence.md)).
- O upsell que antecede a continuidade ([`upsell-downsell-logic.md`](upsell-downsell-logic.md)).
- O avatar e o "trabalho recorrente" que ele precisa resolver de novo a cada ciclo.
- O tipo de garantia/liberação aplicável ([`../../lib/taxonomies/guarantee-types.md`](../../lib/taxonomies/guarantee-types.md)).

## Procedimento
1. **Identifique o valor recorrente real**: o que o cliente precisa **de novo** a cada ciclo (acompanhamento, atualização, comunidade, insumo, suporte)?
2. **Escolha o formato**: assinatura de conteúdo vivo, comunidade/clube, software, consumível recorrente, manutenção/serviço.
3. **Desenhe o gancho de entrada**: o primeiro ciclo costuma vir como upsell do núcleo ou bônus que vira pago — entrada de baixo atrito.
4. **Defina o motivo de ficar**: o valor que se acumula com o tempo (rede, progresso, biblioteca viva, resultado contínuo). É o anti-churn.
5. **Escolha o ciclo de cobrança**: mensal (mais entradas) ou anual (mais caixa e menor churn). Ofereça os dois quando possível.
6. **Aplique a alavanca de valor por ciclo**: cada mês deve mover Probabilidade (resultado contínuo) ou reduzir Esforço/Tempo (atalho recorrente).
7. **Planeje o controle de churn**: onboarding forte, marco de valor rápido, sinais de risco e oferta de retenção (downsell de pausa, não cancelamento).
8. **Use a liberação como garantia**: "pague enquanto entregamos valor; saia quando quiser" reduz risco percebido e atrai (ver garantia tipo liberação de serviço).
9. **Valide LTV:CAC e payback** (com `unit-economics-stack-analyst`) e **registre** no `offer-registry` com o papel "continuidade".

## Outputs
- **Oferta de continuidade definida**: formato, gancho de entrada, motivo de ficar, ciclo de cobrança.
- Plano de controle de churn (onboarding, marco de valor, retenção).
- Modelo de LTV, payback e LTV:CAC com a continuidade incluída.
- Registro no `offer-registry` com o papel "continuidade".

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI. Núcleo: programa de 60 dias.
- **Valor recorrente real**: praticar conversação técnica **toda semana** com pares e mentor — algo que recorre.
- **Formato**: "Clube de Conversação" mensal (R$97/mês) com salas semanais ao vivo.
- **Gancho**: oferecido como upsell no fim do núcleo; primeiro mês incluído.
- **Motivo de ficar**: a rede de pares e o progresso registrado se acumulam — sair zera o ganho social.
- **Ciclo**: mensal padrão; anual com 2 meses grátis para quem quer caixa e compromisso.
- **Churn**: marco de "primeira conversa fluida" na semana 1; oferta de pausa em vez de cancelamento.
- **Resultado**: LTV salta de uma venda única para 8-12 meses de recorrência; a continuidade é o que torna o CAC lucrativo.

## Armadilhas
- **Continuidade sem valor novo.** Cobrar mensal por acesso a um arquivo morto gera churn alto e reembolso.
- **Forçar recorrência sobre entrega única.** Se o problema se resolve uma vez, recorrência soa abusiva.
- **Ignorar o onboarding.** Sem um marco de valor rápido no primeiro ciclo, o cliente cancela antes de ver retorno.
- **Sem oferta de retenção.** Tratar cancelamento como fim, sem pausa ou downsell, perde LTV recuperável.
- **Cobrança sem clareza.** Recorrência escondida vira disputa de cartão e veto de compliance.

## Interações
- **Agentes**: `money-model-designer` (dono — desenha a continuidade); `unit-economics-stack-analyst` (modela LTV, payback, churn); `value-equation-engineer` (confere valor por ciclo); `pricing-wtp-strategist` (preço mensal vs anual); `email-sms-sequence-writer` (onboarding e sequência de retenção).
- **Frameworks que pareiam**: [`upsell-downsell-logic.md`](upsell-downsell-logic.md) (o gancho de entrada), [`attraction-offer-design.md`](attraction-offer-design.md), [`offer-ladder-sequencing.md`](offer-ladder-sequencing.md) (onde a continuidade fecha a escada), [`../../frameworks/money-model-sequence.md`](../../frameworks/money-model-sequence.md), [`../value-equation-engineer/likelihood-of-achievement.md`](../value-equation-engineer/likelihood-of-achievement.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025) — continuidade e recorrência — via [`../../reference/books/offers-and-monetization/hormozi-100m-money-models.md`](../../reference/books/offers-and-monetization/hormozi-100m-money-models.md), acesso 2026-06-02.
> **Fonte:** Alex Hormozi, *$100M Offers* (2021) — maximização de LTV — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
