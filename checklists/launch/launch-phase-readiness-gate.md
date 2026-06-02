---
id: checklist.launch.launch-phase-readiness-gate
title: "Gate — Prontidão de Fase (cada fase com ativo, dono e gatilho)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [launch/product-launch-formula, launch/runway-and-phases, launch/surge-ops]
registries: [decision-registry]
tags: [gate, launch, fases, prontidao, plf, run-of-show, d6]
---

# Gate — Prontidão de Fase

## Propósito
Este gate prova que **cada fase do lançamento está pronta antes de o lançamento começar** — com o ativo na mão, o dono atribuído e o gatilho de transição definido. As Fases I–VIII (do aquecimento ao pós-venda) constroem desejo na ordem certa; uma fase incompleta quebra a sequência e desperdiça a antecipação. Ele existe na lógica de Jeff Walker: um lançamento é uma história contada em fases, e nenhuma fase pode ir ao ar sem seu conteúdo pronto. Vale o princípio `offer_before_persuasion` aplicado à execução: não se agenda o disparo de uma peça que não existe. O gate exige que cada fase tenha seus ativos (e-mails, VSL, página) prontos e aprovados na voz, dono nomeado, e o gatilho que abre a próxima fase. É gate obrigatório do `launch-producer` no `config.yaml` e a barreira que garante que a pista inteira está construída antes da largada.

## Dono & Escopo
- **owner_agent:** `launch-producer` (verifica a prontidão fase a fase). O `voice-style-guardian` garante a copy aprovada na voz; o `funnel-architect` garante o funil sem becos para as fases de venda.
- **Artefato inspecionado:** o `launch-phases` e o `run-of-show` registrados no [`decision-registry`](../../data/registries/decision-registry.md), cruzados com a copy pronta (`vsl-webinar-script`, `email-sms-sequences`) e o `funnel-map`. Gate obrigatório conforme `config.yaml: routing.build-run-of-show`.

## Condição de Passagem
Cada fase do lançamento tem seu ativo pronto e aprovado, um dono nomeado e o gatilho de transição para a fase seguinte definido.

## Itens
1. **Fases na ordem do desejo.** Verificar: as Fases I–VIII estão sequenciadas para provar antes de pedir o dinheiro (`runway-and-phases`).
2. **Ativo pronto por fase.** Verificar: cada fase tem seu conteúdo (e-mail, VSL/webinar, página) existente, não placeholder.
3. **Voz aprovada.** Verificar: a copy de cada fase carrega o veredito de voz aprovado do `voice-style-guardian`.
4. **Dono por fase.** Verificar: cada fase tem um responsável nomeado por sua execução.
5. **Gatilho de transição.** Verificar: cada fase define o gatilho que abre a próxima (data, ação, evento), sem buraco na linha do tempo.
6. **Funil pronto para as fases de venda.** Verificar: as fases de carrinho apontam para um `funnel-map` sem becos sem saída.
7. **Sem disparo de peça inexistente.** Verificar: nenhuma fase agenda o disparo de um ativo que ainda não existe.

## Evidência Exigida
Para marcar ✅: linkar o `launch-phases` com o ativo e o dono por fase (itens 2, 4), os vereditos de voz (item 3), os gatilhos de transição na linha do tempo (item 5) e a ligação das fases de venda ao `funnel-map` (item 6). As decisões de fase apontam para o `decision-registry`.

## Protocolo de Falha
Item vermelho → o `launch-producer` **marca a fase como bloqueada** ("bloqueado por <input>") e **não publica** horários firmes até o ativo chegar; peça inexistente devolve ao Chief. Copy sem aprovação de voz volta ao [`voice-style-guardian`](../../agents/voice-style-guardian.md); funil com beco volta ao [`funnel-architect`](../../agents/funnel-architect.md). A capacidade do pico é tratada no [`launch-surge-gate`](launch-surge-gate.md); os planos B no [`launch-fallback-gate`](launch-fallback-gate.md). Re-entrada: completar os ativos, confirmar a voz, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`launch/product-launch-formula`](../../frameworks/launch/product-launch-formula.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md) · [`launch/surge-ops`](../../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`launch-producer`](../../agents/launch-producer.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md) · [`funnel-architect`](../../agents/funnel-architect.md)
- Gates irmãos: [`launch-objective-gate`](launch-objective-gate.md) · [`launch-roles-gate`](launch-roles-gate.md) · [`launch-surge-gate`](launch-surge-gate.md) · [`launch-fallback-gate`](launch-fallback-gate.md)
