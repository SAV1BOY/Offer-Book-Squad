---
id: data.risk-assumptions.assumptions-log-template
title: "Log de Premissas (EXEMPLO ILUSTRATIVO / Template)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
produces: [data.registry.decision]
frameworks: [value-equation, money-model-sequence, proof-to-claim-chain]
checklists: [offer-book-stack/offer-book-dod-gate]
registries: [decision-registry, offer-registry, proof-registry]
tags: [template, assumptions, confidence, validation, owner]
---

# Log de Premissas (EXEMPLO ILUSTRATIVO / Template)

> **AVISO:** Este arquivo é um **template ilustrativo (seed)**. As premissas e os donos são **fictícios**, só para mostrar o formato. Não use como fato. Cada lançamento real copia este log, renomeia para `assumptions-log-<caso>.md`, apaga o aviso e registra uma linha por premissa.

## Como usar
- **Agente dono:** [`offerbook-chief`](../../agents/offerbook-chief.md) (decide quais premissas precisam virar fato antes da copy); cada premissa tem um **dono nomeado** que a valida. O [`knowledge-librarian`](../../agents/knowledge-librarian.md) consolida o log na memória.
- **Task:** preenchido desde o intake e atualizado quando uma premissa é validada ou cai; revisado no DoD pelo [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).
- **Quando:** uma linha por premissa. Premissa é uma aposta declarada (`evidence_before_opinion`): enquanto `validada? = não`, o plano que depende dela carrega risco. Validação por número liga à fonte em [`metrics/`](../metrics/), [`conversion-data/`](../conversion-data/) ou [`proof-registry`](../registries/proof-registry.md).
- Confiança em escala simples (baixa/média/alta). Premissa de alto impacto e baixa confiança é prioridade de validação.

## Campos & Instruções
- **{{PREMISSA}}** — o que estamos assumindo como verdade, em uma frase.
- **{{BASE}}** — em que essa premissa se apoia (dado, analogia, opinião de especialista, histórico).
- **{{CONFIANCA}}** — `baixa` \| `média` \| `alta` (o quanto confiamos na premissa).
- **{{VALIDADA}}** — `sim` \| `não` \| `em-teste` (já virou fato medido?).
- **{{DONO}}** — o agente responsável por validar a premissa (id de [`config.yaml`](../../config.yaml)).

## O Template
```
# LOG DE PREMISSAS — {{CASO}}
Owner: offerbook-chief · Atualizado: {{DATA}}

| premissa | base | confiança | validada? | dono |
|----------|------|-----------|-----------|------|
| {{PREMISSA}} | {{BASE}} | {{CONFIANCA}} | {{VALIDADA}} | {{DONO}} |
```

## Exemplo preenchido
> **# LOG DE PREMISSAS — Método X**
> Owner: offerbook-chief · Atualizado: 2026-06-02
>
> | premissa | base | confiança | validada? | dono |
> |---|---|---|---|---|
> | A lista própria converte a ≥6% no núcleo _(ex.)_ | teste anterior do mesmo avatar | média | em-teste | money-model-designer |
> | O avatar paga R$ 2497 sem objeção de preço _(ex.)_ | faixa do Van Westendorp (R$ 1750–2400) | média | não | pricing-wtp-strategist |
> | A prova social 40+ derruba a objeção "não funciona para mim" _(ex.)_ | verbatims do VOC + control anterior | alta | sim | proof-credibility-curator |
>
> Leitura: cada premissa nomeia a **base** e o nível de **confiança**, e diz se já foi validada. A premissa de preço fica `validada? = não` e `confiança média` — é prioridade de validação porque sustenta o money model inteiro; quando virar fato, liga à fonte em [`pricing-tests/`](../pricing-tests/). A premissa de prova já é `sim`, com lastro em [`proof-registry`](../registries/proof-registry.md).

## DoD do entregável
O log está pronto quando: (1) cada premissa tem base, confiança, estado de validação e **dono nomeado**, sem `{{PLACEHOLDER}}` solto; (2) toda premissa de **alto impacto** tem um caminho de validação declarado, não fica como aposta cega; (3) o `dono` resolve para um agente real de [`config.yaml`](../../config.yaml); (4) premissa validada aponta para a fonte do número em [`metrics/`](../metrics/), [`conversion-data/`](../conversion-data/) ou [`proof-registry`](../registries/proof-registry.md); (5) premissa que vira decisão material liga ao [`decision-registry`](../registries/decision-registry.md); (6) o texto está em voz ativa e presente, 3ª série. O log é revisado no [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) e consolidado na memória pelo `knowledge-librarian`.
