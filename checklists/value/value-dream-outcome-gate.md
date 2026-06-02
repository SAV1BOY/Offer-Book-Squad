---
id: checklist.value.value-dream-outcome-gate
title: "Gate — Sonho Amplificado e Crível na Voz do Avatar (sem inflar acima da Probabilidade)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [value-equation, value-equation-engineer/dream-outcome-amplification]
registries: [offer-registry]
tags: [gate, value, sonho, dream-outcome, d2, alavanca, credibilidade]
---

# Gate — Sonho Amplificado e Crível

## Propósito
Este gate prova que o `value-equation-engineer` amplificou o **Sonho** (resultado desejado) na linguagem do avatar, sem inflá-lo acima da Probabilidade percebida. Existe porque o Sonho é o numerador mais sedutor e mais perigoso da Equação de Valor: inflar é fácil ("perca 10kg em 7 dias"), mas se a Probabilidade percebida não acompanha, o claim vira inacreditável e **destrói** valor. Este gate garante que o Sonho é o que o avatar de fato quer — extraído do VOC, não do que o produto faz — e que ele está amplificado até o limite do crível, não além. É a primeira das quatro alavancas; sozinho não basta, mas mal calibrado contamina todo o produto da equação.

## Dono & Escopo
- **owner_agent:** `value-equation-engineer` (aplica [`dream-outcome-amplification`](../../frameworks/value-equation-engineer/dream-outcome-amplification.md)).
- **Artefato inspecionado:** a linha **Sonho** do `value-equation-scorecard`, registrada no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O Sonho está escrito na voz do avatar, amplificado até o limite do crível, e a Probabilidade percebida sustenta o tamanho do claim.

## Itens
1. **Sonho na voz do avatar.** Verificar: o Sonho usa a linguagem literal do VOC ("caber na roupa antiga sem passar fome"), não o jargão do produto.
2. **É o que o avatar quer.** Verificar: o Sonho é o resultado que o avatar deseja (ligado ao JTBD), não a descrição da feature.
3. **Amplificado, não inventado.** Verificar: o Sonho está elevado ao máximo defensável, mas ancorado em algo real que a oferta entrega.
4. **Probabilidade acompanha.** Verificar: o tamanho do Sonho não estoura a Probabilidade percebida pelo avatar cético (cruzar com o [`value-likelihood-gate`](value-likelihood-gate.md)).
5. **Sem claim de descrença.** Verificar: o Sonho não é grande o bastante para gerar rejeição imediata no VOC (senão é caso de veto do claim).
6. **Move a alavanca declarada.** Verificar: o scorecard declara o Sonho como alavanca com direção (↑) e um delta estimado.
7. **Coerente com o mecanismo.** Verificar: o Sonho é o resultado que o mecanismo provado promete entregar, não mais do que isso.

## Evidência Exigida
Para marcar cada item ✅, linkar a linha Sonho do `value-equation-scorecard` no [`offer-registry`](../../data/registries/offer-registry.md), o verbatim do VOC que ancora o desejo e a checagem cruzada com a Probabilidade. A coerência com o mecanismo linka o [`mechanism-one-sentence-gate`](../mechanism/mechanism-one-sentence-gate.md). O permalink da linha do registry conta como evidência; um Sonho sem âncora no VOC não é marcado ✅.

## Protocolo de Falha
Item vermelho → o `value-equation-engineer` reancorar o Sonho no VOC e recalibrar contra a Probabilidade. Sonho inflado que gera descrença → o engineer aciona seu **poder de veto do claim** e recomenda a versão crível (ex.: "-5kg em 30 dias" no lugar de "-10kg em 7 dias"). Sonho que é feature, não desejo → reescreve como o resultado que o avatar quer. Sem o desejo explícito no VOC → pede o verbatim ao `avatar-voc-investigator` e marca a alavanca como baixa confiança. Re-entrada: calibrado o Sonho, o gate é re-submetido e alimenta o [`value-no-orphan-lever-gate`](value-no-orphan-lever-gate.md).

## Links
- Frameworks: [`value-equation`](../../frameworks/value-equation.md) · [`dream-outcome-amplification`](../../frameworks/value-equation-engineer/dream-outcome-amplification.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md)
- Par que o equilibra: [`value-likelihood-gate`](value-likelihood-gate.md)
- Veto agregador: [`value-no-orphan-lever-gate`](value-no-orphan-lever-gate.md)
