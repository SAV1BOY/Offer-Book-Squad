---
id: checklist.guarantee-checklist
title: "Checklist — Garantia (reversão de risco real e exequível)"
type: checklist
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [guarantee-design, risk-reversal-ladder, scarcity-urgency-engine]
registries: [offer-registry, claim-registry, decision-registry]
tags: [checklist, garantia, reversao-de-risco, exequivel, d2]
---

# Checklist — Garantia

## Propósito
Este checklist prova que a garantia **reverte o risco de verdade e é cumprível**. Existe porque a garantia é a alavanca que mais derruba a barreira da compra — mas só funciona se for real. Uma garantia vaga não tranquiliza ninguém. Uma garantia que a operação não consegue honrar vira processo e dano de marca. A reversão de risco precisa ser clara: o que o cliente recebe de volta, quando e como. E precisa ser exequível: o financeiro e a operação conseguem pagar. Sem este checklist verde, a garantia é só palavra bonita. Ele garante `value_equation_test` na alavanca de risco percebido e protege a marca de promessa que não se sustenta.

## Dono & Escopo
- **owner_agent:** `unit-economics-stack-analyst` (modela o impacto da garantia na margem); o [`value-equation-engineer`](../agents/value-equation-engineer.md) confirma a força da reversão de risco e o [`compliance-auditor`](../agents/compliance-auditor.md) valida exequibilidade e termos.
- **Artefato inspecionado:** a **garantia** (`templates/offer/guarantee-template` preenchido), registrada no [`offer-registry`](../data/registries/offer-registry.md), com os termos ligados ao [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
A garantia reverte um risco real do cliente, é descrita em termos claros (o quê, quando, como) e é exequível pela operação e pelo financeiro — sem letra miúda que a anule.

## Itens
1. **Risco-alvo nomeado.** Como verificar: a garantia ataca o medo real que trava a compra (perder dinheiro, perder tempo, não funcionar), levantado na pesquisa de avatar.
2. **Tipo de reversão escolhido.** Como verificar: o nível na escada de risco (condicional, incondicional, "melhor que grátis") está definido, conforme [`risk-reversal-ladder`](../frameworks/risk-reversal-ladder.md).
3. **Termos claros.** Como verificar: o documento diz o que o cliente recebe de volta, em quanto tempo e por qual processo, conforme [`guarantee-design`](../frameworks/guarantee-design.md).
4. **Exequível no financeiro.** Como verificar: o custo esperado de acionamento cabe na margem do `offer-registry`; cenário de pico de reembolso modelado.
5. **Exequível na operação.** Como verificar: existe processo para honrar a garantia (reembolso, reentrega, suporte) com dono e prazo.
6. **Sem letra miúda que anule.** Como verificar: não há cláusula escondida que torne a garantia impossível de acionar; o `compliance-auditor` confirma.
7. **Coerente com escassez.** Como verificar: a garantia não contradiz prazos/limites da oferta, conforme [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md).
8. **Registrada e rastreável.** Como verificar: os termos estão no `decision-registry` e o claim da garantia está no [`claim-registry`](../data/registries/claim-registry.md).

## Evidência Exigida
Para marcar ✅: linkar a garantia no `offer-registry`, o vínculo ao risco-alvo do avatar (item 1), o nível na escada de risco (item 2), os termos claros de prazo/processo (item 3) e o modelo de custo de acionamento cabendo na margem (item 4). O processo operacional com dono (item 5) e a confirmação de exequibilidade do `compliance-auditor` (item 6) ficam linkados ao `decision-registry`.

## Protocolo de Falha
Item vermelho → a garantia volta ao `unit-economics-stack-analyst` com o defeito nomeado. Garantia que não cabe na margem é redesenhada (prazo, condição, escopo). Garantia não exequível ou com letra miúda enganosa aciona veto do `compliance-auditor`. Reversão fraca reabre conversa com o `value-equation-engineer`. Re-entrada: corrigir os termos, atualizar o `offer-registry` e o `decision-registry`, re-submeter. Mudança na garantia reabre o `offer-stack-checklist`.

## Links
- Frameworks: [`guarantee-design`](../frameworks/guarantee-design.md) · [`risk-reversal-ladder`](../frameworks/risk-reversal-ladder.md) · [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md)
- Registries: [`offer-registry`](../data/registries/offer-registry.md) · [`claim-registry`](../data/registries/claim-registry.md) · [`decision-registry`](../data/registries/decision-registry.md)
- Agentes: [`unit-economics-stack-analyst`](../agents/unit-economics-stack-analyst.md) · [`value-equation-engineer`](../agents/value-equation-engineer.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Checklists vizinhos: [`offer-stack-checklist`](offer-stack-checklist.md) · [`offer-quality-scorecard-checklist`](offer-quality-scorecard-checklist.md) · [`compliance-checklist`](compliance-checklist.md)
