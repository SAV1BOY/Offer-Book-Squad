---
id: framework.pricing.conjoint-cbc
title: "Conjoint (CBC) — Trade-off de Features e Preço"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [maxdiff, gabor-granger, van-westendorp, value-based-pricing, packaging-good-better-best, kano-model]
sources:
  - "Paul E. Green & V. Srinivasan, *Conjoint Analysis in Consumer Research*, Journal of Consumer Research, vol. 5 (1978)."
  - "Sawtooth Software, *The CBC System for Choice-Based Conjoint Analysis* (technical paper)."
tags: [pricing, conjoint, cbc, choice-based, part-worth, trade-off, packaging, willingness-to-pay]
---

# Conjoint (CBC) — Trade-off de Features e Preço

## TL;DR
Conjoint baseado em escolha (CBC) descobre **o que o cliente realmente valoriza** quando precisa abrir mão de algo. Em vez de perguntar feature por feature (todos dizem "quero tudo"), você mostra **pacotes completos** que competem — cada um com features e um preço — e pede para escolher. A escolha força o trade-off. Do padrão de escolhas, você extrai a **utilidade (part-worth)** de cada feature e de cada nível de preço. Isso permite simular take-rate de qualquer pacote e calcular a **WTP por feature**. É a ferramenta mais poderosa do `pricing-wtp-strategist` para empacotar e precificar.

## Quando usar / Quando não
**Use** quando o produto tem **múltiplas features ou níveis** e você precisa decidir o que incluir em cada pacote e a que preço. É o método para desenhar Good-Better-Best com base em dado.
**Use mais** em mercado de sofisticação 3-5, onde a decisão já é por trade-off (feature × preço), não pela promessa. Ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md).
**Não use** quando o produto é **único** (sem features a variar): aí basta a curva de demanda do [`gabor-granger.md`](gabor-granger.md).
**Não use** quando você só quer **priorizar uma lista longa** de claims ou features sem preço — isso é tarefa do [`maxdiff.md`](maxdiff.md), mais simples e barato.
**Não use** sem amostra suficiente: CBC exige mais respostas (~300+) e desenho estatístico cuidadoso.

## Inputs
- A lista de **atributos** (ex.: suporte, garantia, velocidade, acesso) e seus **níveis** (ex.: suporte = nenhum / e-mail / 1:1).
- O **preço** como um atributo, com 4-6 níveis cobrindo a faixa (do [`van-westendorp.md`](van-westendorp.md)).
- Amostra robusta do avatar-alvo (~300+), segmentável.
- Uma ferramenta de desenho/análise (ex.: Sawtooth, Conjointly, Qualtrics) — CBC não se roda à mão.
- Hipóteses de quais features importam (do VOC e do [`kano-model.md`](kano-model.md)) para limitar o número de atributos.

## Procedimento
1. **Liste atributos e níveis.** Mantenha enxuto: 4-6 atributos, 2-4 níveis cada. Inclua **preço** como atributo. Atributos demais cansam o respondente e poluem o sinal.
2. **Gere o desenho experimental.** A ferramenta cria conjuntos de escolha (cada tela mostra 2-4 pacotes + opção "nenhum") de forma **balanceada e ortogonal**, para que cada nível apareça com frequência justa.
3. **Inclua a opção "não compraria nenhum".** Sem ela, você força uma compra que não existiria e infla a demanda.
4. **Aplique as telas de escolha.** Cada respondente vê 8-15 telas; em cada uma, escolhe o pacote preferido. A repetição revela o padrão.
5. **Estime as utilidades (part-worths).** O modelo (logit / hierarchical Bayes) calcula a utilidade de cada nível, **inclusive dos níveis de preço**. Utilidade alta = preferido.
6. **Calcule a WTP por feature.** Converta a utilidade da feature na **variação de preço** que a iguala (quanto de preço o cliente troca por aquela feature). Isso diz o que cada feature "vale" em reais.
7. **Rode o simulador de mercado.** Monte pacotes candidatos (seu Good-Better-Best e os do concorrente) e o simulador projeta o **share of preference** de cada um. Teste cenários: o que acontece com a demanda se eu subir o preço do Better em R$200? Se eu mover a garantia do Best para o Better?
8. **Escolha os pacotes** que maximizam receita/lucro total da **linha** (não de um único pacote) e desenhe o decoy se ajudar ([`decoy-effect.md`](decoy-effect.md)).
9. **Valide por segmento.** Hierarchical Bayes dá utilidades por respondente; agrupe-as para achar segmentos com preferências distintas → cada um vira um pacote.
10. **Registre** as utilidades, a WTP por feature e os pacotes escolhidos no `price-test-registry`; declare o método no gate `pricing/pricing-method-declared-gate`.

## Outputs
- **Tabela de utilidades (part-worths)** por atributo, nível e preço.
- **WTP por feature** em reais (quanto cada feature adiciona ao preço aceitável).
- **Simulador de share**: take-rate projetado de qualquer pacote ou linha.
- Definição de **Good-Better-Best** orientada por dado, com preços e conteúdo de cada degrau.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- Atributos: **suporte** (gravado / grupo / 1:1), **garantia** (7 dias / aprovado-ou-grátis), **velocidade** (12 sem. / 6 sem.), **preço** (R$990 / R$1.490 / R$1.990 / R$2.990).
- 320 respostas, 12 telas cada. Utilidades mostram: **garantia "aprovado-ou-grátis"** tem WTP ≈ +R$600; **suporte 1:1** ≈ +R$900; velocidade 6 semanas ≈ +R$300.
- Simulador: pacote **Better** (grupo + garantia forte, R$1.490) captura 38% de share; **Best** (1:1 + garantia + 6 sem., R$2.990) captura 22%; **Good** (gravado, R$990) captura 25%; "nenhum" 15%.
- Decisão: a garantia forte entra no Better e no Best (alta WTP por baixo custo). O 1:1 fica só no Best (justifica o salto de preço). Receita da linha maximizada com esses três degraus.

## Armadilhas
- **Atributos demais.** Mais de 6 atributos derruba a qualidade da resposta. Priorize antes com [`maxdiff.md`](maxdiff.md) ou VOC.
- **Esquecer a opção "nenhum".** Força compra irreal e infla todo take-rate.
- **Faixa de preço estreita.** Se o preço não varia o bastante, a utilidade de preço fica chata e a WTP some.
- **Ler utilidade como reais direto.** Utilidade é relativa; só vira WTP **após** converter pela escala de preço.
- **Rodar à mão ou com amostra pequena.** CBC precisa de desenho ortogonal e ~300+. Sem isso, o modelo não estima direito.
- **Otimizar um pacote só.** O ganho está na **linha** inteira; um pacote pode canibalizar outro. Use o simulador no conjunto.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — desenha o estudo, lê as utilidades e roda o simulador); `unit-economics-stack-analyst` (cruza a WTP por feature com o **custo** de entregar a feature, para incluir só o que dá margem); `money-model-designer` (usa os pacotes simulados como degraus da escada); `value-equation-engineer` (a WTP por feature confirma quais alavancas de valor o cliente paga); `positioning-lead-strategist` (as features de maior utilidade viram os atributos únicos e o benefício-chave da posição).
- **Frameworks que pareiam**: [`maxdiff.md`](maxdiff.md) (prioriza features antes do conjoint), [`kano-model.md`](kano-model.md) (classifica features por tipo de satisfação), [`gabor-granger.md`](gabor-granger.md) (alternativa para produto único), [`van-westendorp.md`](van-westendorp.md) (define a faixa de preço), [`packaging-good-better-best.md`](packaging-good-better-best.md) (os pacotes resultantes), [`decoy-effect.md`](decoy-effect.md), [`value-based-pricing.md`](value-based-pricing.md).

## Fontes
> **Fonte:** Paul E. Green & V. Srinivasan, "Conjoint Analysis in Consumer Research", *Journal of Consumer Research* vol. 5 (1978); método CBC sistematizado pela Sawtooth Software — via [`../../reference/books/offers-and-monetization/nagle-strategy-tactics-pricing.md`](../../reference/books/offers-and-monetization/nagle-strategy-tactics-pricing.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
