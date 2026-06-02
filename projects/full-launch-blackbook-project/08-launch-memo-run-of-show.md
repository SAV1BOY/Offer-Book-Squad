---
id: project.full-launch-blackbook-project.08-launch-memo-run-of-show
title: "Fase 08 — Launch Memo & Run-of-Show"
type: project-phase
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
consumes:
  - artifact.offer-book
  - artifact.money-model
  - artifact.funnel-map
  - artifact.tech-deliverability-plan
  - artifact.vsl-script
  - artifact.email-sms-sequences
produces:
  - artifact.launch-memo
  - artifact.launch-phases
  - artifact.run-of-show
  - artifact.sales-flow
tags: [project-phase, ops, launch, memo, phases, run-of-show, sales-flow, surge, d6]
---

# Fase 08 — Launch Memo & Run-of-Show

## Objetivo da Fase
Converter a estratégia aprovada na fundação e na coreografia do lançamento. Primeiro, o launch memo (tese, datas-âncora, metas, papéis) e as Fases I–VIII (do aquecimento ao pós-venda). Depois, o run-of-show da janela crítica minuto a minuto — onde cada e-mail, cada abertura de live, cada virada de página e cada gatilho de escassez tem dono, horário e fallback — mais o sales-flow e o plano de surge. O estado-pronto é a pista de fases na ordem que constrói desejo, o run-of-show executável e o surge plan com capacidade confirmada e plano B, com zero escassez não-lastreada. Abre a camada D6.

## Critério de Entrada
A Fase 01 entrega o `artifact.offer-book` (Big Idea, janela pretendida, ativos de prova) e o `artifact.money-model` (a ordem da escada — a espinha das fases). A Fase 06 entrega o `artifact.funnel-map` (páginas por degrau) e a Fase 07 o `artifact.tech-deliverability-plan` (capacidade, janelas de envio, URLs canônicas — os limites físicos). As Fases 02 e 03 entregam o `artifact.vsl-script` e as `artifact.email-sms-sequences` (as peças a encaixar nas fases). Pré-condição: o Offer Book DoD está verde, a copy (D4) e o funil/tech (D5) entregaram, e o money model está presente — sem a espinha, a pista seria uma agenda de eventos avulsos; sem capacidade confirmada para o pico, escala-se ao chief antes de marcar a data. O [`decision-registry`](../../data/registries/decision-registry.md) é escrito.

## Agentes & Tasks
- **Task [`build-launch-memo`](../../tasks/ops/build-launch-memo.md)** — dono [`launch-producer`](../../agents/launch-producer.md). Escreve a tese, as datas-âncora e a pista I–VIII.
- **Task [`build-run-of-show`](../../tasks/ops/build-run-of-show.md)** — mesmo dono [`launch-producer`](../../agents/launch-producer.md). Detalha a janela crítica, o sales-flow e o surge.

## Passos
1. Confirme as pré-condições: Offer Book DoD verde, copy e funil entregues, money model presente, capacidade técnica confirmada.
2. Escreva o launch memo: tese em uma frase, datas-âncora (pré-lançamento, carrinho abre/fecha), meta e papéis.
3. Escolha a arquitetura com Tree-of-Thoughts (≥3 formatos — PLF clássico, perfect-webinar, challenge — pontuados por fit, aderência do avatar, carga, desejo e risco).
4. Desenhe a pista com [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md) e [`launch/product-launch-formula`](../../frameworks/launch/product-launch-formula.md): Fases I–VIII, cada e-mail/VSL encaixado na fase certa, respeitando a espinha do money model.
5. Atribua dono e ativo por fase; valide que toda escassez planejada é real.
6. Detalhe o run-of-show da janela crítica: para cada disparo, HH:MM — ação — dono — fallback. Coreografe o sales-flow com [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md) (transitiva).
7. Planeje o surge com [`launch/surge-ops`](../../frameworks/launch/surge-ops.md): war-room, fallbacks (página espelho, link reserva), pico minuto a minuto. Escolha a janela de carrinho com Tree-of-Thoughts.
8. Cheque colisões e fadiga; self-verify com red-team (cada disparo com dono+horário+fallback? escassez 100% real?); registre as decisões no `decision-registry` e crave os handoffs.

## Artefatos Produzidos
- `artifact.launch-memo` — tese, datas-âncora, meta, papéis.
- `artifact.launch-phases` — Fases I–VIII com ativos, datas e donos.
- `artifact.run-of-show` — janela crítica minuto a minuto, cada linha com ação, dono e fallback.
- `artifact.sales-flow` — ondas de venda + gatilhos de escassez verdadeiros + picos.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`launch/launch-phase-readiness-gate`](../../checklists/launch/launch-phase-readiness-gate.md)
- [`launch/launch-surge-gate`](../../checklists/launch/launch-surge-gate.md)

## Critério de Saída
O memo tem tese, datas-âncora, meta e papéis; as Fases I–VIII estão na ordem que constrói desejo, respeitando a espinha, cada uma com dono e ativo; o run-of-show da janela crítica tem cada disparo com dono + horário + fallback; o sales-flow tem gatilhos de escassez 100% verdadeiros; o surge plan tem capacidade confirmada e fallbacks; sem buraco ou colisão na linha do tempo; os gates de prontidão de fases e de surge estão verdes. A próxima fase é a [`09-events-logistics`](09-events-logistics.md), que operacionaliza cada evento e cada entrega.
