---
id: framework.money-model-designer.upsell-downsell-logic
title: "Upsell / Downsell Logic — Lógica de Upsell e Downsell"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, attraction-offer-design, continuity-design, offer-ladder-sequencing, value-equation]
sources:
  - "Alex Hormozi, *$100M Money Models* (2025), upsell e downsell."
  - "Alex Hormozi, *$100M Offers* (2021), maximização de valor."
tags: [upsell, downsell, aov, payment-plan, order-bump, sequence, money-model, hormozi]
---

# Upsell / Downsell Logic — Lógica de Upsell e Downsell

## TL;DR
O momento de maior intenção de compra é **logo após** o "sim". É ali que o upsell sobe o AOV sem novo custo de aquisição. E quando vem o "não", o downsell recupera a venda reduzindo preço ou escopo, salvando margem que sumiria. Esta lógica define **o quê** ofertar, **quando** e **em que ordem** — upsells no pico, downsells no "não". O `money-model-designer` é dono da sequência; o `value-equation-engineer` confere que cada passo move uma alavanca, e o `unit-economics-stack-analyst` garante que a conta fecha.

## Quando usar / Quando não
**Use** sempre que houver um núcleo vendido — todo "sim" merece um upsell, todo "não" merece um downsell.
**Use mais** quando o CAC é alto: o upsell no pico é a forma mais barata de subir a receita por cliente, pois não há novo custo de aquisição.
**Não use** upsell que distrai do núcleo antes da primeira compra fechar — ofereça **depois** do sim, não no meio da decisão principal.
**Não use** downsell que canibaliza o núcleo: ele recupera o "não", não substitui a venda cheia para quem compraria inteiro.

## Inputs
- O núcleo e seu preço-âncora já definidos.
- A oferta de atração ([`attraction-offer-design.md`](attraction-offer-design.md)) e a continuidade planejada.
- Unit economics: margem por oferta, AOV-alvo, CAC ([`../../frameworks/money-model-sequence.md`](../../frameworks/money-model-sequence.md)).
- O mapa de objeções (do `objection-registry`) — o "não" tem motivo, e o downsell responde a ele.
- Os eixos de upsell disponíveis: upgrade, feito-para-você, mais volume, mais velocidade, acesso/proximidade.

## Procedimento
1. **Mapeie o pico de intenção**: o upsell vem **imediatamente após** o sim do núcleo (página de upsell, order bump, ligação).
2. **Escolha o eixo do upsell**: o que o cliente quer **mais** depois de comprar?
   - **Upgrade** (versão superior), **feito-para-você** (menos esforço), **mais volume**, **mais velocidade**, **acesso/proximidade** (1:1, grupo, mentoria).
3. **Empilhe upsells em ordem decrescente de relevância**: o mais desejado primeiro; evite cansar com muitos passos.
4. **Pontue cada upsell na equação de valor**: deve mover uma alavanca real para **este** cliente (geralmente Esforço ou Velocidade). Órfão sai (gate `value/value-no-orphan-lever-gate`).
5. **Desenhe o downsell para o "não"**: identifique o motivo da recusa e responda com a alavanca certa.
   - Travou no **preço** → versão menor, **parcelamento** (payment plan) ou início adiado.
   - Travou no **risco** → reforço de garantia + escopo reduzido.
   - Travou no **escopo** → versão "faça você mesmo" mais barata.
6. **Defina o gatilho de cada passo**: o que dispara o upsell (compra) e o downsell (recusa/abandono).
7. **Valide a economia**: o upsell deve subir o AOV sem reembolso em massa; o downsell deve preservar margem positiva (com `unit-economics-stack-analyst`).
8. **Conecte à continuidade**: o último passo natural empurra para a recorrência ([`continuity-design.md`](continuity-design.md)).
9. **Registre** a sequência e as taxas-alvo (take rate de upsell, recuperação de downsell) no `offer-registry`.

## Outputs
- **Sequência de upsell/downsell**: ordem dos passos, eixo de cada um, gatilho de disparo.
- Mapa "objeção do não → downsell que responde".
- Take rate alvo do upsell e recuperação alvo do downsell.
- Registro no `offer-registry` com os papéis "upsell" e "downsell".

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI. Núcleo: programa de 60 dias por R$1.997.
- **Pico (após o sim)**: upsell **acesso/proximidade** = "Simulador de Entrevista 1:1" por R$397 (move Probabilidade e Esforço).
- **Segundo upsell**: **velocidade** = "trilha intensiva de 30 dias" por R$297 — só para quem pegou o 1:1.
- **Downsell (no "não" por preço)**: parcelamento do núcleo em 12x sem juros.
- **Downsell mais profundo**: versão "faça você mesmo" sem 1:1 por R$697, para quem ainda recusa.
- **Continuidade**: ambos caem no "Clube de Conversação" recorrente após 60 dias.
- **Resultado**: o AOV sobe ~30% com o upsell no pico; o parcelamento recupera recusas de preço sem cortar a âncora.

## Armadilhas
- **Upsell antes de fechar o núcleo.** Oferecer mais no meio da decisão principal derruba a conversão do núcleo.
- **Passos demais.** Empilhar muitos upsells cansa e aumenta o arrependimento — pare quando a relevância cai.
- **Downsell que canibaliza.** Oferecer a versão barata cedo demais faz quem compraria inteiro pagar menos.
- **Upsell sem alavanca.** "Mais um bônus" que não move valor para este cliente é órfão — corte.
- **Ignorar a margem do downsell.** Recuperar a venda no prejuízo não é vitória — preserve margem positiva.

## Interações
- **Agentes**: `money-model-designer` (dono — desenha a sequência); `value-equation-engineer` (confere que cada passo move alavanca); `unit-economics-stack-analyst` (valida AOV e margem); `pricing-wtp-strategist` (preço de cada passo e do parcelamento); `email-sms-sequence-writer` (sequência que entrega upsell/downsell e recupera o "não").
- **Frameworks que pareiam**: [`attraction-offer-design.md`](attraction-offer-design.md) (o que precede), [`continuity-design.md`](continuity-design.md) (o que sucede), [`offer-ladder-sequencing.md`](offer-ladder-sequencing.md), [`../../frameworks/money-model-sequence.md`](../../frameworks/money-model-sequence.md), [`../value-equation-engineer/effort-sacrifice-reduction.md`](../value-equation-engineer/effort-sacrifice-reduction.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025) — upsell e downsell — via [`../../reference/books/offers-and-monetization/hormozi-100m-money-models.md`](../../reference/books/offers-and-monetization/hormozi-100m-money-models.md), acesso 2026-06-02.
> **Fonte:** Alex Hormozi, *$100M Offers* (2021) — maximização de valor — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
