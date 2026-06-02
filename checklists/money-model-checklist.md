---
id: checklist.money-model-checklist
title: "Checklist — Money Model (4 partes sequenciadas, preço/gatilho/CTA por degrau)"
type: checklist
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, money-model-designer/attraction-offer-design, money-model-designer/upsell-downsell-logic, money-model-designer/continuity-design, money-model-designer/offer-ladder-sequencing]
registries: [offer-registry, price-test-registry]
tags: [checklist, money-model, sequence, d2, spine]
---

# Checklist — Money Model

## Propósito
Este checklist prova que existe uma **espinha de money model** — a *sequência* atração→upsell→downsell→continuidade — e não uma oferta avulsa. Existe porque o centro do squad é a sequência, não o produto isolado (`money_model_spine`). Sem cada degrau com preço, gatilho e CTA definidos, o lançamento não tem como liquidar CAC no front-end nem maximizar valor por cliente. Cada degrau precisa de uma razão para existir e de um caminho claro para o próximo. É o que transforma uma venda única numa máquina de receita.

## Dono & Escopo
- **owner_agent:** `money-model-designer` (dono da espinha; nada de copy/funil/logística antes da escada existir).
- **Artefato inspecionado:** o money model registrado no [`offer-registry`](../data/registries/offer-registry.md) (`templates/offer/money-model-template` preenchido), com os preços testados no [`price-test-registry`](../data/registries/price-test-registry.md).

## Condição de Passagem
As 4 partes (atração, upsell, downsell, continuidade) estão sequenciadas com preço, gatilho e CTA por degrau, e cada degrau move o cliente ao próximo — mínimo aceitável 2 partes, alvo 4.

## Itens
1. **Oferta de atração definida.** Como verificar: degrau de entrada no `offer-registry` com preço e objetivo (liquidar CAC ou maximizar conversão), conforme `attraction-offer-design`.
2. **Upsell sequenciado.** Como verificar: ≥1 upsell com gatilho (após qual compra) e CTA no `offer-registry`, conforme `upsell-downsell-logic`.
3. **Downsell sequenciado.** Como verificar: ≥1 downsell com gatilho (após qual recusa) e CTA registrados.
4. **Continuidade definida.** Como verificar: oferta recorrente (assinatura/programa) com preço e ciclo de cobrança, conforme `continuity-design` — ou marcada `não-aplicável` com motivo.
5. **Preço por degrau.** Como verificar: cada degrau tem preço numérico no `offer-registry`, rastreável ao `price-test-registry`.
6. **Gatilho por degrau.** Como verificar: cada degrau declara o evento que o dispara (compra anterior, recusa, prazo).
7. **CTA por degrau.** Como verificar: cada degrau tem uma chamada para ação única e explícita.
8. **Sequência sem buraco lógico.** Como verificar: seguir a escada do início ao fim — todo degrau tem origem e destino, sem becos, conforme `offer-ladder-sequencing`.
9. **≥2 partes presentes.** Como verificar: contar as partes ativas — mínimo 2 (`money_model_min_parts`), alvo 4; abaixo de 2 reprova.

## Evidência Exigida
Para marcar ✅: linkar as linhas do `offer-registry` que descrevem cada degrau (itens 1–4), os preços rastreados ao `price-test-registry` (item 5), a tabela degrau→gatilho→CTA (itens 6–7) e o diagrama/tabela da sequência completa (item 8). A contagem de partes (item 9) aparece no resumo do money model.

## Protocolo de Falha
Item vermelho → o `money-model-designer` corrige a escada e **bloqueia downstream** (copy/funil/ops não avançam sem espinha). Degrau sem preço volta ao `pricing-wtp-strategist`; degrau sem viabilidade volta ao `unit-economics-stack-analyst`. Re-entrada: corrige o degrau, atualiza o `offer-registry` e re-submete. Mudança na sequência reabre os checklists downstream que dependem da escada.

## Links
- Frameworks: [`money-model-sequence`](../frameworks/money-model-sequence.md) · [`attraction-offer-design`](../frameworks/money-model-designer/attraction-offer-design.md) · [`upsell-downsell-logic`](../frameworks/money-model-designer/upsell-downsell-logic.md) · [`continuity-design`](../frameworks/money-model-designer/continuity-design.md) · [`offer-ladder-sequencing`](../frameworks/money-model-designer/offer-ladder-sequencing.md)
- Registries: [`offer-registry`](../data/registries/offer-registry.md) · [`price-test-registry`](../data/registries/price-test-registry.md)
- Agentes: [`money-model-designer`](../agents/money-model-designer.md) · [`pricing-wtp-strategist`](../agents/pricing-wtp-strategist.md) · [`unit-economics-stack-analyst`](../agents/unit-economics-stack-analyst.md)
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate relacionado: [`offer-book-stack/offer-architecture-gate`](offer-book-stack/offer-architecture-gate.md)
