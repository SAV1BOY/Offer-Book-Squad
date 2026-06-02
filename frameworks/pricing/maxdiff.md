---
id: framework.pricing.maxdiff
title: "MaxDiff — Best-Worst Scaling para Priorizar Features e Claims"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [conjoint-cbc, kano-model, value-based-pricing, gabor-granger]
sources:
  - "Jordan J. Louviere, *Best-Worst Scaling: Theory, Methods and Applications* (Cambridge University Press, 2015)."
  - "Sawtooth Software, *MaxDiff (Best/Worst) Scaling* (technical paper)."
tags: [pricing, maxdiff, best-worst-scaling, prioritization, features, claims, willingness-to-pay]
---

# MaxDiff — Best-Worst Scaling para Priorizar Features e Claims

## TL;DR
MaxDiff descobre **o que importa mais** numa lista longa. Em vez de pedir notas (todos dão nota alta para tudo), você mostra subconjuntos de 4-5 itens e pede só dois: o **melhor** e o **pior**. A escolha força a hierarquia. Repetindo, você ranqueia toda a lista numa **escala de importância** comparável. Serve para priorizar features, benefícios, claims de copy ou objeções. É mais simples e barato que conjoint, e é o passo que **enxuga a lista** antes de rodar [`conjoint-cbc.md`](conjoint-cbc.md). Ferramenta do `pricing-wtp-strategist` e insumo do `avatar-voc-investigator`.

## Quando usar / Quando não
**Use** quando tem uma **lista longa** (10-30 itens) — features, benefícios, mensagens, objeções — e precisa saber a ordem de importância para o cliente.
**Use mais** antes do conjoint, para escolher quais 4-6 atributos entram no estudo caro. Também para o `avatar-voc-investigator` ranquear dores e para o `ad-creative-factory` ranquear ângulos.
**Não use** quando precisa de **preço e trade-off de pacotes** — MaxDiff não tem preço nem modelo aditivo; vá para [`conjoint-cbc.md`](conjoint-cbc.md).
**Não use** para listas curtas (≤5 itens): aí uma simples ordenação ou nota já resolve.
**Não use** esperando WTP em reais: MaxDiff dá **importância relativa**, não disposição a pagar absoluta.

## Inputs
- A lista de itens a priorizar (10-30 features, benefícios, claims ou objeções), redigidos de forma curta e paralela.
- Amostra do avatar-alvo (~150-300), segmentável.
- Uma ferramenta que gere o desenho balanceado e estime os scores (Sawtooth, Conjointly, Qualtrics).
- Clareza do que você vai **decidir** com o ranking (entrar no conjoint? virar headline? virar bônus?).

## Procedimento
1. **Monte a lista de itens.** Redija cada um curto, claro e no mesmo formato. Evite itens que se sobrepõem (canibalizam o score um do outro).
2. **Gere o desenho.** A ferramenta cria conjuntos (telas) de 4-5 itens cada, de modo **balanceado**: cada item aparece o mesmo número de vezes e em pares variados.
3. **Aplique as telas.** Em cada uma, o respondente marca o **melhor** e o **pior** item daquele subconjunto. Cada tela gera várias comparações implícitas de uma vez.
4. **Cubra a lista toda.** Garanta telas suficientes para cada item aparecer ~3-5 vezes por respondente. Poucas exposições = score instável.
5. **Estime os scores.** O modelo (contagem ou hierarchical Bayes) converte os "melhor/pior" numa **escala de utilidade** por item. HB dá scores por respondente, permitindo segmentar.
6. **Normalize para 0-100.** Reescale os scores para somar 100 (ou média 100), de modo que a importância relativa fique legível: item de score 18 importa 3× mais que um de score 6.
7. **Ranqueie e corte.** Ordene a lista. Os itens do topo entram no conjoint, viram headline ou bônus-âncora; os do fundo saem.
8. **Segmente.** Agrupe scores por avatar: o que é "melhor" para o iniciante difere do sênior. Cada segmento pode pedir empacotamento próprio.
9. **Registre** o ranking e o método no `price-test-registry` (ou no banco de VOC, se for priorização de mensagem); declare o método no gate `pricing/pricing-method-declared-gate` quando alimentar preço.

## Outputs
- **Ranking de importância** (escala 0-100) de cada feature, benefício, claim ou objeção.
- Lista enxuta dos **atributos prioritários** para entrar no [`conjoint-cbc.md`](conjoint-cbc.md).
- Hierarquia de **mensagens/ângulos** para copy e de **dores** para o avatar.
- Diferenças por segmento que orientam empacotamento.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- Lista de 16 benefícios candidatos. Telas de 5 itens, melhor/pior, 200 respostas.
- Top scores (0-100): "passar na entrevista técnica" **22**, "suporte 1:1 com nativo" **15**, "garantia aprovado-ou-grátis" **13**, "certificado" **3**, "app mobile" **2**.
- Decisão: os quatro do topo viram os **atributos do conjoint** ([`conjoint-cbc.md`](conjoint-cbc.md)) e os ganchos da copy. "Certificado" e "app" saem do pacote (score baixo, custo alto) → evita feature shock.
- Por segmento: o "dev júnior" pontua "garantia" mais alto; o "sênior" pontua "1:1 com nativo" → dois pacotes distintos.

## Armadilhas
- **Itens sobrepostos.** Dois itens parecidos dividem o score e ambos parecem fracos. Redija itens mutuamente exclusivos.
- **Lista enorme demais.** 30+ itens exige muitas telas; cansa e degrada o sinal. Pré-filtre.
- **Ler score como WTP.** MaxDiff é importância **relativa**, não reais. Não derive preço dele direto.
- **Poucas exposições por item.** Item visto 1-2 vezes tem score ruidoso. Garanta cobertura.
- **Ignorar o "pior".** Itens que muita gente marca como **pior** são candidatos a **cortar** ou até a reverse feature ([`kano-model.md`](kano-model.md)) — não despreze esse lado.
- **Score único para mercado heterogêneo.** Segmente; a média esconde preferências opostas.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — prioriza features antes do conjoint); `unit-economics-stack-analyst` (cruza os itens do topo com o custo de entregá-los, para incluir só o que dá margem); `positioning-lead-strategist` (os benefícios e jobs mais ranqueados afinam o valor e a categoria da posição); `avatar-voc-investigator` (ranqueia dores e objeções do banco de VOC); `ad-creative-factory` (ranqueia ângulos e claims para a matriz de anúncios); `value-equation-engineer` (os benefícios do topo confirmam quais alavancas de valor priorizar).
- **Frameworks que pareiam**: [`conjoint-cbc.md`](conjoint-cbc.md) (recebe a lista enxuta de atributos), [`kano-model.md`](kano-model.md) (classifica os itens por tipo de satisfação), [`value-based-pricing.md`](value-based-pricing.md) (os drivers de valor priorizados), [`gabor-granger.md`](gabor-granger.md), [`../value-equation.md`](../value-equation.md).

## Fontes
> **Fonte:** Jordan J. Louviere et al., *Best-Worst Scaling: Theory, Methods and Applications* (2015), Cambridge University Press; método operacionalizado pela Sawtooth Software — acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
