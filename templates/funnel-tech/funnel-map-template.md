---
id: template.funnel-tech.funnel-map
title: "Mapa de Funil — O Diagrama de Páginas, Passos e Caminhos da Oferta"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
consumes: [template.core.offer-book-master, template.offer.money-model-template, template.offer.products-and-offers]
produces: [template.funnel-tech.page-specs, template.funnel-tech.links-urls]
frameworks: [offer-to-funnel-mapping, money-model-sequence, launch/cart-open-close]
checklists: [funnel/funnel-no-dead-end-gate, funnel/funnel-backend-gate]
registries: [decision-registry]
tags: [template, funnel, mapa, paginas, fluxo, funnel-tech]
---

# Mapa de Funil — O Diagrama de Páginas, Passos e Caminhos da Oferta

Este template transforma a **espinha do Money Model** num **mapa de páginas navegável**. Ele responde uma pergunta só: por onde o lead anda, da primeira porta até a continuidade, e o que acontece em cada bifurcação. Cada passo do Money Model (atração → núcleo → upsell → downsell → continuidade) vira uma página com um destino claro. Nenhuma página termina em beco. É o primeiro artefato do D5 e alimenta o `page-specs` e o `links-urls`.

## Como usar
- **Agente dono:** `funnel-architect`. Roda na task `map-funnel`, logo depois que o Offer Book cruza o HARD STOP.
- **Inputs:** o [`offer-book-master`](../core/offer-book-master.md) (a oferta e a espinha), o [`money-model-template`](../offer/money-model-template.md) (a sequência) e o [`products-and-offers`](../offer/products-and-offers-template.csv) (os papéis de cada oferta). Use o [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) para mapear cada oferta a uma página.
- **Quando:** abre no início do D5 e fecha quando os dois gates de funil ficam verdes. Cada página recebe um destino de **sim** e um de **não**, sem exceção.
- **Saída:** este mapa vira a entrada do [`page-specs`](page-specs-template.md) (o que cada página precisa ter) e do [`links-urls`](links-urls-template.md) (a URL e o UTM de cada CTA). Preencha o diagrama, a tabela de passos e os caminhos. Campo vazio = beco não resolvido = [`funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) vermelho.

## Campos & Instruções
- **{{NOME_DO_FUNIL}}** — o nome de trabalho do funil, ligado à oferta núcleo. Vem do `offer-book-master`.
- **{{TIPO_DE_FUNIL}}** — o arquétipo: VSL, webinar, carta de vendas, challenge, aplicação. Define a ordem das páginas.
- **{{OBJETIVO_PRIMARIO}}** — a conversão que o funil otimiza, em uma frase (ex.: "vender o núcleo a R$497").
- **{{FONTE_DE_TRAFEGO}}** — de onde o lead chega (ads, e-mail, afiliado, orgânico). Determina a primeira página.
- **{{PAGINA_*}}** — o nome de cada página do fluxo (captura, VSL, checkout, upsell, downsell, obrigado). Uma linha por página na tabela.
- **{{OFERTA_NA_PAGINA}}** — qual oferta do Money Model vive naquela página. Liga ao [`products-and-offers`](../offer/products-and-offers-template.csv) pelo `offer_id`.
- **{{ACAO_PRIMARIA}}** — o único clique que a página pede (o CTA). Uma página, uma ação.
- **{{DESTINO_SIM}}** / **{{DESTINO_NAO}}** — para onde vai quem aceita e para onde vai quem recusa. **Nenhum dos dois pode ser vazio** — recusa vira downsell ou retorno, nunca beco.
- **{{BACKEND_APOS_COMPRA}}** — o que segue depois da compra (upsell, continuidade, nutrição). Sem backend, o funil sangra LTV — [`funnel-backend-gate`](../../checklists/funnel/funnel-backend-gate.md).
- **{{GATILHO_CART_OPEN}}** / **{{GATILHO_CART_CLOSE}}** — quando o carrinho abre e fecha, se o funil é de lançamento. Vem do [`cart-open-close`](../../frameworks/launch/cart-open-close.md).
- **{{STATUS_GATES}}** — verde/vermelho dos dois gates de funil, com data.

## O Template
```
# MAPA DE FUNIL — {{NOME_DO_FUNIL}}
Tipo: {{TIPO_DE_FUNIL}} · Owner: funnel-architect · Data: {{DATA}}
Objetivo primário: {{OBJETIVO_PRIMARIO}}
Fonte de tráfego: {{FONTE_DE_TRAFEGO}}

## 1. DIAGRAMA DO FLUXO (ASCII)
[Tráfego: {{FONTE_DE_TRAFEGO}}]
        │
        ▼
[{{PAGINA_CAPTURA}}] ──não──> [{{SAIDA_OU_RETARGETING}}]
        │ sim (opt-in)
        ▼
[{{PAGINA_VSL_OU_VENDAS}}] ──não──> [{{DOWNSELL_OU_NUTRICAO}}]
        │ sim (clicou no CTA)
        ▼
[{{PAGINA_CHECKOUT}}] ──não──> [{{ABANDONO_RECOVERY}}]
        │ sim (comprou)
        ▼
[{{PAGINA_UPSELL}}] ──não──> [{{PAGINA_DOWNSELL}}]
        │ sim/não (qualquer caminho)
        ▼
[{{PAGINA_OBRIGADO}}] ──> [{{BACKEND_APOS_COMPRA}}]

## 2. TABELA DE PÁGINAS
| # | Página | Oferta (offer_id) | Ação primária (CTA) | Destino SIM | Destino NÃO |
|---|--------|-------------------|---------------------|-------------|-------------|
| 1 | {{PAGINA_1}} | {{OFERTA_1}} | {{CTA_1}} | {{SIM_1}} | {{NAO_1}} |
| 2 | {{PAGINA_2}} | {{OFERTA_2}} | {{CTA_2}} | {{SIM_2}} | {{NAO_2}} |
| 3 | {{PAGINA_3}} | {{OFERTA_3}} | {{CTA_3}} | {{SIM_3}} | {{NAO_3}} |
| 4 | {{PAGINA_4}} | {{OFERTA_4}} | {{CTA_4}} | {{SIM_4}} | {{NAO_4}} |
| 5 | {{PAGINA_5}} | {{OFERTA_5}} | {{CTA_5}} | {{SIM_5}} | {{NAO_5}} |

## 3. BACKEND & CONTINUIDADE
Após a compra do núcleo: {{BACKEND_APOS_COMPRA}}
Sequência de continuidade: {{CONTINUIDADE}}
Recuperação de carrinho: {{ABANDONO_RECOVERY}}

## 4. JANELA DE CARRINHO (se lançamento)
Abre: {{GATILHO_CART_OPEN}} · Fecha: {{GATILHO_CART_CLOSE}}

## 5. STATUS DOS GATES
funnel-no-dead-end-gate: {{STATUS_NO_DEAD_END}} — em {{DATA_GATE}}
funnel-backend-gate: {{STATUS_BACKEND}} — em {{DATA_GATE}}
Becos abertos: {{LISTA_OU_NENHUM}}
```

## Exemplo preenchido
> **# MAPA DE FUNIL — Motor de Recuperação 72h**
> Tipo: VSL · Owner: funnel-architect · Data: 2026-06-02
> Objetivo primário: **vender o Motor 72h a R$497 com upsell de implantação.**
> Fonte de tráfego: **Meta Ads (frio) + e-mail (lista quente).**
>
> **1. DIAGRAMA** — [Meta Ads] → [Página de Captura] ──não──> [Retargeting 7 dias]; sim → [VSL de Vendas] ──não──> [E-mail de nutrição 3 toques]; sim → [Checkout R$47 diagnóstico] ──não──> [Sequência de abandono 72h]; sim → [Upsell Motor R$497] ──não──> [Downsell parcelado 3x]; qualquer caminho → [Página Obrigado] → [Continuidade: gestão mensal].
> **2. TABELA** — 1. Captura · ATR-01 · "Quero meu diagnóstico" · VSL · Retargeting. 2. VSL · CORE-01 · "Quero o Motor 72h" · Checkout · Nutrição. 3. Checkout · ATR-01 · "Finalizar R$47" · Upsell · Abandono-recovery. 4. Upsell · UP-01 · "Sim, instalem" · Obrigado · Downsell. 5. Obrigado · — · "Acessar área" · Continuidade · —.
> **3. BACKEND** — Após o núcleo: oferta de gestão mensal no D7 por e-mail. Continuidade: otimização recorrente R$197/mês. Recuperação: sequência de 7 mensagens na janela 72h.
> **4. JANELA** — Abre: e-mail #1 da semana de lançamento. Fecha: 5 dias depois, 23h59, por capacidade real de 40 setups.
> **5. STATUS** — funnel-no-dead-end-gate: **VERDE** — 2026-06-02. funnel-backend-gate: **VERDE**. Becos abertos: **nenhum**.

## DoD do entregável
O Mapa de Funil está pronto quando: (1) existe um diagrama ASCII do tráfego à continuidade, sem `{{PLACEHOLDER}}` solto; (2) **toda** página tem destino de **sim** e de **não** preenchidos — zero becos, [`funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) verde; (3) cada página aponta para a oferta certa do Money Model pelo `offer_id` do [`products-and-offers`](../offer/products-and-offers-template.csv); (4) cada página pede **uma** ação primária; (5) existe backend depois da compra do núcleo — upsell, continuidade ou nutrição — [`funnel-backend-gate`](../../checklists/funnel/funnel-backend-gate.md) verde; (6) se é lançamento, a janela de carrinho tem gatilhos reais de abertura e fechamento alinhados ao [`cart-open-close`](../../frameworks/launch/cart-open-close.md). Só então o mapa libera o detalhamento em [`page-specs`](page-specs-template.md) e a malha de URLs em [`links-urls`](links-urls-template.md).
