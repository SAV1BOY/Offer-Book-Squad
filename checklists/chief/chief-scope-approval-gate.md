---
id: checklist.chief.chief-scope-approval-gate
title: "Gate — Escopo Aprovado e Travado em Uma Frase (sem scope creep)"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [power-of-one, money-model-sequence]
registries: [decision-registry]
tags: [gate, chief, scope, one-sentence, d0, scope-creep, handoff]
---

# Gate — Escopo Aprovado e Travado

## Propósito
Este gate prova que o escopo do caso cabe em **uma frase** e foi aprovado pelo `offerbook-chief` antes do handoff para o `offer-squad-architect`. Existe porque escopo elástico é o modo de falha mais caro do squad: cada palavra a mais convida um entregável a mais, e o lançamento incha até quebrar na execução. O princípio `power-of-one` manda UMA tese, UM avatar, UM próximo passo. Este gate é o contrato que todo agente a jusante herda: o que está dentro e o que está fora. Sem ele verde, o pipeline corre sem fronteira.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (aprova e trava o escopo; é dono do veto de scope creep).
- **Artefato inspecionado:** a **frase de escopo travada** (`decision.scope-one-sentence`) gravada em [`decision-registry`](../../data/registries/decision-registry.md), com a lista explícita de inclusões e exclusões do caso.

## Condição de Passagem
O escopo está escrito em uma única frase, aprovado pelo chief, com fronteira de dentro/fora explícita e coerente com o project type.

## Itens
1. **Uma frase, sem conjunção elástica.** Verificar: o escopo é uma frase só; não há "e também", "além de", "depois a gente vê" que multiplique entregáveis.
2. **Os quatro elementos presentes.** Verificar: a frase nomeia oferta, avatar, entregável e prazo (formato "Transformar [oferta] para [avatar] em [entregável], até [prazo]").
3. **Fronteira de exclusão escrita.** Verificar: existe uma lista "fora do escopo" com ≥2 itens explicitamente excluídos (o que o caso NÃO vai produzir).
4. **Coerência com o project type.** Verificar: o entregável da frase bate com o tipo travado no [`chief-project-type-gate`](chief-project-type-gate.md) (ex.: `offer-book` não promete VSL).
5. **Avatar único.** Verificar: a frase aponta para UM avatar/mercado; se aponta para dois, o gate fica vermelho e o caso é bifurcado ou priorizado.
6. **Aprovação registrada.** Verificar: o `decision-registry` marca o escopo como `approved` pelo `offerbook-chief` com `decision_id` e data.

## Evidência Exigida
Para marcar cada item ✅, linkar a linha do [`decision-registry`](../../data/registries/decision-registry.md) contendo a frase de escopo literal, a lista de exclusões e o carimbo `approved`. A frase precisa aparecer entre aspas, idêntica à que será passada ao `offer-squad-architect`. O permalink da linha conta como evidência.

## Protocolo de Falha
Item vermelho → o `offerbook-chief` re-trava o escopo em uma frase e corta o que não serve à decisão. Escopo que aponta para dois avatares → devolve ao solicitante para priorizar ou bifurca em dois casos. Pedido posterior de "só mais uma coisa" durante o pipeline → o chief aciona o poder de veto de scope creep, registra a tentativa e mantém a frase original; mudança real de escopo exige reabrir este gate e re-aprovar. Re-entrada: corrigida a frase e re-aprovada no registry, o handoff é liberado.

## Links
- Frameworks: [`power-of-one`](../../frameworks/power-of-one.md) · [`money-model-sequence`](../../frameworks/money-model-sequence.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`offerbook-chief`](../../agents/offerbook-chief.md) · [`offer-squad-architect`](../../agents/offer-squad-architect.md)
- Gate anterior (mesma fase): [`chief-project-type-gate`](chief-project-type-gate.md)
- Conflitos de escopo: [`chief-conflict-resolution-gate`](chief-conflict-resolution-gate.md)
