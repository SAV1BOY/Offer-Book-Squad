---
id: data.backlog.improvement-backlog-template
title: "Backlog de Melhoria / Kaizen (EXEMPLO ILUSTRATIVO / Template)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
consumes: [data.registry.lessons-learned]
produces: [data.registry.decision]
frameworks: [proof-to-claim-chain, money-model-sequence]
checklists: [final-delivery-checklist]
registries: [lessons-learned-registry, decision-registry]
tags: [template, backlog, kaizen, improvement, roi, priority]
---

# Backlog de Melhoria / Kaizen (EXEMPLO ILUSTRATIVO / Template)

> **AVISO:** Este arquivo é um **template ilustrativo (seed)**. Os itens e o ROI são **fictícios**, só para mostrar o formato. Não use como fato. Cada período real copia este backlog, renomeia para `improvement-backlog-<periodo>.md`, apaga o aviso e registra uma linha por item de melhoria.

## Como usar
- **Agente dono:** [`knowledge-librarian`](../../agents/knowledge-librarian.md) (cura e prioriza); o [`offerbook-chief`](../../agents/offerbook-chief.md) adota as melhorias prioritárias no próximo intake. Cada item tem um **dono nomeado** que o executa.
- **Task:** alimentado na `memory-update` (quando as lições são consolidadas) e lido na `intake-and-scope` do próximo lançamento — é o backlog que **alimenta o próximo intake**.
- **Quando:** uma linha por item de melhoria. Cada item nasce de uma lição do [`lessons-learned-registry`](../registries/lessons-learned-registry.md) e é fechado quando vira melhoria entregue. Fecha o ciclo de `memory_before_repetition`.
- ROI estimado em escala simples (baixo/médio/alto) ou número, quando houver. Item sem `origem` (lição) ou sem `dono` = não entra na fila.

## Campos & Instruções
- **{{ITEM}}** — a melhoria proposta, em uma frase acionável.
- **{{ORIGEM}}** — qual lição ou lançamento gerou o item (link ao [`lessons-learned-registry`](../registries/lessons-learned-registry.md)).
- **{{ROI_ESTIMADO}}** — o retorno esperado da melhoria (`baixo` \| `médio` \| `alto`, ou número).
- **{{PRIORIDADE}}** — `P0` \| `P1` \| `P2` (ordena a fila; P0 entra já no próximo intake).
- **{{DONO}}** — o agente responsável por entregar a melhoria (id de [`config.yaml`](../../config.yaml)).
- **{{STATUS}}** — `proposto` \| `priorizado` \| `em-andamento` \| `entregue`.

## O Template
```
# BACKLOG DE MELHORIA (KAIZEN) — {{PERIODO}}
Owner: knowledge-librarian · Atualizado: {{DATA}}

| item | origem | ROI estimado | prioridade | dono | status |
|------|--------|--------------|------------|------|--------|
| {{ITEM}} | {{ORIGEM}} | {{ROI_ESTIMADO}} | {{PRIORIDADE}} | {{DONO}} | {{STATUS}} |
```

## Exemplo preenchido
> **# BACKLOG DE MELHORIA (KAIZEN) — 2026-Q2**
> Owner: knowledge-librarian · Atualizado: 2026-06-02
>
> | item | origem | ROI estimado | prioridade | dono | status |
> |---|---|---|---|---|---|
> | Padronizar a prova social 40+ como bloco reutilizável _(ex.)_ | lição `ll-exemplo-prova` (Método X) | alto | P0 | proof-credibility-curator | priorizado |
> | Antecipar o teste de preço para antes do money model _(ex.)_ | lição `ll-exemplo-preco` (Método X) | médio | P1 | pricing-wtp-strategist | proposto |
> | Criar SMS de presença ao vivo no run-of-show padrão _(ex.)_ | lição `ll-exemplo-presenca` (Método X) | médio | P1 | launch-producer | em-andamento |
>
> Leitura: cada item nomeia a **lição de origem** (rastreável no [`lessons-learned-registry`](../registries/lessons-learned-registry.md)), o ROI esperado e a prioridade. O item P0 (bloco de prova social) entra já no próximo intake porque tem ROI alto e origem clara; quando adotado, vira decisão no [`decision-registry`](../registries/decision-registry.md) e pode promover um padrão de ouro para [`winners/`](../winners/).

## DoD do entregável
O backlog está pronto quando: (1) cada item tem **origem** (lição ou lançamento), ROI estimado, prioridade e **dono nomeado**, sem `{{PLACEHOLDER}}` solto; (2) toda `origem` resolve para uma lição no [`lessons-learned-registry`](../registries/lessons-learned-registry.md); (3) a fila está **ordenada por prioridade**, com os P0 prontos para o próximo `intake-and-scope`; (4) o `dono` resolve para um agente real de [`config.yaml`](../../config.yaml); (5) item adotado liga à decisão no [`decision-registry`](../registries/decision-registry.md); (6) o texto está em voz ativa e presente, 3ª série. O backlog é consolidado na `memory-update` (satisfazendo o [`final-delivery-checklist`](../../checklists/final-delivery-checklist.md)) e relido a cada novo lançamento pelo `offerbook-chief`.
