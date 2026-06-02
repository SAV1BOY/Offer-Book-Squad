---
id: task.offer-architecture.define-mechanism
title: "Define Mechanism — Isolar e Nomear o Mecanismo Único, Provado e Comprimido em Uma Frase"
type: task
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
consumes:
  - artifact.market-brief
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - data.registry.objection
produces:
  - artifact.mechanism-sheet
  - decision.mechanism-name
frameworks: [unique-mechanism, value-equation]
checklists:
  - mechanism/mechanism-naming-gate
  - mechanism/mechanism-proof-gate
  - mechanism/mechanism-one-sentence-gate
registries: [offer-registry]
metrics: [value_equation_score, big_idea_strength, proof_coverage_rate]
tags: [offer-architecture, mecanismo, unique-mechanism, 5-whys, naming, prova, d2]
---

# Define Mechanism — isolar e nomear o mecanismo único, provado e comprimido em uma frase

## Objetivo
Achar a causa-raiz do problema do avatar e a causa-raiz da solução, contrastá-las velho×novo e batizá-las com um nome próprio, crível, provado e comprimido em uma frase que o avatar repete e acredita — o núcleo conceitual do qual todo o resto deriva.

## Agente dono
[`mechanism-architect`](../../agents/mechanism-architect.md). Produz o *porquê* funciona. Não escreve copy, não desenha preço, não monta funil. Sem poder de veto — sinaliza; suas flags informam os vetos do `value-equation-engineer` e do `compliance-auditor`.

## Gatilho / Quando
Roda em D2, quando: (a) o market-brief declara sofisticação e consciência com evidência; (b) o avatar e o banco de VOC existem com a **objeção dominante** mapeada; (c) o chief pede para nomear ou refazer o mecanismo. **Pré-condição:** o diagnóstico de mercado está verde. Se a sofisticação é 1-2, sinalizo que talvez nem precise de mecanismo nomeado (basta claim/amplificação) e devolvo a decisão ao chief. Sem objeção dominante, **não prossigo** — peço o verbatim que ancora a culpa atual. Se o produto não tem nenhuma diferença real de método (commodity pura), recuso fabricar mecanismo falso e escalono — mecanismo inventado sem lastro é mentira.

## Inputs (Consome)
- **`artifact.market-brief`** — estágio de sofisticação (1-5), nível de consciência, mecanismos dos concorrentes já em mercado (para não repetir), o claim saturado que parou de funcionar.
- **`artifact.avatar-icp`** + **`artifact.voc-verbatim-bank`** — a emoção dominante, a **causa que o avatar culpa hoje** ("é genética", "é falta de disciplina") e a linguagem literal.
- **[`data.registry.objection`](../../data/registries/objection-registry.md)** — a objeção #1 ("já tentei tudo e nada funcionou") que o mecanismo precisa neutralizar reposicionando a culpa.
- **Registry escrito:** [`offer-registry`](../../data/registries/offer-registry.md).

## Procedimento
1. **Ache a causa-raiz do problema (5 Whys).** Aplique [`unique-mechanism`](../../frameworks/unique-mechanism.md) sobre a dor: desça do sintoma até um fator sistêmico/fisiológico reposicionável (ex.: "o corpo entra em modo de economia após dietas repetidas"). A culpa real raramente é moral.
2. **Ache a causa-raiz da solução.** Isole o **passo causal** que de fato muda o resultado — não a lista de features. Confirme que esse passo tem lastro no `proof-registry`.
3. **Valide a alavanca.** Aplique [`value-equation`](../../frameworks/value-equation.md): o mecanismo move ≥1 alavanca real (Sonho, Probabilidade, Tempo ou Esforço)? Se não move nenhuma, é só rótulo — reformule em torno da alavanca real, senão o `value-equation-engineer` reprova a jusante.
4. **Monte a tabela velho×novo.** Por dimensão: jeito velho (falha) vs jeito novo (mecanismo). É o contraste que o positioning herda.
5. **Batize (Tree-of-Thoughts).** Calibre pela sofisticação: estágio 3 = **introduzir** o mecanismo; estágio 4 = **elevar** um existente (mais rápido, mais fácil, menos sacrifício). Gere ≥3 nomes candidatos e pontue por *novidade* (×3), *credibilidade* (×3), *simplicidade* (×2), *reposiciona a culpa* (×2). Nome que pontua alto em novidade mas zero em credibilidade é **rejeitado** — novidade sem prova é clickbait.
6. **Comprima em uma frase.** Reescreva o vencedor numa frase de 3ª série que o avatar entende e acredita na primeira leitura ("Você não falhou — seu termostato metabólico travou, e ele pode ser reajustado").
7. **Self-verify (Bloom + red-team).** A cadeia causal está completa? O nome casa com o estágio (introduzir vs elevar)? O mecanismo é diferente dos concorrentes, ou recriei um clichê? Cada elo tem lastro? *"O que o `compliance-auditor` rejeitaria?"* (alegação sem fonte, promessa de cura). *"O que o `value-equation-engineer` reprovaria?"* (mecanismo que não move alavanca). Corrija.
8. **Registre e passe os gates.** Logue o mecanismo no `offer-registry` (`mechanism_id`, nome, problema-raiz, solução-raiz, tabela, frase, alavancas, sofisticação-alvo, `prova_refs`, `status`). `status: provado` só após o `mechanism-proof-gate` verde. Registre a decisão de naming (candidatos, vencedor, motivo da poda).

## Frameworks
- [`unique-mechanism`](../../frameworks/unique-mechanism.md) — 5 Whys, velho×novo, naming → cadeia causal + nome + 1 frase.
- [`value-equation`](../../frameworks/value-equation.md) — validar que o mecanismo move ≥1 alavanca.

## Outputs (Produz)
- **`artifact.mechanism-sheet`** ([`template`](../../templates/strategy/mechanism-sheet-template.md)) — nome próprio, problema-raiz, solução-raiz, tabela velho×novo, alavancas movidas, frase única, sofisticação-alvo, prova, status.
- **`decision.mechanism-name`** — o nome travado com o motivo.
- **Registry escrito:** [`offer-registry`](../../data/registries/offer-registry.md).

## Definition of Done
A cadeia causal está completa do sintoma à raiz; o mecanismo é diferente dos concorrentes do market-brief; cada elo tem lastro no `proof-registry`; o mecanismo move ≥1 alavanca declarada; a frase passa no teste de 1ª leitura; os três gates de mecanismo estão verdes; o registro tem `status: provado`. Máximo de 3 ciclos antes de escalar ao chief.

## Gates
- [`mechanism/mechanism-naming-gate`](../../checklists/mechanism/mechanism-naming-gate.md)
- [`mechanism/mechanism-proof-gate`](../../checklists/mechanism/mechanism-proof-gate.md)
- [`mechanism/mechanism-one-sentence-gate`](../../checklists/mechanism/mechanism-one-sentence-gate.md)

## Métricas
Move KPIs da família **offer_quality** ([`config.yaml`](../../config.yaml) `kpis:`), por nomear o núcleo conceitual do qual o valor, a tese e a prova derivam:
- **`value_equation_score`** — o mecanismo precisa mover ≥1 alavanca real (Sonho/Probabilidade/Tempo/Esforço); um mecanismo que não move alavanca é só rótulo e derruba a nota de valor a jusante.
- **`big_idea_strength`** — a frase única e o contraste velho×novo são a matéria-prima proprietária da Big Idea; sem mecanismo nomeado, a tese perde o critério "novo/proprietário".
- **`proof_coverage_rate`** — cada elo causal só fica `provado` com lastro no `proof-registry`; o mecanismo provado eleva a cobertura de claims.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (família offer_quality), com o mecanismo registrado em [`offer-registry`](../../data/registries/offer-registry.md).

## Handoff
**Próxima task:** [`score-value-equation`](score-value-equation.md) — dono [`value-equation-engineer`](../../agents/value-equation-engineer.md), que recebe o mecanismo nomeado como insumo central da oferta e as alavancas que ele já move. Adiante, o [`money-model-designer`](../../agents/money-model-designer.md) recebe o mecanismo para a espinha; o [`big-idea-architect`](../../agents/big-idea-architect.md), a frase única como matéria-prima da tese; o [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md), o contraste velho×novo. **Garantia:** todo downstream recebe um mecanismo com nome próprio, cadeia causal provada e 1 frase — ou um flag explícito de `provisório` com a lacuna nomeada.
