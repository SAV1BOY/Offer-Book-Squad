---
id: checklist.big-idea.big-idea-relevant-proprietary-gate
title: "Gate — Relevante e Proprietária (os outros dois dos cinco critérios)"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [big-idea-generator, big-idea-architect/big-idea-scoring, big-idea-architect/promise-hook-villain]
registries: [big-idea-registry, objection-registry]
tags: [gate, big-idea, relevante, proprietaria, mecanismo, vilao, d3]
---

# Gate — Relevante e Proprietária

## Propósito
Este gate prova os dois critérios que a [`big-idea-new-big-credible-gate`](big-idea-new-big-credible-gate.md) não cobre: a Big Idea é **Relevante** (acerta a dor/desejo dominante do avatar, no idioma dele) e **Proprietária** (só esta marca pode dizê-la, porque está ancorada no mecanismo único). Relevância é o que faz a ideia ser sobre o leitor e não sobre o produto; sem ela, a tese é tangencial e o tráfego queima. Propriedade é o que defende a margem: uma ideia que qualquer concorrente diria é commodity, e o agente desempata empates justamente por Proprietária. Este gate também checa que a ideia **não bate de frente com uma objeção dominante sem resposta** e que o **vilão culpa uma causa externa**, não o avatar — copy que culpa o leitor não vende. Ele fecha, com o gate irmão, a rubrica dos cinco critérios.

## Dono & Escopo
- **owner_agent:** `big-idea-architect` (**tem poder de veto**: ideia genérica — sem mecanismo único por trás — ou que falha em Relevante/Proprietária é reprovação).
- **Artefato inspecionado:** os `scores` (relevante, proprietária) e o campo `vilao`/`mecanismo_ref` da Big Idea `locked` no [`big-idea-registry`](../../data/registries/big-idea-registry.md), cruzados com as objeções dominantes do [`objection-registry`](../../data/registries/objection-registry.md).

## Condição de Passagem
A Big Idea pontua acima de 2 em Relevante e Proprietária, está ancorada no mecanismo único, culpa uma causa externa e não colide com uma objeção dominante sem resposta.

## Itens
1. **Relevante > 2.** Verificar: a ideia acerta a emoção/desejo dominante do VOC, no idioma do avatar; a nota de Relevante é ≥ 3.
2. **Proprietária > 2.** Verificar: só esta marca pode dizer a ideia, por estar ancorada no mecanismo único; a nota de Proprietária é ≥ 3.
3. **Nenhum dos dois ≤ 2.** Verificar: nem Relevante nem Proprietária estão em 1 ou 2 — um critério fraco reprova o gate.
4. **Mecanismo amarrado.** Verificar: a ideia aponta para o `mecanismo_ref` do mechanism-sheet — promessa sem "por quê" é reprovação.
5. **Vilão é causa externa.** Verificar: o `vilao` é uma causa externa (um sinal, um sistema, um conselho errado), não o avatar ("você é preguiçoso").
6. **Não colide com objeção sem resposta.** Verificar: a tese não bate de frente com uma objeção dominante do `objection-registry` que fique sem réplica.
7. **Falável só por esta oferta.** Verificar: trocar o nome da marca pela do concorrente torna a frase falsa ou vazia — sinal de propriedade real.

## Evidência Exigida
Para marcar ✅: linkar a matriz de pontuação no `big-idea-registry` com as notas de Relevante e Proprietária e suas justificativas (itens 1–3, 7), o `mecanismo_ref` que ancora a ideia (item 4), o `vilao` como causa externa (item 5) e o cruzamento com o `objection-registry` mostrando que nenhuma objeção dominante fica sem resposta (item 6).

## Protocolo de Falha
Item vermelho → **veto**: o `big-idea-architect` reprova. Proprietária baixa → volta ao mechanism-sheet e re-ancora no mecanismo único ([`mechanism-architect`](../../agents/mechanism-architect.md)). Relevante baixa → reabre o VOC com o [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md). Vilão que culpa o avatar → reescreve para causa externa. Re-entrada: re-pontua ou re-ideia e re-submete. Mudança de mecanismo ou de vilão reabre este gate.

## Links
- Gates irmãos: [`big-idea-single-gate`](big-idea-single-gate.md) · [`big-idea-new-big-credible-gate`](big-idea-new-big-credible-gate.md) · [`big-idea-awareness-fit-gate`](big-idea-awareness-fit-gate.md) · [`big-idea-meta-angle-gate`](big-idea-meta-angle-gate.md)
- Frameworks: [`big-idea-generator`](../../frameworks/big-idea-generator.md) · [`big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md) · [`promise-hook-villain`](../../frameworks/big-idea-architect/promise-hook-villain.md)
- Registries: [`big-idea-registry`](../../data/registries/big-idea-registry.md) · [`objection-registry`](../../data/registries/objection-registry.md)
- Agentes: [`big-idea-architect`](../../agents/big-idea-architect.md) · [`mechanism-architect`](../../agents/mechanism-architect.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
