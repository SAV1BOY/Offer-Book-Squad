---
id: template.ops.launch-memo
title: "Launch Memo — O Memorando que Alinha o Lançamento Inteiro"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
consumes: [template.core.offer-book-master, template.offer.products-and-offers, template.ops.launch-phases]
produces: [data.registry.decision]
frameworks: [launch/runway-and-phases, launch/cart-open-close, launch/surge-ops, money-model-sequence]
checklists: [launch-memo-checklist, launch/launch-objective-gate, launch/launch-roles-gate]
registries: [decision-registry, offer-registry]
tags: [template, launch-memo, memorando, ops, lancamento, alinhamento]
---

# Launch Memo — O Memorando que Alinha o Lançamento

Este template produz o **launch memo**: uma página única que diz a todo o squad o que vamos lançar, para quem, quando, com qual meta e quem responde por cada parte. O memo é o contrato de alinhamento do lançamento. Ele nasce do Offer Book aprovado e da escada de ofertas travada — não inventa oferta, apenas a coloca em movimento (`offer_before_persuasion`). Toda escassez ou deadline citado aqui é **100% real** (`truthful_scarcity`): o que o memo promete, a operação cumpre.

## Como usar
- **Agente dono:** [`launch-producer`](../../agents/launch-producer.md). Pareia com o [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) (que transforma o memo em calendário e logística) e com o [`offerbook-chief`](../../agents/offerbook-chief.md) (que aprova a meta e o objetivo).
- **Task:** preenchido no início da produção do lançamento (D6), depois do Offer Book aprovado e da escada definida na planilha [`products-and-offers`](../offer/products-and-offers-template.csv).
- **Quando:** o produtor escreve o memo antes de qualquer ativo nascer. Ele define a meta, a janela e os papéis. Depois deriva as [`launch-phases`](launch-phases-template.md), o [`run-of-show`](run-of-show-template.csv) e o [`events-calendar`](events-calendar-template.csv) a partir dele.
- Use número e prova nos campos de meta e oferta. Use a Big Idea única em toda a comunicação. Campo vazio = lançamento sem alinhamento = gate vermelho.

## Campos & Instruções
- **{{NOME_DO_LANCAMENTO}}** — o nome de trabalho do lançamento, ligado à oferta núcleo.
- **{{OFERTA_NUCLEO}}** — o `offer_id` da oferta principal, da planilha [`products-and-offers`](../offer/products-and-offers-template.csv).
- **{{BIG_IDEA}}** — a tese única do lançamento ([`power-of-one`](../../frameworks/power-of-one.md)). Uma só, nunca duas.
- **{{PUBLICO}}** — a quem o lançamento se dirige, na voz do avatar.
- **{{META}}** — o resultado mensurável do lançamento (faturamento, vendas, leads), com número.
- **{{JANELA}}** — as datas de abertura e fechamento do carrinho, alinhadas ao [`cart-open-close`](../../frameworks/launch/cart-open-close.md).
- **{{DEADLINE_REAL}}** — o prazo único e verdadeiro, e o **motivo honesto** do limite.
- **{{FASES}}** — o resumo das fases ([`launch-phases`](launch-phases-template.md); detalhe lá).
- **{{PAPEIS}}** — quem responde por cada frente (produção, logística, copy, tech, afiliados, compliance).
- **{{RISCOS_E_CONTINGENCIA}}** — os riscos do dia e a ação de contingência de cada um ([`surge-ops`](../../frameworks/launch/surge-ops.md)).
- **{{STATUS}}** — o estado do lançamento: rascunho, aprovado, em-execucao, encerrado.

## O Template
```
# LAUNCH MEMO — {{NOME_DO_LANCAMENTO}}
Owner: launch-producer · Data: {{DATA}} · Status: {{STATUS}}

## 1. O QUE VAMOS LANCAR
Oferta núcleo: {{OFERTA_NUCLEO}}
Big Idea única: {{BIG_IDEA}}
Público: {{PUBLICO}}

## 2. META
Resultado-alvo (com número): {{META}}
Prova de que a oferta converte na lista própria: {{PROVA_CONVERSAO}}

## 3. JANELA & DEADLINE
Abertura do carrinho: {{DATA_ABERTURA}} · Fechamento: {{DATA_FECHAMENTO}}
Deadline real e único: {{DEADLINE_REAL}}
Motivo honesto do limite: {{MOTIVO_ESCASSEZ}}

## 4. FASES (resumo; detalhe em launch-phases)
{{FASES}}

## 5. PAPEIS (quem responde por quê)
| Frente | Dono | Entregável |
|--------|------|-----------|
| Produção | {{DONO_PRODUCAO}} | {{ENTREGAVEL_PRODUCAO}} |
| Logística | {{DONO_LOGISTICA}} | {{ENTREGAVEL_LOGISTICA}} |
| Copy | {{DONO_COPY}} | {{ENTREGAVEL_COPY}} |
| Tech | {{DONO_TECH}} | {{ENTREGAVEL_TECH}} |
| Afiliados | {{DONO_AFILIADOS}} | {{ENTREGAVEL_AFILIADOS}} |
| Compliance | {{DONO_COMPLIANCE}} | {{ENTREGAVEL_COMPLIANCE}} |

## 6. RISCOS & CONTINGENCIA (surge)
| Risco | Sinal | Ação de contingência |
|-------|-------|----------------------|
| {{RISCO_1}} | {{SINAL_1}} | {{ACAO_1}} |
| {{RISCO_2}} | {{SINAL_2}} | {{ACAO_2}} |
```

## Exemplo preenchido
> **# LAUNCH MEMO — Lançamento do Motor 72h**
> Owner: launch-producer · Data: 2026-06-02 · Status: aprovado
>
> **1. O QUE VAMOS LANCAR** — Oferta núcleo: CORE-01 (Motor de Recuperação 72h, R$497). Big Idea: *"A janela de 72 horas que devolve o lucro que seu checkout esconde."* Público: donos de e-commerce que faturam R$50 mil/mês.
> **2. META** — Resultado-alvo: **R$180 mil em 5 dias** (≈360 vendas do núcleo). Prova: a lista própria converte a **6,2%** no teste.
> **3. JANELA & DEADLINE** — Abertura: terça 03/06 · Fechamento: sábado 07/06. Deadline único: **sábado 23h59**. Motivo honesto: a turma tem **40 vagas** de setup feito-para-você por capacidade real.
> **4. FASES** — Aquecimento (28/05–02/06), Abertura (03/06), Carrinho aberto (03–07/06), Fechamento (07/06). Detalhe em launch-phases.
> **5. PAPEIS** — Produção: launch-producer (run-of-show); Logística: events-logistics-coordinator (sala + calendário); Copy: vsl-webinar-scriptwriter (VSL + e-mails); Tech: tech-links-deliverability-engineer (checkout + links); Afiliados: affiliate-program-architect (Dream 100); Compliance: compliance-auditor (veredito de claims).
> **6. RISCOS & CONTINGENCIA** — Risco: presença ao vivo baixa → sinal: <40% dos inscritos → ação: disparar SMS de "estamos ao vivo". Risco: conversão do pitch cai → sinal: <3% no fim do pitch → ação: reforçar a prova e o deadline real no chat.

## DoD do entregável
O memo está pronto quando: (1) os 6 blocos estão preenchidos, sem `{{PLACEHOLDER}}` solto; (2) a oferta núcleo resolve para um `offer_id` real no [`offer-registry`](../../data/registries/offer-registry.md) e a Big Idea é **única** (`power-of-one`); (3) a meta tem número e a prova de conversão na lista própria está declarada (`offer_before_persuasion`); (4) a janela tem abertura, fechamento e um **deadline único e real**, com motivo honesto, satisfazendo o [`launch-objective-gate`](../../checklists/launch/launch-objective-gate.md) e a [política de compliance](../../docs/compliance-policy.md) (`truthful_scarcity`); (5) toda frente tem dono nomeado, sem buraco de responsabilidade, satisfazendo o [`launch-roles-gate`](../../checklists/launch/launch-roles-gate.md); (6) cada risco tem sinal e ação de contingência executável ([`surge-ops`](../../frameworks/launch/surge-ops.md)); (7) o texto está em voz ativa e presente, 3ª série. Só então o produtor deriva as [`launch-phases`](launch-phases-template.md), o [`run-of-show`](run-of-show-template.csv) e o [`events-calendar`](events-calendar-template.csv), e o memo passa no [`launch-memo-checklist`](../../checklists/launch-memo-checklist.md). A versão aprovada vira decisão no [`decision-registry`](../../data/registries/decision-registry.md).
