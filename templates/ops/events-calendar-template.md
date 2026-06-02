---
id: template.ops.events-calendar
title: "Events Calendar — Schema do Calendário de Eventos do Lançamento"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: events-logistics-coordinator
consumes: [template.ops.launch-phases, template.core.offer-book-master]
produces: [data.registry.decision]
frameworks: [launch/runway-and-phases, launch/cart-open-close, launch/perfect-webinar]
checklists: [events-logistics-checklist, launch/launch-phase-readiness-gate]
registries: [decision-registry, control-registry]
tags: [template, csv-schema, events-calendar, calendario, ops, logistica, lancamento]
---

# Events Calendar — Schema do Calendário de Eventos

Este `.md` documenta o schema de [`events-calendar-template.csv`](events-calendar-template.csv), o **calendário de eventos** do lançamento: cada marco com data, dono, onde acontece, o que sai pronto e o estado. Uma linha por evento, em ordem de data. O CSV é a fonte de verdade da agenda; este documento explica cada coluna. O `events-logistics-coordinator` é dono dos dois arquivos e usa a agenda para reservar salas, plataformas e gente antes de cada marco.

## Como usar
- **Agente dono:** `events-logistics-coordinator`. Co-lido pelo [`launch-producer`](../../agents/launch-producer.md) (que amarra cada evento à pista e à fase) e pelo [`affiliate-program-architect`](../../agents/affiliate-program-architect.md) (que encaixa a janela dos afiliados no calendário).
- **Task:** preenchido na produção do lançamento, depois que as fases existem em [`launch-phases-template`](launch-phases-template.md). Lido por todo o squad para saber o que acontece, quando e quem responde.
- **Quando:** o coordenador monta o calendário assim que a runway está definida. Aplica o [`runway-and-phases`](../../frameworks/launch/runway-and-phases.md) para a ordem dos marcos e o [`cart-open-close`](../../frameworks/launch/cart-open-close.md) para travar abertura e fechamento do carrinho.
- **Como editar o CSV:** abra em editor de texto ou planilha. A primeira linha é o header `snake_case` — **não traduza nem reordene as colunas**. Adicione uma linha por evento, em ordem de data. Datas no formato `AAAA-MM-DD`. Campos com vírgula vão entre aspas (`"..."`). Não ponha comentário no CSV — a documentação vive aqui.
- O gate [`events-logistics-checklist`](../../checklists/events-logistics-checklist.md) confere que todo evento tem dono, hosting e entregável. O [`launch-phase-readiness-gate`](../../checklists/launch/launch-phase-readiness-gate.md) confere que os marcos de cada fase estão prontos antes da fase começar.

## Schema
Uma linha por coluna do CSV: nome, tipo, valores aceitos, agente-fonte e exemplo.

| Coluna | Tipo | Valores aceitos | Agente-fonte | Exemplo |
|---|---|---|---|---|
| `data` | data (`AAAA-MM-DD`) | a data do evento, ISO; ordena o calendário | events-logistics-coordinator | `2026-06-03` |
| `evento` | string (slug) | o nome do marco (aquecimento-da-lista, webinar-de-abertura, fechamento-do-carrinho) | events-logistics-coordinator | `webinar-de-abertura` |
| `dono` | ref (agent-id) | o agente ou pessoa responsável pelo evento | events-logistics-coordinator | `launch-producer` |
| `hosting` | string (slug) | onde o evento acontece (zoom-webinar, email-marketing, checkout-stripe) | events-logistics-coordinator | `zoom-webinar` |
| `entregavel` | string | o que precisa estar pronto para o evento, em uma frase | events-logistics-coordinator | `"run-of-show e sala configurada"` |
| `status` | enum | `planejado` `confirmado` `concluido` `cancelado` | events-logistics-coordinator | `confirmado` |

## Exemplo
Calendário de amostra (lançamento do Motor 72h), três eventos preenchidos:

```csv
data,evento,dono,hosting,entregavel,status
2026-05-28,aquecimento-da-lista,launch-producer,email-marketing,"sequencia de 3 emails de pre-aquecimento",confirmado
2026-06-03,webinar-de-abertura,events-logistics-coordinator,zoom-webinar,"run-of-show e sala configurada",confirmado
2026-06-07,fechamento-do-carrinho,launch-producer,checkout-stripe,"pagina de carrinho com deadline real",planejado
```

Leitura: os três marcos sobem em ordem de data, do aquecimento ao fechamento. Cada um tem dono nomeado, um hosting concreto e um entregável claro. O fechamento do carrinho carrega o deadline real, alinhado ao [`cart-open-close`](../../frameworks/launch/cart-open-close.md) e à escassez verdadeira.

## DoD
O calendário está pronto quando: (1) o header do CSV é **idêntico** ao schema, em `snake_case`, sem coluna renomeada ou reordenada; (2) os eventos cobrem a runway inteira, em ordem de data, sem buraco entre fases; (3) todo evento tem `dono` nomeado, satisfazendo o [`events-logistics-checklist`](../../checklists/events-logistics-checklist.md); (4) todo evento tem `hosting` concreto e `entregavel` claro, sem `{{placeholder}}` solto; (5) cada fase abre só quando seus marcos estão prontos, satisfazendo o [`launch-phase-readiness-gate`](../../checklists/launch/launch-phase-readiness-gate.md); (6) a data de abertura e a de fechamento do carrinho são reais e únicas, e qualquer escassez citada é **100% verdadeira** (`truthful_scarcity`), alinhada à [política de compliance](../../docs/compliance-policy.md); (7) o CSV está limpo (sem comentário, sem frontmatter). A versão final do calendário vira uma decisão registrada no [`decision-registry`](../../data/registries/decision-registry.md).
