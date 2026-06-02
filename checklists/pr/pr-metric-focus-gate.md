---
id: checklist.pr.pr-metric-focus-gate
title: "Gate — Foco em Métrica (todo número do PR é real, verificável e lastreado)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
frameworks: [launch/pr-brand-maximization, launch/affiliate-army]
registries: [decision-registry]
tags: [gate, pr, metrica, numero, lastro, verificavel, d6]
---

# Gate — Foco em Métrica

## Propósito
Este gate prova que **todo número usado no PR é real, verificável e lastreado — nunca inflado para o press release**. Ele existe porque um número exagerado destrói a credibilidade na primeira checagem do jornalista, e leva tudo ao veto de compliance. O `pr-brand-strategist` ancora cada métrica do ângulo (número de alunos, resultado coletivo, ROI de cliente) num fato catalogado e usa o número **real**, ainda que menor. Vale o princípio `evidence_before_opinion`: a prova social de massa só convence se o número se sustenta. No modo de falha do agente, o número inflado no press release é trocado pelo real — PR exagerado destrói credibilidade. Qualquer ROI de cliente citado precisa do lastro do Offer Book; sem isso, o claim é rebaixado. Este gate é o complemento numérico do `pr-memorable-angle-gate`: o ângulo escolhe a narrativa, este garante que os números dentro dela são honestos. Este gate julga **só a veracidade das métricas** — a memorabilidade do ângulo é do angle-gate, e os KPIs de marca (como medimos o halo) são do `pr-brand-kpi-gate`. Número sem lastro verificável não vai ao press release.

## Dono & Escopo
- **owner_agent:** `pr-brand-strategist` (ancora cada métrica do ângulo num fato verificável).
- **Artefato inspecionado:** as métricas citadas no `pr-plan` (ângulo, press angle, case), cruzadas com os fatos lastreados do `offer-book` e a prova catalogada. Cada número aponta ao [`proof-registry`](../../data/registries/proof-registry.md); claims ao [`claim-registry`](../../data/registries/claim-registry.md); a decisão ao [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
Todo número citado no PR é o número real, verificável e lastreado na prova, sem inflar para o press release.

## Itens
1. **Número real.** Verificar: cada métrica é o valor real, não arredondado para cima nem inflado.
2. **Lastro na prova.** Verificar: cada número aponta a um fato no `proof-registry` ou equivalente.
3. **ROI de cliente lastreado.** Verificar: qualquer ROI/resultado de cliente tem o lastro do Offer Book.
4. **Verificável por terceiro.** Verificar: um jornalista checaria o número e ele se sustentaria.
5. **Sem superlativo vazio.** Verificar: nenhum "o maior", "recorde" sem dado que comprove.
6. **Consentimento do dado.** Verificar: números de cliente específico têm permissão de uso.

## Evidência Exigida
Para marcar ✅: linkar cada métrica do `pr-plan` à sua prova no [`proof-registry`](../../data/registries/proof-registry.md) (e ao [`claim-registry`](../../data/registries/claim-registry.md) quando vira afirmação pública), mais a confirmação de que o número usado é o real e tem consentimento. A decisão de quais métricas entram fica no [`decision-registry`](../../data/registries/decision-registry.md).

## Protocolo de Falha
Item vermelho → o `pr-brand-strategist` **usa o número real**, ainda que menor, e não publica métrica inflada. Número sem lastro verificável ele rebaixa ou remove. ROI de cliente sem o lastro do Offer Book ele restringe. O estrategista **não tem veto**, mas recusa publicar número inflado e **sinaliza** ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto sobre claim sem prova. Dado de cliente sem consentimento ele remove até obter permissão. O ângulo que envolve a métrica é do [`pr-memorable-angle-gate`](pr-memorable-angle-gate.md). Re-entrada: trocar o número inflado pelo real, lastrear na prova e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md) · [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md)
- Agentes: [`pr-brand-strategist`](../../agents/pr-brand-strategist.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`pr-memorable-angle-gate`](pr-memorable-angle-gate.md) · [`pr-placement-gate`](pr-placement-gate.md) · [`pr-brand-kpi-gate`](pr-brand-kpi-gate.md) · [`pr-timing-gate`](pr-timing-gate.md)
