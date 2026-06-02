---
id: project.full-launch-blackbook-project.12-compliance-and-blackbook-assembly
title: "Fase 12 — Compliance & Montagem do Blackbook (★ HARD STOP de Saída / DoD)"
type: project-phase
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
consumes:
  - artifact.offer-book
  - artifact.vsl-script
  - artifact.email-sms-sequences
  - artifact.mailers-inserts
  - artifact.ad-matrix
  - artifact.funnel-map
  - artifact.tech-deliverability-plan
  - artifact.run-of-show
  - artifact.events-calendar
  - artifact.asset-inventory-tracker
  - artifact.affiliate-program
  - artifact.pr-plan
  - data.registry.proof
  - data.registry.claim
produces:
  - decision.compliance-verdict
  - artifact.compliance-report
  - artifact.launch-blackbook
  - decision.blackbook-readiness
tags: [project-phase, qa, compliance, veto, blackbook, dod, hard-stop, lgpd, ftc, d7]
---

# Fase 12 — Compliance & Montagem do Blackbook (★ HARD STOP de Saída / DoD)

## Objetivo da Fase
Rodar a barreira final e montar o entregável. Primeiro, a auditoria de compliance veta o que violar três barreiras inegociáveis — todo claim tem lastro, toda escassez/urgência é 100% real, e a captura/rastreamento respeita a privacidade (LGPD/FTC). Só com o veredito APROVADO, monta-se o Launch Blackbook: um pacote único, navegável e completo que passa no **★ HARD STOP de saída** — o `blackbook-stack/blackbook-dod-gate`. O estado-pronto é o blackbook que um operador executa sem precisar perguntar nada, com cada claim ligado a prova, cada escassez ligada a inventário real e cada fase com dono e fallback. Este HARD STOP é o espelho do de entrada: assim como nenhuma copy nasceu antes do Offer Book DoD, nenhum lançamento é entregue antes do Blackbook DoD.

## Critério de Entrada
Todas as fases anteriores entregaram seus artefatos aprovados: o `artifact.offer-book` (Fase 01), a copy aprovada na voz (Fases 02-05), o funil e o tech-plan (Fases 06-07), o run-of-show, o events-calendar e o asset-inventory-tracker (Fases 08-09), o `artifact.affiliate-program` (Fase 10) e o `artifact.pr-plan` (Fase 11). Os registries [`proof-registry`](../../data/registries/proof-registry.md) e [`claim-registry`](../../data/registries/claim-registry.md) trazem o lastro catalogado — a cadeia claim→prova é a régua. Pré-condição: a copy já passou no voice-pass. Conforme `config.yaml: defaults.mandatory_compliance_audit: true`, nenhum lançamento publica sem o veredito APROVADO; e a montagem do blackbook só roda com esse APROVADO. Os registries [`decision-registry`](../../data/registries/decision-registry.md), [`claim-registry`](../../data/registries/claim-registry.md) e [`offer-registry`](../../data/registries/offer-registry.md) são escritos.

## Agentes & Tasks
- **Task [`compliance-audit`](../../tasks/qa-memory/compliance-audit.md)** — dono [`compliance-auditor`](../../agents/compliance-auditor.md), a última barreira, com poder de **VETO**. Co-roda com o [`offerbook-chief`](../../agents/offerbook-chief.md), que arbitra overrides.
- **Task [`assemble-blackbook`](../../tasks/qa-memory/assemble-blackbook.md)** — dono [`compliance-auditor`](../../agents/compliance-auditor.md) co-rodando com o [`offerbook-chief`](../../agents/offerbook-chief.md), que assina a prontidão final.

## Passos
1. Carregue a régua (claim-registry + proof-registry) e prepare a cadeia [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md).
2. Audite o lastro de cada claim (barreira 1): claim sem prova, prova fraca ou promessa infalsificável vira VETO.
3. Audite a verdade da escassez (barreira 2) com [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md), cruzando com o asset-inventory-tracker e o run-of-show: deadline que se renova ou "últimas vagas" sem número real vira VETO.
4. Audite a privacidade/dados (barreira 3): aviso de privacidade e consentimento (LGPD), disclosure de afiliação (FTC), prova social de PR consentida. Falha vira VETO.
5. Consolide o veredito de compliance: APROVADO ou VETADO com a violação, a peça/linha e o ponto de re-entrada. Override só com decisão registrada do chief.
6. Com APROVADO, abra o esqueleto do blackbook e mapeie cada artefato à sua seção com [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md), garantindo uma história coerente.
7. Verifique completude (zero stub, zero pendente, zero link quebrado), rastreabilidade ponta a ponta e navegabilidade (um operador executa só com o blackbook).
8. Rode o `blackbook-stack/blackbook-dod-gate` e o `chief/chief-blackbook-readiness-gate`; self-verify com red-team; confirme o status final no `offer-registry` e emita o `blackbook-readiness`.

## Artefatos Produzidos
- `decision.compliance-verdict` — APROVADO ou VETADO, com resumo de violações por barreira.
- `artifact.compliance-report` — cada item binário, com evidência e ponto de re-entrada.
- `artifact.launch-blackbook` — o entregável final navegável com todas as seções e cross-links.
- `decision.blackbook-readiness` — APROVADO com evidência dos dois gates, ou a lista de lacunas.
- Registries escritos: [`decision-registry`](../../data/registries/decision-registry.md), [`claim-registry`](../../data/registries/claim-registry.md) e [`offer-registry`](../../data/registries/offer-registry.md).

## Gates
- [`compliance/compliance-claim-backing-gate`](../../checklists/compliance/compliance-claim-backing-gate.md) · [`compliance/compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md) · [`compliance/compliance-data-privacy-gate`](../../checklists/compliance/compliance-data-privacy-gate.md)
- [`blackbook-stack/blackbook-dod-gate`](../../checklists/blackbook-stack/blackbook-dod-gate.md) — **★ HARD STOP de saída**.
- [`chief/chief-blackbook-readiness-gate`](../../checklists/chief/chief-blackbook-readiness-gate.md)

## Critério de Saída
Cada claim de cada peça está ligado a uma prova catalogada; cada escassez está confirmada como real contra o inventário; cada captura está conforme (LGPD/FTC); os três gates de compliance estão verdes e o veredito é APROVADO. Sobre esse aprovado, o blackbook está montado: cada seção presente com seu artefato-fonte (zero stub), a história fecha ponta a ponta, e é executável por um operador só com ele; o `blackbook-stack/blackbook-dod-gate` e o `chief-blackbook-readiness-gate` estão verdes. Estado terminal: APROVADO (entrega liberada) ou VETADO/lacuna (devolve ao dono do defeito). A próxima fase é a [`13-memory-update`](13-memory-update.md), que extrai do blackbook fechado o que vira memória reutilizável.
