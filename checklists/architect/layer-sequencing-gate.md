---
id: checklist.architect.layer-sequencing-gate
title: "Gate — Camadas na Ordem Certa e o HARD STOP Intransponível"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
frameworks: [power-of-one, awareness-x-sophistication, starving-crowd]
registries: [decision-registry]
tags: [gate, architect, sequencing, camadas, hard-stop, d0, ordem]
---

# Gate — Camadas na Ordem Certa e o HARD STOP Intransponível

## Propósito
Este gate prova que o pipeline do caso respeita a **ordem das camadas** do squad (D0→D1→…→D7) e que o **HARD STOP** entre D3 e D4 é intransponível. Ele existe porque a ordem correta é a primeira coisa que o `offer-squad-architect` protege: o pipeline Mercado→Avatar→Mecanismo→Valor→Money Model→Big Idea→Posição→[OFFER BOOK]→Copy não pode ter uma camada posterior consumindo o que uma anterior ainda não produziu. Sem este gate, uma task de copy (D4) poderia nascer antes do Offer Book passar no DoD, violando `config.yaml: defaults.hard_stop_before_copy: true` e o princípio `offer_before_persuasion`. Diferente do `pipeline-design-gate` (que audita o grafo inteiro) e do `dependency-resolution-gate` (que audita cada aresta), este foca só na **monotonicidade das camadas**: nenhum nó de camada N lê um artefato de camada N+1, e o nó do Offer Book DoD está no caminho de toda task D4+. É o gate que garante que a estratégia precede a persuasão, sempre, sem exceção nem para promoções rápidas.

## Dono & Escopo
- **owner_agent:** `offer-squad-architect` (posiciona os gates nas junções; não executa as fases nem detém veto).
- **Artefato inspecionado:** a ordenação por camada do **`case-pipeline`** e a posição do HARD STOP, anexados à decisão de pipeline no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
As camadas estão em ordem monotônica (D0→D7), nenhum nó consome um artefato de camada posterior, e o HARD STOP (offer-book-dod-gate) está no caminho de toda task D4+.

## Itens
1. **Ordem das camadas respeitada.** Verificar: cada nó tem a `layer` do agente dono (`config.yaml: agents`) e nenhuma aresta vai de uma camada maior para uma menor (sem fluxo retrógrado).
2. **Nenhum consumo antecipado.** Verificar: nenhum nó de camada N lê um artefato produzido em camada N+1 ou superior — todo input vem de igual ou anterior.
3. **HARD STOP entre D3 e D4.** Verificar: o nó [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) está posicionado na transição D3→D4, espelhando `config.yaml: hard_stop`.
4. **Nenhum caminho contorna o HARD STOP.** Verificar: toda task de D4+ (copy, funil, ops) tem o HARD STOP como ancestral obrigatório no grafo — nenhuma aresta de entrada o pula.
5. **Intelligence antes de arquitetura.** Verificar: as tasks de D1 (mercado, avatar, prova) precedem as de D2 (mecanismo, valor, money model, preço, unit economics).
6. **Big Idea/Posição antes do Offer Book.** Verificar: D3 (big idea + positioning) está concluído antes do nó de montagem do Offer Book.
7. **Regra sem exceção registrada.** Verificar: mesmo em `single-promo`, o HARD STOP aparece; qualquer pedido de exceção foi sinalizado ao chief e está no [`decision-registry`](../../data/registries/decision-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar a ordenação por camada do `case-pipeline` no [`decision-registry`](../../data/registries/decision-registry.md), com cada nó rotulado pela `layer` do agente dono e a posição do `offer-book-dod-gate` marcada como `★ HARD STOP`. A prova de que nenhum caminho D4+ contorna o HARD STOP (a lista de ancestrais de cada task de copy/funil/ops) é a evidência-resumo. Pedidos de exceção (negados) ficam na decisão.

## Protocolo de Falha
Item vermelho → o `offer-squad-architect` **reposiciona** o gate ou **re-topologiza** a camada violada (não remenda). Fluxo retrógrado (camada maior alimentando menor) → inverte a dependência ou identifica a aresta falsa. Caminho que fura o HARD STOP → reposiciona o `offer-book-dod-gate` como nó obrigatório no caminho de toda task D4+ e revalida que nenhuma aresta o contorna. Pedido de pular o HARD STOP numa promoção → **recusa o desenho** com a regra sem exceção e **sinaliza** ao [`offerbook-chief`](../../agents/offerbook-chief.md) (o arquiteto não tem veto; o chief decide e registra). Re-entrada: corrigida a ordem, o gate é re-submetido. Conflito sobre a necessidade do HARD STOP → escalona pelo [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md).

## Links
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`starving-crowd`](../../frameworks/starving-crowd.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`offer-squad-architect`](../../agents/offer-squad-architect.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- HARD STOP: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
- Gates irmãos: [`pipeline-design-gate`](pipeline-design-gate.md) · [`handoff-contract-gate`](handoff-contract-gate.md) · [`dependency-resolution-gate`](dependency-resolution-gate.md) · [`scope-alignment-gate`](scope-alignment-gate.md)
- Conflito: [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md)
