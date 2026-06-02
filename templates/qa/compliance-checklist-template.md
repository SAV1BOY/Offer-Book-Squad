---
id: template.qa.compliance-checklist
title: "Compliance Checklist — A Última Barreira Antes de Publicar"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
consumes: [doc.compliance-policy, data.registry.claim, data.registry.proof]
produces: [data.registry.decision]
frameworks: [proof-to-claim-chain, scarcity-urgency-engine, risk-reversal-ladder]
checklists: [compliance-checklist, compliance/compliance-claim-backing-gate, compliance/compliance-scarcity-truth-gate, compliance/compliance-disclaimers-gate, compliance/compliance-data-privacy-gate, compliance/compliance-sector-rules-gate]
registries: [claim-registry, proof-registry, decision-registry]
tags: [template, compliance, claims, escassez, lgpd, ftc, disclaimers, qa, veto]
---

# Compliance Checklist — A Última Barreira

Este template produz o **checklist de compliance** de uma peça: a verificação final antes de publicar. Ele cruza cada claim com sua prova, confere os disclaimers, prova que a escassez é real e testa as regras de privacidade e de setor. O [`compliance-auditor`](../../agents/compliance-auditor.md) é a última barreira e pode **vetar**. Claim sem lastro e escassez falsa não têm override — destroem LTV, marca e expõem a risco legal. A régua inteira vem da [política de compliance](../../docs/compliance-policy.md).

## Como usar
- **Agente dono:** [`compliance-auditor`](../../agents/compliance-auditor.md). Roda no D7, sobre cada peça pronta, depois da voz aprovada pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md) (as duas barreiras são independentes).
- **Task:** preenchido na auditoria final de cada ativo. Lido pelo [`offerbook-chief`](../../agents/offerbook-chief.md) (único que pode registrar override, e nunca para claim/escassez falsos).
- **Quando:** o auditor roda o checklist sobre toda peça antes de ela ir ao ar. Aplica o [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) para o vínculo claim↔prova e o [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) para testar a escassez.
- Cada item é binário e exige evidência (o id da prova, o trecho do disclaimer, a política de vagas). Item sem evidência = fail.

## Campos & Instruções
- **{{PECA}}** — o ativo auditado (`asset_id` + tipo: vsl, email, sms, mailer, ad, pagina).
- **{{CLAIM}}** / **{{PROVA_REF}}** — cada afirmação factual e o id da prova que a sustenta (`proof-registry#PR-NNN`). Sem prova → veto.
- **{{DISCLAIMER}}** — o aviso obrigatório quando há promessa de renda, saúde ou finanças.
- **{{ESCASSEZ}}** / **{{MOTIVO_REAL}}** — o limite (vagas, prazo, lote) e a prova de que é verdadeiro.
- **{{PRIVACIDADE}}** — consentimento, opt-out (STOP no SMS), base legal (LGPD/GDPR).
- **{{SETOR}}** — a regra setorial aplicável (Anvisa, CVM, OAB/CFM/CFC; FTC/CAN-SPAM/TCPA nos EUA; CDC no Brasil).
- **{{VEREDITO}}** — APROVADO, REPROVADO ou VETO; com o ponto de re-entrada se falha.

## O Template
```
# COMPLIANCE CHECKLIST — {{PECA}}
Owner: compliance-auditor · Data: {{DATA}}

## 1. CLAIM <-> PROVA (proof-to-claim-chain)
| Claim | Prova (id) | Resolve? | Veredito |
|-------|-----------|----------|----------|
| {{CLAIM_1}} | {{PROVA_REF_1}} | {{SIM/NAO}} | {{OK/VETO}} |
| {{CLAIM_2}} | {{PROVA_REF_2}} | {{SIM/NAO}} | {{OK/VETO}} |

## 2. DISCLAIMERS
Promessa de resultado? {{SIM/NAO}} — Disclaimer presente: {{DISCLAIMER}}
Saúde / financeiro, se aplicável: {{DISCLAIMER_SETOR}}

## 3. ESCASSEZ VERDADEIRA (truthful_scarcity)
Limite citado: {{ESCASSEZ}} · Motivo real e verificável: {{MOTIVO_REAL}}
Contador reinicia? {{NAO}} · "Últimas vagas" perpétuo? {{NAO}} · Deadline único p/ todos? {{SIM}}

## 4. PRIVACIDADE (LGPD / GDPR)
Consentimento explícito: {{SIM/NAO}} · Opt-out claro (STOP no SMS): {{SIM/NAO}} · Base legal: {{BASE}}

## 5. REGRAS DE SETOR (BR + EUA)
Setor: {{SETOR}} · Regra aplicada: {{REGRA}} · Conforme: {{SIM/NAO}}

## 6. VEREDITO
{{APROVADO | REPROVADO | VETO}} · Ponto de re-entrada: {{QUEM_CORRIGE}}
Override (só offerbook-chief, nunca p/ claim/escassez falsos): {{decision_id ou —}}
```

## Exemplo preenchido
> **# COMPLIANCE CHECKLIST — email-carrinho-aberto-01 (email)**
> Owner: compliance-auditor · Data: 2026-06-02
>
> **1. CLAIM <-> PROVA** —
> | Claim | Prova | Resolve? | Veredito |
> |---|---|---|---|
> | "+18% de receita recuperada em 30 dias" | proof-registry#PR-031 | Sim | OK |
> | "mediana +21% em 142 lojas" | proof-registry#PR-031 | Sim | OK |
>
> **2. DISCLAIMERS** — Promessa de resultado? Sim — Disclaimer presente: "resultados variam; não há garantia de ganho". Financeiro: não se aplica.
> **3. ESCASSEZ VERDADEIRA** — Limite: 40 vagas de setup feito-para-você. Motivo real: capacidade de implantação por turma. Contador reinicia? Não. "Últimas vagas" perpétuo? Não. Deadline único? Sim — sábado 23h59 para todos.
> **4. PRIVACIDADE** — Consentimento explícito: Sim (opt-in na inscrição). Opt-out claro: Sim (link de descadastro). Base legal: consentimento (LGPD).
> **5. REGRAS DE SETOR** — Setor: educação/serviços para e-commerce. Regra: CDC (oferta vincula; publicidade não enganosa) + FTC ("results not typical"). Conforme: Sim.
> **6. VEREDITO** — **APROVADO**. Ponto de re-entrada: não se aplica. Override: —.

## DoD do entregável
O checklist está pronto quando: (1) os 6 blocos estão preenchidos, sem `{{PLACEHOLDER}}` solto; (2) **todo** claim factual aponta para uma prova que resolve no [`proof-registry`](../../data/registries/proof-registry.md), satisfazendo o [`compliance-claim-backing-gate`](../../checklists/compliance/compliance-claim-backing-gate.md) — claim órfão é **veto** (`evidence_before_opinion`); (3) toda promessa de renda/saúde/finanças traz o disclaimer obrigatório, satisfazendo o [`compliance-disclaimers-gate`](../../checklists/compliance/compliance-disclaimers-gate.md); (4) a escassez é **100% verdadeira** — sem contador que reinicia, sem "últimas vagas" perpétuo, com deadline único e motivo real — satisfazendo o [`compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md) (`truthful_scarcity`); (5) a privacidade cumpre LGPD/GDPR (consentimento, opt-out, base legal), satisfazendo o [`compliance-data-privacy-gate`](../../checklists/compliance/compliance-data-privacy-gate.md); (6) as regras de setor (Anvisa/CVM/OAB-CFM-CFC; FTC/CAN-SPAM/TCPA; CDC) estão conferidas, satisfazendo o [`compliance-sector-rules-gate`](../../checklists/compliance/compliance-sector-rules-gate.md); (7) o veredito é binário e, no fail, nomeia quem corrige e o ponto de re-entrada. Override exige decisão registrada no [`decision-registry`](../../data/registries/decision-registry.md) pelo [`offerbook-chief`](../../agents/offerbook-chief.md) — **e nunca para claim ou escassez falsos**. O vínculo claim↔prova fica no [`claim-registry`](../../data/registries/claim-registry.md), e a peça passa no [`compliance-checklist`](../../checklists/compliance-checklist.md) antes de publicar.
