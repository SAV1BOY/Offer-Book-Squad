---
id: template.core.offer-book-master-b2b
title: "Offer Book Master — Variante B2B / Enterprise"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
frameworks: [positioning/jtbd, value-equation, proof-to-claim-chain, pricing/packaging-good-better-best]
checklists: [offer-book-stack/offer-book-dod-gate, avatar/avatar-dmu-gate]
sources:
  - "Dixon & Adamson, *The Challenger Sale* (2011)"
  - "Neil Rackham, *SPIN Selling* (1988)"
tags: [template, b2b, enterprise, dmu, meddpicc, business-case, battle-cards]
---

# Offer Book Master — Variante B2B / Enterprise

## Como usar
Variante do [`offer-book-master`](offer-book-master.md) para o project type [`enterprise-deal-book`](../../projects/enterprise-deal-book-project/00-brief.md). Use quando a compra é **por comitê** (DMU), o ciclo é longo e o "sim" exige **business case**. Pareie com [`battle-cards-template`](../strategy/battle-cards-template.md). Fundamentos: [SPIN](../../reference/books/b2b-enterprise/rackham-spin-selling.md), [Challenger](../../reference/books/b2b-enterprise/dixon-adamson-challenger-sale.md), [MEDDIC/MEDDPICC](../../reference/books/b2b-enterprise/meddic-meddpicc.md).

## Campos & Instruções
Cada `{{PLACEHOLDER}}` é um campo. O que muda vs B2C: o **avatar vira DMU** (vários papéis), a **prova vira referência de par/segmento**, o **preço vira packaging + procurement**, e a **oferta vira business case** (ROI/TCO), não promessa emocional. Regra de ouro do B2B: o "sim" é **coletivo** — cada papel da DMU precisa do seu próprio motivo para comprar (o Economic Buyer quer ROI, o Técnico quer integração/segurança, o Usuário quer menos atrito), e o **custo da inação** costuma derrubar mais negócios que o concorrente direto. Atualize o offer book a cada mudança de comitê, de critério de decisão ou de concorrente — em ciclo longo, a informação envelhece e o deal esfria.

## O Template
```md
# Offer Book B2B — {{empresa/oferta}}

## 1. ICP & DMU (comitê de compra)
- ICP: {{firmographics: setor, porte, stack, gatilho}}
- DMU: Economic Buyer {{quem}} · Champion {{quem}} · Users {{quem}} · Technical Buyer {{quem}} · Blocker {{quem}}
- Job-to-be-done de cada papel: {{jtbd por papel}}

## 2. Qualificação (MEDDPICC)
Metrics {{KPI do cliente}} · Economic buyer {{}} · Decision criteria {{}} · Decision process {{}} · Paper process {{jurídico/procurement}} · Identify pain {{}} · Champion {{}} · Competition {{}}

## 3. Problema & Mecanismo (reframe Challenger)
- Insight que reenquadra o problema do cliente: {{teaching insight}}
- Mecanismo único da solução: {{por que funciona vs o status quo/concorrente}}
- Custo da inação (status quo): {{quantificado}}

## 4. Valor & Business Case
- ROI: {{ganho anual}} ÷ {{investimento}} = {{x}}; payback {{meses}}
- TCO vs alternativa: {{}}
- Value Equation por stakeholder: {{sonho×prob ÷ tempo×esforço}}

## 5. Prova enterprise
- Referências de par/segmento: {{logos/casos}} · dados: {{benchmark}} · segurança/compliance: {{SOC2/LGPD}}

## 6. Pricing & Packaging
- Good/Better/Best + decoy: {{3 pacotes}} · modelo: {{seat/uso/plataforma}} · termos de procurement: {{}}

## 7. Risco & Mutual Action Plan
- Reversão de risco (piloto/SLA/garantia): {{}} · MAP: {{passos+datas até a assinatura}}
```

## Exemplo preenchido
**SaaS de observabilidade, ICP: fintechs 200–1000 func.** DMU: EB = VP Eng, Champion = SRE lead, Blocker = Segurança. MEDDPICC: métrica = MTTR; competition = incumbente legado. Reframe Challenger: "vocês pagam o downtime, não a ferramenta — R$ X/h". Business case: ROI 4,1× via −38% MTTR; payback 5 meses. Packaging: Team/Growth/Enterprise + decoy. MAP: POC 30d → security review → procurement → assinatura.

## DoD do entregável
DMU completo (≥5 papéis) · MEDDPICC sem campo vazio crítico · business case com ROI **quantificado e com fonte** · ≥2 referências de par · packaging com decoy · MAP com datas · passou no [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) e no [`avatar-dmu-gate`](../../checklists/avatar/avatar-dmu-gate.md).
