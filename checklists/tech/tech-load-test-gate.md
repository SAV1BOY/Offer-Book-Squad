---
id: checklist.tech.tech-load-test-gate
title: "Gate — Load Test (a página e o checkout aguentam o pico real)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: tech-links-deliverability-engineer
frameworks: [launch/surge-ops]
registries: [decision-registry]
tags: [gate, tech, load-test, capacidade, pico, checkout, d5]
---

# Gate — Load Test

## Propósito
Este gate prova que **a página de oferta e o checkout foram testados no pico real e aguentam o tráfego do dia**. Ele existe porque "vai aguentar" não é teste — e a página cai sempre no pior momento, no pico do disparo de e-mail ou da abertura de carrinho. Quando o checkout degrada acima de N requisições simultâneas, cada venda perdida nunca volta. O `tech-links-deliverability-engineer` roda o load test no pico estimado a partir do volume da lista e do tráfego pago, aplicando a disciplina de `surge-ops` de Hormozi: a infraestrutura é provada antes do go-live, não no calor da fila. Vale o princípio `evidence_before_opinion`: o número do teste vale mais que a confiança do time. Se o checkout cai em 3,2k simultâneos e o pico-alvo é 5k, o gate falha até a mitigação (CDN, cache, fila, página de espera) estar no lugar e re-testada. Este gate julga **só a capacidade sob carga** — o plano B para quando ainda assim estourar é do `tech-fallback-gate`. A entregabilidade do e-mail que gera o pico é do `tech-deliverability-gate`.

## Dono & Escopo
- **owner_agent:** `tech-links-deliverability-engineer` (estima o pico, roda o teste e dimensiona a mitigação). O [`funnel-architect`](../../agents/funnel-architect.md) entrega as `page-specs` que definem o que testar.
- **Artefato inspecionado:** o `tech-deliverability-plan` na parte de capacidade, cruzado com as `page-specs` e o volume de tráfego/lista. O resultado vai ao [`decision-registry`](../../data/registries/decision-registry.md). Gate consumido em `config.yaml: routing.plan-tech-deliverability`.

## Condição de Passagem
A página de oferta e o checkout sustentam o pico de tráfego estimado sem degradar, com a mitigação testada onde o teste apontou gargalo.

## Itens
1. **Pico-alvo definido.** Verificar: existe um número de requisições/usuários simultâneos derivado do volume da lista e do tráfego pago.
2. **Teste executado.** Verificar: o load test rodou no pico-alvo, não em carga simbólica; há resultado registrado.
3. **Checkout sob carga.** Verificar: o checkout (gateway + página de pagamento) aguenta o pico sem degradar a conversão.
4. **Gargalo identificado.** Verificar: o ponto onde o sistema degrada está medido (ex.: "checkout cai em 3,2k").
5. **Mitigação no lugar.** Verificar: CDN, cache, fila ou página de espera cobrem o gargalo e foram re-testados.
6. **Margem sobre o pico.** Verificar: a capacidade testada tem folga acima do pico-alvo, não fica no limite exato.

## Evidência Exigida
Para marcar ✅: linkar o registro de load test no [`decision-registry`](../../data/registries/decision-registry.md) no formato `{pico_alvo, resultado, gargalo, mitigacao}`, mais o relatório do teste mostrando o ponto de degradação e o re-teste após a mitigação. A `page-specs` e o volume que embasaram o pico-alvo ficam citados.

## Protocolo de Falha
Item vermelho → o `tech-links-deliverability-engineer` **não declara a capacidade pronta** e não libera o go-live até a mitigação cobrir o gargalo e o re-teste passar. Funil com rota ambígua que impede o teste volta ao [`funnel-architect`](../../agents/funnel-architect.md). O engenheiro **não tem veto** sobre o pipeline; ele recusa executar sobre carga não testada e registra a recusa. Capacidade que estoura a viabilidade do dia escala ao [`offerbook-chief`](../../agents/offerbook-chief.md). O plano B para o estouro real é tratado no [`tech-fallback-gate`](tech-fallback-gate.md). Re-entrada: aplicar a mitigação, re-rodar o teste no pico-alvo e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/surge-ops`](../../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`funnel-architect`](../../agents/funnel-architect.md) · [`launch-producer`](../../agents/launch-producer.md)
- Gates irmãos: [`tech-deliverability-gate`](tech-deliverability-gate.md) · [`tech-anti-loop-gate`](tech-anti-loop-gate.md) · [`tech-links-utm-gate`](tech-links-utm-gate.md) · [`tech-fallback-gate`](tech-fallback-gate.md)
- Relacionado: [`launch-fallback-gate`](../launch/launch-fallback-gate.md) · [`launch-surge-gate`](../launch/launch-surge-gate.md)
