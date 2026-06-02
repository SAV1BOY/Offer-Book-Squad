---
id: project.offer-book-project.04-mechanism
title: "Fase 04 — Mecanismo Único"
type: project-phase
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
consumes:
  - artifact.market-brief
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - artifact.proof-bank
  - data.registry.objection
produces:
  - artifact.mechanism-sheet
  - decision.mechanism-name
tags: [project-phase, offer-architecture, mecanismo, unique-mechanism, naming, prova, d2]
---

# Fase 04 — Mecanismo Único

## Objetivo da Fase
Achar a causa-raiz do problema e a causa-raiz da solução, contrastá-las velho × novo e batizar o mecanismo com um nome próprio, crível, provado e comprimido em uma frase. O estado-pronto é o núcleo conceitual do qual todo o resto deriva: o avatar lê a frase, entende e acredita na primeira leitura. Esta fase abre a camada D2. O mecanismo nomeado vira matéria-prima do valor (Fase 05), do money model (Fase 06), da Big Idea (Fase 08) e do posicionamento. Sem mecanismo com lastro, nada a jusante tem âncora.

## Critério de Entrada
A Fase 01 entrega o `artifact.market-brief` (sofisticação e consciência com evidência, mecanismos dos concorrentes já em mercado, o claim saturado). A Fase 02 entrega o avatar, o banco de VOC e a causa que o avatar culpa hoje. A Fase 03 entrega o `artifact.proof-bank` e o [`objection-registry`](../../data/registries/objection-registry.md) com a objeção dominante. Pré-condição: o diagnóstico de mercado está verde. Se a sofisticação é 1-2, sinalizo que talvez nem precise de mecanismo nomeado e devolvo ao chief. Sem objeção dominante, não prossigo. Commodity pura sem diferença real de método: recuso fabricar mecanismo falso e escalono. O [`offer-registry`](../../data/registries/offer-registry.md) é a fonte que esta fase escreve.

## Agentes & Tasks
- **Task [`define-mechanism`](../../tasks/offer-architecture/define-mechanism.md)** — dono [`mechanism-architect`](../../agents/mechanism-architect.md). Produz o porquê funciona. Sem poder de veto; suas flags informam os vetos do value-engineer e do compliance.

## Passos
1. Ache a causa-raiz do problema com [`unique-mechanism`](../../frameworks/unique-mechanism.md) (5 Whys): desça do sintoma a um fator sistêmico reposicionável.
2. Ache a causa-raiz da solução: isole o passo causal que muda o resultado e confirme o lastro no `proof-registry`.
3. Valide a alavanca com [`value-equation`](../../frameworks/value-equation.md): o mecanismo move ≥1 alavanca real (Sonho, Probabilidade, Tempo, Esforço)? Se não move, é só rótulo.
4. Monte a tabela velho × novo por dimensão — o contraste que o positioning herda.
5. Batize com Tree-of-Thoughts, calibrando pela sofisticação (estágio 3 introduz, 4 eleva): ≥3 nomes pontuados por novidade, credibilidade, simplicidade e reposicionamento da culpa.
6. Comprima em uma frase de 3ª série que o avatar entende e acredita.
7. Self-verify com red-team: a cadeia causal está completa? O mecanismo difere dos concorrentes? Cada elo tem lastro? "O que o compliance e o value-engineer reprovariam?"
8. Registre o mecanismo no `offer-registry` (status provado só após o gate de prova verde) e passe os três gates.

## Artefatos Produzidos
- `artifact.mechanism-sheet` — nome próprio, problema-raiz, solução-raiz, tabela velho × novo, alavancas movidas, frase única, sofisticação-alvo, prova, status.
- `decision.mechanism-name` — o nome travado com o motivo.
- Registry escrito: [`offer-registry`](../../data/registries/offer-registry.md).

## Gates
- [`mechanism/mechanism-naming-gate`](../../checklists/mechanism/mechanism-naming-gate.md)
- [`mechanism/mechanism-proof-gate`](../../checklists/mechanism/mechanism-proof-gate.md)
- [`mechanism/mechanism-one-sentence-gate`](../../checklists/mechanism/mechanism-one-sentence-gate.md)

## Critério de Saída
A cadeia causal está completa do sintoma à raiz; o mecanismo é diferente dos concorrentes; cada elo tem lastro no `proof-registry`; o mecanismo move ≥1 alavanca declarada; a frase passa no teste de 1ª leitura; os três gates de mecanismo estão verdes; o registro tem status provado. A próxima fase é a [`05-value-equation`](05-value-equation.md), que recebe o mecanismo nomeado como insumo central da oferta e as alavancas que ele já move.
