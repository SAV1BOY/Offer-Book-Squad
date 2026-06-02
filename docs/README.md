---
id: doc.readme
title: "docs/ — Índice da Documentação"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [docs, index, navigation]
---

# Documentação do Offer Book Squad

Índice da pasta `docs/`. Para a visão geral do squad, veja o [`README.md`](../README.md) na raiz; para a arquitetura, [`ARCHITECTURE.md`](../ARCHITECTURE.md).

## Comece por aqui
- [`onboarding.md`](onboarding.md) — como operar o squad em 10 minutos (ordem de leitura, project types, fluxo).
- [`glossary.md`](glossary.md) — todos os termos (WTP, AOV, LTV, money model, big idea, gates…).
- [`exemplar-project-walkthrough.md`](exemplar-project-walkthrough.md) — um caso ponta a ponta (oferta bruta → Offer Book → Blackbook), fase a fase.

## Como o squad pensa e escreve
- [`methodology-hrm-cot-tot-bloom.md`](methodology-hrm-cot-tot-bloom.md) — HRM (H/L) + CoT/ToT/ReAct/few-shot/self-verification/Bloom.
- [`agent-prompt-spec.md`](agent-prompt-spec.md) — a anatomia (12 seções) de cada um dos 25 agentes.
- [`style-guide.md`](style-guide.md) — templates por tipo de arquivo, voz, pisos de palavras, citação.
- [`principles-enforcement-map.md`](principles-enforcement-map.md) — os 11 princípios → gate → agente → framework (quem veta o quê).
- [`../frameworks/README.md`](../frameworks/README.md) — índice e hierarquia dos frameworks (universais → especializações).

## Regras e governança
- [`compliance-policy.md`](compliance-policy.md) — claims, escassez verdadeira, garantias, LGPD/FTC/CDC, veto.
- [`faq.md`](faq.md) — perguntas frequentes.
- [`contributing.md`](contributing.md) — como adicionar/estender arquivos no padrão.
- [`changelog.md`](changelog.md) — histórico de versões.

## Mapa rápido do repositório
`agents/` cérebro · `frameworks/` como pensa · `reference/` conhecimento · `checklists/` gates · `templates/` esqueletos · `tasks/` runbooks · `workflows/` fluxos · `swipe/` estrutura reutilizável · `voice/` + `phrases/` voz · `data/` registries+métricas · `lib/` componentes+taxonomias · `authority/` prova · `projects/` 7 tipos · `scripts/` automação. Roteamento em [`config.yaml`](../config.yaml); progresso em [`BUILD-PROGRESS.md`](../BUILD-PROGRESS.md).

## Qualidade
Rode `python scripts/qa-runner.py` (gate 95+/100) e `python scripts/coverage-report.py` (contagem vs meta) antes de entregar.
