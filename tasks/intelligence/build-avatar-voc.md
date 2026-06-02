---
id: task.intelligence.build-avatar-voc
title: "Build Avatar & VOC — Construir o Avatar pela Voz do Cliente, Minerar Verbatims e Mapear Objeções"
type: task
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
consumes:
  - artifact.market-brief
  - decision.awareness-level
  - template.strategy.avatar-icp
  - template.strategy.voc-verbatim-bank
produces:
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - artifact.objection-belief-map
frameworks:
  - avatar-voc-investigator/voc-mining
  - avatar-voc-investigator/objection-belief-mapping
  - positioning/jtbd
checklists:
  - avatar/avatar-voc-verbatim-gate
  - avatar/avatar-dominant-emotion-gate
  - avatar/avatar-objection-map-gate
registries: [objection-registry]
metrics: [big_idea_strength, value_equation_score, proof_coverage_rate]
tags: [intelligence, avatar, icp, voc, verbatim, objecao, falsa-crenca, dmu, jtbd, d1]
---

# Build Avatar & VOC — construir o avatar pela voz do cliente, minerar verbatims e mapear objeções

## Objetivo
Reconstruir, na voz literal do comprador, o avatar/ICP por segmento, com ≥10 verbatims literais por segmento, a emoção dominante nomeada e o mapa de objeções/falsas crenças (mais a DMU, se B2B), no estado em que a copy soa como a cabeça do cliente e nenhuma objeção fica sem resposta.

## Agente dono
[`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md). O etnógrafo do squad. Não diagnostica o estágio do mercado (herda do market-brief), não cura prova, não escreve copy; devolve o retrato falado do comprador. Sem poder de veto — sinaliza riscos.

## Gatilho / Quando
Roda em D1, quando o [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md) entrega o market-brief com o mercado-alvo recortado e o nível de consciência, e o pipeline libera a trilha de avatar/VOC. **Pré-condição:** existe um mercado-alvo definido (não "todo mundo") e um nível de consciência declarado — a consciência muda onde a copy começa e, logo, quais objeções pesam mais. Se o mercado-alvo abriga dois públicos com vozes incompatíveis, **segmento e sinalizo** — não forço um avatar médio que não soa como ninguém. Sem fonte de VOC acessível, marco o banco como abaixo do piso e sinalizo, em vez de inventar verbatims (verbatim fabricado é falha grave).

## Inputs (Consome)
- **`artifact.market-brief`** (do market-analyst) — o mercado-alvo recortado, o nível de consciência (1-5) e a célula da matriz. A consciência define o registro emocional esperado (nível 2 = dor crua; nível 4 = comparação/hesitação).
- **VOC bruto** (handoff de pesquisa ou coleta própria) — reviews (1 e 5 estrelas), entrevistas, transcrições de suporte/vendas, posts de fórum, comentários, DMs.
- **[`template.strategy.avatar-icp`](../../templates/strategy/avatar-icp-template.md)** e **[`template.strategy.voc-verbatim-bank`](../../templates/strategy/voc-verbatim-bank-template.md)** — os formatos do avatar e do banco de verbatims.
- **Registry escrito:** [`objection-registry`](../../data/registries/objection-registry.md) — sou o dono da fonte deste registro.

## Procedimento
1. **Segmente o mercado-alvo.** Leia uma amostra de VOC e agrupe por vocabulário/dor. Divida em 1–3 segmentos com voz coerente. Dois sub-perfis com objeções diferentes → minere ≥10 verbatims para **cada**.
2. **Minere VOC (verbatims literais).** Aplique [`voc-mining`](../../frameworks/avatar-voc-investigator/voc-mining.md): extraia frases exatas dos reviews/entrevistas, preservando as palavras do cliente, com fonte rastreável. Piso: ≥10 por segmento. Paráfrase não conta.
3. **Nomeie a emoção dominante (Tree-of-Thoughts).** Gere ≥3 candidatas e pontue por *frequência nos verbatims* (×3), *intensidade* (×2), *alavancagem para a Big Idea* (×1), *aderência ao JTBD social/emocional* (×1). Escolha a mais sustentada pelos verbatims; as outras viram secundárias. Errar a emoção = copy que fala com a cabeça errada.
4. **Mapeie o Job To Be Done.** Aplique [`jtbd`](../../frameworks/positioning/jtbd.md): funcional, emocional, social. Marque qual peso mais — orienta a prova que o curator deve priorizar.
5. **Mapeie objeções e falsas crenças.** Aplique [`objection-belief-mapping`](../../frameworks/avatar-voc-investigator/objection-belief-mapping.md): para cada "não", identifique a **falsa crença-raiz** ("já tentei vários cursos, inglês não é pra mim" → crença: o problema é aptidão, não método). Aprofunde além do "não" de superfície — é o que o mecanismo precisará reverter.
6. **Mapeie a DMU se B2B.** O cliente não é uma pessoa — é um comitê. Para cada papel (econômico/CFO, técnico/usuário, bloqueador/risco/jurídico, influenciador): o medo, a objeção e o que precisa ouvir. Minere verbatims segmentados por papel.
7. **Self-verify (Bloom + red-team).** Cada segmento tem ≥10 verbatims literais com fonte? Há contra-evidência à emoção escolhida? Cada objeção tem a crença-raiz? O que o `compliance-auditor`/`mechanism-architect` rejeitaria (verbatim sem fonte, emoção sem lastro)? Corrija.
8. **Registre e passe os gates.** Escreva cada objeção no `objection-registry` (`objection_text` verbatim, `category`, `underlying_emotion`, `awareness_level`, `severity`, `status: open`, `owner_agent`). Alimente o `proof-registry` com depoimentos colhidos (o curator classifica o `strength`). Passe os três gates de avatar.

## Frameworks
- [`avatar-voc-investigator/voc-mining`](../../frameworks/avatar-voc-investigator/voc-mining.md) — ≥10 verbatims literais/segmento + emoção dominante.
- [`avatar-voc-investigator/objection-belief-mapping`](../../frameworks/avatar-voc-investigator/objection-belief-mapping.md) — mapa objeção → falsa crença → categoria → severidade (e DMU se B2B, via [`dmu-mapping-b2b`](../../frameworks/avatar-voc-investigator/dmu-mapping-b2b.md)).
- [`positioning/jtbd`](../../frameworks/positioning/jtbd.md) — Job To Be Done funcional/emocional/social.

## Outputs (Produz)
- **`artifact.avatar-icp`** — avatar/ICP por segmento (demografia mínima + contexto vivo).
- **`artifact.voc-verbatim-bank`** — ≥10 verbatims literais por segmento com fonte + emoção dominante ancorada.
- **`artifact.objection-belief-map`** — objeção → falsa crença → categoria → severidade (e a DMU por papel, se B2B).
- **Registry escrito:** [`objection-registry`](../../data/registries/objection-registry.md) com cada objeção minerada.

## Definition of Done
Cada segmento tem ≥10 verbatims literais (não paráfrases); a emoção dominante de cada segmento está nomeada e ancorada em ≥3 verbatims; cada objeção tem a falsa crença, a categoria e a severidade; se B2B, a DMU cobre todos os papéis com o medo/critério de cada um; os três gates de avatar estão verdes; as objeções estão no registry. Máximo de 3 ciclos; se a fonte não permite atingir o piso de 10, entregue com confiança rebaixada e pedido de pesquisa registrado.

## Gates
- [`avatar/avatar-voc-verbatim-gate`](../../checklists/avatar/avatar-voc-verbatim-gate.md)
- [`avatar/avatar-dominant-emotion-gate`](../../checklists/avatar/avatar-dominant-emotion-gate.md)
- [`avatar/avatar-objection-map-gate`](../../checklists/avatar/avatar-objection-map-gate.md) (esta é a **aresta-chave** que destrava `curate-proof`)

## Métricas
Move KPIs da família **offer_quality** ([`config.yaml`](../../config.yaml) `kpis:`), por entregar a matéria-prima (voz do cliente) da oferta:
- **`big_idea_strength`** — a emoção dominante e o JTBD ancoram o critério "relevante" da Big Idea; sem o VOC certo a tese fala com a cabeça errada.
- **`value_equation_score`** — o sonho real e os sacrifícios temidos colhidos em verbatim alimentam as alavancas Sonho/Esforço da Value Equation.
- **`proof_coverage_rate`** — o mapa de objeções define **contra o que** provar; depoimentos minerados abastecem o `proof-registry` para a cobertura de claims.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (família offer_quality), com objeções gravadas em [`objection-registry`](../../data/registries/objection-registry.md).

## Handoff
**Próxima task:** [`curate-proof`](curate-proof.md) — dono [`proof-credibility-curator`](../../agents/proof-credibility-curator.md), que recebe o **mapa de objeções** para casar prova a cada objeção (a aresta real do pipeline D1, via `avatar/avatar-objection-map-gate`). Em paralelo, o [`mechanism-architect`](../../agents/mechanism-architect.md) recebe as falsas crenças que o mecanismo precisa reverter; o [`big-idea-architect`](../../agents/big-idea-architect.md), a emoção dominante e o JTBD. **Garantia:** todo downstream recebe avatar/ICP por segmento, ≥10 verbatims literais com fonte, a emoção dominante ancorada, o mapa de objeções categorizado por severidade, o JTBD e (B2B) a DMU por papel — tudo da voz do cliente, nunca de suposição. O curator não recebe um mapa de objeções pela metade.
