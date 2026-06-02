---
id: checklist.architect.pipeline-design-gate
title: "Gate — Pipeline do Caso é um DAG Válido e Completo"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
frameworks: [power-of-one, awareness-x-sophistication, starving-crowd]
registries: [decision-registry, offer-registry]
tags: [gate, architect, pipeline, dag, d0, caminho-critico, handoff]
---

# Gate — Pipeline do Caso é um DAG Válido e Completo

## Propósito
Este gate prova que o **pipeline do caso** desenhado pelo `offer-squad-architect` é um grafo de execução **acíclico, completo e roteável** — não um esboço solto. Ele existe porque um pipeline com ciclo, com nó sem dono ou com uma fase começando sem o input contratado já nasce condenado ao retravamento e ao retrabalho. O gate materializa o mandato do arquiteto: nenhuma fase começa sem seu input estar contratado e o trabalho flui na ordem correta do pipeline (Mercado→Avatar→…→Blackbook). Ele audita o desenho **antes** de o `offerbook-chief` liberar D1, garantindo que toda task do composite do project type está presente, que cada nó aponta para um agente real do `config.yaml: routing`, e que o caminho crítico cabe no prazo do escopo. Diferente do gate de sequenciamento de camadas (que foca na ordem D0→D7) e do de resolução de dependências (que foca nas arestas), este audita o **grafo inteiro** como objeto entregável: existe um DAG, ele converge para UMA tese, e está pronto para acionamento.

## Dono & Escopo
- **owner_agent:** `offer-squad-architect` (engenheiro de processo do war-room, sem poder de veto — sinaliza ao chief).
- **Artefato inspecionado:** o **`case-pipeline`** (DAG + paralelismo + caminho crítico) anexado à decisão de pipeline no [`decision-registry`](../../data/registries/decision-registry.md), e as ofertas-semente reordenadas no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
Existe UM grafo acíclico com toda task do composite presente, cada nó com dono real, cada aresta com contrato, e o caminho crítico cabendo no prazo do escopo.

## Itens
1. **Todas as tasks do composite presentes.** Verificar: o DAG contém cada task do composite do project type (`run-offer-book`, `run-full-launch`, etc.) sem faltar nenhuma; os ids batem com `config.yaml: routing`.
2. **Grafo acíclico (é um DAG).** Verificar: não há dependência circular (nenhum nó depende, direta ou transitivamente, de si mesmo); uma ordenação topológica existe.
3. **Cada nó tem dono real.** Verificar: todo nó aponta para um agente declarado em `config.yaml: agents` — nenhum nó órfão sem responsável.
4. **Cada input satisfeito.** Verificar: toda task tem suas entradas supridas por uma aresta de upstream ou pelo estado inicial declarado — nenhum input pendente.
5. **Pipeline converge para UMA tese.** Verificar: aplicado [`power-of-one`](../../frameworks/power-of-one.md), as trilhas não bifurcam em dois avatares ou duas promessas.
6. **Caminho crítico nomeado e dentro do prazo.** Verificar: a cadeia mais longa está marcada com duração estimada e cabe na restrição de tempo do escopo (ou o risco de prazo foi sinalizado ao chief).
7. **Decisão de topologia registrada.** Verificar: a topologia escolhida e as podadas (com motivo) estão no [`decision-registry`](../../data/registries/decision-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar o registro de pipeline anexado à decisão no [`decision-registry`](../../data/registries/decision-registry.md) (campos `PIPELINE-ID`, `DAG`, `PARALELO`, `CAMINHO-CRÍTICO`, `GATES`, `HARD-STOP`), a lista de nós com seus agentes-donos cruzada contra `config.yaml: routing`, e a linha de topologia escolhida vs alternativas podadas. A ordenação topológica (prova de aciclicidade) e o caminho crítico com duração são a evidência-resumo de que o grafo é válido e cabe no prazo.

## Protocolo de Falha
Item vermelho → o `offer-squad-architect` **re-topologiza** (não remenda): gera o grafo de novo a partir da dependência violada. Ciclo detectado → quebra a aresta "falsa" (ordena por quem produz o dado bruto) e refaz. Task faltante → adiciona o nó e suas arestas. Nó sem dono → mapeia ao agente correto do `config.yaml`. Caminho crítico estoura o prazo → **sinaliza** ao [`offerbook-chief`](../../agents/offerbook-chief.md) (o arquiteto não tem veto) com a alternativa de topologia recomendada; a decisão de prosseguir é do chief. Escopo elástico herdado (bifurca em dois avatares) → não desenha; devolve ao chief com a ambiguidade nomeada. Re-entrada: corrigido o grafo, o gate é re-submetido. Conflito de prioridade entre topologias → escalona ao chief pelo [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md).

## Links
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`starving-crowd`](../../frameworks/starving-crowd.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`offer-squad-architect`](../../agents/offer-squad-architect.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`layer-sequencing-gate`](layer-sequencing-gate.md) · [`dependency-resolution-gate`](dependency-resolution-gate.md) · [`handoff-contract-gate`](handoff-contract-gate.md) · [`scope-alignment-gate`](scope-alignment-gate.md)
- Gate de entrada (montante): [`chief-scope-approval-gate`](../chief/chief-scope-approval-gate.md) · [`chief-project-type-gate`](../chief/chief-project-type-gate.md)
- HARD STOP: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
