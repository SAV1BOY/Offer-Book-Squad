---
id: archive.losing-controls.readme
title: "Arquivo — Controls Perdedores (Autópsias)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [archive, losing-controls, autopsy, control, ab-test, memory]
---

# Arquivo — Controls Perdedores (Autópsias)

## Propósito

Esta pasta guarda a **autópsia de cada control que perdeu** em teste. Um control perdedor não é lixo — é dado. Ele mostra qual hipótese o mercado rejeitou, e por quê. Aqui o `knowledge-librarian` disseca cada VSL, e-mail, ad ou mailer que foi batido, para extrair a lição que torna a próxima peça mais forte.

A maioria dos times joga o perdedor fora e esquece. O squad faz o contrário: ele estuda o perdedor para não repetir a aposta errada e para entender o que o vencedor provou por contraste. Isto cumpre `contradiction_before_conclusion` e `memory_before_repetition`. A autópsia alimenta tanto o swipe de vencedores quanto o registry de lições.

## O que arquivar

- Uma autópsia por control perdedor (use o template).
- O `control_id` real do perdedor e o control que o bateu (`beat_control_id`).
- A hipótese que a peça testava (a aposta de copy/ângulo).
- O que falhou, com a evidência métrica.
- A lição que isto ensina para a próxima peça.

Não arquive a copy literal inteira. Arquive a hipótese, a métrica e a lição — o esqueleto do erro.

## Formato / Template

Use [`losing-control-autopsy-template.md`](losing-control-autopsy-template.md). A estrutura é fixa: **hipótese → o que falhou → evidência → lição**. Veja [`example-autopsy.md`](example-autopsy.md) para um caso preenchido (ilustrativo). Cada arquivo final nomeia o control (`autopsy-<control_id>.md`).

## Autópsias arquivadas
Cada uma diagnostica a **causa raiz via o framework violado** e deixa uma lição no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md):
- [`autopsy-cold-vsl-offer-lead.md`](autopsy-cold-vsl-offer-lead.md) — lead de Oferta em tráfego frio (viola `awareness-x-sophistication` × `lead-types`) → `ll-2026q1-lead-awareness-fit`.
- [`autopsy-false-countdown-scarcity.md`](autopsy-false-countdown-scarcity.md) — contador evergreen falso (viola `truthful_scarcity`) → `ll-2026q1-truthful-scarcity`.
- [`autopsy-orphan-bonus-stack.md`](autopsy-orphan-bonus-stack.md) — stack inchado de bônus órfãos (viola `value_equation_test`) → `ll-2026q1-no-orphan-bonus`.

## Lições para reuso

A autópsia tem dois destinos. Primeiro, a lição vira linha no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), categoria `copy`. Segundo, o contraste perdedor-vencedor alimenta o swipe de vencedores: saber por que um ângulo perdeu afia o padrão do que ganha. Um modo de falha recorrente sobe a default ou a um item de checklist via `promoted_to`.

## Liga com

- [`control-registry`](../../data/registries/control-registry.md) — onde o perdedor e o vencedor estão catalogados.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — onde a lição vira registro.
- [`swipe-registry`](../../data/registries/swipe-registry.md) — o swipe de vencedores que a autópsia afia por contraste.
- [`past-launches/`](../past-launches/README.md) — o postmortem do lançamento que rodou o control.
- [`ARCHITECTURE.md`](../../ARCHITECTURE.md) — o pipeline e a camada D4 (copy).
