---
id: checklist.value.value-effort-gate
title: "Gate — Esforço e Sacrifício Reduzidos (atalhos e feito-por-você mapeados ao medo do avatar)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [value-equation, value-equation-engineer/effort-sacrifice-reduction]
registries: [offer-registry]
tags: [gate, value, esforco, sacrificio, d2, alavanca, feito-por-voce]
---

# Gate — Esforço e Sacrifício Reduzidos

## Propósito
Este gate prova que o `value-equation-engineer` reduziu o **Esforço e sacrifício** que o avatar teme — o segundo denominador da Equação de Valor. Existe porque o avatar não compra só o resultado, ele compra **quão pouco vai precisar fazer e abrir mão** para chegar lá. Cada sacrifício temido no VOC ("não sei o que comer", "não tenho tempo") é uma oportunidade de alavanca: atalhos, feito-por-você, templates, automações que removem o trabalho. É também onde moram as **features órfãs** mais comuns — conteúdo extra que, em vez de reduzir, **aumenta** o esforço (mais um curso para consumir). O gate garante que cada redução de esforço ataca um sacrifício real do VOC, e que nada no stack aumenta o esforço sem subir outra alavanca.

## Dono & Escopo
- **owner_agent:** `value-equation-engineer` (aplica [`effort-sacrifice-reduction`](../../frameworks/value-equation-engineer/effort-sacrifice-reduction.md)).
- **Artefato inspecionado:** a linha **Esforço** do `value-equation-scorecard`, com os sacrifícios removidos, no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O Esforço e o sacrifício estão reduzidos por componentes que atacam medos reais do VOC, e nenhum componente do stack aumenta o esforço sem compensar em outra alavanca.

## Itens
1. **Sacrifícios do VOC mapeados.** Verificar: o scorecard lista os sacrifícios que o avatar teme, extraídos do VOC ("não sei o que comer", "não tenho tempo").
2. **Redução por componente.** Verificar: cada sacrifício temido tem um componente que o remove (planilha de receitas, feito-por-você, atalho), não uma promessa vaga.
3. **Sem componente que aumenta esforço.** Verificar: nenhum item do stack aumenta o trabalho do avatar sem subir Sonho/Probabilidade (senão é órfão/negativo → veto).
4. **Feito-por-você priorizado onde dói.** Verificar: nos sacrifícios mais temidos, há "feito-por-você" ou atalho, não só "faça você mesmo com nosso material".
5. **Move a alavanca declarada.** Verificar: o scorecard declara o Esforço como alavanca com direção (↓) e delta estimado por componente.
6. **Custo de entrega sinalizado.** Verificar: reduções caras de entregar (consultoria 1:1) estão sinalizadas ao [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) para não quebrar a margem.
7. **Coerente com Tempo.** Verificar: a redução de esforço não atrasa o primeiro resultado (cruzar com o [`value-time-gate`](value-time-gate.md)).

## Evidência Exigida
Para marcar cada item ✅, linkar a linha Esforço do scorecard no [`offer-registry`](../../data/registries/offer-registry.md), os verbatims de sacrifício do VOC e o componente que remove cada um. Componentes que aumentam esforço sem compensar são listados como vetados, com motivo. O custo de entrega sinalizado linka o handoff ao unit-econ. O permalink da linha do registry conta como evidência.

## Protocolo de Falha
Item vermelho → o `value-equation-engineer` mapeia um componente que reduz o sacrifício temido. Componente que aumenta esforço sem subir outra alavanca → **veto do componente** (órfão/negativo), com reposicionamento sugerido (ex.: "1000 vídeos" vira "20 vídeos essenciais"). Sacrifício do VOC sem redução → desenha um atalho/feito-por-você. Redução cara demais → sinaliza ao unit-econ antes de manter. Re-entrada: reduzido o esforço sobre os medos reais, o gate é re-submetido e alimenta o [`value-no-orphan-lever-gate`](value-no-orphan-lever-gate.md).

## Links
- Frameworks: [`value-equation`](../../frameworks/value-equation.md) · [`effort-sacrifice-reduction`](../../frameworks/value-equation-engineer/effort-sacrifice-reduction.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md)
- Par (tempo): [`value-time-gate`](value-time-gate.md)
- Veto agregador: [`value-no-orphan-lever-gate`](value-no-orphan-lever-gate.md)
