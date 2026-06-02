---
id: template.ops.sales-flow
title: "Sales Flow — Schema do Fluxo de Venda (Etapa, Gatilho, Oferta, CTA, Redirecionamento)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
consumes: [template.offer.products-and-offers, template.core.offer-book-master]
produces: [data.registry.decision]
frameworks: [offer-to-funnel-mapping, money-model-sequence, launch/cart-open-close]
checklists: [run-of-show-checklist, launch/launch-objective-gate]
registries: [offer-registry, decision-registry]
tags: [template, csv-schema, sales-flow, funil, etapas, ops, lancamento]
---

# Sales Flow — Schema do Fluxo de Venda

Este `.md` documenta o schema de [`sales-flow-template.csv`](sales-flow-template.csv), o **fluxo de venda** do lançamento: a sequência de etapas que leva o lead da captura ao pico de upsell. Uma linha por etapa. Cada etapa amarra um gatilho, a oferta apresentada, a chamada para ação e para onde o comprador vai depois. O CSV é a fonte de verdade do caminho de conversão; este documento explica cada coluna. O `launch-producer` é dono dos dois arquivos, em par com o `funnel-architect`.

## Como usar
- **Agente dono:** `launch-producer`. Co-lido pelo `funnel-architect` (que constrói as páginas e os redirecionamentos) e amarrado à planilha-mãe [`products-and-offers`](../offer/products-and-offers-template.csv) (cada `oferta` aqui é um `offer_id` de lá).
- **Task:** preenchido na produção do lançamento, depois que o Money Model existe. Lido pela copy de D4 (qual CTA usar em cada etapa) e pelo tech (quais redirecionamentos configurar).
- **Quando:** depois que a escada de ofertas está travada. Aplica o [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) para mapear cada oferta a uma etapa do funil e o [`money-model-sequence`](../../frameworks/money-model-sequence.md) para a ordem da escada.
- **Como editar o CSV:** abra em editor de texto ou planilha. A primeira linha é o header `snake_case` — **não traduza nem reordene as colunas**. Adicione uma linha por etapa, em ordem de fluxo. Campos com vírgula vão entre aspas (`"..."`). Não ponha comentário no CSV — a documentação vive aqui.
- O gate [`launch-objective-gate`](../../checklists/launch/launch-objective-gate.md) confere que o fluxo termina num objetivo de venda claro. Cada `oferta` deve resolver para um `offer_id` real do [`offer-registry`](../../data/registries/offer-registry.md).

## Schema
Uma linha por coluna do CSV: nome, tipo, valores aceitos, agente-fonte e exemplo.

| Coluna | Tipo | Valores aceitos | Agente-fonte | Exemplo |
|---|---|---|---|---|
| `etapa` | string (slug) | o passo do fluxo (captura-de-lead, checkout-com-upsell, upsell-no-pico, downsell, pagina-de-obrigado) | launch-producer | `checkout-com-upsell` |
| `gatilho` | string (slug) | o evento que dispara a etapa ([`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md)) | funnel-architect | `conclusao-do-diagnostico` |
| `oferta` | ref (offer_id) | o `offer_id` apresentado na etapa, da planilha [`products-and-offers`](../offer/products-and-offers-template.csv) | money-model-designer | `CORE-01` |
| `cta` | string | a chamada para ação da etapa, na voz do avatar | vsl-webinar-scriptwriter | `"Quero o Motor 72h"` |
| `redirecionamento` | string (slug) | para onde o comprador vai após a ação (página ou próxima etapa) | funnel-architect | `oferta-de-upsell-no-pico` |

## Exemplo
Fluxo de amostra (Motor 72h), três etapas preenchidas:

```csv
etapa,gatilho,oferta,cta,redirecionamento
captura-de-lead,clique-no-anuncio,ATR-01,"Quero meu diagnostico por R$27",pagina-de-checkout
checkout-com-upsell,conclusao-do-diagnostico,CORE-01,"Quero o Motor 72h",oferta-de-upsell-no-pico
upsell-no-pico,clique-no-upsell,UP-01,"Sim, instalem para mim",pagina-de-obrigado
```

Leitura: o fluxo sobe a escada (atração → núcleo → upsell). Cada etapa tem um gatilho, uma oferta rastreável (`ATR-01`, `CORE-01`, `UP-01`), um CTA na voz do avatar e um redirecionamento para a etapa seguinte. O upsell entra no pico de intenção, logo após o "sim" do núcleo.

## DoD
O fluxo está pronto quando: (1) o header do CSV é **idêntico** ao schema, em `snake_case`, sem coluna renomeada ou reordenada; (2) as etapas formam um caminho contínuo, da captura ao objetivo final, sem buraco; (3) cada `oferta` resolve para um `offer_id` existente na planilha [`products-and-offers`](../offer/products-and-offers-template.csv) e no [`offer-registry`](../../data/registries/offer-registry.md); (4) cada etapa tem um `gatilho` e um `redirecionamento` claros, mapeados pelo [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md); (5) cada `cta` está em voz ativa e presente, sem `{{placeholder}}` solto; (6) o fluxo termina num objetivo de venda declarado, satisfazendo o [`launch-objective-gate`](../../checklists/launch/launch-objective-gate.md); (7) nenhuma etapa promete o que a oferta não entrega e nenhuma escassez é falsa (`truthful_scarcity`, [política de compliance](../../docs/compliance-policy.md)); (8) o CSV está limpo (sem comentário, sem frontmatter) e passa no [`run-of-show-checklist`](../../checklists/run-of-show-checklist.md). A versão final vira decisão no [`decision-registry`](../../data/registries/decision-registry.md).
