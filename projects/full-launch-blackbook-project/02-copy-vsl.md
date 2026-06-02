---
id: project.full-launch-blackbook-project.02-copy-vsl
title: "Fase 02 — Copy de Longo Formato (VSL & Webinar)"
type: project-phase
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes:
  - artifact.offer-book
  - artifact.big-idea
  - artifact.positioning
  - decision.lead-type-locked
  - artifact.mechanism-sheet
  - artifact.offer-stack
  - artifact.guarantee
  - data.registry.proof
  - data.registry.objection
produces:
  - artifact.vsl-script
  - artifact.webinar-script
  - artifact.recap-vsl
  - artifact.sales-letter
  - artifact.ty-page-scripts
  - decision.voice-verdict
tags: [project-phase, copy, vsl, webinar, sales-letter, value-before-price, hard-stop, d4]
---

# Fase 02 — Copy de Longo Formato (VSL & Webinar)

## Objetivo da Fase
Transformar o Offer Book aprovado nos roteiros de longo formato — VSL, webinar, recap VSL, sales letter/offer page e TY page scripts — que entregam valor antes do preço, deslizam do gancho ao CTA único e passam no passe de voz. O estado-pronto é o conjunto de roteiros com os três blocos completos (Gancho & Promessa, Conteúdo & Mecanismo, Oferta & Fechamento), cada claim com prova linkada, escassez verdadeira, CTA único, aprovados nos gates de VSL e no veredito de voz. Esta fase abre a camada D4 — a primeira copy do lançamento só existe porque o HARD STOP da Fase 01 já passou.

## Critério de Entrada
A Fase 01 entrega o `artifact.offer-book` aprovado (HARD STOP VERDE) — é a pré-condição inegociável. Junto vêm a `artifact.big-idea` (promessa, gancho, vilão), o `artifact.positioning` e o `decision.lead-type-locked` (o lead define a abertura), o `artifact.mechanism-sheet`, o `artifact.offer-stack`, o `artifact.guarantee` e os registries [`proof-registry`](../../data/registries/proof-registry.md) e [`objection-registry`](../../data/registries/objection-registry.md). Pré-condição: o `offer-book-stack/offer-book-dod-gate` está APROVADO; gate vermelho faz o agente recusar e devolver ao chief. O lead precisa estar travado — se não, devolve ao positioning-lead-strategist. O [`control-registry`](../../data/registries/control-registry.md) é escrito.

## Agentes & Tasks
- **Task [`write-vsl-webinar`](../../tasks/copy/write-vsl-webinar.md)** — dono [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md). Sem poder de veto; submete tudo ao guardião.
- **Task [`voice-pass`](../../tasks/copy/voice-pass.md)** — dono [`voice-style-guardian`](../../agents/voice-style-guardian.md). Passe obrigatório de voz, com poder de veto.

## Passos
1. Verifique o HARD STOP: confirme o `offer-book-dod-gate` verde. Vermelho, recuse e devolva ao chief.
2. Carregue os inputs e trave a abertura pelo lead. Não invente a abertura.
3. Decomponha em 3 blocos: Gancho & Promessa, Conteúdo & Mecanismo (quebra/reconstrói crenças, deposita prova), Oferta & Fechamento (value stack → preço ancorado → garantia → escassez real → CTA único).
4. Gere a abertura com Tree-of-Thoughts: ≥3 ganchos pontuados por scroll-stop, congruência com a Big Idea e velocidade até a recompensa.
5. Sequencie a quebra de crença ordenando as objeções pela crença-raiz; ancore a prova junto de cada claim com [`copy/vsl-structure`](../../frameworks/copy/vsl-structure.md), [`copy/pas`](../../frameworks/copy/pas.md) e [`copy/pastor`](../../frameworks/copy/pastor.md).
6. Empilhe o fechamento: nenhum preço antes do Bloco 3. Gere o webinar com [`launch/perfect-webinar`](../../frameworks/launch/perfect-webinar.md) e aplique a [`copy/slippery-slide`](../../frameworks/copy/slippery-slide.md).
7. Self-verify com red-team: antecipe o veto do compliance (claim sem lastro, escassez falsa) e do guardião (frase longa, advérbio, voz passiva).
8. Registre no `control-registry` como draft e encaminhe ao voice-pass; só copy APROVADA na voz segue ao downstream.

## Artefatos Produzidos
- `artifact.vsl-script`, `artifact.webinar-script`, `artifact.recap-vsl`, `artifact.sales-letter`, `artifact.ty-page-scripts`.
- `decision.voice-verdict` — APROVADO por peça (ou REPROVADO com redline).
- Registry escrito: [`control-registry`](../../data/registries/control-registry.md).

## Gates
- [`vsl/vsl-value-before-price-gate`](../../checklists/vsl/vsl-value-before-price-gate.md) · [`vsl/vsl-risk-reversal-gate`](../../checklists/vsl/vsl-risk-reversal-gate.md) · [`vsl/vsl-cta-strength-gate`](../../checklists/vsl/vsl-cta-strength-gate.md)
- [`voice/voice-checklist`](../../checklists/voice/voice-checklist.md) e os quatro gates de voz.
- Gate de entrada (HARD STOP): [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).

## Critério de Saída
Os três blocos estão presentes; nenhum preço aparece antes do valor; cada claim tem prova linkada; a escassez é verdadeira; o CTA é único; a slippery slide não tem freio; os três gates de VSL estão verdes e o veredito de voz é APROVADO. Os roteiros estão no `control-registry`. A próxima fase é a [`03-email-sms-sequences`](03-email-sms-sequences.md), que recebe o VSL como destino dos e-mails e reaproveita ganchos e provas.
