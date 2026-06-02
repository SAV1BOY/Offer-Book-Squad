---
id: project.full-launch-blackbook-project.07-tech-deliverability
title: "Fase 07 — Tech, Links & Deliverability"
type: project-phase
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: tech-links-deliverability-engineer
consumes:
  - artifact.funnel-map
  - artifact.page-specs
  - artifact.email-sms-sequences
  - artifact.ad-matrix
  - decision.funnel-routes
produces:
  - artifact.links-urls
  - artifact.tech-deliverability-plan
  - decision.tech-fallback
tags: [project-phase, tech, load-test, integracao, anti-loop, links, utm, deliverability, fallback, d5]
---

# Fase 07 — Tech, Links & Deliverability

## Objetivo da Fase
Tornar o funil desenhado realmente executável e resiliente — testado sob carga, integrado aos sistemas (gateway, CRM, 3PL), à prova de loop, com cada link rastreado por UTM, com o e-mail chegando na caixa de entrada, e com plano de fallback em cada ponto crítico. O estado-pronto é o tech-deliverability-plan mais os links-urls mais o plano de fallback, com load test passado, integrações ligadas, SPF/DKIM/DMARC ok e rampa de aquecimento — aprovado no checklist técnico e no gate de fallback. Esta fase fecha a camada D5: a infraestrutura que aguenta o pico e protege a reputação do domínio.

## Critério de Entrada
A Fase 06 entrega o `artifact.funnel-map`, as `artifact.page-specs` e o `decision.funnel-routes` (cada trilha, bifurcação, order bump e destino por temperatura). As Fases 03 e 05 entregam as `artifact.email-sms-sequences` (volume, cadência, tamanho da lista) e a `artifact.ad-matrix` (destinos e temperatura para gerar os links rastreados). Pré-condição: o funil passou no no-dead-end-gate e as rotas estão definidas; funil com rota ambígua é devolvido ao funnel-architect (engenheirar sobre ambiguidade gera loop). A copy de e-mail/SMS está aprovada na voz e pronta para envio. Domínio/IP novo não aquecido + pedido de disparo em massa hoje → recusa o go-live de e-mail e escala ao chief. O [`decision-registry`](../../data/registries/decision-registry.md) é escrito.

## Agentes & Tasks
- **Task [`plan-tech-deliverability`](../../tasks/funnel-tech/plan-tech-deliverability.md)** — dono [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md). Engenheira a infraestrutura. Sem poder de veto, mas recusa executar sobre funil ambíguo ou disparar de domínio frio sem rampa.

## Passos
1. Confirme o funil sem becos (passou no no-dead-end-gate). Ambíguo, devolva ao funnel-architect.
2. Rode o load test com [`launch/surge-ops`](../../frameworks/launch/surge-ops.md): páginas e checkout no pico estimado. Gargalo, adicione CDN/cache/fila e página de espera de fallback.
3. Ligue e teste as integrações (gateway → CRM → 3PL) em sandbox; webhook de pagamento com retry idempotente (chave por pedido) para não duplicar.
4. Varra anti-loop: percorra os redirecionamentos; ciclo vira redirecionamento a um estado terminal (TY/continuidade).
5. Gere links/UTM: um link por ângulo para o tráfego pago (origem, campanha, conteúdo). Convenção consistente para a atribuição funcionar.
6. Configure a entregabilidade: SPF/DKIM/DMARC e a rampa de aquecimento por tamanho de lista e idade de domínio; dispare primeiro ao segmento mais engajado (quente → frio).
7. Escolha a estratégia com Tree-of-Thoughts (≥3 configurações de capacidade + entregabilidade pontuadas por resiliência, fallback, deliverability, integridade e rastreabilidade); rejeite a que ignora o aquecimento.
8. Desenhe o fallback por ponto crítico (página fora do ar, gateway caindo, e-mail bloqueado, 3PL sem estoque); self-verify com red-team; registre tudo no `decision-registry` e entregue ao launch-producer.

## Artefatos Produzidos
- `artifact.links-urls` — tabela de links com UTM (origem/campanha/conteúdo) e encurtamento.
- `artifact.tech-deliverability-plan` — load test, integrações, anti-loop, deliverability (SPF/DKIM/DMARC + rampa), fallback por ponto crítico.
- `decision.tech-fallback` — área, load test, integrações, links, deliverability, fallback testado.
- Registry escrito: [`decision-registry`](../../data/registries/decision-registry.md).

## Gates
- [`tech-deliverability-checklist`](../../checklists/tech/tech-deliverability-checklist.md)
- [`launch/launch-fallback-gate`](../../checklists/launch/launch-fallback-gate.md)

## Critério de Saída
O funil foi confirmado sem rota ambígua; o load test rodou no pico real com mitigação onde degradou; as integrações estão ligadas e testadas em sandbox com webhooks idempotentes; há zero loop de redirecionamento; cada link tem UTM consistente; SPF/DKIM/DMARC estão ok e a rampa de aquecimento está desenhada (quente primeiro); cada ponto crítico tem plano B testado; o checklist técnico e o gate de fallback estão verdes. Fecha a camada D5. A próxima fase é a [`08-launch-memo-run-of-show`](08-launch-memo-run-of-show.md), que coreografa o dia minuto a minuto sobre esta infraestrutura confirmada.
