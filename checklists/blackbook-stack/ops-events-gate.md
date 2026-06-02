---
id: checklist.blackbook-stack.ops-events-gate
title: "Gate — Ops & Eventos (run-of-show + entregáveis com dono/hosting/data)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [product-launch-formula, runway-and-phases, surge-ops, money-model-sequence]
registries: [decision-registry, offer-registry]
tags: [gate, ops, events, run-of-show, logistics, d6, d7, dod-input]
---

# Gate — Ops & Eventos

## Propósito
Este gate prova que **o lançamento tem um run-of-show executável e cada entregável tem dono, hosting e data**. Existe porque lançamentos não morrem na estratégia — morrem na execução: um webinar sem host definido, um bônus sem arquivo hospedado, uma fase sem data de início. Cada momento da operação precisa de um responsável nomeado e um artefato pronto e acessível. É o terceiro insumo do [`blackbook-dod-gate`](blackbook-dod-gate.md): a logística garante que a oferta e a copy cheguem ao mercado no tempo certo.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (audita prontidão operacional); produzido em D6 por `launch-producer` e `events-logistics-coordinator`.
- **Artefato inspecionado:** o run-of-show, o calendário de fases e o inventário de entregáveis, gravados no [`decision-registry`](../../data/registries/decision-registry.md) e ligados aos degraus do [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O run-of-show cobre cada fase do lançamento com data e dono, e cada entregável (evento, bônus, ativo) tem responsável nomeado, local de hosting e data de disponibilização.

## Itens
1. **Run-of-show completo.** Verificar: cada fase (runway→abertura→fechamento→pós) tem início, fim e dono no calendário.
2. **Fluxo de vendas mapeado.** Verificar: a sequência de momentos de venda bate com a escada do money model do `offer-registry`.
3. **Eventos com host e plataforma.** Verificar: cada evento ao vivo (webinar/call) tem host nomeado, plataforma e link de acesso.
4. **Entregáveis com dono.** Verificar: cada bônus/ativo no inventário tem um responsável único.
5. **Entregáveis com hosting.** Verificar: cada ativo tem local de hospedagem definido e link acessível (não "a definir").
6. **Entregáveis com data.** Verificar: cada ativo tem data de disponibilização ligada à fase que o usa.
7. **Plano de surge/contingência.** Verificar: pico de suporte e estouro de demanda têm plano e dono (`surge-ops`).
8. **Dependências resolvidas.** Verificar: nenhum entregável bloqueado por outro sem data — a cadeia de dependências fecha.

## Evidência Exigida
Para marcar ✅: linkar o run-of-show com datas e donos (itens 1–2), a ficha de cada evento com host/plataforma (item 3), o inventário de entregáveis mostrando dono/hosting/data por linha (itens 4–6), o plano de surge (item 7) e o mapa de dependências (item 8). "A definir" em qualquer campo reprova o item.

## Protocolo de Falha
Item vermelho → o `compliance-auditor` devolve a `launch-producer` (run-of-show/fases) ou `events-logistics-coordinator` (entregáveis/hosting) com a lacuna nomeada e **não libera o blackbook-dod-gate**. Re-entrada: atribuir o dono, definir hosting/data, atualizar o inventário no `decision-registry` e re-submeter. Entregável sem dono ou sem data bloqueia a fase que depende dele.

## Links
- Frameworks: [`product-launch-formula`](../../frameworks/launch/product-launch-formula.md) · [`runway-and-phases`](../../frameworks/launch/runway-and-phases.md) · [`surge-ops`](../../frameworks/launch/surge-ops.md) · [`money-model-sequence`](../../frameworks/money-model-sequence.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`launch-producer`](../../agents/launch-producer.md) · [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Agrega para: [`blackbook-dod-gate`](blackbook-dod-gate.md)
