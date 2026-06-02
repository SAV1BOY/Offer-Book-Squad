---
id: data.controls.control-template
title: "Dossiê de Control (EXEMPLO ILUSTRATIVO / Template)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [controls, winner, template, example, illustrative]
---

# Dossiê de Control (EXEMPLO ILUSTRATIVO / Template)

> **AVISO:** Este arquivo é um **template ilustrativo (seed)**. A peça e os números são **fictícios**, só para mostrar o formato. Não use como fato. Cada control real copia este dossiê e preenche com a peça medida.

## Propósito

Mostrar o **dossiê completo** de uma peça campeã — o detalhe que a tabela-índice ([`control-registry`](../registries/control-registry.md)) não cabe. O dossiê responde: o que é a peça, qual ângulo carregava, contra quem ganhou e **por que** ganhou. Toda nova copy do mesmo tipo precisa bater este control.

## Identificação

| Campo | Valor (exemplo) |
|---|---|
| `control_id` | `ctrl-exemplo-vsl-01` |
| `asset_type` | vsl |
| `title` | VSL Método X v3 (amostra) |
| `channel` | vsl-funnel |
| `status` | live |
| `owner_agent` | vsl-webinar-scriptwriter |

## Ângulo & Big Idea

- **Big Idea** ([`big-idea-registry`](../registries/big-idea-registry.md)): `metodo-x-exemplo` — "o equilíbrio hormonal pós-40 é a causa que ninguém te contou".
- **Ângulo do lead**: consciente do problema, inconsciente da solução — nomeia a causa antes da cura.
- **Vilão**: a dieta genérica que ignora o hormônio.

## Oferta & Claims

- **Oferta** ([`offer-registry`](../registries/offer-registry.md)): `core-exemplo-90d` (Mentoria 90 Dias).
- **Claims usados** ([`claim-registry`](../registries/claim-registry.md)): `exemplo-resultado-30d` (resultado em 30 dias, com prova ligada).
- Cada claim tem prova em [`proof-registry`](../registries/proof-registry.md) — sem prova, o `compliance-auditor` veta.

## Métrica & Resultado

| Métrica | Valor (exemplo) | Resultado |
|---|---|---|
| `conversion-rate` | 4,1% | `control` |

- **Benchmark de contexto**: 4,1% fica acima da faixa típica de VSL (ver [`benchmarks/conversion-benchmarks-by-industry.md`](../benchmarks/conversion-benchmarks-by-industry.md)).

## Contra quem ganhou

- `beat_control_id`: `ctrl-exemplo-vsl-00` (versão anterior, 3,2%).
- Lift: +0,9 ponto percentual (amostra).

## Por que funcionou (hipótese)

A v3 trocou a abertura de promessa direta por **nomear a causa hormonal** antes de prometer. Isso encaixou no nível de consciência do avatar. A prova social com mulheres 40+ derrubou a objeção "não funciona para mim".

## Ligação à decisão e ao índice

- Linha em [`control-registry`](../registries/control-registry.md).
- Decisão em [`decision-registry`](../registries/decision-registry.md) (`dec-exemplo-0001`).
- Se virar padrão de ouro do squad, entra em [`winners/winners-index.md`](../winners/winners-index.md).

## DoD do dossiê

Pronto quando: identificação completa, métrica medida com fonte, contra quem ganhou nomeado, claims ligados à prova, e a hipótese de vitória escrita em uma frase.
