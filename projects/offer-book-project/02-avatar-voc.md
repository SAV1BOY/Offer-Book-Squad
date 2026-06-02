---
id: project.offer-book-project.02-avatar-voc
title: "Fase 02 — Avatar & Voz do Cliente"
type: project-phase
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
consumes:
  - artifact.market-brief
  - decision.awareness-level
  - template.strategy.avatar-icp
  - template.strategy.voc-verbatim-bank
produces:
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - artifact.objection-belief-map
tags: [project-phase, intelligence, avatar, icp, voc, verbatim, objecao, jtbd, d1]
---

# Fase 02 — Avatar & Voz do Cliente

## Objetivo da Fase
Reconstruir o comprador na voz literal dele. Esta fase entrega o avatar/ICP por segmento, com ≥10 verbatims literais por segmento, a emoção dominante nomeada e o mapa de objeções/falsas crenças (mais a DMU, se B2B). O estado-pronto é o ponto em que a copy soará como a cabeça do cliente e nenhuma objeção ficará sem resposta. O mapa de objeções desta fase é a aresta que destrava a Fase 03.

## Critério de Entrada
A Fase 01 entrega o `artifact.market-brief` com o mercado-alvo recortado, o nível de consciência (1-5) e a célula da matriz. Pré-condição: existe um mercado-alvo definido e um nível de consciência declarado — a consciência muda quais objeções pesam mais. Se o mercado abriga dois públicos com vozes incompatíveis, a fase segmenta e sinaliza. Sem fonte de VOC acessível, o banco é marcado abaixo do piso e sinalizado — verbatim fabricado é falha grave. O [`objection-registry`](../../data/registries/objection-registry.md) é a fonte que esta fase escreve.

## Agentes & Tasks
- **Task [`build-avatar-voc`](../../tasks/intelligence/build-avatar-voc.md)** — dono [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md).

## Passos
1. Segmente o mercado-alvo lendo uma amostra de VOC; divida em 1–3 segmentos com voz coerente.
2. Minere VOC com [`voc-mining`](../../frameworks/avatar-voc-investigator/voc-mining.md): ≥10 verbatims literais por segmento, com fonte rastreável. Paráfrase não conta.
3. Nomeie a emoção dominante via Tree-of-Thoughts, ancorada em ≥3 verbatims.
4. Mapeie o Job To Be Done com [`jtbd`](../../frameworks/positioning/jtbd.md): funcional, emocional, social.
5. Mapeie objeções e falsas crenças com [`objection-belief-mapping`](../../frameworks/avatar-voc-investigator/objection-belief-mapping.md): para cada "não", a falsa crença-raiz.
6. Se B2B, mapeie a DMU por papel (econômico, técnico, bloqueador, influenciador): medo, objeção e o que cada um precisa ouvir.
7. Faça o self-verify (cada segmento com ≥10 verbatims, emoção ancorada, cada objeção com crença-raiz).
8. Escreva cada objeção no `objection-registry` e alimente o `proof-registry` com depoimentos. Passe os três gates de avatar.

## Artefatos Produzidos
- `artifact.avatar-icp` — avatar/ICP por segmento (demografia mínima + contexto vivo).
- `artifact.voc-verbatim-bank` — ≥10 verbatims literais por segmento com fonte + emoção dominante ancorada.
- `artifact.objection-belief-map` — objeção → falsa crença → categoria → severidade (e a DMU por papel, se B2B).
- Registry escrito: [`objection-registry`](../../data/registries/objection-registry.md).

## Gates
- [`avatar/avatar-voc-verbatim-gate`](../../checklists/avatar/avatar-voc-verbatim-gate.md)
- [`avatar/avatar-dominant-emotion-gate`](../../checklists/avatar/avatar-dominant-emotion-gate.md)
- [`avatar/avatar-objection-map-gate`](../../checklists/avatar/avatar-objection-map-gate.md) — a aresta-chave que destrava a Fase 03.

## Critério de Saída
Cada segmento tem ≥10 verbatims literais; a emoção dominante de cada um está nomeada e ancorada; cada objeção tem falsa crença, categoria e severidade; se B2B, a DMU cobre todos os papéis; os três gates de avatar estão verdes; as objeções estão no registry. A próxima fase é a [`03-proof`](03-proof.md), que recebe o mapa de objeções para casar prova contra cada objeção e cada claim.
