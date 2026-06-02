---
id: checklist.email-sequence-checklist
title: "Checklist — Sequência de Email (cobre degraus; lista/timing/subject/segmentação)"
type: checklist
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
frameworks: [copy/email-sequence-architecture, launch/cart-open-close, launch/abandoned-cart-recovery]
registries: [control-registry, proof-registry, objection-registry]
tags: [checklist, copy, email, sequence, timing, segmentacao, d4]
---

# Checklist — Sequência de Email

## Propósito
Este checklist prova que a sequência de email **cobre cada degrau do lançamento** (registro, pré-lançamento, carrinho aberto, fechamento, abandono, pós-evento), com lista, timing, subject e segmentação definidos por email. Existe porque uma sequência com buraco — um degrau sem email, um envio fora de hora, um subject fraco — derruba a taxa de abertura e a conversão. Cada email precisa saber para quem vai, quando dispara, o que promete no assunto e qual ação pede. Sem este checklist verde, a sequência vira disparo genérico que o cliente ignora. Ela só nasce com o HARD STOP liberado e executa a Big Idea travada ao longo do tempo. É o motor de conversão que trabalha enquanto o time dorme.

## Dono & Escopo
- **owner_agent:** `email-sms-sequence-writer` (escreve os fluxos); o [`voice-style-guardian`](../agents/voice-style-guardian.md) co-assina a voz.
- **Artefato inspecionado:** o `artifact.email-sms-sequences` e a `artifact.sequence-matrix`, registrados no [`control-registry`](../data/registries/control-registry.md), sustentados pelo [`proof-registry`](../data/registries/proof-registry.md) e pelo [`objection-registry`](../data/registries/objection-registry.md).

## Condição de Passagem
Cada degrau do lançamento tem seus emails, e cada email declara lista/segmento, timing, subject e UMA ação — com claims sustentados e voz aprovada.

## Itens
1. **HARD STOP liberado.** Como verificar: o [`offer-book-checklist`](offer-book-checklist.md) está ✅ — sem ele, a sequência não nasce.
2. **Cobertura por degrau.** Como verificar: a sequence-matrix mostra emails para cada fase (registro, pré-lançamento, abertura, fechamento, abandono, pós-evento) — zero degrau vazio, conforme `email-sequence-architecture`.
3. **Lista/segmento por email.** Como verificar: cada email declara o segmento de destino (lead frio, engajado, não-comprou, comprou) e a regra de entrada/saída.
4. **Timing por email.** Como verificar: cada email tem horário/gatilho relativo definido (dia/hora ou "X horas após ação"), conforme `cart-open-close`.
5. **Subject por email.** Como verificar: cada email tem assunto escrito (e idealmente uma variante de teste), claro e na voz do avatar.
6. **UMA ação por email.** Como verificar: cada email pede uma única ação com link/CTA explícito; não três pedidos.
7. **Carrinho aberto/fechado coberto.** Como verificar: a fase de cart-open-close tem a cadência de fechamento com urgência verdadeira, conforme `cart-open-close`.
8. **Abandono de carrinho coberto.** Como verificar: existe fluxo de recuperação de abandono com gatilho e timing, conforme `abandoned-cart-recovery`.
9. **Claims com lastro.** Como verificar: todo número/promessa nos emails tem `proof_id` no `proof-registry`.
10. **Objeções endereçadas.** Como verificar: as objeções dominantes do `objection-registry` aparecem tratadas ao longo da sequência.
11. **Escassez verdadeira.** Como verificar: prazos citados são reais e rastreáveis; escassez falsa = veto do `compliance-auditor`.
12. **Voz aprovada.** Como verificar: o `voice-style-guardian` deu `voice-verdict` APROVADO.

## Evidência Exigida
Para marcar ✅: linkar a sequence-matrix no `control-registry` mostrando cobertura por degrau (item 2), a tabela email→segmento→timing→subject→CTA (itens 3–6), os fluxos de cart-close e abandono (itens 7–8), a tabela claim→proof (item 9) e o `voice-verdict` APROVADO (item 12). Escassez citada exige o limite real linkado (item 11).

## Protocolo de Falha
Item vermelho → a sequência volta ao `email-sms-sequence-writer` com o defeito nomeado e **não entra no automador**. Degrau sem email, email sem timing/segmento, claim órfão ou escassez falsa reabre o fluxo; voz reprovada volta ao `voice-style-guardian`; claim/escassez acionam o `compliance-auditor`. Re-entrada: completar o fluxo, atualizar o `control-registry`, re-submeter. Mudança na oferta ou na escada do money model reabre este checklist.

## Links
- Frameworks: [`email-sequence-architecture`](../frameworks/copy/email-sequence-architecture.md) · [`cart-open-close`](../frameworks/launch/cart-open-close.md) · [`abandoned-cart-recovery`](../frameworks/launch/abandoned-cart-recovery.md)
- Registries: [`control-registry`](../data/registries/control-registry.md) · [`proof-registry`](../data/registries/proof-registry.md) · [`objection-registry`](../data/registries/objection-registry.md)
- Agentes: [`email-sms-sequence-writer`](../agents/email-sms-sequence-writer.md) · [`voice-style-guardian`](../agents/voice-style-guardian.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Gates por agente: [`email-sms/email-step-coverage-gate`](email-sms/email-step-coverage-gate.md) · [`email-sms/email-segmentation-gate`](email-sms/email-segmentation-gate.md) · [`email-sms/email-timing-gate`](email-sms/email-timing-gate.md)
- Checklists vizinhos: [`sms-checklist`](sms-checklist.md) · Agrega para: [`launch-blackbook-checklist`](launch-blackbook-checklist.md)
