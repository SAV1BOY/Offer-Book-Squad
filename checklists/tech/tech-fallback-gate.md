---
id: checklist.tech.tech-fallback-gate
title: "Gate — Fallback Técnico (cada ponto crítico tem plano B testado)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: tech-links-deliverability-engineer
frameworks: [launch/surge-ops]
registries: [decision-registry]
tags: [gate, tech, fallback, plano-b, contingencia, resiliencia, d5]
---

# Gate — Fallback Técnico

## Propósito
Este gate prova que **cada ponto técnico crítico do dia tem um plano B testado, não teórico**. Ele existe porque o que pode quebrar vai quebrar no pico: a página de checkout cai, o gateway de pagamento engasga, o e-mail é bloqueado, o 3PL não confirma estoque. O `tech-links-deliverability-engineer` desenha e **testa** um fallback por ponto crítico — página estática de "vaga reservada", link de pagamento reserva, rota de e-mail alternativa, fila manual com e-mail de confirmação tardia — para que uma falha não vire receita perdida. Vale o princípio `contradiction_before_conclusion`: antes de declarar pronto, pergunta-se "se o gateway cair às 20h do carrinho fechando, o cliente perde a compra ou é recuperado?". Um fallback teórico não conta: ele precisa ter sido testado. Este gate é o complemento técnico do [`launch-fallback-gate`](../launch/launch-fallback-gate.md) do `launch-producer`, e valida os fallbacks que entram no run-of-show. A capacidade que tenta evitar o estouro é do `tech-load-test-gate`; este gate cobre o que acontece **quando ainda assim falha**. Fallback nunca vira pretexto de escassez falsa.

## Dono & Escopo
- **owner_agent:** `tech-links-deliverability-engineer` (desenha e testa o plano B por ponto crítico). O [`launch-producer`](../../agents/launch-producer.md) integra os fallbacks no run-of-show.
- **Artefato inspecionado:** a seção de fallback do `tech-deliverability-plan`, cruzada com o `surge-plan` do run-of-show. O resultado vai ao [`decision-registry`](../../data/registries/decision-registry.md). Gate consumido em `config.yaml: routing.plan-tech-deliverability`.

## Condição de Passagem
Cada ponto técnico crítico tem um plano B testado e acionável, sem usar a falha como pretexto de escassez falsa.

## Itens
1. **Fallback de página.** Verificar: existe página estática/espelho ("alta demanda, vaga reservada") se o checkout cair.
2. **Pagamento reserva.** Verificar: há link/gateway de pagamento alternativo testado.
3. **Rota de e-mail alternativa.** Verificar: existe provedor/rota de envio reserva se o principal travar no pico.
4. **Fallback de 3PL/logística.** Verificar: se o 3PL não confirma estoque, o pedido entra em fila manual + e-mail de confirmação tardia.
5. **Cada fallback testado.** Verificar: nenhum plano B é teórico; cada um foi acionado em teste.
6. **Gatilho e dono.** Verificar: cada fallback tem um gatilho claro e um dono que decide acioná-lo.
7. **Sem escassez falsa.** Verificar: nenhuma "extensão por instabilidade" dispara sem instabilidade real.

## Evidência Exigida
Para marcar ✅: linkar o registro de fallback no [`decision-registry`](../../data/registries/decision-registry.md) no formato `{ponto_critico, plano_b, testado?}` para cada ponto, mais a evidência do teste de acionamento e a tabela fallback→gatilho→dono. O `surge-plan` do run-of-show onde os fallbacks entram fica citado.

## Protocolo de Falha
Item vermelho → o `tech-links-deliverability-engineer` **desenha e testa** o plano B antes de declarar pronto; ponto crítico sem fallback não vai ao ar. Fallback teórico é re-testado até funcionar de verdade. O engenheiro **não tem veto** sobre o pipeline, mas recusa declarar resiliência sobre um plano B não testado. Qualquer extensão de prazo apresentada como escassez é flag ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto de escassez falsa — não há override para escassez inventada. A capacidade que reduz a chance do estouro é do [`tech-load-test-gate`](tech-load-test-gate.md). Re-entrada: testar cada plano B, atualizar o `decision-registry` e re-submeter ao run-of-show.

## Links
- Frameworks: [`launch/surge-ops`](../../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`launch-producer`](../../agents/launch-producer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`tech-load-test-gate`](tech-load-test-gate.md) · [`tech-deliverability-gate`](tech-deliverability-gate.md) · [`tech-anti-loop-gate`](tech-anti-loop-gate.md) · [`tech-links-utm-gate`](tech-links-utm-gate.md)
- Relacionado: [`launch-fallback-gate`](../launch/launch-fallback-gate.md)
