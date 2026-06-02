---
id: checklist.value.value-no-orphan-lever-gate
title: "Gate — Nenhuma Alavanca Abandonada e Nenhum Componente Órfão (VETO do value-equation-engineer)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [value-equation, value-equation-engineer/dream-outcome-amplification, value-equation-engineer/time-delay-compression, value-equation-engineer/effort-sacrifice-reduction]
registries: [offer-registry, decision-registry]
tags: [gate, value, veto, alavanca-orfa, d2, hard-stop, value-equation-test]
---

# Gate — Nenhuma Alavanca Abandonada e Nenhum Componente Órfão

## Propósito
Este é o **gate de veto** do `value-equation-engineer` — o HARD STOP de componente do squad. Ele prova duas coisas ao mesmo tempo: que **cada componente** da oferta move ≥1 das quatro alavancas da Equação de Valor, e que **nenhuma das quatro alavancas** ficou abandonada (sem nenhum componente servindo-a). Existe porque feature órfã infla custo e ruído sem aumentar valor, e alavanca abandonada deixa valor na mesa. É a materialização do princípio `value_equation_test` do `config.yaml`: toda peça move pelo menos uma alavanca, ou não entra. Diferente dos quatro gates por alavanca (que calibram cada uma isoladamente), este audita o **scorecard inteiro** e arma o veto: um componente órfão não entra no stack até ser reposicionado ou cortado.

## Dono & Escopo
- **owner_agent:** `value-equation-engineer` (um dos três guardiões com poder de veto, ao lado de `money-model-designer` e `compliance-auditor`).
- **Artefato inspecionado:** o **`value-equation-scorecard` completo** no [`offer-registry`](../../data/registries/offer-registry.md) — todos os componentes, suas alavancas, direções, deltas e vereditos; e os vetos/overrides no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
Cada componente da oferta mapeia ≥1 alavanca com direção declarada, nenhuma das quatro alavancas está abandonada, e o produto da equação é defensável sem inflar o Sonho artificialmente.

## Itens
1. **Cada componente mapeia ≥1 alavanca.** Verificar: no scorecard, todo componente (núcleo, bônus, garantia, entregável) tem ao menos uma alavanca-alvo e uma direção (↑/↓) — nenhum sem alavanca.
2. **Nenhum componente órfão sobrevivente.** Verificar: nenhum item tem delta líquido **zero ou negativo** (aumenta Esforço/Tempo sem subir Sonho/Probabilidade); os órfãos foram reposicionados ou cortados.
3. **Nenhuma das 4 alavancas abandonada.** Verificar: Sonho, Probabilidade, Tempo e Esforço têm cada uma ≥1 componente servindo-a (os quatro gates por alavanca estão verdes).
4. **Sem claim que infla Sonho derrubando Probabilidade.** Verificar: nenhuma promessa sobrevivente sobe o Sonho à custa da Probabilidade percebida (esse claim recebe veto).
5. **Produto da equação defensável.** Verificar: o scorecard mostra que (Sonho × Probabilidade) / (Tempo × Esforço) subiu de verdade, não por Sonho inflado.
6. **Vetos registrados.** Verificar: cada componente vetado tem registro com alavanca testada, delta líquido e motivo; cada override do chief está no [`decision-registry`](../../data/registries/decision-registry.md).
7. **Flag de pass.** Verificar: a oferta está marcada com `value_equation_pass: true` no registry.

## Evidência Exigida
Para marcar cada item ✅, linkar o `value-equation-scorecard` completo no [`offer-registry`](../../data/registries/offer-registry.md) (tabela `id | componente | alavanca | direção | delta | veredito`), os quatro gates por alavanca verdes ([`value-dream-outcome-gate`](value-dream-outcome-gate.md), [`value-likelihood-gate`](value-likelihood-gate.md), [`value-time-gate`](value-time-gate.md), [`value-effort-gate`](value-effort-gate.md)) e as linhas de veto/override no [`decision-registry`](../../data/registries/decision-registry.md). Cada veto precisa registrar a alavanca testada e o delta líquido. O `value_equation_pass: true` é a evidência-resumo.

## Protocolo de Falha
Item vermelho → **VETO**. Componente órfão (delta líquido ≤ 0) → o `value-equation-engineer` o bloqueia; ele não entra no stack até ser reposicionado para servir a uma alavanca ou ser cortado. Claim que infla Sonho derrubando Probabilidade → **veto do claim**, com recomendação de versão crível. Alavanca abandonada → o engineer recomenda um componente novo para cobri-la (ex.: quick-win para Tempo). **Override:** o veto é sobre o **componente**, não sobre o pipeline — o `offerbook-chief` pode sobrepô-lo com decisão explícita e registrada no [`decision-registry`](../../data/registries/decision-registry.md); sem registro, o veto vale. Conflito com o `money-model-designer` sobre se um componente "paga seu lugar" → escalona ao chief pelo [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md). Re-entrada: corrigido o scorecard (órfãos cortados, alavancas cobertas), o gate é re-submetido.

## Links
- Frameworks: [`value-equation`](../../frameworks/value-equation.md) · [`dream-outcome-amplification`](../../frameworks/value-equation-engineer/dream-outcome-amplification.md) · [`time-delay-compression`](../../frameworks/value-equation-engineer/time-delay-compression.md) · [`effort-sacrifice-reduction`](../../frameworks/value-equation-engineer/effort-sacrifice-reduction.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates por alavanca: [`value-dream-outcome-gate`](value-dream-outcome-gate.md) · [`value-likelihood-gate`](value-likelihood-gate.md) · [`value-time-gate`](value-time-gate.md) · [`value-effort-gate`](value-effort-gate.md)
- Conflito de veto: [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md)
