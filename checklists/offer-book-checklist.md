---
id: checklist.offer-book-checklist
title: "Checklist — Definition of Done do Offer Book (HARD STOP, agrega D1–D3)"
type: checklist
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [power-of-one, money-model-sequence, value-equation, proof-to-claim-chain, offer-to-funnel-mapping]
registries: [offer-registry, big-idea-registry, price-test-registry, claim-registry, proof-registry, decision-registry]
tags: [checklist, hard-stop, offer-book, dod, d1, d2, d3, aggregator, blocker]
---

# Checklist — Definition of Done do Offer Book

## Propósito
Este checklist é o **HARD STOP** do squad. Ele prova que o Offer Book está completo como fundação estratégica antes de uma única palavra de copy nascer. Existe porque o princípio é inegociável: ~50–60% do trabalho é pesquisa e estratégia antes da primeira frase (`offer_before_persuasion`). Sem ele verde, persuasão vira maquiagem sobre oferta fraca. Ele **agrega** os entregáveis de D1 (mercado, avatar, prova), D2 (mecanismo, valor, money model, preço, unit economics) e D3 (Big Idea, posicionamento), e só fecha quando cada peça passou no seu checklist específico. É a barreira que separa estratégia de execução.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (única autoridade que vira este checklist de vermelho para verde); o `compliance-auditor` co-assina a verdade dos claims e da escassez.
- **Artefato inspecionado:** o **Offer Book consolidado** (`templates/core/offer-book-master` preenchido), montado a partir do [`offer-registry`](../data/registries/offer-registry.md), [`big-idea-registry`](../data/registries/big-idea-registry.md), [`price-test-registry`](../data/registries/price-test-registry.md), [`claim-registry`](../data/registries/claim-registry.md), [`proof-registry`](../data/registries/proof-registry.md) e [`decision-registry`](../data/registries/decision-registry.md), via a task `assemble-offer-book`.

## Condição de Passagem
Os checklists de D1–D3 estão verdes, a escassez é 100% verdadeira, nenhum claim está órfão e o Offer Book consolidado existe — logo NENHUMA copy (D4+) nasce enquanto este checklist estiver vermelho.

## Itens
1. **Mercado diagnosticado.** Como verificar: sofisticação (1–5) e consciência declaradas no `offer-registry`, com fonte linkada.
2. **Avatar pela voz dele.** Como verificar: o [`avatar-voc-checklist`](avatar-voc-checklist.md) está ✅ (≥10 verbatims, emoção dominante, objeções).
3. **Prova mapeada.** Como verificar: o [`proof-checklist`](proof-checklist.md) está ✅ — cada claim e objeção com prova ou plano de coleta.
4. **Mecanismo nomeado e provado.** Como verificar: o [`mechanism-checklist`](mechanism-checklist.md) está ✅ (nome próprio + prova em 1 frase).
5. **Equação de valor passada.** Como verificar: o [`value-equation-checklist`](value-equation-checklist.md) está ✅ — cada alavanca com ação concreta, zero alavanca órfã.
6. **Preço deriva de valor.** Como verificar: o [`pricing-wtp-checklist`](pricing-wtp-checklist.md) está ✅ com método declarado.
7. **Unit economics conhecidas.** Como verificar: o [`unit-economics-checklist`](unit-economics-checklist.md) está ✅ (LTV:CAC, payback, break-even).
8. **Money Model em 4 partes.** Como verificar: o [`money-model-checklist`](money-model-checklist.md) está ✅ — ≥2 partes sequenciadas (alvo 4) no `offer-registry`.
9. **UMA Big Idea travada.** Como verificar: o [`big-idea-checklist`](big-idea-checklist.md) está ✅ com exatamente uma tese `locked`.
10. **Posicionamento fechado.** Como verificar: o [`positioning-checklist`](positioning-checklist.md) está ✅ (lead × consciência, casado à copy).
11. **Escassez 100% verdadeira.** Como verificar: cada elemento de escassez aponta para limite real (estoque, prazo, vagas); o `compliance-auditor` confirma — escassez falsa = veto.
12. **Nenhum claim órfão.** Como verificar: todo `claim_id` no `claim-registry` tem `proof_id` correspondente no `proof-registry`.
13. **Offer Book consolidado existe.** Como verificar: o documento-mestre está completo, sem seção em branco, e linkado.

## Evidência Exigida
Para marcar ✅: linkar cada checklist upstream já verde (itens 1–10), a linha do `offer-registry` com a escada e a escassez (item 11), a tabela claim→proof sem órfãos (item 12) e o Offer Book consolidado completo (item 13). A assinatura conjunta `offerbook-chief` + `compliance-auditor` é gravada no `decision-registry`.

## Protocolo de Falha
Qualquer item vermelho mantém o HARD STOP fechado: o `offerbook-chief` **recusa abrir D4** e mostra o item vermelho. Re-entrada: o checklist upstream que falhou volta ao seu agente dono com o defeito nomeado; após correção e atualização do registry, re-submete-se. Override só com decisão humana explícita gravada no `decision-registry` — nunca por pressa de prazo. Mudança em qualquer insumo (money model, preço, Big Idea) reabre este checklist e invalida copy já iniciada.

## Links
- Gate-espelho: [`offer-book-stack/offer-book-dod-gate`](offer-book-stack/offer-book-dod-gate.md)
- Checklists agregados: [`avatar-voc-checklist`](avatar-voc-checklist.md) · [`proof-checklist`](proof-checklist.md) · [`mechanism-checklist`](mechanism-checklist.md) · [`value-equation-checklist`](value-equation-checklist.md) · [`pricing-wtp-checklist`](pricing-wtp-checklist.md) · [`unit-economics-checklist`](unit-economics-checklist.md) · [`money-model-checklist`](money-model-checklist.md) · [`big-idea-checklist`](big-idea-checklist.md) · [`positioning-checklist`](positioning-checklist.md)
- Frameworks: [`power-of-one`](../frameworks/power-of-one.md) · [`money-model-sequence`](../frameworks/money-model-sequence.md) · [`value-equation`](../frameworks/value-equation.md) · [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md) · [`offer-to-funnel-mapping`](../frameworks/offer-to-funnel-mapping.md)
- Registries: [`offer-registry`](../data/registries/offer-registry.md) · [`big-idea-registry`](../data/registries/big-idea-registry.md) · [`claim-registry`](../data/registries/claim-registry.md) · [`proof-registry`](../data/registries/proof-registry.md) · [`decision-registry`](../data/registries/decision-registry.md)
- Agentes: [`offerbook-chief`](../agents/offerbook-chief.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Downstream (bloqueado até verde): [`launch-blackbook-checklist`](launch-blackbook-checklist.md)
