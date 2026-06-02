---
id: archive.losing-controls.example-autopsy
title: "Exemplo Ilustrativo — Autópsia de Control Perdedor"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
registries: [data.registry.control-registry, data.registry.lessons-learned-registry, data.registry.swipe-registry]
tags: [example, illustrative, autopsy, losing-controls, control, memory]
---

# Exemplo Ilustrativo — Autópsia de Control Perdedor

> **AVISO:** Este arquivo é um **exemplo ilustrativo**. Os dados são fictícios e servem só para mostrar como uma autópsia preenchida fica. Não é um registro real. Ao documentar um control de verdade, copie o bloco do [`losing-control-autopsy-template.md`](losing-control-autopsy-template.md) e salve como `autopsy-<control_id>.md`.

## Propósito

Esta página existe para mostrar, com um caso concreto, como o template de autópsia vira um documento útil. Ela segue a mesma estrutura fixa — **hipótese → o que falhou → evidência → lição** — e demonstra o nível de detalhe esperado: número, causa raiz e ação. Quem nunca preencheu uma autópsia lê este exemplo primeiro, vê o padrão, e replica. O exemplo prova que uma boa autópsia não acusa o "mercado" de forma vaga. Ela isola o beat exato que falhou e termina com uma lição que a próxima peça pode usar. Isto cumpre `contradiction_before_conclusion`: o squad estuda o perdedor para entender o vencedor por contraste.

## O que arquivar

Num caso real, você arquivaria o `control_id` do perdedor, o vencedor que o bateu, a hipótese, a evidência métrica e a lição. Aqui, todos os ids têm sufixo `exemplo` para deixar claro que nada disto é real. A copy literal não entra — só o esqueleto do erro.

## Formato / Template

O bloco abaixo é o template já preenchido com dados fictícios.

```md
# Autópsia — VSL Método X v2 (amostra)

- **control_id:** ctrl-exemplo-vsl-00
- **asset_type:** vsl
- **Perdeu para:** ctrl-exemplo-vsl-01
- **Métrica:** conversion-rate — 2.6% vs 4.1%
- **Lançamento:** metodo-x-exemplo-2025-q2

## Hipótese
Abrir a VSL com a dor financeira do avatar ("você está perdendo R$ X por mês") ia prender mais que abrir com a promessa do mecanismo.

## O que falhou
O gancho de dor afastou o avatar frio. O mercado já estava no estágio 3 de sofisticação e tinha visto dezenas de aberturas de dor. O beat de prova só aparecia no minuto 4 — tarde demais.

## Evidência
| Sinal | Métrica perdedor | Métrica vencedor | Delta |
|---|---|---|---|
| conversão | 2.6% | 4.1% | -1.5% |
| retenção até 1 min | 41% | 63% | -22% |

## Lição
Em mercado sofisticado (estágio 3+), abrir com prova do mecanismo bate abrir com dor. Trazer a prova para os primeiros 60 segundos.

## Links
- vencedor: ctrl-exemplo-vsl-01 · lição: ll-exemplo-2025q2-vsl-abertura · swipe: swipe-exemplo-vsl-prova-cedo
```

## Lições para reuso

Neste exemplo, a lição "abrir com prova bate abrir com dor em mercado sofisticado" iria para o [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) na categoria `copy`, com `impact: high`. O contraste perdedor-vencedor também afiaria o [`swipe-registry`](../../data/registries/swipe-registry.md): o padrão "prova nos primeiros 60s" sobe a swipe via `promoted_to`. Assim a derrota de uma peça vira munição para a próxima.

## Liga com

- [`losing-control-autopsy-template.md`](losing-control-autopsy-template.md) — o template que este exemplo demonstra.
- [`control-registry`](../../data/registries/control-registry.md) — onde o perdedor e o vencedor viveriam.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — destino da lição.
- [`swipe-registry`](../../data/registries/swipe-registry.md) — o swipe que a autópsia afia.
- [`README.md`](README.md) — visão da pasta.
