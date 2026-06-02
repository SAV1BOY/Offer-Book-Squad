---
id: data.fixtures.readme
title: "Fixtures de Cenário de Falha (testes negativos dos gates)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [fixtures, tests, gates, veto, negative-tests]
---

# Fixtures de Cenário de Falha

Artefatos **propositalmente ruins** que provam que os gates **bloqueiam** (testes negativos). Rodados por [`scripts/gate-fixtures-test.py`](../../scripts/gate-fixtures-test.py).

> ⚠️ Esta pasta é **excluída das varreduras repo-wide** (`fixtures` está em `SKIP_DIRS` de qa-runner/crosslink/id-resolver/citation/compliance) — senão estes "ruins" quebrariam o hook/CI. O `gate-fixtures-test.py` roda os validadores **explicitamente** contra eles e exige que **falhem**.

## Casos
- [`bad-handoff-incomplete.md`](bad-handoff-incomplete.md) — contrato de handoff faltando 7 dos 9 campos → `handoff-validate.py` deve sair **≠0**.
- [`bad-live-copy-fake-scarcity.md`](bad-live-copy-fake-scarcity.md) — copy viva (`compliance_scan: live`) com escassez falsa + claim sem prova → `compliance-scanner --strict` deve sair **≠0**.

## Controle positivo
O handoff **bom** ([`data/handoffs/example-deepresearch-to-offerbook.md`](../handoffs/example-deepresearch-to-offerbook.md)) deve **passar** (rc=0) — garante que o validador não falha sempre.

`gate-fixtures-test.py` sai 0 só se **todos** os negativos falharem e o positivo passar.
