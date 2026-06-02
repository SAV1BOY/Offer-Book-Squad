---
id: framework.money-model-designer.attraction-offer-design
title: "Attraction Offer Design — Desenho da Oferta de Atração"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, upsell-downsell-logic, continuity-design, offer-ladder-sequencing, value-equation]
sources:
  - "Alex Hormozi, *$100M Money Models* (2025), ofertas de atração."
  - "Alex Hormozi, *$100M Offers* (2021), Grand Slam Offer."
tags: [attraction, cac-liquidation, win-your-money-back, bogo, giveaway, decoy, trial, money-model, hormozi]
---

# Attraction Offer Design — Desenho da Oferta de Atração

## TL;DR
A oferta de atração é a porta de entrada que **transforma estranho em comprador** e **liquida o CAC** no front-end. Ela não precisa dar o maior lucro — precisa adquirir cliente barato (ou lucrativo) para que o upsell e a continuidade façam o resto. Os arquétipos principais: **win-your-money-back** (recupera o valor ao atingir um marco), **BOGO** (compre-um-leve-outro), **giveaway** (sorteio de topo de funil), **decoy** (isca que faz a opção-alvo parecer óbvia) e **trial** (entrada de baixa barreira). O `money-model-designer` é dono; o `unit-economics-stack-analyst` valida que a atração liquida o CAC.

## Quando usar / Quando não
**Use** ao desenhar a **primeira** oferta da escada — a que adquire o cliente. É o passo que viabiliza todo o Money Model.
**Use mais** quando o CAC é alto ou a concorrência por atenção é grande: a atração certa derruba a barreira de entrada sem destruir a percepção de valor.
**Não use** uma oferta de atração isolada e chame de Money Model — sem upsell/continuidade atrás, ela só queima margem (`money_model_spine`).
**Não use** desconto puro como atração: corta a âncora de preço e atrai caçador de barganha. Prefira aumentar valor a baixar preço.

## Inputs
- O núcleo da oferta e seu preço-âncora já definidos.
- Unit economics conhecidos: CAC-alvo, margem, LTV esperado ([`../../frameworks/money-model-sequence.md`](../../frameworks/money-model-sequence.md)).
- O avatar e a dor dominante (do banco de VOC).
- A taxonomia de tipos de atração ([`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md)).
- O upsell e a continuidade planejados, para saber quanto a atração pode "perder".

## Procedimento
1. **Defina o objetivo econômico**: a atração precisa dar lucro no front-end ou só liquidar o CAC? A resposta decide a agressividade.
2. **Escolha o arquétipo** pelo avatar e pela margem:
   - **Win-your-money-back**: o cliente recupera o valor ao atingir um marco (frequência, conclusão). Alinha incentivo e resultado; ótimo para serviços/educação.
   - **BOGO**: aumenta o valor percebido sem cortar o preço de tabela. Forte em produto com baixo custo marginal.
   - **Giveaway / sorteio**: topo de funil, captura lead com baixo atrito. Atrai volume — qualifique depois.
   - **Decoy**: adicione uma opção propositalmente pior que faz a opção-alvo parecer óbvia (ver [`../../frameworks/pricing/van-westendorp.md`](../../frameworks/pricing/van-westendorp.md) para o preço).
   - **Trial**: baixa barreira de entrada que cobra cheio depois. Bom quando o produto "vende sozinho" no uso.
3. **Garanta a captura do cartão/contato** sempre que possível — a atração existe para abrir a relação, não só doar valor.
4. **Conecte ao upsell imediato**: a atração faz sentido econômico porque há um upsell no pico de compra ([`upsell-downsell-logic.md`](upsell-downsell-logic.md)).
5. **Pontue na equação de valor**: a atração deve mover ≥1 alavanca (geralmente Esforço de entrada e Probabilidade percebida) — gate `value/value-no-orphan-lever-gate`.
6. **Valide a liquidação do CAC**: simule quanto a atração + upsell recuperam vs o custo de adquirir (com `unit-economics-stack-analyst`).
7. **Defina a escassez real** se a atração for por evento (vagas, prazo) — nunca falsa (`truthful_scarcity`).
8. **Registre** a oferta de atração e seus números no `offer-registry`.

## Outputs
- **Oferta de atração definida**: arquétipo, mecânica, preço de entrada, captura de contato/cartão.
- Cálculo de liquidação de CAC (atração + upsell vs custo de aquisição).
- Conexão explícita ao upsell e à continuidade da escada.
- Registro no `offer-registry` com o papel "atração".

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Objetivo**: liquidar o CAC; o lucro vem do núcleo e da continuidade.
- **Arquétipo escolhido**: **win-your-money-back** — "termine os 30 desafios de entrevista e ganhe 100% de volta em crédito".
- **Captura**: cartão na entrada de R$97; cobra e devolve em crédito ao cumprir o marco.
- **Upsell imediato**: no checkout, o "Simulador de Entrevista 1:1" por R$397.
- **Equação de valor**: baixa o Esforço de começar (preço pequeno) e sobe a Probabilidade (recupera se cumprir).
- **CAC**: entrada + upsell cobrem o custo de aquisição já no primeiro dia.
- **Resultado**: estranhos viram compradores engajados; o marco de devolução aumenta a conclusão e alimenta a continuidade.

## Armadilhas
- **Atração sem retaguarda.** Sem upsell/continuidade, a oferta de atração só consome margem.
- **Desconto disfarçado de atração.** Cortar preço atrai caçador de barganha e destrói a âncora. Aumente valor.
- **Giveaway sem qualificação.** Sorteio traz volume frio; sem qualificar, enche a lista de não-compradores.
- **Trial sem fricção de cancelamento clara.** Trial mal desenhado vira reembolso em massa e dor de compliance.
- **Esquecer de capturar contato/cartão.** Doar valor sem abrir a relação desperdiça a aquisição.

## Interações
- **Agentes**: `money-model-designer` (dono — escolhe o arquétipo e o encaixa na escada); `unit-economics-stack-analyst` (valida liquidação de CAC); `value-equation-engineer` (confere que a atração move alavanca); `pricing-wtp-strategist` (preço de entrada e decoy); `email-sms-sequence-writer` (sequência que converte o lead da atração).
- **Frameworks que pareiam**: [`../../frameworks/money-model-sequence.md`](../../frameworks/money-model-sequence.md) (a espinha), [`upsell-downsell-logic.md`](upsell-downsell-logic.md) (o upsell imediato), [`continuity-design.md`](continuity-design.md), [`offer-ladder-sequencing.md`](offer-ladder-sequencing.md), [`../value-equation-engineer/effort-sacrifice-reduction.md`](../value-equation-engineer/effort-sacrifice-reduction.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025) — ofertas de atração — via [`../../reference/books/offers-and-monetization/hormozi-100m-money-models.md`](../../reference/books/offers-and-monetization/hormozi-100m-money-models.md), acesso 2026-06-02.
> **Fonte:** Alex Hormozi, *$100M Offers* (2021) — Grand Slam Offer — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
