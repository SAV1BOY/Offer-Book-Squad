---
id: framework.offer.offer-diagnosis
title: "Offer Diagnosis — Diagnosticar uma Oferta Bruta Antes de Reconstruir"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [value-equation, offer-stack-builder, unique-mechanism, guarantee-design, proof-to-claim-chain, grand-slam-offer]
sources:
  - "Alex Hormozi, *$100M Offers* (2021) — diagnóstico de valor."
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966) — fit de mercado/sofisticação."
tags: [diagnosis, audit, value-equation, gap-analysis, rebuild]
---

# Offer Diagnosis — Diagnosticando a Oferta Bruta

## TL;DR
Antes de reconstruir uma oferta, você precisa saber **o que está quebrado**. Este é o exame: uma auditoria sistemática que aponta cada lacuna — promessa fraca, mecanismo ausente, denominador alto (tempo/esforço), prova órfã, garantia tímida, escassez falsa, preço sem âncora. Você gera um **mapa de lacunas priorizado**, não uma reescrita às cegas. O `value-equation-engineer` conduz o diagnóstico; o resultado direciona a remontagem na [Grand Slam Offer](grand-slam-offer.md). Diagnostique, depois reconstrua.

## Quando usar / Quando não
**Use** ao herdar uma oferta existente (controle antigo, oferta de cliente, concorrente) que precisa melhorar.
**Use** quando uma oferta "não converte" e você precisa achar a **causa**, não chutar soluções.
**Não use** para reescrever direto sem mapear: pular o diagnóstico gera conserto do sintoma errado.
**Não use** em uma oferta que ainda nem existe — para o zero, vá direto à montagem ([`grand-slam-offer.md`](grand-slam-offer.md)).

## Inputs
- A **oferta bruta** atual (todos os elementos: promessa, componentes, preço, garantia, escassez, prova).
- O **diagnóstico de mercado**: sofisticação e consciência — ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md) e [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md).
- Métricas, se houver (conversão, refund, objeções recorrentes).
- O banco de VOC e o mapa de objeções.
- A régua da [Value Equation](../value-equation.md) e a [cadeia de prova](../proof-to-claim-chain.md).

## Procedimento
1. **Inventarie a oferta atual**: liste cada elemento existente (promessa, componentes, mecanismo, garantia, escassez, preço, prova). O que está lá, em palavras.
2. **Teste o fit de mercado**: a oferta casa com a [sofisticação/consciência](../awareness-x-sophistication.md)? Mercado estágio-4 com copy de claim puro é diagnóstico imediato.
3. **Pontue a Value Equation**: avalie cada uma das quatro variáveis (Sonho, Probabilidade, Tempo, Esforço). Onde está o **gargalo**? Em mercado maduro, quase sempre Tempo/Esforço.
4. **Cace o mecanismo**: existe mecanismo único nomeado e provado? Se não, registre como lacuna crítica ([`../unique-mechanism.md`](../unique-mechanism.md)).
5. **Audite a pilha**: há órfãos (itens sem alavanca)? Há obstáculos do avatar **sem** componente que os resolva? ([`../offer-stack-builder.md`](../offer-stack-builder.md)).
6. **Audite a reversão de risco**: a garantia é forte e sustentável, ou tímida/ausente? ([`../guarantee-design.md`](../guarantee-design.md)).
7. **Audite escassez/urgência**: é real ou fabricada? Fabricada = bandeira vermelha imediata ([`../scarcity-urgency-engine.md`](../scarcity-urgency-engine.md)).
8. **Audite prova e preço**: há claims órfãos? O preço tem âncora honesta? ([`../proof-to-claim-chain.md`](../proof-to-claim-chain.md), [`../price-anchoring.md`](../price-anchoring.md)).
9. **Priorize as lacunas** por impacto × esforço: o que, corrigido, mais move a conversão? Gere o **mapa de lacunas**.
10. **Registre** o diagnóstico no `offer-registry` e entregue o plano de remontagem para a Grand Slam.

## Outputs
- **Mapa de lacunas priorizado**: cada problema × variável afetada × impacto × esforço de correção.
- Diagnóstico de gargalo da Value Equation.
- Lista de elementos ausentes (mecanismo, garantia forte, prova) e de órfãos a cortar.
- Bandeiras vermelhas (escassez falsa, claim órfão) para o compliance.
- Plano de remontagem priorizado.

## Exemplo
Oferta de amostra herdada: "Curso de Inglês Completo — fluência garantida, R$1.997". Diagnóstico:
- **Fit de mercado**: mercado em sofisticação 4; a oferta usa claim puro ("fluência") → **lacuna de mecanismo**.
- **Value Equation**: promessa genérica (Sonho difuso); Tempo alto ("fluência" = anos); Esforço alto (gramática). **Gargalo: Tempo e Esforço.**
- **Mecanismo**: ausente. **Lacuna crítica** → introduzir "Shadowing Técnico".
- **Pilha**: só "acesso ao curso"; obstáculo "travo na entrevista" não tem componente. **Lacuna** → simulador 1:1.
- **Garantia**: "fluência garantida" é vaga e inexequível. **Bandeira vermelha** → trocar por "aprovado em 60 dias ou seguimos juntos".
- **Escassez**: "vagas limitadas" sem limite real → **bandeira vermelha de compliance**.
- **Prova**: "fluência garantida" é claim órfão. **Lacuna**.
- **Prioridade**: (1) mecanismo, (2) reposicionar promessa para "entrevista" e atacar Tempo/Esforço, (3) garantia exequível, (4) prova. O plano vira a remontagem na Grand Slam.

## Armadilhas
- **Reescrever antes de diagnosticar.** Você conserta o sintoma e perde a causa.
- **Olhar só a copy, não a estrutura.** Conversão fraca costuma vir da **oferta** (denominador alto, sem mecanismo), não das palavras.
- **Ignorar o fit de mercado.** Oferta boa na sofisticação errada parece ruim — diagnostique o estágio primeiro.
- **Não priorizar.** Lista de 20 ajustes sem ordem trava a execução; ordene por impacto × esforço.
- **Passar batido na escassez falsa.** É a lacuna mais perigosa (veto e risco legal) — sinalize sempre.

## Interações
- **Agentes**: `value-equation-engineer` (dono — conduz o exame e prioriza); `mechanism-architect` (preenche a lacuna de mecanismo); `unit-economics-stack-analyst` (reconstrói pilha e garantia); `proof-credibility-curator` (resolve claims órfãos); `compliance-auditor` (recebe as bandeiras vermelhas); `offerbook-chief` (decide reconstruir ou descartar).
- **Frameworks que pareiam**: [`../value-equation.md`](../value-equation.md), [`../offer-stack-builder.md`](../offer-stack-builder.md), [`../unique-mechanism.md`](../unique-mechanism.md), [`../guarantee-design.md`](../guarantee-design.md), [`../proof-to-claim-chain.md`](../proof-to-claim-chain.md), [`grand-slam-offer.md`](grand-slam-offer.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Offers* (2021), diagnóstico de valor; fit de mercado em Eugene M. Schwartz, *Breakthrough Advertising* (1966) — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
