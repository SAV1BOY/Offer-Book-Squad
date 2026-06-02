---
id: data.handoffs.handoff-manifest-template
title: "Manifesto de Handoffs Cross-Squad (EXEMPLO ILUSTRATIVO / Template)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
consumes: [template.cross-squad.handoff-contract]
produces: [data.registry.decision]
frameworks: [offer-to-funnel-mapping, proof-to-claim-chain, power-of-one]
checklists: [cross-squad/cross-squad-handoff-quality, cross-squad/cross-squad-asset-validation, cross-squad/cross-squad-research-request-quality]
registries: [decision-registry, offer-registry]
tags: [template, handoff, manifest, cross-squad, rejection, reentry]
---

# Manifesto de Handoffs Cross-Squad (EXEMPLO ILUSTRATIVO / Template)

> **AVISO:** Este arquivo é um **template ilustrativo (seed)**. Os handoffs e as datas são **fictícios**, só para mostrar o formato. Não use como fato. Cada período real copia este manifesto, renomeia para `handoff-manifest-<periodo>.md`, apaga o aviso e registra uma linha por handoff.

## Como usar
- **Agente dono:** [`offerbook-chief`](../../agents/offerbook-chief.md) (controla as transições de fronteira); o [`compliance-auditor`](../../agents/compliance-auditor.md) co-assina quando o pacote leva claims e o [`knowledge-librarian`](../../agents/knowledge-librarian.md) consolida o log na memória.
- **Task:** atualizado sempre que um pacote sai para outro squad ou entra de outro, em qualquer task que cruze a fronteira (`cross_squad` em [`config.yaml`](../../config.yaml)).
- **Quando:** uma linha por handoff, no momento em que ele é enviado, e atualizada quando o destinatário aceita ou rejeita. Os três gates de fronteira regem a passagem: [`cross-squad-handoff-quality`](../../checklists/cross-squad/cross-squad-handoff-quality.md) (saída), [`cross-squad-asset-validation`](../../checklists/cross-squad/cross-squad-asset-validation.md) (entrada) e [`cross-squad-research-request-quality`](../../checklists/cross-squad/cross-squad-research-request-quality.md) (pedido de pesquisa).
- Cada handoff aponta para o contrato que o rege ([`handoff-contract-template`](../../templates/cross-squad/handoff-contract-template.md)) em `contract_ref` e para a decisão em `decided_in`. Rejeição exige `defeito` nomeado.

## Campos & Instruções
- **{{HANDOFF_ID}}** — id único do handoff em `kebab-case` (ex.: `ho-0001-offerbook-copy`).
- **{{DE_SQUAD}}** — squad de origem (nome de `config.yaml: cross_squad`, ex.: `offerbook`).
- **{{PARA_SQUAD}}** — squad de destino (ex.: `copy_squad`).
- **{{ARTEFATO}}** — o que foi entregue (ex.: offer book + Big Idea).
- **{{CONTRACT_REF}}** — link ao contrato preenchido que rege o handoff.
- **{{STATUS}}** — `enviado` \| `aceito` \| `rejeitado`.
- **{{DEFEITO}}** — o defeito nomeado quando `rejeitado`; `—` quando aceito.
- **{{DATA}}** — data do estado atual (`YYYY-MM-DD`).
- **{{DECIDED_IN}}** — `decision_id` da decisão de handoff no [`decision-registry`](../registries/decision-registry.md).

## O Template
```
# MANIFESTO DE HANDOFFS — {{PERIODO}}
Owner: offerbook-chief · Atualizado: {{DATA}}

| handoff_id | de_squad | para_squad | artefato | contract_ref | status | defeito | data | decided_in |
|------------|----------|------------|----------|--------------|--------|---------|------|------------|
| {{HANDOFF_ID}} | {{DE_SQUAD}} | {{PARA_SQUAD}} | {{ARTEFATO}} | {{CONTRACT_REF}} | {{STATUS}} | {{DEFEITO}} | {{DATA}} | {{DECIDED_IN}} |
```

## Exemplo preenchido
> **# MANIFESTO DE HANDOFFS — 2026-Q2**
> Owner: offerbook-chief · Atualizado: 2026-06-02
>
> | handoff_id | de_squad | para_squad | artefato | contract_ref | status | defeito | data | decided_in |
> |---|---|---|---|---|---|---|---|---|
> | `ho-0001-offerbook-copy` _(ex.)_ | offerbook | copy_squad | offer book + Big Idea + prova | [`handoff-contract`](../../templates/cross-squad/handoff-contract-template.md) | rejeitado | Big Idea sem prova ligada | 2026-05-20 | `dec-exemplo-0001` |
> | `ho-0002-offerbook-copy` _(ex.)_ | offerbook | copy_squad | offer book + Big Idea + prova (corrigido) | [`handoff-contract`](../../templates/cross-squad/handoff-contract-template.md) | aceito | — | 2026-05-22 | `dec-exemplo-0001` |
> | `ho-0003-advisory-offerbook` _(ex.)_ | advisory_board_squad | offerbook | crítica estratégica + flags de risco | [`handoff-contract`](../../templates/cross-squad/handoff-contract-template.md) | aceito | — | 2026-05-25 | `dec-exemplo-0001` |
>
> Leitura: o handoff `ho-0001` voltou rejeitado com o defeito **nomeado** (Big Idea sem prova ligada); o squad corrigiu e re-entrou como `ho-0002`, aceito dois dias depois. O `ho-0003` é um handoff de **entrada** (advisory → offerbook), que segue para validação pelo [`cross-squad-asset-validation`](../../checklists/cross-squad/cross-squad-asset-validation.md) antes de virar insumo. A linha de saída rejeitada nunca é apagada — é memória da fronteira.

## DoD do entregável
O manifesto está pronto quando: (1) cada handoff tem `handoff_id` único, origem e destino nomeados pelos nomes de `config.yaml`, sem `{{PLACEHOLDER}}` solto; (2) cada linha aponta para um `contract_ref` que resolve para um contrato preenchido ([`handoff-contract-template`](../../templates/cross-squad/handoff-contract-template.md)) e para um `decided_in` no [`decision-registry`](../registries/decision-registry.md); (3) todo `status: rejeitado` traz o **defeito nomeado**, não vago; (4) handoffs de saída passaram pelo [`cross-squad-handoff-quality`](../../checklists/cross-squad/cross-squad-handoff-quality.md) e os de entrada pelo [`cross-squad-asset-validation`](../../checklists/cross-squad/cross-squad-asset-validation.md); (5) reentradas aparecem como **nova linha**, sem apagar a rejeição original; (6) o texto está em voz ativa e presente, 3ª série. O log consolidado vira memória reutilizável pelo `knowledge-librarian`.
