---
id: checklist.positioning.positioning-category-gate
title: "Gate — Categoria de Referência Torna a Comparação Favorável"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [positioning/category-design, positioning/dunford-positioning, positioning/moore-positioning-formula, positioning/blue-ocean-strategy]
registries: [decision-registry]
tags: [gate, positioning, categoria, comparacao, dunford, moore, d3]
---

# Gate — Categoria de Referência Torna a Comparação Favorável

## Propósito
Este gate prova que a **categoria de referência** escolhida coloca a oferta numa comparação que favorece o produto — e que a decisão de competir, fazer sub-nicho ou criar categoria nova foi tomada com critério, não por moda. Ele existe porque a categoria é o contexto que faz o produto parecer óbvio (Dunford): ancorar na categoria errada transforma a oferta em commodity de preço, enquanto a categoria certa torna a comparação favorável inevitável. O gate audita o primeiro ponto de ramificação do `positioning-lead-strategist`: gerar ≥3 enquadramentos (competir na existente, sub-nicho, criar nova) e pontuar por facilidade de comparação favorável, demanda já existente, custo de educação do mercado e defensabilidade. Materializa a [`positioning/category-design`](../../frameworks/positioning/category-design.md) e a regra de poda do agente: sofisticação baixa + demanda madura → competir (não pague para educar); sofisticação alta/saturada → criar/renomear (fuja do leilão de claims). É o gate que garante que a oferta não entre num leilão de features que ela perde, e que uma categoria nova só seja nomeada quando a saturação realmente exige a fuga.

## Dono & Escopo
- **owner_agent:** `positioning-lead-strategist` (cartógrafo competitivo; decisor vinculante, sem veto).
- **Artefato inspecionado:** o **`artifact.positioning`** — `categoria_referencia`, `categoria_decisao` (competir | sub-nicho | criar-nova) e `ramos_podados` — e a decisão `positioning-locked` no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
A categoria de referência torna a comparação com as alternativas favorável à oferta, e a decisão de competir, fazer sub-nicho ou criar categoria foi justificada pela sofisticação e pela demanda do mercado.

## Itens
1. **Categoria declarada.** Verificar: o `categoria_referencia` está nomeado — a oferta sabe em que categoria o mercado a coloca.
2. **Comparação favorável.** Verificar: dentro da categoria escolhida, a oferta ganha a comparação (não repete a do concorrente nem vira commodity de preço).
3. **Decisão de categoria justificada.** Verificar: `categoria_decisao` (competir | sub-nicho | criar-nova) está justificada pela sofisticação e pela demanda — não por preferência estética.
4. **Regra de poda respeitada.** Verificar: sofisticação baixa + demanda madura → competir (sem pagar educação); sofisticação alta/saturada → sub-nicho ou categoria nova.
5. **Categoria nova tem lastro.** Verificar: se a decisão é criar-nova, há saturação real que a justifica **e** o `mechanism-sheet` traz o diferenciador que a sustenta — não categoria inventada sem base no que o mercado reconhece.
6. **Custo de educação avaliado.** Verificar: o custo de educar o mercado para uma categoria nova foi pesado e, se alto demais, a decisão rebaixou para sub-nicho de categoria existente.
7. **Decisão registrada.** Verificar: categoria, decisão e ramos podados estão em `positioning-locked` no [`decision-registry`](../../data/registries/decision-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar o `artifact.positioning` (`categoria_referencia`, `categoria_decisao`), a lista de alternativas competitivas do `market-brief`, os ≥3 enquadramentos pontuados (comparação favorável, demanda, custo de educação, defensabilidade) e o `ramos_podados`. Quando a decisão é criar-nova, o ponteiro ao diferenciador do `mechanism-sheet` é a evidência-resumo de que a categoria tem lastro real.

## Protocolo de Falha
Item vermelho → a categoria não está pronta. Categoria que repete a do concorrente (comparação desfavorável) → re-enquadra para sub-nicho ou categoria nova até a comparação virar a favor da oferta. Categoria nova sem demanda nem prova → rebaixa para sub-nicho de categoria existente, ou sinaliza o custo de educação ao [`offerbook-chief`](../../agents/offerbook-chief.md). Categoria nova que exige prova que o `proof-registry` não tem → sinaliza ao chief e ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). Alternativas competitivas não mapeadas → posiciona contra a alternativa mais óbvia e marca a posição como "provisória — validar concorrência". O estrategista **não tem veto**; escalona ao chief quando criar categoria custa caro em educação. Re-entrada: re-enquadrada a categoria, o gate é re-submetido; a fórmula completa de Moore é provada no [`positioning-differentiation-gate`](positioning-differentiation-gate.md).

## Links
- Frameworks: [`category-design`](../../frameworks/positioning/category-design.md) · [`dunford-positioning`](../../frameworks/positioning/dunford-positioning.md) · [`moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md) · [`blue-ocean-strategy`](../../frameworks/positioning/blue-ocean-strategy.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`mechanism-architect`](../../agents/mechanism-architect.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Template: [`positioning-template`](../../templates/strategy/positioning-template.md)
- Gates irmãos: [`positioning-awareness-fit`](positioning-awareness-fit.md) · [`positioning-lead-choice-gate`](positioning-lead-choice-gate.md) · [`positioning-differentiation-gate`](positioning-differentiation-gate.md) · [`positioning-descends-to-copy-gate`](positioning-descends-to-copy-gate.md)
