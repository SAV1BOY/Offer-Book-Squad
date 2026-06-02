---
id: doc.onboarding
title: "Onboarding — Como operar o Offer Book Squad"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [onboarding, how-to, getting-started]
---

# Onboarding — Como operar o squad

Bem-vindo. Em 10 minutos você entende como o squad transforma uma oferta bruta em Offer Book e Blackbook.

## 1. Leia nesta ordem
1. [`README.md`](../README.md) — a missão e o mapa.
2. [`ARCHITECTURE.md`](../ARCHITECTURE.md) — camadas D0–D7, os 25 agentes, convenções.
3. [`config.yaml`](../config.yaml) — o roteamento (task → agentes → frameworks → checklists → templates → registry).
4. [`docs/methodology-hrm-cot-tot-bloom.md`](methodology-hrm-cot-tot-bloom.md) — como os agentes pensam.
5. [`docs/agent-prompt-spec.md`](agent-prompt-spec.md) — a anatomia de um agente.

## 2. Escolha o project type
O [`offerbook-chief`](../agents/offerbook-chief.md) classifica o caso (ver o Mapa de Orquestração dele):
- **offer-book** — só a fundação estratégica.
- **single-promo** — oferta validada → 1 promoção enxuta.
- **full-launch** — máquina completa.
- **offer-ladder · enterprise-deal-book · relaunch · continuity-launch** — variantes.

Regra: **não rode o pipeline inteiro numa oferta não validada.**

## 3. O fluxo (full-launch)
```
D0 escopo/pipeline → D1 mercado/avatar/prova → D2 mecanismo/valor/money-model/preço/unit-econ
→ D3 big-idea/posição → ★ OFFER BOOK (HARD STOP) → D4 copy → D5 funil/tech
→ D6 ops/eventos/afiliados/PR → D7 ★ BLACKBOOK + compliance + memória
```
Cada transição tem um **gate** que precisa ficar verde. O `offerbook-chief` segura a transição.

## 4. Como começar um projeto
1. Preencha [`templates/core/offer-book-master.md`](../templates/core/offer-book-master.md) com o briefing.
2. Rode a fase D1 (inteligência) e registre no `data/registries/`.
3. Avance camada por camada; **não pule o HARD STOP**.
4. No D7, o [`compliance-auditor`](../agents/compliance-auditor.md) audita e pode vetar.
5. O [`knowledge-librarian`](../agents/knowledge-librarian.md) registra o que vira memória.

## 5. Regras de ouro
- **Oferta antes de persuasão.** Sem oferta forte, não escreva.
- **UMA Big Idea.** Múltiplas = reprovação.
- **Escassez verdadeira.** Falsa = veto.
- **Todo claim com prova.**
- **Toda peça move ≥1 alavanca de valor.**

## 6. Qualidade
Rode `python scripts/qa-runner.py` antes de entregar (gate 95+/100) e `python scripts/coverage-report.py` para ver completude. Siga [`docs/style-guide.md`](style-guide.md).
