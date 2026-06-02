---
id: checklist.offer-book-stack.offer-book-dod-gate
title: "★ Gate HARD STOP — Definition of Done do Offer Book (bloqueia D4+)"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [power-of-one, money-model-sequence, proof-to-claim-chain, offer-to-funnel-mapping, value-equation]
registries: [offer-registry, big-idea-registry, price-test-registry, claim-registry, proof-registry, decision-registry]
tags: [gate, hard-stop, offer-book, dod, d3, blocker, aggregator]
---

# ★ Gate HARD STOP — Definition of Done do Offer Book

## Propósito
Este é o **HARD STOP** do squad. Ele prova que o Offer Book está pronto como fundação estratégica completa antes de uma única palavra de copy nascer. Existe porque o princípio Agora é inegociável: ~50–60% do trabalho é pesquisa e estratégia antes da primeira frase. Sem este gate verde, persuasão vira maquiagem sobre uma oferta fraca. Ele **agrega** os três gates de D1–D3 — [`intelligence-complete-gate`](intelligence-complete-gate.md), [`offer-architecture-gate`](offer-architecture-gate.md) e [`big-idea-locked-gate`](big-idea-locked-gate.md) — e só passa quando os três estão verdes ao mesmo tempo. É a barreira que separa estratégia de execução.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (única autoridade que vira este gate de vermelho para verde); o `compliance-auditor` co-assina a verdade dos claims e da escassez antes da liberação.
- **Artefato inspecionado:** o **Offer Book consolidado** — o documento-mestre montado a partir de [`offer-registry`](../../data/registries/offer-registry.md), [`big-idea-registry`](../../data/registries/big-idea-registry.md), [`price-test-registry`](../../data/registries/price-test-registry.md), [`claim-registry`](../../data/registries/claim-registry.md), [`proof-registry`](../../data/registries/proof-registry.md) e [`decision-registry`](../../data/registries/decision-registry.md), via a task `assemble-offer-book`.

## Condição de Passagem
Os três gates D1–D3 estão verdes, a escassez é 100% verdadeira, nenhum claim está órfão, e o Offer Book consolidado existe — logo NENHUMA copy (D4+) pode nascer enquanto este gate estiver vermelho.

## Itens
1. **Inteligência fechada.** Verificar: [`intelligence-complete-gate`](intelligence-complete-gate.md) marcado ✅ com evidência linkada (mercado + avatar + prova).
2. **Arquitetura fechada.** Verificar: [`offer-architecture-gate`](offer-architecture-gate.md) marcado ✅ (mecanismo + valor + money model + preço + unit econ).
3. **Big Idea travada.** Verificar: [`big-idea-locked-gate`](big-idea-locked-gate.md) marcado ✅ com exatamente UMA tese `locked`.
4. **Espinha do money model presente.** Verificar: ≥2 partes sequenciadas (alvo 4) no `offer-registry`, conforme `money_model_spine`.
5. **Escassez 100% verdadeira.** Verificar: cada elemento de escassez/urgência aponta para um limite real (estoque, prazo, vagas) — o `compliance-auditor` confirma; escassez falsa = veto.
6. **Nenhum claim órfão.** Verificar: todo `claim_id` no `claim-registry` tem `proof_id` correspondente no `proof-registry`.
7. **Offer Book consolidado existe.** Verificar: o documento-mestre (`templates/core/offer-book-master` preenchido) está completo, sem seção em branco, e linkado.
8. **Decisões registradas.** Verificar: project type, escopo (1 frase) e cada override têm `decision_id` no `decision-registry`.

## Evidência Exigida
Para marcar ✅: linkar os três gates upstream já verdes (itens 1–3), a linha do `offer-registry` com a escada e a escassez (itens 4–5), a tabela claim→proof sem órfãos (item 6), o Offer Book consolidado completo (item 7) e os `decision_id` (item 8). A assinatura conjunta `offerbook-chief` + `compliance-auditor` é registrada no `decision-registry`.

## Protocolo de Falha
Qualquer item vermelho mantém o HARD STOP fechado: o `offerbook-chief` **recusa abrir D4** e mostra o gate vermelho. Re-entrada: o gate upstream que falhou volta ao seu agente dono (intel/arquitetura/big-idea) com o defeito nomeado; após correção e atualização do registry, re-submete-se a este gate. Override só com decisão humana explícita gravada no `decision-registry` — nunca por pressa de prazo. Mudança em qualquer insumo (money model, preço, Big Idea) reabre este gate e invalida copy já iniciada.

## Links
- Gates agregados: [`intelligence-complete-gate`](intelligence-complete-gate.md) · [`offer-architecture-gate`](offer-architecture-gate.md) · [`big-idea-locked-gate`](big-idea-locked-gate.md)
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`big-idea-registry`](../../data/registries/big-idea-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`offerbook-chief`](../../agents/offerbook-chief.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Downstream (bloqueado até verde): [`blackbook-dod-gate`](../blackbook-stack/blackbook-dod-gate.md)
