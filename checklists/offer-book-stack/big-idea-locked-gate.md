---
id: checklist.offer-book-stack.big-idea-locked-gate
title: "Gate — Big Idea Travada (UMA Big Idea)"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [big-idea-generator, power-of-one, meta-launch-principle, awareness-x-sophistication]
registries: [big-idea-registry, decision-registry]
tags: [gate, big-idea, power-of-one, positioning, d3, dod-input]
---

# Gate — Big Idea Travada

## Propósito
Este gate prova que existe **UMA Grande Ideia travada** (princípio `one_big_idea` / Power of One) e que o posicionamento foi fixado. Ele existe porque múltiplas ideias diluem a mensagem e quebram a conversão: um lançamento carrega UMA tese, UM avatar, UMA promessa, UM próximo passo. É o terceiro insumo do [`offer-book-dod-gate`](offer-book-dod-gate.md), encadeado após o [`offer-architecture-gate`](offer-architecture-gate.md) — a Big Idea destila a inteligência e a oferta em uma frase que vende.

## Dono & Escopo
- **owner_agent:** `offerbook-chief`; o `big-idea-architect` entrega a tese e pode **vetar** versões concorrentes (múltiplas ideias = reprovação).
- **Artefato inspecionado:** a entrada travada no [`big-idea-registry`](../../data/registries/big-idea-registry.md) e a decisão de posicionamento gravada no [`decision-registry`](../../data/registries/decision-registry.md), produzidas por `big-idea-architect` e `positioning-lead-strategist`.

## Condição de Passagem
Exatamente UMA Big Idea está travada no registry, passa nos 5 critérios (nova, grande, crível, ajustada à consciência, com promessa-gancho-vilão) e o posicionamento está fixado.

## Itens
1. **Uma única Big Idea.** Verificar: o `big-idea-registry` tem exatamente UMA entrada com status `locked` para este lançamento; alternativas estão marcadas `pruned`.
2. **Nova, grande, crível.** Verificar: a tese declara o que há de novo, por que é grande e qual prova a torna crível (≤25 palavras na frase-núcleo).
3. **Ajuste à consciência.** Verificar: o tipo de lead (lead-types) bate com o nível de consciência declarado no `intelligence-complete-gate`.
4. **Promessa-gancho-vilão.** Verificar: os três elementos estão preenchidos e coerentes entre si.
5. **Posicionamento fixado.** Verificar: a categoria/alternativa competitiva e o atributo-chave estão gravados no `decision-registry`.
6. **Rastreável à oferta.** Verificar: a Big Idea aponta para o mecanismo único e a promessa central do `offer-registry` (sem contradição).
7. **Decisão registrada.** Verificar: `decision_id` com a opção escolhida e as alternativas podadas, com motivo e data.

## Evidência Exigida
Para marcar ✅: linkar a entrada `locked` no `big-idea-registry` (itens 1–4, 6), a linha de posicionamento no `decision-registry` (item 5) e o `decision_id` com alternativas podadas (item 7). A frase-núcleo deve aparecer literal na evidência.

## Protocolo de Falha
Item vermelho → o `big-idea-architect` reprova e o `offerbook-chief` **não libera o offer-book-dod-gate**. Mais de uma ideia ativa = reprovação automática até poda. Re-entrada: o `big-idea-architect` poda para UMA, registra a decisão e re-submete; o `positioning-lead-strategist` reajusta a posição se a consciência não bate.

## Links
- Frameworks: [`big-idea-generator`](../../frameworks/big-idea-generator.md) · [`power-of-one`](../../frameworks/power-of-one.md) · [`meta-launch-principle`](../../frameworks/meta-launch-principle.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`lead-types`](../../frameworks/lead-types.md)
- Registries: [`big-idea-registry`](../../data/registries/big-idea-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`big-idea-architect`](../../agents/big-idea-architect.md) · [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Agrega para: [`offer-book-dod-gate`](offer-book-dod-gate.md)
