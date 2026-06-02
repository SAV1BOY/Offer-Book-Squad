---
id: checklist.cart-close-checklist
title: "Checklist — Fechamento de Carrinho (sequência de fechamento coerente e verdadeira)"
type: checklist
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
frameworks: [launch/cart-open-close, copy/close-frameworks, scarcity-urgency-engine]
registries: [control-registry, claim-registry, proof-registry]
tags: [checklist, cart-close, fechamento, sequencia, escassez, d4]
---

# Checklist — Fechamento de Carrinho

## Propósito
Este checklist prova que a sequência de fechamento é **coerente e verdadeira** — ela cresce a tensão até o prazo real sem mentir. Existe porque o fechamento é onde a maior parte da receita acontece e também onde mais se mente: prazos que não fecham, "últimas vagas" que reabrem, contagem regressiva falsa. A sequência precisa de uma lógica clara — abertura, aprofundamento, prova, resposta às objeções, urgência final — com cada mensagem puxando para o "sim". E o prazo precisa ser real, porque escassez falsa é veto. Sem este checklist verde, o fechamento queima confiança no momento decisivo. Ele garante `truthful_scarcity` e `decision_before_ornament`: cada mensagem move a venda e cada gatilho de urgência é honesto.

## Dono & Escopo
- **owner_agent:** `email-sms-sequence-writer` (escreve a sequência de fechamento); o [`voice-style-guardian`](../agents/voice-style-guardian.md) co-assina a voz, o [`funnel-architect`](../agents/funnel-architect.md) garante o caminho até o checkout e o [`compliance-auditor`](../agents/compliance-auditor.md) veta escassez falsa.
- **Artefato inspecionado:** a **sequência de fechamento de carrinho** (parte do `templates/copy/email-sms-sequences-template` e `templates/copy/sequence-matrix-template`), registrada no [`control-registry`](../data/registries/control-registry.md).

## Condição de Passagem
A sequência tem lógica de fechamento clara, cada mensagem puxa para o "sim", a urgência aponta para um prazo real, e nenhum claim de fechamento está sem prova.

## Itens
1. **Lógica de fechamento.** Como verificar: a sequência segue uma progressão (abertura, valor, prova, objeção, urgência final), conforme [`launch/cart-open-close`](../frameworks/launch/cart-open-close.md); nenhuma mensagem é redundante.
2. **Cobertura de objeções.** Como verificar: as objeções principais do avatar têm ao menos uma mensagem que as responde antes do fechamento.
3. **Prazo real.** Como verificar: a data/hora de fechamento é verdadeira e única; nada de "última chance" que reabre, conforme [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md); falsa = veto.
4. **Urgência crescente honesta.** Como verificar: a tensão sobe rumo ao prazo (24h, última chamada) e cada aviso reflete o tempo real restante.
5. **CTA único por mensagem.** Como verificar: cada e-mail/SMS tem UMA ação clara que leva ao checkout, conforme [`copy/close-frameworks`](../frameworks/copy/close-frameworks.md).
6. **Claim com lastro.** Como verificar: todo número/promessa de fechamento tem `proof_id` no [`proof-registry`](../data/registries/proof-registry.md).
7. **Voz aprovada.** Como verificar: o `voice-style-guardian` deu `voice-verdict` APROVADO (3ª série, ativa, presente).
8. **Caminho até o checkout.** Como verificar: cada CTA leva à página certa e viva; o `funnel-architect` confirma que o carrinho fecha de fato no prazo anunciado.

## Evidência Exigida
Para marcar ✅: linkar a sequência no `control-registry`, o mapa da progressão de fechamento (item 1), a tabela objeção→mensagem (item 2), a prova de que o prazo é real e único (item 3) e a tabela claim→proof sem órfãos (item 6). O `voice-verdict` APROVADO (item 7) e a confirmação de checkout vivo no prazo (item 8) ficam linkados.

## Protocolo de Falha
Item vermelho → a sequência volta ao `email-sms-sequence-writer` com o defeito nomeado e **não é agendada**. Prazo falso ou "última chance" que reabre aciona veto do `compliance-auditor`. Mensagem redundante ou sem CTA é reescrita. Caminho de checkout quebrado reabre conversa com o `funnel-architect`. Re-entrada: corrigir a sequência, atualizar o `control-registry`, re-submeter. Mudança no prazo de fechamento reabre toda a contagem de urgência.

## Links
- Frameworks: [`launch/cart-open-close`](../frameworks/launch/cart-open-close.md) · [`copy/close-frameworks`](../frameworks/copy/close-frameworks.md) · [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md)
- Registries: [`control-registry`](../data/registries/control-registry.md) · [`claim-registry`](../data/registries/claim-registry.md) · [`proof-registry`](../data/registries/proof-registry.md)
- Agentes: [`email-sms-sequence-writer`](../agents/email-sms-sequence-writer.md) · [`voice-style-guardian`](../agents/voice-style-guardian.md) · [`funnel-architect`](../agents/funnel-architect.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Checklists vizinhos: [`funnel-map-checklist`](funnel-map-checklist.md) · [`run-of-show-checklist`](run-of-show-checklist.md) · [`compliance-checklist`](compliance-checklist.md)
