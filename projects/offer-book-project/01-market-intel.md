---
id: project.offer-book-project.01-market-intel
title: "Fase 01 — Inteligência de Mercado"
type: project-phase
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
consumes:
  - decision.scope-one-sentence
  - artifact.case-pipeline
  - template.strategy.market-brief
produces:
  - artifact.market-brief
  - decision.sophistication-stage
  - decision.awareness-level
tags: [project-phase, intelligence, mercado, sofisticacao, consciencia, starving-crowd, d1]
---

# Fase 01 — Inteligência de Mercado

## Objetivo da Fase
Diagnosticar o terreno antes de qualquer palavra. Esta fase devolve um market-brief com dois números defensáveis — sofisticação (1-5) e consciência (1-5), cada um com ≥2 evidências independentes — mais o dimensionamento TAM/SAM/SOM e o veredito da multidão faminta. O estado-pronto é o terreno lido sem palpite: avatar, mecanismo, Big Idea e posicionamento poderão ser calibrados sobre evidência, não sobre suposição.

## Critério de Entrada
A Fase 00 entrega: a frase de escopo travada (sei qual transformação e qual público), o `artifact.case-pipeline` com a posição desta trilha no DAG (sei se sou "construção completa" ou "revalidação leve") e os contratos de handoff. Pré-condição: existe um público-alvo definido, não "todo mundo". Se o escopo aponta para dois mercados distintos, a fase devolve ao architect/chief pedindo priorização. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para checar se já há oferta validada.

## Agentes & Tasks
- **Task [`run-market-intel`](../../tasks/intelligence/run-market-intel.md)** — dono [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md), com apoio do [`offer-squad-architect`](../../agents/offer-squad-architect.md) no roteamento do handoff de pesquisa.

## Passos
1. Delimite o mercado pelo recorte exato do escopo. Mercado vago gera diagnóstico vago.
2. Rode o teste [`starving-crowd`](../../frameworks/starving-crowd.md) como portão de entrada: pontue Dor, Poder de compra e Alcance (0-10) com evidência por nota. Sem fome, recomende mudar mercado/oferta.
3. Diagnostique a sofisticação (1-5) pelos claims dominantes dos concorrentes, com ≥2 evidências.
4. Diagnostique a consciência (1-5) pela VOC, com ≥2 evidências.
5. Resolva a ambiguidade com Tree-of-Thoughts; na dúvida, arredonde para o mais sofisticado.
6. Dimensione TAM/SAM/SOM de baixo para cima, com base de cálculo explícita; confirme SOM ≤ SAM ≤ TAM.
7. Derive as implicações: qual mecanismo o estágio exige, qual lead, qual abertura de copy.
8. Faça o self-verify (cada número com ≥2 evidências, contra-evidência buscada). Registre a oferta-semente no `offer-registry` e passe os três gates de mercado com evidência linkada.

## Artefatos Produzidos
- `artifact.market-brief` — sofisticação + consciência com evidência, célula da matriz, veredito starving-crowd, TAM/SAM/SOM, implicações de mecanismo/lead/abertura, nível de confiança.
- `decision.sophistication-stage` e `decision.awareness-level` — os dois números travados.
- Registry escrito: [`offer-registry`](../../data/registries/offer-registry.md) com a oferta-semente.

## Gates
- [`market/market-sophistication-gate`](../../checklists/market/market-sophistication-gate.md)
- [`market/market-awareness-gate`](../../checklists/market/market-awareness-gate.md)
- [`market/market-starving-crowd-gate`](../../checklists/market/market-starving-crowd-gate.md)

## Critério de Saída
Os dois números estão declarados com os termos das taxonomias e ≥2 evidências independentes cada; o veredito starving-crowd tem nota tripla justificada; TAM/SAM/SOM são coerentes e o SOM bate com a meta; as implicações estão derivadas; os três gates de mercado estão verdes; a oferta-semente está no registry. A próxima fase é a [`02-avatar-voc`](02-avatar-voc.md), que parte do mercado-alvo recortado e do nível de consciência para minerar a voz certa.
