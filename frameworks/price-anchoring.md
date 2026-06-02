---
id: framework.price-anchoring
title: "Price Anchoring — Ancoragem de Preço"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [value-equation, offer-stack-builder, value-stacking, money-model-sequence, grand-slam-offer]
sources:
  - "Daniel Kahneman, *Thinking, Fast and Slow* (2011) — anchoring & adjustment."
  - "Dan Ariely, *Predictably Irrational* (2008) — relatividade e isca."
tags: [anchoring, price, perception, decoy, framing, wtp]
---

# Price Anchoring — Ancoragem de Preço

## TL;DR
O preço não é julgado em absoluto; é julgado **em relação a uma âncora**. A primeira cifra que o cérebro vê puxa todas as seguintes (Kahneman). Você define deliberadamente a âncora — valor empilhado, preço "de", alternativa cara, custo da inação — para que o **seu** preço pareça uma pechincha óbvia. O `pricing-wtp-strategist` é o dono; ancoragem **molda a percepção** do número, enquanto a ciência de WTP **define** o número. Âncora honesta converte; âncora inventada é veto de compliance.

## Quando usar / Quando não
**Use** sempre que apresentar preço — na página, na VSL, no webinar, no mailer.
**Use** com a [pilha de valor](offer-stack-builder.md): o valor total empilhado é a âncora mais natural e honesta.
**Não use** preço "de R$X por R$Y" se o "de" nunca foi praticado — é âncora falsa e risco legal.
**Não use** ancoragem para mascarar valor fraco: ela reduz a fricção do número, não substitui a [Value Equation](value-equation.md).

## Inputs
- O **preço-alvo** derivado de WTP (Van Westendorp/Gabor-Granger do `pricing-wtp-strategist`).
- O **valor empilhado** da oferta ([`offer-stack-builder.md`](offer-stack-builder.md) e [`offer/value-stacking.md`](offer/value-stacking.md)).
- **Alternativas de referência** reais (o custo de resolver de outro jeito: contratar, errar, adiar).
- O **custo da inação** (o que o avatar perde por não agir — liga à [escassez](scarcity-urgency-engine.md)).
- A estrutura de pacotes good-better-best, se houver.

## Procedimento
1. **Estabeleça a âncora alta primeiro**: apresente o **valor total empilhado** (soma dos componentes) antes de qualquer preço. O cérebro fixa nesse número.
2. **Mostre a alternativa cara honesta**: o que custaria resolver de outro jeito (contratar um profissional, anos de tentativa e erro, o concorrente premium). Real, não inventada.
3. **Quantifique o custo da inação**: o preço de **não** agir (dinheiro/tempo/oportunidade perdidos). Outra âncora legítima.
4. **Revele o preço como contraste**: depois das âncoras, o seu número parece pequeno. "Tudo isso (valor X) por Y."
5. **Use a isca (decoy) quando houver pacotes**: posicione uma opção propositalmente pior para fazer a opção-alvo parecer óbvia (Ariely). Ver [`../lib/taxonomies/offer-types.md`](../lib/taxonomies/offer-types.md).
6. **Enquadre o parcelamento** como âncora de acessibilidade ("12× de Z"), mantendo o à-vista visível para preservar a percepção de valor.
7. **Cheque a verdade de cada âncora**: todo "de", toda comparação, todo custo evitado precisa ser **real e defensável**.
8. **Registre** as âncoras usadas e suas fontes no `price-test-registry`; rode os gates de pricing (`pricing/pricing-value-derived-gate`).

## Outputs
- **Sequência de ancoragem**: ordem em que valor, alternativa, custo da inação e preço aparecem.
- Tabela de pacotes com isca posicionada (se aplicável).
- Justificativa de verdade por âncora (fonte real).
- Roteiro de apresentação de preço para a copy.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI. Preço-alvo (de WTP): R$1.997.
- **Âncora 1 (valor empilhado)**: a pilha soma R$2.800 (banco de frases R$497 + simulador 1:1 R$1.500 + trilha R$300 + garantia). Apresentada primeiro.
- **Âncora 2 (alternativa cara honesta)**: um professor particular de inglês de negócios cobra ~R$150/hora; 60 dias de preparo passariam de R$5.000. Real.
- **Âncora 3 (custo da inação)**: perder a vaga remota = ~US$ 4.000/mês não ganhos. O preço some diante disso.
- **Revelação**: "Tudo isso — valor R$2.800, equivalente a R$5.000 em aulas particulares — por R$1.997, ou 12× de R$197."
- **Isca (pacotes)**: o pacote "só gravações" (R$1.497, sem 1:1) existe para fazer o pacote completo parecer a escolha óbvia.
- **Resultado**: o mesmo R$1.997 parece barato — sem nenhuma âncora falsa.

## Armadilhas
- **Preço "de" fictício.** "De R$5.000 por R$1.997" sem nunca ter vendido a R$5.000 é fraude e risco legal.
- **Âncora sem lastro.** Comparação inventada quebra na primeira checagem do prospect — e no compliance.
- **Revelar o preço antes da âncora.** Sem âncora alta antes, o número fica grande e a fricção sobe.
- **Esconder o à-vista.** Só mostrar parcela distorce a percepção de valor e gera desconfiança.
- **Ancorar para tapar valor fraco.** Ancoragem reduz fricção; não cria valor. Conserte a oferta primeiro.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — ancora e fixa o preço); `value-equation-engineer` (o valor percebido alimenta a âncora); `unit-economics-stack-analyst` (o valor empilhado é a âncora-base); `vsl-webinar-scriptwriter` (executa a sequência de ancoragem antes do CTA); `compliance-auditor` (**veta** âncora falsa); `money-model-designer` (ancoragem por degrau da escada).
- **Frameworks que pareiam**: [`value-equation.md`](value-equation.md), [`offer-stack-builder.md`](offer-stack-builder.md), [`offer/value-stacking.md`](offer/value-stacking.md), [`money-model-sequence.md`](money-model-sequence.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md).

## Fontes
> **Fonte:** Daniel Kahneman, *Thinking, Fast and Slow* (2011), "anchoring & adjustment"; Dan Ariely, *Predictably Irrational* (2008), relatividade e isca — via [`../reference/books/persuasion-psychology/kahneman-thinking-fast-slow.md`](../reference/books/persuasion-psychology/kahneman-thinking-fast-slow.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
