---
id: checklist.positioning.positioning-descends-to-copy-gate
title: "Gate — Posição e Lead Descem Limpos para a Copy"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [positioning/moore-positioning-formula, lead-types, awareness-x-sophistication, positioning/category-design]
registries: [decision-registry]
tags: [gate, positioning, handoff, copy, lead, descida, d3]
---

# Gate — Posição e Lead Descem Limpos para a Copy

## Propósito
Este gate prova que a posição e o lead travados **descem inteiros para a copy** — que os agentes de copy a jusante recebem uma moldura completa e não precisam "escolher" a abertura por conta própria. Ele existe porque o ponto de vazamento do posicionamento é o handoff: se a categoria, o atributo único, a fórmula de Moore e o lead não chegam juntos e explícitos, cada redator preenche os buracos do seu jeito e a oferta perde a unidade que o `positioning-lead-strategist` travou. O gate materializa o contrato de §9 do agente: o [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md), o [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md), o [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md) e o [`ad-creative-factory`](../../agents/ad-creative-factory.md) recebem (1) a categoria de referência e o atributo único, (2) a fórmula de Moore pronta para virar headline/abertura, e (3) **o lead travado** com a justificativa de consciência. Diferente dos gates que auditam a qualidade da decisão (categoria, diferenciação, fit do lead), este audita a **transmissão**: o pacote está completo, é consumível e respeita o HARD STOP do Offer Book DoD. É o último portão do estrategista antes de a copy aplicar a moldura.

## Dono & Escopo
- **owner_agent:** `positioning-lead-strategist` (decisor vinculante; sua decisão de lead prevalece sobre os agentes de copy, mas ele registra a divergência).
- **Artefato inspecionado:** o **`artifact.positioning`** completo e as decisões `positioning-locked` + `lead-type-locked` no [`decision-registry`](../../data/registries/decision-registry.md) — o pacote que os agentes de copy consomem a jusante.

## Condição de Passagem
Os agentes de copy recebem categoria, atributo único, fórmula de Moore completa e lead travado com justificativa de consciência, tudo registrado e liberado somente após o Offer Book DoD.

## Itens
1. **Pacote de posição completo.** Verificar: a categoria de referência e o `atributo_unico` estão no `artifact.positioning`, prontos para a copy — nenhum campo pendente.
2. **Fórmula pronta para headline.** Verificar: a `moore_formula` está completa e em forma utilizável como abertura/headline, sem placeholder.
3. **Lead travado e nomeado.** Verificar: o `lead_type` é um dos seis e está travado com `lead_justificativa` de consciência — o redator não escolhe a abertura.
4. **Por segmento quando preciso.** Verificar: se o lançamento mistura consciências (lista quente + tráfego frio), o lead foi entregue **por segmento**, não uma abertura única para todos.
5. **Gates a montante verdes.** Verificar: [`positioning-category-gate`](positioning-category-gate.md), [`positioning-differentiation-gate`](positioning-differentiation-gate.md), [`positioning-lead-choice-gate`](positioning-lead-choice-gate.md) e [`positioning-awareness-fit`](positioning-awareness-fit.md) estão verdes antes da descida.
6. **Respeita o HARD STOP.** Verificar: o pacote só é liberado à copy **após** o Offer Book DoD — o estrategista trava antes, a copy aplica depois.
7. **Decisões registradas e rastreáveis.** Verificar: `positioning-locked` e `lead-type-locked` estão no [`decision-registry`](../../data/registries/decision-registry.md) com `big_idea_ref`, e os agentes de copy a jusante apontam para esses ids.

## Evidência Exigida
Para marcar cada item ✅, linkar o `artifact.positioning` completo (categoria, atributo único, fórmula de Moore, lead, justificativa) e as decisões `positioning-locked` + `lead-type-locked` no [`decision-registry`](../../data/registries/decision-registry.md) com `big_idea_ref`. Os quatro gates irmãos verdes são a evidência-resumo de que a moldura está madura; o ponteiro de que a liberação ocorreu após o Offer Book DoD confirma o respeito ao HARD STOP. Quando há multi-consciência, a matriz de lead por segmento é a evidência exigida.

## Protocolo de Falha
Item vermelho → o pacote não desce. Campo pendente na posição ou na fórmula → o estrategista completa antes de liberar; a copy não recebe moldura furada. Lead não travado ou sem justificativa → volta ao [`positioning-awareness-fit`](positioning-awareness-fit.md) e ao [`positioning-lead-choice-gate`](positioning-lead-choice-gate.md) antes da descida. Liberação antes do Offer Book DoD → segura o pacote até o DoD; o HARD STOP é inegociável. Conflito com um agente de copy sobre o lead → a decisão do estrategista **prevalece** (é o mandato dele), mas a divergência é registrada no [`decision-registry`](../../data/registries/decision-registry.md); o estrategista **não tem veto** sobre o pipeline. Multi-consciência com abertura única → trava o lead por segmento e reentrega a matriz. Categoria nova que exige prova que o `proof-registry` não tem → sinaliza ao [`offerbook-chief`](../../agents/offerbook-chief.md) e ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). Re-entrada: completo o pacote e verdes os gates a montante, este gate é re-submetido e a copy recebe a moldura.

## Links
- Frameworks: [`moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md) · [`lead-types`](../../frameworks/lead-types.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`category-design`](../../frameworks/positioning/category-design.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) · [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) · [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md) · [`ad-creative-factory`](../../agents/ad-creative-factory.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Template: [`positioning-template`](../../templates/strategy/positioning-template.md)
- Gates irmãos: [`positioning-awareness-fit`](positioning-awareness-fit.md) · [`positioning-lead-choice-gate`](positioning-lead-choice-gate.md) · [`positioning-category-gate`](positioning-category-gate.md) · [`positioning-differentiation-gate`](positioning-differentiation-gate.md)
