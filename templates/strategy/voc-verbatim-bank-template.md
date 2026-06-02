---
id: template.strategy.voc-verbatim-bank
title: "VOC Verbatim Bank — Banco da Voz do Cliente"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
consumes: [template.strategy.market-brief, template.strategy.avatar-icp]
produces: [template.core.offer-book-master]
frameworks: [avatar-voc-investigator/voc-mining, avatar-voc-investigator/objection-belief-mapping]
checklists: [avatar/avatar-voc-verbatim-gate, avatar/avatar-dominant-emotion-gate]
registries: [objection-registry]
tags: [template, voc, verbatim, swipe-language, strategy]
---

# VOC Verbatim Bank — Banco da Voz do Cliente

Este template guarda a **fala literal** do cliente, organizada para virar copy. Não é resumo do que o cliente quis dizer — é a citação exata, com a fonte. É a matéria-prima da linguagem de mercado: ganchos, dores, desejos e objeções saem daqui em palavras que o avatar reconhece como dele. Voz copiada do cliente vende; voz inventada pelo redator soa falsa.

## Como usar
- **Agente dono:** `avatar-voc-investigator` (camada D1).
- **Task:** `build-avatar-voc`. Consome reviews, comentários, transcrições de entrevistas, tickets de suporte, posts de fórum.
- **Quando:** em paralelo com o [`avatar-icp`](avatar-icp-template.md). Alimenta o bloco 2 ("AVATAR") do [`offer-book-master`](../core/offer-book-master.md) e abastece toda a copy de D4. Validado por [`avatar-voc-verbatim-gate`](../../checklists/avatar/avatar-voc-verbatim-gate.md) (≥10 verbatims) e [`avatar-dominant-emotion-gate`](../../checklists/avatar/avatar-dominant-emotion-gate.md).
- Regra: **transcreva, não parafraseie**. Cada linha cita a fala exata + a fonte verificável. Marque a emoção e a categoria para a copy achar rápido.

## Campos & Instruções
- **{{N_VERBATIMS}}** — o total de citações coletadas. O piso do gate é **10**; o alvo é variar fonte (review, entrevista, comentário, suporte).
- **{{VERBATIM}}** — a fala literal, entre aspas, sem editar a gramática do cliente. É o que dá autenticidade.
- **{{FONTE}}** — onde a fala foi dita (review da loja X, entrevista #3, comentário no anúncio, ticket #112). Verificável.
- **{{CATEGORIA}}** — o tipo da fala: DOR, DESEJO, OBJEÇÃO, LINGUAGEM (jeito de falar/jargão), GANCHO (frase que já vende sozinha). Ajuda a copy a filtrar.
- **{{EMOCAO}}** — a emoção embutida na fala (medo, frustração, esperança, vergonha, orgulho). Soma para a emoção dominante.
- **{{USO_NA_COPY}}** — onde aquela frase serve (lead, dor agitada, depoimento por objeção, fascination bullet).
- **{{EMOCAO_DOMINANTE}}** — a emoção que mais aparece no banco — o tom-base de toda a copy.
- **{{TOP_GANCHOS}}** — as 3 falas que já funcionam como gancho de abertura quase sem edição.
- **{{PALAVRAS_PROIBIDAS}}** — termos que o cliente **nunca** usa (jargão de dentro da casa) — para a copy evitar.

## O Template
```
# VOC VERBATIM BANK — {{MERCADO_OU_AVATAR}}
Owner: avatar-voc-investigator · Data: {{DATA}} · Verbatims: {{N_VERBATIMS}} (piso 10)

## TABELA DE VERBATIMS
| # | Verbatim (literal) | Categoria | Emoção | Fonte | Uso na copy |
|---|---|---|---|---|---|
| 1 | "{{VERBATIM_1}}" | {{CATEGORIA_1}} | {{EMOCAO_1}} | {{FONTE_1}} | {{USO_1}} |
| 2 | "{{VERBATIM_2}}" | {{CATEGORIA_2}} | {{EMOCAO_2}} | {{FONTE_2}} | {{USO_2}} |
| 3 | "{{VERBATIM_3}}" | {{CATEGORIA_3}} | {{EMOCAO_3}} | {{FONTE_3}} | {{USO_3}} |
| ... | ... | ... | ... | ... | ... |
| 10+ | "{{VERBATIM_N}}" | {{CATEGORIA_N}} | {{EMOCAO_N}} | {{FONTE_N}} | {{USO_N}} |

## SÍNTESE
Emoção dominante: {{EMOCAO_DOMINANTE}} (aparece em {{QUANTAS}}/{{N_VERBATIMS}})
Top 3 ganchos prontos:
  1. "{{GANCHO_1}}"
  2. "{{GANCHO_2}}"
  3. "{{GANCHO_3}}"
Palavras que o cliente NUNCA usa (banir na copy): {{PALAVRAS_PROIBIDAS}}
```

## Exemplo preenchido
> **# VOC VERBATIM BANK — E-commerce PME (recuperação de carrinho)**
> Owner: avatar-voc-investigator · Data: 2026-06-02 · Verbatims: **12** (piso 10)
>
> | # | Verbatim | Categoria | Emoção | Fonte | Uso na copy |
> |---|---|---|---|---|---|
> | 1 | "vejo o dinheiro escapar no carrinho e não sei recuperar" | DOR | frustração | entrevista #2 | lead / dor agitada |
> | 2 | "quero lucrar mais sem gastar mais em anúncio" | DESEJO | esperança | review loja | promessa |
> | 3 | "já tentei e-mail e não funcionou" | OBJEÇÃO | descrença | comentário ad | depoimento por objeção |
> | 4 | "não tenho tempo de ficar configurando" | OBJEÇÃO | cansaço | ticket #112 | bônus "feito-para-você" |
> | 5 | "meu nicho é diferente, comigo não funciona" | OBJEÇÃO | medo | grupo FB | prova multi-nicho |
> | 6 | "todo dia abro o painel e vejo carrinho abandonado" | LINGUAGEM | frustração | entrevista #3 | dia-na-vida |
> | 7 | "parece que deixo dinheiro na mesa" | GANCHO | culpa | review | gancho de abertura |
> | ... | (mais 5 verbatims) | ... | ... | ... | ... |
>
> **SÍNTESE** — Emoção dominante: **frustração** (7/12). Top ganchos: 1. *"parece que deixo dinheiro na mesa"*; 2. *"vejo o dinheiro escapar no carrinho"*; 3. *"quero lucrar mais sem gastar mais"*. Banir: "abandoned cart rate", "fluxo de automação" (jargão técnico que o avatar não usa).

## DoD do entregável
O VOC Verbatim Bank está pronto quando: (1) há **pelo menos 10** verbatims literais — citação exata, sem paráfrase nem correção de gramática (gate `avatar-voc-verbatim-gate`); (2) cada verbatim tem fonte verificável (review, entrevista, comentário, ticket); (3) cada verbatim está categorizado (dor/desejo/objeção/linguagem/gancho) e marcado com a emoção; (4) a emoção dominante está identificada com a contagem que a sustenta (gate `avatar-dominant-emotion-gate`); (5) há 3 ganchos prontos e a lista de palavras a banir. As objeções coletadas alimentam o [`objection-registry`](../../data/registries/objection-registry.md) e o [`avatar-icp`](avatar-icp-template.md); a síntese alimenta o bloco "AVATAR" do [`offer-book-master`](../core/offer-book-master.md) e vira linguagem de mercado para toda a copy de D4.
