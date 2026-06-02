---
id: checklist.launch.launch-roles-gate
title: "Gate — Papéis (cada disparo tem dono, horário e fallback)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [launch/product-launch-formula, launch/runway-and-phases, launch/surge-ops]
registries: [decision-registry]
tags: [gate, launch, papeis, dono, horario, war-room, d6]
---

# Gate — Papéis

## Propósito
Este gate prova que **cada disparo do lançamento tem dono, horário e fallback** — e que ninguém precisa adivinhar quem faz o quê no dia. Ele existe porque o lançamento quebra na execução quando uma tarefa não tem responsável: o e-mail de fechamento não sai, a live abre sem operador, o pagamento cai sem ninguém monitorando. Na disciplina do `launch-producer`, o run-of-show é uma coreografia, e toda coreografia exige papéis atribuídos. Vale o princípio `traceability_before_eloquence`: cada ação tem um nome ao lado, não uma intenção difusa. O gate exige que cada e-mail, live, SMS e gatilho de escassez carregue dono e horário, que o war-room do pico tenha papéis nomeados (pagamento, deliverability, suporte), e que cada papel tenha um substituto se o titular cair. É a barreira contra o caos do dia do lançamento.

## Dono & Escopo
- **owner_agent:** `launch-producer` (atribui papéis e horários no run-of-show). O `offerbook-chief` arbitra conflitos de calendário entre lançamento, eventos, afiliados e PR.
- **Artefato inspecionado:** o `run-of-show` e o `launch-memo` com a matriz de papéis registrada no [`decision-registry`](../../data/registries/decision-registry.md), incluindo o war-room do `surge-plan` e os handoffs para eventos, afiliados e PR.

## Condição de Passagem
Cada disparo e cada posto do war-room tem dono nomeado, horário definido e um substituto de fallback.

## Itens
1. **Dono por disparo.** Verificar: cada e-mail, live, SMS e gatilho de escassez no run-of-show tem um responsável nomeado.
2. **Horário por disparo.** Verificar: cada ação tem horário cravado, sem "em algum momento do dia".
3. **War-room nomeado.** Verificar: o pico tem papéis atribuídos — quem monitora pagamento, deliverability e suporte.
4. **Substituto por papel.** Verificar: cada papel crítico tem um fallback humano se o titular cair.
5. **Sem colisão de pessoa.** Verificar: nenhuma pessoa é dona de dois disparos simultâneos no mesmo minuto.
6. **Handoffs atribuídos.** Verificar: os repasses a eventos, afiliados e PR têm dono e janela definidos.
7. **Escalonamento definido.** Verificar: há um caminho de escalonamento ao `offerbook-chief` para conflito que o produtor não resolve.

## Evidência Exigida
Para marcar ✅: linkar a matriz disparo→dono→horário do run-of-show (itens 1–2), os papéis do war-room (item 3), o mapa de substitutos (item 4) e a tabela de handoffs com dono (item 6). A decisão de papéis aponta para o `decision-registry`.

## Protocolo de Falha
Item vermelho → o `launch-producer` **atribui o dono, o horário e o substituto** faltantes; disparo sem responsável não entra no run-of-show. Colisão de pessoa no mesmo minuto é redistribuída. Conflito de calendário entre lançamento, eventos, afiliados e PR escala-se ao [`offerbook-chief`](../../agents/offerbook-chief.md). A prontidão de ativos por fase é tratada no [`launch-phase-readiness-gate`](launch-phase-readiness-gate.md); os fallbacks técnicos do pico no [`launch-surge-gate`](launch-surge-gate.md) e no [`launch-fallback-gate`](launch-fallback-gate.md). Re-entrada: completar a matriz de papéis, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`launch/product-launch-formula`](../../frameworks/launch/product-launch-formula.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md) · [`launch/surge-ops`](../../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`launch-producer`](../../agents/launch-producer.md) · [`offerbook-chief`](../../agents/offerbook-chief.md) · [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md)
- Gates irmãos: [`launch-objective-gate`](launch-objective-gate.md) · [`launch-phase-readiness-gate`](launch-phase-readiness-gate.md) · [`launch-surge-gate`](launch-surge-gate.md) · [`launch-fallback-gate`](launch-fallback-gate.md)
