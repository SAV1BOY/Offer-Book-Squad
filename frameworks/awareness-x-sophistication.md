---
id: framework.awareness-x-sophistication
title: "Awareness × Sophistication — A Matriz 5×5 de Schwartz"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [lead-types, unique-mechanism, big-idea-generator, power-of-one, starving-crowd]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
tags: [awareness, sophistication, schwartz, lead-selection, matrix, positioning]
---

# Awareness × Sophistication — A Matriz 5×5

## TL;DR
Dois eixos de Schwartz decidem **onde a copy começa**: o **nível de consciência** do prospect (o quanto ele sabe) e o **nível de sofisticação** do mercado (o quanto ele já ouviu). Cruzados numa matriz 5×5, eles apontam o **lead** correto, o **comprimento** da peça e o **grau de mecanismo** necessário. É o primeiro filtro estratégico: errar a célula queima o tráfego inteiro. O `positioning-lead-strategist` usa esta matriz para travar o lead antes de qualquer palavra de copy.

## Quando usar / Quando não
**Use** logo após o diagnóstico de mercado, antes de escolher lead, Big Idea e abertura de VSL/ad.
**Use** sempre que o mesmo lançamento atingir públicos em estados diferentes (frio vs lista quente) — uma célula por segmento.
**Não use** uma única célula para o funil inteiro: tráfego frio e remarketing vivem em células opostas. Segmente.
**Não use** o palpite no lugar da evidência — ambos os eixos saem de dados (ads de concorrentes, reviews, buscas, VOC).

## Inputs
- **Nível de consciência** dominante por segmento — ver [`../lib/taxonomies/awareness-levels.md`](../lib/taxonomies/awareness-levels.md).
- **Nível de sofisticação** do mercado — ver [`../lib/taxonomies/sophistication-levels.md`](../lib/taxonomies/sophistication-levels.md).
- Evidência de cada eixo (anúncios atuais vs antigos dos concorrentes, reviews, termos de busca, verbatims).
- O mecanismo único, se já nomeado ([`unique-mechanism.md`](unique-mechanism.md)).
- A lista de segmentos de público do lançamento.

## Procedimento
1. **Diagnostique a consciência** (1-5) por segmento, com evidência. Onde está a maioria do tráfego que você vai comprar?
2. **Diagnostique a sofisticação** (1-5) do mercado, com evidência. Os concorrentes ainda fazem claim puro, ou já competem em mecanismo?
3. **Plote a célula** (linha = consciência, coluna = sofisticação) para cada segmento.
4. **Leia o eixo da consciência → lead e comprimento**: quanto **menos** consciente, mais **longa e indireta** a abertura (História/Proclamação); quanto **mais** consciente, mais **direta** (Oferta/Preço). Use a coluna "lead recomendado" da taxonomia.
5. **Leia o eixo da sofisticação → grau de mecanismo**: estágio 1-2 vende **claim**; estágio 3-4 exige **mecanismo nomeado**; estágio 5 migra para **identidade**.
6. **Cruze os dois**: a célula final define lead + comprimento + quanto peso dar ao mecanismo. Ex.: consciência 2 × sofisticação 4 = lead de História/Segredo **carregando** o mecanismo (não claim seco).
7. **Escolha o lead** na taxonomia [`lead-types.md`](lead-types.md) e ancore a [Big Idea](big-idea-generator.md) na mesma célula.
8. **Registre célula + justificativa** no `decision-registry`; rode o gate `positioning/positioning-awareness-fit`.

## Outputs
- **Mapa de células** (uma por segmento) com evidência de cada eixo.
- Lead travado por segmento + comprimento recomendado.
- Grau de mecanismo exigido (claim / mecanismo nomeado / identidade).
- Justificativa rastreável para o gate de fit de consciência.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Segmento frio (anúncio)**: consciência **2** (sente "meu inglês trava", não conhece solução) × sofisticação **4** (mercado cheio de apps e métodos). **Célula 2×4** → lead de **História/Segredo** que **carrega o mecanismo** "Shadowing Técnico"; copy mais longa; claim puro seria invisível.
- **Segmento quente (lista de e-mail)**: consciência **4-5** (já conhece o programa) × mesma sofisticação **4**. **Célula 4×5** → lead de **Oferta direta**: preço ancorado, bônus, escassez verdadeira, CTA único.
- **Resultado**: a mesma oferta usa duas aberturas — narrativa-com-mecanismo no frio, oferta-direta no quente. Tentar uma só célula para os dois queimaria o tráfego frio.

## Armadilhas
- **Tratar mercado estágio-4 com copy estágio-2** (só claim): invisível. O eixo de sofisticação te obriga ao mecanismo.
- **Usar lead direto (Oferta) em público inconsciente**: queima o tráfego frio. O eixo de consciência manda começar pela história.
- **Uma célula para o funil todo.** Frio e remarketing são células opostas — segmente.
- **Inferir os eixos do palpite.** Sem evidência, a matriz mente. Use ads, reviews, buscas, VOC.
- **Esquecer o estágio 5.** Mercado exausto não responde a mecanismo novo — pede identidade e prova pesada.

## Interações
- **Agentes**: `positioning-lead-strategist` (dono — trava o lead); `market-sophistication-analyst` (fornece os dois eixos com evidência); `big-idea-architect` (ancora a Big Idea na célula); `vsl-webinar-scriptwriter` e `ad-creative-factory` (ajustam abertura e comprimento à célula); `email-sms-sequence-writer` (usa a célula quente).
- **Frameworks que pareiam**: [`lead-types.md`](lead-types.md), [`unique-mechanism.md`](unique-mechanism.md), [`big-idea-generator.md`](big-idea-generator.md), [`power-of-one.md`](power-of-one.md), [`starving-crowd.md`](starving-crowd.md).

## Fontes
> **Fonte:** Eugene M. Schwartz, *Breakthrough Advertising* (1966), caps. "The Five States of Awareness" e "The Five Stages of Market Sophistication" — via [`../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../reference/books/copywriting/schwartz-breakthrough-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
