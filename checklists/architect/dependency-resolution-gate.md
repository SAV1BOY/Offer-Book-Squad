---
id: checklist.architect.dependency-resolution-gate
title: "Gate — Zero Dependência Circular e Paralelismo Seguro"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
frameworks: [power-of-one, awareness-x-sophistication, starving-crowd]
registries: [decision-registry]
tags: [gate, architect, dependencia, paralelismo, dag, d0, caminho-critico]
---

# Gate — Zero Dependência Circular e Paralelismo Seguro

## Propósito
Este gate prova que as **arestas** do pipeline estão resolvidas: não há dependência circular, todo input de cada nó é satisfeito por um upstream ou pelo estado inicial, e só roda em paralelo o que é de fato independente. Ele existe porque o terceiro mandato do `offer-squad-architect` é o **paralelismo seguro**: rodar junto duas tasks que dependem uma da outra produz artefato órfão e retrabalho — o caso clássico é a curadoria de prova começar antes do mapa de objeções, gerando prova solta sem a objeção que ela deveria desarmar. Diferente do `pipeline-design-gate` (grafo inteiro) e do `handoff-contract-gate` (o conteúdo do contrato), este foca na **resolução das dependências**: a ordenação topológica existe, o caminho crítico está identificado, e cada grupo paralelo é seguro. É o gate que separa "rápido e quebrado" de "rápido e correto" — o paralelismo agressivo que produz prova órfã é reprovado aqui.

## Dono & Escopo
- **owner_agent:** `offer-squad-architect` (resolve o grafo de dependências; sem veto, sinaliza ao chief).
- **Artefato inspecionado:** as **arestas e grupos paralelos** do `case-pipeline` (o DAG e o `PARALELO[...]`), com a decisão de topologia no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
Não há ciclo, todo input está satisfeito por uma aresta ou pelo estado inicial, e cada grupo paralelo contém apenas tasks mutuamente independentes.

## Itens
1. **Zero dependência circular.** Verificar: nenhum nó depende, direta ou transitivamente, de si mesmo; uma ordenação topológica do DAG existe.
2. **Todo input resolvido.** Verificar: cada task tem suas entradas supridas por uma aresta de upstream ou pelo estado inicial declarado — nenhum input pendente.
3. **Paralelismo seguro.** Verificar: cada grupo em `PARALELO[...]` contém só tasks sem aresta entre si (mutuamente independentes).
4. **Sem prova órfã por paralelismo cego.** Verificar: a curadoria de prova **não** está paralela ao avatar antes do mapa de objeções — a aresta avatar→proof é respeitada via [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md).
5. **Caminho crítico identificado.** Verificar: a cadeia mais longa de dependências está marcada (define o prazo) e nenhum nó fora dela vira gargalo escondido.
6. **Aresta falsa quebrada.** Verificar: onde houve ciclo aparente, a aresta "falsa" foi removida ordenando por quem produz o dado bruto.
7. **Resolução registrada.** Verificar: os grupos paralelos, o caminho crítico e as arestas resolvidas estão no [`decision-registry`](../../data/registries/decision-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar a ordenação topológica do DAG (prova de aciclicidade), a seção `PARALELO[...]` do registro de pipeline no [`decision-registry`](../../data/registries/decision-registry.md) com a justificativa de independência de cada grupo, e o `CAMINHO-CRÍTICO` marcado. A demonstração explícita de que a aresta avatar→proof é obrigatória (proof depende do [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md)) é a evidência-resumo de que o paralelismo não produz prova órfã.

## Protocolo de Falha
Item vermelho → o `offer-squad-architect` **re-sequencia** (não remenda). Ciclo detectado → identifica a aresta falsa (ordena por quem produz o dado bruto) e re-topologiza. Input não satisfeito → adiciona a aresta de upstream que o supre ou declara o estado inicial. Paralelismo inseguro (duas tasks dependentes no mesmo grupo) → serializa-as ou move a dependente para depois do gate da independente. Prova órfã (proof antes do objection-map) → marca a aresta avatar→proof como obrigatória e segura o proof até o [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md) verde. O arquiteto **não tem veto**: se a falha vem de um artefato de outro agente, **sinaliza** ao [`offerbook-chief`](../../agents/offerbook-chief.md). Re-entrada: resolvidas as dependências, o gate é re-submetido. Conflito de prioridade → escalona pelo [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md).

## Links
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`starving-crowd`](../../frameworks/starving-crowd.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`offer-squad-architect`](../../agents/offer-squad-architect.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md)
- Gate de dependência (avatar→proof): [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md)
- Gates irmãos: [`pipeline-design-gate`](pipeline-design-gate.md) · [`handoff-contract-gate`](handoff-contract-gate.md) · [`layer-sequencing-gate`](layer-sequencing-gate.md) · [`scope-alignment-gate`](scope-alignment-gate.md)
- Conflito: [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md)
