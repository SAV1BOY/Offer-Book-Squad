---
id: task.qa-memory.compliance-audit
title: "Task — Auditoria de Compliance (★ VETO)"
type: task
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
  - artifact.run-of-show
  - artifact.asset-inventory-tracker
  - artifact.affiliate-program
  - artifact.pr-plan
  - data.registry.proof
  - data.registry.claim
produces:
  - decision.compliance-verdict
  - artifact.compliance-report
frameworks: [proof-to-claim-chain, scarcity-urgency-engine]
checklists:
  - compliance/compliance-claim-backing-gate
  - compliance/compliance-scarcity-truth-gate
  - compliance/compliance-data-privacy-gate
registries: [decision-registry, claim-registry]
tags: [qa, compliance, veto, claim-backing, escassez-real, lgpd, ftc, hard-stop, d7]
---

# Task — Auditoria de compliance: a última barreira que VETA claim sem lastro e escassez falsa

## Objetivo
Auditar cada peça do lançamento contra três barreiras inegociáveis — todo claim tem lastro, toda escassez/urgência é 100% real, e a captura/rastreamento respeita a privacidade (LGPD/FTC) — e emitir UM veredito com poder de **VETO**. O estado-pronto: cada claim ligado a uma prova catalogada, cada deadline/limite batendo com a realidade, cada captura com aviso de privacidade — APROVADO; ou VETADO com a lista exata de violações e o ponto de re-entrada.

## Agente dono
[`compliance-auditor`](../../agents/compliance-auditor.md). É a **última barreira** do pipeline e **pode VETAR** (conforme `config.yaml: agents` veto=true e o [`ARCHITECTURE.md`](../../ARCHITECTURE.md): "Compliance Auditor é a última barreira e pode vetar claim sem lastro ou escassez falsa"). Co-roda com o [`offerbook-chief`](../../agents/offerbook-chief.md), que arbitra overrides.

## Gatilho / Quando
Roda em D7, **depois** que a copy (D4, já aprovada na voz via [`voice-pass`](../copy/voice-pass.md)), o funil (D5) e as ops/growth (D6) entregaram seus artefatos. É gate obrigatório de toda composição que vende (`run-full-launch`, `run-single-promo`, `run-enterprise-deal-book`). Conforme `config.yaml: defaults.mandatory_compliance_audit: true`. Nenhum lançamento publica sem este veredito APROVADO.

## Inputs (Consome)
- `artifact.offer-book` — a promessa, a garantia e os limites declarados.
- `artifact.vsl-script` / `artifact.email-sms-sequences` / `artifact.mailers-inserts` / `artifact.ad-matrix` — **cada claim** e **cada gatilho de escassez** nas peças de copy.
- `artifact.funnel-map` — garantia/T&C por página; pontos de captura de dados.
- `artifact.run-of-show` + `artifact.asset-inventory-tracker` — os deadlines/limites agendados e o inventário real que deve sustentá-los.
- `artifact.affiliate-program` + `artifact.pr-plan` — claims e disclosure de afiliados; prova social/endossos de PR (consentimento).
- [`data.registry.proof`](../../data/registries/proof-registry.md) + [`data.registry.claim`](../../data/registries/claim-registry.md) — o lastro catalogado por claim. **A cadeia claim→prova é a régua.**

## Procedimento
1. **Carregar a régua.** Ler o claim-registry e o proof-registry; preparar a cadeia [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md).
2. **Auditar o lastro de cada claim (barreira 1).** Para **cada** claim em cada peça, exigir uma prova catalogada ligada. Claim sem prova, prova fraca, ou promessa de resultado infalsificável → **VETO** do claim. Registrar `{peça, linha, claim, prova_ausente}`.
3. **Auditar a verdade da escassez (barreira 2).** Para **cada** deadline, "últimas vagas", lote ou contagem regressiva, aplicar [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) e cruzar com o `asset-inventory-tracker` e o `run-of-show`: o limite bate com um número real? O deadline de fato fecha? Deadline que se renova sozinho, "últimas 50 vagas" sem 50 no tracker, urgência inventada → **VETO da escassez falsa**.
4. **Auditar a privacidade/dados (barreira 3).** Cada ponto de captura/rastreamento tem aviso de privacidade e base de consentimento (LGPD)? Disclosure de afiliação (FTC/CDC) presente em cada peça de afiliado? Prova social/endosso de PR com consentimento/permissão? Falha → **VETO** até corrigir.
5. **Checar T&Cs e disclaimers.** Garantia visível antes do preço; disclaimers obrigatórios presentes; FAQ coerente com a oferta.
6. **Consolidar o veredito.** Os três gates passam? Qualquer barreira violada → **VETADO** + relatório com a violação, a peça/linha e o ponto de re-entrada (quem corrige). Não há "aprovado com ressalvas" em claim/escassez.
7. **Tratar override.** Conflito legítimo (ex.: disclaimer que o voice-guardian não pôde acomodar) → o [`offerbook-chief`](../../agents/offerbook-chief.md) arbitra e registra o override no `decision-registry`. Override sem registro não existe; a lei nunca é dispensada.
8. **Registrar e devolver/liberar.** Logar o veredito e cada violação no `decision-registry`; atualizar o `claim-registry` com o status de lastro. VETADO → devolver ao autor responsável (copy → voice-pass/autor; escassez → [`launch-producer`](../../agents/launch-producer.md)/[`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md); privacidade → [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md)). APROVADO → liberar para a montagem do blackbook.

## Frameworks
[`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md).

## Outputs (Produz)
- `decision.compliance-verdict` — APROVADO | VETADO, com o resumo de violações por barreira.
- `artifact.compliance-report` (template em [`qa/compliance-checklist-template`](../../templates/qa/compliance-checklist-template.md); FAQ em [`qa/faq-template`](../../templates/qa/faq-template.md)) — cada item binário, com evidência e ponto de re-entrada.
- [`decision-registry`](../../data/registries/decision-registry.md) atualizado (veredito, violações, overrides) e [`claim-registry`](../../data/registries/claim-registry.md) atualizado (status de lastro por claim).

## Definition of Done
- **Cada** claim de **cada** peça ligado a uma prova catalogada (zero claim sem lastro).
- **Cada** escassez/urgência cruzada com inventário/run-of-show e confirmada como **real** (zero deadline/limite falso).
- **Cada** ponto de captura com aviso de privacidade/consentimento (LGPD); disclosure de afiliação (FTC) em cada peça de afiliado; prova social de PR consentida.
- T&Cs e disclaimers presentes; garantia visível antes do preço.
- Os três gates de compliance verdes; veredito e violações registrados; overrides (se houver) registrados pelo chief.

## Gates
[`compliance/compliance-claim-backing-gate`](../../checklists/compliance/compliance-claim-backing-gate.md) · [`compliance/compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md) · [`compliance/compliance-data-privacy-gate`](../../checklists/compliance/compliance-data-privacy-gate.md).

## Handoff
**Veto e devolução:** peça VETADA volta ao dono do defeito com o ponto de re-entrada nomeado — copy ao autor via [`voice-pass`](../copy/voice-pass.md), escassez ao [`launch-producer`](../ops/build-run-of-show.md) ou [`events-logistics-coordinator`](../ops/build-events-logistics.md), privacidade ao [`plan-tech-deliverability`](../funnel-tech/plan-tech-deliverability.md). **Próxima task (só com veredito APROVADO):** [`assemble-blackbook`](assemble-blackbook.md). **Contrato:** o blackbook só monta sobre material com compliance APROVADO — cada claim lastreado, cada escassez real, cada captura conforme. O veto é absoluto; só o chief libera, com decisão explícita e registrada.
