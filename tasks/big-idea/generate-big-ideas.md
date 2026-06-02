---
id: task.big-idea.generate-big-ideas
title: "Generate Big Ideas — Gerar Muitas Grandes Ideias, Pontuar nos 5 Critérios e Travar UMA"
type: task
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
consumes:
  - artifact.market-brief
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - artifact.mechanism-sheet
  - artifact.value-equation
  - artifact.money-model
  - data.registry.objection
  - data.registry.proof
produces:
  - decision.big-idea-locked
  - artifact.big-idea
frameworks: [big-idea-generator, power-of-one, big-idea-architect/big-idea-ideation-tot, big-idea-architect/big-idea-scoring, big-idea-architect/promise-hook-villain, meta-launch-principle]
checklists:
  - big-idea/big-idea-single-gate
  - big-idea/big-idea-new-big-credible-gate
  - big-idea/big-idea-awareness-fit-gate
registries: [big-idea-registry]
tags: [big-idea, tree-of-thoughts, power-of-one, hook, awareness-fit, veto, d3]
---

# Generate Big Ideas — gerar muitas Grandes Ideias, pontuar nos 5 critérios e travar UMA

## Objetivo
Entregar UMA Big Idea — e apenas uma — que passe nos cinco critérios (nova, grande, crível, relevante, proprietária), case com a consciência dominante do mercado e fique cravada com promessa, gancho e vilão, ancorada no mecanismo único e rastreável à oferta provada.

## Agente dono
[`big-idea-architect`](../../agents/big-idea-architect.md), o destilador do squad. Primeiro **abre** o leque (gera 3 a 5 candidatas via Tree-of-Thoughts), depois **poda** sem dó até sobrar uma. Não escreve copy, não desenha funil, não inventa oferta. **Tem poder de veto:** múltiplas ideias travadas, ou uma ideia que falha num critério, é reprovação.

## Gatilho / Quando
Roda em D3, quando: (a) a camada D2 fecha — mecanismo nomeado e provado, value equation aprovada, money model com ≥2 partes (alvo 4), preço derivado de valor; (b) o chief pede uma Big Idea para travar antes do Offer Book DoD; (c) uma Big Idea anterior foi reprovada em gate e precisa de nova rodada. **Pré-condição:** o market-brief declara consciência e sofisticação com evidência; o mechanism-sheet traz o mecanismo em uma frase; o VOC tem a emoção dominante. **Sem mecanismo nomeado eu não gero ideia** — sem um "por quê" novo, qualquer promessa vira fanfarrice sem lastro. Se me pressionam a travar duas ideias "para testar depois", **veto** e escalono — teste A/B de ângulos é trabalho do `ad-creative-factory` sobre UMA Big Idea, não duas teses concorrentes.

## Inputs (Consome)
- **`artifact.market-brief`** — nível de consciência dominante, sofisticação, claims gastos, a multidão faminta.
- **`artifact.avatar-icp`** + **`artifact.voc-verbatim-bank`** — a emoção dominante, o desejo no idioma do avatar, os verbatims exatos.
- **`artifact.mechanism-sheet`** — o mecanismo único em uma frase, o contraste velho×novo, a causa-raiz. **É o coração proprietário da ideia.**
- **`artifact.value-equation`** + **`artifact.money-model`** — o sonho, a probabilidade, o tempo, o esforço; a espinha. A Big Idea precisa ser fiel ao que a oferta entrega.
- **[`data.registry.objection`](../../data/registries/objection-registry.md)** + **[`data.registry.proof`](../../data/registries/proof-registry.md)** — as objeções dominantes (a ideia não pode bater de frente com uma objeção sem resposta) e a prova disponível (a ideia não pode prometer além do que se prova).
- **Registry escrito:** [`big-idea-registry`](../../data/registries/big-idea-registry.md).

## Procedimento
1. **Extraia o desejo dominante e o vilão.** Aplique [`promise-hook-villain`](../../frameworks/big-idea-architect/promise-hook-villain.md): o vilão não é o avatar, é uma causa externa nova que o mecanismo revela. Reposicione a culpa.
2. **Ancore no mecanismo único.** O `mechanism-sheet` é o lastro proprietário — a ideia precisa de UM mecanismo por trás.
3. **Divergir: gere 3 a 5 candidatas (Tree-of-Thoughts — o coração).** Aplique [`big-idea-ideation-tot`](../../frameworks/big-idea-architect/big-idea-ideation-tot.md), cada uma de um ângulo distinto para não serem variações da mesma frase: (A) Oposição ao conselho convencional; (B) Descoberta do mecanismo; (C) Identidade nova; (D) Inevitabilidade matemática; (E) Atalho proibido (só com prova forte). Uma ideia solitária é palpite, não escolha.
4. **Pontuar nos 5 critérios.** Aplique [`big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md) com os critérios de [`big-idea-generator`](../../frameworks/big-idea-generator.md), nota 1-5: **Nova** (o mercado já ouviu à exaustão?), **Grande** (importa de verdade?), **Crível** (acredita, dada a prova?), **Relevante** (acerta a dor/desejo do VOC?), **Proprietária** (só você pode dizer?).
5. **Podar para UMA.** Descarte toda candidata com **qualquer critério ≤ 2** (um critério fraco afunda a ideia). Entre as sobreviventes, vence a de maior soma; desempate por **Proprietária** (a defensabilidade protege a margem). As podadas **não somem** — vão ao registry como `pruned` com o motivo, viram matéria-prima de ângulos de ad.
6. **Comprima a vencedora.** Promessa (uma frase) + gancho (o que faz parar) + vilão (causa externa). Aplique [`power-of-one`](../../frameworks/power-of-one.md): UMA tese.
7. **Cheque o fit de consciência.** A vencedora casa com a consciência dominante? (Inconsciente/problema → tese indireta, vilão/história; produto/mais-consciente → tese direta, próxima da oferta.) É fiel ao que a value-equation e o money-model entregam? Use [`meta-launch-principle`](../../frameworks/meta-launch-principle.md) para a congruência lançamento↔habilidade.
8. **Self-verify (Bloom + red-team).** Pontuei **todas** sem favoritismo pela primeira? Alguma sobrevivente tem critério ≤ 2 que deixei passar? É mesmo UMA? O gancho faz parar? O vilão culpa algo externo? *"O que o `voice-style-guardian` e o `compliance-auditor` rejeitariam?"* — se a tese só funciona com promessa que a prova não sustenta, reprovo antes da copy.
9. **Registre e passe os gates.** Logue a vencedora como `locked` e **todas** as podadas como `pruned` (com `motivo_poda`) no `big-idea-registry`; a trava também vai ao `decision-registry`. Passe os três gates de Big Idea.

## Frameworks
- [`big-idea-architect/big-idea-ideation-tot`](../../frameworks/big-idea-architect/big-idea-ideation-tot.md) — 3–5 candidatas de ângulos distintos (divergir).
- [`big-idea-architect/big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md) — matriz 5 critérios × candidata (pontuar).
- [`big-idea-generator`](../../frameworks/big-idea-generator.md) — define os 5 critérios.
- [`big-idea-architect/promise-hook-villain`](../../frameworks/big-idea-architect/promise-hook-villain.md) — promessa + gancho + vilão.
- [`power-of-one`](../../frameworks/power-of-one.md) — UMA tese travada (podar).
- [`meta-launch-principle`](../../frameworks/meta-launch-principle.md) — a tese que o próprio lançamento demonstra.

## Outputs (Produz)
- **`decision.big-idea-locked`** — a UMA tese travada.
- **`artifact.big-idea`** ([`template`](../../templates/strategy/big-idea-template.md)) — promessa, gancho, vilão, mecanismo amarrado, consciência-alvo, scores, ramos podados.
- **Registry escrito:** [`big-idea-registry`](../../data/registries/big-idea-registry.md) com a `locked` e todas as `pruned`.

## Definition of Done
Existe UMA Big Idea (não duas); a soma de critérios é alta e nenhum critério é ≤ 2; o fit de consciência está confirmado; há UM mecanismo por trás; o gancho faz o mercado parar e o vilão culpa algo externo; os três gates estão verdes; a vencedora está `locked` e as podadas `pruned` no registry. Máximo de 2 ciclos de re-ideação antes de escalar ao chief.

## Gates
- [`big-idea/big-idea-single-gate`](../../checklists/big-idea/big-idea-single-gate.md) (UMA só)
- [`big-idea/big-idea-new-big-credible-gate`](../../checklists/big-idea/big-idea-new-big-credible-gate.md) (os 5 critérios)
- [`big-idea/big-idea-awareness-fit-gate`](../../checklists/big-idea/big-idea-awareness-fit-gate.md) (fit de consciência)

## Handoff
**Próxima task:** [`lock-positioning-lead`](lock-positioning-lead.md) — dono [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md), que recebe a Big Idea travada para escolher posicionamento + lead. Adiante (após o HARD STOP), os agentes de copy recebem a tese via Offer Book. **Garantia:** o downstream recebe UMA tese, com promessa+gancho+vilão explícitos, mecanismo amarrado, fit de consciência confirmado e os ângulos podados disponíveis para variação. Nenhum agente de copy precisa "escolher entre ideias" — a escolha já foi feita e travada.
