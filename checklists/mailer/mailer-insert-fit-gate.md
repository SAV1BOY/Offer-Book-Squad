---
id: checklist.mailer.mailer-insert-fit-gate
title: "Gate — Fit do Insert ao Degrau (cada insert entra no degrau certo da escada)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: direct-mail-insert-writer
frameworks: [offer-stack-builder, scarcity-urgency-engine]
registries: [control-registry]
tags: [gate, mailer, insert, degrau, money-model, ascensao, d4]
---

# Gate — Fit do Insert ao Degrau

## Propósito
Este gate prova que **cada insert físico entra no degrau certo da escada do money model**: o que entra na caixa do front-end fala de boas-vindas e ativação, o que entra na do upsell celebra a compra e ascende, e o da continuidade reforça pertencimento. Ele existe porque um insert no degrau errado quebra a sequência: uma oferta de continuidade na caixa do front-end soa fora de hora, e um insert que pula um degrau confunde o cliente. O `direct-mail-insert-writer` materializa cada peça por degrau, porque o insert depende de **onde** o cliente acabou de comprar. Vale o princípio `step_before_eloquence`: o degrau define a mensagem, não o contrário. Cada insert mapeia um degrau declarado (front-end, upsell, downsell, continuidade), responde a objeção dominante daquele degrau e ascende ao próximo passo da escada na hora certa. Este gate julga **só o encaixe ao degrau** — se as specs de produção estão completas é do `mailer-spec-gate`, se o QR rastreia é do `mailer-cta-trackable-gate`, e se a oferta resumida bate com a Big Idea é do `mailer-offer-coherence-gate`. Um upsell sem margem validada não vira insert: o writer suspende a peça até o sinal verde da unit economics.

## Dono & Escopo
- **owner_agent:** `direct-mail-insert-writer` (mapeia cada insert ao degrau correto da escada do money model).
- **Artefato inspecionado:** o campo `degrau` de cada insert em `artifact.mailers-inserts`, cruzado com a escada do `artifact.money-model`, registrado no [`control-registry`](../../data/registries/control-registry.md). A margem de cada upsell é validada com o [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md); a escada vem do [`money-model-designer`](../../agents/money-model-designer.md).

## Condição de Passagem
Cada insert declara um degrau da escada, fala a mensagem própria daquele degrau, responde a objeção dominante dele e ascende ao próximo passo na hora certa.

## Itens
1. **Degrau declarado.** Verificar: cada insert tem o campo `degrau` preenchido (front-end, upsell, downsell ou continuidade).
2. **Mensagem do degrau.** Verificar: a copy corresponde ao degrau — front-end ativa, upsell celebra e ascende, continuidade reforça pertencimento.
3. **Objeção do degrau.** Verificar: o insert responde a objeção dominante daquele degrau, lida do `objection-registry`.
4. **Ascensão na ordem.** Verificar: o insert ascende ao **próximo** degrau da escada, sem pular etapas nem voltar.
5. **Sem insert órfão.** Verificar: não há insert sem degrau correspondente na escada do money model.
6. **Upsell com margem.** Verificar: qualquer insert que empurra um upsell tem a margem validada pela unit economics.

## Evidência Exigida
Para marcar ✅: linkar, por insert, o campo `degrau` e a `objecao_alvo` no [`control-registry`](../../data/registries/control-registry.md), cruzados com a escada do `money-model`. A validação de margem do upsell pelo [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) fica citada para os inserts de ascensão.

## Protocolo de Falha
Item vermelho → o `direct-mail-insert-writer` **realinha o insert ao degrau correto** da escada antes de mandar à produção. Insert no degrau errado (continuidade na caixa do front-end) ele move para o degrau certo. Upsell sem margem validada ele **suspende** e sinaliza ao [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md). Sem a escada definida, ele para e pede ao [`money-model-designer`](../../agents/money-model-designer.md) — não há como ramificar inserts por degrau sem ela. O writer **não tem veto**; escalona ao [`offerbook-chief`](../../agents/offerbook-chief.md). Se as specs faltam é do [`mailer-spec-gate`](mailer-spec-gate.md). Re-entrada: corrigir o `degrau`, validar a margem e re-submeter ao control-registry.

## Links
- Frameworks: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`mailer-spec-gate`](mailer-spec-gate.md) · [`mailer-cta-trackable-gate`](mailer-cta-trackable-gate.md) · [`mailer-offer-coherence-gate`](mailer-offer-coherence-gate.md) · [`mailer-compliance-gate`](mailer-compliance-gate.md)
