---
id: checklist.launch.launch-surge-gate
title: "Gate — Pico (capacidade confirmada e war-room para o dia)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [launch/surge-ops, launch/product-launch-formula, launch/runway-and-phases]
registries: [decision-registry]
tags: [gate, launch, surge, pico, capacidade, war-room, d6]
---

# Gate — Pico

## Propósito
Este gate prova que o **pico do lançamento tem capacidade confirmada e um war-room pronto** — para que o momento de maior tráfego (em geral o fechamento de carrinho) não derrube a página, o pagamento ou a entrega. Ele existe porque o sucesso do lançamento se concentra em poucas horas: se a página cai no minuto do pico, a receita evapora. Na disciplina de `surge-ops` do `launch-producer`, o pico é planejado como uma operação, não torcido. O gate exige que a capacidade técnica esteja confirmada contra o tráfego projetado, que o war-room tenha postos de monitoramento (pagamento, deliverability, suporte) e que o teto e o gatilho de fallback estejam definidos antes do dia. É gate obrigatório do `launch-producer` no `config.yaml`. Os planos B propriamente ditos são detalhados no gate irmão de fallback; aqui se prova que o pico foi dimensionado e tem quem o vigie.

## Dono & Escopo
- **owner_agent:** `launch-producer` (planeja a operação de pico). O `tech-links-deliverability-engineer` confirma a capacidade física e os limites de envio.
- **Artefato inspecionado:** o `surge-plan` dentro do `run-of-show`, registrado no [`decision-registry`](../../data/registries/decision-registry.md), cruzado com o `tech-deliverability-plan` (capacidade, janelas, URLs). Gate obrigatório conforme `config.yaml: routing.build-run-of-show`.

## Condição de Passagem
A capacidade técnica do pico está confirmada contra o tráfego projetado e o war-room tem postos de monitoramento e gatilho de fallback definidos.

## Itens
1. **Tráfego projetado.** Verificar: o plano estima o pico (ex.: 3x o tráfego médio) na janela crítica.
2. **Capacidade confirmada.** Verificar: o `tech-deliverability-plan` confirma que a infra aguenta o pico projetado.
3. **Limite de envio respeitado.** Verificar: a cadência de e-mail/SMS no pico não estoura o limite de deliverability.
4. **War-room com postos.** Verificar: há monitores nomeados para pagamento, deliverability e suporte durante o pico.
5. **Teto e gatilho de fallback.** Verificar: o plano define o teto de carga e o gatilho que aciona o fallback.
6. **Janela crítica minuto a minuto.** Verificar: o run-of-show da janela de pico está cravado (ex.: e-mails de contagem regressiva).
7. **Capacidade ≠ suposição.** Verificar: a confirmação vem do engenheiro de tech, não de um palpite do produtor.

## Evidência Exigida
Para marcar ✅: linkar a estimativa de tráfego e a confirmação de capacidade do `tech-deliverability-plan` (itens 1–2), a cadência dentro do limite de envio (item 3), os postos do war-room (item 4) e o teto/gatilho de fallback (item 5). O plano de pico aponta para o `decision-registry`.

## Protocolo de Falha
Item vermelho → o `launch-producer` **não publica** o run-of-show até a capacidade ser confirmada e o war-room ter postos; pico sem plano não vai ao ar. Capacidade não confirmada escala-se ao [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) e ao [`offerbook-chief`](../../agents/offerbook-chief.md) antes de marcar a data. Cadência que estoura o limite de envio é redistribuída com o tech. Os planos B (página espelho, link reserva) são detalhados no [`launch-fallback-gate`](launch-fallback-gate.md). Re-entrada: confirmar capacidade, definir war-room e teto, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`launch/surge-ops`](../../frameworks/launch/surge-ops.md) · [`launch/product-launch-formula`](../../frameworks/launch/product-launch-formula.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`launch-producer`](../../agents/launch-producer.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`launch-objective-gate`](launch-objective-gate.md) · [`launch-roles-gate`](launch-roles-gate.md) · [`launch-phase-readiness-gate`](launch-phase-readiness-gate.md) · [`launch-fallback-gate`](launch-fallback-gate.md)
