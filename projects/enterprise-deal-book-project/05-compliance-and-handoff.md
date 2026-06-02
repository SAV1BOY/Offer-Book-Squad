---
id: project.enterprise-deal-book-project.05-compliance-and-handoff
title: "Fase 05 — Compliance & Handoff de Vendas"
type: project-phase
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
consumes:
  - artifact.offer-book-master
  - artifact.deal-deck
  - artifact.business-case-doc
  - artifact.champion-kit
produces:
  - artifact.compliance-report
  - artifact.faq
  - decision.deal-book-handoff-approval
  - artifact.lessons-learned
tags: [project-phase, enterprise, b2b, compliance, handoff, sales, lgpd, ftc, memoria, d7]
---

# Fase 05 — Compliance & Handoff de Vendas

## Objetivo da Fase
Auditar cada claim do caso de negócio, liberar o deal book e entregá-lo ao time de vendas. Em B2B, um número errado no business case não custa uma venda — custa a credibilidade na conta inteira. Esta é a última barreira. O [`compliance-auditor`](../../agents/compliance-auditor.md) confere que cada métrica de ROI tem base de cálculo, que cada claim de segurança ou conformidade é verdadeiro, que nenhuma urgência é fabricada e que T&Cs, disclaimers e privacidade (LGPD/FTC) estão conformes. O estado-pronto é o relatório de compliance sem pendência, o FAQ do comitê publicado, a aprovação de handoff registrada e o deal book entregue ao time de vendas com a malha MEDDPICC preenchida. Compliance pode vetar: claim de ROI sem lastro derruba o handoff. E o que se aprendeu na conta vira memória reutilizável para o próximo deal.

## Critério de Entrada
A [`04-deal-deck-and-business-case`](04-deal-deck-and-business-case.md) entrega o Offer Book Master, o deal deck, o business case doc e o champion kit. Pré-condição: o HARD STOP está verde e o deck está completo. Pré-condição dura: existe um claim-registry e um proof-registry para cruzar cada métrica de ROI e cada claim de segurança com sua evidência. Se uma métrica do business case não tem base de cálculo, esta fase abre uma falha e devolve à [`02-value-and-pricing-packaging`](02-value-and-pricing-packaging.md). O [`claim-registry`](../../data/registries/claim-registry.md) e o [`proof-registry`](../../data/registries/proof-registry.md) são as fontes do cruzamento.

## Agentes & Tasks
- **Task [`compliance-audit`](../../tasks/qa-memory/compliance-audit.md)** — donos [`compliance-auditor`](../../agents/compliance-auditor.md) e [`offerbook-chief`](../../agents/offerbook-chief.md). Audita e libera.
- **Task [`memory-update`](../../tasks/qa-memory/memory-update.md)** — dono [`knowledge-librarian`](../../agents/knowledge-librarian.md). Grava as lições da conta.

## Passos
1. Cruze cada métrica de ROI e cada claim do business case com sua prova usando [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md). Claim sem lastro = veto.
2. Valide os claims de segurança e conformidade do champion kit: a certificação, a homologação e a base legal existem de fato.
3. Confira que nenhuma urgência ou escassez é fabricada com [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md): prazos de proposta são reais.
4. Audite T&Cs, disclaimers de resultado e a base de privacidade (LGPD/FTC) do material que circula no comitê.
5. Escreva o FAQ do comitê que neutraliza as últimas objeções por papel e formaliza as regras da proposta.
6. Confirme a malha MEDDPICC preenchida: métrica, comprador econômico, critérios, processo, papel, campeão e concorrência mapeados.
7. Passe os gates de compliance. Pendência aberta bloqueia o handoff.
8. Com tudo verde, registre a `decision.deal-book-handoff-approval` e entregue o deal book ao time de vendas.
9. Grave o que funcionou e o que falhou no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) e promova a estrutura vencedora ao [`control-registry`](../../data/registries/control-registry.md).

## Artefatos Produzidos
- `artifact.compliance-report` — cada métrica, claim de segurança e disclaimer auditado.
- `artifact.faq` — o FAQ do comitê, por papel.
- `decision.deal-book-handoff-approval` — a liberação registrada do deal book.
- `artifact.lessons-learned` — as lições da conta para o próximo deal.
- Registries escritos: [`claim-registry`](../../data/registries/claim-registry.md), [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md), [`control-registry`](../../data/registries/control-registry.md).

## Gates
- [`compliance/compliance-claim-backing-gate`](../../checklists/compliance/compliance-claim-backing-gate.md) — nenhum claim de ROI ou segurança sem lastro.
- [`compliance/compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md) — nenhuma urgência fabricada.
- [`compliance/compliance-disclaimers-gate`](../../checklists/compliance/compliance-disclaimers-gate.md) e [`final-delivery-checklist`](../../checklists/final-delivery-checklist.md).

## Critério de Saída
Cada métrica de ROI e cada claim de segurança tem prova; nenhuma urgência é fabricada; T&Cs, disclaimers e privacidade estão conformes; o FAQ do comitê está publicado; a malha MEDDPICC está preenchida; a aprovação de handoff está registrada; as lições estão no registry. Os três gates de compliance estão verdes. Esta é a fase final da trilha enterprise-deal-book: o deal book está auditado e entregue ao time de vendas. Se uma métrica ficou sem base de cálculo, o veto de compliance bloqueia o handoff até a correção.
