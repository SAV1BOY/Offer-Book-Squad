---
id: checklist.value.value-likelihood-gate
title: "Gate — Probabilidade Percebida de Sucesso Sustentada por Prova e Garantia"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [value-equation, value-equation-engineer/likelihood-of-achievement]
registries: [offer-registry]
tags: [gate, value, probabilidade, likelihood, d2, alavanca, garantia]
---

# Gate — Probabilidade Percebida Sustentada

## Propósito
Este gate prova que o `value-equation-engineer` sustentou a **Probabilidade percebida** de sucesso com prova, garantia e o mecanismo provado — não com promessa. Existe porque a Probabilidade é o contrapeso do Sonho: um Sonho gigante com Probabilidade baixa vale menos que um Sonho médio crível, porque o avatar não acredita que **ele** vai conseguir. Esta alavanca é onde o ceticismo morre: depoimentos de pares, garantia que reverte o risco, e o mecanismo que explica por que vai funcionar desta vez. É a alavanca que o `mechanism-proof-gate` habilita a montante — sem mecanismo provado, a Probabilidade flutua. Calibrá-la bem é o que permite ao engineer amplificar o Sonho com segurança.

## Dono & Escopo
- **owner_agent:** `value-equation-engineer` (aplica [`likelihood-of-achievement`](../../frameworks/value-equation-engineer/likelihood-of-achievement.md)).
- **Artefato inspecionado:** a linha **Probabilidade** do `value-equation-scorecard`, com as provas/garantias que a sustentam, no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
A Probabilidade percebida está sustentada por prova, garantia e mecanismo, no tamanho necessário para o avatar cético acreditar que ele próprio vai conseguir.

## Itens
1. **Prova ligada à Probabilidade.** Verificar: a Probabilidade se apoia em prova rastreável (casos, dados, depoimentos) do [`proof-registry`](../../data/registries/proof-registry.md), não em afirmação.
2. **Garantia reverte risco.** Verificar: há garantia que move o risco do comprador para o vendedor, e ela está declarada como alavanca de Probabilidade↑.
3. **Mecanismo sustenta o "por quê".** Verificar: o mecanismo provado ([`mechanism-proof-gate`](../mechanism/mechanism-proof-gate.md)) explica por que vai funcionar desta vez.
4. **Endereça o medo do avatar.** Verificar: a Probabilidade ataca os medos do VOC que derrubam a crença ("já tentei e não funcionou pra mim").
5. **Prova por pares quando o job é social.** Verificar: se o JTBD dominante é social, a prova prioriza casos de pares respeitados, não só métricas.
6. **Move a alavanca declarada.** Verificar: o scorecard declara a Probabilidade como alavanca com direção (↑) e delta estimado.
7. **Aguenta o Sonho.** Verificar: a Probabilidade é alta o bastante para sustentar o tamanho do Sonho do [`value-dream-outcome-gate`](value-dream-outcome-gate.md) — senão o produto da equação cai.

## Evidência Exigida
Para marcar cada item ✅, linkar a linha Probabilidade do scorecard no [`offer-registry`](../../data/registries/offer-registry.md), os `proof_id` que a sustentam no [`proof-registry`](../../data/registries/proof-registry.md) e a garantia declarada. A prova por pares (quando aplicável) linka o [`avatar-jtbd-gate`](../avatar/avatar-jtbd-gate.md). A checagem Sonho-vs-Probabilidade linka o gate par. O permalink das provas conta como evidência.

## Protocolo de Falha
Item vermelho → o `value-equation-engineer` reforça a Probabilidade com prova/garantia adicional ou recalibrar o Sonho para baixo. Probabilidade que não aguenta o Sonho → o engineer aciona o **veto do claim** (Sonho↑/Probabilidade↓ derruba o produto da equação) e recomenda a versão crível. Prova fraca em ponto crítico → flag ao `proof-credibility-curator`. Mecanismo ainda provisório → marca o scorecard como condicional e bloqueia os componentes que dependem do elo não-provado. Re-entrada: sustentada a Probabilidade, o gate é re-submetido e alimenta o [`value-no-orphan-lever-gate`](value-no-orphan-lever-gate.md).

## Links
- Frameworks: [`value-equation`](../../frameworks/value-equation.md) · [`likelihood-of-achievement`](../../frameworks/value-equation-engineer/likelihood-of-achievement.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md)
- Agentes: [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md)
- Habilitado por: [`mechanism-proof-gate`](../mechanism/mechanism-proof-gate.md)
- Par que ele equilibra: [`value-dream-outcome-gate`](value-dream-outcome-gate.md) · Veto agregador: [`value-no-orphan-lever-gate`](value-no-orphan-lever-gate.md)
