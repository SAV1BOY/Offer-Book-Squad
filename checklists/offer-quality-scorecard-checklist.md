---
id: checklist.offer-quality-scorecard-checklist
title: "Checklist — Scorecard de Qualidade da Oferta (0–100 por dimensão)"
type: checklist
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [value-equation, money-model-sequence, proof-to-claim-chain, big-idea-generator, scarcity-urgency-engine]
registries: [offer-registry, big-idea-registry, claim-registry, proof-registry, decision-registry]
tags: [checklist, scorecard, qualidade, oferta, value-equation, money-model, big-idea, d3]
---

# Checklist — Scorecard de Qualidade da Oferta

## Propósito
Este checklist transforma "a oferta está boa?" em **um número de 0 a 100**. Existe porque opinião sobre força de oferta é fraca: precisamos de uma nota auditável que diga onde a oferta ganha e onde sangra. O scorecard pesa cinco dimensões — equação de valor, money model, prova, Big Idea e escassez verdadeira — porque são as alavancas que decidem se a persuasão tem base (`offer_before_persuasion`). A nota não substitui os checklists específicos; ela os resume num placar de decisão. Sem este scorecard, abrir copy vira aposta. Com ele, o `offerbook-chief` vê em uma tela se a fundação merece virar lançamento ou volta para a oficina.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (dono da definição de pronto; calcula e assina a nota); o [`value-equation-engineer`](../agents/value-equation-engineer.md) e o [`compliance-auditor`](../agents/compliance-auditor.md) co-assinam as dimensões de valor e de escassez/prova.
- **Artefato inspecionado:** o **Offer Book consolidado** (`templates/core/offer-book-master`), lido a partir do [`offer-registry`](../data/registries/offer-registry.md), [`big-idea-registry`](../data/registries/big-idea-registry.md), [`claim-registry`](../data/registries/claim-registry.md) e [`proof-registry`](../data/registries/proof-registry.md); a nota é gravada no [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
A oferta soma **≥ 80/100** no scorecard, com **nenhuma dimensão abaixo de 60%** do seu peso e **escassez verdadeira sem penalidade** — abaixo disso, a oferta não vira copy.

## Scorecard 0–100 (pesos por dimensão)
| # | Dimensão | Peso | O que mede | Fonte da nota |
|---|---|---|---|---|
| 1 | Equação de valor | **30** | Sonho↑, probabilidade↑, tempo↓, esforço↓ — zero alavanca órfã | [`value-equation`](../frameworks/value-equation.md) · [`value-equation-checklist`](value-equation-checklist.md) |
| 2 | Money model | **25** | 4 partes sequenciadas, preço/gatilho/CTA por degrau, sem beco | [`money-model-sequence`](../frameworks/money-model-sequence.md) · [`money-model-checklist`](money-model-checklist.md) |
| 3 | Prova | **20** | Cada claim com lastro; cobertura de objeções | [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md) · [`proof-checklist`](proof-checklist.md) |
| 4 | Big Idea | **15** | UMA tese nova, grande e crível, casada à consciência | [`big-idea-generator`](../frameworks/big-idea-generator.md) · [`big-idea-checklist`](big-idea-checklist.md) |
| 5 | Escassez verdadeira | **10** | Todo gatilho de escassez/urgência aponta para limite real | [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md) · [`compliance-checklist`](compliance-checklist.md) |
| | **Total** | **100** | | |

> **Regra de gating:** a dimensão 5 (escassez) é **porteira** — se houver escassez falsa, o `compliance-auditor` zera a dimensão e **veta** o lançamento, independentemente do total.

## Itens
1. **Equação de valor pontuada (0–30).** Como verificar: pontuar cada alavanca; alavanca órfã ou sem ação concreta derruba a nota; base no `value-equation-checklist`.
2. **Money model pontuado (0–25).** Como verificar: 4 partes = nota cheia; menos partes ou beco lógico reduz; base no `money-model-checklist`.
3. **Prova pontuada (0–20).** Como verificar: % de claims com `proof_id` e % de objeções cobertas no `proof-registry`/`claim-registry`.
4. **Big Idea pontuada (0–15).** Como verificar: UMA tese `locked` nos cinco critérios = nota cheia; múltiplas ideias ou tese morna reduz; base no `big-idea-checklist`.
5. **Escassez pontuada (0–10) com porteira.** Como verificar: todo gatilho aponta para limite real = nota cheia; qualquer escassez falsa zera e veta.
6. **Nenhuma dimensão < 60% do peso.** Como verificar: checar cada dimensão isolada; uma dimensão fraca reprova mesmo com total alto.
7. **Total ≥ 80.** Como verificar: somar as cinco notas; abaixo de 80 a oferta volta para a oficina.
8. **Nota rastreável e assinada.** Como verificar: a planilha de pontuação com fonte por dimensão está no `decision-registry`, assinada pelo `offerbook-chief`.

## Evidência Exigida
Para marcar ✅: linkar a planilha de pontuação por dimensão com a fonte de cada nota (itens 1–5), o cálculo do total (item 7), a verificação de piso de 60% por dimensão (item 6) e a confirmação da porteira de escassez pelo `compliance-auditor` (item 5). A nota final assinada é gravada no `decision-registry` (item 8) e referenciada pelo [`offer-book-checklist`](offer-book-checklist.md).

## Protocolo de Falha
Total < 80, dimensão < 60% do peso, ou escassez falsa → a oferta **não vira copy** e volta ao agente dono da dimensão fraca (valor → `value-equation-engineer`; money model → `money-model-designer`; prova → `proof-credibility-curator`; Big Idea → `big-idea-architect`; escassez → `compliance-auditor`). Escassez falsa é veto absoluto. Re-entrada: corrigir a dimensão, recalcular a nota, atualizar o `decision-registry`, re-submeter ao `offerbook-chief`. Mudança em qualquer insumo recalcula o scorecard inteiro.

## Links
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate-espelho: [`offer-book-stack/offer-book-dod-gate`](offer-book-stack/offer-book-dod-gate.md)
- Dimensões: [`value-equation-checklist`](value-equation-checklist.md) · [`money-model-checklist`](money-model-checklist.md) · [`proof-checklist`](proof-checklist.md) · [`big-idea-checklist`](big-idea-checklist.md) · [`compliance-checklist`](compliance-checklist.md)
- Frameworks: [`value-equation`](../frameworks/value-equation.md) · [`money-model-sequence`](../frameworks/money-model-sequence.md) · [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md) · [`big-idea-generator`](../frameworks/big-idea-generator.md) · [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md)
- Registries: [`offer-registry`](../data/registries/offer-registry.md) · [`big-idea-registry`](../data/registries/big-idea-registry.md) · [`claim-registry`](../data/registries/claim-registry.md) · [`proof-registry`](../data/registries/proof-registry.md) · [`decision-registry`](../data/registries/decision-registry.md)
- Agentes: [`offerbook-chief`](../agents/offerbook-chief.md) · [`value-equation-engineer`](../agents/value-equation-engineer.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Checklists vizinhos: [`offer-stack-checklist`](offer-stack-checklist.md) · [`guarantee-checklist`](guarantee-checklist.md)
