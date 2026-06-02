---
id: task.copy.write-mailers-inserts
title: "Task — Escrever Mala Direta & Inserts Físicos"
type: task
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: direct-mail-insert-writer
consumes:
  - artifact.offer-book
  - artifact.big-idea
  - artifact.positioning
  - decision.lead-type-locked
  - artifact.offer-stack
  - artifact.guarantee
  - artifact.money-model
  - data.registry.proof
  - data.registry.objection
produces:
  - artifact.mailers-inserts
frameworks: [offer-stack-builder, scarcity-urgency-engine]
checklists:
  - offer-book-stack/offer-book-dod-gate
  - mailer-checklist
registries: [control-registry]
metrics: [opt_in_rate, upsell_take_rate, copy_throughput]
tags: [copy, direct-mail, mailer, insert, save-the-date, qr-code, specs, hard-stop]
---

# Task — Escrever a mala direta e os inserts físicos por degrau de compra

## Objetivo
Transformar o Offer Book aprovado em peças físicas — mailers de save-the-date, mailers com QR que levam ao funil, e inserts por degrau de compra (front-end, upsell, downsell, continuidade) — cada peça com copy E specs de produção, convertendo um toque físico em um passo digital. O estado-pronto: cada peça com gancho, oferta resumida, objeção respondida, CTA físico→digital coordenado, specs completas, urgência real, aprovada no mailer-checklist e encaminhada ao [`voice-pass`](voice-pass.md).

## Agente dono
[`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md). Materializa a estratégia em papel. Sem poder de veto; submete tudo ao voice-guardian.

## Gatilho / Quando
**HARD STOP: esta task de copy (D4) só ativa APÓS o [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) estar APROVADO.** Conforme `config.yaml: defaults.hard_stop_before_copy: true` e o [`ARCHITECTURE.md`](../../ARCHITECTURE.md), nenhuma palavra de copy nasce antes de o Offer Book passar no Definition of Done. Gate vermelho → o agente **recusa** e devolve ao [`offerbook-chief`](../../agents/offerbook-chief.md). Demais gatilhos: pedido de mailer (save-the-date / QR) ou de inserts por degrau, com a camada D3 fechada (Big Idea + posição + **lead travados**) e a **escada do money model definida** (o insert depende do degrau).

## Inputs (Consome)
- `artifact.offer-book` — o pacote estratégico aprovado (fonte de verdade).
- `artifact.big-idea` + `artifact.positioning` + `decision.lead-type-locked` — tese, posição e o **lead travado** (o mailer abre pelo lead; o espaço é escasso, o gancho precisa parar a mão).
- `artifact.money-model` — os **degraus** (front-end → upsell → downsell → continuidade). Cada insert é específico do degrau onde o cliente comprou.
- `artifact.offer-stack` + `artifact.guarantee` — componentes e reversão de risco a relembrar.
- [`data.registry.proof`](../../data/registries/proof-registry.md) — prova por claim. **Peça física também não carrega claim sem lastro.**
- [`data.registry.objection`](../../data/registries/objection-registry.md) — a objeção dominante do degrau.
- **URLs/QR** coordenados com o [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) (ou marca `[URL/QR PENDENTE]`).

## Procedimento
1. **Verificar o HARD STOP.** Confirmar o `offer-book-dod-gate` verde. Vermelho → recusar e devolver ao chief.
2. **Carregar inputs e confirmar a escada.** Sem a escada do money model, parar — não há como ramificar inserts por degrau. Sem ela, pedir ao [`money-model-designer`](../../agents/money-model-designer.md).
3. **Decompor por tipo de peça.** Save-the-date (antecipação + data + QR de registro) · mailer com QR (gancho do lead → oferta resumida → QR para a página) · inserts por degrau (front-end: boas-vindas + ativação + ascensão; upsell/downsell: parabeniza + próximo degrau + prazo; continuidade: pertencimento + valor recorrente + redução de churn).
4. **Abrir cada peça pelo lead travado.** Um gancho de uma linha que cabe no envelope/frente; o verso/miolo responde a objeção do degrau e ancora a prova; o QR leva à página onde a oferta completa mora.
5. **Empilhar a oferta no espaço físico.** Usar [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) para condensar o stack ao que cabe na peça.
6. **Aplicar urgência verdadeira.** Usar [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md): prazo do save-the-date, validade do insert. Toda urgência impressa **tem de ser real** — papel postado não se corrige. Urgência falsa → sinalizar ao chief; não imprimir.
7. **Especificar produção.** Para cada peça: formato, dimensões (mm), dobras, sangria (3 mm), tamanho e quiet zone do QR (fora de dobra, com contraste), cores, e o CTA físico→digital (QR primário, URL curta vanity como fallback). Coordenar URL/UTM com o tech-engineer.
8. **Ramificar por degrau (ToT).** Gerar ≥3 formatos (postal, carta dobrada, dimensional) e pontuar por cut-through, custo e fit com o degrau. Dimensional só quando o LTV do degrau paga o custo. Cada upsell só entra se o [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) validou a margem.
9. **Self-verify (Bloom + red-team).** Checar: insert no degrau correto? QR fora de dobra com quiet zone? Specs completas? Urgência real? CTA único e de baixa fricção? Antecipar o veto do compliance (urgência falsa, claim sem lastro) e do voice-guardian.
10. **Registrar e encaminhar.** Logar cada peça no `control-registry` e entregar ao voice-pass.

## Frameworks
[`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md).

## Outputs (Produz)
- `artifact.mailers-inserts` (template em [`copy/mailers-inserts-template`](../../templates/copy/mailers-inserts-template.md)).
- [`control-registry`](../../data/registries/control-registry.md) atualizado com cada peça (`asset_id`, tipo, degrau, `gancho_frente`, oferta resumida, objeção-alvo, `cta_fisico_digital` {tipo, destino/UTM, fallback}, specs {formato, dimensões, dobras, sangria, qr_mm, quiet_zone, cores}, `urgencia_real: true`, `status: draft`).

## Definition of Done
- HARD STOP verde (offer-book-dod-gate aprovado) **antes** de qualquer linha.
- Cada peça mapeia um tipo e, no insert, o **degrau correto** da escada.
- Cada peça tem copy **e** specs completas (formato, dimensões, sangria, QR, CTA).
- QR fora de dobra, com quiet zone e contraste; URL/UTM coordenada.
- Cada claim com prova linkada; urgência impressa **real**; CTA físico→digital único.
- Mailer-checklist verde; peças registradas no `control-registry` e encaminhadas ao voice-pass.

## Gates
[`mailer-checklist`](../../checklists/mailer-checklist.md). Gate de entrada (HARD STOP): [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).

## Métricas
Move KPIs da família **conversion** ([`config.yaml`](../../config.yaml) `kpis:`), por converter um toque físico em um passo digital por degrau:
- **`opt_in_rate`** — o save-the-date e o mailer com QR levam ao funil/registro, alimentando a taxa de optin a partir do canal físico.
- **`upsell_take_rate`** — os inserts por degrau (upsell/downsell/continuidade) ascendem o cliente ao próximo passo, movendo a take rate.
- **`copy_throughput`** — cada peça física aprovada (copy + specs) conta na vazão de copy.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (família conversion), com cada peça em [`control-registry`](../../data/registries/control-registry.md).

## Handoff
**Próxima task:** [`voice-pass`](voice-pass.md) (passe obrigatório do voice-style-guardian). **Contrato de saída:** cada peça tem copy + specs de produção completas, QR/CTA físico→digital coordenado, urgência real e (no insert) o degrau correto — pronta para o guardião e, após o veredito APROVADO, para o [`funnel-architect`](../funnel-tech/map-funnel.md) (destinos dos QR → páginas), o [`tech-links-deliverability-engineer`](../funnel-tech/plan-tech-deliverability.md) (URLs/UTM → rastreio) e o [`events-logistics-coordinator`](../ops/build-events-logistics.md) (save-the-date → logística do evento).
