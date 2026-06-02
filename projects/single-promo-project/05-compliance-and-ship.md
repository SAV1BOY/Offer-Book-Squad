---
id: project.single-promo-project.05-compliance-and-ship
title: "Fase 05 — Compliance & Lançamento"
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
  - artifact.links-urls
produces:
  - artifact.compliance-report
  - artifact.faq
  - decision.ship-approval
  - artifact.lessons-learned
tags: [project-phase, single-promo, compliance, ship, lgpd, ftc, memoria, d7]
---

# Fase 05 — Compliance & Lançamento

## Objetivo da Fase
Auditar tudo, liberar o disparo e gravar a memória. Esta é a última barreira da promo enxuta. O [`compliance-auditor`](../../agents/compliance-auditor.md) confere cada claim contra sua prova, valida que toda escassez e urgência são reais, e checa T&Cs, disclaimers e privacidade (LGPD/FTC). O estado-pronto é o relatório de compliance sem pendência aberta, o FAQ publicado, a aprovação de disparo registrada e as lições aprendidas gravadas para o próximo caso. Compliance pode vetar: claim sem lastro ou escassez falsa derruba o lançamento até a correção. Depois do verde, a promo vai ao ar. E o que funcionou ou falhou vira memória reutilizável — porque o squad não repete erro de uma promo na seguinte.

## Critério de Entrada
As fases anteriores entregam o Offer Book, a peça-âncora, a sequência de e-mail, o mapa de funil e a planilha de URLs. Pré-condição: a copy está completa, o funil testado e os links no ar. Pré-condição dura: existe um claim-registry e um proof-registry para cruzar cada afirmação com sua evidência. Se houver claim sem prova ou escassez vaga, esta fase abre uma falha e devolve à fase de origem. O [`claim-registry`](../../data/registries/claim-registry.md) e o [`proof-registry`](../../data/registries/proof-registry.md) são as fontes de verdade do cruzamento.

## Agentes & Tasks
- **Task [`compliance-audit`](../../tasks/qa-memory/compliance-audit.md)** — donos [`compliance-auditor`](../../agents/compliance-auditor.md) e [`offerbook-chief`](../../agents/offerbook-chief.md). Audita e libera.
- **Task [`memory-update`](../../tasks/qa-memory/memory-update.md)** — dono [`knowledge-librarian`](../../agents/knowledge-librarian.md). Grava as lições e promove o que ganhou a padrão.

## Passos
1. Cruze cada claim com sua prova usando [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md). Claim sem lastro = veto.
2. Valide a escassez e a urgência com [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md): a janela e o limite são reais? Falso = veto.
3. Confira T&Cs, disclaimers de resultado e a base legal de privacidade (LGPD/FTC).
4. Escreva o FAQ que neutraliza as últimas objeções e formaliza as regras da oferta.
5. Passe os três gates de compliance. Pendência aberta bloqueia o disparo.
6. Com tudo verde, registre a `decision.ship-approval` e libere a promo ao ar.
7. Depois do lançamento, colha o que funcionou e o que falhou e grave no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md).
8. Promova o que ganhou a padrão reutilizável: estrutura vencedora ao [`control-registry`](../../data/registries/control-registry.md), ângulo de copy ao [`swipe-registry`](../../data/registries/swipe-registry.md).
9. Atualize o `decision-registry` com o fechamento do caso.

## Artefatos Produzidos
- `artifact.compliance-report` — o relatório com cada claim, escassez e disclaimer auditado.
- `artifact.faq` — o FAQ público da oferta.
- `decision.ship-approval` — a liberação registrada de disparo.
- `artifact.lessons-learned` — as lições gravadas para o próximo caso.
- Registries escritos: [`claim-registry`](../../data/registries/claim-registry.md), [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), [`control-registry`](../../data/registries/control-registry.md).

## Gates
- [`compliance/compliance-claim-backing-gate`](../../checklists/compliance/compliance-claim-backing-gate.md) — nenhum claim sem lastro.
- [`compliance/compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md) — escassez 100% real.
- [`compliance/compliance-disclaimers-gate`](../../checklists/compliance/compliance-disclaimers-gate.md) e [`final-delivery-checklist`](../../checklists/final-delivery-checklist.md).

## Critério de Saída
Cada claim tem prova; toda escassez e urgência são verdadeiras; T&Cs, disclaimers e privacidade estão conformes; o FAQ está publicado; os três gates de compliance estão verdes; a aprovação de disparo está registrada; as lições estão no registry. A promo está no ar e a memória, gravada. Este é o fim da trilha single-promo. Se um claim ficou sem lastro ou a escassez é falsa, o disparo não acontece — o veto de compliance é final.
