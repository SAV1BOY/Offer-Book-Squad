---
id: checklist.sms-checklist
title: "Checklist — SMS (opt-out, timing, link — compliance de SMS)"
type: checklist
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
frameworks: [copy/email-sequence-architecture, launch/cart-open-close, launch/abandoned-cart-recovery]
registries: [control-registry, proof-registry]
tags: [checklist, copy, sms, opt-out, compliance, timing, d4]
---

# Checklist — SMS

## Propósito
Este checklist prova que cada SMS é **curto, oportuno e em conformidade**: tem opt-out claro, dispara em horário permitido, leva a um link rastreável e usa só claims com lastro. Existe porque SMS é o canal mais íntimo e o mais regulado — uma mensagem fora de hora, sem opção de sair ou com link quebrado queima a lista e expõe a marca a multa. O SMS reforça a sequência de email nos momentos de pico (carrinho fechando, evento começando), não a substitui. Sem este checklist verde, o SMS vira spam que destrói reputação de remetente. Ele encarna `truthful_scarcity` e a disciplina de compliance: cada disparo respeita o consentimento e a janela legal. É o canal de maior atenção e, por isso, o de maior risco.

## Dono & Escopo
- **owner_agent:** `email-sms-sequence-writer` (escreve os SMS); o [`voice-style-guardian`](../agents/voice-style-guardian.md) co-assina a voz, o [`tech-links-deliverability-engineer`](../agents/tech-links-deliverability-engineer.md) confirma o link e o `compliance-auditor` valida opt-out e janela legal.
- **Artefato inspecionado:** os SMS dentro do `artifact.email-sms-sequences` e da `artifact.sequence-matrix`, registrados no [`control-registry`](../data/registries/control-registry.md).

## Condição de Passagem
Cada SMS tem opt-out claro, dispara em horário permitido para o destinatário, leva a UM link rastreável e usa só claims com prova — com consentimento confirmado.

## Itens
1. **HARD STOP liberado.** Como verificar: o [`offer-book-checklist`](offer-book-checklist.md) está ✅ — sem ele, a sequência não nasce.
2. **Opt-out presente.** Como verificar: cada SMS (ou o fluxo) traz instrução clara de saída (ex.: responder SAIR/STOP); sem opt-out não envia.
3. **Consentimento confirmado.** Como verificar: a lista de destino só contém números com opt-in registrado; o `compliance-auditor` valida a base.
4. **Timing em janela permitida.** Como verificar: cada disparo cai em horário comercial razoável do fuso do destinatário — nada de madrugada, conforme `cart-open-close`.
5. **UM link rastreável.** Como verificar: cada SMS com link usa URL curta com parâmetro de rastreio que resolve na página certa; o `tech-links-deliverability-engineer` confirma o link vivo.
6. **Mensagem curta e única ação.** Como verificar: o SMS cabe no limite de caracteres e pede UMA ação clara.
7. **Identificação do remetente.** Como verificar: a marca/remetente está identificável na mensagem, sem fingir ser pessoa privada.
8. **Claims com lastro.** Como verificar: todo número/promessa no SMS tem `proof_id` no `proof-registry`; claim sem prova sai.
9. **Escassez verdadeira.** Como verificar: prazo/limite citado é real e rastreável; escassez falsa = veto do `compliance-auditor`.
10. **Pico coberto.** Como verificar: os momentos de maior conversão (fechamento de carrinho, início de evento, abandono) têm SMS com gatilho, conforme `abandoned-cart-recovery`.
11. **Voz aprovada.** Como verificar: o `voice-style-guardian` deu `voice-verdict` APROVADO.

## Evidência Exigida
Para marcar ✅: linkar os SMS no `control-registry`, a confirmação de opt-out e consentimento validados pelo `compliance-auditor` (itens 2–3), a janela de envio por fuso (item 4), o teste do link curto com parâmetro de rastreio resolvendo na página certa (item 5), a tabela claim→proof (item 8) e o `voice-verdict` APROVADO (item 11). Escassez citada exige o limite real linkado (item 9).

## Protocolo de Falha
Item vermelho → o SMS volta ao `email-sms-sequence-writer` com o defeito nomeado e **não entra no disparador**. Ausência de opt-out, consentimento não comprovado, horário proibido, claim órfão ou escassez falsa aciona **veto do `compliance-auditor`** (compliance de SMS é absoluto). Link quebrado volta ao `tech-links-deliverability-engineer`. Re-entrada: corrigir o SMS e a base, atualizar o `control-registry`, re-submeter. Mudança na oferta reabre este checklist.

## Links
- Frameworks: [`email-sequence-architecture`](../frameworks/copy/email-sequence-architecture.md) · [`cart-open-close`](../frameworks/launch/cart-open-close.md) · [`abandoned-cart-recovery`](../frameworks/launch/abandoned-cart-recovery.md)
- Registries: [`control-registry`](../data/registries/control-registry.md) · [`proof-registry`](../data/registries/proof-registry.md)
- Agentes: [`email-sms-sequence-writer`](../agents/email-sms-sequence-writer.md) · [`voice-style-guardian`](../agents/voice-style-guardian.md) · [`tech-links-deliverability-engineer`](../agents/tech-links-deliverability-engineer.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Checklists vizinhos: [`email-sequence-checklist`](email-sequence-checklist.md) · [`compliance-checklist`](compliance-checklist.md)
- Agrega para: [`launch-blackbook-checklist`](launch-blackbook-checklist.md)
