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
- [`failure-paths-and-gate-recovery.md`](failure-paths-and-gate-recovery.md) — o que acontece quando um gate fica vermelho ou um agente veta (pontos de re-entrada).
- [`faq.md`](faq.md) — perguntas frequentes.
- [`contributing.md`](contributing.md) — como adicionar/estender arquivos no padrão.
- [`changelog.md`](changelog.md) — histórico de versões.

## Governança HRM & operação
- [`hrm-governance.md`](hrm-governance.md) — as 4 camadas HRM, escalonamento, comando central, go/no-go.
- [`team-coordination.md`](team-coordination.md) — os 10 grupos funcionais (teams/swarms): líder, sequência, gate intermediário.
- [`quality-gate-cascade.md`](quality-gate-cascade.md) — o DAG completo dos quality gates (6 níveis).
- [`improvement-loop-kaizen.md`](improvement-loop-kaizen.md) — o loop de aprendizado (memória → próximo lançamento).
- [`traceability-matrix.md`](traceability-matrix.md) — task → agents → frameworks → checklists → templates → registries → metrics (gerada por script).
- [`handoff-matrix.md`](handoff-matrix.md) — handoffs explícitos: intra-squad (agente→agente, por camada) + cross-squad (os 12 squads MMOS).
- [`audit-report.md`](audit-report.md) — relatório da auditoria interna total (score por camada + verdict).

## Mapa rápido do repositório
`agents/` cérebro · `frameworks/` como pensa · `reference/` conhecimento · `checklists/` gates · `templates/` esqueletos · `tasks/` runbooks · `workflows/` fluxos · `swipe/` estrutura reutilizável · `voice/` + `phrases/` voz · `data/` registries+métricas · `lib/` componentes+taxonomias · `authority/` prova · `projects/` 7 tipos · `scripts/` automação. Roteamento em [`config.yaml`](../config.yaml); progresso em [`BUILD-PROGRESS.md`](../BUILD-PROGRESS.md).

## Qualidade
Rode `python scripts/qa-runner.py` (gate 95+/100), `python scripts/coverage-report.py` (contagem vs meta), `python scripts/readiness-check.py --milestone <marco> [--scorecard <path>]` (go/no-go) e `python scripts/traceability-matrix.py` (regenera a matriz) antes de entregar. **Hooks:** `bash scripts/install-hooks.sh` ativa o pre-commit (regen matrizes + qa-strict + crosslink + id + citation). Operação viva: `handoff-validate.py`, `kpi-snapshot.py`, `backlog-prioritize.py`.
