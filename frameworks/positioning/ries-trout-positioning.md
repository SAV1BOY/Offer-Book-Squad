---
id: framework.positioning.ries-trout-positioning
title: "Ries & Trout Positioning — Possuir uma Palavra na Mente"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [dunford-positioning, moore-positioning-formula, category-design, perceived-value-stack]
sources:
  - "Al Ries & Jack Trout, *Positioning: The Battle for Your Mind* (20th Anniversary ed., 2001), McGraw-Hill, ISBN 978-0-07-137358-6."
tags: [positioning, ries, trout, mind, word-ownership, category, first-mover, perception]
---

# Ries & Trout Positioning — Possuir uma Palavra na Mente

## TL;DR
Posicionamento não é o que você faz com o produto. É o que você faz com a **mente** do cliente. A mente é um campo lotado que se defende do excesso guardando só o **líder** de cada categoria e descartando o resto. Por isso a regra de ouro é **ser o primeiro** e **possuir uma palavra**. Se a posição de líder está tomada, você cria uma **categoria nova** onde é o primeiro, ou reposiciona o rival. Para o squad, isto antecede a copy: decidimos qual palavra o produto vai possuir antes de escrever. É a camada de percepção que o `positioning-lead-strategist` trava.

## Quando usar / Quando não
**Use** para decidir a **única palavra/conceito** que o produto vai ocupar na mente — o foco que a Big Idea vai reforçar.
**Use mais** em mercado saturado (sofisticação 4-5), onde a mente já está cheia e só posição clara é visível. Ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md).
**Use mais** quando a categoria existente já tem um líder forte — sinal para criar uma categoria nova ([`category-design.md`](category-design.md)).
**Não use** como substituto do trabalho concreto dos 5 componentes — Ries/Trout dá o **princípio** (a palavra, a mente); Dunford dá o **método** auditável.
**Não use** para reivindicar "o primeiro/o melhor" sem lastro: superlativo vazio é veto de compliance.

## Inputs
- O diagnóstico de mercado: a categoria existente já tem um líder na mente? Qual palavra ele possui?
- A **escada mental** do cliente na categoria (quais 2-3 nomes ele lembra e em que ordem).
- O mecanismo único e o valor provado (o que pode sustentar uma palavra própria).
- O nível de consciência do mercado ([`../awareness-x-sophistication.md`](../awareness-x-sophistication.md)).

## Procedimento
1. **Mapeie a escada da categoria.** Liste os 2-3 nomes que o cliente já guarda nesta categoria e a palavra que cada um possui. A mente comporta poucos degraus — descubra os ocupados.
2. **Decida a estratégia de entrada:**
   - **Ser o primeiro** na categoria (se ela é nova ou sem dono claro) — ocupe a palavra antes de todos.
   - **Criar categoria nova** (se o líder atual é forte) — onde você seja o primeiro por definição ([`category-design.md`](category-design.md)).
   - **Reposicionar o concorrente** — recoloque o líder numa caixa que o enfraqueça e abra espaço para você.
3. **Escolha a palavra.** Uma só. O conceito que você quer que dispare na mente quando o cliente pensa no problema. Deve ser **verdadeira, simples e defensável**. "Mais rápido", "sem código", "para devs", "à prova de recaída".
4. **Cheque a posse.** A palavra já é de outro? Se sim, não dispute de frente — estreite ou crie a sua. Possuir uma palavra livre vale mais que ser o segundo numa ocupada.
5. **Estreite, não amplie.** Resista à tentação de dizer que serve para tudo. A força vem do foco. "Mais é menos": estender a marca dilui a posição.
6. **Sustente a palavra com prova e mecanismo.** A palavra é uma promessa de categoria; o produto tem que entregá-la de fato. Ligue ao mecanismo único e ao proof.
7. **Alinhe a Big Idea à palavra.** A tese única do lançamento ([`../big-idea-generator.md`](../big-idea-generator.md)) reforça a mesma palavra. Uma tese, uma palavra ([`../power-of-one.md`](../power-of-one.md)).
8. **Repita em todos os pontos de contato.** Ads, VSL, página — todos martelam a mesma palavra. Repetição é o que grava na mente.
9. **Registre** a palavra e a estratégia (primeiro / categoria nova / reposicionar) no `decision-registry`.

## Outputs
- A **palavra/conceito** que o produto vai possuir na mente.
- A **estratégia de entrada** (ser o primeiro, criar categoria, ou reposicionar).
- A **escada mental** da categoria, com os degraus ocupados.
- Alinhamento da palavra com a Big Idea e os pontos de contato.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Escada da categoria "inglês"**: apps famosos possuem "fácil/gratuito"; escolas tradicionais possuem "fluência/diploma". A mente está cheia de generalistas.
- **Estratégia**: não disputar "inglês" (palavra ocupada por gigantes). **Criar categoria nova**: "preparação de entrevista técnica em inglês".
- **Palavra a possuir**: "**entrevista**" (ou "aprovação"). Quando o dev pensa "preciso passar na entrevista em inglês", queremos ser o primeiro nome.
- **Sustentação**: mecanismo de shadowing técnico + simulação com recrutador + 37 aprovados em 2025. A palavra tem lastro.
- **Reforço**: todo anúncio e o VSL martelam "aprovado na entrevista", não "aprenda inglês". Foco estreito → posição clara → visível num mercado lotado.

## Armadilhas
- **Disputar uma palavra ocupada.** Brigar de frente com o líder pela mesma palavra é caro e perdido. Estreite ou crie a sua.
- **Querer possuir várias palavras.** A mente guarda uma. Múltiplas mensagens = nenhuma gruda. Foco.
- **Ampliar a posição.** "Serve para todo mundo" dilui. A força vem do estreitamento.
- **Palavra sem lastro.** "O melhor", "o número 1" sem prova é veto de compliance. A palavra é uma promessa que o produto entrega.
- **Trocar a palavra a cada campanha.** A posição se grava por **repetição**. Mudar de palavra apaga o que foi construído.
- **Confundir princípio com método.** Ries/Trout inspira; o trabalho concreto e auditável vem dos 5 componentes de Dunford.

## Interações
- **Agentes**: `positioning-lead-strategist` (dono — decide a palavra e a estratégia de entrada); `big-idea-architect` (destila a posição numa tese alinhada à palavra); `market-sophistication-analyst` (avalia quão cheia está a mente e se a categoria tem dono); `pricing-wtp-strategist` (a palavra "premium" ou "barato" precede e sustenta a estratégia de preço); `unit-economics-stack-analyst` (confere que possuir a palavra escolhida cabe na economia da oferta); `vsl-webinar-scriptwriter` e `ad-creative-factory` (martelam a mesma palavra em todo ponto de contato); `compliance-auditor` (veta superlativo de "primeiro/melhor" sem lastro).
- **Frameworks que pareiam**: [`dunford-positioning.md`](dunford-positioning.md) (o método concreto), [`category-design.md`](category-design.md) (criar a categoria onde você é o primeiro), [`moore-positioning-formula.md`](moore-positioning-formula.md) (a frase que carrega a palavra), [`../power-of-one.md`](../power-of-one.md) (uma tese, uma palavra), [`../big-idea-generator.md`](../big-idea-generator.md), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md).

## Fontes
> **Fonte:** Al Ries & Jack Trout, *Positioning: The Battle for Your Mind* (ed. 20º aniversário, 2001; orig. 1981), McGraw-Hill — via [`../../reference/books/positioning/ries-trout-positioning.md`](../../reference/books/positioning/ries-trout-positioning.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
