---
id: framework.value-equation-engineer.likelihood-of-achievement
title: "Likelihood of Achievement — Probabilidade Percebida de Sucesso"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [value-equation, dream-outcome-amplification, time-delay-compression, effort-sacrifice-reduction, guarantee-design]
sources:
  - "Alex Hormozi, *$100M Offers* (2021), seção 'The Value Equation' — Perceived Likelihood of Achievement."
tags: [value-equation, probability, likelihood, belief, proof, guarantee, risk-reversal, hormozi]
---

# Likelihood of Achievement — Probabilidade Percebida de Sucesso

## TL;DR
A **Probabilidade Percebida de Sucesso** é a segunda variável da [Equação de Valor](../value-equation.md) — a outra metade do numerador. É o quanto o avatar acredita que o resultado vai funcionar **para ele**. Não importa quão grande seja o sonho: se ele não acredita, o valor percebido cai. Esta alavanca sobe com **prova, mecanismo nomeado e reversão de risco**. É a que o `value-equation-engineer` puxa para vencer o ceticismo de quem "já tentou e não deu". Crença é o que separa promessa de venda.

## Quando usar / Quando não
**Use** sempre que o avatar é cético ou já falhou antes — quando o "será que funciona pra mim?" trava a compra.
**Use mais** em mercado de sofisticação 3-5: o público já viu promessas iguais; prova e mecanismo são o que restabelece a crença.
**Não use** prova falsa ou inflada para subir a crença — depoimento fabricado é veto de compliance e destrói confiança.
**Não use** isolada: crença alta num resultado pouco desejado não vende. Pareie com [`dream-outcome-amplification.md`](dream-outcome-amplification.md).

## Inputs
- O mapa de objeções e crenças falsas do avatar (do `objection-registry` e do banco de VOC).
- O banco de prova: depoimentos, dados, demonstrações, estudos de caso ([`../proof-to-claim-chain.md`](../proof-to-claim-chain.md)).
- O mecanismo único nomeado ([`../unique-mechanism.md`](../unique-mechanism.md)).
- O tipo de garantia aplicável ([`../../lib/taxonomies/guarantee-types.md`](../../lib/taxonomies/guarantee-types.md)).
- O histórico de tentativas falhas do avatar (o que já não funcionou para ele).

## Procedimento
1. **Pontue a crença atual** (0-10): o avatar acredita que VAI funcionar para ele? Liste o que a derruba e o que a sustenta.
2. **Mapeie as crenças falsas**: "isso não funciona", "não funciona pra mim", "minha situação é diferente". Cada uma exige um movimento.
3. **Nomeie o mecanismo único**: um método com nome próprio explica **por que** desta vez é diferente do que falhou.
4. **Empilhe prova por objeção**: para cada crença falsa, traga o tipo de prova que a derruba — caso de alguém "como ele", dado, demonstração.
5. **Reverta o risco**: escolha a garantia certa ([`../guarantee-design.md`](../guarantee-design.md)) — ela transfere o risco do avatar para o vendedor e sobe a crença.
6. **Mostre o caminho**: torne o passo-a-passo visível e crível; um plano claro aumenta a sensação de "eu consigo".
7. **Use prova social específica**: pessoas com o mesmo ponto de partida atingindo o resultado quebram "minha situação é diferente".
8. **Pontue a alavanca**: confirme que cada movimento **sobe a Probabilidade** e registre a leitura no `offer-registry`.

## Outputs
- **Probabilidade pontuada** (antes → depois) com os movimentos que a elevaram.
- Mapa crença-falsa → prova/garantia/mecanismo que a derruba.
- Garantia selecionada e justificada (real e exequível).
- Leitura da alavanca registrada no `offer-registry`.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Crença atual (4/10)**: "já tentei apps e desisti — não levo jeito pra inglês".
- **Crença falsa #1 ("não funciona")**: nomeia o mecanismo "Shadowing Técnico" e explica por que apps de gramática falham.
- **Crença falsa #2 ("não pra mim")**: caso de dev que "travava" e foi aprovado em 8 semanas.
- **Crença falsa #3 ("minha situação")**: aluno que estuda 20 min/dia trabalhando 10h.
- **Reversão de risco**: garantia condicional "aprovado na entrevista ou seguimos juntos de graça".
- **Resultado**: a Probabilidade sobe de 4 para 7-8; o numerador da equação cresce sem tocar no preço.

## Armadilhas
- **Prova fraca ou genérica.** Depoimento vago não quebra ceticismo. Use caso específico, com ponto de partida igual ao do avatar.
- **Prova inflada ou falsa.** Fabricar resultado é veto de compliance e mata a confiança.
- **Mecanismo sem nome.** Sem um "porquê desta vez é diferente", o avatar assume que vai falhar de novo.
- **Garantia que a operação não sustenta.** Reversão de risco impossível de honrar destrói LTV e marca.
- **Subir crença e ignorar desejo.** Acreditar muito num resultado morno não converte — amplifique o sonho junto.

## Interações
- **Agentes**: `value-equation-engineer` (dono — puxa esta alavanca); `proof-credibility-curator` (fornece a prova por objeção); `mechanism-architect` (nomeia o mecanismo que explica o porquê); `unit-economics-stack-analyst` (escolhe a garantia exequível); `vsl-webinar-scriptwriter` (quebra as crenças falsas antes do preço).
- **Frameworks que pareiam**: [`../value-equation.md`](../value-equation.md), [`dream-outcome-amplification.md`](dream-outcome-amplification.md) (a outra metade do numerador), [`time-delay-compression.md`](time-delay-compression.md), [`effort-sacrifice-reduction.md`](effort-sacrifice-reduction.md), [`../guarantee-design.md`](../guarantee-design.md), [`../launch/perfect-webinar.md`](../launch/perfect-webinar.md) (as 3 secrets quebram crença).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Offers* (2021), seção "The Value Equation" — Perceived Likelihood of Achievement — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
