---
id: checklist.blackbook-stack.funnel-tech-gate
title: "Gate — Funil & Tech (mapa + URLs + load test + deliverability)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [offer-to-funnel-mapping, cart-open-close, surge-ops]
registries: [decision-registry, control-registry]
tags: [gate, funnel, tech, urls, load-test, deliverability, d5, d7, dod-input]
---

# Gate — Funil & Tech

## Propósito
Este gate prova que o **funil está mapeado sem becos sem saída e a infraestrutura aguenta o lançamento**. Existe porque a melhor copy morre num link quebrado, numa página que cai no pico de tráfego ou num email que vai para spam. Cada degrau do money model precisa de uma página, uma URL viva, um caminho de saída e entrega de email confiável. É o segundo insumo do [`blackbook-dod-gate`](blackbook-dod-gate.md): o funil traduz a oferta e a copy em um caminho técnico que converte sob carga real.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (audita prontidão técnica e privacidade); produzido em D5 por `funnel-architect` e `tech-links-deliverability-engineer`.
- **Artefato inspecionado:** o mapa de funil, a lista de URLs e o plano de deliverability/surge, gravados no [`decision-registry`](../../data/registries/decision-registry.md) e ligados às peças do [`control-registry`](../../data/registries/control-registry.md).

## Condição de Passagem
Cada degrau do funil tem página e URL viva, não há becos sem saída nem backend faltando, o load test passou no pico esperado, e a deliverability está configurada e testada.

## Itens
1. **Mapa de funil sem beco sem saída.** Verificar: cada página tem ≥1 próximo passo; nenhuma rota termina sem CTA ou redirecionamento.
2. **Backend presente.** Verificar: upsell/downsell/continuidade do money model têm página e fluxo no mapa.
3. **URLs vivas.** Verificar: cada URL da lista retorna 200 e aponta para a página certa (checagem de status).
4. **Rastreamento e pixels.** Verificar: cada página tem o rastreamento/pixel exigido e os eventos de conversão disparam.
5. **Load test no pico.** Verificar: teste de carga no volume de tráfego esperado (ex.: abertura de carrinho) com tempo de resposta dentro do limite.
6. **Plano de fallback.** Verificar: rota de contingência se a página principal cair (`launch-fallback`), com dono e gatilho.
7. **Deliverability configurada.** Verificar: SPF, DKIM, DMARC válidos; IP/domínio aquecido; teste de inbox passou nos principais provedores.
8. **Privacidade/consentimento.** Verificar: captura de dados tem base legal (LGPD) e opt-in/opt-out funcionando.

## Evidência Exigida
Para marcar ✅: linkar o mapa de funil (itens 1–2), o relatório de status das URLs e rastreamento (itens 3–4), o resultado do load test com números (item 5), o plano de fallback (item 6), os registros SPF/DKIM/DMARC + teste de inbox (item 7) e a configuração de consentimento (item 8).

## Protocolo de Falha
Item vermelho → o `compliance-auditor` devolve a `funnel-architect` (mapa/becos) ou `tech-links-deliverability-engineer` (URLs/load/deliverability) com o defeito nomeado e **não libera o blackbook-dod-gate**. Re-entrada: corrigir a rota/URL/configuração, re-rodar o teste, atualizar o `decision-registry` e re-submeter. Falha de deliverability ou load test bloqueia a abertura de carrinho — sem exceção por prazo.

## Links
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`cart-open-close`](../../frameworks/launch/cart-open-close.md) · [`surge-ops`](../../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`funnel-architect`](../../agents/funnel-architect.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Depende de: [`copy-coverage-gate`](copy-coverage-gate.md) · Agrega para: [`blackbook-dod-gate`](blackbook-dod-gate.md)
