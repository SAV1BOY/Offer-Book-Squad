---
id: task.funnel-tech.plan-tech-deliverability
title: "Task — Plano Técnico, Links & Deliverability"
type: task
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
frameworks: [launch/surge-ops]
checklists:
  - tech-deliverability-checklist
  - launch/launch-fallback-gate
registries: [decision-registry]
tags: [tech, load-test, integracao, anti-loop, links, utm, deliverability, aquecimento, fallback, d5]
---

# Task — Plano técnico, links & deliverability: tornar o funil executável, resiliente e entregável na caixa de entrada

## Objetivo
Tornar o funil desenhado realmente executável e resiliente — testado sob carga, integrado aos sistemas (gateway, CRM, 3PL), à prova de loop, com cada link rastreado por UTM, com o e-mail chegando na caixa de entrada, e com plano de fallback em cada ponto crítico. O estado-pronto: o `tech-deliverability-plan` + `links-urls` + plano de fallback, com load test passado, integrações ligadas, SPF/DKIM/DMARC ok e rampa de aquecimento — aprovado no checklist técnico e no gate de fallback.

## Agente dono
[`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md). Engenheira a infraestrutura; não desenha o funil, não escreve copy. Sem poder de veto, mas **recusa executar** sobre funil ambíguo ou disparar de domínio frio sem rampa.

## Gatilho / Quando
Roda em D5, **depois** do funil: ativa quando (a) o [`funnel-architect`](../../agents/funnel-architect.md) entrega `funnel-map` + `page-specs`; (b) a copy de e-mail/SMS está **aprovada na voz** e pronta para envio (saída do [`voice-pass`](../copy/voice-pass.md)); (c) o chief pede o plano técnico/links/deliverability/fallback. Funil com rota ambígua ou estado sem destino → **recusar** e devolver ao funnel-architect (engenheirar sobre ambiguidade gera loop/rota órfã). Domínio/IP novo não aquecido + pedido de disparo em massa hoje → **recusar o go-live de e-mail** e escalar ao [`offerbook-chief`](../../agents/offerbook-chief.md).

## Inputs (Consome)
- `artifact.funnel-map` + `decision.funnel-routes` — cada trilha, bifurcação (sim/não/comprou/abandonou→destino), order bump e destino por temperatura, para implementar redirecionamentos sem loop e ligar cada estado ao sistema certo.
- `artifact.page-specs` — cada página, CTA, garantia/T&C e dependência, para estimar carga, configurar a página e instrumentar os links.
- `artifact.email-sms-sequences` — volume de envio, cadência (carrinho aberto/fechado, recuperação) e tamanho da lista, para dimensionar aquecimento e entregabilidade.
- `artifact.ad-matrix` — os destinos de cada ad e a temperatura, para gerar os links rastreados (UTM por origem/campanha/ângulo) que o tráfego pago exige.

## Procedimento
1. **Confirmar o funil sem becos.** Verificar que passou em `funnel-no-dead-end-gate` e as rotas/bifurcações estão definidas. Ambíguo → devolver ao funnel-architect.
2. **Rodar o load test.** Aplicar [`launch/surge-ops`](../../frameworks/launch/surge-ops.md): testar páginas e checkout no pico estimado (derivado do volume de tráfego/lista). Gargalo → adicionar CDN/cache/fila e uma página de espera de fallback.
3. **Ligar e testar integrações.** Gateway → CRM → 3PL/logística em sandbox. Webhook de pagamento com **retry idempotente** (chave por pedido) para o retry não duplicar pedido. Integração sem credencial/sandbox → marcar bloqueio e acionar o responsável.
4. **Varrer anti-loop.** Percorrer os redirecionamentos do `funnel-map`. Ciclo (ex.: segundo "não" do upsell apontando de volta ao upsell) → quebrar redirecionando para um estado terminal (TY/continuidade).
5. **Gerar links/UTM.** Encurtar, padronizar e rastrear cada destino. Para o tráfego pago, um link por **ângulo** (origem=ad, campanha=oferta, conteúdo=eixo). Convenção consistente para a atribuição funcionar.
6. **Configurar a entregabilidade.** SPF/DKIM/DMARC. Desenhar a **rampa de aquecimento** a partir do tamanho da lista e da idade do domínio; disparar primeiro ao **segmento mais engajado** (quente → frio).
7. **Escolher a estratégia (ToT).** Gerar ≥3 configurações de capacidade + entregabilidade e pontuar 0–5 por: resiliência sob pico (×3), cobertura de fallback (×3), entregabilidade (×3), integridade do fluxo (×2), rastreabilidade (×2). Rejeitar a que ignora o aquecimento (queima o domínio).
8. **Desenhar o fallback por ponto crítico.** Plano B testado para: página fora do ar (estática/espelho), gateway caindo (página "vaga reservada" + cobrança posterior), e-mail bloqueado (segmento/rampa), 3PL sem estoque (fila manual + e-mail de confirmação tardia).
9. **Self-verify (Bloom + red-team).** "Se o gateway cair às 20h do carrinho fechando, o cliente perde a compra ou é recuperado?" Checar UTM consistente, retry idempotente, rampa que protege a reputação. Antecipar o que o compliance marcaria (link/captura sem aviso de privacidade, rastreamento sem consentimento — LGPD/cookies) e sinalizar.
10. **Registrar e entregar.** Logar capacidade testada, integrações, links, rampa e fallback no `decision-registry`. Entregar o plano ao launch-producer. Máximo de 3 ciclos antes de escalar ao chief.

## Frameworks
[`launch/surge-ops`](../../frameworks/launch/surge-ops.md).

## Outputs (Produz)
- `artifact.links-urls` (template em [`funnel-tech/links-urls-template`](../../templates/funnel-tech/links-urls-template.md)) — tabela de links com UTM (origem/campanha/conteúdo) e encurtamento.
- `artifact.tech-deliverability-plan` (template em [`funnel-tech/tech-deliverability-plan-template`](../../templates/funnel-tech/tech-deliverability-plan-template.md)) — load test, integrações, anti-loop, deliverability (SPF/DKIM/DMARC + rampa), fallback por ponto crítico.
- `decision.tech-fallback` + [`decision-registry`](../../data/registries/decision-registry.md) atualizado (área, load_test, integrações, links, deliverability, fallback testado).

## Definition of Done
- Funil confirmado sem rota ambígua/órfã antes de engenheirar.
- Load test rodado no pico real; páginas e checkout com mitigação (CDN/cache/fila) onde degradaram.
- Integrações (gateway/CRM/3PL) ligadas e testadas em sandbox; webhooks idempotentes.
- Zero loop de redirecionamento; cada link com UTM consistente.
- SPF/DKIM/DMARC ok; rampa de aquecimento desenhada (quente primeiro) — sem disparo total de domínio novo.
- Cada ponto crítico com plano B **testado**; o checklist técnico e o gate de fallback verdes; tudo registrado.

## Gates
[`tech-deliverability-checklist`](../../checklists/tech/tech-deliverability-checklist.md) · [`launch/launch-fallback-gate`](../../checklists/launch/launch-fallback-gate.md).

## Handoff
**Próxima task:** [`build-run-of-show`](../ops/build-run-of-show.md) — dono [`launch-producer`](../../agents/launch-producer.md). **Contrato:** o produtor recebe o `tech-deliverability-plan` + `links-urls` + plano de fallback para entrar no run-of-show e na surge-ops do dia (capacidade confirmada, URLs canônicas, limites de envio). Também entrega ao [`events-logistics-coordinator`](../ops/build-events-logistics.md) as integrações de logística/3PL e ao [`compliance-auditor`](../qa-memory/compliance-audit.md) os links/rastreamento para checagem de privacidade. **Garantia:** funil testado sob carga, integrado, à prova de loop, com links rastreados, e-mail autenticado/aquecido e fallback por ponto crítico — ou um flag explícito de `pendente`/`bloqueado` com o risco nomeado.
