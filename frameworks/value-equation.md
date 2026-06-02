---
id: framework.value-equation
title: "Value Equation — A Equação de Valor (Hormozi)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [offer-stack-builder, unique-mechanism, guarantee-design, scarcity-urgency-engine, price-anchoring]
sources:
  - "Alex Hormozi, *$100M Offers* (2021), seção 'The Value Equation'."
tags: [value, hormozi, dream-outcome, probability, time, effort, scoring]
---

# Value Equation — A Equação de Valor

## TL;DR
Valor percebido não é opinião. É uma conta. Hormozi expressa em quatro variáveis: **(Resultado dos Sonhos × Probabilidade Percebida de Sucesso) ÷ (Tempo até o Resultado × Esforço & Sacrifício)**. Você sobe o numerador e derruba o denominador. Toda peça da oferta precisa mover ao menos uma das quatro alavancas. A que não move, sai. Esta é a régua que o `value-equation-engineer` usa para aprovar ou reprovar cada componente.

## Quando usar / Quando não
**Use** sempre que existir uma oferta para pontuar: ao desenhar o núcleo, ao decidir bônus, ao comparar duas versões, ao justificar preço. É o teste universal de toda peça (`value_equation_test`).
**Use mais** em mercado sofisticação 3-5: lá o valor já não vem só da promessa, vem do mecanismo que ataca Tempo e Esforço. Ver [`../lib/taxonomies/sophistication-levels.md`](../lib/taxonomies/sophistication-levels.md).
**Não use** como única ferramenta de preço — ela mede valor percebido, não disposição a pagar; pareie com a ciência de WTP do `pricing-wtp-strategist`.
**Não use** para fabricar números falsos: a equação é uma bússola de decisão, não uma calculadora de ROI para a copy.

## Inputs
- A transformação prometida (o "antes → depois" do avatar), em verbatim do avatar.
- A lista de componentes/entregáveis candidatos da oferta.
- Evidência de prova por componente (depoimento, dado, demonstração) — ver [`proof-to-claim-chain.md`](proof-to-claim-chain.md).
- O mecanismo único nomeado, se já existir ([`unique-mechanism.md`](unique-mechanism.md)).
- A dor dominante e o medo dominante do avatar (do banco de VOC).

## Procedimento
1. **Escreva o Resultado dos Sonhos** na linguagem do avatar. Não "perder peso" — "caber na roupa do casamento em foto sem retoque". Quanto mais vívido e desejado, maior o numerador.
2. **Pontue a Probabilidade Percebida** (0-10): o avatar acredita que VAI funcionar **para ele**? Liste o que derruba a crença (ceticismo, tentativas falhas) e o que a sustenta (prova, mecanismo, garantia).
3. **Pontue o Tempo até o Resultado** (alto = ruim): em quanto tempo ele sente o **primeiro** ganho? Separe "tempo até o primeiro resultado" de "tempo até o resultado final" — o primeiro pesa mais na decisão.
4. **Pontue o Esforço & Sacrifício** (alto = ruim): o que ele precisa fazer, largar ou aguentar? Cada passo, cada renúncia, cada hábito novo aumenta o denominador.
5. **Monte a tabela de alavancas** (uma linha por componente, quatro colunas). Marque, para cada componente, **qual alavanca ele move** e em que direção.
6. **Sinalize órfãos**: todo componente que não move nenhuma alavanca é um órfão. Corte ou redesenhe. (Gate `value/value-no-orphan-lever-gate`.)
7. **Ataque o gargalo**: identifique a variável mais fraca e direcione os próximos componentes/bônus a ela. Em mercado maduro, o gargalo quase sempre é **Tempo** ou **Esforço** — daí a força do mecanismo "mais rápido, sem X".
8. **Reescreva a promessa** para refletir as alavancas movidas (ex.: garantia eleva Probabilidade; "feito-para-você" derruba Esforço).
9. **Recalcule e registre** a leitura qualitativa (sobe/desce) de cada variável no `offer-registry`.

## Outputs
- **Tabela de alavancas** (componente × 4 variáveis) com órfãos sinalizados.
- **Diagnóstico de gargalo**: qual variável limita o valor e o plano para movê-la.
- Promessa reescrita, alinhada às alavancas reais.
- Veredito por componente: **mantém / redesenha / corta**.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Resultado dos Sonhos**: "passar na entrevista técnica em inglês e fechar a vaga remota internacional". Vívido, alto valor → numerador forte.
- **Probabilidade (4/10)**: o avatar já tentou apps e desistiu. Baixa crença. **Movimento**: adicionar mecanismo nomeado ("Método Shadowing Técnico") + garantia condicional de resultado → sobe para 7/10.
- **Tempo (alto)**: cursos comuns prometem fluência "em 1 ano". **Movimento**: bônus "50 frases de entrevista" entrega ganho na **semana 1** → tempo-até-primeiro-resultado despenca.
- **Esforço (alto)**: estudar gramática cansa. **Movimento**: trocar gramática por roleplay guiado de entrevista → menos sacrifício percebido.
- **Tabela**: o bônus "certificado" não move nenhuma alavanca para este avatar → **órfão, cortado**. O "simulador de entrevista 1:1" move Probabilidade **e** Esforço → mantido como bônus-âncora.
- **Resultado**: valor percebido sobe sem mexer no preço; a promessa vira "aprovado na entrevista em inglês em 60 dias — ou seguimos juntos de graça".

## Armadilhas
- **Inflar o numerador e ignorar o denominador.** Promessa enorme com esforço enorme não vende; o avatar faz a conta sozinho.
- **Confundir tempo-final com tempo-ao-primeiro-resultado.** Entregue um ganho rápido cedo, mesmo que pequeno.
- **Pontuar com a sua crença, não a do avatar.** Probabilidade é **percebida**; use VOC e prova, não otimismo interno.
- **Manter órfãos "porque é legal ter".** Componente sem alavanca dilui o foco e aumenta custo. Corte.
- **Usar a equação como cálculo de ROI literal na copy.** Ela orienta decisão de design; não vire número fabricado (veto de compliance).

## Interações
- **Agentes**: `value-equation-engineer` (dono — pode **vetar** componente sem alavanca); `mechanism-architect` (o mecanismo é o que mais derruba Tempo/Esforço); `unit-economics-stack-analyst` (aplica ao montar o stack e os bônus); `pricing-wtp-strategist` (cruza valor percebido com WTP); `vsl-webinar-scriptwriter` (constrói o valor antes do preço usando as alavancas).
- **Frameworks que pareiam**: [`offer-stack-builder.md`](offer-stack-builder.md) (cada item da pilha é pontuado aqui), [`unique-mechanism.md`](unique-mechanism.md), [`guarantee-design.md`](guarantee-design.md) (sobe Probabilidade), [`scarcity-urgency-engine.md`](scarcity-urgency-engine.md) (cria custo de adiar), [`price-anchoring.md`](price-anchoring.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md) e [`offer/value-stacking.md`](offer/value-stacking.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Offers* (2021), seção "The Value Equation" — via [`../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
