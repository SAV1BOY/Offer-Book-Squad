---
id: checklist.offer-book-stack.offer-architecture-gate
title: "Gate — Arquitetura de Oferta (Mecanismo + Valor + Money Model + Preço + Unit Econ)"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [unique-mechanism, value-equation, money-model-sequence, value-based-pricing, offer-stack-builder]
registries: [offer-registry, price-test-registry]
tags: [gate, offer-architecture, mechanism, value-equation, money-model, pricing, unit-economics, d2, dod-input]
---

# Gate — Arquitetura de Oferta

## Propósito
Este gate prova que a **arquitetura de oferta (D2)** está completa e coerente. Ele existe para garantir a espinha do princípio `money_model_spine`: o centro é a *sequência*, não a oferta avulsa. Sem mecanismo único, alavancas de valor acionadas, money model sequenciado, preço derivado de valor e unit economics conhecidos, a oferta não sustenta copy nem funil. É o segundo insumo do [`offer-book-dod-gate`](offer-book-dod-gate.md), encadeado após o [`intelligence-complete-gate`](intelligence-complete-gate.md).

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (libera D2→D3); o `value-equation-engineer` e o `money-model-designer` podem **vetar** componentes.
- **Artefato inspecionado:** o bloco de arquitetura no [`offer-registry`](../../data/registries/offer-registry.md) e os testes de preço no [`price-test-registry`](../../data/registries/price-test-registry.md), produzidos por mechanism/value/money-model/pricing/unit-econ.

## Condição de Passagem
O mecanismo único está nomeado e provado, cada alavanca de valor tem ação concreta, o money model tem suas partes sequenciadas, o preço deriva de valor por método declarado, e LTV:CAC + payback são conhecidos.

## Itens
1. **Mecanismo único nomeado.** Verificar: nome próprio do mecanismo + descrição em UMA frase no `offer-registry`.
2. **Mecanismo provado.** Verificar: ≥1 `proof_id` ligado ao porquê o mecanismo funciona.
3. **Nenhuma alavanca órfã.** Verificar: as 4 alavancas (sonho, probabilidade, tempo, esforço) têm ação concreta listada.
4. **Money model com partes sequenciadas.** Verificar: ≥2 partes (alvo 4: atração→upsell→downsell→continuidade) com ordem explícita; `money_model_min_parts` do config respeitado.
5. **CTA por degrau.** Verificar: cada degrau do money model tem um próximo passo único.
6. **Preço derivado de valor.** Verificar: método nomeado (van Westendorp / Gabor-Granger / conjoint / value-based) e número de WTP gravados no `price-test-registry`.
7. **Unit economics conhecidos.** Verificar: LTV, CAC, payback e liquidação de CAC de front-end com os números no registry.

## Evidência Exigida
Para marcar ✅: linkar a linha do `offer-registry` (mecanismo, alavancas, money model — itens 1–5), a entrada do `price-test-registry` com método e WTP (item 6) e a planilha/linha de unit economics (item 7). Cada número precisa de origem rastreável, não estimativa solta.

## Protocolo de Falha
Item vermelho → o `offerbook-chief` devolve ao agente dono (mechanism/value/money-model/pricing/unit-econ) com o defeito nomeado e **não libera D3**. O `value-equation-engineer` reprova qualquer componente sem alavanca; o `money-model-designer` bloqueia se a escada não existir. Re-entrada: corrigir o componente, atualizar o registry, re-submeter. Mudança no money model obriga reavaliar preço e unit econ.

## Links
- Frameworks: [`unique-mechanism`](../../frameworks/unique-mechanism.md) · [`value-equation`](../../frameworks/value-equation.md) · [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`guarantee-design`](../../frameworks/guarantee-design.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`price-test-registry`](../../data/registries/price-test-registry.md)
- Agentes: [`mechanism-architect`](../../agents/mechanism-architect.md) · [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) · [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md)
- Agrega para: [`offer-book-dod-gate`](offer-book-dod-gate.md)
