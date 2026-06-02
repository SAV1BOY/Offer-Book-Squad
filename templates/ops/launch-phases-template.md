---
id: template.ops.launch-phases
title: "Launch Phases — As Fases da Runway do Lançamento"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
consumes: [template.ops.launch-memo, template.core.offer-book-master]
produces: [template.ops.run-of-show, template.ops.events-calendar]
frameworks: [launch/runway-and-phases, launch/product-launch-formula, launch/cart-open-close, launch/surge-ops]
checklists: [launch-memo-checklist, launch/launch-phase-readiness-gate, launch/launch-fallback-gate]
registries: [decision-registry]
tags: [template, launch-phases, fases, runway, ops, lancamento]
---

# Launch Phases — As Fases da Runway

Este template desenha as **fases do lançamento**: a runway que leva da pré-pré-venda ao fechamento do carrinho, fase a fase, cada uma com objetivo, janela, dono e critério de prontidão. As fases vêm do [`launch-memo`](launch-memo-template.md) e dão origem ao [`run-of-show`](run-of-show-template.csv) e ao [`events-calendar`](events-calendar-template.csv). Cada fase só abre quando a anterior cumpre seu critério — sem atalho. Toda escassez de janela é **100% real** (`truthful_scarcity`): o carrinho abre e fecha nas datas que o memo prometeu.

## Como usar
- **Agente dono:** [`launch-producer`](../../agents/launch-producer.md). Pareia com o [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) (que reserva sala e gente por fase) e com o [`affiliate-program-architect`](../../agents/affiliate-program-architect.md) (que encaixa a janela dos afiliados na fase de carrinho aberto).
- **Task:** preenchido logo após o [`launch-memo`](launch-memo-template.md), na produção do lançamento (D6).
- **Quando:** o produtor quebra a runway em fases assim que o memo está aprovado. Aplica o [`runway-and-phases`](../../frameworks/launch/runway-and-phases.md) e o [`product-launch-formula`](../../frameworks/launch/product-launch-formula.md) para a sequência de fases, e o [`cart-open-close`](../../frameworks/launch/cart-open-close.md) para as datas de abertura e fechamento.
- Use data real em cada janela. Use um critério de prontidão binário por fase. Campo vazio = runway com buraco = gate vermelho.

## Campos & Instruções
- **{{NOME_DO_LANCAMENTO}}** — o nome do lançamento, herdado do [`launch-memo`](launch-memo-template.md).
- **{{FASE}}** — o nome da fase (pre-aquecimento, aquecimento, abertura, carrinho-aberto, fechamento, pos-lancamento).
- **{{OBJETIVO_DA_FASE}}** — o que a fase precisa conseguir, em uma frase.
- **{{JANELA}}** — as datas de início e fim da fase, formato `AAAA-MM-DD`.
- **{{DONO}}** — o agente responsável pela fase.
- **{{ENTREGAVEIS}}** — os ativos e marcos que saem prontos na fase.
- **{{CRITERIO_DE_PRONTIDAO}}** — a condição binária que prova que a fase pode começar (entra da fase anterior).
- **{{GATILHO_DE_TRANSICAO}}** — o evento que passa o bastão para a fase seguinte.
- **{{FALLBACK}}** — o que fazer se a fase atrasa ou falha ([`surge-ops`](../../frameworks/launch/surge-ops.md), [`launch-fallback-gate`](../../checklists/launch/launch-fallback-gate.md)).
- **{{STATUS}}** — o estado da fase: planejada, pronta, em-execucao, concluida.

## O Template
```
# FASES DO LANCAMENTO — {{NOME_DO_LANCAMENTO}}
Owner: launch-producer · Data: {{DATA}} · Status: {{STATUS}}

## RUNWAY (visão geral)
Da fase {{PRIMEIRA_FASE}} ({{DATA_INICIO}}) ao fechamento ({{DATA_FECHAMENTO}}).
Deadline real e único do carrinho: {{DEADLINE_REAL}} — motivo honesto: {{MOTIVO_ESCASSEZ}}

## FASE 1 — {{FASE_1}}
Objetivo: {{OBJETIVO_1}}
Janela: {{INICIO_1}} → {{FIM_1}} · Dono: {{DONO_1}}
Entregáveis: {{ENTREGAVEIS_1}}
Critério de prontidão (entra de): {{CRITERIO_1}}
Gatilho de transição (sai para a próxima): {{GATILHO_1}}
Fallback se atrasar: {{FALLBACK_1}}

## FASE 2 — {{FASE_2}}
Objetivo: {{OBJETIVO_2}}
Janela: {{INICIO_2}} → {{FIM_2}} · Dono: {{DONO_2}}
Entregáveis: {{ENTREGAVEIS_2}}
Critério de prontidão (entra de): {{CRITERIO_2}}
Gatilho de transição: {{GATILHO_2}}
Fallback se atrasar: {{FALLBACK_2}}

## FASE 3 — {{FASE_3}}
Objetivo: {{OBJETIVO_3}}
Janela: {{INICIO_3}} → {{FIM_3}} · Dono: {{DONO_3}}
Entregáveis: {{ENTREGAVEIS_3}}
Critério de prontidão (entra de): {{CRITERIO_3}}
Gatilho de transição: {{GATILHO_3}}
Fallback se atrasar: {{FALLBACK_3}}
```

## Exemplo preenchido
> **# FASES DO LANCAMENTO — Lançamento do Motor 72h**
> Owner: launch-producer · Data: 2026-06-02 · Status: planejada
>
> **RUNWAY** — Da fase de aquecimento (28/05) ao fechamento (07/06). Deadline único: **sábado 07/06, 23h59** — motivo honesto: 40 vagas de setup por capacidade real.
>
> **FASE 1 — Aquecimento** — Objetivo: encher a lista de espera e provar a dor. Janela: 28/05 → 02/06 · Dono: launch-producer. Entregáveis: 3 e-mails de pré-aquecimento, página de inscrição. Critério de prontidão: Offer Book aprovado e VSL pronta. Gatilho de transição: a inscrição atinge a meta de leads. Fallback: estender 1 dia e subir o orçamento de tráfego.
> **FASE 2 — Abertura (webinar)** — Objetivo: revelar a oferta e abrir o carrinho. Janela: 03/06 → 03/06 · Dono: events-logistics-coordinator. Entregáveis: run-of-show, sala configurada, checkout no ar. Critério de prontidão: todos os ativos do inventário entregues. Gatilho de transição: o carrinho abre ao vivo no pitch. Fallback: gravação de reposição no mesmo dia.
> **FASE 3 — Carrinho aberto → Fechamento** — Objetivo: vender até o pico e fechar no deadline real. Janela: 03/06 → 07/06 · Dono: launch-producer. Entregáveis: sequência de e-mails de carrinho, reforço de escassez verdadeira. Critério de prontidão: webinar concluído e checkout estável. Gatilho de transição: o relógio bate o deadline único. Fallback: e-mail de "última chamada" se a conversão cair, sem mover o prazo.

## DoD do entregável
A runway está pronta quando: (1) todas as fases estão preenchidas, sem `{{PLACEHOLDER}}` solto; (2) as fases cobrem a runway inteira em ordem, sem buraco entre janelas, do aquecimento ao pós-lançamento; (3) cada fase tem `dono` nomeado e `entregaveis` claros; (4) cada fase tem um `critério de prontidão` **binário** que prova que pode começar, satisfazendo o [`launch-phase-readiness-gate`](../../checklists/launch/launch-phase-readiness-gate.md); (5) cada fase tem `gatilho de transição` e `fallback` executável se atrasa ([`surge-ops`](../../frameworks/launch/surge-ops.md), [`launch-fallback-gate`](../../checklists/launch/launch-fallback-gate.md)); (6) a janela do carrinho tem abertura, fechamento e **deadline único e real**, com motivo honesto, e o fallback **nunca move o prazo** (`truthful_scarcity`, [política de compliance](../../docs/compliance-policy.md)); (7) o texto está em voz ativa e presente, 3ª série. Só então as fases alimentam o [`run-of-show`](run-of-show-template.csv) e o [`events-calendar`](events-calendar-template.csv), e o conjunto passa no [`launch-memo-checklist`](../../checklists/launch-memo-checklist.md). A runway final vira decisão no [`decision-registry`](../../data/registries/decision-registry.md).
