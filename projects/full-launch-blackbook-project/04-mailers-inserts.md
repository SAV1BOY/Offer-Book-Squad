---
id: project.full-launch-blackbook-project.04-mailers-inserts
title: "Fase 04 — Mala Direta & Inserts Físicos"
type: project-phase
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
  - artifact.money-model
  - artifact.offer-stack
  - artifact.guarantee
  - data.registry.proof
  - data.registry.objection
produces:
  - artifact.mailers-inserts
  - decision.voice-verdict
tags: [project-phase, copy, direct-mail, mailer, insert, qr-code, specs, hard-stop, d4]
---

# Fase 04 — Mala Direta & Inserts Físicos

## Objetivo da Fase
Transformar o Offer Book aprovado em peças físicas — mailers de save-the-date, mailers com QR que levam ao funil, e inserts por degrau de compra (front-end, upsell, downsell, continuidade) — cada peça com copy E specs de produção, convertendo um toque físico em um passo digital. O estado-pronto é cada peça com gancho, oferta resumida, objeção respondida, CTA físico→digital coordenado, specs completas (formato, dimensões, sangria, QR, quiet zone) e urgência real, aprovada no mailer-checklist e no veredito de voz. Papel postado não se corrige — por isso a urgência impressa tem de ser real.

## Critério de Entrada
A Fase 01 entrega o `artifact.offer-book` aprovado (HARD STOP VERDE). A Fase 06 do offer-book (incorporada na Fase 01) entrega o `artifact.money-model` com a escada definida — o insert depende do degrau onde o cliente comprou. Junto vêm a Big Idea, o positioning, o `decision.lead-type-locked`, o `artifact.offer-stack`, o `artifact.guarantee` e os registries [`proof-registry`](../../data/registries/proof-registry.md) e [`objection-registry`](../../data/registries/objection-registry.md). As URLs/QR vêm coordenadas com o tech-engineer (ou marcadas pendentes). Pré-condição: o `offer-book-dod-gate` está APROVADO e a escada do money model está definida — sem ela, não há como ramificar inserts por degrau. O [`control-registry`](../../data/registries/control-registry.md) é escrito.

## Agentes & Tasks
- **Task [`write-mailers-inserts`](../../tasks/copy/write-mailers-inserts.md)** — dono [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md). Materializa a estratégia em papel. Sem poder de veto; submete ao guardião.
- **Task [`voice-pass`](../../tasks/copy/voice-pass.md)** — dono [`voice-style-guardian`](../../agents/voice-style-guardian.md). Passe obrigatório de voz.

## Passos
1. Verifique o HARD STOP e confirme a escada do money model. Sem a escada, pare e peça ao money-model-designer.
2. Decomponha por tipo de peça: save-the-date, mailer com QR, inserts por degrau (front-end: boas-vindas + ativação; upsell/downsell: parabeniza + próximo degrau + prazo; continuidade: pertencimento + redução de churn).
3. Abra cada peça pelo lead travado: um gancho de uma linha; o miolo responde a objeção do degrau e ancora a prova; o QR leva à página.
4. Empilhe a oferta no espaço físico com [`offer-stack-builder`](../../frameworks/offer-stack-builder.md).
5. Aplique urgência verdadeira com [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md): prazo do save-the-date, validade do insert — sempre reais.
6. Especifique produção: formato, dimensões em mm, dobras, sangria 3 mm, tamanho e quiet zone do QR (fora de dobra, com contraste), cores e o CTA físico→digital (QR primário, URL vanity de fallback). Coordene UTM com o tech-engineer.
7. Ramifique por degrau com Tree-of-Thoughts (≥3 formatos pontuados por cut-through, custo e fit). Dimensional só quando o LTV do degrau paga o custo.
8. Self-verify com red-team (insert no degrau certo? QR fora de dobra? specs completas? urgência real?); registre no `control-registry` e encaminhe ao voice-pass.

## Artefatos Produzidos
- `artifact.mailers-inserts` — cada peça com tipo, degrau, gancho de frente, oferta resumida, objeção-alvo, CTA físico→digital, specs e urgência real.
- `decision.voice-verdict` — APROVADO por peça.
- Registry escrito: [`control-registry`](../../data/registries/control-registry.md).

## Gates
- [`mailer-checklist`](../../checklists/mailer/mailer-checklist.md)
- Os quatro gates de voz via [`voice/voice-checklist`](../../checklists/voice/voice-checklist.md).
- Gate de entrada (HARD STOP): [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).

## Critério de Saída
Cada peça mapeia um tipo e, no insert, o degrau correto da escada; cada peça tem copy E specs completas; o QR fica fora de dobra com quiet zone e contraste; a URL/UTM está coordenada; cada claim tem prova linkada; a urgência impressa é real; o CTA físico→digital é único; o mailer-checklist está verde e o veredito de voz é APROVADO. A próxima fase é a [`05-ad-matrix`](05-ad-matrix.md), que multiplica a tese em criativos para tráfego pago.
