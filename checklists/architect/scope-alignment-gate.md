---
id: checklist.architect.scope-alignment-gate
title: "Gate — Pipeline Fiel ao Escopo e ao Project Type (UM Avatar, UMA Promessa)"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
frameworks: [power-of-one, awareness-x-sophistication, starving-crowd]
registries: [decision-registry, offer-registry]
tags: [gate, architect, escopo, project-type, power-of-one, d0, convergencia]
---

# Gate — Pipeline Fiel ao Escopo e ao Project Type

## Propósito
Este gate prova que o pipeline desenhado é **fiel à frase de escopo travada** e ao **project type** classificado pelo `offerbook-chief` — nem mais, nem menos. Ele existe porque um pipeline construído sobre escopo elástico já nasce errado: se a frase de escopo ainda admite dois avatares ou duas promessas, as trilhas produzem material divergente e violam o princípio `one_big_idea`. O gate também impede o **over-engineering** (desenhar pesquisa completa para uma oferta já validada) e o **under-engineering** (rota fina demais para uma oferta nova num mercado sofisticado). Ele garante que o composite de tasks corresponde exatamente ao project type (`run-offer-book`, `run-full-launch`, etc.) e que o peso de cada trilha casa com o estado inicial (oferta validada? prova existente? mercado maduro?). É o gate que liga o que o chief pediu ao que o arquiteto desenhou, antes de a planta virar execução. Sem ele, o pipeline pode ser um DAG válido e ainda assim resolver o problema errado.

## Dono & Escopo
- **owner_agent:** `offer-squad-architect` (traduz escopo+project type em plano; sem veto, sinaliza ambiguidade ao chief).
- **Artefato inspecionado:** o **`case-pipeline`** contra a `decision.scope-one-sentence` e a `decision.project-type`, com a decisão de topologia no [`decision-registry`](../../data/registries/decision-registry.md) e as ofertas-semente no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O composite de tasks corresponde ao project type, o pipeline produz UM avatar e UMA promessa, e o peso das trilhas casa com o estado inicial declarado.

## Itens
1. **Composite casa com o project type.** Verificar: o conjunto de tasks do pipeline é exatamente o composite do project type travado no `config.yaml` — sem task a mais nem a menos.
2. **Escopo não bifurca.** Verificar: aplicado [`power-of-one`](../../frameworks/power-of-one.md), a frase de escopo aponta para UM avatar e UMA promessa; se admite duas leituras, o desenho foi devolvido ao chief.
3. **Peso das trilhas casa com o estado inicial.** Verificar: oferta já validada → trilhas D1 em "revalidação leve"; oferta nova → trilhas D1 completas (sem over/under-engineering).
4. **Profundidade casa com a sofisticação.** Verificar: aplicado [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md), mercado sofisticação 4–5 recebe peso extra em mecanismo/prova a jusante.
5. **Gate de viabilidade quando cabe.** Verificar: aplicado [`starving-crowd`](../../frameworks/starving-crowd.md), há (ou não há, com justificativa) um gate vai/não-vai no topo do pipeline.
6. **Entregável bate com o project type.** Verificar: o nó final produz o entregável esperado (offer book, blackbook, deal-book) do project type.
7. **Decisão de escopo registrada.** Verificar: a leitura do escopo, o peso das trilhas e as podas (over/under-engineering evitados) estão no [`decision-registry`](../../data/registries/decision-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar a `decision.project-type` e a `decision.scope-one-sentence` (gates de chief verdes a montante), o composite de tasks do pipeline cruzado contra o `config.yaml`, e a decisão de topologia no [`decision-registry`](../../data/registries/decision-registry.md) registrando o estado inicial (oferta validada? prova? sofisticação) e o peso atribuído a cada trilha. A confirmação `power-of-one` (UM avatar, UMA promessa) e o entregável final batendo com o project type são a evidência-resumo.

## Protocolo de Falha
Item vermelho → corrige antes de entregar ao chief. Escopo elástico (bifurca em dois avatares/promessas) → o arquiteto **não desenha**; devolve ao [`offerbook-chief`](../../agents/offerbook-chief.md) com a ambiguidade nomeada e duas topologias condicionais. Over-engineering (pesquisa completa para oferta validada) → rebaixa as trilhas D1 a "revalidação leve" e registra a poda. Under-engineering (rota fina para oferta nova/mercado maduro) → expande as trilhas e adiciona gates de sofisticação. Project type que contradiz a maturidade da oferta (ex.: full-launch sem oferta validada) → **sinaliza** o risco ao chief antes de desenhar (sem veto). Re-entrada: alinhado o escopo, o gate é re-submetido. Conflito sobre o project type → escalona pelo [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md).

## Links
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`starving-crowd`](../../frameworks/starving-crowd.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`offer-squad-architect`](../../agents/offer-squad-architect.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates de entrada (montante): [`chief-project-type-gate`](../chief/chief-project-type-gate.md) · [`chief-scope-approval-gate`](../chief/chief-scope-approval-gate.md)
- Gates irmãos: [`pipeline-design-gate`](pipeline-design-gate.md) · [`handoff-contract-gate`](handoff-contract-gate.md) · [`layer-sequencing-gate`](layer-sequencing-gate.md) · [`dependency-resolution-gate`](dependency-resolution-gate.md)
- Conflito: [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md)
