---
id: doc.contributing
title: "Como Contribuir / Estender o Squad"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
tags: [contributing, conventions, how-to]
---

# Como Contribuir / Estender o Squad

Manter os ~600 arquivos coerentes exige disciplina. Siga este fluxo.

## 1. Antes de criar um arquivo
- Confirme o **tipo** (agent, framework, checklist, gate, template, task, workflow, swipe, voice, phrases, registry, lib, doc, project-phase, script).
- Reserve o **id** no [`config.yaml`](../config.yaml) se for agente/gate/registry/workflow novo.
- Gere o esqueleto: `python scripts/scaffold.py` (frontmatter + seções obrigatórias do tipo).

## 2. Convenções (resumo — completo em style-guide)
- **kebab-case**; `id` derivado do path (ex.: `agents/x.md` → `agent.x`).
- Frontmatter completo; **omita** chaves vazias.
- Cross-links **relativos**; conteúdo em **PT**, chaves/paths em **EN**.
- Pisos de palavras: agente ≥1200 · framework ≥500 · reference ≥400 · task ≥350 · gate/checklist ≥150.
- Citação: princípios em redação **original**; literal **≤25 palavras** atribuída.

## 3. Antes do commit (Definition of Done)
- [ ] `python scripts/qa-runner.py --dir <pasta>` → score ≥ 95.
- [ ] `python scripts/id-resolver.py` → sem colisão de id.
- [ ] `python scripts/crosslink-graph.py` → sem link quebrado (forward-refs OK durante o build).
- [ ] `python scripts/citation-checker.py` (se reference/framework/swipe) → sem citação > 25 palavras.
- [ ] Atualize [`config.yaml`](../config.yaml) se mudou roteamento e [`BUILD-PROGRESS.md`](../BUILD-PROGRESS.md) se fechou uma camada.

## 4. Git
- Commits descritivos por camada (`feat(<camada>): ...`).
- Branch de feature; nunca commitar copy/escassez falsa (o `compliance-auditor` veta).
- **Hooks (uma vez):** `bash scripts/install-hooks.sh` ativa o pre-commit, que regenera as matrizes geradas e roda `qa-runner --strict` + `crosslink-graph` + `id-resolver` + `citation-checker`, **bloqueando** qualquer commit abaixo do padrão GOLD.
- **CI:** [`.github/workflows/qa.yml`](../.github/workflows/qa.yml) espelha o hook no servidor (+ `compliance-scanner --strict`), bloqueando merge abaixo do padrão. `compliance-scanner` só falha em **copy viva** (frontmatter `compliance_scan: live` ou fora dos dirs de sistema); metodologia/templates são informativos.

## 5. Princípios que não se quebram
`offer_before_persuasion` · `one_big_idea` · `truthful_scarcity` · `value_equation_test` · `money_model_spine`. Quando em dúvida, leia [`ARCHITECTURE.md`](../ARCHITECTURE.md) e [`docs/methodology-hrm-cot-tot-bloom.md`](methodology-hrm-cot-tot-bloom.md).
