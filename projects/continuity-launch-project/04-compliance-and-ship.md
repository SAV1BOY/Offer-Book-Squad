---
id: project.continuity-launch-project.04-compliance-and-ship
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
  - artifact.retention-sequence
  - artifact.funnel-map
  - artifact.churn-playbook
produces:
  - artifact.compliance-report
  - artifact.faq
  - decision.ship-approval
  - artifact.lessons-learned
tags: [project-phase, continuity, compliance, ship, billing, cancelamento, lgpd, ftc, memoria, d7]
---

# Fase 04 — Compliance & Lançamento

## Objetivo da Fase
Auditar tudo, liberar o lançamento e gravar a memória — com atenção redobrada às regras de cobrança recorrente. Continuidade tem um risco de compliance que a oferta única não tem: a cobrança que se repete. Termo de assinatura obscuro, cancelamento difícil ou renovação sem aviso são as principais armadilhas legais da recorrência. Esta é a última barreira. O [`compliance-auditor`](../../agents/compliance-auditor.md) confere cada claim de valor recorrente contra a prova, valida que toda escassez é real, e checa com rigor as regras de cobrança: o termo de assinatura é claro, o cancelamento é fácil, a renovação avisa, e a privacidade (LGPD/FTC) está conforme. O estado-pronto é o relatório de compliance sem pendência, o FAQ com as regras de cobrança e cancelamento, a aprovação de disparo registrada e as lições gravadas. Compliance pode vetar: cobrança recorrente obscura derruba o lançamento.

## Critério de Entrada
A [`03-copy-and-sequence`](03-copy-and-sequence.md) entrega a peça-âncora, as sequências e o funil; a [`02-retention-and-onboarding`](02-retention-and-onboarding.md) entrega o playbook de churn com o dunning. Pré-condição: a copy está completa, o funil testado e o checkout recorrente configurado. Pré-condição dura: existe um claim-registry e um proof-registry para cruzar cada claim de valor recorrente com a evidência, e as regras de cobrança estão escritas. Se o cancelamento não está claro ou um claim de valor recorrente não tem prova, esta fase abre uma falha e devolve. O [`claim-registry`](../../data/registries/claim-registry.md) e o [`proof-registry`](../../data/registries/proof-registry.md) são as fontes do cruzamento.

## Agentes & Tasks
- **Task [`compliance-audit`](../../tasks/qa-memory/compliance-audit.md)** — donos [`compliance-auditor`](../../agents/compliance-auditor.md) e [`offerbook-chief`](../../agents/offerbook-chief.md). Audita e libera.
- **Task [`memory-update`](../../tasks/qa-memory/memory-update.md)** — dono [`knowledge-librarian`](../../agents/knowledge-librarian.md). Grava as lições de retenção e churn.

## Passos
1. Cruze cada claim de valor recorrente com sua prova usando [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md). Claim sem lastro = veto.
2. Audite as regras de cobrança recorrente: o termo de assinatura é claro, o valor e a cadência estão visíveis antes da compra.
3. Confirme que o cancelamento é fácil e a renovação avisa: cobrança recorrente obscura é veto.
4. Valide a escassez e a urgência do lançamento com [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md): a janela é real? Falso = veto.
5. Confira a base de privacidade (LGPD/FTC) e o tratamento dos dados de cobrança.
6. Escreva o FAQ com as regras de cobrança, renovação e cancelamento, e as últimas objeções de assinatura.
7. Passe os três gates de compliance. Pendência aberta bloqueia o disparo.
8. Com tudo verde, registre a `decision.ship-approval` e libere o lançamento ao ar.
9. Grave as lições de venda, onboarding e retenção no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) e promova o que ganhou ao [`control-registry`](../../data/registries/control-registry.md).

## Artefatos Produzidos
- `artifact.compliance-report` — cada claim, escassez, regra de cobrança e disclaimer auditado.
- `artifact.faq` — o FAQ com as regras de cobrança, renovação e cancelamento.
- `decision.ship-approval` — a liberação registrada de disparo.
- `artifact.lessons-learned` — as lições de venda, onboarding e retenção.
- Registries escritos: [`claim-registry`](../../data/registries/claim-registry.md), [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), [`control-registry`](../../data/registries/control-registry.md).

## Gates
- [`compliance/compliance-claim-backing-gate`](../../checklists/compliance/compliance-claim-backing-gate.md) — nenhum claim de valor recorrente sem lastro.
- [`compliance/compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md) — escassez 100% real.
- [`compliance/compliance-disclaimers-gate`](../../checklists/compliance/compliance-disclaimers-gate.md) — regras de cobrança, cancelamento e privacidade conformes; e [`final-delivery-checklist`](../../checklists/final-delivery-checklist.md).

## Critério de Saída
Cada claim de valor recorrente tem prova; as regras de cobrança são claras, o cancelamento é fácil e a renovação avisa; toda escassez é verdadeira; a privacidade está conforme; o FAQ traz as regras de cobrança e cancelamento; os três gates de compliance estão verdes; a aprovação de disparo está registrada; as lições estão no registry. O lançamento de continuidade está no ar e a memória, gravada. Esta é a fase final da trilha continuity-launch. Se a cobrança recorrente é obscura ou um claim ficou sem lastro, o disparo não acontece — o veto de compliance é final.
