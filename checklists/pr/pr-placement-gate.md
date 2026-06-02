---
id: checklist.pr.pr-placement-gate
title: "Gate — Placement (cada canal mapeado com ativo lastreado e consentido)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
frameworks: [launch/pr-brand-maximization, launch/affiliate-army]
registries: [decision-registry]
tags: [gate, pr, placement, canais, midia-ganha, ativos, d6]
---

# Gate — Placement

## Propósito
Este gate prova que **cada canal de PR está mapeado com o ativo certo, lastreado e consentido**. Ele existe porque um ângulo memorável sem canal não alcança ninguém: precisa de um plano de onde a narrativa chega e com qual peça. O `pr-brand-strategist` mapeia os focos — mídia ganha (imprensa de nicho), autoridade do fundador (podcasts, palcos), prova social interna (recapitular o resultado para a base e o próximo lançamento), e parceiros do Dream 100 como multiplicadores de PR/co-marketing (via `affiliate-army`). Para cada canal, define o ativo (press angle, estudo de caso, conteúdo de autoridade, depoimento), e cada ativo é lastreado e consentido. Vale o princípio `decision_before_ornament`: cada canal serve a um objetivo de alcance ou autoridade. No ToT do agente, o foco com pior relação esforço×durabilidade para o estágio da marca é podado. Este gate julga **só os canais e os ativos** — a memorabilidade do ângulo é do `pr-memorable-angle-gate`, a veracidade dos números é do `pr-metric-focus-gate`, e a cadência/janela é do `pr-timing-gate`. Uso de nome/logo de cliente sem permissão formal não passa.

## Dono & Escopo
- **owner_agent:** `pr-brand-strategist` (mapeia canais e define os ativos de PR).
- **Artefato inspecionado:** a parte de canais e ativos do `pr-plan`, cruzada com o `affiliate-program` (parceiros como canal) e os fatos lastreados do `offer-book`. As decisões de foco de canal vão ao [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
Cada canal de PR tem um ativo definido, lastreado e consentido, com foco adequado ao estágio da marca.

## Itens
1. **Canais mapeados.** Verificar: os focos estão definidos (mídia ganha, autoridade do fundador, prova social interna, parceiros).
2. **Ativo por canal.** Verificar: cada canal tem o ativo certo (press angle, caso, conteúdo, depoimento).
3. **Ativos lastreados.** Verificar: cada ativo nasce de um fato verificável (não buzz inventado).
4. **Consentimento de uso.** Verificar: nome/logo/depoimento de cliente têm permissão formal.
5. **Parceiros como canal.** Verificar: os parceiros do Dream 100 que fazem co-marketing/endosso estão identificados.
6. **Foco por estágio.** Verificar: o foco escolhido bate com o estágio da marca (esforço × durabilidade).

## Evidência Exigida
Para marcar ✅: linkar a parte de canais do `pr-plan` com, por canal, `{ativo, lastro, consentimento}`, mais a confirmação de permissão de uso para nome/logo/depoimento. O `affiliate-program` que aponta os parceiros como canal e a decisão de foco no [`decision-registry`](../../data/registries/decision-registry.md) ficam citados.

## Protocolo de Falha
Item vermelho → o `pr-brand-strategist` **não publica** o ativo sem lastro ou sem consentimento; uso de nome/logo de cliente sem permissão formal ele remove até obter autorização e **sinaliza** ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto. Canal sem ativo definido ele completa antes de declarar o plano pronto. O estrategista **não tem veto**, mas recusa publicar placement sobre ativo podre. Foco mal escolhido para o estágio da marca ele re-prioriza. A janela em que cada canal dispara é do [`pr-timing-gate`](pr-timing-gate.md). Re-entrada: definir o ativo de cada canal, obter consentimento e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md) · [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`pr-brand-strategist`](../../agents/pr-brand-strategist.md) · [`affiliate-program-architect`](../../agents/affiliate-program-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`pr-memorable-angle-gate`](pr-memorable-angle-gate.md) · [`pr-metric-focus-gate`](pr-metric-focus-gate.md) · [`pr-brand-kpi-gate`](pr-brand-kpi-gate.md) · [`pr-timing-gate`](pr-timing-gate.md)
