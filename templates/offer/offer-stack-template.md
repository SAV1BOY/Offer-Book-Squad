---
id: template.offer.offer-stack
title: "Offer Stack — A Pilha de Valor da Grand Slam Offer"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes: [template.strategy.value-equation, template.strategy.proof-bank, template.offer.guarantee, template.strategy.pricing-wtp]
produces: [template.offer.money-model, template.core.offer-book-master]
frameworks: [offer-stack-builder, value-equation, magic-naming, price-anchoring, guarantee-design]
checklists: [value-equation/value-lever-coverage-gate, money-model/money-model-four-parts-gate]
registries: [offer-registry, proof-registry]
tags: [template, offer-stack, value-stack, grand-slam-offer, anchoring]
---

# Offer Stack — A Pilha de Valor da Grand Slam Offer

O offer stack monta a oferta núcleo como uma **pilha**: cada item recebe nome magnético, resolve uma dor nomeada, ganha valor defensável, e a soma vira a âncora alta contra a qual o preço real parece pequeno. É a saída direta do [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) e o coração da Grand Slam Offer. Regra de ouro: **todo item move ≥1 alavanca da [Value Equation](../../frameworks/value-equation.md)** — item que não move alavanca dilui a oferta e é reprovado pelo `value-equation-engineer`.

## Como usar
- **Agente dono:** `money-model-designer`, com o `unit-economics-stack-analyst` (valor ancorado e lastro) e o `value-equation-engineer` (cada item move alavanca).
- **Task:** `build-offer-stack`. Roda depois da Value Equation e antes do preço final; alimenta a planilha [`products-and-offers`](products-and-offers-template.csv) (coluna `valor_ancorado`) e o [`money-model`](money-model-template.md).
- **Quando:** D2. Monte a pilha da oferta núcleo (e de cada upsell, se houver). Use os componentes reutilizáveis: [`offer-block`](../../lib/components/offer-block.md), [`value-stack-block`](../../lib/components/value-stack-block.md), [`bonus-block`](../../lib/components/bonus-block.md), [`guarantee-block`](../../lib/components/guarantee-block.md).
- Cada valor ancorado precisa de uma **justificativa** (preço de mercado do item, custo de fazer sozinho, ou custo de não resolver). Valor inflado e falso é risco de compliance e quebra a confiança. Anote o lastro de cada linha.

## Campos & Instruções
- **{{NOME_OFERTA}}** — o nome da oferta núcleo ([`magic-naming`](../../frameworks/magic-naming.md)).
- **{{RESULTADO_DOS_SONHOS}}** — o destino que a oferta entrega, na voz do avatar.
- **{{ITEM_NUCLEO}}** / **{{VALOR_NUCLEO}}** — o componente principal e seu valor ancorado.
- **{{BONUS_N}}** / **{{VALOR_BONUS_N}}** — cada bônus com seu papel (acelera / remove obstáculo / vence objeção — ver [`bonus-block`](../../lib/components/bonus-block.md)) e valor.
- **{{ALAVANCA_DO_ITEM}}** — qual das 4 alavancas cada item move (Resultado dos Sonhos ↑, Probabilidade ↑, Tempo ↓, Esforço ↓). Nenhum item órfão.
- **{{GARANTIA}}** — a reversão de risco ([`guarantee`](guarantee-template.md)), listada sem preço.
- **{{VALOR_TOTAL}}** — a soma de todos os itens (a âncora).
- **{{PRECO_REAL}}** — o preço de fato (deriva de WTP, muito abaixo do total).
- **{{ECONOMIA}}** / **{{PCT_ECONOMIA}}** — quanto e que % o cliente "economiza" (total − preço).
- **{{LASTRO_VALOR}}** — a justificativa do valor de cada item (para o `compliance-auditor`).

## O Template
```
# OFFER STACK — {{NOME_OFERTA}}
Resultado dos sonhos: {{RESULTADO_DOS_SONHOS}}

## A PILHA (item → resolve → alavanca → valor)
1. {{ITEM_NUCLEO}} — resolve {{DOR_NUCLEO}} — alavanca: {{ALAVANCA_NUCLEO}} ... R$ {{VALOR_NUCLEO}}
2. Bônus: {{BONUS_1}} — resolve {{DOR_1}} — alavanca: {{ALAVANCA_1}} ........ R$ {{VALOR_BONUS_1}}
3. Bônus: {{BONUS_2}} — resolve {{DOR_2}} — alavanca: {{ALAVANCA_2}} ........ R$ {{VALOR_BONUS_2}}
4. Ferramenta: {{FERRAMENTA}} — resolve {{DOR_3}} — alavanca: {{ALAVANCA_3}} . R$ {{VALOR_3}}
5. Garantia: {{GARANTIA}} — remove o risco ........................ (sem preço)
-----------------------------------------------------------------
VALOR TOTAL ..................................................... R$ {{VALOR_TOTAL}}
HOJE VOCÊ INVESTE .............................................. R$ {{PRECO_REAL}}
VOCÊ ECONOMIZA ................................................. R$ {{ECONOMIA}} ({{PCT_ECONOMIA}})

## LASTRO DO VALOR (por linha — para compliance)
{{LASTRO_VALOR}}

## COBERTURA DE ALAVANCAS (Value Equation)
Resultado ↑: {{ITENS}} · Probabilidade ↑: {{ITENS}} · Tempo ↓: {{ITENS}} · Esforço ↓: {{ITENS}}
Itens órfãos de alavanca: {{NENHUM_OU_LISTA}}
```

## Exemplo preenchido
> **# OFFER STACK — Motor de Recuperação 72h**
> Resultado dos sonhos: recuperar a receita que escapa no carrinho, sem gastar mais em tráfego.
>
> **A PILHA**
> 1. Método Motor 72h — resolve "o dinheiro escapa no carrinho" — alavanca: Resultado ↑ ... R$ 2.000
> 2. Bônus: Planilha de Recuperação Automática — resolve "não sei configurar" — Esforço ↓ ... R$ 600
> 3. Bônus: 10 Modelos de E-mail Prontos — resolve "não sei o que escrever" — Tempo ↓ ... R$ 400
> 4. Ferramenta: Aula de Tráfego que Liquida o CAC — resolve "tráfego é caro" — Probabilidade ↑ ... R$ 800
> 5. Garantia: Dobro ou Nada em 60 dias — remove o risco ... (sem preço)
> **VALOR TOTAL: R$ 3.800 — HOJE: R$ 497 — VOCÊ ECONOMIZA R$ 3.303 (87%)**
>
> **LASTRO DO VALOR** — Método: equivale a uma consultoria de R$2.000. Planilha: substitui 8h de setup a R$75/h. Modelos: 10 e-mails a R$40 cada no mercado. Aula: preço avulso do módulo de tráfego.
> **COBERTURA DE ALAVANCAS** — Resultado ↑: método. Probabilidade ↑: aula + garantia. Tempo ↓: modelos. Esforço ↓: planilha. Itens órfãos: **nenhum**.

Cada item tem nome próprio, resolve uma dor nomeada, move uma alavanca e tem valor com lastro. A soma de R$3.800 torna R$497 quase trivial.

## DoD do entregável
A pilha está pronta quando: (1) cada item tem nome magnético, a dor que resolve e o valor ancorado; (2) **nenhum item é órfão de alavanca** — todo item move Resultado, Probabilidade, Tempo ou Esforço (`value-lever-coverage-gate` verde); (3) cada valor ancorado tem justificativa de lastro registrada (o `compliance-auditor` pode pedir); (4) o valor total é a soma real dos itens e é maior que o preço; (5) o preço real deriva de um método de WTP, não de custo, e a economia (total − preço) está calculada; (6) a garantia da [`guarantee`](guarantee-template.md) entra na pilha sem preço; (7) o valor total preenche a coluna `valor_ancorado` da planilha [`products-and-offers`](products-and-offers-template.csv) e cada bônus mapeia uma objeção real; (8) nenhum `{{PLACEHOLDER}}` solto. A pilha alimenta o [`money-model`](money-model-template.md) e o [`offer-book-master`](../core/offer-book-master.md).
