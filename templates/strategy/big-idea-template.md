---
id: template.strategy.big-idea
title: "Big Idea Sheet — UMA Tese Travada pelos 5 Critérios"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
consumes: [template.strategy.mechanism-sheet, template.strategy.proof-bank, template.strategy.avatar-icp, template.strategy.market-brief]
produces: [template.core.offer-book-master, template.strategy.positioning]
frameworks: [big-idea-architect.big-idea-scoring, big-idea-architect.big-idea-ideation-tot, big-idea-architect.promise-hook-villain, power-of-one, big-idea-generator, awareness-x-sophistication]
checklists: [big-idea/big-idea-single-gate, big-idea/big-idea-new-big-credible-gate, big-idea/big-idea-awareness-fit-gate, big-idea/big-idea-relevant-proprietary-gate]
registries: [big-idea-registry, decision-registry]
tags: [template, big-idea, power-of-one, scoring, criteria, strategy]
---

# Big Idea Sheet — UMA Tese Travada pelos 5 Critérios

Esta planilha destila tudo numa **única** Big Idea (princípio `one_big_idea` / [`power-of-one`](../../frameworks/power-of-one.md)). Você diverge em 3-5 candidatas ([`big-idea-ideation-tot`](../../frameworks/big-idea-architect/big-idea-ideation-tot.md)) e converge pontuando cada uma em **5 critérios** ([`big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md)): **Nova** (fresca, não-óbvia), **Grande** (importa de verdade ao avatar), **Crível** (mecanismo + prova reais), **Casa com a consciência** (fit com a célula de Schwartz) e **Única/Possuível** (só você pode dizer). A vencedora vira a tese do lançamento, em formato promessa-gancho-vilão. Múltiplas ideias = reprovação automática. É o documento que o `big-idea-architect` entrega antes do posicionamento e do HARD STOP do Offer Book.

## Como usar
- **Agente dono:** `big-idea-architect` (camada D3, entrega **UMA** tese — duas = reprovação). Aprovado pelo `offerbook-chief`; "Crível" checado pelo `compliance-auditor` (pode vetar).
- **Task:** `lock-big-idea`. Consome o [`mechanism-sheet`](mechanism-sheet-template.md) (sustenta "Crível" e "Única"), o [`proof-bank`](proof-bank-template.md) (o lastro), o [`avatar-icp`](avatar-icp-template.md) (sustenta "Grande") e o [`market-brief`](market-brief-template.md) (a célula de consciência × sofisticação).
- **Quando:** depois do Offer Book de oferta (mecanismo, valor, preço, money model), antes do posicionamento. Alimenta o [`offer-book-master`](../core/offer-book-master.md) e a [`positioning`](positioning-template.md). Validado pelos gates de big-idea.
- Regra: pontue cada critério **0-5** com justificativa rastreável (gosto disfarçado de nota = reprovação). Aplique as **eliminatórias**: Crível ≤ 2 ou Casa ≤ 2 descarta a candidata, por maior que seja a soma. O output é sempre UMA.

## Campos & Instruções
- **{{CANDIDATAS}}** — as 3-5 candidatas do ToT, cada uma em uma linha (mecanismo, inimigo, promessa, descoberta, identidade).
- **{{NOTA_NOVA}}** — 0-5: quão fresca e contra-intuitiva é? Ângulo já saturado (sofisticação alta) = nota baixa. Cheque o [`big-idea-registry`](../../data/registries/big-idea-registry.md): o que já foi usado não é "Novo".
- **{{NOTA_GRANDE}}** — 0-5: quão profundamente importa ao avatar? Toca a emoção e o resultado dominantes do VOC? "Interessante mas pequena" = nota baixa.
- **{{NOTA_CRIVEL}}** — 0-5: há mecanismo nomeado **e** prova que sustentam? Promessa grande sem lastro = nota baixa e risco de veto. **Eliminatória ≤ 2.**
- **{{NOTA_CASA}}** — 0-5: encaixa na célula de consciência × sofisticação do público? Ideia direta para público frio = nota baixa. **Eliminatória ≤ 2.**
- **{{NOTA_UNICA}}** — 0-5: só **você** pode dizer isto (pelo mecanismo, história, prova)? Se o concorrente copia a frase amanhã = nota baixa.
- **{{VENCEDORA}}** — a candidata de maior soma entre as sobreviventes. Empate decide-se pelo maior "Casa".
- **{{PROMESSA}}** / **{{GANCHO}}** / **{{VILAO}}** — a vencedora formatada: a promessa central, o gancho que para, o inimigo comum a derrotar ([`promise-hook-villain`](../../frameworks/big-idea-architect/promise-hook-villain.md)).
- **{{JUSTIFICATIVA}}** — por que esta venceu e por que as demais perderam (rastreável, célula a célula).

## O Template
```
# BIG IDEA SHEET — {{NOME_DO_LANCAMENTO}}
Owner: big-idea-architect · Data: {{DATA}}
Regra: UMA Big Idea (Power of One). Eliminatórias: Crível ≤2 ou Casa ≤2 = descarte.

## 1. CANDIDATAS (do ToT) E SCORING (0-5)
| Candidata | Nova | Grande | Crível | Casa | Única | Soma |
|---|---|---|---|---|---|---|
| {{CAND_1}} | {{N}} | {{G}} | {{C}} | {{CA}} | {{U}} | {{SOMA}} |
| {{CAND_2}} | {{N}} | {{G}} | {{C}} | {{CA}} | {{U}} | {{SOMA}} |
| {{CAND_3}} | {{N}} | {{G}} | {{C}} | {{CA}} | {{U}} | {{SOMA}} |

## 2. ELIMINATÓRIAS APLICADAS
{{QUEM_FOI_ELIMINADA_E_POR_QUE}}

## 3. A VENCEDORA (UMA)
Big Idea: {{VENCEDORA}}  (soma {{SOMA_VENCEDORA}})
Promessa: {{PROMESSA}}
Gancho: {{GANCHO}}
Vilão (inimigo comum): {{VILAO}}

## 4. JUSTIFICATIVA RASTREÁVEL
{{JUSTIFICATIVA}}  (por célula de consciência × sofisticação)

## 5. GATES
UMA só ideia (big-idea-single-gate): {{STATUS_SINGLE}}
Nova/Grande/Crível (big-idea-new-big-credible-gate): {{STATUS_NBC}}
Casa com a consciência (big-idea-awareness-fit-gate): {{STATUS_FIT}}
```

## Exemplo preenchido
> **# BIG IDEA SHEET — Aprovado em Inglês (curso para devs)**
> Owner: big-idea-architect · Data: 2026-06-02
>
> **1. CANDIDATAS E SCORING**
> | Candidata | Nova | Grande | Crível | Casa | Única | Soma |
> |---|---|---|---|---|---|---|
> | Mecanismo ("Shadowing Técnico") | 4 | 4 | 5 | 4 | 5 | **22** |
> | Inimigo ("a gramática matou seu inglês") | 5 | 5 | 4 | 5 | 4 | **23** |
> | Promessa ("fluente em 60 dias") | 2 | 5 | 3 | 4 | 2 | 16 |
> | Identidade ("o dev global") | 3 | 4 | 3 | 2 | 3 | eliminada |
>
> **2. ELIMINATÓRIAS** — "Identidade" descartada por Casa = 2 (público frio ainda não se vê como "dev global"). Nenhuma com Crível ≤ 2.
> **3. A VENCEDORA** — Big Idea: **"A gramática matou seu inglês falado"** (soma 23). Promessa: você passa na entrevista em inglês em 60 dias. Gancho: "Você lê documentação em inglês o dia todo, mas trava na call. O problema não é o seu inglês." Vilão: o método de gramática que ensina inglês de turista.
> **4. JUSTIFICATIVA** — Mais nova e maior que o mecanismo puro; casa com a célula 2×4 (público sente a dor e culpa o próprio inglês); é possuível porque ancora no Shadowing Técnico como a alternativa ao vilão.
> **5. GATES** — UMA só ideia: **VERDE**. Nova/Grande/Crível: **VERDE** (mecanismo nomeado + 37 alunos contratados). Casa: **VERDE** (célula 2×4).

## DoD do entregável
A Big Idea Sheet está pronta quando: (1) há 3-5 candidatas geradas por ToT, cada uma pontuada **0-5** nos cinco critérios com justificativa (sem gosto disfarçado de nota); (2) as **eliminatórias** foram aplicadas — toda candidata com Crível ≤ 2 ou Casa ≤ 2 está descartada com o porquê; (3) o output é **UMA** vencedora (princípio Power of One — duas = reprovação automática, `big-idea-single-gate`); (4) "Crível" se apoia em mecanismo nomeado **e** prova real do [`proof-bank`](proof-bank-template.md), não na força retórica da frase (`big-idea-new-big-credible-gate`); (5) "Casa" confirma o fit com a célula de consciência × sofisticação do [`market-brief`](market-brief-template.md) (`big-idea-awareness-fit-gate`); (6) a vencedora está formatada em promessa-gancho-vilão; (7) "Nova" e "Única" foram checadas contra o [`big-idea-registry`](../../data/registries/big-idea-registry.md) (ângulo gasto não é novo); (8) a matriz, a vencedora e as descartadas estão registradas no [`big-idea-registry`](../../data/registries/big-idea-registry.md) e a decisão no [`decision-registry`](../../data/registries/decision-registry.md). Só então a tese alimenta a [`positioning`](positioning-template.md) e o [`offer-book-master`](../core/offer-book-master.md).
