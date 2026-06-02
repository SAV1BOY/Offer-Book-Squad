---
id: checklist.email-sms.email-timing-gate
title: "Gate — Timing (cada mensagem na hora certa, sem colisão)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
frameworks: [copy/email-sequence-architecture, launch/cart-open-close, launch/abandoned-cart-recovery]
registries: [control-registry]
tags: [gate, email, sms, timing, offset, cadencia, d4]
---

# Gate — Timing

## Propósito
Este gate prova que **cada mensagem dispara na hora certa, sem colisão**. Timing é tão decisivo quanto conteúdo: um lembrete de show-up que chega depois do evento é inútil, dois disparos no mesmo minuto irritam e podem cair em spam, e uma cadência de fechamento mal-espaçada ou queima a lista ou perde a urgência. O gate exige que cada mensagem tenha um **offset explícito** relativo ao seu gatilho (T+0, T+1h, dia 3, T−3h), que não haja **colisão** (dois disparos conflitantes no mesmo instante para o mesmo segmento) nem **salto** (uma mensagem que depende de outra que não veio). Ele checa a cadência da janela de fechamento — suave, padrão ou agressiva — escolhida pelo Tree-of-Thoughts do agente, equilibrando pressão de conversão contra risco de descadastro. O [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) e o [`launch-producer`](../../agents/launch-producer.md) dependem desse timing coerente.

## Dono & Escopo
- **owner_agent:** `email-sms-sequence-writer` (sem poder de veto; saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md)).
- **Artefato inspecionado:** o campo `timing_offset` e o `gatilho` de cada mensagem na `sequence-matrix` do [`control-registry`](../../data/registries/control-registry.md), com as janelas de carrinho/datas do [`launch-producer`](../../agents/launch-producer.md) (ou marcadas `[DATA PENDENTE]`).

## Condição de Passagem
Cada mensagem tem um offset explícito relativo ao seu gatilho, sem colisão entre disparos nem dependência de uma mensagem que não chegou, dentro de uma cadência coerente.

## Itens
1. **Offset explícito por mensagem.** Verificar: cada linha tem `timing_offset` (T+0, T+1h, dia 3, T−3h) — nenhuma mensagem sem timing.
2. **Gatilho declarado.** Verificar: cada offset é relativo a um gatilho claro (opt-in, abertura de carrinho, abandono, data de evento).
3. **Sem colisão.** Verificar: dois disparos não caem no mesmo instante de forma conflitante para o mesmo segmento.
4. **Sem salto de dependência.** Verificar: nenhuma mensagem pressupõe outra anterior que não foi enviada àquele segmento.
5. **Cadência coerente com a janela.** Verificar: a cadência de fechamento (suave/padrão/agressiva) casa com a tolerância da lista, sem queimar nem afrouxar a urgência.
6. **Lembretes no tempo útil.** Verificar: lembretes de show-up e de últimas horas chegam **antes** do evento/prazo, não depois.
7. **Datas pendentes sinalizadas.** Verificar: onde faltam datas, há `[DATA PENDENTE]` e sinal ao `launch-producer` — não um offset inventado.

## Evidência Exigida
Para marcar ✅: linkar a `sequence-matrix` no `control-registry` com `timing_offset` e `gatilho` por mensagem (itens 1–2, 7), a varredura que confirma ausência de colisão e de salto (itens 3–4) e a cadência da janela de fechamento com os lembretes no tempo útil (itens 5–6).

## Protocolo de Falha
Item vermelho → o `email-sms-sequence-writer` **reescalona** os offsets em colisão e fecha os saltos de dependência; cadência agressiva demais é rebaixada para evitar queima. Faltando datas, escreve com placeholders e sinaliza ao [`launch-producer`](../../agents/launch-producer.md). Re-entrada: corrige `timing_offset` no `control-registry` e re-submete ao [`voice-style-guardian`](../../agents/voice-style-guardian.md). Mudança de janela de carrinho reabre este gate e o [`email-urgency-coherence-gate`](email-urgency-coherence-gate.md).

## Links
- Gates irmãos: [`email-step-coverage-gate`](email-step-coverage-gate.md) · [`email-segmentation-gate`](email-segmentation-gate.md) · [`email-subject-gate`](email-subject-gate.md) · [`email-urgency-coherence-gate`](email-urgency-coherence-gate.md)
- Frameworks: [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md) · [`cart-open-close`](../../frameworks/launch/cart-open-close.md) · [`abandoned-cart-recovery`](../../frameworks/launch/abandoned-cart-recovery.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) · [`launch-producer`](../../agents/launch-producer.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
