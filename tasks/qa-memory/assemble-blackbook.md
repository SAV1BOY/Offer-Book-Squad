---
id: task.qa-memory.assemble-blackbook
title: "Task — Montar o Launch Blackbook (★ Blackbook DoD)"
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
  - artifact.tech-deliverability-plan
  - artifact.run-of-show
  - artifact.events-calendar
  - artifact.affiliate-program
  - artifact.pr-plan
  - decision.compliance-verdict
produces:
  - artifact.launch-blackbook
  - decision.blackbook-readiness
frameworks: [offer-to-funnel-mapping]
checklists:
  - blackbook-stack/blackbook-dod-gate
  - chief/chief-blackbook-readiness-gate
registries: [offer-registry]
metrics: [time_to_blackbook, compliance_pass_rate, registry_currency]
tags: [qa, blackbook, dod, montagem, entregavel-final, hard-stop, d7]
---

# Task — Montar o Launch Blackbook: o entregável final navegável, completo e auditado

## Objetivo
Reunir todos os artefatos aprovados do lançamento — Offer Book, copy, funil, tech, run-of-show, eventos, afiliados, PR — num **Launch Blackbook** único, navegável e completo, que passe no Blackbook Definition of Done. O estado-pronto: o blackbook montado, cada seção presente e ligada ao seu artefato-fonte, o compliance APROVADO, e os dois gates (blackbook-dod + chief-blackbook-readiness) verdes — o pacote que um operador executa sem precisar perguntar nada.

## Agente dono
[`compliance-auditor`](../../agents/compliance-auditor.md), co-rodando com o [`offerbook-chief`](../../agents/offerbook-chief.md). O auditor garante que nada entra no blackbook sem estar conforme; o chief assina a prontidão final.

## Gatilho / Quando
Roda em D7, **depois** da [`compliance-audit`](compliance-audit.md): ativa **somente** quando o `decision.compliance-verdict` é APROVADO. É o **HARD STOP de saída** — espelho do HARD STOP de entrada (offer-book-dod-gate): assim como nenhuma copy nasce antes do Offer Book passar no DoD, nenhum lançamento é entregue antes do blackbook passar no [`blackbook-stack/blackbook-dod-gate`](../../checklists/blackbook-stack/blackbook-dod-gate.md). Compliance vetado → **não montar**; devolver à [`compliance-audit`](compliance-audit.md) com as violações pendentes.

## Inputs (Consome)
- `decision.compliance-verdict` — **deve ser APROVADO**. É o portão de entrada.
- `artifact.offer-book` — o núcleo estratégico (mercado, avatar, mecanismo, valor, money model, big idea, posição).
- `artifact.vsl-script` / `artifact.email-sms-sequences` / `artifact.mailers-inserts` / `artifact.ad-matrix` — toda a copy aprovada na voz e no compliance.
- `artifact.funnel-map` + `artifact.tech-deliverability-plan` — o funil e o plano técnico/deliverability/fallback.
- `artifact.run-of-show` + `artifact.events-calendar` — o calendário datado, a logística e o inventário.
- `artifact.affiliate-program` + `artifact.pr-plan` — o programa de afiliados e o plano de PR.

## Procedimento
1. **Confirmar o HARD STOP de saída.** `compliance-verdict` APROVADO. Vetado → não montar; devolver à compliance-audit.
2. **Abrir o esqueleto do blackbook.** A partir de [`core/launch-blackbook-skeleton`](../../templates/core/launch-blackbook-skeleton.md), instanciar as seções: Offer Book, Copy, Funil & Tech, Run-of-Show & Eventos, Afiliados, PR, Compliance.
3. **Mapear cada artefato à sua seção.** Aplicar [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) para garantir que a oferta, a copy, o funil e a execução contam **uma história coerente** — cada peça de copy aponta para a página certa, cada página para o degrau certo do money model.
4. **Verificar completude (sem stubs).** Cada seção tem o artefato-fonte presente e ligado; nenhum `[PENDENTE]`, nenhum link quebrado, nenhum placeholder. Seção faltante → marcar a lacuna e acionar o dono do artefato.
5. **Verificar a rastreabilidade ponta a ponta.** Cada claim → prova; cada escassez → inventário real; cada página → CTA único; cada fase → dono e fallback. O blackbook carrega o veredito de compliance e os vereditos de voz por peça.
6. **Verificar a navegabilidade.** Um operador consegue executar o lançamento só com o blackbook? Índice, ordem das seções e cross-links resolvem sem ambiguidade.
7. **Rodar o Blackbook DoD.** Passar no [`blackbook-stack/blackbook-dod-gate`](../../checklists/blackbook-stack/blackbook-dod-gate.md): completude (todas as seções), coerência (a história fecha), conformidade (compliance APROVADO), executabilidade (datas, donos, fallbacks, URLs). Depois, a prontidão final no [`chief/chief-blackbook-readiness-gate`](../../checklists/chief/chief-blackbook-readiness-gate.md).
8. **Self-verify (red-team).** "Falta alguma peça para alguém lançar isto amanhã?" "Algum claim/escassez entrou sem o aval do compliance?" Corrigir antes de declarar pronto.
9. **Registrar e entregar.** Confirmar no `offer-registry` o status final das ofertas; emitir o `blackbook-readiness` e entregar à [`memory-update`](memory-update.md). Máximo de 2 ciclos antes de escalar ao chief.

## Frameworks
[`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md).

## Outputs (Produz)
- `artifact.launch-blackbook` (esqueleto em [`core/launch-blackbook-skeleton`](../../templates/core/launch-blackbook-skeleton.md)) — o entregável final navegável com todas as seções e cross-links.
- `decision.blackbook-readiness` — APROVADO com evidência dos dois gates, ou a lista de lacunas.
- [`offer-registry`](../../data/registries/offer-registry.md) atualizado com o status final das ofertas.

## Definition of Done
- `compliance-verdict` APROVADO confirmado antes da montagem (HARD STOP de saída).
- Cada seção do blackbook presente, com o artefato-fonte ligado (zero stub, zero `[PENDENTE]`, zero link quebrado).
- A história fecha: cada claim→prova, cada escassez→inventário real, cada página→CTA único, cada fase→dono e fallback.
- O blackbook é executável por um operador só com ele; índice e cross-links resolvem.
- O `blackbook-stack/blackbook-dod-gate` e o `chief/chief-blackbook-readiness-gate` verdes; status final no `offer-registry`.

## Gates
[`blackbook-stack/blackbook-dod-gate`](../../checklists/blackbook-stack/blackbook-dod-gate.md) · [`chief/chief-blackbook-readiness-gate`](../../checklists/chief/chief-blackbook-readiness-gate.md).

## Métricas
Move KPIs de **efficiency** e **operational** ([`config.yaml`](../../config.yaml) `kpis:`), por ser o ★ HARD STOP de saída que fecha o entregável final:
- **`time_to_blackbook`** — esta task **fecha o relógio** do KPI (dias até o Blackbook completo); o `blackbook-readiness` APROVADO é o marco medido.
- **`compliance_pass_rate`** — só monta sobre `compliance-verdict` APROVADO; nada com claim sem lastro ou escassez falsa entra no pacote final.
- **`registry_currency`** — confirmar o status final das ofertas no `offer-registry` na entrega mantém o registro atualizado no fechamento.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (famílias efficiency e operational), com o status final em [`offer-registry`](../../data/registries/offer-registry.md).

## Handoff
**Próxima task:** [`memory-update`](memory-update.md) — dono [`knowledge-librarian`](../../agents/knowledge-librarian.md). **Contrato:** a memória recebe o blackbook fechado e aprovado para extrair o que vira reutilizável — controles vencedores, swipe, lições aprendidas. **Garantia:** o blackbook entregue é completo, coerente, conforme (compliance APROVADO) e executável — o pacote final do lançamento, sem peça faltando e sem nada que o compliance não tenha liberado.
