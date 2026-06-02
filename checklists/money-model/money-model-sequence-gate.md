---
id: checklist.money-model.money-model-sequence-gate
title: "Gate — Sequência do Money Model (ordem e timing fazem sentido)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, money-model-designer/offer-ladder-sequencing, money-model-designer/upsell-downsell-logic]
registries: [offer-registry, price-test-registry]
tags: [gate, money-model, sequencia, timing, ordenacao, d2]
---

# Gate — Sequência do Money Model

## Propósito
Este gate prova que a escada não é só um conjunto de partes — é uma **ordem** com timing. Quatro ofertas certas na ordem errada vendem mal: o upsell precisa cair no pico de compra, o downsell logo após o "não", a continuidade depois da primeira vitória. Ele protege a tese de que *quando* e *como* você oferece importa tanto quanto *o quê*. A meta dos 30 dias — o cliente liquida a aquisição e financia mais clientes — só se realiza se a sequência respeitar os momentos psicológicos da compra. Sem ordem coerente, a espinha de [`money-model-four-parts-gate`](money-model-four-parts-gate.md) existe no papel mas falha na prática.

## Dono & Escopo
- **owner_agent:** `money-model-designer` (dono da ordenação e do timing da escada).
- **Artefato inspecionado:** a coluna de ordem/timing da espinha no [`offer-registry`](../../data/registries/offer-registry.md) e a sequência registrada via task `design-money-model`, com os offsets de cada degrau (imediato, mesma sessão, pós-entrega).

## Condição de Passagem
Os degraus estão em ordem lógica, cada um disparado no momento psicológico certo, e a sequência mira liquidar o CAC no front-end dentro da janela alvo.

## Itens
1. **Atração vem primeiro.** Verificar: o degrau de atração abre a sequência — nenhum degrau caro antecede a entrada de baixo atrito.
2. **Upsell no pico de compra.** Verificar: o upsell dispara imediatamente após o "sim" do núcleo (mesma sessão/checkout), não dias depois.
3. **Downsell após o "não".** Verificar: o downsell é oferecido a quem recusou o upsell, não a quem já comprou tudo.
4. **Continuidade após a primeira vitória.** Verificar: a recorrência entra depois de o cliente ter o primeiro resultado/entrega, não antes de provar valor.
5. **Timing declarado por degrau.** Verificar: cada linha tem um offset explícito (T+0, mesma sessão, T+X dias) no `offer-registry`.
6. **Sem colisão ou salto.** Verificar: dois degraus não disparam no mesmo instante de forma conflitante, e nenhum degrau exige um anterior que não veio.
7. **Janela dos 30 dias mirada.** Verificar: a ordem busca liquidar o CAC no front-end dentro da janela alvo (atração+upsell cobrem a aquisição cedo).

## Evidência Exigida
Para marcar ✅: linkar a tabela de espinha ordenada no `offer-registry` com a coluna de timing/offset por degrau (itens 1–6) e a nota de sequência que justifica a janela dos 30 dias (item 7). A ordem dos papéis deve aparecer explícita na evidência.

## Protocolo de Falha
Item vermelho → o `money-model-designer` reordena a escada (move o upsell para o checkout, atrasa a continuidade) e re-submete. Sequência que não mira a liquidação do CAC volta junto ao [`money-model-cac-liquidation-gate`](money-model-cac-liquidation-gate.md). Re-entrada: corrige o offset no `offer-registry`, revalida contra `offer-ladder-sequencing` e re-submete. Mudança de degrau ou de timing reabre este gate e o `four-parts-gate`.

## Links
- Sibling gates: [`money-model-four-parts-gate`](money-model-four-parts-gate.md) · [`money-model-cac-liquidation-gate`](money-model-cac-liquidation-gate.md) · [`money-model-cta-per-step-gate`](money-model-cta-per-step-gate.md) · [`money-model-propagation-gate`](money-model-propagation-gate.md)
- Frameworks: [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`offer-ladder-sequencing`](../../frameworks/money-model-designer/offer-ladder-sequencing.md) · [`upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`price-test-registry`](../../data/registries/price-test-registry.md)
- Agentes: [`money-model-designer`](../../agents/money-model-designer.md) · [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
