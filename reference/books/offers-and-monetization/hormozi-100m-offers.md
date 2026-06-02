---
id: reference.book.hormozi-100m-offers
title: "$100M Offers — Alex Hormozi (2021)"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Alex Hormozi, *$100M Offers: How To Make Offers So Good People Feel Stupid Saying No* (Acquisition.com, 2021), ISBN 978-1-7374757-1-2."
tags: [offers, value-equation, grand-slam-offer, guarantees, scarcity, urgency, bonuses, hormozi]
---

# $100M Offers — Alex Hormozi (2021)

## Citação
> **Fonte:** Alex Hormozi, *$100M Offers* (2021), Acquisition.com $100M Series, ISBN 978-1-7374757-1-2.
> **Anti-verbatim:** princípios em redação original; citação literal ≤25 palavras, atribuída.

## Tese central
O livro defende uma ideia simples. Você não compete em preço. Você compete em oferta. Quando a oferta é boa o bastante, o cliente para de comparar e só pensa em dizer sim. Hormozi chama isso de **Grand Slam Offer**: uma proposta tão acima do mercado que o prospect sente que recusar seria burrice. O caminho para chegar lá não é baixar preço. É **subir o valor percebido** até que o preço pareça pequeno perto do que se recebe. O autor inverte a lógica do varejo de commodity: em vez de brigar por margem num mercado lotado, você escolhe um mercado faminto, isola um mecanismo, empilha valor e cobra um preço **premium** que a maioria teme pedir. O preço alto, bem ancorado, vira parte da prova de valor — não um obstáculo.

## Frameworks/Modelos

### Value Equation (Equação de Valor)
Quatro variáveis governam o valor percebido: **Resultado dos Sonhos** e **Probabilidade Percebida de Alcançá-lo** (no numerador, a maximizar) divididos por **Tempo até o Resultado** e **Esforço & Sacrifício** (no denominador, a minimizar). Toda peça de uma oferta deve mover ao menos uma dessas alavancas. Nós operacionalizamos isso em [`../../frameworks/value-equation.md`](../../../frameworks/value-equation.md), e os sub-frameworks de amplificação de resultado, compressão de tempo e redução de esforço orientam o `value-equation-engineer`.

### Grand Slam Offer (Oferta Imbatível)
A montagem completa: problema dimensionado, solução com mecanismo nomeado, value stack de entregáveis, garantia que reverte o risco, escassez e urgência verdadeiras, bônus que esmagam objeções, e um nome magnético. Implementamos o empilhamento em [`../../frameworks/offer-stack-builder.md`](../../../frameworks/offer-stack-builder.md).

### Escassez, Urgência, Garantias e Bônus
São os quatro "intensificadores" que elevam a conversão depois que o núcleo de valor existe. **Escassez** (limite de quantidade) e **urgência** (limite de tempo) criam custo de adiar. **Garantias** transferem o risco do comprador para o vendedor. **Bônus** atacam objeções específicas e inflam o valor da pilha. Ver [`../../frameworks/scarcity-urgency-engine.md`](../../../frameworks/scarcity-urgency-engine.md), [`../../frameworks/guarantee-design.md`](../../../frameworks/guarantee-design.md) e [`../../frameworks/risk-reversal-ladder.md`](../../../frameworks/risk-reversal-ladder.md).

### Naming (a fórmula M-A-G-I-C)
Hormozi propõe nomear a oferta para puxar atenção e fixar promessa. Nosso adaptador vive em [`../../frameworks/magic-naming.md`](../../../frameworks/magic-naming.md), usado pelo `mechanism-architect` ao batizar o mecanismo.

## Princípios
- Cobre pelo valor, nunca pelo custo. Preço alto bem ancorado vira prova, não barreira.
- Escolha um mercado **faminto** antes de polir a copy: dor aguda, poder de compra, fácil de alcançar, crescente.
- Resolva cada objeção com um componente da oferta — bônus, garantia ou prova — em vez de desconto.
- Escassez e urgência só funcionam se forem **reais**; limite falso é veto de compliance.
- Divida a solução em problemas e venda a remoção de cada um; a pilha vale mais que o pacote único.
- Nas palavras do autor, a meta é uma oferta que faça as pessoas "feel stupid saying no" (≤25 palavras, atribuída a Hormozi, 2021).

## Como o squad usa
- `value-equation-engineer`: pontua cada componente pelas quatro alavancas e **reprova** o que não move nenhuma (`value_equation_test`).
- `mechanism-architect`: deriva o mecanismo único e o nome (M-A-G-I-C) que ancora a Grand Slam Offer.
- `unit-economics-stack-analyst`: monta o value stack, a escada de garantias e os bônus dentro de `model-unit-economics`.
- `pricing-wtp-strategist`: usa a tese de preço premium para ancorar a faixa derivada de WTP.
- `compliance-auditor`: audita escassez/urgência contra `truthful_scarcity` e veta limites falsos.

## Cross-refs
- [`hormozi-100m-leads.md`](hormozi-100m-leads.md) — como encher o topo com a oferta pronta.
- [`hormozi-100m-money-models.md`](hormozi-100m-money-models.md) — a sequência onde a Grand Slam Offer é a atração.
- [`ramanujam-monetizing-innovation.md`](ramanujam-monetizing-innovation.md) — WTP antes do produto, base do preço por valor.
- [`../copywriting/schwartz-breakthrough-advertising.md`](../copywriting/schwartz-breakthrough-advertising.md) — sofisticação que decide quando o mecanismo entra.
- [`../../lib/taxonomies/guarantee-types.md`](../../../lib/taxonomies/guarantee-types.md) · [`../../lib/taxonomies/offer-types.md`](../../../lib/taxonomies/offer-types.md)
