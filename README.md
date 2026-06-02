# Offer Book Squad

> O Offer Book Squad mais completo, lucrativo e pronto-para-lançar possível — **25 agentes** que transformam qualquer oferta bruta, em qualquer mercado, em (1) um **Offer Book** (o documento-mestre que codifica mercado, avatar, mecanismo, prova, economia e oferta) e (2) um **Launch Blackbook** completo (a máquina operacional de lançamento).

Sistema de agentes de IA, frameworks, checklists, templates e playbooks de **direct response / offer engineering**, ancorado nas obras de Alex Hormozi (*$100M Offers / Leads / Money Models*), Eugene Schwartz (*Breakthrough Advertising*), Robert Cialdini, Gary Halbert, Joseph Sugarman, David Ogilvy, Russell Brunson, Jeff Walker e Madhavan Ramanujam — operacionalizado com a metodologia **HRM (Hierarchical Reasoning Model)** e técnicas de prompt engineering (CoT, ToT, few-shot, ReAct, self-verification, Bloom).

---

## Princípio central

```
Mercado → Avatar → Mecanismo → Valor → Money Model → Big Idea → Posição
        → [★ OFFER BOOK] → Copy → Funil → Ops/Eventos → Afiliados/PR
        → [★ BLACKBOOK] → Memória
```

**HARD STOP:** nenhuma copy nasce antes do Offer Book passar no *Definition of Done*. ~50–60% do trabalho é pesquisa e estratégia **antes** da primeira palavra.

## Os 11 princípios não-negociáveis

`evidence_before_opinion` · `contradiction_before_conclusion` · `traceability_before_eloquence` · `decision_before_ornament` · `memory_before_repetition` · `clarity_before_volume` · **`offer_before_persuasion`** · **`one_big_idea`** · **`truthful_scarcity`** · **`value_equation_test`** · **`money_model_spine`**

---

## Como navegar

| Diretório | O que contém |
|---|---|
| [`agents/`](agents/) | Os 25 prompts operacionais HRM (o cérebro do squad) |
| [`checklists/`](checklists/) | Quality gates por entregável e por agente (DoD + vetos) |
| [`frameworks/`](frameworks/) | Como o squad pensa (oferta, copy, pricing, posicionamento, lançamento) |
| [`reference/`](reference/) | Base de conhecimento (livros, swipe-breakdowns, indústrias, psicologia) |
| [`templates/`](templates/) | Esqueletos prontos de cada entregável (.md + .csv) |
| [`tasks/`](tasks/) | Tarefas executáveis (runbooks) do intake ao memory-update |
| [`workflows/`](workflows/) | Fluxos ponta-a-ponta (offer-book, full-launch, single-promo…) |
| [`swipe/`](swipe/) · [`swipe-sources/`](swipe-sources/) | Biblioteca de swipe (estrutura, não copy alheia) + proveniência |
| [`voice/`](voice/) · [`phrases/`](phrases/) | Guia de voz e biblioteca de frases de poder |
| [`data/`](data/) | Registries, métricas, benchmarks, pricing-tests, winners |
| [`lib/`](lib/) | Componentes, padrões, utilitários e taxonomias reutilizáveis |
| [`authority/`](authority/) | Banco de resultados, casos, depoimentos, prova |
| [`projects/`](projects/) | 7 tipos de projeto com fases numeradas (00-…) |
| [`scripts/`](scripts/) | Automação Python (scaffold, qa-runner, assemblers, validators) |
| [`docs/`](docs/) | Documentação, metodologia, glossário, compliance-policy |
| [`archive/`](archive/) | Lançamentos passados, controls perdedores (com autópsia) |

**Roteamento:** [`config.yaml`](config.yaml) é a **fonte única de verdade** — mapeia cada task → agentes → frameworks → checklists → templates → registries.
**Arquitetura completa:** [`ARCHITECTURE.md`](ARCHITECTURE.md).
**Status do build:** [`BUILD-PROGRESS.md`](BUILD-PROGRESS.md).

---

## Tipos de projeto (escolha o nível certo)

- **offer-book** — só a fundação estratégica (Tier 0).
- **single-promo** — oferta validada → 1 promoção enxuta (Tier 1).
- **full-launch-blackbook** — máquina de lançamento completa (Tier 2).
- **offer-ladder** · **enterprise-deal-book** · **relaunch** · **continuity-launch** — variantes especializadas.

> Não rode o pipeline inteiro numa oferta não validada — a tierização evita over-engineering.

## Uso ético & legal

O swipe e a base de referência guardam **estrutura, anatomia e princípios** em redação **original**. Nenhuma copy protegida é reproduzida na íntegra (citação literal ≤ 25 palavras, atribuída). Escassez/urgência são **100% verdadeiras** — escassez falsa é veto automático do `compliance-auditor`. Claims exigem prova. Ver [`docs/compliance-policy.md`](docs/compliance-policy.md).

---

*Estruturado por HRM (divisões/agentes hierárquicos) · CoT (protocolos passo a passo) · ToT (project types + geração de Big Ideas) · Bloom (Lembrar→Criar ao longo do pipeline).*
