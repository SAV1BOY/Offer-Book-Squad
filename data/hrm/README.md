---
id: data.hrm.readme
title: "data/hrm/ — Squad Rollups para o HRM Central"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [hrm, rollup, central-command, memory, go-no-go]
---

# data/hrm/ — Squad Rollups

Memória da **interface com o HRM Central** (camada L4). Cada arquivo `rollup-<case>.md` é o **pacote padrão** que o chief do Offer Book Squad emite para o comando central consumir. Spec da interface: [`docs/hrm-central-spec.md`](../../docs/hrm-central-spec.md).

## O que guardar
Um rollup por lançamento, **gerado** por [`scripts/hrm-rollup.py`](../../scripts/hrm-rollup.py) (não editar à mão): score estrutural, scorecard editorial, readiness GO/NO-GO, riscos abertos (backlog), handoffs pendentes e a recomendação ao `hrm_central`.

## Como alimenta os agentes
- [`offerbook-chief`](../../agents/offerbook-chief.md) gera o rollup ao fim do D7 (junto do `memory-update`) e o usa para escalar ao `hrm_central` quando `score < gold` após 2 loops (ver [`hrm-governance`](../../docs/hrm-governance.md) `escalation_rules`).
- O `hrm_central` (futuro) lê os rollups de todos os squads para o **go/no-go sistêmico**.

## Exemplo
[`rollup-example.md`](rollup-example.md) — rollup ilustrativo do caso Mariana (gerado pelo script).
