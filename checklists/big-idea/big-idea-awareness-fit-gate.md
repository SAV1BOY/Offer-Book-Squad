---
id: checklist.big-idea.big-idea-awareness-fit-gate
title: "Gate — Fit de Consciência (a tese casa com o nível dominante do mercado)"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [awareness-x-sophistication, big-idea-generator, meta-launch-principle]
registries: [big-idea-registry, decision-registry]
tags: [gate, big-idea, consciencia, awareness, sofisticacao, fit, d3]
---

# Gate — Fit de Consciência

## Propósito
Este gate prova que a Big Idea travada **casa com o nível de consciência dominante** do mercado. A mesma tese que vence num público inconsciente do problema fracassa num público mais-consciente, e vice-versa. Schwartz é a base: o nível de consciência decide quão direta ou indireta a abordagem deve ser. Público inconsciente ou consciente-do-problema pede tese mais indireta — vilão, história, descoberta do mecanismo; público consciente-do-produto ou mais-consciente pede tese mais direta, próxima da oferta e da prova. Um lead errado queima tráfego: ou entrega a oferta cedo demais para quem ainda não sente o problema, ou enrola quem já quer comprar. Este gate amarra a tese ao diagnóstico de mercado e prepara o handoff ao [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md), que escolhe o lead a partir desse fit.

## Dono & Escopo
- **owner_agent:** `big-idea-architect` (**tem poder de veto**: ideia que não casa com a consciência dominante é reprovação).
- **Artefato inspecionado:** o campo `consciencia_alvo` da Big Idea `locked` no [`big-idea-registry`](../../data/registries/big-idea-registry.md), confrontado com o nível de consciência e de sofisticação declarados no `market-brief` (taxonomias [`awareness-levels`](../../lib/taxonomies/awareness-levels.md) e [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md)).

## Condição de Passagem
O nível de consciência-alvo da Big Idea coincide com o nível dominante declarado no market-brief, e a abordagem (direta/indireta) corresponde a esse nível.

## Itens
1. **Consciência dominante declarada.** Verificar: o `market-brief` traz o nível de consciência dominante com evidência (via [`awareness-levels`](../../lib/taxonomies/awareness-levels.md)).
2. **Consciência-alvo registrada.** Verificar: a Big Idea `locked` tem `consciencia_alvo` preenchido no `big-idea-registry`.
3. **Coincidência de nível.** Verificar: o `consciencia_alvo` bate com o nível dominante do market-brief — divergência sem justificativa reprova.
4. **Abordagem coerente com o nível.** Verificar: níveis baixos → tese indireta (vilão/história/descoberta); níveis altos → tese direta (próxima da oferta/prova).
5. **Sofisticação considerada.** Verificar: em mercados muito sofisticados (nível 4–5), a ideia compete por identidade/prova mecânica, não por promessa maior (via [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md)).
6. **Lead errado evitado.** Verificar: a tese não entrega a oferta cedo demais a um público frio nem enrola um público quente.
7. **Pronta para o lead.** Verificar: o fit está documentado para o `positioning-lead-strategist` escolher o lead a partir dele.

## Evidência Exigida
Para marcar ✅: linkar o nível de consciência dominante no `market-brief` e o `consciencia_alvo` no `big-idea-registry` lado a lado (itens 1–3), a nota de abordagem direta/indireta coerente com o nível (itens 4, 6), a consideração de sofisticação (item 5) e o registro do fit para o handoff de posicionamento (item 7).

## Protocolo de Falha
Item vermelho → **veto**: o `big-idea-architect` reprova. Consciência não declarada → devolve ao [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md). Tese indireta para público quente (ou direta para público frio) → reformula a abordagem ou re-ideia. Re-entrada: ajusta o `consciencia_alvo` e a abordagem, registra no `decision-registry` e re-submete. Mudança no diagnóstico de mercado reabre este gate.

## Links
- Gates irmãos: [`big-idea-single-gate`](big-idea-single-gate.md) · [`big-idea-new-big-credible-gate`](big-idea-new-big-credible-gate.md) · [`big-idea-relevant-proprietary-gate`](big-idea-relevant-proprietary-gate.md) · [`big-idea-meta-angle-gate`](big-idea-meta-angle-gate.md)
- Frameworks: [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`big-idea-generator`](../../frameworks/big-idea-generator.md) · [`meta-launch-principle`](../../frameworks/meta-launch-principle.md)
- Taxonomias: [`awareness-levels`](../../lib/taxonomies/awareness-levels.md) · [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md)
- Registries: [`big-idea-registry`](../../data/registries/big-idea-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`big-idea-architect`](../../agents/big-idea-architect.md) · [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
