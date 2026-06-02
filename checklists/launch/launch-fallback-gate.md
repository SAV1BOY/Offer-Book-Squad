---
id: checklist.launch.launch-fallback-gate
title: "Gate — Fallback (todo ponto de falha do dia tem plano B)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [launch/surge-ops, launch/product-launch-formula, launch/runway-and-phases]
registries: [decision-registry]
tags: [gate, launch, fallback, plano-b, resiliencia, contingencia, d6]
---

# Gate — Fallback

## Propósito
Este gate prova que **todo ponto de falha do dia do lançamento já tem plano B antes de o dia chegar** — página espelho, link de pagamento reserva, rota de e-mail alternativa e protocolo para instabilidade real. Ele existe porque o que pode quebrar vai quebrar no pior momento: a página de checkout cai no pico, o provedor de e-mail trava, o gateway de pagamento engasga. Sem plano B, uma falha técnica vira receita perdida e clientes furiosos. Na disciplina de `surge-ops` do `launch-producer`, a resiliência é planejada, não improvisada. Vale o princípio `contradiction_before_conclusion`: antes de declarar o lançamento pronto, pergunta-se "e se cair?". Este gate também é consumido pelo `tech-links-deliverability-engineer` no `config.yaml`, que valida os fallbacks técnicos. Um ponto crítico de extensão de prazo só vale **se a instabilidade for real** — fallback nunca vira pretexto para escassez falsa.

## Dono & Escopo
- **owner_agent:** `launch-producer` (define os planos B do dia). O `tech-links-deliverability-engineer` valida e implementa os fallbacks técnicos; o `compliance-auditor` veta qualquer extensão de prazo que não seja por instabilidade real.
- **Artefato inspecionado:** a seção de fallbacks do `surge-plan` no `run-of-show`, registrada no [`decision-registry`](../../data/registries/decision-registry.md), cruzada com o `tech-deliverability-plan`. Gate consumido em `config.yaml: routing.plan-tech-deliverability`.

## Condição de Passagem
Cada ponto crítico de falha do dia tem um plano B definido, validado pelo tech e acionável por um gatilho claro, sem usar a falha como pretexto de escassez falsa.

## Itens
1. **Página espelho.** Verificar: existe uma página de checkout/oferta espelho pronta para assumir se a principal cair.
2. **Link de pagamento reserva.** Verificar: há um link/gateway de pagamento alternativo testado.
3. **Rota de e-mail alternativa.** Verificar: existe um provedor/rota de envio reserva se o principal travar no pico.
4. **Gatilho de acionamento.** Verificar: cada fallback tem um gatilho claro e um dono que decide acioná-lo (liga ao war-room).
5. **Extensão só por instabilidade real.** Verificar: qualquer "deadline estendido por instabilidade" só dispara se a instabilidade for **verdadeira** — não é tática de urgência.
6. **Validação do tech.** Verificar: o `tech-links-deliverability-engineer` confirmou que cada fallback funciona, não é teórico.
7. **Comunicação de contingência.** Verificar: há uma mensagem pronta para avisar a lista com honestidade se algo falhar.

## Evidência Exigida
Para marcar ✅: linkar a página espelho e o link reserva testados (itens 1–2), a rota de e-mail alternativa (item 3), a tabela fallback→gatilho→dono (item 4), a regra de extensão só por instabilidade real (item 5) e a validação do tech (item 6). Os fallbacks apontam para o `decision-registry`.

## Protocolo de Falha
Item vermelho → o `launch-producer` **não publica** o run-of-show até cada ponto crítico ter plano B validado; pico sem fallback não vai ao ar. Fallback teórico volta ao [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) para validação real. Qualquer extensão de prazo apresentada como escassez é **vetada** pelo [`compliance-auditor`](../../agents/compliance-auditor.md) — escassez falsa não tem override. A capacidade e o war-room são tratados no [`launch-surge-gate`](launch-surge-gate.md). Re-entrada: validar cada fallback, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`launch/surge-ops`](../../frameworks/launch/surge-ops.md) · [`launch/product-launch-formula`](../../frameworks/launch/product-launch-formula.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`launch-producer`](../../agents/launch-producer.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`launch-objective-gate`](launch-objective-gate.md) · [`launch-roles-gate`](launch-roles-gate.md) · [`launch-phase-readiness-gate`](launch-phase-readiness-gate.md) · [`launch-surge-gate`](launch-surge-gate.md)
