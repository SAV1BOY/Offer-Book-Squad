---
id: project.relaunch-project.04-compliance-and-ship
title: "Fase 04 — Compliance & Lançamento"
type: project-phase
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
consumes:
  - artifact.offer-book-master
  - artifact.vsl-script
  - artifact.email-sequence
  - artifact.funnel-map
  - artifact.failure-diagnosis
produces:
  - artifact.compliance-report
  - artifact.faq
  - decision.ship-approval
  - artifact.lessons-learned
tags: [project-phase, relaunch, compliance, ship, lgpd, ftc, memoria, d7]
---

# Fase 04 — Compliance & Lançamento

## Objetivo da Fase
Auditar tudo, liberar o relançamento e gravar a memória — fechando o ciclo que a autópsia abriu. Esta é a última barreira da trilha de relançamento. O [`compliance-auditor`](../../agents/compliance-auditor.md) confere cada claim da nova copy contra sua prova, valida que toda escassez e urgência são reais, e checa T&Cs, disclaimers e privacidade (LGPD/FTC). Há um foco extra aqui: confirmar que as correções da autópsia foram de fato aplicadas — que o ponto que sangrou antes não voltou. O estado-pronto é o relatório de compliance sem pendência, o FAQ publicado, a aprovação de disparo registrada e as lições do relançamento gravadas. Compliance pode vetar. E, como o relançamento nasceu da memória, ele também a alimenta: o que finalmente funcionou vira padrão, e o que ainda falhou vira a próxima lição. Memória antes de repetição, fechando o laço.

## Critério de Entrada
A [`03-new-copy-and-funnel`](03-new-copy-and-funnel.md) entrega a nova peça-âncora, a sequência, o funil e os links; a [`01-previous-launch-autopsy`](01-previous-launch-autopsy.md) entrega o diagnóstico de falha para conferir as correções. Pré-condição: a nova copy está completa, o funil testado e os links no ar. Pré-condição dura: existe um claim-registry e um proof-registry para cruzar cada claim com sua evidência. Se houver claim sem prova ou se uma correção da autópsia não foi aplicada, esta fase abre uma falha e devolve à fase de origem. O [`claim-registry`](../../data/registries/claim-registry.md) e o [`proof-registry`](../../data/registries/proof-registry.md) são as fontes do cruzamento.

## Agentes & Tasks
- **Task [`compliance-audit`](../../tasks/qa-memory/compliance-audit.md)** — donos [`compliance-auditor`](../../agents/compliance-auditor.md) e [`offerbook-chief`](../../agents/offerbook-chief.md). Audita e libera.
- **Task [`memory-update`](../../tasks/qa-memory/memory-update.md)** — dono [`knowledge-librarian`](../../agents/knowledge-librarian.md). Grava as lições e fecha o laço da autópsia.

## Passos
1. Cruze cada claim da nova copy com sua prova usando [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md). Claim sem lastro = veto.
2. Valide a escassez e a urgência com [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md): a janela e o limite são reais? Falso = veto.
3. Confirme que as correções da autópsia foram aplicadas: o ponto de sangramento anterior não voltou.
4. Confira T&Cs, disclaimers de resultado e a base de privacidade (LGPD/FTC).
5. Escreva o FAQ que neutraliza as últimas objeções e formaliza as regras da oferta.
6. Passe os três gates de compliance. Pendência aberta bloqueia o disparo.
7. Com tudo verde, registre a `decision.ship-approval` e libere o relançamento ao ar.
8. Depois do lançamento, compare o resultado com o anterior e grave no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md): a correção funcionou?
9. Promova o que ganhou a padrão reutilizável: estrutura vencedora ao [`control-registry`](../../data/registries/control-registry.md), ângulo ao [`swipe-registry`](../../data/registries/swipe-registry.md). Aposente o controle que perdeu de novo.

## Artefatos Produzidos
- `artifact.compliance-report` — cada claim, escassez e disclaimer auditado, mais a checagem das correções.
- `artifact.faq` — o FAQ público da oferta.
- `decision.ship-approval` — a liberação registrada de disparo.
- `artifact.lessons-learned` — as lições do relançamento, comparadas ao anterior.
- Registries escritos: [`claim-registry`](../../data/registries/claim-registry.md), [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), [`control-registry`](../../data/registries/control-registry.md).

## Gates
- [`compliance/compliance-claim-backing-gate`](../../checklists/compliance/compliance-claim-backing-gate.md) — nenhum claim sem lastro.
- [`compliance/compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md) — escassez 100% real.
- [`compliance/compliance-disclaimers-gate`](../../checklists/compliance/compliance-disclaimers-gate.md) e [`final-delivery-checklist`](../../checklists/final-delivery-checklist.md).

## Critério de Saída
Cada claim tem prova; toda escassez é verdadeira; as correções da autópsia foram aplicadas; T&Cs, disclaimers e privacidade estão conformes; o FAQ está publicado; os três gates de compliance estão verdes; a aprovação de disparo está registrada; as lições do relançamento estão no registry, comparadas ao anterior. O relançamento está no ar e o laço da memória, fechado. Esta é a fase final da trilha relaunch. Se um claim ficou sem lastro ou uma correção não foi aplicada, o disparo não acontece — o veto de compliance é final.
