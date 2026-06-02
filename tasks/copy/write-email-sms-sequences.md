---
id: task.copy.write-email-sms-sequences
title: "Task — Escrever Sequências de E-mail & SMS"
type: task
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
consumes:
  - artifact.offer-book
  - artifact.big-idea
  - artifact.positioning
  - decision.lead-type-locked
  - artifact.vsl-script
  - artifact.value-equation
  - artifact.offer-stack
  - data.registry.proof
  - data.registry.objection
produces:
  - artifact.email-sms-sequences
  - artifact.sequence-matrix
frameworks: [copy/email-sequence-architecture, launch/cart-open-close, launch/abandoned-cart-recovery]
checklists:
  - offer-book-stack/offer-book-dod-gate
  - email-sms/email-step-coverage-gate
  - email-sms/email-segmentation-gate
  - email-sms/email-timing-gate
registries: [control-registry]
tags: [copy, email, sms, sequencias, cart-open-close, abandono, segmentacao, timing, hard-stop]
---

# Task — Escrever sequências de e-mail & SMS

## Objetivo
Transformar o Offer Book aprovado em TODOS os fluxos de e-mail e SMS do ciclo de vida — do opt-in ao pós-evento — cada mensagem com lista-alvo, timing, subject line e regra de segmentação, sem buraco de cobertura. O estado-pronto: a matriz de sequências completa, cada claim com prova linkada, escassez verdadeira, supressão definida, aprovada nos três gates de e-mail e encaminhada ao [`voice-pass`](../qa-memory/voice-pass.md).

## Agente dono
[`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md). Orquestra a conversa por mensagens ao longo do tempo. Sem poder de veto; submete tudo ao voice-guardian.

## Gatilho / Quando
**HARD STOP: esta task de copy (D4) só ativa APÓS o [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) estar APROVADO.** Conforme `config.yaml: defaults.hard_stop_before_copy: true` e o [`ARCHITECTURE.md`](../../ARCHITECTURE.md), nenhuma palavra de copy nasce antes de o Offer Book passar no Definition of Done. Gate vermelho → o agente **recusa** e devolve ao [`offerbook-chief`](../../agents/offerbook-chief.md). Demais gatilhos: pedido de qualquer fluxo (registro, pré-lançamento, carrinho, cart-close, abandono, pós-evento), com a camada D3 fechada (Big Idea + posição + **lead travados**) e, idealmente, o VSL já roteirizado (os e-mails apontam para ele).

## Inputs (Consome)
- `artifact.offer-book` — o pacote estratégico aprovado (fonte de verdade).
- `artifact.big-idea` + `artifact.positioning` + `decision.lead-type-locked` — tese, posição e o **lead travado** (cada e-mail-chave herda o lead por segmento de consciência).
- `artifact.vsl-script` — o destino para onde os e-mails empurram; reaproveita ganchos e provas.
- `artifact.value-equation` + `artifact.offer-stack` — alavancas e componentes a relembrar na janela de venda.
- [`data.registry.proof`](../../data/registries/proof-registry.md) — prova por claim. **Nenhum e-mail carrega claim sem lastro.**
- [`data.registry.objection`](../../data/registries/objection-registry.md) — objeções por nível, para mapear **uma objeção por e-mail** no fechamento.
- **Janelas de carrinho e datas de evento** do [`launch-producer`](../../agents/launch-producer.md) (ou marca `[DATA PENDENTE]`).

## Procedimento
1. **Verificar o HARD STOP.** Confirmar o `offer-book-dod-gate` verde. Vermelho → recusar e devolver ao chief.
2. **Carregar inputs e mapear a espinha de cobertura.** Listar os fluxos do ciclo de vida: registro/indoctrination · pré-lançamento (runway) · cart-open · cart-close · abandono · pós-evento/pós-compra. Cada estágio precisa de pelo menos uma mensagem.
3. **Definir o destino de cada fluxo.** Os e-mails de pré-lançamento e cart-open empurram para o VSL/oferta. Se o VSL não existe, escrever só os fluxos cujo destino independe dele (ex.: nurture de topo) e marcar os demais como bloqueados.
4. **Aplicar a arquitetura de sequência.** Usar [`copy/email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md) para o esqueleto geral; [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md) para a janela de venda; [`launch/abandoned-cart-recovery`](../../frameworks/launch/abandoned-cart-recovery.md) para a recuperação. Para cada mensagem definir **lista/segmento, timing (offset), subject (+ pré-header), corpo e CTA**.
5. **Mapear uma objeção por e-mail no fechamento.** Ordenar as objeções do `objection-registry` pela que destrava a compra; o cart-close ataca uma por mensagem. Cada claim ancora prova do `proof-registry` junto. Claim sem prova → `[PROVA PENDENTE]` e escalar ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md).
6. **Gerar subjects (ToT).** Para cada e-mail-chave, produzir ≥3 subjects (curiosidade, benefício, urgência) + pré-header; pontuar por abertura provável, congruência com o corpo (sem clickbait) e fit com a consciência. Podar o que promete o que o corpo não entrega.
7. **Definir segmentação e supressão.** Gerar ≥3 cortes de lista (engajamento, estágio no funil, consciência, ação) e escolher o que aumenta relevância sem fragmentar demais. **Quem comprou sai dos fluxos de venda** — escrever a regra de supressão por ação.
8. **Calibrar a cadência (ToT).** Gerar ≥3 cadências para o fechamento (suave, padrão, agressiva); pontuar por conversão vs risco de queima de lista/descadastro. Usar SMS para o lembrete de últimas horas; e-mail para o conteúdo. Respeitar opt-out e LGPD.
9. **Validar a escassez.** Toda urgência usada **tem de ser real**. Prazo que o offer-book não sustenta → sinalizar ao chief; não escrever deadline falso.
10. **Self-verify (Bloom + red-team).** Checar buraco de cobertura, colisão de timing, segmento recebendo mensagem incoerente, comprador ainda em fluxo de venda. Antecipar o veto do compliance (escassez falsa, falta de opt-out) e do voice-guardian.
11. **Registrar e encaminhar.** Logar cada mensagem no `control-registry` e a `sequence-matrix` (linha do tempo × segmento). Entregar ao voice-pass. Máximo de 2 passes de reescrita antes de escalar ao chief.

## Frameworks
[`copy/email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md) · [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md) · [`launch/abandoned-cart-recovery`](../../frameworks/launch/abandoned-cart-recovery.md).

## Outputs (Produz)
- `artifact.email-sms-sequences` + `artifact.sequence-matrix` (templates em [`copy/email-sms-sequences-template`](../../templates/copy/email-sms-sequences-template.md) e [`copy/sequence-matrix-template`](../../templates/copy/sequence-matrix-template.md)).
- [`control-registry`](../../data/registries/control-registry.md) atualizado com cada mensagem (`sequence_id`, fluxo, `msg_id`, canal, lista/segmento, gatilho, `timing_offset`, subject + variantes, objeção-alvo, CTA, supressão, `escassez_real: true`, `status: draft`).

## Definition of Done
- HARD STOP verde (offer-book-dod-gate aprovado) **antes** de qualquer linha.
- Todos os estágios do ciclo de vida têm mensagem (zero buraco de cobertura).
- Cada mensagem tem lista, timing, subject e CTA preenchidos; supressão definida (comprador sai da venda).
- Cada claim tem prova linkada (zero `[PROVA PENDENTE]` no estado final); escassez verdadeira.
- Sem colisão de timing; subjects batem com o corpo (sem clickbait).
- Os três gates de e-mail verdes; matriz registrada no `control-registry` e encaminhada ao voice-pass.

## Gates
[`email-sms/email-step-coverage-gate`](../../checklists/email-sms/email-step-coverage-gate.md) · [`email-sms/email-segmentation-gate`](../../checklists/email-sms/email-segmentation-gate.md) · [`email-sms/email-timing-gate`](../../checklists/email-sms/email-timing-gate.md). Gate de entrada (HARD STOP): [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).

## Handoff
**Próxima task:** [`voice-pass`](../qa-memory/voice-pass.md) (passe obrigatório do voice-style-guardian). **Contrato de saída:** cada mensagem tem lista, timing, subject e CTA, com supressão definida, escassez real e cobertura sem buraco — pronta para o guardião e, após o veredito APROVADO, para o [`funnel-architect`](../funnel-tech/map-funnel.md) (destinos → páginas), o [`tech-links-deliverability-engineer`](../funnel-tech/plan-tech-deliverability.md) (volume/cadência → deliverability) e o [`launch-producer`](../ops/build-run-of-show.md) (timeline → run-of-show).
