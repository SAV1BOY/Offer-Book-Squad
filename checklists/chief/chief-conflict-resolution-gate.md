---
id: checklist.chief.chief-conflict-resolution-gate
title: "Gate — Conflito entre Agentes Resolvido com Decisão Registrada (o pipeline não trava)"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [power-of-one, value-equation, money-model-sequence]
registries: [decision-registry]
tags: [gate, chief, conflito, veto, d0, escalonamento, decisao]
---

# Gate — Conflito entre Agentes Resolvido

## Propósito
Este gate prova que, quando dois agentes entram em desacordo, o `offerbook-chief` decidiu de forma rastreável e o pipeline voltou a andar. Existe porque o squad tem três agentes com poder de veto (`value-equation-engineer`, `money-model-designer`, `compliance-auditor`) e um veto sobreposto a outro trava o lançamento. O chief é o árbitro único: ele não escreve copy nem desenha oferta, mas decide quem tem razão quando há choque, e registra o porquê. Sem este gate, um impasse vira paralisia silenciosa — ninguém sabe quem manda, e o caso para. O gate transforma o conflito em decisão documentada, reutilizável e auditável.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (árbitro único de conflitos entre agentes).
- **Artefato inspecionado:** a **decisão de resolução** gravada em [`decision-registry`](../../data/registries/decision-registry.md), contendo os dois lados, a posição escolhida, o motivo e o ponto de re-entrada do pipeline.

## Condição de Passagem
O conflito está nomeado, a decisão do chief está registrada com motivo, e o agente que perdeu o ponto recebeu instrução clara de re-entrada.

## Itens
1. **Conflito nomeado.** Verificar: o registro identifica os **dois agentes** em desacordo e o objeto exato da disputa (ex.: componente que um veta e o outro quer manter).
2. **Posições documentadas.** Verificar: a posição de cada lado está escrita em uma frase, com a evidência que cada um alega — não "achismo".
3. **Tipo de conflito classificado.** Verificar: o registro marca se é conflito de **veto** (ex.: `value-equation-engineer` vs `money-model-designer` sobre componente órfão), de escopo, ou de sequência.
4. **Decisão única tomada.** Verificar: o chief escolheu exatamente UMA resolução, alinhada a `power-of-one`; não há "fazemos os dois".
5. **Motivo rastreável.** Verificar: a decisão cita o princípio ou a evidência que a justifica (ex.: `value_equation_test`, `money_model_spine`, `truthful_scarcity`).
6. **Re-entrada definida.** Verificar: o registro diz a qual task/agente o pipeline retorna e o que o lado vencido deve ajustar.
7. **Override marcado quando aplicável.** Verificar: se a decisão sobrepõe um veto legítimo, está marcada como `override` com a razão estratégica explícita.

## Evidência Exigida
Para marcar cada item ✅, linkar a linha do [`decision-registry`](../../data/registries/decision-registry.md) com `{decision_id, agentes_em_conflito, posicoes, tipo, resolucao, motivo, re_entrada, override?}`. As duas posições precisam aparecer literalmente, não parafraseadas pelo chief. O permalink da linha do registry conta como evidência da resolução.

## Protocolo de Falha
Item vermelho → o conflito **não está resolvido** e o pipeline permanece parado no ponto de impasse; o chief completa o registro antes de liberar. Conflito de veto irreconciliável por evidência insuficiente → o chief devolve aos dois agentes pedindo a evidência que falta, conforme o princípio `evidence_before_opinion`. Risco estratégico acima da alçada do chief → escalona ao humano/advisory e marca a decisão como pendente. Re-entrada: gravada a decisão com motivo e ponto de retorno, o agente vencido ajusta seu artefato e o pipeline retoma na task indicada. Override de veto só vale com razão registrada — sem registro, o veto original prevalece.

## Links
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`value-equation`](../../frameworks/value-equation.md) · [`money-model-sequence`](../../frameworks/money-model-sequence.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`offerbook-chief`](../../agents/offerbook-chief.md) · [`value-equation-engineer`](../../agents/value-equation-engineer.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gate de escopo (fonte comum de conflito): [`chief-scope-approval-gate`](chief-scope-approval-gate.md)
- Veto de valor relacionado: [`value-no-orphan-lever-gate`](../value/value-no-orphan-lever-gate.md)
