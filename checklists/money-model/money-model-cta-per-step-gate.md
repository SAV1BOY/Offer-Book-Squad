---
id: checklist.money-model.money-model-cta-per-step-gate
title: "Gate — Um CTA por Degrau (cada passo tem um próximo passo único)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, money-model-designer/offer-ladder-sequencing, money-model-designer/upsell-downsell-logic, offer-to-funnel-mapping]
registries: [offer-registry, price-test-registry]
tags: [gate, money-model, cta, proximo-passo, power-of-one, d2]
---

# Gate — Um CTA por Degrau

## Propósito
Este gate prova que cada degrau da espinha tem **um, e apenas um, próximo passo claro**. Uma escada sem CTA por degrau é um corredor com portas sem maçaneta: o cliente chega, mas não sabe para onde ir, e a sequência morre no atrito. O money model só converte estranho em comprador e comprador em cliente recorrente se cada degrau empurrar deliberadamente para o seguinte. Aqui o princípio `clarity_before_volume` e o Power of One se aplicam ao nível do passo: dois pedidos no mesmo degrau dividem a decisão e derrubam a conversão. Este gate também garante que o funil a jusante possa **espelhar** a escada — o [`funnel-architect`](../../agents/funnel-architect.md) precisa de um destino único por degrau para mapear páginas sem becos sem saída. Sem um próximo passo por degrau, a escada existe no papel mas não roda na prática, e o handoff para copy e funil fica incompleto.

## Dono & Escopo
- **owner_agent:** `money-model-designer` (dono da espinha; garante o próximo passo único de cada degrau antes de liberar D4+).
- **Artefato inspecionado:** a coluna `cta` (próximo passo) de cada degrau na tabela de espinha do [`offer-registry`](../../data/registries/offer-registry.md), produzida pela task `design-money-model` a partir do `money-model` e da planilha `products-and-offers`, cruzada com os pontos de preço do [`price-test-registry`](../../data/registries/price-test-registry.md).

## Condição de Passagem
Cada degrau da espinha declara exatamente um próximo passo (CTA), sem ambiguidade e sem pedido duplo, e o conjunto de CTAs encadeia a sequência do começo ao fim.

## Itens
1. **CTA presente em todo degrau.** Verificar: cada linha da espinha no `offer-registry` tem a coluna `cta` preenchida — nenhuma fica vazia.
2. **Um único pedido por degrau.** Verificar: cada `cta` faz **um** pedido (comprar, agendar, ativar) — dois pedidos concorrentes no mesmo degrau reprovam (Power of One no passo).
3. **CTA aponta para o degrau seguinte.** Verificar: o próximo passo de cada degrau leva ao degrau imediatamente seguinte da sequência (atração→núcleo→upsell→…), sem salto que pule um papel.
4. **Próximo passo é concreto e acionável.** Verificar: o CTA usa verbo de ação e destino claro ("ativar minha vaga", "adicionar o acelerador"), não uma frase vaga ("saiba mais").
5. **Continuidade tem CTA de adesão e de saída.** Verificar: o degrau de continuidade declara como o cliente entra e como cancela — recorrência sem saída clara é sinalizada ao [`compliance-auditor`](../../agents/compliance-auditor.md).
6. **Sem CTA órfão ou em loop.** Verificar: nenhum CTA aponta para um degrau inexistente nem devolve o cliente a um passo já concluído.
7. **CTAs encadeiam ponta a ponta.** Verificar: seguindo os CTAs do primeiro ao último degrau, a sequência fecha sem buraco — o funil pode espelhá-la.

## Evidência Exigida
Para marcar ✅: linkar a tabela de espinha no `offer-registry` com a coluna `cta` por degrau preenchida (itens 1–4, 7), a mecânica de adesão/saída da continuidade (item 5) e a verificação de encadeamento (itens 6–7) — o caminho dos CTAs deve aparecer explícito na evidência, passo a passo, do primeiro degrau ao último.

## Protocolo de Falha
Item vermelho mantém o handoff bloqueado: o `money-model-designer` reescreve o próximo passo do degrau com defeito (define o pedido único, corrige o destino), atualiza o `offer-registry` e re-submete. Degrau sem CTA, ou com CTA duplo, é reprovação automática. Continuidade sem saída clara volta com flag ao [`compliance-auditor`](../../agents/compliance-auditor.md). Re-entrada: corrige a coluna `cta`, revalida contra [`offer-ladder-sequencing`](../../frameworks/money-model-designer/offer-ladder-sequencing.md) e re-submete. Mudança de degrau ou de destino reabre este gate e o [`money-model-sequence-gate`](money-model-sequence-gate.md).

## Links
- Gates irmãos: [`money-model-four-parts-gate`](money-model-four-parts-gate.md) · [`money-model-sequence-gate`](money-model-sequence-gate.md) · [`money-model-cac-liquidation-gate`](money-model-cac-liquidation-gate.md) · [`money-model-propagation-gate`](money-model-propagation-gate.md)
- Frameworks: [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`offer-ladder-sequencing`](../../frameworks/money-model-designer/offer-ladder-sequencing.md) · [`upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md) · [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`price-test-registry`](../../data/registries/price-test-registry.md)
- Agentes: [`money-model-designer`](../../agents/money-model-designer.md) · [`funnel-architect`](../../agents/funnel-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
