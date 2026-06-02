---
id: project.offer-ladder-project.04-products-and-offers
title: "Fase 04 — Produtos & Ofertas (Compliance & Handoff)"
type: project-phase
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes:
  - artifact.money-model
  - decision.sequence-and-triggers
  - template.offer.products-and-offers
produces:
  - artifact.products-and-offers
  - artifact.offer-stack
  - artifact.compliance-report
  - decision.ladder-handoff-approval
  - artifact.lessons-learned
tags: [project-phase, offer-ladder, produtos, ofertas, offer-stack, compliance, handoff, d2]
---

# Fase 04 — Produtos & Ofertas (Compliance & Handoff)

## Objetivo da Fase
Detalhar cada degrau num produto e oferta concretos, auditar a escada e entregá-la pronta para as outras trilhas. A sequência já existe; aqui ela vira planilha operável: para cada degrau, o produto, o stack de valor, a garantia, a escassez verdadeira, o preço e o gatilho. O estado-pronto é a planilha de produtos e ofertas completa, cada degrau com seu offer stack montado, a auditoria de compliance sem pendência e a aprovação de handoff registrada. Como toda trilha do squad, esta termina em compliance: nenhum preço enganoso, nenhuma garantia impossível, nenhuma escassez falsa. Depois do verde, a escada é entregue — para uma single-promo, um full-launch ou um relaunch consumirem. E o que se aprendeu vira memória.

## Critério de Entrada
A [`03-money-model`](03-money-model.md) entrega o `artifact.money-model` com a sequência, os gatilhos e o desenho de continuidade. Pré-condição: a espinha tem no mínimo duas partes sequenciadas, cada degrau tem CTA e a economia se paga. Se a sequência ainda não fechou os gates de money model, esta fase não abre. O [`offer-registry`](../../data/registries/offer-registry.md) é lido para puxar cada degrau; o [`claim-registry`](../../data/registries/claim-registry.md) e o [`proof-registry`](../../data/registries/proof-registry.md) sustentam a auditoria de claims.

## Agentes & Tasks
- **Task [`design-money-model`](../../tasks/offer-architecture/design-money-model.md)** — dono [`money-model-designer`](../../agents/money-model-designer.md), com [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) detalhando cada oferta.
- **Task [`compliance-audit`](../../tasks/qa-memory/compliance-audit.md)** — donos [`compliance-auditor`](../../agents/compliance-auditor.md) e [`offerbook-chief`](../../agents/offerbook-chief.md).
- **Task [`memory-update`](../../tasks/qa-memory/memory-update.md)** — dono [`knowledge-librarian`](../../agents/knowledge-librarian.md).

## Passos
1. Para cada degrau, detalhe o produto e monte o offer stack com [`offer-stack-builder`](../../frameworks/offer-stack-builder.md): componentes, bônus, ancoragem.
2. Desenhe a garantia de cada degrau com [`guarantee-design`](../../frameworks/guarantee-design.md) e a reversão de risco com [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md).
3. Defina a escassez verdadeira de cada oferta com [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md). Limite real, nunca fabricado.
4. Preencha a planilha de produtos e ofertas: produto, papel, preço, stack, garantia, escassez, gatilho, por degrau.
5. Audite a escada: cada claim de preço e resultado com lastro em [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md). Claim sem prova = veto.
6. Valide que nenhuma escassez é falsa e que cada garantia é cumprível.
7. Passe os gates de compliance e de offer stack. Pendência aberta bloqueia o handoff.
8. Registre a `decision.ladder-handoff-approval` e entregue a escada às trilhas consumidoras.
9. Grave o que funcionou no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) e atualize o `offer-registry`.

## Artefatos Produzidos
- `artifact.products-and-offers` — a planilha completa, um degrau por linha.
- `artifact.offer-stack` — o stack de valor de cada degrau.
- `artifact.compliance-report` — a auditoria de claims, garantias e escassez.
- `decision.ladder-handoff-approval` — a liberação da escada.
- `artifact.lessons-learned` — as lições gravadas.
- Registries escritos: [`offer-registry`](../../data/registries/offer-registry.md), [`claim-registry`](../../data/registries/claim-registry.md), [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md).

## Gates
- [`offer-stack-checklist`](../../checklists/offer-stack-checklist.md) e [`guarantee-checklist`](../../checklists/guarantee-checklist.md) — stack e garantia válidos.
- [`compliance/compliance-claim-backing-gate`](../../checklists/compliance/compliance-claim-backing-gate.md) — nenhum claim sem lastro.
- [`compliance/compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md) — escassez 100% real.

## Critério de Saída
Cada degrau tem produto, offer stack, garantia, escassez verdadeira e preço na planilha; cada claim tem prova; cada garantia é cumprível; nenhuma escassez é falsa; a aprovação de handoff está registrada; as lições estão no registry. Os gates de offer stack e de compliance estão verdes. Esta é a fase final da trilha offer-ladder: a escada está economicamente válida, auditada e pronta para uma single-promo, um full-launch ou um relaunch consumirem. Se um claim ficou sem lastro, o veto de compliance bloqueia o handoff até a correção.
