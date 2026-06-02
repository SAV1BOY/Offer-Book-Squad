---
id: template.strategy.pricing-wtp
title: "Pricing & WTP Sheet — Preço Derivado de Valor e Disposição a Pagar"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
consumes: [template.strategy.value-equation, template.strategy.mechanism-sheet, template.strategy.market-brief, template.strategy.unit-economics]
produces: [template.core.offer-book-master, template.offer.money-model]
frameworks: [pricing.value-based-pricing, pricing.van-westendorp, pricing.gabor-granger, pricing.packaging-good-better-best, pricing.decoy-effect, value-equation]
checklists: [pricing/pricing-method-declared-gate, pricing/pricing-value-derived-gate, pricing/pricing-anchor-gate, pricing/pricing-packaging-gate]
registries: [price-test-registry, decision-registry]
tags: [template, pricing, wtp, value-based, van-westendorp, packaging, strategy]
---

# Pricing & WTP Sheet — Preço Derivado de Valor e Disposição a Pagar

Esta planilha fixa o preço pela regra-mestre do squad: **preço deriva de valor, nunca de custo**. O custo é só o piso de margem; o teto é o valor econômico que a oferta cria para o cliente. Você combina o valor econômico ([`value-based-pricing`](../../frameworks/pricing/value-based-pricing.md)) com a faixa de disposição a pagar medida ([`van-westendorp`](../../frameworks/pricing/van-westendorp.md), [`gabor-granger`](../../frameworks/pricing/gabor-granger.md)) e fecha num número defensável, com o método declarado. É o documento que o `pricing-wtp-strategist` usa para travar preço antes do Money Model. Sem método declarado e sem lastro de valor, o preço é palpite — e palpite não passa nos gates.

## Como usar
- **Agente dono:** `pricing-wtp-strategist` (camada D2). Validado pelo `unit-economics-stack-analyst` (margem/payback) e pelo `value-equation-engineer` (as alavancas são os diferenciadores que entram no valor econômico).
- **Task:** `set-pricing-wtp`. Consome o [`value-equation`](value-equation-template.md), o [`mechanism-sheet`](mechanism-sheet-template.md), o [`market-brief`](market-brief-template.md) e o [`unit-economics`](unit-economics-template.md).
- **Quando:** depois do valor, antes do Money Model. Alimenta o bloco de preço do [`offer-book-master`](../core/offer-book-master.md) e os preços da escada em [`money-model`](../offer/money-model-template.md). Validado pelos gates de pricing.
- Regra: declare o **método** de WTP (que ferramenta, que amostra) — nada de número solto. Cada preço cita a alternativa de referência. Cruze sempre com o piso de custo do `unit-economics`. Campo `{{...}}` vazio = preço incompleto = gate vermelho.

## Campos & Instruções
- **{{ALTERNATIVA_REFERENCIA}}** — a melhor alternativa real do cliente (concorrente, status quo, planilha, "não fazer nada") e quanto ela custa. É a âncora do valor de referência. Via [`value-based-pricing`](../../frameworks/pricing/value-based-pricing.md).
- **{{VALOR_DIFERENCIACAO}}** — o que você entrega a mais que a alternativa, **monetizado** (horas poupadas × custo da hora, receita extra, risco evitado). Cada número precisa de lastro (dado, benchmark, depoimento).
- **{{EVA}}** — Valor Econômico Total = referência + diferenciação líquida. É o **teto** lógico do preço.
- **{{METODO_WTP}}** — qual ferramenta mediu a disposição a pagar (Van Westendorp PSM, Gabor-Granger, conjoint) e a amostra (tamanho, segmento). É o gate `pricing-method-declared-gate`.
- **{{FAIXA_WTP}}** — a faixa aceitável medida (PMC → PME no Van Westendorp) com OPP e IPP marcados, por segmento.
- **{{FATIA_CAPTURA}}** — quanto do EVA você captura no preço (nunca 100% — deixe excedente para o cliente trocar).
- **{{PRECO_ANCORA}}** — o valor total somado/âncora mostrado antes do preço real (gate `pricing-anchor-gate`).
- **{{PRECO_FINAL}}** — o número fechado, entre o piso de custo e o teto do EVA, dentro da faixa de WTP.
- **{{PACOTES}}** — se há segmentos com WTP distinta, os pacotes good-better-best ([`packaging-good-better-best`](../../frameworks/pricing/packaging-good-better-best.md)). Gate `pricing-packaging-gate`.
- **{{PISO_CUSTO}}** — o custo incremental (só para confirmar margem; não é base de preço).
- **{{CASO_DE_VALOR}}** — a conta que a copy mostra ao cliente ("R$X para destravar R$Y").

## O Template
```
# PRICING & WTP SHEET — {{NOME_DA_OFERTA}}
Owner: pricing-wtp-strategist · Data: {{DATA}}
Regra: preço deriva de VALOR (custo = só piso de margem)

## 1. VALOR ECONÔMICO (o teto)
Alternativa de referência: {{ALTERNATIVA_REFERENCIA}} (custa R$ {{CUSTO_ALTERNATIVA}})
Valor de diferenciação (monetizado): {{VALOR_DIFERENCIACAO}}
EVA (Valor Econômico Total): R$ {{EVA}}

## 2. DISPOSIÇÃO A PAGAR (medida)
Método declarado: {{METODO_WTP}}  (amostra: {{AMOSTRA}})
Faixa aceitável (PMC→PME): R$ {{FAIXA_WTP}}  · OPP: R$ {{OPP}} · IPP: R$ {{IPP}}

## 3. PISO DE CUSTO (margem)
Custo incremental: R$ {{PISO_CUSTO}}  → margem no preço final: {{MARGEM}}

## 4. DECISÃO DE PREÇO
Fatia de captura do EVA: {{FATIA_CAPTURA}}
Âncora exibida (valor total): R$ {{PRECO_ANCORA}}
PREÇO FINAL: R$ {{PRECO_FINAL}}  (entre piso de custo e teto de EVA, dentro da faixa de WTP)

## 5. EMPACOTAMENTO (se há segmentos)
{{PACOTES}}  (good-better-best por WTP)

## 6. CASO DE VALOR (para a copy)
{{CASO_DE_VALOR}}

## 7. GATES
Método declarado (pricing-method-declared-gate): {{STATUS_METODO}}
Preço derivado de valor (pricing-value-derived-gate): {{STATUS_VALOR}}
Âncora presente (pricing-anchor-gate): {{STATUS_ANCORA}}
```

## Exemplo preenchido
> **# PRICING & WTP SHEET — Motor de Recuperação 72h**
> Owner: pricing-wtp-strategist · Data: 2026-06-02
>
> **1. VALOR ECONÔMICO** — Alternativa de referência: contratar um especialista de CRO (custa R$3.000/mês) ou não fazer nada (perde ~R$9.000/mês em carrinhos abandonados). Diferenciação monetizada: recupera +18% da receita perdida = ~R$1.620/mês para uma loja de R$50 mil/mês. EVA no primeiro ano: ~R$19.440.
> **2. DISPOSIÇÃO A PAGAR** — Método: Van Westendorp PSM, 160 respostas do ICP "dono de e-commerce R$30-80 mil/mês". Faixa aceitável: R$290 → R$1.200. OPP ≈ R$497. IPP ≈ R$690.
> **3. PISO DE CUSTO** — Custo incremental por cliente: ~R$40 (suporte + infra). Margem no preço final: 92%.
> **4. DECISÃO DE PREÇO** — Captura ~3% do ganho do 1º ano. Âncora exibida (valor total dos componentes): R$2.400. **PREÇO FINAL: R$497** (no OPP, dentro da faixa, muito acima do piso).
> **5. EMPACOTAMENTO** — Bom: Motor 72h (R$497). Melhor: Motor + Implementação feita-para-você (R$1.497). Top: Motor + Implementação + Otimização recorrente (R$197/mês). Segmento sênior (loja >R$200 mil/mês) tem WTP para o pacote top.
> **6. CASO DE VALOR** — "R$497 para recuperar R$1.620 todo mês. Você paga uma vez e o sistema se paga na primeira semana."
> **7. GATES** — Método declarado: **VERDE** (PSM, n=160). Preço derivado de valor: **VERDE** (EVA documentado). Âncora: **VERDE** (R$2.400 antes de R$497).

## DoD do entregável
A Pricing & WTP Sheet está pronta quando: (1) a alternativa de referência está nomeada com o custo dela; (2) o valor de diferenciação está **monetizado** e cada número tem lastro (sem isso, é veto de compliance); (3) o EVA está calculado e serve de teto lógico; (4) o **método** de WTP está declarado com a amostra (`pricing-method-declared-gate` verde) e a faixa medida aparece com OPP/IPP; (5) o preço final cai entre o piso de custo e o teto do EVA, dentro da faixa de WTP, com a fatia de captura explícita; (6) existe uma âncora de valor exibida antes do preço (`pricing-anchor-gate` verde) e o preço deriva de valor, não de custo (`pricing-value-derived-gate` verde); (7) se há segmentos com WTP distinta, há pacotes good-better-best (`pricing-packaging-gate` verde); (8) o caso de valor está escrito para a copy mostrar a conta ao cliente; (9) o método, o preço e o EVA estão registrados no [`price-test-registry`](../../data/registries/price-test-registry.md) e a decisão no [`decision-registry`](../../data/registries/decision-registry.md). Só então o preço alimenta o [`money-model`](../offer/money-model-template.md) e o [`offer-book-master`](../core/offer-book-master.md).
