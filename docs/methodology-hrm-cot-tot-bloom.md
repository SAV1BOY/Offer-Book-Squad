---
id: doc.methodology-hrm-cot-tot-bloom
title: "Metodologia de Raciocínio — HRM · CoT · ToT · ReAct · Bloom"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
frameworks: [reference-intellectual/hrm-hierarchical-reasoning]
sources:
  - "Sapient Inc., Hierarchical Reasoning Model, arXiv 2506.21734 (2025)"
tags: [hrm, cot, tot, react, few-shot, bloom, methodology]
---

# Metodologia de Raciocínio do Squad

Os 25 agentes não "respondem" — eles **raciocinam em camadas**. Este documento explica as técnicas e onde cada uma vive. O esqueleto operacional está em [`agent-prompt-spec.md`](agent-prompt-spec.md); o framework de referência em [`hrm-hierarchical-reasoning`](../frameworks/reference-intellectual/hrm-hierarchical-reasoning.md).

## Visão geral

| Técnica | Papel | Onde vive (no agente) |
|---|---|---|
| **HRM** | dois loops: planejar (lento) + executar (rápido) | §3.1, §3.2, §3.4 |
| **CoT** | pensar passo a passo | §3.2 |
| **ToT** | gerar/pontuar/podar alternativas | §3.3 |
| **ReAct** | agir → observar → refinar + write-back | §3.2 + §8 |
| **Few-shot** | exemplos resolvidos no contexto | §5 |
| **Self-verification** | autocrítica antes de emitir | §6 |
| **Bloom** | subir de Lembrar até Criar/Avaliar | §6 |

## HRM (Hierarchical Reasoning Model)

Base: Sapient Inc., *Hierarchical Reasoning Model* (arXiv 2506.21734, 2025) — um **H-Module** (alto nível, lento, planejador abstrato) dirige um **L-Module** (baixo nível, rápido, executor). No squad: o H enquadra o problema e decompõe; o L executa cada sub-passo; o H reavalia até **convergir** nos gates. É por isso que cada agente sabe *quando parar* — a parada é um DoD mensurável, não "achismo".

## CoT (Chain-of-Thought)

Dentro do L-Module, o agente raciocina explicitamente: "primeiro… então… portanto…". Evita pular para a conclusão. Combinado com `evidence_before_opinion`.

## ToT (Tree-of-Thoughts)

Onde há ramificação real, o agente **gera ≥3 candidatos**, pontua contra uma rubrica (Value Equation, sofisticação, prova) e **poda**. Centrais: `big-idea-architect` (gera 3-5 Big Ideas → trava UMA), `money-model-designer` (≥3 configurações de escada), `pricing-wtp-strategist` (≥3 métodos de WTP).

## ReAct (Reason + Act)

O agente alterna **Pensamento → Ação** (aplica framework / lê registry) **→ Observação** (o que retornou) → próximo Pensamento. O *write-back* (§8) grava decisões e artefatos nos registries — memória que outros agentes leem (`memory_before_repetition`).

## Few-shot

Cada agente carrega ≥2 mini-exemplos resolvidos (input→raciocínio→output) em estágios de sofisticação diferentes. Ancoram o padrão de qualidade sem depender de improviso.

## Self-verification

Antes de emitir, o agente roda uma autocrítica (§6) e um *red-team* ("o que o compliance-auditor / voice-guardian rejeitaria?"). Falhou → volta ao L-Module. É o que sustenta o gate 95+/100.

## Bloom (taxonomia)

O agente sobe a escada: **Lembrar → Entender → Aplicar → Analisar → Avaliar → Criar**. Não basta aplicar um framework (Aplicar); o agente precisa **Avaliar** o próprio output e, quando o caso pede, **Criar** uma solução nova (ex.: um mecanismo único nomeado).

## Como se combina no pipeline

O [`offerbook-chief`](../agents/offerbook-chief.md) orquestra (HRM no nível do pipeline). Cada agente roda seu próprio loop HRM. O `config.yaml` é a memória de roteamento; os registries são a memória de fatos. O resultado é um sistema que **diagnostica antes de afirmar, prova antes de prometer e decide antes de ornamentar** — espelhando como Agora/Empiricus e Hormozi operam: pesquisa e oferta antes da copy.
