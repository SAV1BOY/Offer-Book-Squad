---
id: task.copy.generate-ad-matrix
title: "Task — Gerar a Matriz de Ads"
type: task
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
consumes:
  - artifact.offer-book
  - artifact.mechanism-sheet
  - artifact.big-idea
  - artifact.voc-verbatim-bank
  - data.registry.objection
  - data.registry.proof
produces:
  - artifact.ad-matrix
  - decision.ad-angles
frameworks: [copy/hook-frameworks, lead-types, copy/fascination-bullets]
checklists:
  - offer-book-stack/offer-book-dod-gate
  - ads/ads-angle-coverage-gate
  - ads/ads-claim-backing-gate
  - ads/ads-variation-gate
registries: [control-registry, swipe-registry]
tags: [copy, ads, matriz, angulos, retargeting, continuidade, hook, fascination, hard-stop]
---

# Task — Gerar a matriz de ads que ataca cada dor por múltiplos ângulos

## Objetivo
Transformar UMA Big Idea e UM mecanismo numa matriz de ads onde cada dor do avatar é atacada por ≥3 ângulos distintos, o retargeting cobre cada objeção dominante, e a continuidade estende a recorrência — todos rastreáveis à tese e com claim lastreado. O estado-pronto: a matriz com as três camadas (frio, retarget, continuidade), cada gancho com prova linkada, ângulos realmente diferentes (não cosméticos), aprovada nos três gates de ads e encaminhada ao [`voice-pass`](voice-pass.md).

## Agente dono
[`ad-creative-factory`](../../agents/ad-creative-factory.md). Multiplica a tese estratégica em criativos. Sem poder de veto; submete tudo ao voice-guardian.

## Gatilho / Quando
**HARD STOP: esta task de copy (D4) só ativa APÓS o [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) estar APROVADO.** Conforme `config.yaml: defaults.hard_stop_before_copy: true` e o [`ARCHITECTURE.md`](../../ARCHITECTURE.md), nenhuma palavra de copy nasce antes de o Offer Book passar no Definition of Done. Gate vermelho → o agente **recusa** e devolve ao [`offerbook-chief`](../../agents/offerbook-chief.md). Demais gatilhos: pedido da matriz de ads, ou de retargeting/continuidade para tráfego pago, com a **Big Idea travada** (UMA, via `big-idea-single-gate`), o mecanismo nomeado e o banco de objeções disponível. Sem Big Idea única não prossegue — múltiplas teses geram ads que competem e confundem o pixel.

## Inputs (Consome)
- `artifact.offer-book` — a oferta de núcleo, a garantia e a promessa central que o ad honra (nada de prometer além do que a oferta entrega).
- `artifact.big-idea` — a UMA tese, o gancho-mãe, o vilão e a promessa (a coluna que todo ângulo veste).
- `artifact.mechanism-sheet` — a frase única do mecanismo e a tabela velho×novo (matéria dos ângulos de "por que funciona quando o resto falhou").
- `artifact.voc-verbatim-bank` — as dores na **linguagem literal** do avatar (cada dor vira um ângulo).
- [`data.registry.objection`](../../data/registries/objection-registry.md) — objeções ranqueadas; cada uma vira um ângulo de **retargeting**.
- [`data.registry.proof`](../../data/registries/proof-registry.md) — lastro por claim; define qual gancho vai ao ar e qual fica bloqueado.

## Procedimento
1. **Verificar o HARD STOP.** Confirmar o `offer-book-dod-gate` verde. Vermelho → recusar e devolver ao chief.
2. **Mapear as dores em eixos de ângulo.** Para cada dor do verbatim, definir os eixos possíveis: dor, mecanismo, prova, identidade, medo/ganho. O objetivo é diferença real de ângulo, não troca de cor de botão.
3. **Gerar ganchos por dor (ToT).** Para cada dor, produzir ≥3 ganchos que abrem por eixos diferentes via [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md). Pontuar 0–5 por: paragem de scroll (×3), fidelidade à Big Idea (×3), lastro do claim (×3), diferença de ângulo (×2), casamento de consciência (×2). Podar variações cosméticas (diferença de ângulo = 0).
4. **Escrever a camada de retargeting.** Um ad por objeção dominante do `objection-registry`; cada um reverte a objeção com o mecanismo + a garantia. Abertura pela objeção (o público já conhece a oferta), não pela dor de descoberta.
5. **Escrever a camada de continuidade.** Ângulos de retenção/recompra que falam a quem **já** teve o primeiro resultado, fechando o ciclo do money model.
6. **Casar lead e consciência.** Usar [`lead-types`](../../lib/taxonomies/lead-types.md): frio = História/Proclamação/Segredo; retarget/quente = Oferta direta. Calibrar pela sofisticação (3-4 puxa mecanismo; 5 puxa identidade/prova).
7. **Gerar os corpos.** Usar [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md) para os bullets de curiosidade por ad.
8. **Validar o lastro.** Todo gancho/claim aponta para prova no `proof-registry`. Gancho sedutor sem lastro → bloquear o ângulo, acionar o [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) e substituir por promessa verificável até a prova chegar (`pendente_de_prova`).
9. **Self-verify (Bloom + red-team).** Checar: cada dor coberta por ≥3 ângulos distintos? Cada objeção com retarget? Continuidade presente? Variações são ângulos diferentes, não cosméticas? Promessa de prazo/resultado infalsificável? Antecipar o veto do compliance (claim sem lastro, escassez falsa, resultado garantido) e do voice-guardian.
10. **Registrar e encaminhar.** Logar cada ad no `control-registry`, a decisão de ângulos (eixos por dor, podados, motivo), e os ganchos reutilizáveis no `swipe-registry`. Entregar ao voice-pass. Máximo de 3 ciclos antes de escalar ao chief.

## Frameworks
[`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`lead-types`](../../lib/taxonomies/lead-types.md) · [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md).

## Outputs (Produz)
- `artifact.ad-matrix` (template em [`copy/ad-matrix-template`](../../templates/copy/ad-matrix-template.md)) com as três camadas: frio (≥3 ângulos por dor), retargeting (1 por objeção), continuidade.
- `decision.ad-angles` — eixos escolhidos por dor, candidatos podados, motivo.
- [`control-registry`](../../data/registries/control-registry.md) atualizado (cada ad: `ad_id`, camada, dor/objeção-alvo, eixo, lead_type, gancho, corpo, claim_refs, prova_refs, big_idea_id, `status`). Ganchos reutilizáveis no [`swipe-registry`](../../data/registries/swipe-registry.md).

## Definition of Done
- HARD STOP verde (offer-book-dod-gate aprovado) **antes** de qualquer linha.
- Cada dor dominante coberta por ≥3 ângulos distintos (dor ≠ mecanismo ≠ identidade); retargeting cobre cada objeção; continuidade presente.
- Cada ad rastreável à UMA Big Idea (nenhuma tese paralela); cada gancho com claim lastreado (zero `pendente_de_prova` no estado final).
- Variações são ângulos diferentes, não cosméticas; lead casado à temperatura/consciência do destino.
- Os três gates de ads verdes; matriz registrada e ganchos no swipe-registry; encaminhada ao voice-pass.

## Gates
[`ads/ads-angle-coverage-gate`](../../checklists/ads/ads-angle-coverage-gate.md) · [`ads/ads-claim-backing-gate`](../../checklists/ads/ads-claim-backing-gate.md) · [`ads/ads-variation-gate`](../../checklists/ads/ads-variation-gate.md). Gate de entrada (HARD STOP): [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).

## Handoff
**Próxima task:** [`voice-pass`](voice-pass.md) (passe obrigatório do voice-style-guardian). **Contrato de saída:** todo ad é rastreável à UMA Big Idea, com claim lastreado, ângulo declarado e lead casado à consciência — pronto para o guardião e, após o veredito APROVADO, para o [`funnel-architect`](../funnel-tech/map-funnel.md) (ângulo/temperatura → página de destino) e o [`tech-links-deliverability-engineer`](../funnel-tech/plan-tech-deliverability.md) (destinos → UTM por origem/campanha/ângulo).
