---
id: framework.offer-stack-builder
title: "Offer Stack Builder — Empilhamento de Valor"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [value-equation, value-stacking, guarantee-design, price-anchoring, proof-to-claim-chain, grand-slam-offer]
sources:
  - "Alex Hormozi, *$100M Offers* (2021), seções 'Trim & Stack' e 'Enhancing the Offer'."
tags: [offer-stack, value-stacking, bonuses, anchoring, perceived-value]
---

# Offer Stack Builder — Empilhamento de Valor

## TL;DR
Uma oferta forte não é **um** produto. É uma **pilha** de componentes, cada um resolvendo um obstáculo específico do avatar, cada um com valor percebido próprio, somados muito acima do preço. Você divide o problema em passos, cria um item para cada passo, ancora cada item por seu valor, e empilha. O `unit-economics-stack-analyst` monta a pilha; cada item passa pela [Value Equation](value-equation.md) — o que não move alavanca, sai.

## Quando usar / Quando não
**Use** ao construir o núcleo e os bônus de qualquer oferta de núcleo, e sempre que precisar elevar valor percebido sem cortar preço.
**Use mais** em sofisticação 3-5: a pilha é onde você materializa o mecanismo, ataca Tempo/Esforço e justifica preço alto. Ver [`../lib/taxonomies/sophistication-levels.md`](../lib/taxonomies/sophistication-levels.md).
**Não use** para inflar a pilha com "enchimento": item sem alavanca dilui foco e custo. Empilhe **valor**, não quantidade.
**Não use** em substituição à ciência de preço — a pilha cria percepção; a [precificação por WTP](price-anchoring.md) define o número.

## Inputs
- O **mecanismo único** nomeado ([`unique-mechanism.md`](unique-mechanism.md)) e a transformação prometida.
- A lista de **obstáculos** que separam o avatar do resultado (do banco de VOC e do mapa de objeções).
- Prova por componente — ver [`proof-to-claim-chain.md`](proof-to-claim-chain.md).
- A taxonomia de garantias — ver [`../lib/taxonomies/guarantee-types.md`](../lib/taxonomies/guarantee-types.md).
- Faixa de preço-alvo e WTP (do `pricing-wtp-strategist`).

## Procedimento
1. **Liste todos os obstáculos** entre o avatar e o Resultado dos Sonhos. Um por linha. Esta lista é a planta da pilha.
2. **Crie um componente por obstáculo**: para cada barreira, desenhe a entrega que a remove (módulo, ferramenta, template, sessão, comunidade).
3. **Classifique cada componente** por alavanca da Value Equation: sobe Sonho? sobe Probabilidade? derruba Tempo? derruba Esforço? Marque a direção.
4. **Ancore o valor percebido de cada item** isoladamente: o que custaria comprar isso sozinho, ou o que vale em tempo/dinheiro evitado. Ver [`offer/value-stacking.md`](offer/value-stacking.md) e [`price-anchoring.md`](price-anchoring.md).
5. **Aplique o "Trim & Stack"**: corte o que é caro de entregar **e** baixo em valor percebido; mantenha o que é barato de entregar **e** alto em valor. Maximize a razão valor/custo.
6. **Sequencie a pilha** do item-âncora (maior valor percebido) ao item de fechamento (remove a última objeção). A ordem de apresentação importa.
7. **Acople a garantia** certa ao topo da pilha para subir Probabilidade ([`guarantee-design.md`](guarantee-design.md)).
8. **Some o valor empilhado** e contraste com o preço (o "preço vs valor" do fechamento). O delta precisa ser óbvio.
9. **Marque órfãos** (item sem alavanca) e **corte**. Registre a pilha final no `offer-registry`; rode `offer-stack-checklist`.

## Outputs
- **Tabela da pilha**: componente × obstáculo-que-resolve × alavanca × valor ancorado × custo de entrega.
- Item-âncora identificado e ordem de apresentação.
- Valor total empilhado vs preço (delta de fechamento).
- Lista de cortes (Trim) com justificativa.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI. Obstáculos → componentes:
- "Não sei o vocabulário de entrevista" → **Banco de 200 frases técnicas** (valor ancorado R$497; baixo custo de entrega). Sobe Probabilidade.
- "Travo na hora de falar" → **Simulador de entrevista 1:1** (valor R$1.500). Sobe Probabilidade, derruba Esforço. **Item-âncora.**
- "Não tenho tempo" → **Trilha de 20 min/dia** (valor R$300). Derruba Tempo e Esforço.
- "Tenho medo de errar no inglês real" → **Garantia: aprovado em 60 dias ou seguimos juntos** ([condicional de serviço](../lib/taxonomies/guarantee-types.md)). Sobe Probabilidade.
- **Trim**: "certificado em PDF" tem valor percebido baixo para este avatar → cortado.
- **Resultado**: valor empilhado ≈ R$2.800; preço R$1.997. O delta é óbvio sem mexer no preço.

## Armadilhas
- **Empilhar quantidade, não valor.** Vinte bônus fracos valem menos que três fortes — e cheiram a desespero.
- **Ignorar o custo de entrega.** Item caríssimo de operar destrói a margem; o Trim existe para isso.
- **Ancorar valores inacreditáveis.** Âncora exagerada queima a credibilidade da pilha inteira (risco de compliance).
- **Esquecer a ordem.** Abrir pela garantia ou pelo item fraco enfraquece o fechamento. Comece pelo âncora.
- **Manter órfãos "porque é legal ter".** Sem alavanca, o item só dilui o foco.

## Interações
- **Agentes**: `unit-economics-stack-analyst` (dono — monta e poda a pilha); `value-equation-engineer` (pontua cada item, **veta** órfão); `pricing-wtp-strategist` (ancora valores e fixa preço); `proof-credibility-curator` (prova por componente); `vsl-webinar-scriptwriter` (apresenta a pilha antes do preço); `direct-mail-insert-writer` (usa a pilha em mailers).
- **Frameworks que pareiam**: [`value-equation.md`](value-equation.md), [`offer/value-stacking.md`](offer/value-stacking.md), [`guarantee-design.md`](guarantee-design.md), [`price-anchoring.md`](price-anchoring.md), [`proof-to-claim-chain.md`](proof-to-claim-chain.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Offers* (2021), seções "Trim & Stack" e "Enhancing the Offer" — via [`../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
