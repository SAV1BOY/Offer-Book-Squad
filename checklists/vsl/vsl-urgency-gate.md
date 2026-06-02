---
id: checklist.vsl.vsl-urgency-gate
title: "Gate — Urgência Verdadeira (escassez 100% real, reforça truthful_scarcity)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [scarcity-urgency-engine, copy/vsl-structure, launch/perfect-webinar]
registries: [control-registry, offer-registry]
tags: [gate, vsl, urgencia, escassez, truthful-scarcity, compliance, d4]
---

# Gate — Urgência Verdadeira

## Propósito
Este gate prova que a escassez e a urgência do roteiro são **100% reais** — e reforça o princípio não-negociável `truthful_scarcity`. Urgência move a ação: sem um motivo para agir agora, o leitor adia e nunca volta. Mas a escassez falsa — um cronômetro que reinicia, "últimas vagas" que nunca acabam, um prazo inventado — é veto direto do [`compliance-auditor`](../../agents/compliance-auditor.md) e destrói a confiança que a marca leva anos para construir. O gate força a urgência no Bloco 3, ancorada num limite **verdadeiro**: vagas de fato limitadas, prazo de carrinho real, bônus de ação rápida com estoque genuíno. Ele exige que o roteiro **nomeie a fonte** da escassez e que essa fonte exista no offer book e nas janelas do [`launch-producer`](../../agents/launch-producer.md). É o gate onde o roteirista, que não tem veto, antecipa e remove o que o compliance vetaria — escrevendo só o deadline que é verdade.

## Dono & Escopo
- **owner_agent:** `vsl-webinar-scriptwriter` (sem poder de veto; **não escreve escassez falsa** e sinaliza ao chief o que o offer book não sustenta como real). O [`compliance-auditor`](../../agents/compliance-auditor.md) **veta** escassez falsa.
- **Artefato inspecionado:** a escassez/urgência do Bloco 3 do roteiro no [`control-registry`](../../data/registries/control-registry.md), confrontada com o limite real registrado no [`offer-registry`](../../data/registries/offer-registry.md) e com as janelas/datas do `launch-producer` (via [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md)).

## Condição de Passagem
Toda escassez ou urgência do roteiro corresponde a um limite real e verificável (vagas, prazo ou estoque), com a fonte nomeada e sem nenhum gatilho falso.

## Itens
1. **Urgência presente, mas honesta.** Verificar: o Bloco 3 dá um motivo real para agir agora — sem ele a conversão cai, mas o motivo não pode ser inventado.
2. **Fonte da escassez nomeada.** Verificar: o roteiro diz **por que** é escasso (turma com vagas, carrinho fecha em data X, estoque do bônus) — não "vagas limitadas" genérico.
3. **Limite existe no offer book.** Verificar: a vaga/prazo/estoque citado consta no `offer-registry` e nas janelas do [`launch-producer`](../../agents/launch-producer.md).
4. **Sem cronômetro falso.** Verificar: nenhum timer que reinicia, "última chance" recorrente ou prazo que não termina de verdade.
5. **Bônus de ação rápida real.** Verificar: se há fast-action bonus, o prazo e o estoque dele são verdadeiros.
6. **Coerente com os e-mails.** Verificar: o prazo no roteiro bate com o que a sequência de [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) comunica (mesma data/hora).
7. **`escassez_real` marcada.** Verificar: o roteiro registra a urgência como real, com a fonte, no `control-registry`.

## Evidência Exigida
Para marcar ✅: linkar a escassez do Bloco 3 no `control-registry` com a fonte nomeada (itens 1–2, 7), o limite correspondente no `offer-registry`/janelas do launch (item 3), a ausência de gatilhos falsos (itens 4–5) e a conferência de coerência de prazo com a sequência de e-mail (item 6).

## Protocolo de Falha
Item vermelho → o `vsl-webinar-scriptwriter` **remove ou realinha** a urgência ao limite verdadeiro; nunca escreve deadline inexistente. Escassez que o offer book não sustenta → sinaliza ao [`offerbook-chief`](../../agents/offerbook-chief.md) e ao [`compliance-auditor`](../../agents/compliance-auditor.md) (que **veta** escassez falsa). Prazo divergente dos e-mails → alinha com o [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md). Re-entrada: corrige a escassez no `control-registry` e re-submete. Mudança de janela de carrinho reabre este gate e o gate de coerência de urgência dos e-mails.

## Links
- Gates irmãos: [`vsl-formula-fit-gate`](vsl-formula-fit-gate.md) · [`vsl-value-before-price-gate`](vsl-value-before-price-gate.md) · [`vsl-risk-reversal-gate`](vsl-risk-reversal-gate.md) · [`vsl-cta-strength-gate`](vsl-cta-strength-gate.md)
- Frameworks: [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`vsl-structure`](../../frameworks/copy/vsl-structure.md) · [`perfect-webinar`](../../frameworks/launch/perfect-webinar.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) · [`compliance-auditor`](../../agents/compliance-auditor.md) · [`launch-producer`](../../agents/launch-producer.md) · [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md)
- Relacionado: [`email-urgency-coherence-gate`](../email-sms/email-urgency-coherence-gate.md) · [`compliance-scarcity-truth-gate`](../compliance/compliance-scarcity-truth-gate.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
