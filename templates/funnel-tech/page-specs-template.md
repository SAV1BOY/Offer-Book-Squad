---
id: template.funnel-tech.page-specs
title: "Especificações de Página — O Briefing de Cada Página do Funil"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
consumes: [template.funnel-tech.funnel-map, template.core.offer-book-master, template.copy.sales-letter-offer-page]
produces: [template.funnel-tech.links-urls]
frameworks: [offer-to-funnel-mapping, money-model-sequence]
checklists: [funnel/funnel-no-dead-end-gate]
registries: [decision-registry]
tags: [template, funnel, page-specs, briefing, wireframe, funnel-tech]
---

# Especificações de Página — O Briefing de Cada Página do Funil

O [`funnel-map`](funnel-map-template.md) diz **quais** páginas existem e como se ligam. Este template diz **o que vai dentro de cada uma**. É o briefing que o designer, o copywriter e o engenheiro leem para construir a página sem adivinhar nada. Uma ficha por página: a meta, a dobra, os blocos, a prova, o CTA e a regra de aprovação. É o segundo artefato do D5.

## Como usar
- **Agente dono:** `funnel-architect`. Roda dentro da task `map-funnel`, logo após o [`funnel-map`](funnel-map-template.md) ficar verde.
- **Inputs:** o [`funnel-map`](funnel-map-template.md) (a lista de páginas e os caminhos), o [`offer-book-master`](../core/offer-book-master.md) (oferta, prova, garantia, escassez) e a copy de D4 que cabe na página (ex.: a [`sales-letter-offer-page`](../copy/sales-letter-offer-page-template.md)).
- **Quando:** uma ficha por página do mapa. Comece pela página que carrega a conversão primária (VSL ou checkout) e desça.
- **Saída:** cada ficha aponta o CTA e o destino, que viram linha no [`links-urls`](links-urls-template.md). Use número e prova nos blocos; use a voz do avatar no headline. Bloco vazio = página incompleta.

## Campos & Instruções
- **{{NOME_DA_PAGINA}}** — o nome da página, igual ao do [`funnel-map`](funnel-map-template.md) (ex.: "VSL de Vendas").
- **{{PAPEL_NO_FUNIL}}** — o trabalho da página: capturar, vender, fazer upsell, confirmar. Vem do mapa.
- **{{OBJETIVO_DE_CONVERSAO}}** — a única métrica que a página move (ex.: "clique no botão de checkout").
- **{{ESTAGIO_CONSCIENCIA}}** — o nível de consciência (1-5) de quem chega aqui. Vem do `offer-book-master`. Define o tom do headline.
- **{{HEADLINE}}** — a promessa principal acima da dobra, na voz do avatar. Liga à Big Idea.
- **{{ACIMA_DA_DOBRA}}** — o que aparece sem rolar: headline, sub, prova rápida, CTA. O essencial em 5 segundos.
- **{{BLOCO_*}}** — os blocos da página em ordem (problema, mecanismo, oferta, stack, prova, garantia, escassez, FAQ). Liste só os que a página usa.
- **{{PROVA_NA_PAGINA}}** — quais provas entram (depoimento, número, print, selo), com link ao `proof-bank`. Cada claim grande na página precisa de lastro.
- **{{GARANTIA_EXIBIDA}}** — a reversão de risco mostrada, do `offer-book-master`. Usa o [`guarantee-block`](../../lib/components/guarantee-block.md).
- **{{ESCASSEZ_EXIBIDA}}** — o limite real exibido (vagas/prazo). Usa o [`scarcity-block`](../../lib/components/scarcity-block.md). Compliance confirma.
- **{{CTA_TEXTO}}** / **{{CTA_DESTINO}}** — o texto do botão e a página de destino. Vira linha no [`links-urls`](links-urls-template.md).
- **{{ELEMENTOS_TECNICOS}}** — pixel, evento de conversão, timer, vídeo, formulário, integração de checkout.
- **{{CRITERIO_APROVACAO}}** — o que precisa estar certo para a página ir ao ar (mobile, velocidade, link testado).

## O Template
```
# ESPECIFICAÇÃO DE PÁGINA — {{NOME_DA_PAGINA}}
Papel no funil: {{PAPEL_NO_FUNIL}} · Owner: funnel-architect · Data: {{DATA}}
Objetivo de conversão: {{OBJETIVO_DE_CONVERSAO}}
Consciência de quem chega: nível {{ESTAGIO_CONSCIENCIA}}

## 1. ACIMA DA DOBRA
Headline: {{HEADLINE}}
Sub-headline: {{SUBHEADLINE}}
Prova rápida: {{PROVA_RAPIDA}}
CTA principal: {{CTA_TEXTO}} → {{CTA_DESTINO}}

## 2. BLOCOS (em ordem)
1. {{BLOCO_1}} — {{CONTEUDO_1}}
2. {{BLOCO_2}} — {{CONTEUDO_2}}
3. {{BLOCO_3}} — {{CONTEUDO_3}}
4. {{BLOCO_4}} — {{CONTEUDO_4}}
5. {{BLOCO_5}} — {{CONTEUDO_5}}

## 3. PROVA
{{PROVA_NA_PAGINA}} (link: proof-bank#{{ID}})
Claims na página sem lastro: {{LISTA_OU_NENHUM}}

## 4. REVERSÃO DE RISCO & ESCASSEZ
Garantia exibida: {{GARANTIA_EXIBIDA}}
Escassez exibida: {{ESCASSEZ_EXIBIDA}} (compliance OK? {{SIM/NAO}})

## 5. CTA
Texto: {{CTA_TEXTO}} · Destino: {{CTA_DESTINO}} · Cor/posição: {{ESTILO_CTA}}

## 6. ELEMENTOS TÉCNICOS
{{ELEMENTOS_TECNICOS}}

## 7. CRITÉRIO DE APROVAÇÃO
{{CRITERIO_APROVACAO}}
```

## Exemplo preenchido
> **# ESPECIFICAÇÃO DE PÁGINA — VSL de Vendas**
> Papel no funil: vender o diagnóstico de atração · Owner: funnel-architect · Data: 2026-06-02
> Objetivo de conversão: **clique no botão "Quero o Motor 72h".**
> Consciência de quem chega: **nível 3** (compara apps vs agências).
>
> **1. ACIMA DA DOBRA** — Headline: *"A janela de 72 horas que devolve o lucro que seu checkout esconde."* Sub: "Sem mais tráfego. Sem trocar de plataforma." Prova rápida: "142 lojas, mediana +21% de receita recuperada." CTA: **"Quero o Motor 72h" → /checkout-72h**.
> **2. BLOCOS** — 1. Problema — o carrinho que engole vendas. 2. Mecanismo — a Janela 72h. 3. Oferta — o Motor de 7 mensagens. 4. Stack + valor — itens e ancoragem R$3.800. 5. Prova + garantia — 142 casos + Dobro ou Nada.
> **3. PROVA** — 3 depoimentos em vídeo + gráfico de receita (proof-bank#PR-031). Claims sem lastro: **nenhum**.
> **4. REVERSÃO & ESCASSEZ** — Garantia: Dobro ou Nada em 60 dias. Escassez: 40 vagas/turma por capacidade real de setup (compliance OK: sim).
> **5. CTA** — "Quero o Motor 72h" → /checkout-72h · botão laranja, repetido 3x (após dobra, após prova, após garantia).
> **6. TÉCNICOS** — pixel Meta, evento ViewContent, player Wistia autoplay, botão revela após 8 min.
> **7. APROVAÇÃO** — mobile OK, carrega <2,5s, link do CTA testado em 2 dispositivos, vídeo sem corte.

## DoD do entregável
A Especificação de Página está pronta quando: (1) existe **uma ficha por página** do [`funnel-map`](funnel-map-template.md), sem `{{PLACEHOLDER}}` solto; (2) cada ficha define a conversão única, o headline na voz do avatar e o conteúdo acima da dobra; (3) os blocos estão em ordem e nenhum claim grande na página fica órfão de prova; (4) garantia e escassez exibidas vêm do [`offer-book-master`](../core/offer-book-master.md) e a escassez é confirmada real pelo `compliance-auditor`; (5) o CTA tem texto e destino definidos, prontos para virar linha no [`links-urls`](links-urls-template.md); (6) os elementos técnicos (pixel, evento, timer) e o critério de aprovação (mobile, velocidade, link testado) estão listados. Páginas com destino coerente com o mapa mantêm o [`funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) verde e liberam a malha de URLs.
