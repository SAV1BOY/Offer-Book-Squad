---
id: checklist.money-model.money-model-four-parts-gate
title: "Gate — Money Model com as Quatro Partes (atração, núcleo, upsell/downsell, continuidade)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, money-model-designer/attraction-offer-design, money-model-designer/upsell-downsell-logic, money-model-designer/continuity-design]
registries: [offer-registry, price-test-registry]
tags: [gate, money-model, espinha, four-parts, d2, hard-stop, dod-input]
---

# Gate — Money Model com as Quatro Partes

## Propósito
Este gate prova que a espinha existe como **sequência** e não como oferta avulsa. Ele protege o princípio `money_model_spine`: o centro de uma oferta forte é a escada deliberada — atração, núcleo, upsell/downsell e continuidade — não um produto solto com preço. O mínimo aceitável são 2 partes; o alvo são 4. Sem os papéis cobertos, o ticket médio fica raso, o CAC não se liquida e o LTV não cresce. Este é o gate de veto mais estrutural do squad: ele alimenta o [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP) e barra qualquer copy (D4), funil (D5) ou logística (D6) antes de a escada nascer.

## Dono & Escopo
- **owner_agent:** `money-model-designer` (dono da espinha; **veta** o início de copy/funil/logística sem escada).
- **Artefato inspecionado:** a linha de espinha gravada no [`offer-registry`](../../data/registries/offer-registry.md) e os pontos de preço por degrau no [`price-test-registry`](../../data/registries/price-test-registry.md), produzidos pela task `design-money-model` a partir do `money-model` e da planilha `products-and-offers`.

## Condição de Passagem
A escada cobre os papéis com pelo menos 2 partes sequenciadas (alvo 4) e cada degrau tem papel, tipo de oferta e preço declarados no registry.

## Itens
1. **Atração presente.** Verificar: há uma oferta de entrada (tripwire, free+frete, challenge) no `offer-registry` com tipo e preço.
2. **Núcleo presente.** Verificar: existe a oferta-núcleo que entrega o mecanismo, ligada ao `mechanism-sheet`.
3. **Upsell ou downsell presente.** Verificar: há ≥1 oferta de elevação no pico de compra (upsell) e/ou recuperação do "não" (downsell), com preço.
4. **Continuidade desenhada.** Verificar: existe mecânica de recorrência (assinatura, comunidade, clube) com preço e valor contínuo real.
5. **Mínimo de 2 partes (alvo 4).** Verificar: contar os papéis cobertos — ≥2 passa, <2 reprova; marcar quais dos 4 faltam.
6. **Cada degrau move uma alavanca.** Verificar: cada linha aponta a alavanca de valor servida (Sonho/Probabilidade/Tempo/Esforço), conforme o value scorecard.
7. **Orbita o mesmo mecanismo.** Verificar: todos os degraus servem o mecanismo único — nenhum degrau é um produto desconexo.

## Evidência Exigida
Para marcar ✅: linkar a tabela de espinha no `offer-registry` (papel, tipo, preço, alavanca por linha — itens 1–6), os pontos de preço no `price-test-registry`, e a referência ao `mechanism-sheet` que cada degrau orbita (item 7). A contagem de partes cobertas deve aparecer literal na evidência.

## Protocolo de Falha
Item vermelho mantém o veto fechado: o `money-model-designer` **recusa liberar D4+** e devolve com `VETO: espinha incompleta`. Re-entrada: o designer reconfigura a escada (adiciona o papel faltante, troca o tipo de oferta da atração), atualiza o `offer-registry` e re-submete. Oferta avulsa disfarçada de money model = reprovação automática. Só o [`offerbook-chief`](../../agents/offerbook-chief.md) libera exceção, com decisão gravada no [`decision-registry`](../../data/registries/decision-registry.md). Mudança em qualquer degrau reabre este gate.

## Links
- Sibling gates: [`money-model-sequence-gate`](money-model-sequence-gate.md) · [`money-model-cac-liquidation-gate`](money-model-cac-liquidation-gate.md) · [`money-model-cta-per-step-gate`](money-model-cta-per-step-gate.md) · [`money-model-propagation-gate`](money-model-propagation-gate.md)
- Frameworks: [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`attraction-offer-design`](../../frameworks/money-model-designer/attraction-offer-design.md) · [`upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md) · [`continuity-design`](../../frameworks/money-model-designer/continuity-design.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`price-test-registry`](../../data/registries/price-test-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`money-model-designer`](../../agents/money-model-designer.md) · [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
