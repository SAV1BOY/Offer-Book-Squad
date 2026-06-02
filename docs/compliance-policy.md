---
id: doc.compliance-policy
title: "Política de Compliance — Claims, Escassez, Privacidade, Setor"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [proof-to-claim-chain, scarcity-urgency-engine]
checklists: [compliance/compliance-claim-backing-gate, compliance/compliance-scarcity-truth-gate, compliance/compliance-data-privacy-gate]
tags: [compliance, claims, scarcity, lgpd, ftc, cdc, ethics]
---

# Política de Compliance

Esta política é **vinculante** para todo artefato do squad. O [`compliance-auditor`](../agents/compliance-auditor.md) é a última barreira e pode **vetar** a entrega. Compliance não é detalhe — escassez falsa e claim sem lastro destroem LTV, marca e expõem a risco legal.

## 1. Princípio

Vender a verdade, com força. Toda alavanca de persuasão do squad (prova, escassez, garantia, ancoragem) só é usada quando é **real**. O princípio `truthful_scarcity` é não-negociável.

## 2. Claims & Prova

- **Todo claim aponta para uma prova** (princípio `evidence_before_opinion` + framework [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md)).
- Claim sem prova → **veto** (gate [`compliance/compliance-claim-backing-gate`](../checklists/compliance/compliance-claim-backing-gate.md)).
- Prova registrada no [`proof-registry`](../data/registries/proof-registry.md); o vínculo claim↔prova no [`claim-registry`](../data/registries/claim-registry.md).
- Resultados atípicos exigem **disclaimer** ("resultados variam; não há garantia de ganho").

## 3. Escassez & Urgência (100% verdadeiras)

- Quantidade, prazo e bônus de escassez precisam ser **reais e verificáveis**.
- Contador que reinicia, "últimas vagas" perpétuo, falso lote → **veto** (gate [`compliance/compliance-scarcity-truth-gate`](../checklists/compliance/compliance-scarcity-truth-gate.md)).
- Ver [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md).

## 4. Garantias

- A garantia precisa ser **exequível** pela operação (ver [`guarantee-types`](../lib/taxonomies/guarantee-types.md)).
- Garantia que a operação não honra → veto.

## 5. Disclaimers obrigatórios

- **Renda/resultado:** quando há promessa de ganho ou transformação.
- **Saúde:** sem promessa de cura; "não substitui orientação profissional".
- **Financeiro:** "não é recomendação de investimento; rentabilidade passada não garante futura".

## 6. Privacidade (LGPD / GDPR)

- Consentimento explícito para coleta; opt-out claro em e-mail/SMS.
- Base legal declarada; dados mínimos necessários.
- SMS: opt-out (STOP) e horário adequado (gate de privacidade [`compliance/compliance-data-privacy-gate`](../checklists/compliance/compliance-data-privacy-gate.md)).

## 7. Regras setoriais (Brasil + EUA)

- **Saúde/suplementos:** Anvisa; sem alegação de doença/cura.
- **Finanças/investimentos:** CVM; educação ≠ recomendação.
- **Serviços profissionais:** códigos de ética (OAB/CFM/CFC) — sem garantia de resultado.
- **EUA:** FTC (endorsements, "results not typical"), CAN-SPAM, TCPA. **Brasil:** CDC (oferta vincula; publicidade não enganosa).

## 8. Anti-plágio & citação

- Estrutura e princípios em **redação original**; citação literal **≤ 25 palavras**, atribuída.
- Nenhuma copy protegida reproduzida na íntegra. Proveniência em [`swipe-sources/attribution-log.md`](../swipe-sources/attribution-log.md). Enforçado por `scripts/citation-checker.py`.

## 9. O veto do compliance-auditor

O `compliance-auditor` roda no D7 (gate final do Blackbook) e pode parar a entrega por: claim sem lastro · escassez/urgência falsa · garantia inexequível · disclaimer ausente · violação setorial · violação de privacidade. Override exige decisão registrada no [`decision-registry`](../data/registries/decision-registry.md) pelo [`offerbook-chief`](../agents/offerbook-chief.md) — e nunca para claims/escassez falsos (esses não têm override).
