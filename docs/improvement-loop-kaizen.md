---
id: doc.improvement-loop-kaizen
title: "Loop de Melhoria — RalphLoop / Kaizen"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [kaizen, ralphloop, learning, memory, backlog, continuous-improvement]
---

# Loop de Melhoria — RalphLoop / Kaizen

O squad **aprende a cada lançamento**. A memória não é arquivo morto: ela **influencia a próxima execução**. Regra viva em [`config.yaml`](../config.yaml) `improvement_loop`. Princípio: `memory_before_repetition`.

## O ciclo (cadence: per_launch)
```
[1] RUN            ── o lançamento executa (D0→D7)
        │
[2] MEMORY-UPDATE  ── tasks/qa-memory/memory-update.md (D7, knowledge-librarian)
        │            grava: lessons-learned-registry, control-registry, winners, swipe-registry
        │            calcula: data/scorecards/ (score 0-100 do lançamento)
        │
[3] BACKLOG        ── cada lição vira item em data/backlog/ (origem, ROI, prioridade, dono)
        │
[4] NEXT INTAKE    ── tasks/planning/intake-and-scope.md consulta lessons-learned + backlog
        │            ANTES de desenhar o próximo offer book (não recomeça do zero)
        └──────────► volta a [1] mais forte
```

## Quem faz o quê
- **[knowledge-librarian](../agents/knowledge-librarian.md)** — cura a memória: roda o memory-update, mantém os registries, transforma lição → item de [`data/backlog`](../data/backlog/README.md).
- **[offerbook-chief](../agents/offerbook-chief.md)** — prioriza o backlog por ROI e decide o que entra no próximo ciclo; aciona o `hrm_central` para melhorias que cruzam squads.

## De lição a mudança (como um item evolui)
1. **Lição** (ex.: "garantia condicional converteu +18% vs incondicional neste nicho") → [`lessons-learned-registry`](../data/registries/lessons-learned-registry.md).
2. **Item de backlog** com origem, ROI estimado, prioridade, dono → [`data/backlog`](../data/backlog/README.md).
3. **Aplicação** no próximo ciclo: vira ajuste em um agente / framework / template / `config.yaml` (ex.: atualizar [`guarantee-design`](../frameworks/guarantee-design.md) ou o swipe).
4. **Verificação:** o próximo `scorecard` mostra se a mudança subiu o score (fecha o loop).

## Gatilhos de melhoria (quando abrir item de backlog)
- `score < gold` em qualquer marco (rework + lição).
- Veto recorrente do mesmo tipo (padrão de falha → melhorar o framework/checklist).
- Control vencedor novo → vira swipe + atualiza `winners`.
- Handoff cross-squad rejeitado → melhorar o contrato/qualidade do input.

## Cadência
- **Por lançamento:** passos [2]–[4] são obrigatórios no D7 (`mandatory_registry_update`, `kaizen_loop: true`).
- **Periódica (review):** knowledge-librarian + chief revisam o backlog acumulado e promovem os itens de maior ROI (ver [próximos upgrades no audit-report](audit-report.md)).

## Ferramentas vivas do loop
- **Backlog vivo:** [`data/backlog/improvement-backlog.md`](../data/backlog/improvement-backlog.md) — ROI numérico (`impact × confidence ÷ effort`), ranqueado por `scripts/backlog-prioritize.py`.
- **Scorecard do lançamento:** [`data/scorecards/example-launch-scorecard.md`](../data/scorecards/example-launch-scorecard.md) — go/no-go via `scripts/readiness-check.py --scorecard`.
- **KPI snapshot:** [`data/metrics/kpi-snapshot-example.md`](../data/metrics/kpi-snapshot-example.md) — gerado por `scripts/kpi-snapshot.py`; KPI < meta vira item de backlog.
- **Pre-commit hook:** `scripts/install-hooks.sh` mantém matrizes e qualidade em sync a cada commit.

> Sem este loop, cada lançamento recomeça do zero — o anti-pattern mais caro. Com ele, a vantagem é **composta**: cada lançamento começa do melhor estado do anterior.
