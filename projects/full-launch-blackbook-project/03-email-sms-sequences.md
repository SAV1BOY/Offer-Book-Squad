---
id: project.full-launch-blackbook-project.03-email-sms-sequences
title: "Fase 03 — Sequências de E-mail & SMS"
type: project-phase
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
  - artifact.offer-stack
  - data.registry.proof
  - data.registry.objection
produces:
  - artifact.email-sms-sequences
  - artifact.sequence-matrix
  - decision.voice-verdict
tags: [project-phase, copy, email, sms, sequencias, cart-open-close, segmentacao, hard-stop, d4]
---

# Fase 03 — Sequências de E-mail & SMS

## Objetivo da Fase
Transformar o Offer Book aprovado em TODOS os fluxos de e-mail e SMS do ciclo de vida — do opt-in ao pós-evento — cada mensagem com lista-alvo, timing, subject line e regra de segmentação, sem buraco de cobertura. O estado-pronto é a matriz de sequências completa, cada claim com prova linkada, escassez verdadeira, supressão definida (comprador sai da venda), aprovada nos três gates de e-mail e no veredito de voz. Esta fase orquestra a conversa por mensagens ao longo do tempo e empurra o público para o VSL da Fase 02.

## Critério de Entrada
A Fase 01 entrega o `artifact.offer-book` aprovado (HARD STOP VERDE). A Fase 02 entrega o `artifact.vsl-script` — o destino para onde os e-mails de pré-lançamento e cart-open empurram. Junto vêm a Big Idea, o positioning, o `decision.lead-type-locked`, o `artifact.offer-stack` e os registries [`proof-registry`](../../data/registries/proof-registry.md) e [`objection-registry`](../../data/registries/objection-registry.md). As janelas de carrinho e datas de evento vêm do launch-producer (ou ficam marcadas como pendentes). Pré-condição: o `offer-book-dod-gate` está APROVADO; gate vermelho faz o agente recusar. Se o VSL ainda não existe, escreve só os fluxos cujo destino independe dele (nurture de topo) e marca os demais bloqueados. O [`control-registry`](../../data/registries/control-registry.md) é escrito.

## Agentes & Tasks
- **Task [`write-email-sms-sequences`](../../tasks/copy/write-email-sms-sequences.md)** — dono [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md). Sem poder de veto; submete ao guardião.
- **Task [`voice-pass`](../../tasks/copy/voice-pass.md)** — dono [`voice-style-guardian`](../../agents/voice-style-guardian.md). Passe obrigatório de voz.

## Passos
1. Verifique o HARD STOP: confirme o `offer-book-dod-gate` verde.
2. Mapeie a espinha de cobertura: registro/indoctrination, pré-lançamento, cart-open, cart-close, abandono, pós-evento. Cada estágio precisa de ≥1 mensagem.
3. Defina o destino de cada fluxo; os de pré-lançamento e cart-open empurram para o VSL/oferta.
4. Aplique [`copy/email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md), [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md) e [`launch/abandoned-cart-recovery`](../../frameworks/launch/abandoned-cart-recovery.md). Por mensagem: lista/segmento, timing, subject + pré-header, corpo, CTA.
5. Mapeie uma objeção por e-mail no fechamento; ancore prova junto de cada claim. Gere subjects com Tree-of-Thoughts (≥3 por e-mail-chave).
6. Defina segmentação e supressão: quem comprou sai dos fluxos de venda. Calibre a cadência com Tree-of-Thoughts (suave, padrão, agressiva).
7. Valide a escassez: toda urgência tem de ser real; respeite opt-out e LGPD. Use SMS para o lembrete de últimas horas.
8. Self-verify com red-team (buraco de cobertura, colisão de timing, comprador ainda em venda); registre a matriz no `control-registry` e encaminhe ao voice-pass.

## Artefatos Produzidos
- `artifact.email-sms-sequences` + `artifact.sequence-matrix` — linha do tempo × segmento, cada mensagem com canal, lista, gatilho, timing, subject, objeção-alvo, CTA, supressão, escassez real.
- `decision.voice-verdict` — APROVADO por peça.
- Registry escrito: [`control-registry`](../../data/registries/control-registry.md).

## Gates
- [`email-sms/email-step-coverage-gate`](../../checklists/email-sms/email-step-coverage-gate.md) · [`email-sms/email-segmentation-gate`](../../checklists/email-sms/email-segmentation-gate.md) · [`email-sms/email-timing-gate`](../../checklists/email-sms/email-timing-gate.md)
- Os quatro gates de voz via [`voice/voice-checklist`](../../checklists/voice/voice-checklist.md).
- Gate de entrada (HARD STOP): [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).

## Critério de Saída
Todos os estágios do ciclo de vida têm mensagem (zero buraco); cada mensagem tem lista, timing, subject e CTA; a supressão está definida; cada claim tem prova linkada; a escassez é verdadeira; sem colisão de timing; os três gates de e-mail estão verdes e o veredito de voz é APROVADO. A próxima fase é a [`04-mailers-inserts`](04-mailers-inserts.md), que materializa a estratégia em peças físicas por degrau da escada.
