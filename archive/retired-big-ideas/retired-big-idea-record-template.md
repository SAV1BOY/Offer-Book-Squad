---
id: archive.retired-big-ideas.retired-big-idea-record-template
title: "Template — Registro de Big Idea Aposentada"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
registries: [data.registry.big-idea-registry, data.registry.lessons-learned-registry, data.registry.decision-registry]
tags: [template, retired-big-idea, big-idea, positioning, memory]
---

# Template — Registro de Big Idea Aposentada

## Propósito

Este template padroniza o **registro de aposentadoria de uma Big Idea**. Ele força o squad a nomear o motivo da retirada com número, não com palpite. O `knowledge-librarian` preenche um por tese retirada. O resultado responde a três perguntas: por que a tese saiu, o que prova isso, e o que a substitui. Sem este registro, o time recicla teses gastas como se fossem novas e perde ângulos que só faltou timing.

Um bom registro separa "a ideia era fraca" de "o mercado saturou". Ele mostra a trajetória: o melhor resultado que a tese deu e quando começou a cair. Ele cita a decisão e a métrica. Isto cumpre `evidence_before_opinion` e `one_big_idea` — uma tese por vez, e cada aposentadoria documentada antes da próxima entrar. Assim o squad nunca improvisa um ângulo "novo" que já queimou.

## O que arquivar

Arquive um registro por tese, nomeado `retired-<big_idea_id>.md`. Inclua a versão final, o motivo, a evidência métrica, a substituta, os controls que a carregaram e a lição. Não duplique a tese — ela já vive no [`big-idea-registry`](../../data/registries/big-idea-registry.md).

## Formato / Template

Copie o bloco abaixo. Troque cada `{{PLACEHOLDER}}`. O exemplo ao final é **ilustrativo** — apague antes de salvar o registro real.

```md
# Big Idea Aposentada — {{NOME_DA_TESE}}

- **big_idea_id:** {{big-idea-id-kebab}}
- **Versão final:** {{vX.Y}}
- **Ângulo central:** {{a promessa/tese em uma frase}}
- **Data de aposentadoria:** {{YYYY-MM-DD}}
- **Substituída por:** {{big-idea-id | nenhuma}}

## Por que foi retirada
{{O motivo em 2-3 frases. Saturação, fadiga, mecanismo superado ou troca por ângulo melhor.}}

## Trajetória & Evidência
| Sinal | Pico | Última medição | Veredito |
|---|---|---|---|
| {{conversão}} | {{x%}} | {{y%}} | {{em queda}} |

## O que a substitui
{{Tese substituta + por que ela ataca o que esta já não atacava. Ou "nenhuma".}}

## Lição
{{O que isto ensina sobre quando trocar de tese. Vira linha em lessons-learned-registry.}}

## Links
- big-idea: {{big-idea-id}} · decisão: {{decision-id}} · lição: {{lesson-id}} · controls: {{control-ids}}
```

## Lições para reuso

A lição central de cada aposentadoria — o sinal de que uma tese está cansando — vira uma linha no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), categoria `big-idea` ou `copy`. Sinais recorrentes (ex.: queda de conversão após N meses no mesmo ângulo) sobem a default via `promoted_to`, virando gatilho de revisão de posicionamento. A tese aposentada também pode renascer: o registro guarda o avatar e o mercado em que ela funcionou, caso um novo contexto a reabilite.

## Liga com

- [`big-idea-registry`](../../data/registries/big-idea-registry.md) — onde a tese viva está catalogada.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — destino da lição.
- [`decision-registry`](../../data/registries/decision-registry.md) — a decisão que aposentou.
- [`README.md`](README.md) — visão da pasta.

---

> **Exemplo ilustrativo (apagar):** Big Idea aposentada `metodo-x-exemplo` v3.0 — ângulo "o atalho de 90 dias", aposentada 2025-05-20, substituída por `metodo-x-anti-atalho-exemplo`. Por que foi retirada: o ângulo de atalho saturou após o mercado virar estágio 4 e ver a mesma promessa em todo concorrente. Trajetória: conversão de pico 4.1% caiu para 1.9% em quatro meses. O que a substitui: a tese "anti-atalho" (o método lento que dura), que reposiciona contra a fadiga de promessas mágicas. Lição: trocar de tese quando a conversão cai abaixo de metade do pico por dois ciclos.
