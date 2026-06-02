---
id: checklist.unit-econ.unit-econ-margin-gate
title: "Gate — Margem de Contribuição Saudável e Stack Sem Item Órfão"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [offer-stack-builder, guarantee-design, scarcity-urgency-engine, magic-naming, risk-reversal-ladder]
registries: [offer-registry]
tags: [gate, unit-econ, margem, stack, item-orfao, d2, valor-percebido]
---

# Gate — Margem de Contribuição Saudável e Stack Sem Item Órfão

## Propósito
Este gate prova que a **margem de contribuição** de cada degrau é saudável e que o **offer stack** empilha valor percebido acima do preço **sem item órfão** — sem componente que aumenta o custo de entrega sem aumentar valor. Ele existe porque uma oferta pode liquidar o CAC e ainda ter margem corroída por itens que custam caro entregar e não movem a venda: cada item do stack precisa pagar seu lugar. O gate junta as duas metades do mandato do analista — a margem (a aritmética) e o stack (a embalagem de valor) — e se conecta ao veto do `value-equation-engineer`: um item que não move nenhuma alavanca de valor é órfão e será vetado lá. Ele também exige que as âncoras do stack sejam **reais** (preço de alternativas, custo de entregar), não fictícias, sob pena de veto do compliance. Diferente dos gates de razão/payback/liquidação, este olha a **qualidade da margem e da composição do stack**: o valor percebido supera o preço de forma defensável, item a item.

## Dono & Escopo
- **owner_agent:** `unit-economics-stack-analyst` (calcula margem e monta o stack; sem veto, aciona value-engineer/compliance).
- **Artefato inspecionado:** a **`margem_contrib`**, o **`offer-stack`** (item, valor ancorado, custo de entrega) e o `valor_percebido_total` vs `preco` no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
A margem de contribuição por degrau é saudável, o stack tem valor percebido acima do preço sem item órfão, e todas as âncoras de valor são reais.

## Itens
1. **Margem por degrau conhecida.** Verificar: a `margem_contrib` está calculada por degrau (receita menos custo variável de entrega).
2. **Margem saudável.** Verificar: a margem está acima do piso do caso ou o desvio está justificado (degrau de atração pode ter margem fina por design, compensado a jusante).
3. **Valor percebido > preço.** Verificar: a soma do `valor_ancorado` do stack supera o `preco` de forma que o preço pareça uma pechincha.
4. **Sem item órfão.** Verificar: cada item do stack aumenta valor percebido sem estourar o custo de entrega — nenhum item com custo alto e delta de valor nulo (que o [`value-equation-engineer`](../../agents/value-equation-engineer.md) vetaria).
5. **Âncoras reais.** Verificar: cada `valor_ancorado` se baseia em preço de alternativa real ou custo de entregar — sem âncora fictícia que o compliance derrubaria.
6. **Custo de entrega registrado.** Verificar: cada item do stack tem o `custo_entrega` declarado, para confrontar valor × custo.
7. **Margem e stack registrados.** Verificar: `margem_contrib`, stack (item/valor/custo) e `valor_percebido_total` vs `preco` estão no [`offer-registry`](../../data/registries/offer-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar a `unit-economics-sheet` e o `offer-stack` no [`offer-registry`](../../data/registries/offer-registry.md) (tabela `item | valor_ancorado | custo_entrega`), o cálculo de `margem_contrib` por degrau, e o confronto `valor_percebido_total` vs `preco`. A justificativa de cada âncora (a alternativa real ou o custo que a sustenta) é a evidência-resumo de que o stack não infla com valores fictícios.

## Protocolo de Falha
Item vermelho → não fecha o stack. Margem fina sem justificativa → revê custo de entrega ou preço. Item órfão (custo alto, valor nulo) → **flag ao [`value-equation-engineer`](../../agents/value-equation-engineer.md)** (que veta o componente); o analista reposiciona ou remove o item do stack. Âncora fictícia → troca por valor ancorado real (preço de alternativa, custo de entregar) para o compliance não vetar. Custo de entrega não declarado → completa antes de confrontar valor × custo. O analista **não tem veto**: item órfão → flag ao value-engineer; âncora fictícia → flag ao [`compliance-auditor`](../../agents/compliance-auditor.md); margem inviável → flag ao [`money-model-designer`](../../agents/money-model-designer.md) e ao [`offerbook-chief`](../../agents/offerbook-chief.md). Re-entrada: saneados margem e stack, o gate é re-submetido.

## Links
- Frameworks: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`guarantee-design`](../../frameworks/guarantee-design.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`magic-naming`](../../frameworks/magic-naming.md) · [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Template: [`offer-stack-template`](../../templates/offer/offer-stack-template.md)
- Veto de item órfão: [`value-no-orphan-lever-gate`](../value/value-no-orphan-lever-gate.md)
- Gates irmãos: [`unit-econ-ltv-cac-gate`](unit-econ-ltv-cac-gate.md) · [`unit-econ-payback-gate`](unit-econ-payback-gate.md) · [`unit-econ-breakeven-gate`](unit-econ-breakeven-gate.md) · [`unit-econ-cac-liquidation-gate`](unit-econ-cac-liquidation-gate.md)
