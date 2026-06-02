---
id: reference.case.agora-empiricus-front-to-back
title: "Caso — O Modelo Editorial Front-to-Back (Agora / Empiricus)"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "beehiiv Blog, 'Agora Financial's Blueprint for Email Marketers': https://blog.beehiiv.com/p/agora-financial-case-study"
  - "Growth Models, 'Behind the curtain of a $1B newsletter business': https://growthmodels.co/agora-growth-study/"
  - "Game of Conversions, 'Agora Financial — How To Nail A Prediction Lead': https://gameofconversions.com/agora-financial-how-to-nail-a-prediction-lead-a-breakdown/"
  - "Padrões representativos de mercado editorial (faixas observadas, não auditadas) — rotulados no texto."
tags: [case-study, agora, empiricus, editorial, front-end, back-end, lead-types, vsl, continuity]
---

# Caso — O Modelo Editorial Front-to-Back (Agora / Empiricus)

## Contexto
A Agora é um conglomerado editorial de newsletters financeiras com receita estimada na casa de **US$ 1 bilhão** e mais de **120 publicações** pagas e gratuitas.¹ A Empiricus, no Brasil, popularizou o mesmo modelo (a famosa campanha "Diga adeus ao seu chefe"). O segredo não está no conteúdo financeiro — está na **mecânica de monetização**. O modelo é chamado **front-to-back**: a frente do funil é **barata ou gratuita** e existe só para capturar o leitor; o lucro real mora **atrás**, em assinaturas premium e produtos de alto valor. A peça central é a **carta de vendas longa** (em texto ou VSL) que enquadra um problema urgente e uma promessa irresistível. Este caso disseca o esqueleto. As cifras agregadas são públicas; as métricas de conversão são **faixas representativas de mercado**, rotuladas.

## A jogada
A jogada é uma **escada editorial** clássica, ver papéis em [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md):

- **Atração (front-end):** tráfego pago e co-promoções levam a uma **VSL ou página longa** que explica o problema e o benefício; a conversão acontece numa oferta **grátis ou de baixo preço** (uma newsletter de entrada barata).² O objetivo é **capturar o lead** e liquidar o custo de aquisição, não lucrar na frente.
- **Núcleo:** uma assinatura paga de nível médio, vendida logo após a entrada.
- **Upsell (back-end):** assinaturas premium e "lifetime" de alto valor — é onde o lucro se concentra.²
- **Downsell:** versão mais barata ou parcelada para recuperar o "não".
- **Continuidade:** renovação recorrente das assinaturas + **upsells periódicos** sobre a base já nutrida.² A relação com o leitor é o ativo.

A **big idea** (UMA, ver `one_big_idea`) é carregada por um **tipo de lead** — o ângulo de abertura que prende. Os arquétipos editoriais clássicos:
- **Prediction lead (lead de previsão):** uma previsão ousada e datada ("um evento vai acontecer e poucos estão prontos").³
- **Secret/Curiosity lead:** um segredo guardado que inverte o que o leitor acreditava.
- **Big Promise lead:** uma promessa de transformação grande e específica.
- **Story/Common-enemy lead:** uma narrativa com vilão comum (o sistema, o banco, a elite).

O **money model** é puro `money_model_spine`: a frente barata só existe para alimentar o back-end caro. Quem olha a newsletter grátis e pensa "como isso dá dinheiro?" está olhando o degrau errado da escada.

## Por que funcionou
- **Custo de aquisição financiado pela escada:** a frente captura barato; o back-end caro paga a mídia e gera o lucro. O crescimento se autofinancia.
- **Lead type certo para o nível de consciência:** o ângulo de abertura é casado ao estado do leitor (ver [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md)). Lead de previsão para o curioso; promessa grande para o consciente do problema.
- **Carta longa que vende valor antes do preço:** a VSL/página longa constrói desejo e mata objeção antes de pedir a venda. Vende-se o valor primeiro, o preço por último.
- **Relação como ativo:** a base nutrida aceita upsells periódicos. O LTV vem da **sequência de ofertas** sobre a mesma lista, não da primeira venda.²
- **Teste constante:** A/B test sistemático de páginas, leads e CTAs descobre o ângulo vencedor empiricamente.²

## Números & resultado
- **Agregado público:** Agora com receita estimada **~US$ 1 bilhão** e **120+ newsletters** sob o guarda-chuva.¹
- **Estrutura de funil verificada:** tráfego (ads/co-promo) → VSL/página longa → oferta grátis ou de baixo preço → upsell para assinatura premium → downsells → nutrição com upsells periódicos.²
- **Conversões de etapa:** trate como **padrão representativo do mercado** — conversão de página longa de tráfego frio costuma ficar em **um dígito baixo** (faixa observada ampla); a economia fecha porque o **back-end** carrega o LTV, não a frente.
- **Lead types:** o "prediction lead" é um dos arquétipos mais documentados do modelo Agora.³
As cifras de conversão por etapa **não são auditadas aqui** — o agregado de receita e a estrutura do funil são públicos; as taxas são faixas de mercado.

## Lições reutilizáveis
- **money-model-designer:** monte a **frente barata para financiar o back-end caro**. Aceite margem nula ou negativa na captura; concentre o lucro na assinatura premium e na renovação recorrente. O LTV vem da **sequência de upsells sobre a base nutrida**, não da primeira venda.
- **big-idea-architect:** escolha o **lead type** (previsão, segredo, promessa grande, inimigo comum) casado ao **nível de consciência** do leitor. UMA ideia por carta — o ângulo de abertura é a Big Idea.
- **launch-producer:** trate a **carta longa / VSL** como o motor do funil e a **renovação + upsell periódico** como o ciclo de continuidade; teste leads e páginas em A/B constante.
- **affiliate-program-architect:** use **co-promoções** (a base de um parceiro promove a sua oferta) como canal de atração de baixo custo — o motor de tráfego clássico do modelo editorial.

## Cross-refs
- [`high-ticket-application-funnel.md`](high-ticket-application-funnel.md) — o back-end de alto valor levado ao extremo.
- [`evergreen-webinar.md`](evergreen-webinar.md) — a VSL/aula como motor de conversão sempre ligado.
- [`free-plus-shipping-winners.md`](free-plus-shipping-winners.md) — outra forma de degrau de atração barato.
- [`ladder-pricing-examples.md`](ladder-pricing-examples.md) — a escada de preços por trás do front-to-back.
- [`../books/copywriting/schwartz-breakthrough-advertising.md`](../books/copywriting/schwartz-breakthrough-advertising.md) — consciência de mercado e construção de leads.
- [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md) — casar lead type ao nível de consciência.

## Fontes
¹ Growth Models, *Behind the curtain of a $1B newsletter business*: <https://growthmodels.co/agora-growth-study/>, acesso 2026-06-02.
² beehiiv Blog, *Agora Financial's Blueprint for Email Marketers*: <https://blog.beehiiv.com/p/agora-financial-case-study>, acesso 2026-06-02.
³ Game of Conversions, *Agora Financial — How To Nail A Prediction Lead*: <https://gameofconversions.com/agora-financial-how-to-nail-a-prediction-lead-a-breakdown/>, acesso 2026-06-02.
> **Fonte:** agregados públicos via Growth Models e beehiiv (ver notas ¹²³). Métricas de conversão por etapa marcadas como **padrão representativo do mercado**, não auditadas.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
