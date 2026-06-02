---
id: checklist.big-idea.big-idea-single-gate
title: "Gate — UMA Big Idea (Power of One, gate de veto)"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [power-of-one, big-idea-generator, big-idea-architect/big-idea-scoring]
registries: [big-idea-registry, decision-registry]
tags: [gate, big-idea, power-of-one, veto, uma-tese, d3]
---

# Gate — UMA Big Idea

## Propósito
Este é o **gate de veto** do [`big-idea-architect`](../../agents/big-idea-architect.md): ele prova que o lançamento trava **uma, e apenas uma, Big Idea**. Ele protege o princípio `one_big_idea` (Power of One): duas teses dividem a atenção do mercado e nenhuma vence. Conforme o ARCHITECTURE, "Big Idea Architect entrega UMA tese — múltiplas ideias = reprovação". O agente é divergente por dentro (gera de 3 a 5 candidatas via Tree-of-Thoughts) e brutal por fora (poda até sobrar uma); este gate fiscaliza o resultado da poda. Ele não julga a qualidade dos cinco critérios (isso é da [`big-idea-new-big-credible-gate`](big-idea-new-big-credible-gate.md)) nem o fit de consciência (da [`big-idea-awareness-fit-gate`](big-idea-awareness-fit-gate.md)) — ele cobra **a unicidade**. As candidatas podadas não somem: viram `pruned` no registry e matéria-prima de ângulos de ad, nunca teses concorrentes carregando o mesmo lançamento.

## Dono & Escopo
- **owner_agent:** `big-idea-architect` (**tem poder de veto**: múltiplas ideias travadas é reprovação imediata; o teste A/B de ângulos é trabalho do [`ad-creative-factory`](../../agents/ad-creative-factory.md) sobre UMA tese, não de duas teses concorrentes).
- **Artefato inspecionado:** o [`big-idea-registry`](../../data/registries/big-idea-registry.md) — exige exatamente um registro `locked` por lançamento e as demais candidatas como `pruned` com motivo —, e a decisão de trava no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
Existe exatamente uma Big Idea com status `locked` para o lançamento, e todas as outras candidatas estão marcadas `pruned` com o motivo da poda.

## Itens
1. **Exatamente uma `locked`.** Verificar: o `big-idea-registry` tem **um** registro com `status: locked` para este lançamento — dois ou mais reprova de imediato.
2. **Candidatas podadas registradas.** Verificar: as outras candidatas (de 3 a 5 geradas) constam como `pruned`, cada uma com `motivo_poda`.
3. **A vencedora é defensável, não a primeira.** Verificar: a `locked` venceu por soma de critérios na matriz de [`big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md), não por ter aparecido primeiro.
4. **Promessa única.** Verificar: a `locked` tem uma promessa, um gancho e um vilão — não um amálgama de duas ideias disfarçado de uma.
5. **Sem teses concorrentes "para testar".** Verificar: não há segunda tese travada sob pretexto de A/B; ângulos de teste são variações sobre a UMA, geradas a jusante.
6. **Decisão de trava registrada.** Verificar: a trava está no `decision-registry` com data e referência à matriz de pontuação.
7. **Override só pelo chief.** Verificar: qualquer exceção (caso raro) tem decisão explícita do [`offerbook-chief`](../../agents/offerbook-chief.md) gravada — sem registro, o veto vale.

## Evidência Exigida
Para marcar ✅: linkar o `big-idea-registry` mostrando o único `locked` e as `pruned` com motivo (itens 1–2), a matriz de pontuação que justifica a vencedora (itens 3–4), a confirmação de ausência de segunda tese travada (item 5) e a entrada no `decision-registry` (itens 6–7).

## Protocolo de Falha
Item vermelho → **veto**: o `big-idea-architect` reprova e devolve. Se há duas teses travadas, escolhe pela rubrica e marca a perdedora como `pruned`; se a melhor soma ainda é fraca (todas medianas), re-ideia (mínimo de 3 ramos no ToT) antes de travar — não trava a "menos pior". Re-entrada: atualiza o `big-idea-registry` para um único `locked` e re-submete. Override apenas pelo [`offerbook-chief`](../../agents/offerbook-chief.md), com decisão no `decision-registry`. Máximo de 2 ciclos de re-ideação antes de escalar.

## Links
- Gates irmãos: [`big-idea-new-big-credible-gate`](big-idea-new-big-credible-gate.md) · [`big-idea-relevant-proprietary-gate`](big-idea-relevant-proprietary-gate.md) · [`big-idea-awareness-fit-gate`](big-idea-awareness-fit-gate.md) · [`big-idea-meta-angle-gate`](big-idea-meta-angle-gate.md)
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`big-idea-generator`](../../frameworks/big-idea-generator.md) · [`big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md)
- Registries: [`big-idea-registry`](../../data/registries/big-idea-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`big-idea-architect`](../../agents/big-idea-architect.md) · [`offerbook-chief`](../../agents/offerbook-chief.md) · [`ad-creative-factory`](../../agents/ad-creative-factory.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
