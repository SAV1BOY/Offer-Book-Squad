---
id: data.case-studies.readme
title: "Data Store — Case Studies (Estudos de Caso)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [case-studies, proof, results, narrative, data-store]
---

# Data Store — Case Studies (Estudos de Caso)

## Propósito

Este diretório guarda os **estudos de caso** do squad — a narrativa completa de um lançamento ou de uma transformação de cliente, com o número e a prova. Um case responde "funcionou?" com história **e** evidência. Ele serve a dois usos: alimentar prova social para a copy ([`proof-registry`](../registries/proof-registry.md)) e ensinar o squad o que fazer de novo (`memory_before_repetition`).

A pasta cumpre `evidence_before_opinion`: um case não é depoimento solto, é resultado **datado, atribuído e verificável**. O `proof-credibility-curator` extrai a prova daqui; o `knowledge-librarian` guarda a lição; os escritores de copy usam a história (com permissão e sem inventar números).

## O que guardar

- **Cases de lançamento** (ex.: `case-metodo-x-2026q2.md`): contexto, o que foi feito, resultado, lição.
- **Cases de cliente/transformação** (antes → depois, com prova) para prova social.
- **Pós-mortem** de lançamento (o que deu certo, o que falhou, o que mudar).
- Cada case com **fonte da prova** (print, dashboard, depoimento assinado) e **permissão de uso**.

Não guardar aqui: a tabela de provas catalogadas (fica no [`proof-registry`](../registries/proof-registry.md)) nem as lições atômicas (vão para [`lessons-learned-registry`](../registries/lessons-learned-registry.md)). O case é a **narrativa**; o registro é a **linha**.

## Formato / Schema

Cada case é um `.md` com frontmatter (`type: doc`) e seções: contexto/avatar, desafio, o que foi feito, resultado (com número e fonte), lição e permissão de uso. Todo número factual **cita fonte** ou é marcado como `ilustrativo`. Depoimentos ficam entre aspas, atribuídos, com data e consentimento registrado.

## Como alimenta os agentes

- **Escrevem**: `knowledge-librarian` (consolida o case na memória/Blackbook), `proof-credibility-curator` (extrai e cataloga a prova), `offerbook-chief` (pós-mortem de lançamento).
- **Leem**: `vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `ad-creative-factory` (prova social para copy), `big-idea-architect` (a transformação que vira tese), `compliance-auditor` (confere que a prova lastreia o claim e tem permissão).
- **Ligações a registries**: alimenta [`proof-registry`](../registries/proof-registry.md) (a prova extraída) e [`claim-registry`](../registries/claim-registry.md) (o claim que a prova sustenta); lições viram linha em [`lessons-learned-registry`](../registries/lessons-learned-registry.md).

## Exemplo

Cases reais chegam pelo squad **DeepResearch** e pela operação do cliente. Um case ilustrativo seguiria o avatar de [`research/example-market-thesis.md`](../research/example-market-thesis.md) (emagrecimento feminino 40+): contexto, desafio, método aplicado, resultado **com fonte** e a lição — sempre com permissão de uso registrada. Esta pasta começa com apenas o README; os cases entram conforme os lançamentos acontecem.
