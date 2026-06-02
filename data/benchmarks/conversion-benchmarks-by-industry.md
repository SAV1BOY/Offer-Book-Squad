---
id: data.benchmarks.conversion-benchmarks-by-industry
title: "Benchmarks de Conversão por Indústria (com fontes)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [benchmarks, conversion, email, webinar, checkout, sources]
---

# Benchmarks de Conversão por Indústria (com fontes)

> **Nota de uso:** Cada número abaixo **cita fonte** com URL e data de acesso (2026-06-02). Benchmarks variam por amostra, ano e metodologia — leia as faixas como referência, não como verdade fixa. Privacidade (ex.: Apple Mail Privacy Protection) **infla taxas de abertura** de e-mail; por isso o clique é sinal mais confiável que a abertura.

## Propósito

Este arquivo dá ao squad os **pisos de mercado** para julgar conversão. Ele responde: "4,1% de conversão de VSL é bom?" Resposta só faz sentido contra um benchmark. As tabelas cobrem landing page, e-mail, webinar e checkout.

## Landing page — conversão por indústria

| Categoria | Faixa / mediana | Observação | Fonte |
|---|---|---|---|
| Todas as indústrias (mediana) | ~6,6% | Mediana sobre ~41 mil páginas; ~10% é "bom", 15%+ é excelente | Unbounce via análises de mercado |
| Média global (18 indústrias) | ~10,76% | Média (puxada por outliers); use a mediana como piso | Compilações de mercado |
| B2B / serviços profissionais | ~1-3% | Ciclo de decisão longo derruba a taxa | First Page Sage |
| Serviços jurídicos | ~7,4% | Alta intenção, decisão curta | First Page Sage |
| Saúde | ~3,0-4,2% | Barreira de confiança e compliance | First Page Sage |
| Serviços financeiros | ~8,4% (mediana) | Topo da tabela | First Page Sage |
| E-commerce | ~2,35% | Páginas otimizadas chegam a 5%+ | Compilações de mercado |

> **Fonte:** First Page Sage, *Landing Page Conversion Rates by Industry: 2026 Report* — via <https://firstpagesage.com/seo-blog/landing-page-conversion-rates-by-industry/>, acesso 2026-06-02.
> **Fonte:** SeoSherpa, *Landing Page Statistics 2026* — via <https://seosherpa.com/landing-page-statistics/>, acesso 2026-06-02.

## E-mail — abertura, clique e clique-para-abrir

| Métrica | Média 2025 | Observação | Fonte |
|---|---|---|---|
| Taxa de abertura | ~43,5% | **Inflada** por Apple Mail (~46% dos clientes pré-carregam imagens) | MailerLite / Mailchimp |
| Taxa de clique (CTR) | ~2,1% | Faixa por indústria ~0,8% a ~4,9% | MailerLite / Mailchimp |
| Clique-para-abrir (CTOR) | ~6,8% | Menos distorcido que a abertura | MailerLite / Mailchimp |
| Maior abertura (setor) | ONGs ~53% | Manufatura ~33% fica na base | MailerLite |
| Maior clique (setor) | Manufatura ~4,3%; governo ~4,8% | Varejo ~1,8% fica na base | Mailchimp |

> **Fonte:** MailerLite, *Email Marketing Benchmarks 2025* — via <https://www.mailerlite.com/blog/compare-your-email-performance-metrics-industry-benchmarks>, acesso 2026-06-02.
> **Fonte:** Mailchimp, *Email Marketing Benchmarks by Industry* — via <https://mailchimp.com/resources/email-marketing-benchmarks/>, acesso 2026-06-02.

## Webinar — registro → comparecimento

| Métrica | Faixa típica | Observação | Fonte |
|---|---|---|---|
| Registro → comparecimento ao vivo | ~40-50% comparecem; média ~56-57% | Sequências de lembrete com IA empurram para ~71% | ON24 / MarketingProfs |
| Topo de desempenho | até ~90% | Casos de alto engajamento | ON24 |
| Lift de CTA com personalização | +48% vs sem personalização | Personalização move conversão | ON24 |

> **Fonte:** ON24, *2025 Webinar Benchmarks Report (Key Takeaways)* — via <https://www.on24.com/blog/key-takeaways-from-the-2025-webinar-benchmarks-report/>, acesso 2026-06-02.
> **Fonte:** MarketingProfs, *B2B Webinar Benchmarks* — via <https://www.marketingprofs.com/charts/2025/52917/b2b-webinar-benchmarks-conversion-attendance-personalization>, acesso 2026-06-02.

## Checkout — abandono de carrinho

| Métrica | Faixa típica | Observação | Fonte |
|---|---|---|---|
| Abandono médio de carrinho | ~70% (mediana de ~50 estudos) | Algumas fontes citam ~77% em 2025 | Baymard Institute |
| Mobile vs desktop | mobile ~78%+; desktop ~65-68% | Mobile abandona mais | Compilações de mercado |
| Por categoria | Beleza >80%; produtos digitais ~55-65% | Moda costuma ser alta (75-80%) | Compilações de mercado |
| Causa principal | ~39% por custos extras (frete/taxas) | Custo-surpresa é o líder do abandono | Baymard Institute |

> **Fonte:** Baymard Institute, *Cart Abandonment Rate Statistics* — via <https://baymard.com/lists/cart-abandonment-rate>, acesso 2026-06-02.

## Como alimenta os agentes

- `funnel-architect` calibra metas de etapa (optin, comparecimento, checkout) contra estas faixas.
- `pricing-wtp-strategist` cruza conversão esperada com preço para projetar receita.
- `unit-economics-stack-analyst` usa o abandono de checkout para dimensionar a recuperação de carrinho.
- `vsl-webinar-scriptwriter` e `email-sms-sequence-writer` julgam se o `metric_value` em [`control-registry`](../registries/control-registry.md) bate o mercado.
- `offerbook-chief` decide se um control é forte o bastante para escalar.

## Cross-refs

- Metas internas espelhadas em [`metrics/kpi-dashboard-template.md`](../metrics/kpi-dashboard-template.md).
- Dados crus do nosso funil em [`conversion-data/`](../conversion-data/).
- Resultados de teste do squad em [`controls/`](../controls/) e [`winners/`](../winners/).
