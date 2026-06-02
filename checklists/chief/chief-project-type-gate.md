---
id: checklist.chief.chief-project-type-gate
title: "Gate — Project Type Classificado (um dos sete, com escopo em uma frase)"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [power-of-one, awareness-x-sophistication]
registries: [decision-registry, offer-registry]
tags: [gate, chief, project-type, d0, intake, scope, roteamento]
---

# Gate — Project Type Classificado

## Propósito
Este gate prova que o `offerbook-chief` classificou o caso em **um único project type** antes de acionar qualquer agente a jusante. Existe porque o tipo errado desperdiça o squad: rodar um `full-launch` numa oferta não validada queima a lista, e tratar um lançamento provado como `offer-book` só deixa dinheiro na mesa. O tipo define o composite do `config.yaml` (a sequência de tasks), os gates obrigatórios e a profundidade da pesquisa. Sem esta classificação travada, o pipeline não tem forma. É o primeiro portão do squad: nada roda sem ele verde.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (única autoridade que classifica e trava o tipo).
- **Artefato inspecionado:** a **decisão de project type** gravada em [`decision-registry`](../../data/registries/decision-registry.md), derivada do `briefing.raw-offer` e da frase de escopo, junto da oferta-semente em [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O caso está classificado em exatamente um dos sete project types, com a frase de escopo travada e o composite do pipeline nomeado.

## Itens
1. **Tipo único escolhido.** Verificar: o `decision-registry` registra exatamente UM de `offer-book · single-promo · full-launch · offer-ladder · enterprise-deal-book · relaunch · continuity-launch` — nunca dois.
2. **Frase de escopo presente.** Verificar: o campo de escopo cabe em uma frase no formato "Transformar [oferta] para [avatar] em [entregável], até [prazo]".
3. **Composite mapeado.** Verificar: o tipo aponta para um composite real do `config.yaml` (ex.: `single-promo → run-single-promo`); o nome bate exatamente.
4. **Alternativas podadas registradas.** Verificar: o registro lista ≥2 tipos candidatos descartados, cada um com o motivo da poda (risco, maturidade da oferta, ROI, prazo).
5. **Maturidade da oferta declarada.** Verificar: o registro diz se a oferta é "validada/provada" ou "não validada" — e o tipo é coerente (não validada + prazo curto → tier menor).
6. **Gates obrigatórios listados.** Verificar: a decisão nomeia os gates de fase que o tipo exige, incluindo o HARD STOP [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) quando há copy.
7. **Inputs mínimos do briefing presentes.** Verificar: mercado-alvo, dor e meta de receita estão no briefing; se faltar qualquer um, o gate fica vermelho e o caso volta ao solicitante.

## Evidência Exigida
Para marcar cada item ✅, linkar a linha do [`decision-registry`](../../data/registries/decision-registry.md) com `{decision_id, project_type, escopo_1_frase, composite, alternativas_podadas, motivo}` e a oferta-semente em [`offer-registry`](../../data/registries/offer-registry.md). O permalink da linha do registry conta como evidência. A frase de escopo precisa estar literalmente escrita, não parafraseada.

## Protocolo de Falha
Item vermelho → o `offerbook-chief` **não aciona D1** e corrige a classificação. Se o briefing não permite travar uma frase de escopo (falta mercado, dor ou meta), o chief devolve ao solicitante com 3 perguntas objetivas, conforme a task `intake-and-scope` — nunca inventa escopo. Tipo super-dimensionado (full-launch em oferta crua) → rebaixa o tier e re-registra. Re-entrada: corrigida a classificação e atualizado o `decision-registry`, o gate é re-submetido. Override só com decisão humana explícita gravada no registry.

## Links
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`offerbook-chief`](../../agents/offerbook-chief.md) · [`offer-squad-architect`](../../agents/offer-squad-architect.md)
- Próximo gate (mesma fase): [`chief-scope-approval-gate`](chief-scope-approval-gate.md)
- HARD STOP a jusante: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
