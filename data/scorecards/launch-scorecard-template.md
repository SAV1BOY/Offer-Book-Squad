---
id: data.scorecards.launch-scorecard-template
title: "Scorecard de Lançamento (EXEMPLO ILUSTRATIVO / Template)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
consumes: [template.core.offer-book-master]
produces: [data.registry.decision]
frameworks: [value-equation, money-model-sequence, proof-to-claim-chain, big-idea-generator, scarcity-urgency-engine]
checklists: [offer-quality-scorecard-checklist, offer-book-stack/offer-book-dod-gate]
registries: [decision-registry, offer-registry, big-idea-registry, claim-registry, proof-registry]
tags: [template, scorecard, qualidade, gold, sota, verdict, gating]
---

# Scorecard de Lançamento (EXEMPLO ILUSTRATIVO / Template)

> **AVISO:** Este arquivo é um **template ilustrativo (seed)**. As notas e o veredito são **fictícios**, só para mostrar o formato. Não use como fato. Cada lançamento real copia este scorecard, renomeia para `scorecard-<caso>-<periodo>.md`, apaga o aviso e preenche cada dimensão com nota e evidência.

## Como usar
- **Agente dono:** [`offerbook-chief`](../../agents/offerbook-chief.md) (calcula e assina o veredito); o [`knowledge-librarian`](../../agents/knowledge-librarian.md) consolida na memória. O [`value-equation-engineer`](../../agents/value-equation-engineer.md) e o [`compliance-auditor`](../../agents/compliance-auditor.md) co-assinam as dimensões de valor e de escassez/prova.
- **Task:** preenchido em `assemble-offer-book`, depois que o Offer Book consolidado existe em [`offer-book-master`](../../templates/core/offer-book-master.md) e antes de liberar qualquer copy (é o placar do hard stop).
- **Quando:** uma passada por lançamento; repontuar inteiro a cada mudança de insumo. A régua de cálculo (pesos por dimensão, piso de 60%, porteira de escassez) é a do [`offer-quality-scorecard-checklist`](../../checklists/offer-quality-scorecard-checklist.md); o gate-espelho é o [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).
- Cada linha exige **evidência ligada** (registro ou framework), não opinião. Linha sem evidência = nota não vale = gate vermelho.

## Campos & Instruções
- **{{LANCAMENTO}}** — o nome do lançamento avaliado, ligado à oferta núcleo no [`offer-registry`](../registries/offer-registry.md).
- **{{DIMENSAO}}** — uma das cinco dimensões fixas: equação de valor, money model, prova, Big Idea, escassez verdadeira.
- **{{SCORE}}** — a nota **0–100** da dimensão (lida contra o peso: valor 30, money model 25, prova 20, Big Idea 15, escassez 10).
- **{{GATE}}** — o checklist/gate que sustenta a dimensão (ex.: `value-equation-checklist`).
- **{{EVIDENCIA}}** — o link à fonte da nota (registro, planilha de pontuação, framework).
- **{{VERDICT}}** — o veredito por dimensão e o total: **WEAK** (<80), **GOOD** (80–94), **GOLD** (≥95), **SOTA** (≥98).

## O Template
```
# SCORECARD DE LANCAMENTO — {{LANCAMENTO}}
Owner: offerbook-chief · Data: {{DATA}} · Status: {{STATUS}}

| Dimensão | Peso | Score 0-100 | Gate | Evidência | Verdict |
|----------|------|-------------|------|-----------|---------|
| Equação de valor | 30 | {{SCORE_VALOR}} | {{GATE_VALOR}} | {{EVID_VALOR}} | {{VERDICT_VALOR}} |
| Money model | 25 | {{SCORE_MM}} | {{GATE_MM}} | {{EVID_MM}} | {{VERDICT_MM}} |
| Prova | 20 | {{SCORE_PROVA}} | {{GATE_PROVA}} | {{EVID_PROVA}} | {{VERDICT_PROVA}} |
| Big Idea | 15 | {{SCORE_BI}} | {{GATE_BI}} | {{EVID_BI}} | {{VERDICT_BI}} |
| Escassez verdadeira | 10 | {{SCORE_ESC}} | {{GATE_ESC}} | {{EVID_ESC}} | {{VERDICT_ESC}} |
| **TOTAL** | **100** | {{TOTAL}} | offer-book-dod-gate | {{EVID_TOTAL}} | {{VERDICT_TOTAL}} |

Regra de veredito: GOLD >= 95, SOTA >= 98. Abaixo de 80 = WEAK; 80-94 = GOOD.
Porteira: escassez falsa zera a dimensão e VETA o lançamento, qualquer que seja o total.
```

## Exemplo preenchido
> **# SCORECARD DE LANCAMENTO — Método X (2026-Q2)**
> Owner: offerbook-chief · Data: 2026-06-02 · Status: aprovado
>
> | Dimensão | Peso | Score | Gate | Evidência | Verdict |
> |---|---|---|---|---|---|
> | Equação de valor | 30 | 92 _(ex.)_ | [`value-equation-checklist`](../../checklists/value-equation-checklist.md) | [`offer-registry`](../registries/offer-registry.md) `core-exemplo-90d` | GOOD |
> | Money model | 25 | 96 _(ex.)_ | [`money-model-checklist`](../../checklists/money-model-checklist.md) | [`offer-registry`](../registries/offer-registry.md) (4 partes) | GOLD |
> | Prova | 20 | 90 _(ex.)_ | [`proof-checklist`](../../checklists/proof-checklist.md) | [`proof-registry`](../registries/proof-registry.md) (90% claims) | GOOD |
> | Big Idea | 15 | 95 _(ex.)_ | [`big-idea-checklist`](../../checklists/big-idea-checklist.md) | [`big-idea-registry`](../registries/big-idea-registry.md) `metodo-x-exemplo` | GOLD |
> | Escassez verdadeira | 10 | 100 _(ex.)_ | [`compliance-checklist`](../../checklists/compliance-checklist.md) | 40 vagas reais de setup | GOLD |
> | **TOTAL** | **100** | **93 _(ex.)_** | [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) | [`decision-registry`](../registries/decision-registry.md) | **GOOD** |
>
> Leitura: total 93 = **GOOD** — passa no piso de 80 e nenhuma dimensão fica abaixo de 60% do peso, então a fundação vira copy. Para virar **GOLD** o lançamento precisa subir prova e valor até o total cruzar 95.

## DoD do entregável
O scorecard está pronto quando: (1) as cinco dimensões têm nota 0–100 com **evidência ligada**, sem `{{PLACEHOLDER}}` solto; (2) cada nota deriva da régua do [`offer-quality-scorecard-checklist`](../../checklists/offer-quality-scorecard-checklist.md), com os pesos corretos; (3) **nenhuma dimensão fica abaixo de 60% do seu peso**; (4) a porteira de escassez foi checada pelo `compliance-auditor` — escassez falsa zera e veta, conforme a [política de compliance](../../docs/compliance-policy.md) (`truthful_scarcity`); (5) o total foi somado e o veredito segue a regra **GOLD ≥ 95, SOTA ≥ 98** (WEAK < 80, GOOD 80–94); (6) o texto está em voz ativa e presente, 3ª série. A nota final assinada é gravada como decisão no [`decision-registry`](../registries/decision-registry.md) e libera (ou segura) a copy pelo [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).
