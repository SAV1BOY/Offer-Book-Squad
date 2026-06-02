---
id: archive.losing-controls.losing-control-autopsy-template
title: "Template — Autópsia de Control Perdedor"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
registries: [data.registry.control-registry, data.registry.lessons-learned-registry, data.registry.swipe-registry]
tags: [template, autopsy, losing-controls, control, ab-test, memory]
---

# Template — Autópsia de Control Perdedor

## Propósito

Este template padroniza a **autópsia de cada control que perdeu** em teste. Ele força o squad a tratar o perdedor como dado, não como lixo. O `knowledge-librarian` preenche um por control batido. A estrutura é fixa e segue quatro passos: **hipótese → o que falhou → evidência → lição**. O resultado responde a uma pergunta dura: qual aposta o mercado rejeitou, e por quê.

Uma boa autópsia é honesta sobre a causa raiz. Ela nomeia a hipótese que a peça carregava, mostra a métrica que reprovou, e termina com uma lição acionável. Ela não culpa o "mercado" de forma vaga. Ela isola o ângulo, o claim ou o beat que falhou. Isto cumpre `contradiction_before_conclusion` e `evidence_before_opinion`. A autópsia alimenta dois destinos ao mesmo tempo: afia o swipe de vencedores por contraste, e vira lição no registry.

## O que arquivar

Arquive uma autópsia por control perdedor, nomeada `autopsy-<control_id>.md`. Inclua o `control_id` do perdedor, o `beat_control_id` do vencedor que o bateu, a hipótese testada, a evidência métrica e a lição. Não duplique a copy literal inteira — o control já vive no [`control-registry`](../../data/registries/control-registry.md). Arquive o esqueleto do erro: a aposta, o número e o aprendizado.

## Formato / Template

Copie o bloco abaixo. Troque cada `{{PLACEHOLDER}}`. O exemplo vive em arquivo separado, [`example-autopsy.md`](example-autopsy.md), e é **ilustrativo**.

```md
# Autópsia — {{NOME_DA_PEÇA}}

- **control_id:** {{control-id-kebab}}
- **asset_type:** {{vsl | webinar | email | sms | ad | sales-page | mailer | insert}}
- **Perdeu para:** {{beat_control_id}}
- **Métrica:** {{conversion-rate | ctr | epc | ...}} — {{valor perdedor}} vs {{valor vencedor}}
- **Lançamento:** {{launch_id}}

## Hipótese
{{A aposta que a peça carregava: ângulo, claim ou promessa. Uma frase clara.}}

## O que falhou
{{O beat, o claim ou o ângulo exato que não pegou. Concreto, não vago.}}

## Evidência
| Sinal | Métrica perdedor | Métrica vencedor | Delta |
|---|---|---|---|
| {{conversão}} | {{x%}} | {{y%}} | {{-z%}} |

## Lição
{{O que isto ensina para a próxima peça. Vira linha em lessons-learned-registry.}}

## Links
- vencedor: {{beat_control_id}} · lição: {{lesson-id}} · swipe: {{swipe-id}}
```

## Lições para reuso

A autópsia tem dois destinos. Primeiro, a lição vira uma linha no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), categoria `copy`, com `action` e `impact`. Segundo, o contraste perdedor-vencedor alimenta o [`swipe-registry`](../../data/registries/swipe-registry.md): saber por que um ângulo perdeu afia o padrão do que ganha. Um modo de falha recorrente sobe a default ou a um item de checklist via `promoted_to`. A autópsia é a prova; o registry é o índice.

## Liga com

- [`control-registry`](../../data/registries/control-registry.md) — onde o perdedor e o vencedor estão catalogados.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — destino da lição.
- [`swipe-registry`](../../data/registries/swipe-registry.md) — o swipe de vencedores que a autópsia afia.
- [`example-autopsy.md`](example-autopsy.md) — um caso preenchido (ilustrativo).
- [`README.md`](README.md) — visão da pasta.
