---
id: checklist.funnel.funnel-order-bump-gate
title: "Gate — Order Bump (1-clique, baixo atrito, sem roubar o foco)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
frameworks: [offer-to-funnel-mapping, launch/cart-open-close]
registries: [decision-registry]
tags: [gate, funil, order-bump, checkout, aov, atrito, d5]
---

# Gate — Order Bump

## Propósito
Este gate prova que o **order bump no checkout é um complemento de 1-clique e baixo atrito** que sobe o ticket médio sem competir com a oferta de núcleo nem travar a compra. Ele existe porque o checkout é o ponto de maior intenção: um complemento certo eleva o AOV de graça, mas um errado distrai, gera dúvida e derruba a conversão do núcleo. Vale o princípio `value_equation_test`: o bump precisa mover uma alavanca de valor real para o comprador, não ser só um item a mais. O gate exige que o bump seja barato em relação ao núcleo, relevante à compra, com regra de 1-clique explícita para o engenheiro de tech, e posicionado sem roubar o foco do botão de pagar. É a barreira entre um bump que liquida CAC e um que sabota o checkout.

## Dono & Escopo
- **owner_agent:** `funnel-architect` (insere e especifica o order bump no checkout). O `compliance-auditor` detém o **veto** sobre garantia/T&C do item; o `money-model-designer` confirma o encaixe na escada.
- **Artefato inspecionado:** a spec do checkout no `funnel-map`/`page-specs`, com o order bump registrado no [`decision-registry`](../../data/registries/decision-registry.md) e cruzado com o `money-model` (o complemento de alta margem) e o `offer-book` (preço e garantia).

## Condição de Passagem
O order bump é um complemento relevante de 1-clique e baixo atrito, barato em relação ao núcleo, e não compete com o foco da oferta principal.

## Itens
1. **Relevância à compra.** Verificar: o bump complementa o núcleo (ex.: garantia estendida, templates), não é um produto solto.
2. **Preço subordinado.** Verificar: o preço do bump é baixo em relação ao núcleo, lido como "adição óbvia", não nova decisão.
3. **Regra de 1-clique.** Verificar: a spec define o bump como caixa de 1-clique antes do botão de pagar, sem etapa extra.
4. **Foco preservado.** Verificar: o bump não desloca a atenção do CTA principal nem adia a compra do núcleo.
5. **Margem confirmada.** Verificar: o complemento tem alta margem no `money-model`, contribuindo para liquidar o CAC.
6. **Garantia/T&C visíveis.** Verificar: termos do item visíveis, sem inflar o que a oferta entrega (pré-checagem de compliance).
7. **Spec implementável.** Verificar: o engenheiro de tech consegue montar o bump sem adivinhar a regra de exibição ou cobrança.

## Evidência Exigida
Para marcar ✅: linkar a spec de checkout com o bump de 1-clique (itens 1–4), a confirmação de margem no `money-model` (item 5), a paridade de garantia/T&C com o `offer-book` (item 6) e a regra de exibição/cobrança nas `page-specs` (item 7). A decisão de bump aponta para o `decision-registry`.

## Protocolo de Falha
Item vermelho → o `funnel-architect` **reduz o bump** a um complemento de 1-clique e baixo atrito, ou o remove se ele compete com o núcleo. Bump que rouba o foco do CTA principal é reprovado e reposicionado. Garantia ou termo inflado é encaminhado ao [`compliance-auditor`](../../agents/compliance-auditor.md), que detém o veto. Se o complemento não encaixa na escada, escala-se ao [`money-model-designer`](../../agents/money-model-designer.md). Re-entrada: reescrever a spec do bump, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`funnel-architect`](../../agents/funnel-architect.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`funnel-path-coverage-gate`](funnel-path-coverage-gate.md) · [`funnel-redirect-gate`](funnel-redirect-gate.md) · [`funnel-no-dead-end-gate`](funnel-no-dead-end-gate.md) · [`funnel-backend-gate`](funnel-backend-gate.md)
