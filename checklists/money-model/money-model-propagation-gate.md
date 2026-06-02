---
id: checklist.money-model.money-model-propagation-gate
title: "Gate — Propagação da Espinha (o funil, a copy e a logística espelham a escada)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, money-model-designer/offer-ladder-sequencing, offer-to-funnel-mapping]
registries: [offer-registry, price-test-registry, decision-registry]
tags: [gate, money-model, propagacao, espinha, downstream, coerencia, d2]
---

# Gate — Propagação da Espinha

## Propósito
Este gate prova que a espinha **propaga** sem distorção para tudo o que vem depois dela: a copy, o funil, a logística e os afiliados precisam espelhar a mesma sequência de degraus, os mesmos preços e os mesmos próximos passos. Ele protege o princípio `money_model_spine` na fronteira do handoff — onde a escada mais costuma vazar. Uma espinha perfeita que o funil contradiz (uma página que vende o upsell antes do núcleo) ou que a copy ignora (um VSL sem o degrau de continuidade) volta a ser uma oferta avulsa na prática. Este gate é o contrato de saída do [`money-model-designer`](../../agents/money-model-designer.md): garante que cada agente a jusante recebe a sequência **completa, sequenciada e rastreável** ao `offer-registry`. É também a salvaguarda contra deriva silenciosa — quando alguém muda um preço ou um degrau a jusante sem reabrir os gates da espinha.

## Dono & Escopo
- **owner_agent:** `money-model-designer` (dono da espinha; valida que os downstream a espelham antes e depois do HARD STOP).
- **Artefato inspecionado:** a tabela de espinha-fonte no [`offer-registry`](../../data/registries/offer-registry.md) e os pontos de preço no [`price-test-registry`](../../data/registries/price-test-registry.md), confrontados com os artefatos derivados — o mapa do [`funnel-architect`](../../agents/funnel-architect.md), os roteiros do [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md), as sequências do [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) e o que o [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) precisa operar.

## Condição de Passagem
Todo artefato derivado da espinha reproduz a mesma ordem de degraus, os mesmos preços e os mesmos CTAs do `offer-registry`, sem inventar, omitir ou reordenar degraus.

## Itens
1. **Funil espelha a escada.** Verificar: o mapa de funil tem uma etapa por degrau, na mesma ordem, sem etapa que pule ou inverta um papel — via [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md).
2. **Copy cobre todos os degraus.** Verificar: VSL/sales letter e sequências de e-mail referenciam o núcleo, o(s) upsell/downsell e a continuidade — nenhum degrau some na copy.
3. **Preços batem com o registry.** Verificar: cada preço citado a jusante é idêntico ao do `price-test-registry` — nenhum número divergente.
4. **CTAs batem com a espinha.** Verificar: os próximos passos na copy e no funil são os mesmos da coluna `cta` do `offer-registry` (consistente com o [`money-model-cta-per-step-gate`](money-model-cta-per-step-gate.md)).
5. **Logística cobre cada degrau.** Verificar: o que cada degrau exige operar (entrega, acesso, recorrência) está repassado ao `events-logistics-coordinator`.
6. **Rastreabilidade ao registry.** Verificar: cada artefato derivado aponta de volta para o `ladder_id` de origem no `offer-registry` (`traceability_before_eloquence`).
7. **Deriva reabre os gates.** Verificar: qualquer mudança de degrau/preço a jusante está registrada no [`decision-registry`](../../data/registries/decision-registry.md) e reabriu os gates da espinha — nenhuma alteração silenciosa.

## Evidência Exigida
Para marcar ✅: linkar a tabela-fonte do `offer-registry` lado a lado com cada artefato derivado (mapa de funil, roteiros, matriz de e-mail) mostrando ordem, preços e CTAs idênticos (itens 1–4), a passagem de logística por degrau (item 5), o ponteiro de cada derivado ao `ladder_id` (item 6) e o registro de qualquer mudança no `decision-registry` (item 7).

## Protocolo de Falha
Item vermelho → o `money-model-designer` devolve ao agente a jusante com `VETO: espinha não espelhada` e aponta a divergência (degrau omitido, preço diferente, ordem trocada). Re-entrada: o agente dono do artefato derivado corrige para espelhar o `offer-registry` e re-submete; mudança legítima de degrau/preço reabre os gates [`money-model-four-parts-gate`](money-model-four-parts-gate.md), [`money-model-sequence-gate`](money-model-sequence-gate.md) e [`money-model-cac-liquidation-gate`](money-model-cac-liquidation-gate.md). Só o [`offerbook-chief`](../../agents/offerbook-chief.md) autoriza uma divergência deliberada, com decisão gravada no `decision-registry`.

## Links
- Gates irmãos: [`money-model-four-parts-gate`](money-model-four-parts-gate.md) · [`money-model-sequence-gate`](money-model-sequence-gate.md) · [`money-model-cac-liquidation-gate`](money-model-cac-liquidation-gate.md) · [`money-model-cta-per-step-gate`](money-model-cta-per-step-gate.md)
- Frameworks: [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`offer-ladder-sequencing`](../../frameworks/money-model-designer/offer-ladder-sequencing.md) · [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`price-test-registry`](../../data/registries/price-test-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`money-model-designer`](../../agents/money-model-designer.md) · [`funnel-architect`](../../agents/funnel-architect.md) · [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) · [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) · [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
