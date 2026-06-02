---
id: checklist.email-sms.email-urgency-coherence-gate
title: "Gate — Coerência de Urgência (escassez real e idêntica em toda a sequência)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
frameworks: [scarcity-urgency-engine, launch/cart-open-close, launch/abandoned-cart-recovery]
registries: [control-registry, offer-registry]
tags: [gate, email, sms, urgencia, escassez, truthful-scarcity, coerencia, d4]
---

# Gate — Coerência de Urgência

## Propósito
Este gate prova que a urgência da sequência é **100% real e idêntica em todas as mensagens** — reforçando, no canal de e-mail/SMS, o princípio `truthful_scarcity`. Uma sequência de fechamento vive de urgência: "penúltimo dia", "último dia", "últimas horas". Se esse prazo é falso — um deadline que não termina, um "fecha hoje" que se repete amanhã — é veto do [`compliance-auditor`](../../agents/compliance-auditor.md) e queima a lista para sempre. Pior ainda é a **incoerência**: o e-mail diz "fecha às 23h59" e o SMS diz "mais 2 dias", ou os e-mails contradizem o prazo do VSL. O gate exige que o prazo seja verdadeiro, que sua fonte exista no offer book, e que **todas** as mensagens — e o roteiro de VSL — comuniquem a mesma data e hora. Ele é o par, no canal de mensagens, da [`vsl-urgency-gate`](../vsl/vsl-urgency-gate.md): a urgência precisa bater ponta a ponta.

## Dono & Escopo
- **owner_agent:** `email-sms-sequence-writer` (sem poder de veto; **não escreve deadline falso** e sinaliza ao chief o que o offer book não sustenta). O [`compliance-auditor`](../../agents/compliance-auditor.md) **veta** escassez falsa.
- **Artefato inspecionado:** o campo `escassez_real` e os prazos comunicados em cada mensagem da `sequence-matrix` no [`control-registry`](../../data/registries/control-registry.md), confrontados com o limite real no [`offer-registry`](../../data/registries/offer-registry.md), as janelas do [`launch-producer`](../../agents/launch-producer.md) e a urgência do roteiro do [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md).

## Condição de Passagem
Toda urgência comunicada na sequência corresponde a um limite real, com a mesma data e hora em todas as mensagens e coerente com o prazo do VSL.

## Itens
1. **Urgência ancorada em limite real.** Verificar: cada prazo na sequência corresponde a uma janela/estoque verdadeiro no `offer-registry` e nas datas do `launch-producer`.
2. **Mesma data/hora em toda a sequência.** Verificar: todas as mensagens que citam o prazo usam a **mesma** data e hora — nenhuma diverge.
3. **Coerência e-mail × SMS.** Verificar: o SMS de últimas horas e o e-mail de fechamento comunicam o mesmo deadline.
4. **Coerência com o VSL.** Verificar: o prazo dos e-mails bate com o da [`vsl-urgency-gate`](../vsl/vsl-urgency-gate.md) (mesma janela de carrinho).
5. **Sem deadline falso.** Verificar: nenhum "fecha hoje" que reabre, nenhum cronômetro que reinicia, nenhuma "última chance" recorrente.
6. **Fonte da escassez nomeada.** Verificar: as mensagens dizem **por que** é escasso (carrinho fecha, vagas, estoque do bônus), não urgência genérica.
7. **`escassez_real` marcada.** Verificar: a sequência registra a urgência como real, com a fonte e a data, no `control-registry`.

## Evidência Exigida
Para marcar ✅: linkar a `sequence-matrix` no `control-registry` mostrando o mesmo prazo em todas as mensagens e a fonte nomeada (itens 2–3, 6–7), o limite correspondente no `offer-registry`/janelas do launch (item 1), a conferência cruzada com a urgência do VSL (item 4) e a ausência de gatilhos falsos (item 5).

## Protocolo de Falha
Item vermelho → o `email-sms-sequence-writer` **remove ou realinha** o prazo ao limite verdadeiro e unifica a data/hora em todas as mensagens; deadline falso ou incoerente é reprovação. Escassez que o offer book não sustenta → sinaliza ao [`offerbook-chief`](../../agents/offerbook-chief.md) e ao [`compliance-auditor`](../../agents/compliance-auditor.md). Divergência com o VSL → alinha com o [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md). Re-entrada: corrige `escassez_real` e os prazos no `control-registry` e re-submete. Mudança de janela de carrinho reabre este gate, o [`email-timing-gate`](email-timing-gate.md) e a [`vsl-urgency-gate`](../vsl/vsl-urgency-gate.md).

## Links
- Gates irmãos: [`email-step-coverage-gate`](email-step-coverage-gate.md) · [`email-segmentation-gate`](email-segmentation-gate.md) · [`email-timing-gate`](email-timing-gate.md) · [`email-subject-gate`](email-subject-gate.md)
- Frameworks: [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`cart-open-close`](../../frameworks/launch/cart-open-close.md) · [`abandoned-cart-recovery`](../../frameworks/launch/abandoned-cart-recovery.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md) · [`launch-producer`](../../agents/launch-producer.md) · [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md)
- Relacionado: [`vsl-urgency-gate`](../vsl/vsl-urgency-gate.md) · [`compliance-scarcity-truth-gate`](../compliance/compliance-scarcity-truth-gate.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
