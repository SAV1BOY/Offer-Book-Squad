---
id: template.strategy.battle-cards
title: "Battle Cards — nós × concorrente (B2B)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [positioning/dunford-positioning, positioning/category-design, proof-to-claim-chain]
checklists: [positioning/positioning-differentiation-gate]
sources:
  - "Dixon & Adamson, *The Challenger Sale* (2011)"
tags: [template, battle-cards, competition, positioning, b2b, sales-enablement]
---

# Battle Cards — nós × concorrente

## Como usar
Uma carta por concorrente, usada na fase [`03-positioning-and-battle-cards`](../../projects/enterprise-deal-book-project/03-positioning-and-battle-cards.md) do enterprise-deal-book e por quem está no deal. Arma o vendedor/champion com **win themes**, **landmines** (perguntas que expõem a fraqueza do concorrente) e **respostas a objeção**. Toda afirmação sobre o concorrente precisa de lastro ([`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)) — nada de FUD inventado (o [`compliance-auditor`](../../agents/compliance-auditor.md) veta).

## Campos & Instruções
Preencha um bloco por concorrente. `win_themes` = onde ganhamos de forma defensável. `landmines` = perguntas que o cliente deve fazer ao concorrente. `traps` = onde NÃO entrar (onde eles ganham) — seja honesto. Revise cada carta por **trimestre**, ou sempre que um concorrente mudar preço, posição ou lançar feature: uma battle card desatualizada perde o deal e queima a credibilidade do champion interno. A honestidade nos `traps` é estratégica, não fraqueza — reconhecer onde o rival ganha aumenta a confiança de quem defende você por dentro e evita que o champion seja pego de surpresa numa reunião de comitê.

## O Template
```md
# Battle Card — {{nós}} vs {{concorrente}}

- **Categoria/posição deles:** {{como se posicionam}}
- **Quando aparecem:** {{em que tipo de deal}}

## Nós × Eles
| Dimensão | Nós | Eles | Evidência (nossa) |
|---|---|---|---|
| {{mecanismo}} | {{}} | {{}} | {{proof-id}} |
| {{TCO}} | {{}} | {{}} | {{}} |
| {{tempo p/ valor}} | {{}} | {{}} | {{}} |

## Win themes (onde ganhamos, defensável)
- {{tema 1 + prova}} · {{tema 2 + prova}}

## Landmines (perguntas p/ o cliente fazer a eles)
- "{{pergunta que expõe a fraqueza deles}}"

## Traps (onde eles ganham — não brigar aqui)
- {{cenário em que eles são a escolha certa}}

## Objeção → Resposta
| Objeção ("eles fazem X") | Resposta (com prova) |
|---|---|
| {{}} | {{}} |
```

## Exemplo preenchido
**Nós (observabilidade nativa) vs Incumbente legado.** Win theme: MTTR −38% (caso fintech Z, `proof-fintech-z`). Landmine: "pergunte a eles o custo por GB ingerido a 1TB/dia". Trap: se já têm contrato enterprise de 3 anos com o legado e baixo MTTR, não force — nutra. Objeção "eles têm mais integrações" → "temos as 20 que importam para fintech + API aberta; veja `proof-integrations`".

## DoD do entregável
1 carta por concorrente ativo · win themes **com prova** (sem FUD) · ≥1 landmine e ≥1 trap honesto por carta · objeções mapeadas com resposta lastreada · passou no [`positioning-differentiation-gate`](../../checklists/positioning/positioning-differentiation-gate.md).
