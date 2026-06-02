---
id: template.ops.asset-inventory-tracker
title: "Asset Inventory Tracker — Schema do Inventário de Ativos do Lançamento"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: events-logistics-coordinator
consumes: [template.ops.launch-phases, template.ops.run-of-show]
produces: [data.registry.control]
frameworks: [launch/runway-and-phases, launch/surge-ops]
checklists: [events-logistics-checklist, launch/launch-phase-readiness-gate]
registries: [control-registry, decision-registry]
tags: [template, csv-schema, asset-inventory, ativos, ops, logistica, lancamento]
---

# Asset Inventory Tracker — Schema do Inventário de Ativos

Este `.md` documenta o schema de [`asset-inventory-tracker-template.csv`](asset-inventory-tracker-template.csv), o **inventário de ativos** do lançamento: cada peça (vídeo, e-mail, página) com tipo, dono, onde mora, quando entrega e o estado. Uma linha por ativo. O CSV é a fonte de verdade do que existe e do que falta; este documento explica cada coluna. O `events-logistics-coordinator` é dono dos dois arquivos e usa o inventário para garantir que nada chega tarde no dia do lançamento.

## Como usar
- **Agente dono:** `events-logistics-coordinator`. Co-lido pelo [`launch-producer`](../../agents/launch-producer.md) (que cruza cada ativo com a pista do [`run-of-show`](run-of-show-template.csv)) e pelos autores de cada peça (que atualizam o `status`).
- **Task:** preenchido na produção do lançamento e atualizado a cada entrega. Lido na véspera para confirmar que todo ativo da pista está pronto e hospedado.
- **Quando:** o coordenador abre o inventário assim que a lista de peças do lançamento existe. Aplica o [`runway-and-phases`](../../frameworks/launch/runway-and-phases.md) para amarrar cada entrega a uma fase e o [`surge-ops`](../../frameworks/launch/surge-ops.md) para ter um plano se um ativo atrasa.
- **Como editar o CSV:** abra em editor de texto ou planilha. A primeira linha é o header `snake_case` — **não traduza nem reordene as colunas**. Adicione uma linha por ativo. Datas no formato `AAAA-MM-DD`. Campos com vírgula vão entre aspas (`"..."`). Não ponha comentário no CSV — a documentação vive aqui.
- O gate [`events-logistics-checklist`](../../checklists/events-logistics-checklist.md) confere que todo ativo tem dono, hosting e data de entrega. O [`launch-phase-readiness-gate`](../../checklists/launch/launch-phase-readiness-gate.md) confere que os ativos de uma fase estão entregues antes de a fase começar.

## Schema
Uma linha por coluna do CSV: nome, tipo, valores aceitos, agente-fonte e exemplo.

| Coluna | Tipo | Valores aceitos | Agente-fonte | Exemplo |
|---|---|---|---|---|
| `asset` | string (slug) | o nome da peça (vsl-de-abertura, sequencia-de-carrinho, pagina-de-checkout) | events-logistics-coordinator | `vsl-de-abertura` |
| `tipo` | string (slug) | o formato do ativo (video, email, landing-page, sms, anuncio) | events-logistics-coordinator | `video` |
| `dono` | ref (agent-id) | o agente que produz e entrega o ativo | events-logistics-coordinator | `vsl-webinar-scriptwriter` |
| `hosting` | string (slug) | onde o ativo mora (vimeo, plataforma-de-email, checkout-stripe) | tech-links-deliverability-engineer | `vimeo` |
| `data_entrega` | data (`AAAA-MM-DD`) | a data prometida de entrega, ISO | events-logistics-coordinator | `2026-06-01` |
| `status` | enum | `em-producao` `em-revisao` `entregue` `publicado` | events-logistics-coordinator | `entregue` |

## Exemplo
Inventário de amostra (lançamento do Motor 72h), três ativos preenchidos:

```csv
asset,tipo,dono,hosting,data_entrega,status
vsl-de-abertura,video,vsl-webinar-scriptwriter,vimeo,2026-06-01,entregue
sequencia-de-carrinho,email,email-sms-sequence-writer,plataforma-de-email,2026-06-02,em-revisao
pagina-de-checkout,landing-page,funnel-architect,checkout-stripe,2026-06-03,em-producao
```

Leitura: cada ativo tem um dono nomeado, um tipo claro, um hosting concreto e uma data de entrega. O `status` mostra de relance o que já está pronto (entregue), o que está em fila (em-revisao) e o que ainda corre (em-producao). O coordenador cruza esta lista com o [`run-of-show`](run-of-show-template.csv) para confirmar que nenhum bloco da pista fica sem o ativo dele.

## DoD
O inventário está pronto quando: (1) o header do CSV é **idêntico** ao schema, em `snake_case`, sem coluna renomeada ou reordenada; (2) toda peça citada na pista do [`run-of-show`](run-of-show-template.csv) e no fluxo de venda tem uma linha aqui; (3) todo ativo tem `dono` nomeado, satisfazendo o [`events-logistics-checklist`](../../checklists/events-logistics-checklist.md); (4) todo ativo tem `hosting` concreto e `data_entrega` real, sem `{{placeholder}}` solto; (5) na entrada de cada fase, os ativos da fase têm `status = entregue` ou `publicado`, satisfazendo o [`launch-phase-readiness-gate`](../../checklists/launch/launch-phase-readiness-gate.md); (6) ativos com claim aprovado pelo [`compliance-auditor`](../../agents/compliance-auditor.md) só viram `publicado` depois do veredito; (7) o CSV está limpo (sem comentário, sem frontmatter). O estado de cada ativo espelha o [`control-registry`](../../data/registries/control-registry.md), ligado ao `asset_id`.
