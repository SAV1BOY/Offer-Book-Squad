---
id: task.growth.build-pr-plan
title: "Task — Construir o Plano de PR"
type: task
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
consumes:
  - artifact.offer-book
  - artifact.run-of-show
  - artifact.events-calendar
  - artifact.affiliate-program
  - artifact.big-idea
produces:
  - artifact.pr-plan
  - decision.brand-angle
frameworks: [launch/pr-brand-maximization]
checklists:
  - pr-plan-checklist
registries: [decision-registry]
metrics: [compliance_pass_rate, lessons_learned_frequency]
tags: [growth, pr, marca, autoridade, buzz, angulo, kpis, d6]
---

# Task — Construir o plano de PR: isolar o ângulo memorável e medir o halo de marca

## Objetivo
Transformar o resultado do lançamento em capital de marca duradouro, através de um ângulo memorável e verdadeiro, e medi-lo com KPIs de marca. O estado-pronto: plano de PR com ângulo memorável lastreado em fato verificável + mapa de canais + ativos + KPIs de marca, onde o ângulo estende a Big Idea (não cria tese paralela) e a prova social é consentida — aprovado no pr-plan-checklist.

## Agente dono
[`pr-brand-strategist`](../../agents/pr-brand-strategist.md). O guardião do halo do lançamento; isola a narrativa, planeja o alcance e define a medição. Não vende, não desenha oferta, não escreve copy de venda. Sem poder de veto, mas recusa publicar narrativa sobre conquista inventada.

## Gatilho / Quando
Roda em D6, no flanco pós-venda: ativa quando o lançamento foi executado (ou está na janela final) e há resultado/prova suficiente para virar narrativa. Demais gatilhos: pedido de plano de PR + ângulo memorável + KPIs de marca, ou um marco (número de resultado, caso forte, parceiro de peso) que gera pauta. **Sem um fato lastreado não cria ângulo** — PR sobre conquista inventada destrói a marca e cai no veto de compliance. Sem fato algum digno de pauta → **dizer isso** e recomendar construir o ativo (caso, dado) primeiro.

## Inputs (Consome)
- `artifact.offer-book` + `artifact.big-idea` — a tese, a promessa e o mecanismo. O ângulo de PR **estende** a Big Idea para o público amplo, sem contradizê-la.
- `artifact.run-of-show` + `artifact.events-calendar` — o que aconteceu no lançamento e quando (marcos, eventos, números de público) — a matéria cronológica da narrativa.
- `artifact.affiliate-program` — os parceiros de topo (Dream 100) que também são **multiplicadores de PR** (co-marketing, endossos, plataformas emprestadas).
- **Provas e resultados** (via offer-book e registries) — os fatos lastreados (números de resultado, casos com consentimento, marcos verificáveis). **Nenhum ângulo sem um desses por trás.**

## Procedimento
1. **Inventariar os fatos lastreados.** Listar o que merece pauta: números de resultado, casos com consentimento, endossos com permissão, marcos verificáveis. Sem nenhum, parar e recomendar construir o ativo.
2. **Gerar o ângulo memorável (ToT).** Gerar ≥3 ângulos de fontes de prova diferentes — resultado coletivo, história/herói (com consentimento), tese/contrarian — aplicando [`launch/pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md). Pontuar por veracidade/lastro (critério **eliminatório**), memorabilidade, fit com a Big Idea e apelo de imprensa. Descartar **imediatamente** qualquer ângulo de lastro baixo; entre os lastreados, vence a maior soma, desempate por memorabilidade.
3. **Confirmar o fit com a Big Idea.** O ângulo escolhido estende a tese travada pelo [`big-idea-architect`](../../agents/big-idea-architect.md); ângulo que cria tese paralela → realinhar.
4. **Mapear os canais (ToT).** Gerar ≥3 focos — mídia ganha, autoridade do fundador, prova social interna — e pontuar por alcance novo, custo/esforço, durabilidade do ativo e contribuição para a próxima conversão. Incluir os parceiros do Dream 100 como canal (co-marketing).
5. **Definir os ativos de PR.** Press angle, estudo de caso (com consentimento), conteúdo de autoridade, depoimento de terceiro — cada um lastreado e consentido.
6. **Definir os KPIs de marca.** Menções ganhas, share of voice, crescimento de audiência, lift de prova social na próxima conversão, sentimento — métricas de halo mensuráveis, nunca vaidade pura.
7. **Self-verify (Bloom + red-team).** Cada ângulo tem fato verificável + consentimento? O ângulo contradiz a Big Idea? Os KPIs medem halo de verdade? Um jornalista checaria e o fato se sustenta? Antecipar o veto do [`compliance-auditor`](../../agents/compliance-auditor.md) (caso sem consentimento, número inflado, endosso sem permissão, claim de resultado sem lastro) e corrigir antes.
8. **Registrar e entregar.** Logar o ângulo escolhido (e os podados, com o fato que os lastreava ou a falta dele), os canais e os KPIs no `decision-registry`. O desempenho do PR segue ao [`knowledge-librarian`](../../agents/knowledge-librarian.md). Máximo de 2 ciclos antes de escalar.

## Frameworks
[`launch/pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md) · (herdado) [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md) para parceiros como canal de PR.

## Outputs (Produz)
- `artifact.pr-plan` (template em [`growth/pr-plan-template`](../../templates/growth/pr-plan-template.md)) — ângulo memorável + fato que o lastreia + como estende a Big Idea + canais/cadência + ativos + KPIs de marca.
- `decision.brand-angle` — o ângulo escolhido, os podados e o foco de canal.
- [`decision-registry`](../../data/registries/decision-registry.md) atualizado (`decision_type: positioning`, ângulo, alternativas, rationale, KPIs).

## Definition of Done
- Existe pelo menos um fato lastreado por trás do ângulo (zero PR sobre conquista inventada).
- O ângulo é verificável e consentido; estende a Big Idea travada (não cria tese órfã).
- Mapa de canais e cadência pós-cart definidos; ativos de PR cada um lastreado e consentido.
- KPIs de marca mensuráveis (não vaidade); o pr-plan-checklist verde; ângulo registrado.

## Gates
[`pr-plan-checklist`](../../checklists/pr-plan-checklist.md).

## Métricas
Move KPIs da família **operational** ([`config.yaml`](../../config.yaml) `kpis:`) — os KPIs de **marca** do plano (menções, share of voice, sentimento) são métricas próprias do PR, não da grade dos 20:
- **`compliance_pass_rate`** — exigir fato verificável + consentimento por ângulo (veracidade é critério eliminatório) é o que evita o veto de compliance sobre prova social/endosso de PR no D7.
- **`lessons_learned_frequency`** — os ângulos vencedores e os KPIs de marca como baseline seguem ao `knowledge-librarian`, alimentando as lições registradas por lançamento.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (família operational), com o ângulo e os KPIs em [`decision-registry`](../../data/registries/decision-registry.md).

## Handoff
**Próxima task:** [`compliance-audit`](../qa-memory/compliance-audit.md) — dono [`compliance-auditor`](../../agents/compliance-auditor.md), que recebe o ângulo, os ativos e a prova social para auditoria de consentimento/veracidade (a prova social usada em PR passa pela barreira final). Também entrega ao [`knowledge-librarian`](../../agents/knowledge-librarian.md) o que vira memória (ângulos vencedores, KPIs de marca como baseline). **Garantia:** um plano de PR onde cada ângulo nasce de um fato verificável e consentido, estende a Big Idea travada, e vem com KPIs de marca mensuráveis — nunca buzz sobre conquista inventada.
