---
id: doc.changelog
title: "Changelog"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [changelog, versioning]
---

# Changelog

Formato: [Keep a Changelog](https://keepachangelog.com). Versionamento semântico do squad como um todo.

## [1.0.0] — 2026-06-02

### Adicionado — build inicial completo do Offer Book Squad
- **Fundação (Fase 0):** árvore de diretórios na raiz; `config.yaml` (cérebro de roteamento + reserva de ids dos 25 agentes/10 registries/gates/workflows); `ARCHITECTURE.md`; `docs/agent-prompt-spec.md` (esqueleto HRM canônico); `docs/style-guide.md`; `README`, `swipe.config`, `.gitignore`, `BUILD-PROGRESS.md`.
- **Taxonomias (Fase 1):** awareness/sophistication (Schwartz), lead-types (Masterson/Forde), offer-types e guarantee-types (Hormozi).
- **Reference (Fase 2):** corpus citado — 28 livros (Hormozi ×3, Schwartz, Cialdini, Halbert, Sugarman, Ogilvy, Caples, Hopkins, Collier, Bencivenga, Kennedy, Nagle, Ramanujam, Kahneman, Ariely, Voss, Ries/Trout, Dunford, Moore, Walker, Brunson, MEDDIC, Challenger, SPIN) + psychology + industries + case-studies + swipe-breakdowns.
- **Frameworks (Fase 3):** ~82 frameworks (universais, copy, pricing, positioning, launch, por-agente, reference-intellectual incl. HRM).
- **Lib (Fase 4):** components, patterns, utilities, taxonomias.
- **Agentes (Fase 5):** os 25 prompts operacionais HRM + 10 registries.
- **Demais camadas:** checklists, templates, tasks, workflows, swipe, voice, phrases, data, authority, projects, scripts, docs, archive.

### Metodologia
- Raciocínio HRM (arXiv 2506.21734) + CoT/ToT/ReAct/few-shot/self-verification/Bloom.
- Auditoria automatizada por `scripts/qa-runner.py` (gate 95+/100) e `scripts/coverage-report.py`.

### Compliance
- Citações em redação original (literal ≤25 palavras); escassez 100% verdadeira; claims com prova; LGPD/FTC/CDC.

---
*Versões futuras: registre aqui adições/mudanças/remoções por lançamento, com link para o `decision-registry`.*
