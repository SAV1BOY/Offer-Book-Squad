---
id: doc.team-coordination
title: "Teams & Swarms — Coordenação dos 10 Grupos Funcionais"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
tags: [teams, swarms, coordination, leads, intermediate-gate]
---

# Teams & Swarms — Coordenação dos 10 Grupos Funcionais

A camada L2 (ver [`hrm-governance`](hrm-governance.md)): os 25 agentes se organizam em **10 grupos funcionais** (campo `group` em [`config.yaml`](../config.yaml)). Cada grupo tem um **líder**, um **modo de coordenação** (sequencial ou swarm paralelo) e um **gate intermediário** antes de subir ao chief.

| Grupo | Líder | Membros | Modo | Gate intermediário (sobe ao chief) |
|---|---|---|---|---|
| command (D0) | [offerbook-chief](../agents/offerbook-chief.md) | offer-squad-architect | sequencial | [chief-scope-approval-gate](../checklists/chief/chief-scope-approval-gate.md) |
| intelligence (D1) | [market-sophistication-analyst](../agents/market-sophistication-analyst.md) | avatar-voc-investigator, proof-credibility-curator | **swarm** (paralelo) | [intelligence-complete-gate](../checklists/offer-book-stack/intelligence-complete-gate.md) |
| offer-architecture (D2) | [money-model-designer](../agents/money-model-designer.md) (dono da espinha) | mechanism-architect, value-equation-engineer, pricing-wtp-strategist, unit-economics-stack-analyst | sequencial c/ loop | [offer-architecture-gate](../checklists/offer-book-stack/offer-architecture-gate.md) |
| big-idea (D3) | [big-idea-architect](../agents/big-idea-architect.md) | positioning-lead-strategist | sequencial | [big-idea-locked-gate](../checklists/offer-book-stack/big-idea-locked-gate.md) |
| copy (D4) | [vsl-webinar-scriptwriter](../agents/vsl-webinar-scriptwriter.md) | email-sms-sequence-writer, direct-mail-insert-writer, ad-creative-factory, voice-style-guardian | **swarm** + voice-pass | [copy-coverage-gate](../checklists/blackbook-stack/copy-coverage-gate.md) |
| funnel-tech (D5) | [funnel-architect](../agents/funnel-architect.md) | tech-links-deliverability-engineer | sequencial | [funnel-tech-gate](../checklists/blackbook-stack/funnel-tech-gate.md) |
| ops (D6) | [launch-producer](../agents/launch-producer.md) | events-logistics-coordinator | sequencial | [ops-events-gate](../checklists/blackbook-stack/ops-events-gate.md) |
| growth (D6) | [affiliate-program-architect](../agents/affiliate-program-architect.md) | pr-brand-strategist | **swarm** (paralelo) | [growth-affiliate-pr-gate](../checklists/blackbook-stack/growth-affiliate-pr-gate.md) |
| qa (D7) | [compliance-auditor](../agents/compliance-auditor.md) | — | gate terminal | [blackbook-dod-gate](../checklists/blackbook-stack/blackbook-dod-gate.md) |
| memory (D7) | [knowledge-librarian](../agents/knowledge-librarian.md) | — | registro | [final-delivery-checklist](../checklists/final-delivery-checklist.md) |

## Como um líder coordena (responsabilidade do lead)
1. Recebe o handoff da camada anterior e confirma o **input acceptance** (campos + qualidade mínima — ver o contrato de handoff).
2. **Sequencial:** ordena os membros pela dependência (ex.: offer-architecture: mechanism → value → pricing → unit-econ → money-model).
3. **Swarm (paralelo):** dispara os membros ao mesmo tempo quando não há dependência (ex.: copy: VSL + e-mail + mailer + ads em paralelo), depois **converge** no gate (copy passa pela voice-pass do voice-style-guardian).
4. Roda o **gate intermediário** do grupo. Vermelho → devolve ao membro dono. Verde → entrega ao chief.
5. Loga decisões do grupo no [`decision-registry`](../data/registries/decision-registry.md).

## Regras de swarm
- **Sem dependência → paralelo.** Com dependência → sequência declarada.
- Todo swarm **converge num único gate** antes de subir (nada sobe "meio pronto").
- O lead resolve conflito intra-grupo; se não resolver, escala ao chief ([chief-conflict-resolution-gate](../checklists/chief/chief-conflict-resolution-gate.md)).
- O **voice-style-guardian** é o gate de qualidade do grupo copy (veta peça fora da voz).

> O grupo é a unidade de coordenação; o **gate intermediário** é o que impede que trabalho fraco de um membro contamine a entrega do squad.
