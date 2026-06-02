---
id: checklist.architect.handoff-contract-gate
title: "Gate — Todo Handoff Tem Contrato Completo e o Downstream Não Recebe Pela Metade"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
frameworks: [power-of-one, awareness-x-sophistication]
registries: [decision-registry]
tags: [gate, architect, handoff, contrato, d0, integridade, downstream]
---

# Gate — Todo Handoff Tem Contrato Completo e o Downstream Não Recebe Pela Metade

## Propósito
Este gate prova que **cada aresta** do pipeline carrega um **contrato de handoff escrito** — campos de entrada nomeados, qualidade mínima declarada e dono identificado — para que o agente downstream nunca confie num artefato pela metade. Ele existe porque a integridade do handoff é a segunda coisa que o `offer-squad-architect` protege: um handoff sem contrato é onde a informação se perde, onde a prova vira órfã e onde o retrabalho nasce. O gate garante que o downstream sabe exatamente o que vai receber, com que qualidade, e o que o próximo nó espera dele. Ele formaliza arestas críticas como **avatar→proof** (a curadoria de prova só começa com o mapa de objeções entregue) e **market→todos** (o diagnóstico de sofisticação/consciência precede e calibra avatar e prova). Sem este gate, o pipeline pode ser um DAG válido na forma e ainda assim quebrar na execução, porque uma fase começa lendo um input incompleto. É o gate que transforma "a ordem está certa" em "cada passagem de bastão é confiável".

## Dono & Escopo
- **owner_agent:** `offer-squad-architect` (define o contrato de cada handoff; não executa as fases).
- **Artefato inspecionado:** os **`handoff-contracts`** de cada aresta do `case-pipeline`, registrados junto à decisão de pipeline no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
Cada aresta do DAG tem um contrato escrito com campos de entrada, qualidade mínima e dono, e as arestas críticas (avatar→proof, market→todos) estão formalizadas.

## Itens
1. **Toda aresta tem contrato.** Verificar: nenhuma dependência do DAG existe sem um contrato de handoff escrito (campos + qualidade + dono).
2. **Contrato de entrada por nó.** Verificar: cada agente downstream recebe a lista de campos que o input já tem e a qualidade mínima de cada campo.
3. **Contrato de saída por nó.** Verificar: cada nó declara o que o próximo espera dele (ex.: o avatar garante ao proof um mapa de objeções com ≥N objeções categorizadas).
4. **Peso esperado declarado.** Verificar: cada handoff marca "construção completa" vs "revalidação leve", para o downstream calibrar o esforço.
5. **Aresta avatar→proof formalizada.** Verificar: a dependência está marcada como obrigatória — proof só começa após o [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md) verde.
6. **Aresta market→todos formalizada.** Verificar: o diagnóstico de sofisticação/consciência precede e calibra avatar e prova, com os campos `sophistication 1-5` e `awareness 1-5` no contrato.
7. **Contratos registrados.** Verificar: os contratos estão anexados à decisão de pipeline no [`decision-registry`](../../data/registries/decision-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar a seção `CONTRATOS DE HANDOFF` do registro de pipeline no [`decision-registry`](../../data/registries/decision-registry.md), com cada aresta listando seus campos, qualidade mínima, dono e peso esperado. As arestas `market → avatar/proof` (entrega `{sophistication, awareness, mercado-alvo, starving-crowd verdict}`) e `avatar → proof` (entrega `{objection map ≥N, segmentos, verbatims}`) precisam aparecer explicitamente, com o gate de objeção referenciado como gatilho.

## Protocolo de Falha
Item vermelho → o `offer-squad-architect` completa o contrato faltante antes de entregar o pipeline ao chief. Aresta sem contrato → escreve os campos, a qualidade mínima e o dono. Handoff vazio na execução (input chega sem os campos do contrato) → marca o nó de origem como "incompleto", avisa o dono upstream e **segura o downstream** até o contrato ficar verde. Prova órfã por paralelismo cego (proof rodou antes do objection-map) → re-sequencia: a aresta avatar→proof passa a depender do [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md). O arquiteto **não tem veto**: se a falha vem de um artefato de outro agente, sinaliza ao [`offerbook-chief`](../../agents/offerbook-chief.md) e registra. Re-entrada: completados os contratos, o gate é re-submetido.

## Links
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`offer-squad-architect`](../../agents/offer-squad-architect.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md)
- Gate de dependência (aresta avatar→proof): [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md)
- Gates irmãos: [`pipeline-design-gate`](pipeline-design-gate.md) · [`dependency-resolution-gate`](dependency-resolution-gate.md) · [`layer-sequencing-gate`](layer-sequencing-gate.md)
