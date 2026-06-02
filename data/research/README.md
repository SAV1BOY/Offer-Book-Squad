---
id: data.research.readme
title: "Data Store — Pesquisa de Mercado (Research)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [research, market-thesis, voc, competitive-intel, deepresearch, data-store]
---

# Data Store — Pesquisa de Mercado (Research)

## Propósito

Este diretório guarda a **inteligência bruta de mercado** que alimenta a camada D1 do pipeline ([`ARCHITECTURE.md`](../../ARCHITECTURE.md) §3). É a porta de entrada do squad **DeepResearch**: teses de mercado, tamanho de mercado, voz do cliente (VOC) e inteligência competitiva chegam aqui antes de virarem avatar, mecanismo e oferta.

A pasta cumpre `evidence_before_opinion`: nenhuma decisão de oferta nasce de palpite. O `market-sophistication-analyst` lê estes arquivos para declarar **estágio de sofisticação** e **nível de consciência** do mercado. O `avatar-voc-investigator` minera os verbatims daqui para o banco de VOC. Sem pesquisa rastreável, o gate `market/market-sophistication-gate` não passa.

## O que guardar

- **Teses de mercado** (`market-thesis-*.md`): a leitura de um mercado — dor dominante, tamanho, tendência, players, lacuna.
- **Sínteses de VOC** vindas do DeepResearch (verbatims agrupados por dor/desejo/objeção).
- **Inteligência competitiva**: o que os concorrentes prometem, a que preço, com qual mecanismo.
- **Sizing**: TAM/SAM/SOM com fonte e data.
- **Tendências e gatilhos** de mercado (eventos, sazonalidade, mudança de regra).

Não guardar aqui: o avatar finalizado (vai para os templates de estratégia), claims já validados ([`claim-registry`](../registries/claim-registry.md)) nem provas catalogadas ([`proof-registry`](../registries/proof-registry.md)).

## Formato / Schema

Cada tese é um `.md` com frontmatter (`type: doc`, `layer: cross`, `owner_agent: market-sophistication-analyst` ou `avatar-voc-investigator`) e as seções: contexto, tamanho de mercado, sofisticação, consciência, dores/desejos, concorrência, lacuna e fontes. **Todo número factual cita fonte** (URL + data de acesso) ou é marcado como `aproximado/ilustrativo`. Verbatims ficam entre aspas com a origem.

## Como alimenta os agentes

- **Escrevem**: handoff do squad **DeepResearch** (`cross_squad.deepresearch_squad`, ver [`config.yaml`](../../config.yaml)); `market-sophistication-analyst` e `avatar-voc-investigator` refinam e anotam.
- **Leem**: `market-sophistication-analyst` (sofisticação + consciência), `avatar-voc-investigator` (VOC), `mechanism-architect` (lacuna que o mecanismo preenche), `positioning-lead-strategist` (categoria e concorrência), `offerbook-chief` (escopo).
- **Ligações a registries**: alimenta indiretamente [`offer-registry`](../registries/offer-registry.md) (via mecanismo) e [`objection-registry`](../registries/objection-registry.md) (objeções colhidas na VOC).

## Exemplo

Ver [`example-market-thesis.md`](example-market-thesis.md) — uma tese de mercado ilustrativa (emagrecimento feminino 40+), claramente marcada como amostra, mostrando o nível de detalhe e a citação de fontes esperados.
