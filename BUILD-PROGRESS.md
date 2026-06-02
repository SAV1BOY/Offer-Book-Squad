# BUILD-PROGRESS — Offer Book Squad

> Rastreador de build **multi-sessão**. Cada sessão: lê este arquivo → escolhe a próxima fase pendente → constrói o diretório à profundidade total → roda `python scripts/qa-runner.py --phase N` (ou validação inline) → **commit** com a mensagem da camada → **push** `-u origin claude/inspiring-thompson-OKBH1` → atualiza este arquivo → reporta.

**Branch:** `claude/inspiring-thompson-OKBH1` · **Layout:** raiz do repo · **Estratégia:** camada por camada, completa · **Meta total:** ~768 arquivos.

Legenda: ⬜ pendente · 🟨 em progresso · ✅ concluída (qa-runner verde)

| Fase | Camada | Meta arq. | Status | Commit |
|---|---|---|---|---|
| 0  | Foundation & Contracts (raiz + docs + config + árvore) | ~10 | ✅ | `feat(foundation)` |
| 1  | `lib/taxonomies/` | 5 | ✅ | `feat(taxonomies)` |
| 2  | `reference/` (com citações web) | ~90 | 🟨 | — |
| 3  | `frameworks/` | ~95 | ⬜ | — |
| 4  | `lib/` (components, patterns, utilities) | ~33 | ⬜ | — |
| 5  | `agents/` + `data/registries/` | 35 | ⬜ | — |
| 6  | `checklists/` | ~120 | ⬜ | — |
| 7  | `templates/` | ~45 | ⬜ | — |
| 8  | `tasks/` | ~55 | ⬜ | — |
| 9  | `workflows/` | ~20 | ⬜ | — |
| 10 | `swipe/` + `swipe-sources/` | ~46 | ⬜ | — |
| 11 | `voice/` + `phrases/` | ~40 | ⬜ | — |
| 12 | `data/` (sem registries) | ~45 | ⬜ | — |
| 13 | `authority/` | ~22 | ⬜ | — |
| 14 | `projects/` | ~55 | ⬜ | — |
| 15 | `scripts/` | ~14 | ⬜ | — |
| 16 | `docs/` | ~18 | ⬜ | — |
| 17 | `archive/` | ~20 | ⬜ | — |
| 18 | QA de integração (link-check, contagens, reconciliação) | — | ⬜ | — |

## Próxima ação
- **Fase 2** — `reference/` (~90, com citações web): `books/` (offers-and-monetization, copywriting, persuasion-psychology, positioning, launches-and-funnels, b2b-enterprise), `psychology/`, `industries/`, `case-studies/`, `swipe-breakdowns/`. Heavy de pesquisa — confirmar autor/título/ano antes de escrever; literal ≤25 palavras.

## Regras de retomada (para qualquer sessão futura)
1. **Não duplicar:** confira o status aqui antes de criar arquivos.
2. **Profundidade SOTA:** respeite os pisos de palavras (agente ≥1200, framework ≥500, gate ≥150). Sem stubs no estado final.
3. **IDs determinísticos:** `id` deriva do path; toda referência de frontmatter deve resolver (rode `qa-runner`).
4. **`config.yaml` é a verdade:** ao adicionar arquivo, garanta que seu id já está reservado/listado no config.
5. **Citações reais:** `reference/`, `frameworks/reference-intellectual/`, `swipe-*` exigem bloco de fonte; literal ≤25 palavras.
6. **Commit por camada** com a mensagem da tabela; **push** com retry/backoff; manter o **PR draft** atualizado.

## Log de sessões
- **2026-06-02** — Sessão 1: árvore de 124 diretórios criada; **Fase 0 concluída** (`.gitignore`, `README`, `ARCHITECTURE.md`, `config.yaml` (cérebro de roteamento + reserva de ids), `swipe.config`, `BUILD-PROGRESS.md`, `docs/agent-prompt-spec.md`, `docs/style-guide.md`). YAML validado. PR draft #1 aberto. **Fase 1 concluída** (`lib/taxonomies/`: awareness-levels, sophistication-levels, lead-types, offer-types, guarantee-types — com citações Schwartz/Hormozi/Masterson). Próximo: Fase 2.
