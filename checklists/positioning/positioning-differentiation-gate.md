---
id: checklist.positioning.positioning-differentiation-gate
title: "Gate — Atributo Único Diferencia e a Fórmula de Moore Fecha"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [positioning/moore-positioning-formula, positioning/dunford-positioning, positioning/category-design, positioning/perceived-value-stack]
registries: [decision-registry]
tags: [gate, positioning, diferenciacao, atributo-unico, moore, dunford, d3]
---

# Gate — Atributo Único Diferencia e a Fórmula de Moore Fecha

## Propósito
Este gate prova que a posição travada tem um **atributo de valor único** que separa a oferta das alternativas — e que a **fórmula de Moore fecha sem nenhum campo vazio**. Ele existe porque o erro silencioso do posicionamento é alegar um diferenciador que não diferencia: um atributo que o concorrente também tem, ou que o "fazer sozinho no YouTube" entrega de graça, deixa a oferta empatada e a comparação volta a ser preço. O gate audita o coração da [`positioning/dunford-positioning`](../../frameworks/positioning/dunford-positioning.md) (alternativas reais → atributo único → categoria) e o fechamento da [`positioning/moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md): "para [alvo] que [necessidade], o [produto] é um [categoria] que [benefício], diferente de [alternativa]". O atributo único precisa estar ancorado no diferenciador proprietário do `mechanism-sheet`, não em adjetivo de marketing. Diferente do gate de categoria (que prova que a moldura favorece a comparação) e do de awareness-fit (que prova o fit do lead), este audita a **substância da diferença**: existe um eixo no qual só esta oferta vence, e a frase de Moore o declara por inteiro. É o gate que impede que a posição seja uma promessa genérica vestida de fórmula.

## Dono & Escopo
- **owner_agent:** `positioning-lead-strategist` (cartógrafo competitivo; decisor vinculante, sem poder de veto — sinaliza ao chief quando discorda a montante).
- **Artefato inspecionado:** o **`artifact.positioning`** — campos `atributo_unico`, `moore_formula` e `alternativas_competitivas` — e a decisão `positioning-locked` no [`decision-registry`](../../data/registries/decision-registry.md), cruzados com o diferenciador do `mechanism-sheet`.

## Condição de Passagem
A oferta tem um atributo de valor único que as alternativas mapeadas não entregam, e a fórmula de Moore está completa, sem nenhum dos cinco campos vazio.

## Itens
1. **Atributo único declarado.** Verificar: o `atributo_unico` está nomeado em uma frase concreta — não um adjetivo vago ("melhor", "completo") nem uma lista de features.
2. **Diferencia de verdade.** Verificar: nenhuma das `alternativas_competitivas` mapeadas (concorrente direto, solução caseira, não-ação) entrega esse mesmo atributo — há um eixo onde só esta oferta vence.
3. **Ancorado no mecanismo.** Verificar: o atributo único aponta para o diferenciador proprietário do `mechanism-sheet`, não para uma alegação sem lastro.
4. **Fórmula de Moore completa.** Verificar: a `moore_formula` preenche os cinco campos — alvo, necessidade, categoria, benefício e alternativa — sem nenhum em branco.
5. **Campos da fórmula coerentes.** Verificar: o "benefício" da fórmula é o atributo único (não um benefício genérico) e a "categoria" é a mesma travada no [`positioning-category-gate`](positioning-category-gate.md).
6. **Não vence pelo grátis.** Verificar: o atributo não é algo que o conteúdo gratuito ou o "fazer sozinho" já resolve — se for, o atributo foi reescrito para o eixo de implementação/resultado.
7. **Decisão registrada.** Verificar: `atributo_unico`, `moore_formula` e `alternativas_competitivas` estão em `positioning-locked` no [`decision-registry`](../../data/registries/decision-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar o `artifact.positioning` com o `atributo_unico` e a `moore_formula` completa, a lista de `alternativas_competitivas` do `market-brief` (incluindo a não-ação), e o ponteiro ao diferenciador do `mechanism-sheet` que sustenta o atributo. A tabela "alternativa × entrega esse atributo? (sim/não)" é a evidência-resumo de que a diferença é real; a decisão `positioning-locked` no [`decision-registry`](../../data/registries/decision-registry.md) fecha o registro.

## Protocolo de Falha
Item vermelho → a diferenciação não está pronta. Atributo que o concorrente também entrega (comparação empatada) → o estrategista re-enquadra o atributo para o eixo de implementação ou resultado, onde só esta oferta vence, ou re-enquadra a categoria via [`positioning-category-gate`](positioning-category-gate.md). Atributo sem lastro no mecanismo → sinaliza ao [`mechanism-architect`](../../agents/mechanism-architect.md) que o diferenciador proprietário está fraco. Campo vazio na fórmula de Moore → volta ao L-Module e preenche o campo antes de travar. Atributo que o grátis resolve → reescreve para "implementação guiada com o mecanismo X". O estrategista **não tem veto**; quando a Big Idea não permite posição defensável, **sinaliza** ao [`offerbook-chief`](../../agents/offerbook-chief.md) que a tese pode estar fraca em "Proprietária", sem bloquear o pipeline. Re-entrada: reescrito o atributo e fechada a fórmula, o gate é re-submetido; o fit do lead segue no [`positioning-awareness-fit`](positioning-awareness-fit.md) e a descida à copy no [`positioning-descends-to-copy-gate`](positioning-descends-to-copy-gate.md).

## Links
- Frameworks: [`moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md) · [`dunford-positioning`](../../frameworks/positioning/dunford-positioning.md) · [`category-design`](../../frameworks/positioning/category-design.md) · [`perceived-value-stack`](../../frameworks/positioning/perceived-value-stack.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`mechanism-architect`](../../agents/mechanism-architect.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Template: [`positioning-template`](../../templates/strategy/positioning-template.md)
- Gates irmãos: [`positioning-awareness-fit`](positioning-awareness-fit.md) · [`positioning-lead-choice-gate`](positioning-lead-choice-gate.md) · [`positioning-category-gate`](positioning-category-gate.md) · [`positioning-descends-to-copy-gate`](positioning-descends-to-copy-gate.md)
