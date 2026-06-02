---
id: checklist.positioning.positioning-awareness-fit
title: "Gate — Lead Casa com a Consciência do Mercado"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [lead-types, awareness-x-sophistication, positioning/moore-positioning-formula]
registries: [decision-registry]
tags: [gate, positioning, lead, consciencia, awareness, d3, fit]
---

# Gate — Lead Casa com a Consciência do Mercado

## Propósito
Este gate prova que o **tipo de lead travado** abre a copy no ponto exato em que o mercado está — que a abertura "encontra o prospect onde ele está", e não onde o estrategista gostaria que ele estivesse. Ele existe porque o erro de abertura mais caro do `positioning-lead-strategist` é cruzar o lead com a consciência errada: usar Oferta direta num público frio queima o tráfego, e usar História num público que já conhece o produto desperdiça o "sim" maduro. O gate materializa a matriz consciência×sofisticação da [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) e os seis leads da [`lead-types`](../../frameworks/lead-types.md). Ele força uma escolha entre os seis leads (Oferta, Promessa, Problema-Solução, Segredo, Proclamação, História) ancorada no nível de consciência declarado pelo `market-brief`. Diferente do gate de lead-choice (que audita o **rigor da seleção** entre alternativas), este audita o **fit final**: o lead vencedor de fato casa com a consciência 1–5? É o gate obrigatório que o agente cita no seu critério de parada e que reprova qualquer abertura que ignore onde o prospect está na escada de consciência.

## Dono & Escopo
- **owner_agent:** `positioning-lead-strategist` (decisor vinculante, sem poder de veto — sinaliza ao chief quando discorda a montante).
- **Artefato inspecionado:** o **`artifact.positioning`** — campos `lead_type`, `consciencia_alvo` e `lead_justificativa` — e a decisão `lead-type-locked` no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
O tipo de lead travado casa com o nível de consciência dominante declarado no `market-brief`, com justificativa explícita que conecta a abertura ao estado do prospect.

## Itens
1. **Consciência declarada.** Verificar: o `market-brief` declara o nível de consciência dominante (1–5) com evidência — sem isso, o gate devolve ao [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md).
2. **Lead é um dos seis.** Verificar: o `lead_type` é exatamente um dos seis (Oferta, Promessa, Problema-Solução, Segredo, Proclamação, História), não um híbrido vago.
3. **Lead casa com a consciência.** Verificar: o par (lead × consciência) bate com a matriz da [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) — ex.: consciência 1 → História/Proclamação; consciência 5 → Oferta direta.
4. **Sem Oferta direta para público frio.** Verificar: o lead não usa Oferta direta com consciência 1–2 (queima tráfego), nem História com consciência 5 (desperdiça maturidade).
5. **Justificativa explícita.** Verificar: o `lead_justificativa` explica por que esta abertura casa com este estado de consciência, em uma frase concreta.
6. **Lead carrega o gancho da Big Idea.** Verificar: a abertura escolhida é congruente com o gancho/vilão da Big Idea travada (não briga com a tese).
7. **Multi-consciência tratado.** Verificar: se o lançamento mistura segmentos (lista quente + tráfego frio), o lead foi travado **por segmento**, não uma abertura única para todos.

## Evidência Exigida
Para marcar cada item ✅, linkar o `artifact.positioning` com `lead_type`, `consciencia_alvo` e `lead_justificativa`, a linha de consciência do `market-brief` (com evidência), e a célula correspondente da matriz da [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md). A decisão `lead-type-locked` no [`decision-registry`](../../data/registries/decision-registry.md), com `ramos_podados` listando os leads descartados, é a evidência-resumo de que o fit foi deliberado.

## Protocolo de Falha
Item vermelho → o lead não está pronto para descer à copy. Consciência ausente → devolve ao [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md); sem ela não há como casar o lead. Lead que contradiz a consciência (ex.: Oferta direta para frio) → corrige via a matriz; público frio recebe História/Proclamação. Lead que briga com o gancho da Big Idea → realinha à tese travada (a abertura serve a Big Idea, nunca o contrário). Lançamento multi-consciência com abertura única → trava o lead por segmento e entrega a matriz. O estrategista **não tem veto**: quando discorda de algo a montante, **sinaliza** ao [`offerbook-chief`](../../agents/offerbook-chief.md) e registra a ressalva, sem bloquear o pipeline. Re-entrada: corrigido o par lead×consciência, o gate é re-submetido.

## Links
- Frameworks: [`lead-types`](../../frameworks/lead-types.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md) · [`big-idea-architect`](../../agents/big-idea-architect.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Template: [`positioning-template`](../../templates/strategy/positioning-template.md)
- Gates irmãos: [`positioning-lead-choice-gate`](positioning-lead-choice-gate.md) · [`positioning-category-gate`](positioning-category-gate.md) · [`positioning-differentiation-gate`](positioning-differentiation-gate.md) · [`positioning-descends-to-copy-gate`](positioning-descends-to-copy-gate.md)
