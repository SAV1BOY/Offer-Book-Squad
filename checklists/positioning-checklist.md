---
id: checklist.positioning-checklist
title: "Checklist — Posicionamento & Lead (lead × consciência, desce para a copy)"
type: checklist
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [positioning/dunford-positioning, positioning/moore-positioning-formula, positioning/category-design, lead-types, awareness-x-sophistication]
registries: [decision-registry]
tags: [checklist, positioning, lead-types, consciencia, d3]
---

# Checklist — Posicionamento & Lead

## Propósito
Este checklist prova que o **posicionamento competitivo está fechado** e que o **tipo de lead casa com o nível de consciência** do mercado — e que ambos descem em instruções claras para a copy. Existe porque a melhor oferta morre com a abertura errada: um lead de oferta direta para um público inconsciente queima a venda, e um lead de história para um público pronto para comprar enrola. O posicionamento define contra o quê a oferta compete e por que vence; o lead define como a copy abre. Sem este checklist verde, o copywriter chuta a abertura. Ele encarna `decision_before_ornament`: a posição e o lead são decisões travadas que a copy executa, não reinventa.

## Dono & Escopo
- **owner_agent:** `positioning-lead-strategist` (define a posição competitiva e trava o tipo de lead).
- **Artefato inspecionado:** o `artifact.positioning`, a `decision.positioning-locked` e a `decision.lead-type-locked`, registrados no [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
A posição competitiva está travada (contra o quê compete, por que vence), o tipo de lead casa com a consciência dominante, e ambos descem em instrução explícita para a copy.

## Itens
1. **Posição competitiva travada.** Como verificar: a `decision.positioning-locked` declara o concorrente/alternativa de referência e o porquê a oferta vence, conforme `dunford-positioning`.
2. **Categoria definida.** Como verificar: a oferta declara em que categoria compete (ou que categoria cria), conforme `category-design`.
3. **Fórmula de posicionamento preenchida.** Como verificar: público-alvo, categoria, benefício e diferencial estão escritos em uma estrutura, conforme `moore-positioning-formula`.
4. **Tipo de lead travado.** Como verificar: a `decision.lead-type-locked` nomeia o lead (oferta, promessa, problema-solução, história, proclamação, secret), conforme `lead-types`.
5. **Lead casa com a consciência.** Como verificar: o lead bate com o nível de consciência dominante — mais consciente → oferta/promessa; inconsciente → problema/história, conforme `awareness-x-sophistication`.
6. **Coerência com a Big Idea.** Como verificar: a posição e o lead sustentam a UMA Big Idea travada, sem contradizê-la.
7. **Desce para a copy.** Como verificar: a posição e o lead estão escritos como instrução acionável que o `vsl-webinar-scriptwriter` e o `email-sms-sequence-writer` executam, não como teoria.
8. **Diferencial defensável.** Como verificar: o porquê-vence apoia-se no mecanismo único, não em adjetivo genérico.

## Evidência Exigida
Para marcar ✅: linkar a `decision.positioning-locked` e a `decision.lead-type-locked` no `decision-registry` (itens 1–4), a nota de fit lead×consciência (item 5), a referência à Big Idea travada (item 6) e a instrução de abertura escrita para a copy (item 7). O diferencial aponta para o mechanism_id (item 8).

## Protocolo de Falha
Item vermelho → a posição/lead volta ao `positioning-lead-strategist` com o defeito nomeado e **bloqueia D3→Offer Book** (parte do HARD STOP). Lead que não casa com a consciência reabre o diagnóstico de consciência. Re-entrada: re-travar posição e lead, atualizar o `decision-registry`, re-submeter. Mudança na Big Idea, no mercado ou na concorrência reabre este checklist e a copy que dele dependia.

## Links
- Frameworks: [`dunford-positioning`](../frameworks/positioning/dunford-positioning.md) · [`moore-positioning-formula`](../frameworks/positioning/moore-positioning-formula.md) · [`category-design`](../frameworks/positioning/category-design.md) · [`lead-types`](../frameworks/lead-types.md) · [`awareness-x-sophistication`](../frameworks/awareness-x-sophistication.md)
- Registries: [`decision-registry`](../data/registries/decision-registry.md)
- Agentes: [`positioning-lead-strategist`](../agents/positioning-lead-strategist.md) · [`big-idea-architect`](../agents/big-idea-architect.md) · [`vsl-webinar-scriptwriter`](../agents/vsl-webinar-scriptwriter.md)
- Gate por agente: [`positioning/positioning-awareness-fit`](positioning/positioning-awareness-fit.md)
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate relacionado: [`offer-book-stack/big-idea-locked-gate`](offer-book-stack/big-idea-locked-gate.md)
