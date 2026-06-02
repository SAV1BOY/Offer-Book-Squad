---
id: archive.past-launches.launch-postmortem-template
title: "Template — Postmortem de Lançamento"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
registries: [data.registry.lessons-learned-registry, data.registry.control-registry, data.registry.decision-registry]
tags: [template, postmortem, past-launches, retrospective, memory]
---

# Template — Postmortem de Lançamento

## Propósito

Este template padroniza a **retrospectiva de cada lançamento encerrado**. Ele força o squad a passar do "como foi" para o "o que muda na próxima vez". O `knowledge-librarian` preenche um por promoção, ganhou ou perdeu. O resultado é um caso auditável: número, causa raiz e ação. Sem isto, o time repete erros já pagos e perde o que venceu.

Um bom postmortem é curto e honesto. Ele aponta a causa raiz, não o sintoma. Ele cita o control e a decisão. Ele termina com ações que viram linha no registry. Isto cumpre `memory_before_repetition` e `evidence_before_opinion`.

## O que arquivar

Arquive um postmortem por lançamento, nomeado `postmortem-<launch_id>.md`. Inclua datas, resultado financeiro, a Big Idea, os controls e as lições. Não inclua copy bruta — só o aprendizado e os links para os registries.

## Formato / Template

Copie o bloco abaixo. Troque cada `{{PLACEHOLDER}}`. O exemplo ao final é **ilustrativo** — apague antes de salvar o postmortem real.

```md
# Postmortem — {{NOME_DO_LANCAMENTO}}

- **launch_id:** {{launch-id-kebab}}
- **Janela:** {{DATA_INICIO}} → {{DATA_FIM}}
- **Project type:** {{full-launch | single-promo | offer-ladder | ...}}
- **Big Idea:** {{big-idea-id}}
- **Resultado:** {{R$ receita}} · {{ROAS}} · {{conversão}}

## Contexto
{{Mercado, sofisticação, avatar e oferta em 3-4 frases.}}

## Números
| KPI | Meta | Real | Veredito |
|---|---|---|---|
| {{conversão}} | {{x%}} | {{y%}} | {{bate / fica abaixo}} |

## O que funcionou
- {{Fato + número + por quê.}}

## O que falhou
- {{Fato + número + por quê.}}

## Causa raiz
{{A causa, não o sintoma. Uma frase por falha.}}

## Ações para a próxima vez
1. {{Ação acionável.}} → vira linha em lessons-learned-registry (impact: {{high}}).

## Links
- control: {{control-id}} · decisão: {{decision-id}} · lição: {{lesson-id}}
```

## Lições para reuso

Cada item de "Ações para a próxima vez" vira uma linha no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), com `action`, `impact` e `source_ref`. Lições que viram padrão sobem para swipe ou framework via `promoted_to`. O postmortem é a prova; o registry é o índice.

## Liga com

- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — destino de cada ação.
- [`control-registry`](../../data/registries/control-registry.md) — os controls do lançamento.
- [`decision-registry`](../../data/registries/decision-registry.md) — a decisão que o originou.
- [`README.md`](README.md) — visão da pasta.

---

> **Exemplo ilustrativo (apagar):** Postmortem `metodo-x-2025-q2` — janela 2025-04-01 a 2025-04-30, Big Idea `metodo-x-exemplo`, ROAS 3.1. Funcionou: e-mail de fechamento à noite (conversão 4.1%). Falhou: upsell caro demais para avatar frio. Causa raiz: oferta de continuidade sem ponte de valor. Ação: testar downsell antes do upsell premium.
