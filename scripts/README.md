---
id: scripts.readme
title: "Scripts — Automação do Offer Book Squad"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [scripts, automation, runbook, ci, validation, doc]
---

# Scripts — Automação do Offer Book Squad

Automação **runnable** (stdlib + `pyyaml`) que valida, gera e consolida os artefatos do squad. Todo script tem header-docstring no formato de [`qa-runner.py`](qa-runner.py) (`PART OF / OWNER_AGENT / CONSUMES / PRODUCES / USAGE / DEPENDS / EXIT`), aceita `--check` (dry-run **read-only**) e segue a convenção de exit-codes: **0** ok, **1** falha de validação, **2** erro de uso. Conteúdo em português; código e identificadores em inglês. Ver a §4k do [`docs/style-guide.md`](../docs/style-guide.md) e a §5 do [`ARCHITECTURE.md`](../ARCHITECTURE.md).

## Pré-requisitos

- **Python 3.9+** e **pyyaml** (`pip install pyyaml`). Nenhuma outra dependência externa.
- Rode sempre a partir da raiz do repo: `python scripts/<nome>.py [args]`. Cada script descobre a raiz pelo próprio path, então funciona de qualquer diretório.
- Os relatórios `.json` (gerados na raiz) estão no [`.gitignore`](../.gitignore). Em modo `--check` **nada é escrito**.

## Convenção comum

| Flag | Efeito |
|---|---|
| `--check` | Dry-run **read-only**: reporta o que faria; não escreve arquivo nem `.json`. |
| `--dir <subdir>` | Restringe a varredura a um subdiretório (validadores). |
| `--quiet` | Só o resumo (suprime o detalhe linha-a-linha). |
| `--force` | Sobrescreve o arquivo de saída se já existir (geradores). |

## Validadores (leem o repo, reportam saúde)

- **`qa-runner.py`** — auditor de qualidade: frontmatter, tipos, ids, pisos de palavras e links. `python scripts/qa-runner.py [--dir D] [--strict] [--phase N]`. Exit 1 se score < gate (95).
- **`id-resolver.py`** — constrói o mapa `id↔path` de todos os `.md` e exige **bijeção** (zero colisão, zero inconsistência). `python scripts/id-resolver.py [--dir D] [--check]`.
- **`coverage-report.py`** — contagem viva de arquivos por diretório vs meta do plano. `python scripts/coverage-report.py [--phase N]`. Sempre exit 0 (informativo).
- **`citation-checker.py`** — varre `reference/`, `frameworks/reference-intellectual/`, `swipe*/`; sinaliza citação literal **> 25 palavras** e bloco de fonte ausente. `python scripts/citation-checker.py [--dir D] [--max-words N] [--check]`.
- **`crosslink-graph.py`** — grafo dos cross-links relativos; reporta **links quebrados** (exit 1) e **arquivos órfãos** (informativo). `python scripts/crosslink-graph.py [--dir D] [--check]`.
- **`compliance-scanner.py`** — heurística de **claims sem prova** e **escassez/urgência suspeita** por arquivo. `python scripts/compliance-scanner.py [--dir D] [--strict] [--check]`. Informativo por padrão; `--strict` transforma flags em falha.
- **`build-manifest.py`** — manifesto do build: contagem por diretório, por tipo e lista de ids (detecta duplicados). `python scripts/build-manifest.py [--dir D] [--check]`. Sempre exit 0.

## Geradores (criam/atualizam artefatos)

- **`scaffold.py`** — gera frontmatter + esqueleto de seções `##` conforme o `type` (regras do style-guide §4); cria um `.md` novo conformante. `python scripts/scaffold.py --type T --path P/arquivo.md [--title "..."] [--check] [--force]`.
- **`swipe-indexer.py`** — lê [`swipe.config`](../swipe.config), indexa `swipe/` (+ `reference/swipe-breakdowns/`) e regenera a tabela sob `## Registros` em [`data/registries/swipe-registry.md`](../data/registries/swipe-registry.md). `python scripts/swipe-indexer.py [--check]` (`--check` só reporta).
- **`sequence-matrix-generator.py`** — gera a **matriz de e-mail/SMS** (CSV no schema de [`sequence-matrix-template.csv`](../templates/copy/sequence-matrix-template.csv)) a partir de um money model simples. `python scripts/sequence-matrix-generator.py [--in money-model.yaml] [--offer "..."] [--cart-days N] [--out f.csv] [--check]`.
- **`link-utm-builder.py`** — gera **vanity URLs + UTM** por CTA a partir de um input. `python scripts/link-utm-builder.py --base https://dominio --campaign slug [--in ctas.yaml] [--cta "Label:source:content"] [--out f.csv] [--check]`.
- **`blackbook-assembler.py`** — consolida os artefatos do Blackbook (esqueleto + gates + entregáveis por domínio) num **índice/sumário** markdown. `python scripts/blackbook-assembler.py [--out data/blackbook-index.md] [--check]`.

## Ordem sugerida (sanity check do build)

```bash
python scripts/id-resolver.py            # bijeção id<->path
python scripts/qa-runner.py              # qualidade (gate 95)
python scripts/crosslink-graph.py        # links quebrados + órfãos
python scripts/citation-checker.py       # anti-plágio (<=25 palavras)
python scripts/coverage-report.py        # contagem vs meta
python scripts/build-manifest.py         # manifesto + ids
```

Na **Fase 18** (QA de integração), rode `qa-runner.py --strict` e `crosslink-graph.py` no repo inteiro para fechar forward-refs. Os geradores rodam sob demanda do agente dono (ver `OWNER_AGENT` no header de cada script).
