---
id: template.offer.products-and-offers
title: "Products & Offers — Schema da Planilha-Mãe da Escada"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes: [template.strategy.value-equation, template.strategy.pricing-wtp, template.strategy.unit-economics, template.offer.offer-stack, template.offer.guarantee]
produces: [data.registry.offer]
frameworks: [money-model-sequence, offer-stack-builder, value-equation, unique-mechanism]
checklists: [money-model/money-model-four-parts-gate, money-model/money-model-cac-liquidation]
registries: [offer-registry]
tags: [template, csv-schema, money-model, products-and-offers, spreadsheet, ladder]
---

# Products & Offers — Schema da Planilha-Mãe da Escada

Este `.md` documenta o schema de [`products-and-offers-template.csv`](products-and-offers-template.csv), a **planilha-mãe** que lista cada oferta da escada (Money Model) — uma linha por oferta, do tripwire de atração à continuidade. O CSV é a fonte de verdade da sequência; este documento explica cada coluna. O `money-model-designer` é dono dos dois arquivos.

## Como usar
- **Agente dono:** `money-model-designer`. Co-lido pelo `unit-economics-stack-analyst` (valida que a atração liquida o CAC) e pelo `pricing-wtp-strategist` (confere preço vs WTP).
- **Task:** preenchido em `design-money-model` (a escada nasce aqui) e lido por toda a copy de D4 (a planilha diz qual oferta cada peça vende).
- **Quando:** depois que a Value Equation passa e o preço deriva de um método de WTP. Cada linha é uma oferta com um **papel** na escada ([`offer-types`](../../lib/taxonomies/offer-types.md)).
- **Como editar o CSV:** abra em editor de texto ou planilha. A primeira linha é o header `snake_case` — **não traduza nem reordene as colunas**. Adicione uma linha por oferta. Campos com vírgula vão entre aspas (`"..."`). Campo vazio fica vazio (sem espaço). Não ponha comentário no CSV — a documentação vive aqui.
- O gate `money-model-four-parts-gate` confere ≥2 papéis (alvo 4: atração, núcleo, upsell, downsell/continuidade). O gate `money-model-cac-liquidation` confere que ≥1 linha de `papel_money_model = atracao` liquida o CAC.

## Campos & Instruções
Uma linha por coluna do CSV: nome, tipo, valores aceitos, agente-fonte e exemplo.

| Coluna | Tipo | Valores aceitos | Agente-fonte | Exemplo |
|---|---|---|---|---|
| `offer_id` | string (chave) | `PREFIXO-NN` único (ATR/CORE/UP/DOWN/CONT) | money-model-designer | `CORE-01` |
| `nome_oferta` | string | nome de trabalho magnético ([`magic-naming`](../../frameworks/magic-naming.md)) | money-model-designer | `Motor de Recuperação 72h` |
| `papel_money_model` | enum | `atracao` `core` `upsell` `downsell` `continuidade` | money-model-designer | `core` |
| `tipo_oferta` | enum | tipos da taxonomia [`offer-types`](../../lib/taxonomies/offer-types.md) (tripwire, grand-slam-offer, done-for-you, payment-plan, assinatura…) | money-model-designer | `grand-slam-offer` |
| `publico_alvo` | string | a quem esta oferta é apresentada (avatar ou estágio do funil) | avatar-voc-investigator | `"quem comprou o diagnóstico"` |
| `resultado_prometido` | string | o resultado mensurável, na voz do avatar | value-equation-engineer | `+18% de receita recuperada em 30 dias` |
| `mecanismo_unico` | string | o mecanismo nomeado ([`unique-mechanism`](../../frameworks/unique-mechanism.md)) | mechanism-architect | `Sequência de 7 Mensagens Cronometradas` |
| `preco` | número (BRL) | inteiro em reais, sem símbolo; deriva de WTP, nunca de custo | pricing-wtp-strategist | `497` |
| `valor_ancorado` | número (BRL) | soma defensável do value stack (âncora alta) | unit-economics-stack-analyst | `3800` |
| `garantia_tipo` | enum (slug) | um dos 13 tipos de [`guarantee-types`](../../lib/taxonomies/guarantee-types.md), em slug | unit-economics-stack-analyst | `dobro-do-dinheiro` |
| `upsell_de` | ref (offer_id) | `offer_id` da oferta que esta sobe (vazio se não for upsell) | money-model-designer | `CORE-01` |
| `downsell_de` | ref (offer_id) | `offer_id` da oferta cujo "não" esta recupera (vazio se não) | money-model-designer | `CORE-01` |
| `proximo_passo` | string (slug) | a ação seguinte na escada (slug verbo-objeto) | funnel-architect | `oferecer-upsell-no-pico` |
| `gatilho_oferta` | string (slug) | o evento que dispara esta oferta no funil | funnel-architect | `conclusao-do-diagnostico` |
| `cta` | string | a chamada para ação, na voz do avatar ([`cta-block`](../../lib/components/cta-block.md)) | vsl-webinar-scriptwriter | `"Quero o Motor 72h"` |
| `objecao_alvo` | string (slug) | a objeção dominante que esta oferta vence ([`objection-registry`](../../data/registries/objection-registry.md)) | avatar-voc-investigator | `ja-tentei-de-tudo` |
| `prova_chave` | ref | id no [`proof-registry`](../../data/registries/proof-registry.md) (`proof-registry#PR-NNN`) | proof-credibility-curator | `proof-registry#PR-031` |
| `status` | enum | `draft` `review` `stable` `deprecated` | money-model-designer | `stable` |

## O Template
O artefato é o CSV. O bloco abaixo mostra o header e uma linha exemplo por papel (atração → núcleo → upsell). Mantenha o header idêntico ao do [`products-and-offers-template.csv`](products-and-offers-template.csv).

```csv
offer_id,nome_oferta,papel_money_model,tipo_oferta,publico_alvo,resultado_prometido,mecanismo_unico,preco,valor_ancorado,garantia_tipo,upsell_de,downsell_de,proximo_passo,gatilho_oferta,cta,objecao_alvo,prova_chave,status
{{ID}},{{NOME}},{{PAPEL}},{{TIPO}},"{{PUBLICO}}",{{RESULTADO}},{{MECANISMO}},{{PRECO}},{{VALOR_ANCORADO}},{{GARANTIA_SLUG}},{{UPSELL_DE}},{{DOWNSELL_DE}},{{PROXIMO_PASSO}},{{GATILHO}},"{{CTA}}",{{OBJECAO_SLUG}},{{PROVA_REF}},{{STATUS}}
```

## Exemplo preenchido
Escada de amostra (Motor de Recuperação 72h), três papéis preenchidos:

```csv
offer_id,nome_oferta,papel_money_model,tipo_oferta,publico_alvo,resultado_prometido,mecanismo_unico,preco,valor_ancorado,garantia_tipo,upsell_de,downsell_de,proximo_passo,gatilho_oferta,cta,objecao_alvo,prova_chave,status
ATR-01,Diagnóstico Lucro em 7 Dias,atracao,tripwire,"donos de e-commerce que faturam R$50 mil/mês",mapa de onde o lucro vaza,Auditoria das 3 Fugas,27,197,reembolso-sem-perguntas,,,oferecer-core-no-checkout,clique-no-anuncio,"Quero meu diagnóstico por R$27",é-caro-demais,proof-registry#PR-014,stable
CORE-01,Motor de Recuperação 72h,core,grand-slam-offer,"quem comprou o diagnóstico",+18% de receita recuperada em 30 dias,Sequência de 7 Mensagens Cronometradas,497,3800,dobro-do-dinheiro,,,oferecer-upsell-no-pico,conclusao-do-diagnostico,"Quero o Motor 72h",ja-tentei-de-tudo,proof-registry#PR-031,stable
UP-01,Implementação Feita-para-Você,upsell,done-for-you,"quem comprou o core",sequência instalada e rodando em 48h,Time de Implantação Dedicado,1497,4000,garantia-de-servico,CORE-01,,oferecer-continuidade-pos-resultado,clique-no-upsell,"Sim, instalem para mim",nao-tenho-tempo,proof-registry#PR-022,stable
```

Leitura: três papéis distintos, a atração (R$27) liquida o CAC, cada linha tem mecanismo nomeado, garantia da taxonomia, objeção-alvo e prova rastreável. `upsell_de = CORE-01` amarra o upsell ao núcleo.

## DoD do entregável
A planilha está pronta quando: (1) o header do CSV é **idêntico** ao schema, em `snake_case`, sem coluna renomeada ou reordenada; (2) cada `offer_id` é único e segue `PREFIXO-NN`; (3) há ≥2 valores distintos em `papel_money_model` (alvo: 4 papéis), satisfazendo o `money-model-four-parts-gate`; (4) ≥1 linha `atracao` existe e o `unit-economics-stack-analyst` confirma que ela **liquida o CAC** (`money-model-cac-liquidation`); (5) `preco` deriva de um método de WTP, nunca de custo, e `valor_ancorado > preco` em toda oferta núcleo/upsell; (6) `garantia_tipo` cita um dos 13 [tipos](../../lib/taxonomies/guarantee-types.md); (7) `prova_chave` resolve para um id real do [`proof-registry`](../../data/registries/proof-registry.md) e nenhum claim grande fica órfão; (8) `upsell_de`/`downsell_de` referenciam `offer_id` existentes; (9) o CSV está limpo (sem comentário, sem frontmatter) e cada linha de oferta também vira um registro no [`offer-registry`](../../data/registries/offer-registry.md).
