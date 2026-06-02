---
id: checklist.pr.pr-memorable-angle-gate
title: "Gate — Ângulo Memorável (uma narrativa verdadeira que estende a Big Idea e gruda)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
frameworks: [launch/pr-brand-maximization, launch/affiliate-army]
registries: [decision-registry]
tags: [gate, pr, angulo, memoravel, big-idea, lastro, d6]
---

# Gate — Ângulo Memorável

## Propósito
Este gate prova que **o ângulo de PR é memorável, verdadeiro e estende a Big Idea do lançamento**. Ele existe porque um ângulo genérico não gera buzz nem fica na cabeça, e um ângulo sobre conquista inventada destrói a marca na primeira checagem. O `pr-brand-strategist` isola a narrativa que merece ser contada: nasce de um fato lastreado (resultado real, caso com consentimento, endosso verificável), estende a tese travada pelo `big-idea-architect` (não cria uma tese órfã), e é dito numa frase que a imprensa e a audiência repetem. Vale o princípio `one_big_idea`: o ângulo de PR amplia a Big Idea, não inventa outra. No ToT do agente, qualquer ângulo com lastro baixo é descartado **imediatamente** — é o critério eliminatório; entre os lastreados, vence o mais memorável. A alavanca é prova social e autoridade (Cialdini, via o framework). Este gate julga **só o ângulo e seu lastro** — a veracidade do número específico é do `pr-metric-focus-gate`, os canais são do `pr-placement-gate`, e a medição é do `pr-brand-kpi-gate`. Ângulo sobre fato inflado ou tese paralela não passa.

## Dono & Escopo
- **owner_agent:** `pr-brand-strategist` (gera e escolhe o ângulo memorável lastreado).
- **Artefato inspecionado:** a parte de ângulo do `pr-plan` e a `decision.brand-angle`, cruzadas com a `big-idea` (a tese que o ângulo estende) e os fatos lastreados do `offer-book`. O ângulo escolhido e os podados vão ao [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
O ângulo é memorável, nasce de um fato verificável e consentido, e estende a Big Idea travada sem contradizê-la.

## Itens
1. **Fato por trás.** Verificar: o ângulo nasce de um fato lastreado (resultado, caso, endosso) verificável.
2. **Consentimento.** Verificar: casos, depoimentos e endossos têm consentimento/permissão.
3. **Estende a Big Idea.** Verificar: o ângulo amplia a tese travada, sem criar uma tese paralela órfã.
4. **Memorável.** Verificar: o ângulo cabe numa frase que uma pessoa repete para outra.
5. **Apelo de pauta.** Verificar: um jornalista ou podcast pautaria o ângulo.
6. **Lastro como eliminatório.** Verificar: nenhum ângulo de lastro baixo sobreviveu à seleção.

## Evidência Exigida
Para marcar ✅: linkar a `decision.brand-angle` no [`decision-registry`](../../data/registries/decision-registry.md) no formato `{chosen_option (ângulo), alternatives, rationale (veracidade/memorabilidade/fit)}`, mais o fato verificável e o consentimento que lastreiam o ângulo. A `big-idea` que o ângulo estende fica citada.

## Protocolo de Falha
Item vermelho → o `pr-brand-strategist` **não publica** o ângulo sobre fato inflado ou inexistente; re-angula a partir de um fato verificável, ou recomenda construir o ativo (caso/dado) antes. Ângulo órfão (tese paralela) ele realinha à tese travada pelo [`big-idea-architect`](../../agents/big-idea-architect.md). Prova social sem consentimento ele remove até obter permissão e **sinaliza** ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto. O estrategista **não tem veto**, mas recusa publicar narrativa sem lastro e escala ao [`offerbook-chief`](../../agents/offerbook-chief.md) quando não há fato digno de pauta. A veracidade do número é do [`pr-metric-focus-gate`](pr-metric-focus-gate.md). Re-entrada: re-angular sobre um fato lastreado, confirmar o consentimento e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md) · [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`pr-brand-strategist`](../../agents/pr-brand-strategist.md) · [`big-idea-architect`](../../agents/big-idea-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`pr-metric-focus-gate`](pr-metric-focus-gate.md) · [`pr-placement-gate`](pr-placement-gate.md) · [`pr-brand-kpi-gate`](pr-brand-kpi-gate.md) · [`pr-timing-gate`](pr-timing-gate.md)
