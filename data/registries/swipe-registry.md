---
id: data.registry.swipe-registry
title: "Registro de Swipe (Índice)"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [knowledge-librarian, ad-creative-factory]
read_agents: [vsl-webinar-scriptwriter, email-sms-sequence-writer, direct-mail-insert-writer, ad-creative-factory, big-idea-architect, positioning-lead-strategist]
tags: [swipe, index, pattern, reuse, generated, registry]
---

# Registro de Swipe (Índice)

## Propósito

Este é o **índice do swipe** — o catálogo navegável de todos os padrões reutilizáveis em [`swipe/`](../../swipe/) e dos teardowns em [`reference/swipe-breakdowns/`](../../reference/swipe-breakdowns/). Cada entrada aponta para um arquivo de swipe (estrutura/anatomia em **redação original**, nunca copy literal) e marca o **princípio** que o faz funcionar e o **estágio** onde encaixa.

Diferente dos outros registros, este é **gerado por script**: [`scripts/swipe-indexer.py`](../../scripts/swipe-indexer.py) varre `swipe/` e `reference/swipe-breakdowns/`, lê o frontmatter de cada arquivo e regenera a tabela abaixo. **Não editar a tabela à mão** — rode o indexer (`python scripts/swipe-indexer.py`; `--check` = dry-run). O registro serve `memory_before_repetition`: reusar um padrão vencedor antes de inventar.

## Schema

Cada linha é derivada do frontmatter do arquivo de swipe (`id`, `title`, `type`, `tags`, `frameworks`, `sources`). O estágio usa [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md).

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `swipe_id` | string (id) | id derivado do path, ex.: `swipe.vsl.origin-story-open` | Sim |
| `title` | string | título humano do swipe | Sim |
| `swipe_type` | enum | `swipe` \| `swipe-source` (de [`style-guide`](../../docs/style-guide.md) §4g) | Sim |
| `category` | enum | `vsl` \| `email` \| `ad` \| `sales-page` \| `webinar` \| `mailer` \| `hook` \| `headline` | Sim |
| `pattern_name` | string | o padrão/anatomia que captura | Sim |
| `principle` | string | princípio nomeado que dispara (cita framework/reference) | Sim |
| `sophistication_fit` | string | estágio(s) 1-5 onde encaixa, ex.: `3-4` | Não |
| `source_ref` | ref/URL | proveniência (bloco de citação no arquivo) | Não |
| `path` | path | caminho relativo do arquivo de swipe | Sim |
| `reuse_count` | int | quantas vezes foi reusado (KPI `swipe_reuse_rate`) | Não |
| `status` | enum | `indexed` \| `stale` \| `archived` | Sim |
| `owner_agent` | agent-id | id real de [`config.yaml`](../../config.yaml) | Sim |
| `updated` | ISO date | `YYYY-MM-DD` (carimbo do indexer) | Sim |

## Quem escreve / Quem lê

**Escrevem**:
- `knowledge-librarian` — dono do registro; roda [`scripts/swipe-indexer.py`](../../scripts/swipe-indexer.py) na tarefa `memory-update` para regenerar o índice a partir dos arquivos de swipe.
- `ad-creative-factory` — quando cria um padrão novo de ad reutilizável, adiciona o arquivo em `swipe/` (o indexer o cataloga); registra reuso via `reuse_count`.

**Leem**: todos os escritores de copy (`vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `direct-mail-insert-writer`, `ad-creative-factory`) buscam um padrão antes de escrever do zero; `big-idea-architect` e `positioning-lead-strategist` consultam ganchos e ângulos comprovados.

## Registros

| swipe_id | title | swipe_type | category | pattern_name | principle | sophistication_fit | source_ref | path | reuse_count | status | owner_agent | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `swipe.vsl.exemplo-origin-open` _(EXEMPLO ILUSTRATIVO — apagar; gerado pelo indexer)_ | Abertura por História de Origem (amostra) | swipe | vsl | lead de história + reviravolta | slippery-slide (atrito decrescente) | 1-2 | `reference/swipe-breakdowns/exemplo.md` | `swipe/vsl/exemplo-origin-open.md` | 0 | indexed | knowledge-librarian | 2026-06-02 |

<!-- Tabela GERADA por scripts/swipe-indexer.py — não editar à mão. A linha acima é um exemplo ilustrativo; o indexer a substitui pelos arquivos reais de swipe/. -->
