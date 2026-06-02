---
id: checklist.offer-stack-checklist
title: "Checklist — Offer Stack (garantia, bônus, escassez/urgência, naming MAGIC)"
type: checklist
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [offer-stack-builder, guarantee-design, scarcity-urgency-engine, magic-naming, risk-reversal-ladder]
registries: [offer-registry, claim-registry, proof-registry]
tags: [checklist, offer-stack, garantia, bonus, escassez, magic-naming, d2]
---

# Checklist — Offer Stack

## Propósito
Este checklist prova que a oferta empilhada é **irresistível e verdadeira** — com garantia, bônus, escassez real e nomes que vendem. Existe porque uma oferta forte não é só produto e preço: é a pilha de valor que faz o "sim" parecer óbvio. A garantia reverte o risco. Os bônus aumentam o valor percebido sem inflar custo. A escassez/urgência empurra a decisão — mas só se for real. O naming MAGIC faz cada item soar concreto e desejável. Sem este checklist verde, a oferta fica fraca ou desonesta. Ele garante `value_equation_test`: cada elemento da pilha move uma alavanca de valor, e `truthful_scarcity`: nenhum gatilho de pressa é inventado.

## Dono & Escopo
- **owner_agent:** `unit-economics-stack-analyst` (monta a pilha e responde pela viabilidade); o [`value-equation-engineer`](../agents/value-equation-engineer.md) confirma que cada item move uma alavanca e o [`compliance-auditor`](../agents/compliance-auditor.md) veta escassez falsa ou bônus impossível.
- **Artefato inspecionado:** o **offer stack** (`templates/offer/offer-stack-template` preenchido), registrado no [`offer-registry`](../data/registries/offer-registry.md), com claims dos bônus ligados ao [`claim-registry`](../data/registries/claim-registry.md).

## Condição de Passagem
A pilha traz garantia exequível, bônus que somam valor real, escassez/urgência 100% verdadeira e cada componente com nome no padrão MAGIC — e cada item move uma alavanca de valor.

## Itens
1. **Núcleo de valor claro.** Como verificar: a oferta principal nomeia o resultado-sonho e o mecanismo, conforme [`offer-stack-builder`](../frameworks/offer-stack-builder.md); o cliente entende o que recebe em uma frase.
2. **Garantia presente e exequível.** Como verificar: há reversão de risco cumprível, conforme [`guarantee-design`](../frameworks/guarantee-design.md) e [`risk-reversal-ladder`](../frameworks/risk-reversal-ladder.md); detalhada no [`guarantee-checklist`](guarantee-checklist.md).
3. **Bônus que somam valor.** Como verificar: cada bônus ataca uma objeção ou acelera o resultado; bônus de enfeite que não move alavanca sai.
4. **Cada item move uma alavanca.** Como verificar: mapear cada componente a sonho↑, probabilidade↑, tempo↓ ou esforço↓; nenhum item órfão de valor.
5. **Escassez/urgência verdadeira.** Como verificar: prazo, vagas ou estoque apontam para limite real e rastreável, conforme [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md); falsa = veto.
6. **Naming MAGIC.** Como verificar: cada item tem nome concreto, magnético e específico, conforme [`magic-naming`](../frameworks/magic-naming.md); nada de nome genérico.
7. **Valor percebido > preço.** Como verificar: a soma do valor declarado da pilha supera com folga o preço pedido, registrado no `offer-registry`.
8. **Claims dos bônus com lastro.** Como verificar: toda promessa de bônus tem `proof_id` no [`proof-registry`](../data/registries/proof-registry.md).

## Evidência Exigida
Para marcar ✅: linkar a pilha no `offer-registry`, o mapa item→alavanca sem órfãos (item 4), a verificação de que cada gatilho de escassez aponta para limite real (item 5), a lista de nomes no padrão MAGIC (item 6) e a soma valor-percebido vs preço (item 7). Os claims de bônus rastreados a prova (item 8) ficam linkados ao `proof-registry`.

## Protocolo de Falha
Item vermelho → a pilha volta ao `unit-economics-stack-analyst` com o defeito nomeado. Item que não move alavanca é cortado ou justificado pelo `value-equation-engineer`. Escassez falsa ou bônus impossível aciona veto do `compliance-auditor`. Bônus que estoura a margem reabre as unit economics. Re-entrada: corrigir a pilha, atualizar o `offer-registry`, re-submeter. Mudança no núcleo da oferta reabre este checklist e o `guarantee-checklist`.

## Links
- Frameworks: [`offer-stack-builder`](../frameworks/offer-stack-builder.md) · [`guarantee-design`](../frameworks/guarantee-design.md) · [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md) · [`magic-naming`](../frameworks/magic-naming.md) · [`risk-reversal-ladder`](../frameworks/risk-reversal-ladder.md)
- Registries: [`offer-registry`](../data/registries/offer-registry.md) · [`claim-registry`](../data/registries/claim-registry.md) · [`proof-registry`](../data/registries/proof-registry.md)
- Agentes: [`unit-economics-stack-analyst`](../agents/unit-economics-stack-analyst.md) · [`value-equation-engineer`](../agents/value-equation-engineer.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Checklists vizinhos: [`guarantee-checklist`](guarantee-checklist.md) · [`offer-quality-scorecard-checklist`](offer-quality-scorecard-checklist.md) · [`compliance-checklist`](compliance-checklist.md)
