---
id: checklist.email-sms.email-step-coverage-gate
title: "Gate — Cobertura de Etapas (nenhum degrau do ciclo de vida falta)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
frameworks: [copy/email-sequence-architecture, launch/cart-open-close, launch/abandoned-cart-recovery]
registries: [control-registry]
tags: [gate, email, sms, cobertura, ciclo-de-vida, sequencias, d4]
---

# Gate — Cobertura de Etapas

## Propósito
Este gate prova que a **espinha de cobertura** está completa: nenhum estágio do ciclo de vida fica sem mensagem. Uma sequência com buraco — um carrinho que abre sem e-mail de abertura, um abandono sem recuperação, um pós-evento sem ascensão — deixa dinheiro na mesa em silêncio. O gate enumera os fluxos do ciclo: registro/opt-in e indoctrination, pré-lançamento (runway), cart-open, cart-close, abandoned-cart e pós-evento/pós-compra. Para cada um, exige que exista a mensagem que aquele momento pede. Ele também garante a **ascensão do money model** no pós-compra — o próximo degrau da escada — e que os não-compradores recebam nurture sem queima. É o gate que transforma uma lista de e-mails avulsos numa orquestração de conversa por mensagens ao longo do tempo, espelhando a sequência que o [`money-model-designer`](../../agents/money-model-designer.md) desenhou.

## Dono & Escopo
- **owner_agent:** `email-sms-sequence-writer` (sem poder de veto; toda saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md)).
- **Artefato inspecionado:** a `sequence-matrix` e os fluxos registrados no [`control-registry`](../../data/registries/control-registry.md), montados a partir de [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md), [`cart-open-close`](../../frameworks/launch/cart-open-close.md) e [`abandoned-cart-recovery`](../../frameworks/launch/abandoned-cart-recovery.md).

## Condição de Passagem
Todos os estágios do ciclo de vida aplicáveis ao lançamento têm ao menos a mensagem que aquele momento exige, sem nenhum buraco de cobertura.

## Itens
1. **Registro/Opt-in & indoctrination.** Verificar: há confirmação e a mensagem que planta a Big Idea; se há evento, há os lembretes de show-up.
2. **Pré-lançamento (runway).** Verificar: existe a sequência de valor que abre crenças antes do carrinho (quando o tipo de lançamento pede).
3. **Cart-open.** Verificar: há o e-mail de abertura mais reforço de valor e prova nos primeiros dias.
4. **Cart-close.** Verificar: existe a sequência de fechamento (penúltimo dia, último dia, últimas horas).
5. **Abandoned-cart.** Verificar: há o fluxo de recuperação de quem iniciou e não concluiu (lembrete, FAQ/fricção, incentivo final).
6. **Pós-evento/pós-compra com ascensão.** Verificar: há entrega, a **ascensão do money model** (próximo degrau) e nurture dos não-compradores.
7. **Sem buraco de cobertura.** Verificar: percorrer a matriz — todo estágio aplicável tem mensagem; lacuna reprova.

## Evidência Exigida
Para marcar ✅: linkar a `sequence-matrix` no `control-registry` com a lista de fluxos e as mensagens de cada estágio (itens 1–6) e a varredura que confirma ausência de buraco (item 7). A ascensão do money model no pós-compra deve aparecer explícita, ligada ao degrau seguinte da espinha.

## Protocolo de Falha
Item vermelho → o `email-sms-sequence-writer` **adiciona o degrau** que falta (não deixa gap); estágio sem mensagem é reprovação. Se falta o destino (VSL) para um fluxo, escreve os fluxos independentes e marca os bloqueados. Re-entrada: completa a matriz no `control-registry` e re-submete ao [`voice-style-guardian`](../../agents/voice-style-guardian.md). Mudança na espinha do money model (degrau novo) reabre este gate.

## Links
- Gates irmãos: [`email-segmentation-gate`](email-segmentation-gate.md) · [`email-timing-gate`](email-timing-gate.md) · [`email-subject-gate`](email-subject-gate.md) · [`email-urgency-coherence-gate`](email-urgency-coherence-gate.md)
- Frameworks: [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md) · [`cart-open-close`](../../frameworks/launch/cart-open-close.md) · [`abandoned-cart-recovery`](../../frameworks/launch/abandoned-cart-recovery.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Relacionado: [`money-model-propagation-gate`](../money-model/money-model-propagation-gate.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
