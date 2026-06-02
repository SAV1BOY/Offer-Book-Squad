---
id: task.funnel-tech.map-funnel
title: "Task — Mapear o Funil"
type: task
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
consumes:
  - artifact.offer-book
  - artifact.money-model
  - artifact.vsl-script
  - artifact.email-sms-sequences
  - artifact.ad-matrix
  - decision.voice-verdict
produces:
  - artifact.funnel-map
  - artifact.page-specs
  - decision.funnel-routes
frameworks: [offer-to-funnel-mapping, launch/cart-open-close]
checklists:
  - funnel/funnel-no-dead-end-gate
  - funnel/funnel-backend-gate
registries: [decision-registry]
tags: [funnel, funil, money-model, paginas, checkout, order-bump, sem-becos, pos-compra, d5]
---

# Task — Mapear o funil: trilhas por degrau do money model, sem becos sem saída, cobrindo o "não" e o pós-compra

## Objetivo
Traduzir o money model travado e a copy aprovada num mapa de funil com uma trilha por degrau (atração, núcleo, upsell, downsell, continuidade), sem nenhum beco sem saída, cobrindo o "não" do comprador e o pós-compra, e especificando cada página, checkout e order bump de forma executável. O estado-pronto: o `funnel-map` + `page-specs` onde toda página/estado tem próximo passo, as 4 partes do money model viram trilhas reais, e a recuperação do abandono/recusa existe — aprovado nos dois gates de funil.

## Agente dono
[`funnel-architect`](../../agents/funnel-architect.md). Arquiteta o caminho do tráfego; não escreve copy, não desenha a oferta, não configura o servidor. Sem poder de veto.

## Gatilho / Quando
Roda em D5, **depois** da copy: ativa quando (a) a copy de núcleo está **aprovada na voz** (`voice-verdict` APROVADO — saída do [`voice-pass`](../copy/voice-pass.md)); (b) o money model está **travado** com as 4 partes sequenciadas (passou em `money-model-four-parts-gate`); (c) o chief pede o mapa de funil. Copy sem aprovação de voz → **devolver** ao [`voice-style-guardian`](../../agents/voice-style-guardian.md) (não mapear sobre texto que pode mudar). Money model abaixo das partes mínimas (atração + núcleo) → **recusar** e escalar ao [`money-model-designer`](../../agents/money-model-designer.md) via chief (sem backend o CAC não liquida).

## Inputs (Consome)
- `artifact.money-model` — a **sequência** das 4 partes, o CTA por degrau e o objetivo econômico de cada um (liquidar CAC, subir AOV, recuperar o "não", LTV).
- `artifact.offer-book` — a oferta de núcleo, a garantia, o preço ancorado e os bônus (o que cada página apresenta e onde a garantia entra).
- `artifact.vsl-script` / `artifact.email-sms-sequences` — onde está o CTA/oferta/garantia na VSL e as sequências de carrinho aberto/fechado e recuperação (o funil tem de casar com elas).
- `artifact.ad-matrix` — a **temperatura** e o ângulo de cada ad, para casar o destino certo (frio → educativa/VSL; retarget → oferta; continuidade → backend).
- `decision.voice-verdict` — a confirmação de que a copy está aprovada antes de especificar páginas sobre ela.

## Procedimento
1. **Confirmar pré-condições.** `voice-verdict` APROVADO e money model com 4 partes. Se falta, devolver/recusar conforme o gatilho.
2. **Desenhar a trilha principal.** Entrada → VSL/oferta → checkout → TY, aplicando [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md). Cada página com **um** próximo passo (CTA único).
3. **Inserir o order bump.** No checkout, um complemento de alta margem em 1-clique, baixo atrito, sem roubar o foco do núcleo.
4. **Sequenciar upsell → downsell pós-compra.** O "sim" sobe ao upsell; o "não" do upsell cai no downsell, nunca numa página morta.
5. **Desenhar a recuperação.** Aplicar [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md): ligar o gatilho de abandono à sequência de e-mail/SMS; o "não" final cai numa oferta de backend. O "não" sempre tem rota, não silêncio.
6. **Ligar a continuidade.** O backend de recorrência (assinatura/comunidade) ganha trilha própria pós-primeiro-resultado; a TY convida à continuidade (sem beco).
7. **Especificar cada página.** Objetivo, seções, CTA único, garantia/T&C visível, consciência-alvo e dependência de copy. Página cuja copy não existe → marcar `bloqueada_por_copy` e acionar o autor.
8. **Escolher a topologia (ToT).** Gerar ≥3 configurações e pontuar 0–5 por: sem beco sem saída (×3), fidelidade ao money model (×3), cobertura do "não" e pós-compra (×3), atrito mínimo (×2), casamento de consciência (×2). Podar a topologia sem backend (CAC não liquida) ou que deixa o abandono sem recuperação.
9. **Calibrar o destino por temperatura.** Frio entra por página educativa/VSL longa; retarget na página de oferta; e-mail quente vai direto ao checkout.
10. **Self-verify (Bloom + red-team).** Seguir cada seta — alguma página/estado (TY, "não" do upsell, abandono) termina no vazio? O backend está ligado? Antecipar o que o [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) não conseguiria implementar (rota ambígua, order bump sem regra de 1-clique, loop) e o que o [`compliance-auditor`](../../agents/compliance-auditor.md) marcaria (página sem garantia/T&C visível).
11. **Registrar e entregar.** Logar a topologia e cada bifurcação (sim/não/comprou/abandonou→destino) no `decision-registry`. Entregar specs executáveis ao tech-engineer. Máximo de 3 ciclos antes de escalar ao chief.

## Frameworks
[`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md).

## Outputs (Produz)
- `artifact.funnel-map` (template em [`funnel-tech/funnel-map-template`](../../templates/funnel-tech/funnel-map-template.md)) — entrada por temperatura, trilha principal, pós-compra, recuperação, regra "sem beco sem saída".
- `artifact.page-specs` (template em [`funnel-tech/page-specs-template`](../../templates/funnel-tech/page-specs-template.md)) — por página: objetivo, seções, CTA único, garantia/T&C, consciência-alvo, dependência de copy.
- `decision.funnel-routes` + [`decision-registry`](../../data/registries/decision-registry.md) atualizado (trilha, páginas, bifurcações, order_bump, destino por temperatura, alternativas podadas, motivo).

## Definition of Done
- `voice-verdict` APROVADO e money model com 4 partes confirmados antes do mapa.
- Todas as 4 partes do money model aparecem como trilha; o backend (upsell/downsell/continuidade) está ligado.
- Nenhuma página/estado sem próximo passo (TY, "não" do upsell, abandono têm rota); abandono ligado à sequência de recuperação.
- Cada página especificada (objetivo, seções, CTA único, garantia/T&C, consciência); destino casado por temperatura.
- Os dois gates de funil verdes; rotas registradas no `decision-registry`; specs executáveis prontas para o tech.

## Gates
[`funnel/funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) · [`funnel/funnel-backend-gate`](../../checklists/funnel/funnel-backend-gate.md).

## Handoff
**Próxima task:** [`plan-tech-deliverability`](plan-tech-deliverability.md) — dono [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md). **Contrato:** o engenheiro recebe o `funnel-map` + `page-specs` como **specs executáveis** (cada página, CTA, bump, redirecionamento e rota de recuperação com estados explícitos — sim/não/comprou/abandonou→destino), sem ambiguidade. Também entrega ao [`launch-producer`](../ops/build-run-of-show.md) o mapa para o run-of-show e ao [`compliance-auditor`](../qa-memory/compliance-audit.md) o funil para checagem de garantia/T&C por página. **Garantia:** funil sem becos sem saída, com as 4 partes em trilhas e o "não"/abandono com recuperação — ou um flag explícito de `bloqueada_por_copy`/`bloqueada_por_money_model`.
