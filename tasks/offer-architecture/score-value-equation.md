---
id: task.offer-architecture.score-value-equation
title: "Score Value Equation — Mapear Cada Componente a uma Alavanca e Vetar os Órfãos"
type: task
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
consumes:
  - artifact.mechanism-sheet
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - artifact.offer-registry-state
produces:
  - artifact.value-equation-scorecard
  - decision.lever-assignment
frameworks:
  - value-equation
  - value-equation-engineer/dream-outcome-amplification
  - value-equation-engineer/time-delay-compression
  - value-equation-engineer/effort-sacrifice-reduction
checklists:
  - value/value-no-orphan-lever-gate
registries: [offer-registry]
metrics: [value_equation_score, money_model_completeness]
tags: [offer-architecture, value-equation, alavancas, sonho, probabilidade, tempo, esforco, veto, d2]
---

# Score Value Equation — mapear cada componente a uma alavanca e vetar os órfãos

## Objetivo
Maximizar (Sonho × Probabilidade) / (Tempo × Esforço) provando, para cada componente da oferta, qual alavanca ele move, em que direção e com qual evidência — e cortar todo componente órfão, no estado em que nenhuma das quatro alavancas fica abandonada e o produto da equação é defensável.

## Agente dono
[`value-equation-engineer`](../../agents/value-equation-engineer.md). O engenheiro do valor percebido. Não escreve copy, não fixa preço. **Tem poder de veto** sobre componentes e claims (HARD STOP do componente).

## Gatilho / Quando
Roda em D2, quando: (a) o mecanismo único está nomeado e **provado**; (b) há componentes de oferta propostos para pontuar; (c) alguém pede auditoria de valor de uma peça, bônus ou garantia. **Pré-condição:** o [`mechanism-sheet`](define-mechanism.md) está provado (não provisório) — o valor se ancora no mecanismo. O avatar/VOC declaram a emoção dominante e o **sonho real** (o que o avatar quer, não o que o produto faz). Se a lista de componentes vier sem o resultado-alvo de cada um, devolvo pedindo o "para quê". Se o mecanismo ainda é provisório, marco o scorecard como **condicional** e bloqueio só os componentes que dependem do elo não-provado.

## Inputs (Consome)
- **`artifact.mechanism-sheet`** (do mechanism-architect) — as alavancas que o mecanismo já move, para não duplicar e para amplificar.
- **`artifact.avatar-icp`** + **`artifact.voc-verbatim-bank`** — o Sonho na linguagem do avatar, os medos (que derrubam a Probabilidade percebida), os sacrifícios temidos (tempo/esforço).
- **`artifact.offer-registry-state`** — a lista corrente de componentes (núcleo, bônus, garantia, entregáveis) a auditar.
- **Registry escrito:** [`offer-registry`](../../data/registries/offer-registry.md).

## Procedimento
1. **Mapeie e amplifique o Sonho.** Aplique [`dream-outcome-amplification`](../../frameworks/value-equation-engineer/dream-outcome-amplification.md): o sonho real do avatar, amplificado **e crível**. Sonho inflado sem Probabilidade que o acompanhe destrói valor.
2. **Suba a Probabilidade percebida.** Prova, garantia e mecanismo sustentam o "vou conseguir". Use [`value-equation`](../../frameworks/value-equation.md) como fórmula-mestra.
3. **Comprima o Tempo.** Aplique [`time-delay-compression`](../../frameworks/value-equation-engineer/time-delay-compression.md): traga o primeiro resultado para mais cedo (quick-win).
4. **Reduza o Esforço/sacrifício.** Aplique [`effort-sacrifice-reduction`](../../frameworks/value-equation-engineer/effort-sacrifice-reduction.md): feito-por-você, atalhos, remoção do trabalho temido (confirmado no VOC).
5. **Audite cada componente contra as 4 alavancas.** Para cada item, declare alavanca-alvo e direção (↑/↓). Componente cujo delta líquido é zero ou negativo (aumenta Esforço/Tempo sem subir Sonho/Probabilidade) é **órfão** → `VETO` (HARD STOP do componente) até reposicionar ou cortar.
6. **Resolva ambiguidade (Tree-of-Thoughts).** Quando um componente poderia servir a mais de uma alavanca, gere ≥3 enquadramentos e pontue por *delta na alavanca* (×3), *custo de entrega* (×2, penaliza), *risco de credibilidade* (×3, penaliza inflar Sonho derrubando Probabilidade), *sinergia* (×1). Escolha o de maior delta no produto da equação.
7. **Vete o claim inacreditável.** Promessa que infla o Sonho mas gera descrença no avatar cético (evidência no VOC) faz o produto da equação cair → `VETO do claim`, com recomendação de versão crível.
8. **Reavalie o scorecard inteiro.** Alguma das 4 alavancas ficou abandonada (zero componentes)? Sobrou órfão? Itere. *"O que o `unit-economics-stack-analyst` reclamaria?"* (alavanca cara demais para o delta). Corrija.
9. **Registre e passe o gate.** Logue o scorecard no `offer-registry` (`component_id`, alavanca-alvo, direção, delta, veredito, motivo, `prova_refs`), cada veto e cada override do chief. Marque `value_equation_pass: true|false`. Passe o `value-no-orphan-lever-gate`.

## Frameworks
- [`value-equation`](../../frameworks/value-equation.md) — fórmula-mestra, Probabilidade.
- [`dream-outcome-amplification`](../../frameworks/value-equation-engineer/dream-outcome-amplification.md) — alavanca Sonho.
- [`time-delay-compression`](../../frameworks/value-equation-engineer/time-delay-compression.md) — alavanca Tempo.
- [`effort-sacrifice-reduction`](../../frameworks/value-equation-engineer/effort-sacrifice-reduction.md) — alavanca Esforço. (Probabilidade detalhada em [`likelihood-of-achievement`](../../frameworks/value-equation-engineer/likelihood-of-achievement.md).)

## Outputs (Produz)
- **`artifact.value-equation-scorecard`** ([`template`](../../templates/strategy/value-equation-template.md)) — leitura das 4 alavancas, componentes mapeados (id/alavanca/direção/delta/veredito), vetos, `value_equation_pass`.
- **`decision.lever-assignment`** — a alavanca dominante e a atribuição por componente.
- **Registry escrito:** [`offer-registry`](../../data/registries/offer-registry.md).

## Definition of Done
Cada componente mapeia ≥1 alavanca, com direção declarada; nenhuma das 4 alavancas está abandonada; nenhum componente órfão sobrevive; o produto da equação é defensável sem inflar Sonho artificialmente; o `value-no-orphan-lever-gate` está verde; vetos e overrides estão registrados. Máximo de 3 ciclos antes de escalar.

## Gates
- [`value/value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md)

## Métricas
Move KPIs da família **offer_quality** ([`config.yaml`](../../config.yaml) `kpis:`), por ser quem audita a força do valor percebido da oferta:
- **`value_equation_score`** — esta task **é** a fonte direta do KPI (nota 0-100 da Value Equation): pontua cada alavanca e veta os órfãos, então a nota só sobe quando o scorecard fecha sem buraco.
- **`money_model_completeness`** — a atribuição de cada componente à alavanca certa abastece a alocação por degrau na espinha; valor mal mapeado vira escada incompleta a jusante.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (família offer_quality), com o scorecard registrado em [`offer-registry`](../../data/registries/offer-registry.md).

## Handoff
**Próxima task:** [`set-pricing-wtp`](set-pricing-wtp.md) — dono [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md), que recebe o valor percebido por alavanca (base do preço por valor). Adiante, o [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) recebe o custo×delta de cada componente; o [`money-model-designer`](../../agents/money-model-designer.md), o scorecard para alocar cada componente ao degrau certo; o [`big-idea-architect`](../../agents/big-idea-architect.md), a alavanca dominante. **Garantia:** todo componente que chega ao downstream move pelo menos uma alavanca, declarada e com direção — zero órfãos.
