---
id: archive.deprecated-offers.deprecation-record-template
title: "Template — Registro de Descontinuação de Oferta"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
registries: [data.registry.offer-registry, data.registry.lessons-learned-registry, data.registry.decision-registry]
tags: [template, deprecation, deprecated-offers, sunset, memory]
---

# Template — Registro de Descontinuação de Oferta

## Propósito

Este template padroniza o **registro de morte de uma oferta**. Ele força o squad a nomear o motivo com número, não com palpite. O `knowledge-librarian` preenche um por oferta aposentada. O resultado responde a três perguntas: por que saiu, o que prova isso, e o que a substitui. Sem este registro, o time ressuscita ofertas mortas e repete o erro que as matou.

Um bom registro de descontinuação é honesto sobre a causa raiz. Ele separa "a oferta era ruim" de "o timing era ruim". Ele cita a decisão e a métrica. Isto cumpre `evidence_before_opinion` e `decision_before_ornament`.

## O que arquivar

Arquive um registro por oferta, nomeado `deprecation-<offer_id>.md`. Inclua a versão final, o motivo, a evidência métrica, a substituta e a lição. Não duplique a oferta — ela já vive no [`offer-registry`](../../data/registries/offer-registry.md).

## Formato / Template

Copie o bloco abaixo. Troque cada `{{PLACEHOLDER}}`. O exemplo ao final é **ilustrativo** — apague antes de salvar o registro real.

```md
# Descontinuação — {{NOME_DA_OFERTA}}

- **offer_id:** {{offer-id-kebab}}
- **Versão final:** {{vX.Y}}
- **Papel no Money Model:** {{atração | núcleo | upsell | downsell | continuidade}}
- **Data de descontinuação:** {{YYYY-MM-DD}}
- **Substituída por:** {{offer-id | nenhuma}}

## Por que saiu
{{O motivo em 2-3 frases. Causa raiz, não sintoma.}}

## Evidência
| Sinal | Métrica | Limiar | Veredito |
|---|---|---|---|
| {{margem caiu}} | {{valor}} | {{limiar}} | {{abaixo}} |

## O que a substitui
{{Oferta substituta + por que ela resolve o que esta não resolvia. Ou "nenhuma".}}

## Lição
{{O que isto ensina sobre quando aposentar. Vira linha em lessons-learned-registry.}}

## Links
- offer: {{offer-id}} · decisão: {{decision-id}} · lição: {{lesson-id}}
```

## Lições para reuso

A lição central de cada descontinuação — o sinal de que uma oferta está morrendo — vira uma linha no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), categoria `offer` ou `money-model`. Sinais recorrentes (ex.: queda de margem por X períodos) sobem a default via `promoted_to`, virando gatilho de revisão automática.

## Liga com

- [`offer-registry`](../../data/registries/offer-registry.md) — onde a oferta viva está catalogada.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — destino da lição.
- [`decision-registry`](../../data/registries/decision-registry.md) — a decisão que aposentou.
- [`README.md`](README.md) — visão da pasta.

---

> **Exemplo ilustrativo (apagar):** Descontinuação `core-exemplo-90d` v2.3 — papel núcleo, aposentada 2025-05-15, substituída por `core-exemplo-anual`. Por que saiu: refund rate subiu para 14% após o mercado virar estágio 4 de sofisticação. Evidência: margem líquida caiu de 38% para 11%. Lição: revisar o mecanismo quando refund passa de 10% por dois ciclos.
