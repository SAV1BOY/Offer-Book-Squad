---
id: framework.money-model-designer.offer-ladder-sequencing
title: "Offer Ladder Sequencing — Sequenciamento da Escada de Ofertas"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, attraction-offer-design, upsell-downsell-logic, continuity-design, value-equation]
sources:
  - "Alex Hormozi, *$100M Money Models* (2025), sequência de ofertas."
  - "Russell Brunson, *DotCom Secrets* (2015; ed. atualizada, 2020), value ladder."
tags: [offer-ladder, value-ladder, sequencing, ascension, money-model, cac-liquidation, hormozi, brunson]
---

# Offer Ladder Sequencing — Sequenciamento da Escada de Ofertas

## TL;DR
A escada de ofertas é a **espinha** do Money Model: a ordem deliberada em que o cliente sobe de atração → núcleo → upsell → downsell → continuidade. Sequenciar é decidir **o quê** vem **quando**, com **qual CTA**, para extrair o máximo de valor o mais rápido possível. A meta clássica de Hormozi: ganhar de **um** cliente o bastante para adquirir e atender **dois** em menos de 30 dias. O `money-model-designer` é dono da escada; sem ela, não há espinha e copy/funil/logística ficam bloqueados (`money_model_spine`).

## Quando usar / Quando não
**Use** ao montar o Money Model completo — depois de cada oferta existir, a escada define a ordem e os gatilhos.
**Use mais** quando há múltiplas ofertas e o CAC precisa ser liquidado rápido: a sequência certa acelera o caixa e a ascensão.
**Não use** uma escada de uma oferta só e chame de Money Model — o mínimo aceitável é 2 partes; o alvo é 4 (gate `money-model/money-model-four-parts-gate`).
**Não use** sequência sem CTA em cada passo: todo degrau precisa de um próximo passo claro (gate `money-model/money-model-cta-per-step-gate`).

## Inputs
- As ofertas individuais já desenhadas: atração, núcleo, upsell(s), downsell, continuidade.
- Unit economics da escada: CAC, margem por degrau, LTV, payback ([`../../frameworks/money-model-sequence.md`](../../frameworks/money-model-sequence.md)).
- Os gatilhos de transição (compra, recusa, conclusão, tempo).
- A taxonomia de papéis de oferta ([`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md)).
- A planilha de produtos e ofertas ([`../../templates/offer/products-and-offers-template.csv`](../../templates/offer/products-and-offers-template.csv)).

## Procedimento
1. **Liste cada oferta com seu papel**: atração, núcleo, upsell, downsell, continuidade (mín. 2, alvo 4).
2. **Ordene pela jornada de valor**: o cliente entra barato (atração), recebe a transformação (núcleo), recebe mais no pico (upsell), é recuperado no "não" (downsell) e fica (continuidade).
3. **Defina o gatilho de cada transição**: o que move o cliente de um degrau ao próximo — compra, recusa, conclusão de marco, passagem de tempo.
4. **Garanta um CTA por degrau**: cada oferta termina apontando o próximo passo claro (gate `money-model/money-model-cta-per-step-gate`).
5. **Posicione a liquidação de CAC**: confirme que atração + upsell recuperam o custo de aquisição cedo (idealmente no front-end).
6. **Pontue a escada inteira na equação de valor**: cada degrau move ≥1 alavanca; degrau órfão sai ([`../../frameworks/value-equation.md`](../../frameworks/value-equation.md)).
7. **Verifique a coerência de preço**: a âncora sobe de forma lógica; o downsell não canibaliza o núcleo; a continuidade ancora no valor recorrente.
8. **Mapeie a escada ao funil**: cada degrau vira uma etapa de funil sem beco sem saída (handoff ao `funnel-architect`).
9. **Valide as 4 partes e a meta de payback** (gate `money-model/money-model-four-parts-gate`) e **registre** no `offer-registry`.

## Outputs
- **Escada sequenciada**: ordem dos degraus, papel, preço-âncora e gatilho de transição de cada um.
- Mapa de CTA por degrau (próximo passo claro).
- Cálculo de liquidação de CAC e payload de payback (<30 dias quando viável).
- Planilha de produtos e ofertas preenchida + registro no `offer-registry`.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Degrau 1 — Atração** (R$97, win-your-money-back): "30 desafios de entrevista". Gatilho: anúncio/lançamento.
- **Degrau 2 — Núcleo** (R$1.997): programa de 60 dias. Gatilho: webinar/checkout.
- **Degrau 3 — Upsell** (R$397, no pico): "Simulador 1:1". Gatilho: compra do núcleo.
- **Degrau 4 — Downsell** (12x sem juros): parcelamento do núcleo. Gatilho: recusa por preço.
- **Degrau 5 — Continuidade** (R$97/mês): "Clube de Conversação". Gatilho: fim dos 60 dias.
- **CAC**: atração + upsell liquidam o custo no primeiro dia; o núcleo e a continuidade são lucro.
- **Resultado**: 5 degraus, cada um com CTA e gatilho; a escada paga a aquisição rápido e ascende o cliente.

## Armadilhas
- **Oferta avulsa virando "money model".** Um núcleo sozinho não é escada — viola a espinha.
- **Degrau sem gatilho.** Sem definir o que move o cliente adiante, a sequência não flui.
- **Sem CTA por degrau.** Um beco sem saída no meio da escada perde o cliente engajado.
- **Downsell que canibaliza.** Posicionar a versão barata antes do "não" faz quem compraria inteiro pagar menos.
- **CAC liquidado tarde demais.** Se só a continuidade paga a aquisição, o caixa demora e o crescimento trava.

## Interações
- **Agentes**: `money-model-designer` (dono — sequencia a escada); `unit-economics-stack-analyst` (liquidação de CAC e payback); `value-equation-engineer` (cada degrau move alavanca); `pricing-wtp-strategist` (coerência de preço entre degraus); `funnel-architect` (mapeia a escada ao funil sem beco sem saída).
- **Frameworks que pareiam**: [`attraction-offer-design.md`](attraction-offer-design.md), [`upsell-downsell-logic.md`](upsell-downsell-logic.md), [`continuity-design.md`](continuity-design.md), [`../../frameworks/money-model-sequence.md`](../../frameworks/money-model-sequence.md) (a espinha), [`../../frameworks/value-equation.md`](../../frameworks/value-equation.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Money Models* (2025) — sequência de ofertas — via [`../../reference/books/offers-and-monetization/hormozi-100m-money-models.md`](../../reference/books/offers-and-monetization/hormozi-100m-money-models.md), acesso 2026-06-02.
> **Fonte:** Russell Brunson, *DotCom Secrets* (2015; ed. atualizada, 2020) — value ladder — via [`../../reference/books/launches-and-funnels/brunson-dotcom-secrets.md`](../../reference/books/launches-and-funnels/brunson-dotcom-secrets.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
