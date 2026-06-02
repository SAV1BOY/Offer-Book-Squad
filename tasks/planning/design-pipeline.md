---
id: task.planning.design-pipeline
title: "Design Pipeline — Desenhar o Grafo de Execução do Caso, Posicionar os Gates e Contratar os Handoffs"
type: task
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
consumes:
  - decision.project-type
  - decision.scope-one-sentence
  - artifact.offer-book-master-skeleton
  - template.core.offer-book-master
produces:
  - artifact.case-pipeline
  - artifact.handoff-contracts
  - artifact.market-brief-routing
frameworks: [power-of-one, awareness-x-sophistication, starving-crowd]
checklists:
  - chief/chief-project-type-gate
  - chief/chief-scope-approval-gate
  - market/market-sophistication-gate
  - market/market-awareness-gate
  - market/market-starving-crowd-gate
registries: [decision-registry, offer-registry]
tags: [planning, pipeline, dag, handoff, contratos, hard-stop, command, d0]
---

# Design Pipeline — desenhar o grafo de execução do caso, posicionar os gates e contratar os handoffs

## Objetivo
Transformar o project type e a frase de escopo travados em UM grafo acíclico de execução — cada nó com dono, cada aresta com contrato de handoff, todos os gates posicionados e o HARD STOP intransponível — pronto para o chief liberar a camada D1.

## Agente dono
[`offer-squad-architect`](../../agents/offer-squad-architect.md). É o engenheiro de processo do war-room. Não pesquisa mercado, não desenha oferta, não escreve copy; desenha **a planta** por onde tudo passa. Sem poder de veto — sinaliza riscos ao chief.

## Gatilho / Quando
Roda em D0, logo após [`intake-and-scope`](intake-and-scope.md) fechar com os dois gates de comando verdes. Ativa quando: (a) o chief trava o project type + a frase de escopo e passa o caso; (b) o project type muda no meio do caminho e o pipeline precisa ser redesenhado; (c) chega um handoff do `deepresearch_squad` que precisa ser roteado para as trilhas de D1. **Pré-condição:** [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) verdes. Sem project type não há composite a ordenar; sem escopo travado não sei quais trilhas são necessárias.

## Inputs (Consome)
- **`decision.project-type`** — um dos 7 tipos. Define o **composite** do `config.yaml` (`run-offer-book`, `run-full-launch`, `run-single-promo`, `run-enterprise-deal-book`) e, portanto, o conjunto de tasks a ordenar.
- **`decision.scope-one-sentence`** — avatar-alvo, transformação, entregável, prazo. Daqui derivo quais trilhas de D1 são críticas (ex.: B2B com comitê → trilha DMU reforçada).
- **`artifact.offer-book-master-skeleton`** + **[`template.core.offer-book-master`](../../templates/core/offer-book-master.md)** — o mapa-mestre de pré-requisitos: a checklist de "o que precisa existir" que eu converto em "em que ordem produzir".
- **Registries lidos:** [`decision-registry`](../../data/registries/decision-registry.md) (decisões do intake) e [`offer-registry`](../../data/registries/offer-registry.md) (existe oferta com `status: active/control`? define se as trilhas D1 são construção ou revalidação leve).

## Procedimento
1. **Mapeie o estado inicial.** Leia o `offer-registry`: a oferta já foi validada? Há prova? Houve pesquisa prévia? Oferta nova → trilhas D1 completas; oferta provada → revalidação leve. Registre o estado.
2. **Selecione as tasks do composite.** A partir do project type, puxe o composite do `config.yaml: routing` (ex.: `full-launch` → `run-full-launch`). Confirme que os ids das tasks batem com o config — id que não bate **falha** no qa-runner.
3. **Monte o DAG.** Para cada task, identifique de quem ela depende. A regra-mãe: `run-market-intel` primeiro (produz sofisticação + consciência + veredito starving-crowd); `build-avatar-voc` depende do market-brief; `curate-proof` depende do **mapa de objeções** do avatar (aresta real `avatar/avatar-objection-map-gate`). Marque o que pode rodar em **paralelo seguro** (só o que não depende um do outro).
4. **Posicione os gates nas junções.** Encaixe os gates obrigatórios de cada transição (os de `market/*`, `avatar/*`, etc.). Posicione o **★ HARD STOP** [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) entre D3 e D4, espelhando `config.yaml: hard_stop`. Nenhuma aresta de entrada de copy pode contornar esse nó.
5. **Gere ≥3 topologias candidatas (Tree-of-Thoughts).** Ex.: (A) série pura, (B) paralelo agressivo, (C) paralelo faseado. Pontue cada uma por *integridade de dependência* (×3), *prazo/caminho crítico* (×2), *risco de retrabalho* (×2), *carga de coordenação* (×1). Pode as duas piores. Topologia que produz prova órfã (proof antes do objection-map) é reprovada na trave.
6. **Nomeie o caminho crítico** — a cadeia mais longa que define o prazo — e confronte com a restrição de tempo do escopo. Não cabe no prazo → sinalize ao chief antes de entregar.
7. **Escreva o contrato de cada handoff.** Para cada aresta: campos entregues + qualidade mínima + dono. Formalize a aresta `avatar→proof` (proof só começa com o objection-map entregue) e `market→todos` (o diagnóstico precede e calibra avatar e prova). Roteie o handoff de pesquisa (`market-brief-routing`) para a trilha de mercado.
8. **Valide a aciclicidade e o HARD STOP.** Confirme: nenhum ciclo; todo nó com input satisfeito; nenhum caminho entra em D4 sem cruzar o `offer-book-dod-gate`.
9. **Sinalize riscos e registre.** Sem veto, sinalize ao chief: dependência impossível (full-launch sem oferta validada), prazo inviável, risco de furo no HARD STOP, escopo que bifurcou. Logue a topologia escolhida e as podadas no `decision-registry`.

## Frameworks
- [`power-of-one`](../../frameworks/power-of-one.md) — garante que as trilhas convergem para UM avatar/UMA tese (não bifurcam).
- [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) — dimensiona a profundidade das trilhas (sofisticação 4-5 → mais gates em mecanismo/prova a jusante).
- [`starving-crowd`](../../frameworks/starving-crowd.md) — decide se o topo do pipeline ganha um gate de viabilidade vai/não-vai.

## Outputs (Produz)
- **`artifact.case-pipeline`** — o DAG: nós (tasks com dono), arestas (dependências), grupos paralelos, caminho crítico, gates nas junções, HARD STOP.
- **`artifact.handoff-contracts`** — o contrato de cada aresta (campos + qualidade mínima + peso esperado: construção vs revalidação).
- **`artifact.market-brief-routing`** — o roteamento do handoff de pesquisa para a trilha D1.
- **Registries escritos:** [`decision-registry`](../../data/registries/decision-registry.md) com a decisão de topologia (`{decision_id, fase: "pipeline-design", opção_escolhida, alternativas_podadas, motivo, caminho_crítico, gates_posicionados, data}`); [`offer-registry`](../../data/registries/offer-registry.md) quando o desenho cria/reordena uma oferta-semente.

## Definition of Done
Existe UM grafo acíclico; cada nó tem dono (agente do `config.yaml: routing`); cada aresta tem um contrato de handoff escrito; todos os gates obrigatórios estão posicionados; o HARD STOP é intransponível; o caminho crítico está nomeado e cabe no prazo; a decisão de topologia (com as podadas) está no registry. Máximo de 3 ciclos H↔L antes de escalar ao chief.

## Gates
- [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) (já verdes a montante; pré-condição de entrada).
- Gates que o pipeline **posiciona** (não executa): [`market/market-sophistication-gate`](../../checklists/market/market-sophistication-gate.md) · [`market/market-awareness-gate`](../../checklists/market/market-awareness-gate.md) · [`market/market-starving-crowd-gate`](../../checklists/market/market-starving-crowd-gate.md).

## Handoff
**Próxima task:** [`run-market-intel`](../intelligence/run-market-intel.md) — dono [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md). **Contrato:** cada agente de D1 recebe (i) sua posição no DAG, (ii) seu contrato de entrada, (iii) seu contrato de saída (ex.: o avatar garante ao proof um mapa de objeções com ≥N objeções categorizadas), (iv) os gates que precisa passar e (v) o peso esperado (construção completa vs revalidação leve). Garantia: nenhum downstream começa uma fase sem o input contratado — entradas nomeadas, qualidade mínima declarada, dono identificado. Se o escopo herdado ainda bifurca, esta task não fecha e devolve ao [`offerbook-chief`](../../agents/offerbook-chief.md).
