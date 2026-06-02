---
id: doc.failure-paths-and-gate-recovery
title: "Caminhos de Falha & Recuperação de Gates/Vetos"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [failure-paths, gates, veto, recovery, integration]
---

# Caminhos de Falha & Recuperação de Gates/Vetos

O squad é definido tanto pelo que **bloqueia** quanto pelo que produz. Este documento mostra o que acontece quando um gate fica **vermelho** ou um agente **veta** — o ponto de re-entrada e como o sistema se autocorrige (sem becos sem saída).

## Protocolo geral de gate (todo gate segue isto)
1. **Vermelho:** o gate lista o(s) item(ns) reprovado(s) com "como verificar".
2. **Devolução:** o artefato volta ao **agente dono** do bloco que falhou (não ao início).
3. **Correção + registro:** o dono corrige, atualiza o registry relevante e **re-submete** ao mesmo gate.
4. **Verde:** só então a fase avança. Nenhum estado "parcial" libera a próxima camada.

## Cenários de veto (os 6 agentes com poder de parada)

### ★ HARD STOP — `offer-book-dod-gate` vermelho (D3→D4)
- **Quem segura:** [offerbook-chief](../agents/offerbook-chief.md). **O que acontece:** **nenhuma** copy (D4+) começa. O chief identifica qual gate agregado falhou ([intelligence-complete](../checklists/offer-book-stack/intelligence-complete-gate.md), [offer-architecture](../checklists/offer-book-stack/offer-architecture-gate.md) ou [big-idea-locked](../checklists/offer-book-stack/big-idea-locked-gate.md)) e devolve ao bloco correspondente (D1/D2/D3). **Re-entrada:** a fase que falhou; o D4 só abre com o DoD verde.

### `money-model-designer` veta (espinha) — D2
- **Gatilho:** tentar copy/funil/logística sem a escada de 4 partes existir, ou a oferta de atração não liquida o CAC. **Retorno:** ao próprio money-model-designer para completar a sequência ([money-model-four-parts-gate](../checklists/money-model/money-model-four-parts-gate.md)). **Por quê:** viola `money_model_spine`.

### `value-equation-engineer` veta (componente órfão) — D2
- **Gatilho:** um componente da oferta não move nenhuma alavanca (Sonho/Probabilidade/Tempo/Esforço). **Retorno:** o componente é cortado ou reposicionado ([value-no-orphan-lever-gate](../checklists/value/value-no-orphan-lever-gate.md)). **Por quê:** `value_equation_test`.

### `big-idea-architect` veta (múltiplas ideias) — D3
- **Gatilho:** o lançamento sai com mais de uma tese central. **Retorno:** volta à poda do ToT até travar UMA ([big-idea-single-gate](../checklists/big-idea/big-idea-single-gate.md)). **Por quê:** `one_big_idea` / Power of One.

### `voice-style-guardian` veta (voz) — D4
- **Gatilho:** copy fora do padrão (frases longas, voz passiva, advérbios, jargão). **Retorno:** REPROVADO com redline ao agente de copy; re-roda a [voice-pass](../tasks/copy/voice-pass.md). **Por quê:** `clarity_before_volume`.

### `compliance-auditor` veta (a última barreira) — D7
- **Gatilho:** claim sem prova, escassez/urgência falsa, garantia inexequível, disclaimer ausente, violação setorial/privacidade. **Retorno por tipo de defeito:**
  - claim sem lastro → [proof-credibility-curator](../agents/proof-credibility-curator.md) (coletar prova) ou copy (suavizar/cortar);
  - escassez falsa → [launch-producer](../agents/launch-producer.md) (criar limite real) ou copy (remover);
  - privacidade → [tech-links-deliverability-engineer](../agents/tech-links-deliverability-engineer.md).
- **Override:** só o [offerbook-chief](../agents/offerbook-chief.md), com decisão gravada no [decision-registry](../data/registries/decision-registry.md) — **exceto** claim falso e escassez falsa, que **não têm override**. **Por quê:** `truthful_scarcity` + `evidence_before_opinion`.

## Conflito entre agentes
Quando dois agentes discordam e travam o pipeline, o [chief-conflict-resolution-gate](../checklists/chief/chief-conflict-resolution-gate.md) é acionado: o chief decide, registra o trade-off no [decision-registry](../data/registries/decision-registry.md) e o pipeline segue.

## Princípio
Todo "não" vem com um **caminho de volta**: o gate nomeia o defeito, o dono corrige, o registry guarda a decisão. O sistema falha **fechado** (bloqueia a entrega ruim), nunca **aberto** (deixa passar). É isso que protege LTV e marca a cada lançamento.
