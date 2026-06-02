---
id: checklist.funnel.funnel-redirect-gate
title: "Gate — Redirecionamentos (cada estado leva ao destino certo, sem loop)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
frameworks: [offer-to-funnel-mapping, launch/cart-open-close]
registries: [decision-registry]
tags: [gate, funil, redirecionamento, bifurcacao, loop, estados, d5]
---

# Gate — Redirecionamentos

## Propósito
Este gate prova que **cada bifurcação do funil leva ao destino certo, sem loop e sem rota ambígua**. Em cada ponto de decisão — sim, não, comprou, abandonou — o tráfego é redirecionado para uma página explícita. Ele existe porque uma rota mal definida é um vazamento: o comprador cai numa página errada, num loop de redirecionamento ou numa tela em branco, e a venda morre no clique. Vale o princípio `traceability_before_eloquence`: o caminho precisa ser rastreável estado a estado, não improvisado. O gate exige que o `funnel-architect` declare o destino de cada estado de forma que o engenheiro de tech implemente sem adivinhação — sem redirecionamento circular, sem destino duplicado, sem upsell que volta ao próprio upsell. É a barreira que garante que seguir qualquer seta sempre chega a uma página viva e correta.

## Dono & Escopo
- **owner_agent:** `funnel-architect` (define cada bifurcação e seu destino). O `tech-links-deliverability-engineer` implementa as rotas e sinaliza o que for inexequível.
- **Artefato inspecionado:** as bifurcações do `funnel-map` registradas no [`decision-registry`](../../data/registries/decision-registry.md) no formato `{estado: sim|nao|comprou|abandonou, destino}`, com as URLs e regras nas `page-specs`.

## Condição de Passagem
Cada estado de decisão do funil redireciona para uma página explícita e correta, sem loop, ambiguidade ou destino duplicado.

## Itens
1. **Estados enumerados.** Verificar: cada página de decisão lista seus estados (sim/não/comprou/abandonou) no `decision-registry`.
2. **Destino explícito por estado.** Verificar: cada estado aponta para uma página nomeada, sem "depende" nem destino em branco.
3. **Sem loop de redirecionamento.** Verificar: nenhuma rota volta a si mesma (upsell→upsell) nem cria ciclo entre páginas.
4. **Sem destino duplicado ambíguo.** Verificar: dois estados distintos não caem no mesmo destino quando deveriam divergir (sim≠não).
5. **Abandono roteado.** Verificar: o estado "abandonou" dispara a sequência de recuperação, não o silêncio (via `launch/cart-open-close`).
6. **URLs canônicas.** Verificar: cada destino usa a URL canônica acordada, sem link quebrado ou provisório.
7. **Spec sem adivinhação.** Verificar: o engenheiro de tech consegue mapear cada `estado→destino` sem interpretar.

## Evidência Exigida
Para marcar ✅: linkar a tabela `estado→destino` do `decision-registry` (itens 1–2), a checagem de ciclos e duplicidades (itens 3–4), a ligação do abandono à sequência (item 5) e a lista de URLs canônicas nas `page-specs` (item 6).

## Protocolo de Falha
Item vermelho → o `funnel-architect` **reescreve a rota com estados explícitos** (`sim/não/comprou/abandonou→destino`) até ser implementável sem adivinhação. Loop de redirecionamento ou destino ambíguo reabre o gate. Rota inexequível é registrada como restrição para o [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) resolver. A ausência de próximo passo é tratada no [`funnel-no-dead-end-gate`](funnel-no-dead-end-gate.md). Re-entrada: corrigir a bifurcação, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`funnel-architect`](../../agents/funnel-architect.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md)
- Gates irmãos: [`funnel-path-coverage-gate`](funnel-path-coverage-gate.md) · [`funnel-order-bump-gate`](funnel-order-bump-gate.md) · [`funnel-no-dead-end-gate`](funnel-no-dead-end-gate.md) · [`funnel-backend-gate`](funnel-backend-gate.md)
