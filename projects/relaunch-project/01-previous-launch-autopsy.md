---
id: project.relaunch-project.01-previous-launch-autopsy
title: "Fase 01 — Autópsia do Lançamento Anterior"
type: project-phase
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
consumes:
  - artifact.prior-launch-inventory
  - decision.scope-one-sentence
produces:
  - artifact.launch-autopsy
  - artifact.failure-diagnosis
  - decision.what-to-keep-kill-change
tags: [project-phase, relaunch, autopsia, losing-controls, licoes, diagnostico, d1]
---

# Fase 01 — Autópsia do Lançamento Anterior

## Objetivo da Fase
Dissecar o lançamento anterior e nomear, com evidência, por que ele não atingiu a meta. Esta é a fase que define a trilha de relançamento. Em vez de refazer no escuro, abrimos o corpo e olhamos os números: onde a conversão caiu, qual etapa do funil sangrou, qual ângulo cansou, qual objeção ficou sem resposta. O estado-pronto é a autópsia completa — o diagnóstico de falha ligado a cada peça do lançamento anterior — e a decisão fria do que manter, do que matar e do que mudar. Memória antes de repetição: o squad não repete o erro de um lançamento no seguinte. Os controles que perderam viram aprendizado, não lixo. A autópsia separa o que era bom mas mal executado do que era ruim na raiz. Sem este diagnóstico, o relançamento é só um chute mais caro.

## Critério de Entrada
A [`00-brief`](00-brief.md) entrega o `artifact.prior-launch-inventory` com os ativos e dados do lançamento anterior. Pré-condição: existe material arquivado e ao menos um dado de resultado (conversão, faturamento, taxa de abertura, take rate). Se não há nenhum dado de desempenho, a autópsia é qualitativa e marca a lacuna — sem número, o diagnóstico é hipótese, não fato. O [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) é lido para puxar as lições já gravadas; o [`control-registry`](../../data/registries/control-registry.md) localiza os controles que perderam.

## Agentes & Tasks
- **Task [`memory-update`](../../tasks/qa-memory/memory-update.md)** — dono [`knowledge-librarian`](../../agents/knowledge-librarian.md), que lê a memória e estrutura a autópsia.
- **Task [`run-market-intel`](../../tasks/intelligence/run-market-intel.md)** — dono [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md), para checar se o mercado mudou desde o lançamento anterior.

## Passos
1. Reúna os ativos do lançamento anterior de [`archive/losing-controls`](../../archive/losing-controls) e [`archive/past-launches`](../../archive/past-launches): copy, funil, sequência, oferta, Big Idea.
2. Leia as lições gravadas no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md): o que já se sabia que falhou.
3. Mapeie o funil anterior e localize onde a conversão sangrou: opt-in, VSL, checkout, upsell.
4. Diagnostique a oferta com [`offer/offer-diagnosis`](../../frameworks/offer/offer-diagnosis.md): a oferta era forte ou o problema era a oferta?
5. Avalie a Big Idea anterior em [`archive/retired-big-ideas`](../../archive/retired-big-ideas): ela ainda é nova, grande e crível, ou cansou?
6. Cheque se o mercado mudou com [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md): a sofisticação subiu? O claim que funcionava ficou genérico?
7. Busque a contra-evidência: o que parecia culpa da copy pode ter sido tráfego ou oferta. Não conclua antes de contradizer.
8. Decida o que manter, matar e mudar — peça por peça, com motivo. Grave a decisão no [`decision-registry`](../../data/registries/decision-registry.md) e atualize as lições.

## Artefatos Produzidos
- `artifact.launch-autopsy` — a dissecação do lançamento anterior, peça por peça, com os números.
- `artifact.failure-diagnosis` — a causa-raiz de cada queda, com evidência e contra-evidência.
- `decision.what-to-keep-kill-change` — a decisão fria do que manter, matar e mudar.
- Registries escritos: [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`final-delivery-checklist`](../../checklists/final-delivery-checklist.md) — a autópsia cobre cada peça do lançamento anterior.
- [`chief/chief-conflict-resolution-gate`](../../checklists/chief/chief-conflict-resolution-gate.md) — a decisão manter/matar/mudar tem motivo e resolve conflitos.

## Critério de Saída
A autópsia cobre cada peça do lançamento anterior; cada queda de conversão tem causa-raiz com evidência; a oferta e a Big Idea anteriores foram diagnosticadas; o mercado foi reavaliado; a contra-evidência foi buscada; a decisão do que manter, matar e mudar está travada com motivo. Os gates estão verdes; as lições estão atualizadas. A próxima fase é a [`02-offer-and-bigidea-refresh`](02-offer-and-bigidea-refresh.md), que recebe o diagnóstico e a decisão para renovar a oferta e a Big Idea sobre o que sobreviveu à autópsia.
