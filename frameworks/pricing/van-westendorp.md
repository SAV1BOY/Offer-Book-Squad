---
id: framework.pricing.van-westendorp
title: "Van Westendorp — Price Sensitivity Meter (PSM)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [gabor-granger, value-based-pricing, price-anchoring, packaging-good-better-best]
sources:
  - "Peter H. van Westendorp, *NSS Price Sensitivity Meter (PSM)*, ESOMAR Congress (1976)."
tags: [pricing, wtp, price-sensitivity, psm, survey, opp, ipp, range]
---

# Van Westendorp — Price Sensitivity Meter (PSM)

## TL;DR
O PSM acha a **faixa de preço aceitável** ao perguntar quatro vezes sobre preço, não uma. Em vez de "quanto você pagaria?", ele pede quatro pontos: caro demais, barato demais, caro mas aceitável, barato e bom. Você cruza as quatro curvas e lê quatro interseções: o preço ótimo (OPP), o ponto de indiferença (IPP) e os limites inferior e superior da faixa. É rápido, barato e ótimo para **descobrir um teto e um piso** quando você ainda não tem preço. É a primeira ferramenta de WTP do `pricing-wtp-strategist`.

## Quando usar / Quando não
**Use** quando precisa de uma **faixa** de preço para um produto novo, sem histórico, e quer um estudo barato e rápido. Bom para achar onde começar antes de testar preços exatos.
**Use mais** em mercado de sofisticação 1-3, onde o cliente ainda forma a âncora de preço. Ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md).
**Não use** como prova de **demanda** ou de receita: o PSM mede percepção de preço, não quantos vão comprar a cada preço. Para curva de demanda use [`gabor-granger.md`](gabor-granger.md); para trade-off real de features use [`conjoint-cbc.md`](conjoint-cbc.md).
**Não use** sozinho para fixar o número final. Ele dá a faixa; o preço sai do cruzamento com valor ([`value-based-pricing.md`](value-based-pricing.md)) e unit economics.

## Inputs
- Uma descrição clara do produto e do que ele entrega (o respondente precisa "ver" a oferta).
- Uma amostra do público-alvo (não clientes gerais) — mínimo prático ~100-200 respostas por segmento.
- Uma faixa ampla de preços plausível para ancorar o instrumento.
- Segmentação (por avatar, ICP ou caso de uso) para cortar os resultados depois.

## Procedimento
1. **Escreva as quatro perguntas** na ordem, sempre sobre o **mesmo** produto descrito:
   - **Caro demais**: "A que preço isto seria tão caro que você nem consideraria comprar?"
   - **Barato demais**: "A que preço seria tão barato que você duvidaria da qualidade?"
   - **Caro (mas aceitável)**: "A que preço começa a ficar caro, mas você ainda consideraria?"
   - **Bom negócio**: "A que preço seria uma boa compra pelo valor entregue?"
2. **Colete preços abertos** (cada resposta é um valor em R$), não escalas. Garanta que cada respondente vê a mesma descrição de oferta.
3. **Limpe os dados**: descarte respostas inconsistentes (ex.: "caro demais" menor que "barato demais") e outliers absurdos.
4. **Monte as curvas cumulativas**: para cada preço, calcule o % de pessoas que classificam aquele preço como caro demais, caro, barato, barato demais. As de "barato/barato demais" entram **invertidas** (cumulativo decrescente).
5. **Plote as quatro curvas** no mesmo gráfico (eixo X = preço, eixo Y = % acumulado).
6. **Leia as interseções**:
   - **OPP (Preço Ótimo)** = cruzamento de "caro demais" × "barato demais". Igual nº rejeita por caro e por barato.
   - **IPP (Indiferença)** = cruzamento de "caro" × "barato". Em geral, perto do preço do líder/mediana.
   - **PMC (limite inferior)** = cruzamento de "barato demais" × "caro". Abaixo disso, soa barato demais.
   - **PME (limite superior)** = cruzamento de "caro demais" × "barato". Acima disso, caro demais.
7. **Defina a faixa aceitável** = entre PMC e PME. O OPP é o candidato de menor resistência; o IPP indica a âncora de mercado.
8. **Corte por segmento**: rode as interseções por avatar. WTP costuma diferir muito entre faixas — isso vira o empacotamento ([`packaging-good-better-best.md`](packaging-good-better-best.md)).
9. **Registre** a faixa, o OPP, o IPP e o método no `price-test-registry`; declare o método no gate `pricing/pricing-method-declared-gate`.

## Outputs
- **Faixa de preço aceitável** (PMC → PME) com OPP e IPP marcados.
- Gráfico das quatro curvas por segmento.
- Recomendação de **ponto de partida** de preço (não final) para cruzar com valor e custo.
- Entrada para o empacotamento e para o teste de demanda (Gabor-Granger).

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI (núcleo).
- Coletamos 180 respostas do ICP "dev pleno mirando vaga remota".
- Curvas cruzam assim: **PMC ≈ R$690**, **OPP ≈ R$1.490**, **IPP ≈ R$1.800**, **PME ≈ R$2.600**.
- Leitura: abaixo de R$690 o curso "soa fraco"; acima de R$2.600 vira caro demais. A faixa aceitável é R$690-R$2.600.
- Decisão: ancoramos o núcleo perto do OPP (R$1.490-R$1.800), deixando espaço para um upsell premium acima do PME para quem tem WTP alta. O segmento "dev sênior" mostrou PME ≈ R$3.900 → justifica um pacote "Pro".

## Armadilhas
- **Tratar o OPP como o preço certo.** Ele é o de **menor resistência**, não o que maximiza lucro. Premium proposital muitas vezes vence.
- **Descrição fraca do produto.** Se o respondente não enxerga o valor, ele responde sobre um produto genérico e a faixa despenca.
- **Amostra errada.** Perguntar para quem não é o avatar contamina tudo. Filtre o público antes.
- **Ignorar a segmentação.** Uma faixa única esconde dois mercados; rode as curvas por segmento.
- **Confundir faixa com demanda.** O PSM não diz quantos compram. Para volume × preço, vá ao Gabor-Granger.
- **Esquecer o piso de custo.** A faixa pode incluir preços abaixo da sua margem viável; cruze com unit economics.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — roda o estudo e lê as interseções); `unit-economics-stack-analyst` (cruza a faixa com margem e payback); `positioning-lead-strategist` (usa o IPP como âncora de mercado para enquadrar o preço contra a alternativa).
- **Frameworks que pareiam**: [`gabor-granger.md`](gabor-granger.md) (transforma a faixa em curva de demanda), [`value-based-pricing.md`](value-based-pricing.md) (cruza com valor econômico), [`conjoint-cbc.md`](conjoint-cbc.md) (trade-off de features), [`packaging-good-better-best.md`](packaging-good-better-best.md) (segmentos viram pacotes), [`price-anchoring.md`](../price-anchoring.md), [`../value-equation.md`](../value-equation.md).

## Fontes
> **Fonte:** Peter H. van Westendorp, "NSS Price Sensitivity Meter (PSM)", ESOMAR Congress (1976) — via [`../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
