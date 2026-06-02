---
id: checklist.value.value-time-gate
title: "Gate — Atraso de Tempo Comprimido com Primeiro Resultado Cedo (quick-win mapeado)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [value-equation, value-equation-engineer/time-delay-compression]
registries: [offer-registry]
tags: [gate, value, tempo, time-delay, d2, alavanca, quick-win]
---

# Gate — Atraso de Tempo Comprimido

## Propósito
Este gate prova que o `value-equation-engineer` comprimiu o **Atraso de tempo** — antecipou o primeiro resultado percebido pelo avatar. Existe porque o tempo é um denominador da Equação de Valor: quanto mais cedo o avatar sente o primeiro ganho, maior o valor percebido e menor a chance de ele desistir antes do resultado final. Esta é a alavanca mais frequentemente **abandonada**: ofertas prometem a transformação completa em meses, sem nenhum quick-win nos primeiros dias. O gate força um primeiro resultado cedo e concreto ("primeiro ajuste de roupa em 14 dias"), que segura o avatar e prova o mecanismo na prática. Sem ele, a alavanca Tempo fica órfã e o `value-no-orphan-lever-gate` reprova.

## Dono & Escopo
- **owner_agent:** `value-equation-engineer` (aplica [`time-delay-compression`](../../frameworks/value-equation-engineer/time-delay-compression.md)).
- **Artefato inspecionado:** a linha **Tempo** do `value-equation-scorecard`, com o primeiro resultado e o prazo, no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O Atraso de tempo está comprimido com um primeiro resultado concreto e cedo, mapeado a um componente da oferta, sem prometer prazo inacreditável.

## Itens
1. **Primeiro resultado nomeado.** Verificar: o scorecard nomeia um primeiro ganho concreto que o avatar percebe cedo ("primeiro ajuste de roupa em 14 dias").
2. **Prazo declarado.** Verificar: há um prazo explícito para esse primeiro resultado, não "em breve".
3. **Quick-win mapeado a componente.** Verificar: existe um componente da oferta que entrega esse primeiro resultado (ex.: protocolo dos 7 dias), não uma promessa solta.
4. **Prazo crível.** Verificar: o prazo do primeiro resultado não estoura a Probabilidade percebida (prazo fantasia vira descrença).
5. **Distinto do resultado final.** Verificar: o primeiro resultado é um marco intermediário, não a transformação completa rebatizada.
6. **Move a alavanca declarada.** Verificar: o scorecard declara o Tempo como alavanca com direção (↓ no atraso) e delta estimado.
7. **Não cria esforço extra.** Verificar: antecipar o resultado não aumenta o Esforço do avatar (cruzar com o [`value-effort-gate`](value-effort-gate.md)).

## Evidência Exigida
Para marcar cada item ✅, linkar a linha Tempo do scorecard no [`offer-registry`](../../data/registries/offer-registry.md), o componente que entrega o quick-win e o prazo declarado. A credibilidade do prazo é checada contra a Probabilidade ([`value-likelihood-gate`](value-likelihood-gate.md)). A ausência de esforço extra linka o gate de Esforço. O permalink da linha do registry conta como evidência; um "primeiro resultado" sem componente que o entregue não é marcado ✅.

## Protocolo de Falha
Item vermelho → o `value-equation-engineer` desenha um quick-win real para cobrir a alavanca Tempo. Alavanca Tempo abandonada (ninguém serve) → o engineer **recomenda um componente novo** (ex.: protocolo dos 7 dias) para cobri-la. Prazo fantasia → recalibrar para um prazo crível. Primeiro resultado que é só o final rebatizado → define um marco intermediário verdadeiro. Re-entrada: comprimido o tempo com quick-win mapeado, o gate é re-submetido e alimenta o [`value-no-orphan-lever-gate`](value-no-orphan-lever-gate.md).

## Links
- Frameworks: [`value-equation`](../../frameworks/value-equation.md) · [`time-delay-compression`](../../frameworks/value-equation-engineer/time-delay-compression.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`money-model-designer`](../../agents/money-model-designer.md)
- Par (esforço): [`value-effort-gate`](value-effort-gate.md) · Credibilidade do prazo: [`value-likelihood-gate`](value-likelihood-gate.md)
- Veto agregador: [`value-no-orphan-lever-gate`](value-no-orphan-lever-gate.md)
