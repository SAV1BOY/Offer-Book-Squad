---
id: checklist.compliance.compliance-data-privacy-gate
title: "Gate — Privacidade de Dados (★ VETO: LGPD/FTC em cada captura)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [proof-to-claim-chain, scarcity-urgency-engine]
registries: [decision-registry, claim-registry]
tags: [gate, compliance, privacidade, lgpd, ftc, consentimento, veto, d7]
---

# Gate — Privacidade de Dados (★ VETO)

## Propósito
Este gate prova que **cada ponto de captura e rastreamento respeita a privacidade** — consentimento explícito (LGPD/GDPR), opt-out claro e disclosure de afiliação (FTC/CDC). É um dos cinco gates de **veto** do `compliance-auditor`. Ele existe porque coletar dado sem base legal, enviar SMS sem opt-out ou esconder uma relação de afiliado é violação direta de lei e quebra de confiança. A política exige consentimento explícito para coleta, opt-out claro em e-mail/SMS (STOP), base legal declarada, dados mínimos, e horário adequado de envio. Soma-se a disclosure de afiliação em cada peça de afiliado (FTC) e o consentimento para prova social/endosso de PR. Vale o princípio `traceability_before_eloquence`: cada captura tem base e aviso rastreáveis. Falha **veta** a peça até corrigir; o veto só cai por override registrado do `offerbook-chief`, nunca dispensando a lei.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (audita cada captura/rastreamento e **veta** a falha; `config.yaml: agents` veto=true). O `tech-links-deliverability-engineer` corrige a captura/opt-out na origem; o `offerbook-chief` arbitra override (sem dispensar a lei).
- **Artefato inspecionado:** cada ponto de captura do `funnel-map`, as regras de envio das `email-sms-sequences`, a disclosure do `affiliate-program` e o consentimento de prova social do `pr-plan`, sob a política [`compliance-policy`](../../docs/compliance-policy.md).

## Condição de Passagem
Cada ponto de captura tem aviso de privacidade e base de consentimento, cada canal tem opt-out claro, e cada peça de afiliado e endosso de PR tem disclosure e consentimento.

## Itens
1. **Consentimento na captura.** Verificar: cada formulário do `funnel-map` tem aviso de privacidade e base legal declarada (LGPD).
2. **Dados mínimos.** Verificar: a captura pede só os dados necessários, sem coleta excessiva.
3. **Opt-out em e-mail.** Verificar: cada e-mail tem descadastramento claro (CAN-SPAM/LGPD).
4. **Opt-out e horário em SMS.** Verificar: cada SMS traz opt-out (STOP) e respeita horário adequado (TCPA/LGPD).
5. **Disclosure de afiliação.** Verificar: cada peça de afiliado declara a relação (FTC/CDC), sem esconder o incentivo.
6. **Consentimento de prova social.** Verificar: depoimentos/endossos de PR têm permissão de uso do titular.
7. **Rastreamento avisado.** Verificar: pixels e rastreadores estão cobertos pelo aviso de privacidade.

## Evidência Exigida
Para marcar ✅: linkar o aviso de privacidade e a base legal por captura do `funnel-map` (itens 1–2), o opt-out de e-mail e SMS (itens 3–4), a disclosure por peça de afiliado (item 5) e o consentimento dos endossos de PR (item 6). O veredito aponta para o `decision-registry`.

## Protocolo de Falha
Captura sem consentimento, canal sem opt-out ou afiliado sem disclosure → **VETO** da peça; o `compliance-auditor` registra a violação no `decision-registry` e devolve a privacidade ao [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md), a disclosure ao dono do `affiliate-program`. A peça **não vai ao blackbook** até a captura ficar conforme. **Override:** só o [`offerbook-chief`](../../agents/offerbook-chief.md) arbitra, com decisão explícita gravada no `decision-registry` — e a lei nunca é dispensada (um override não autoriza coletar dado sem base legal). As regras setoriais específicas são tratadas no gate irmão de setor.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md)
- Política: [`compliance-policy`](../../docs/compliance-policy.md)
- Agentes: [`compliance-auditor`](../../agents/compliance-auditor.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`compliance-claim-backing-gate`](compliance-claim-backing-gate.md) · [`compliance-disclaimers-gate`](compliance-disclaimers-gate.md) · [`compliance-scarcity-truth-gate`](compliance-scarcity-truth-gate.md) · [`compliance-sector-rules-gate`](compliance-sector-rules-gate.md)
