---
id: template.funnel-tech.links-urls
title: "Links & URLs — A Malha de Vanity URLs e UTMs por CTA do Funil"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: tech-links-deliverability-engineer
consumes: [template.funnel-tech.funnel-map, template.funnel-tech.page-specs, template.core.offer-book-master]
produces: [template.funnel-tech.tech-deliverability-plan]
frameworks: [offer-to-funnel-mapping, launch/cart-open-close]
checklists: [funnel/funnel-no-dead-end-gate, tech/tech-links-utm-gate]
registries: [decision-registry]
tags: [template, links, urls, vanity, utm, tracking, funnel-tech]
---

# Links & URLs — A Malha de Vanity URLs e UTMs por CTA do Funil

O [`funnel-map`](funnel-map-template.md) diz por onde o lead anda. O [`page-specs`](page-specs-template.md) diz o que cada página pede. Este template fecha o D5 do lado técnico: **toda página vira uma vanity URL** e **todo CTA vira um link rastreável com UTM**. É a planilha que o engenheiro usa para registrar domínios, redirecionamentos e parâmetros — sem ela, o lançamento perde a leitura de origem e quebra atribuição. Um link, um destino, um conjunto de UTMs. Nenhum CTA fica sem URL final testada.

## Como usar
- **Agente dono:** `tech-links-deliverability-engineer`. Roda na task `plan-tech-deliverability`, logo depois que o [`funnel-map`](funnel-map-template.md) e o [`page-specs`](page-specs-template.md) ficam verdes.
- **Inputs:** o [`funnel-map`](funnel-map-template.md) (a lista de páginas e os caminhos sim/não), o [`page-specs`](page-specs-template.md) (o texto e o destino de cada CTA) e o [`offer-book-master`](../core/offer-book-master.md) (o nome da oferta e da Big Idea, que dão o slug da vanity URL). O cruzamento oferta→página vem do [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md).
- **Quando:** abre quando o mapa de páginas está estável e fecha quando cada CTA tem link final, UTM e teste de clique. É a entrada direta do [`tech-deliverability-plan`](tech-deliverability-plan-template.md) (que cuida de envio, domínio e fallback).
- **Saída:** preencha as três tabelas (vanity URLs, UTM por CTA, redirecionamentos) e o painel de status. Link quebrado ou destino vazio = beco técnico = [`funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) e [`tech-links-utm-gate`](../../checklists/tech/tech-links-utm-gate.md) vermelhos.

## Campos & Instruções
- **{{DOMINIO_RAIZ}}** — o domínio (ou subdomínio) que hospeda o funil (ex.: `go.minhamarca.com`). Define o prefixo de toda vanity URL.
- **{{ENCURTADOR}}** — o serviço de vanity/short link usado (ex.: Bitly, domínio próprio). Define quem gera e mede o clique.
- **{{PAGINA}}** — o nome da página, idêntico ao do [`funnel-map`](funnel-map-template.md) (captura, VSL, checkout, upsell, obrigado).
- **{{VANITY_URL}}** — a URL curta e legível da página (ex.: `go.minhamarca.com/motor72h`). Curta, sem parâmetro, fácil de ditar. Liga a oferta à página.
- **{{URL_DESTINO_REAL}}** — a URL técnica final para onde a vanity aponta (a página real no construtor/checkout). Nunca vazia.
- **{{CTA_TEXTO}}** — o texto exato do botão, vindo do [`page-specs`](page-specs-template.md) (ex.: "Quero o Motor 72h"). Um CTA, uma linha.
- **{{CTA_PAGINA_ORIGEM}}** / **{{CTA_DESTINO}}** — onde o CTA vive e para onde leva. O destino é a vanity URL da próxima página, nunca um beco.
- **{{UTM_SOURCE}}** — a origem do tráfego daquele clique (ex.: `meta`, `email`, `afiliado`, `organico`). Em `snake_case`/minúsculas, padronizado.
- **{{UTM_MEDIUM}}** — o meio (ex.: `cpc`, `email`, `sms`, `referral`). Vocabulário fixo para não fragmentar relatório.
- **{{UTM_CAMPAIGN}}** — a campanha/lançamento (ex.: `lancamento-motor72h`). Igual em todos os CTAs do mesmo lançamento.
- **{{UTM_CONTENT}}** — o que diferencia o CTA na página (ex.: `botao-pos-dobra`, `botao-pos-garantia`). Distingue cliques da mesma página.
- **{{UTM_TERM}}** — opcional; palavra-chave ou variação de anúncio. Vazio se não usar.
- **{{LINK_FINAL_RASTREAVEL}}** — a URL de destino **com** a query string de UTM montada. É o que entra no botão/anúncio/e-mail.
- **{{REDIRECIONAMENTO}}** — qualquer regra de redirect (ex.: 301 de URL antiga, fechamento de carrinho que manda para lista de espera). Vem do [`cart-open-close`](../../frameworks/launch/cart-open-close.md).
- **{{TESTE_CLIQUE}}** — sim/não: o link foi clicado e abriu o destino certo em desktop e mobile, com o UTM chegando no analytics.

## O Template
```
# LINKS & URLs — {{NOME_DO_FUNIL}}
Domínio raiz: {{DOMINIO_RAIZ}} · Encurtador: {{ENCURTADOR}}
Owner: tech-links-deliverability-engineer · Data: {{DATA}}
Convenção UTM: source/medium/campaign/content em snake_case, minúsculas, sem acento.

## 1. VANITY URLs (uma por página)
| Página | Vanity URL | URL de destino real | Redirecionamento |
|--------|-----------|---------------------|------------------|
| {{PAGINA_1}} | {{VANITY_1}} | {{DESTINO_REAL_1}} | {{REDIRECT_1}} |
| {{PAGINA_2}} | {{VANITY_2}} | {{DESTINO_REAL_2}} | {{REDIRECT_2}} |
| {{PAGINA_3}} | {{VANITY_3}} | {{DESTINO_REAL_3}} | {{REDIRECT_3}} |

## 2. UTM POR CTA (uma linha por CTA do funil)
| CTA (texto) | Página origem | Destino | source | medium | campaign | content | Link final rastreável |
|-------------|---------------|---------|--------|--------|----------|---------|------------------------|
| {{CTA_1}} | {{ORIGEM_1}} | {{DESTINO_1}} | {{SOURCE_1}} | {{MEDIUM_1}} | {{CAMPAIGN}} | {{CONTENT_1}} | {{LINK_FINAL_1}} |
| {{CTA_2}} | {{ORIGEM_2}} | {{DESTINO_2}} | {{SOURCE_2}} | {{MEDIUM_2}} | {{CAMPAIGN}} | {{CONTENT_2}} | {{LINK_FINAL_2}} |
| {{CTA_3}} | {{ORIGEM_3}} | {{DESTINO_3}} | {{SOURCE_3}} | {{MEDIUM_3}} | {{CAMPAIGN}} | {{CONTENT_3}} | {{LINK_FINAL_3}} |

## 3. REDIRECIONAMENTOS & FECHAMENTO DE CARRINHO
Carrinho abre: {{GATILHO_CART_OPEN}} → destino {{DESTINO_ABERTURA}}
Carrinho fecha: {{GATILHO_CART_CLOSE}} → redirect para {{DESTINO_FECHAMENTO}}
Redirects antigos (301): {{LISTA_OU_NENHUM}}

## 4. STATUS DE INTEGRIDADE
Links com teste de clique OK (desktop+mobile): {{N_OK}}/{{N_TOTAL}}
UTM chegando no analytics: {{SIM/NAO}}
CTAs sem link final: {{LISTA_OU_NENHUM}}
funnel-no-dead-end-gate: {{STATUS}} — em {{DATA_GATE}}
tech-links-utm-gate: {{STATUS}} — em {{DATA_GATE}}
```

## Exemplo preenchido
> **# LINKS & URLs — Motor de Recuperação 72h**
> Domínio raiz: **go.minhaloja.com** · Encurtador: **domínio próprio (Bitly Brand)**
> Owner: tech-links-deliverability-engineer · Data: 2026-06-02
>
> **1. VANITY URLs** — Captura → `go.minhaloja.com/diagnostico` → `https://app.builder.io/p/captura-72h` (sem redirect). VSL → `go.minhaloja.com/motor72h` → `https://app.builder.io/p/vsl-72h` (sem redirect). Checkout → `go.minhaloja.com/checkout72h` → `https://pay.checkout.com/c/motor-72h` (sem redirect).
> **2. UTM POR CTA** —
> 1. "Quero meu diagnóstico" · página Captura · destino `/motor72h` · source `meta` · medium `cpc` · campaign `lancamento-motor72h` · content `botao-pos-dobra` · link final `go.minhaloja.com/motor72h?utm_source=meta&utm_medium=cpc&utm_campaign=lancamento-motor72h&utm_content=botao-pos-dobra`.
> 2. "Quero o Motor 72h" · página VSL · destino `/checkout72h` · source `email` · medium `email` · campaign `lancamento-motor72h` · content `botao-pos-garantia` · link final `go.minhaloja.com/checkout72h?utm_source=email&utm_medium=email&utm_campaign=lancamento-motor72h&utm_content=botao-pos-garantia`.
> 3. "Sim, instalem para mim" · página Upsell · destino `/obrigado` · source `email` · medium `email` · campaign `lancamento-motor72h` · content `botao-upsell-unico` · link final `go.minhaloja.com/obrigado?utm_source=email&utm_medium=email&utm_campaign=lancamento-motor72h&utm_content=botao-upsell-unico`.
> **3. REDIRECIONAMENTOS** — Carrinho abre: e-mail #1 da semana → destino `/motor72h`. Carrinho fecha: 5 dias depois, 23h59 → redirect 301 de `/checkout72h` para `/lista-espera`. Redirects antigos: nenhum.
> **4. STATUS** — Links com teste OK: **8/8**. UTM no analytics: **sim**. CTAs sem link final: **nenhum**. funnel-no-dead-end-gate: **VERDE** — 2026-06-02. tech-links-utm-gate: **VERDE** — 2026-06-02.

## DoD do entregável
A malha de Links & URLs está pronta quando: (1) **toda** página do [`funnel-map`](funnel-map-template.md) tem uma vanity URL legível e uma URL de destino real, sem `{{PLACEHOLDER}}` solto; (2) **todo** CTA do [`page-specs`](page-specs-template.md) tem uma linha na tabela de UTM, com `source`, `medium`, `campaign` e `content` preenchidos no padrão `snake_case`/minúsculas, e o `campaign` é o mesmo em todo o lançamento; (3) cada linha tem o link final rastreável montado (destino + query string) pronto para entrar no botão, anúncio ou e-mail; (4) os redirecionamentos de carrinho (abre/fecha) seguem o [`cart-open-close`](../../frameworks/launch/cart-open-close.md) e mandam o "fora da janela" para lista de espera, nunca para beco; (5) cada link passou no teste de clique em desktop e mobile e o UTM chega no analytics — sem isso o [`tech-links-utm-gate`](../../checklists/tech/tech-links-utm-gate.md) reprova; (6) nenhum CTA fica sem link final e nenhum destino aponta para beco, mantendo o [`funnel-no-dead-end-gate`](../../checklists/funnel/funnel-no-dead-end-gate.md) verde. Só então a malha alimenta o [`tech-deliverability-plan`](tech-deliverability-plan-template.md), que garante que esses links chegam à caixa de entrada e aguentam o pico.
