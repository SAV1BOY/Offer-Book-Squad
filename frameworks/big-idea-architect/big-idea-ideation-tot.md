---
id: framework.big-idea-architect.big-idea-ideation-tot
title: "Big Idea Ideation (Tree-of-Thoughts) — Gerar 3–5 Ideias Candidatas"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [big-idea-architect.big-idea-scoring, big-idea-architect.promise-hook-villain, power-of-one, big-idea-generator, awareness-x-sophistication]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
  - "David Ogilvy, *Ogilvy on Advertising* (1983)."
  - "Sapient Inc., *Hierarchical Reasoning Model* (HRM), arXiv:2506.21734 (2025)."
tags: [big-idea, ideation, tree-of-thoughts, divergence, hook]
---

# Big Idea Ideation (Tree-of-Thoughts) — Gerar 3–5 Candidatas

## TL;DR
Antes de travar UMA Big Idea (Power of One), você precisa **divergir** com método. Tree-of-Thoughts (ToT) gera 3-5 ideias candidatas explorando ramos distintos — por dimensão (mecanismo, inimigo, promessa, identidade, descoberta) — em vez de fixar na primeira que aparece. Cada ramo vira uma ideia testável, que depois passa pelo [`big-idea-scoring`](big-idea-scoring.md). Vence quando você quer evitar a "primeira ideia óbvia" e dar ao scoring um leque real para escolher. A regra: **divirja com ToT, convirja com scoring, trave UMA**.

## Quando usar / Quando não
**Use** na fase D3, depois do Offer Book (mecanismo, prova, valor prontos) e antes de travar a Big Idea.
**Use** quando a primeira ideia parece "boa demais cedo demais" — ToT força alternativas e revela ângulos melhores.
**Use** quando o mercado é sofisticado (estágio 3-5): aí a ideia óbvia já foi usada e você precisa de ramos não-óbvios.
**Não use** para **entregar** várias ideias — o `big-idea-architect` entrega **UMA** (múltiplas = reprovação, ARCHITECTURE §4). ToT é divergência interna; o output final converge.
**Não use** sem os inputs do Offer Book: ideia sem mecanismo e prova vira slogan vazio.

## Inputs
- O **mecanismo único** nomeado e provado (do `mechanism-architect`).
- A **dor**, o **resultado dos sonhos** e o **inimigo percebido** em verbatim ([`../avatar-voc-investigator/voc-mining.md`](../avatar-voc-investigator/voc-mining.md)).
- A **célula** de consciência × sofisticação ([`../awareness-x-sophistication.md`](../awareness-x-sophistication.md)).
- A **oferta** e a **prova** mais forte disponíveis.
- O **registro de Big Ideas passadas** (`big-idea-registry`) para não repetir ângulos já gastos.

## Procedimento
1. **Defina a raiz** — escreva o objetivo: "UMA tese que pare o público da célula X e enquadre a oferta". Tudo cresce daqui.
2. **Abra 5 ramos por dimensão** (um ângulo por ramo):
   - **Ramo Mecanismo** — a ideia gira em torno do "como" único (ex.: "Shadowing Técnico").
   - **Ramo Inimigo** — a ideia nomeia o vilão comum (ex.: "a gramática matou seu inglês falado").
   - **Ramo Promessa** — a ideia é o resultado ousado e específico (ex.: "fluente em entrevista em 60 dias").
   - **Ramo Identidade** — a ideia é quem o avatar se torna (ex.: "o dev global").
   - **Ramo Descoberta/Segredo** — a ideia é a revelação contra-intuitiva (ex.: "fluência não vem de estudar mais").
3. **Expanda cada ramo em 2-3 brotos** — variações da mesma dimensão. Não julgue ainda; gere quantidade.
4. **Pode os brotos fracos** — em cada ramo, mantenha o broto mais forte (mais novo, mais crível, melhor casado com a célula). Critério de poda rápido: tem mecanismo? é específico? casa com a consciência?
5. **Selecione 3-5 candidatas finais** — uma ou duas por ramo sobrevivente, garantindo **diversidade de dimensão** (não 3 variações de promessa).
6. **Formate cada candidata** no esqueleto [`promise-hook-villain`](promise-hook-villain.md): promessa + gancho + vilão, em uma frase.
7. **Cheque o lastro** — cada candidata precisa de mecanismo e prova reais por trás. Candidata sem lastro sai.
8. **Encaminhe ao scoring** — passe as 3-5 ao [`big-idea-scoring`](big-idea-scoring.md), que converge para UMA.

## Outputs
- **3-5 Big Ideas candidatas**, cada uma de uma dimensão distinta, em formato promessa-gancho-vilão.
- A **árvore de ramos** documentada (para auditoria e reúso no `big-idea-registry`).
- Cada candidata com seu **mecanismo e prova** anexados.
- Entrada pronta para o [`big-idea-scoring`](big-idea-scoring.md).

## Exemplo
Oferta de amostra: curso de inglês para devs (célula 2×4). Árvore ToT (candidatas finais):
- **Ramo Mecanismo** → "Shadowing Técnico: o método de imitação que te faz falar inglês de entrevista em 60 dias."
- **Ramo Inimigo** → "Não é o seu inglês. É a gramática que te ensinaram e que ninguém usa numa entrevista real."
- **Ramo Promessa** → "Passe na entrevista em inglês da sua vaga dos sonhos em 60 dias — falando, não decorando."
- **Ramo Identidade** → "Vire o dev que trabalha de qualquer lugar do mundo, em dólar, sem travar na call."
- **Ramo Descoberta** → "Por que ler documentação em inglês o dia todo não te faz falar — e o que faz."
- Estas 5 seguem para o scoring; suponha que "Inimigo" vença por novidade + fit de célula 2×4 (público sente a dor, não a solução).

## Armadilhas
- **Fixar na primeira ideia.** O propósito do ToT é justamente romper isso. Force os 5 ramos antes de favorecer qualquer um.
- **Ramos que são a mesma ideia.** 5 promessas disfarçadas não é divergência. Garanta uma dimensão diferente por ramo.
- **Gerar sem lastro.** Ideia bonita sem mecanismo/prova é slogan. Toda candidata carrega evidência.
- **Confundir divergência com entrega.** ToT é interno; o agente entrega UMA. Não despeje 5 ideias no Offer Book.
- **Ignorar a célula.** Ramos que não casam com a consciência × sofisticação geram candidatas natimortas.
- **Pular o registro.** Repetir um ângulo já gasto (no `big-idea-registry`) desperdiça o exercício. Consulte o histórico.

## Interações
- **Agentes**: `big-idea-architect` (dono — diverge com ToT, depois converge), `avatar-voc-investigator` (fornece dor, sonho, inimigo em verbatim), `mechanism-architect` (fornece o mecanismo de cada ramo), `positioning-lead-strategist` (a célula que filtra os ramos), `market-sophistication-analyst` (o estágio que exige ramos não-óbvios).
- **Frameworks que pareiam**: [`big-idea-scoring`](big-idea-scoring.md) (converge as candidatas), [`promise-hook-villain`](promise-hook-villain.md) (formata cada candidata), [`power-of-one`](../power-of-one.md) (a regra de UMA ideia), [`big-idea-generator`](../big-idea-generator.md), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md).

## Fontes
> **Fonte:** Tree-of-Thoughts como método de divergência estruturada, alinhado ao raciocínio hierárquico de Sapient Inc., *Hierarchical Reasoning Model* (arXiv:2506.21734, 2025); fundamentos de Big Idea em Eugene M. Schwartz, *Breakthrough Advertising* (1966) e David Ogilvy, *Ogilvy on Advertising* (1983) — via [`../../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../../reference/books/copywriting/schwartz-breakthrough-advertising.md) e [`../../reference/books/copywriting/ogilvy-on-advertising.md`](../../reference/books/copywriting/ogilvy-on-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
