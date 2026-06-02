---
id: data.handoffs.example-deepresearch-to-offerbook
title: "Handoff (exemplo) — deepresearch_squad → Offer Book Squad"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
tags: [handoff, cross-squad, deepresearch, example, input-acceptance]
---

# Handoff executável — deepresearch_squad → Offer Book Squad

Instância **preenchida** do [contrato de handoff](../../templates/cross-squad/handoff-contract-template.md), validada pela gate de entrada [`cross-squad-asset-validation`](../../checklists/cross-squad/cross-squad-asset-validation.md). Valide com `python scripts/handoff-validate.py data/handoffs/example-deepresearch-to-offerbook.md`. É o **input-acceptance** real que o [offer-squad-architect](../../agents/offer-squad-architect.md) aplica antes de a D1 começar.

## Campos do contrato
- **de_squad:** deepresearch_squad
- **para_squad:** offer-book-squad (Offer Book Squad)
- **artefato:** Pacote de Inteligência de Mercado (market sizing + VOC + competitor intel)
- **campos_esperados:** TAM/SAM/SOM com fonte; ≥10 verbatims de VOC por segmento; tabela de concorrentes (oferta, preço, ângulo, prova); nível de sofisticação/consciência inferido de evidência
- **qualidade_minima_por_campo:** sizing triangulado de ≥2 fontes; verbatims literais com origem (review/call/fórum); concorrentes com link/print; sofisticação justificada por ads/reviews (não palpite)
- **dono:** chefe do deepresearch_squad (entrega) → offer-squad-architect (aceite)
- **criterio_de_aceite:** passa [`cross-squad-asset-validation`](../../checklists/cross-squad/cross-squad-asset-validation.md) — proveniência ok, sem claim sem lastro, coerente com o briefing; alimenta [`market-brief-template`](../../templates/strategy/market-brief-template.md)
- **return_on_reject:** se faltar sizing triangulado ou <10 verbatims → devolvido ao deepresearch_squad com o defeito nomeado; offer book **não** inicia D1 até aceite (input fraco = bloqueio)
- **registry_entry:** logar em [`data/handoffs/handoff-manifest-template.md`](handoff-manifest-template.md) (handoff_id, de/para, artefato, status, data) + decisão em [`decision-registry`](../registries/decision-registry.md)

## Estado
- **status:** aceito (exemplo) · **handoff_id:** hx-2026-001 · **gate de entrada:** ✅ · **destino:** [`run-market-intel`](../../tasks/intelligence/run-market-intel.md)
