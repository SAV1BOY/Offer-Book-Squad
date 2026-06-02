---
id: checklist.funnel-map-checklist
title: "Checklist — Mapa de Funil (sem becos sem saída, cobre o 'não' e o pós-compra)"
type: checklist
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
frameworks: [offer-to-funnel-mapping, launch/cart-open-close, money-model-sequence]
registries: [decision-registry, offer-registry, control-registry]
tags: [checklist, funnel, mapa, no-dead-end, backend, pos-compra, d5]
---

# Checklist — Mapa de Funil

## Propósito
Este checklist prova que o mapa de funil traduz a espinha do money model em páginas e caminhos **sem nenhum beco sem saída**. Existe porque um funil bonito perde dinheiro nos buracos: uma página sem próximo passo, um "não" do cliente que termina em tela morta, um pós-compra que esquece de oferecer o degrau seguinte. Cada degrau da escada — atração, upsell, downsell, continuidade — precisa virar uma página com uma saída clara. O caminho do "sim" e o caminho do "não" precisam estar desenhados. Sem este checklist verde, o funil deixa cliente preso, deixa receita de backend na mesa e quebra o princípio `money_model_spine`. Ele garante que cada clique leva a uma decisão e que nenhum caminho morre antes da venda ou da recompra.

## Dono & Escopo
- **owner_agent:** `funnel-architect` (desenha o mapa e responde pelos caminhos); o [`money-model-designer`](../agents/money-model-designer.md) confirma que cada degrau virou página e o [`tech-links-deliverability-engineer`](../agents/tech-links-deliverability-engineer.md) recebe as URLs.
- **Artefato inspecionado:** o **mapa de funil** (`templates/funnel-tech/funnel-map-template` preenchido) e as page-specs, registrados no [`decision-registry`](../data/registries/decision-registry.md), derivados do [`offer-registry`](../data/registries/offer-registry.md).

## Condição de Passagem
Cada página tem um próximo passo explícito, cada degrau do money model aparece no mapa, o caminho do "não" tem destino e o pós-compra oferece o degrau seguinte — zero beco sem saída.

## Itens
1. **Cada degrau virou página.** Como verificar: comparar a escada do `offer-registry` com o mapa; todo degrau (atração, upsell, downsell, continuidade) tem página correspondente, conforme [`offer-to-funnel-mapping`](../frameworks/offer-to-funnel-mapping.md).
2. **Toda página tem próximo passo.** Como verificar: percorrer o mapa página a página; cada uma aponta para a próxima ou para uma ação — nenhuma termina em tela morta.
3. **Caminho do "não" coberto.** Como verificar: cada ponto de recusa (não comprou, não fez upsell) tem destino — downsell, sequência de recuperação ou saída digna, conforme [`launch/cart-open-close`](../frameworks/launch/cart-open-close.md).
4. **Pós-compra oferece o seguinte.** Como verificar: a página de obrigado/entrega de cada compra apresenta o próximo degrau da sequência, não um fim de linha.
5. **Backend existe.** Como verificar: o funil tem caminho de continuidade/recompra registrado; venda única sem backend é sinalizada.
6. **Opt-in e captura.** Como verificar: o ponto de entrada captura o lead antes do pitch, com destino claro pós-opt-in.
7. **Abandono tratado.** Como verificar: carrinho/checkout abandonado dispara caminho de recuperação mapeado.
8. **Coerência de URLs.** Como verificar: cada página do mapa tem slug/URL nomeado e único, pronto para o `tech-links-deliverability-engineer` instrumentar.

## Evidência Exigida
Para marcar ✅: linkar o mapa no `decision-registry`, a tabela degrau→página que prova a cobertura (item 1), o diagrama de fluxo mostrando próximo passo em cada nó (itens 2–4), a marcação do caminho de backend/continuidade (item 5) e a lista de URLs nomeadas (item 8). O caminho de abandono (item 7) aparece como ramo do diagrama.

## Protocolo de Falha
Item vermelho → o mapa volta ao `funnel-architect` com o beco nomeado e **não vai para implementação**. Página sem próximo passo ou "não" sem destino é redesenhado antes de qualquer URL viva. Degrau faltando reabre conversa com o `money-model-designer`. Re-entrada: corrigir o mapa, atualizar o `decision-registry`, re-submeter. Mudança na escada do money model reabre este checklist por inteiro.

## Links
- Gate relacionado: [`funnel/funnel-no-dead-end-gate`](funnel/funnel-no-dead-end-gate.md) · [`funnel/funnel-backend-gate`](funnel/funnel-backend-gate.md)
- Frameworks: [`offer-to-funnel-mapping`](../frameworks/offer-to-funnel-mapping.md) · [`launch/cart-open-close`](../frameworks/launch/cart-open-close.md) · [`money-model-sequence`](../frameworks/money-model-sequence.md)
- Registries: [`decision-registry`](../data/registries/decision-registry.md) · [`offer-registry`](../data/registries/offer-registry.md) · [`control-registry`](../data/registries/control-registry.md)
- Agentes: [`funnel-architect`](../agents/funnel-architect.md) · [`money-model-designer`](../agents/money-model-designer.md) · [`tech-links-deliverability-engineer`](../agents/tech-links-deliverability-engineer.md)
- Checklists vizinhos: [`tech-deliverability-checklist`](tech-deliverability-checklist.md) · [`cart-close-checklist`](cart-close-checklist.md)
