---
id: checklist.pr.pr-brand-kpi-gate
title: "Gate — KPI de Marca (o halo é medido, não vaidade)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
frameworks: [launch/pr-brand-maximization, launch/affiliate-army]
registries: [decision-registry]
tags: [gate, pr, kpi, marca, halo, mensuravel, d6]
---

# Gate — KPI de Marca

## Propósito
Este gate prova que **o halo de marca tem KPIs mensuráveis, não métricas de vaidade**. Ele existe porque marca sem KPI vira vaidade: curtidas sem ligação com autoridade ou conversão não provam que a marca subiu. O `pr-brand-strategist` define como saberemos se o halo cresceu — menções ganhas, share of voice, crescimento de audiência, lift de prova social na conversão do próximo lançamento, sentimento, qualidade de lead inbound. O sucesso do PR não é venda direta, é **autoridade acumulada** que aumenta a próxima conversão. Vale o princípio `decision_before_ornament`: cada KPI serve a uma decisão futura, não ao ego. No modo de falha do agente, o KPI de vaidade (curtidas sem ligação com marca/conversão) é trocado por uma métrica de halo mensurável. Esses KPIs viram baseline de memória no `knowledge-librarian` — um ângulo que funcionou vira padrão reutilizável. Este gate julga **só a mensurabilidade do halo** — o ângulo é do `pr-memorable-angle-gate`, os números do ângulo são do `pr-metric-focus-gate`, e os canais são do `pr-placement-gate`. KPI que não liga a autoridade ou conversão não passa.

## Dono & Escopo
- **owner_agent:** `pr-brand-strategist` (define os KPIs de marca mensuráveis).
- **Artefato inspecionado:** a parte de KPIs do `pr-plan`, cruzada com os objetivos de marca e os marcos do lançamento. Os KPIs e a decisão de medição vão ao [`decision-registry`](../../data/registries/decision-registry.md); o desempenho vira baseline no [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) via o knowledge-librarian.

## Condição de Passagem
Cada KPI de marca é mensurável e liga a autoridade ou à próxima conversão, sem métrica de vaidade pura.

## Itens
1. **KPIs definidos.** Verificar: o plano lista KPIs de marca (menções, share of voice, audiência, sentimento, lead inbound).
2. **Mensurável.** Verificar: cada KPI tem como ser medido, com fonte e cadência claras.
3. **Liga a halo/conversão.** Verificar: cada KPI conecta a autoridade ou ao lift da próxima conversão, não só a curtidas.
4. **Sem vaidade pura.** Verificar: nenhuma métrica de vaidade sem ligação com marca/conversão.
5. **Baseline para memória.** Verificar: os KPIs ficam como baseline reutilizável (knowledge-librarian).
6. **Atrelado ao ângulo.** Verificar: os KPIs medem o efeito do ângulo escolhido, não métricas soltas.

## Evidência Exigida
Para marcar ✅: linkar os KPIs no `pr-plan` com fonte e cadência de medição, mais a ligação explícita de cada um a halo/autoridade ou ao lift de conversão. A decisão de quais KPIs entram fica no [`decision-registry`](../../data/registries/decision-registry.md); o baseline segue ao [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md).

## Protocolo de Falha
Item vermelho → o `pr-brand-strategist` **troca** o KPI de vaidade por uma métrica de halo mensurável antes de declarar o plano pronto. KPI sem fonte clara ele define a fonte e a cadência. O estrategista **não tem veto**, mas recusa declarar o plano pronto com métricas que não provam o halo. KPIs soltos, sem ligação com o ângulo, ele realinha ao ângulo escolhido no [`pr-memorable-angle-gate`](pr-memorable-angle-gate.md). O desempenho de marca segue ao [`knowledge-librarian`](../../agents/knowledge-librarian.md) como baseline. Re-entrada: substituir vaidade por métrica de halo, definir a fonte e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md) · [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md)
- Agentes: [`pr-brand-strategist`](../../agents/pr-brand-strategist.md) · [`knowledge-librarian`](../../agents/knowledge-librarian.md)
- Gates irmãos: [`pr-memorable-angle-gate`](pr-memorable-angle-gate.md) · [`pr-metric-focus-gate`](pr-metric-focus-gate.md) · [`pr-placement-gate`](pr-placement-gate.md) · [`pr-timing-gate`](pr-timing-gate.md)
