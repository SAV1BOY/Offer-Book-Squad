---
id: data.registry.offer-registry
title: "Registro de Ofertas"
type: registry
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
write_agents: [market-sophistication-analyst, mechanism-architect, value-equation-engineer, money-model-designer, unit-economics-stack-analyst, offer-squad-architect]
read_agents: [vsl-webinar-scriptwriter, email-sms-sequence-writer, ad-creative-factory, funnel-architect, events-logistics-coordinator, compliance-auditor, offerbook-chief]
tags: [offer, money-model, registry, memory, traceability]
---

# Registro de Ofertas

## Propósito

Esta é a **memória estruturada das ofertas** do squad — cada oferta e cada versão que entra no Money Model. Uma oferta nasce do mecanismo, ganha valor pela [Value Equation](../../frameworks/value-equation.md), recebe preço derivado de WTP e ocupa um **papel na sequência** (atração, núcleo, upsell, downsell, continuidade). Aqui registramos **o quê existe, em qual versão, a que preço e por quê**, com link para a decisão que a originou.

O registro existe para cumprir três princípios: `memory_before_repetition` (reusar antes de recriar), `traceability_before_eloquence` (toda oferta aponta para a decisão que a criou) e `money_model_spine` (cada oferta tem um papel na escada, não é avulsa). Sem ele, copy e funil escreveriam sobre ofertas fantasma.

## Schema

Os valores controlados vêm de [`offer-types`](../../lib/taxonomies/offer-types.md), [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md) e [`guarantee-types`](../../lib/taxonomies/guarantee-types.md).

| Campo | Tipo | Valores permitidos | Obrigatório? |
|---|---|---|---|
| `offer_id` | string (slug) | `kebab-case` único, ex.: `core-mentoria-90d` | Sim |
| `name` | string | nome humano da oferta | Sim |
| `version` | semver | ex.: `1.0.0`; sobe em mudança material | Sim |
| `money_model_role` | enum | `atracao` \| `core` \| `upsell` \| `downsell` \| `continuidade` | Sim |
| `offer_subtype` | enum | tripwire, free-frete, bogo, giveaway, win-money-back, decoy, trial-pago, grand-slam, upgrade, dfy, parcelado, assinatura, comunidade | Não |
| `mechanism_id` | ref | id em [`offer-registry`/mecanismo](../../frameworks/unique-mechanism.md) ou claim ligado | Não |
| `price` | money | número + moeda, ex.: `R$ 2497` | Sim |
| `price_basis` | enum | `value-based` \| `wtp` \| `anchor` \| `cost-plus` (evitar) | Sim |
| `sophistication_stage` | int 1-5 | 1=primeiro · 2=amplifica · 3=mecanismo · 4=eleva-mecanismo · 5=identidade | Sim |
| `guarantee_type` | enum | 1-13 de [`guarantee-types`](../../lib/taxonomies/guarantee-types.md), ex.: `reembolso-incondicional` | Não |
| `status` | enum | `draft` \| `proposed` \| `active` \| `control` \| `retired` | Sim |
| `value_eq_score` | int 0-100 | nota da Value Equation | Não |
| `owner_agent` | agent-id | id real de [`config.yaml`](../../config.yaml) | Sim |
| `decided_in` | ref | id de decisão em [`decision-registry`](decision-registry.md) | Sim |
| `updated` | ISO date | `YYYY-MM-DD` | Sim |

## Quem escreve / Quem lê

**Escrevem** (cada um na sua etapa do pipeline D2):
- `market-sophistication-analyst` — cria a oferta-semente com `sophistication_stage` justificado.
- `mechanism-architect` — liga `mechanism_id` e nomeia o núcleo.
- `value-equation-engineer` — preenche `value_eq_score` (pode reprovar oferta sem alavanca).
- `pricing-wtp-strategist` — define `price` e `price_basis` (cruza com [`price-test-registry`](price-test-registry.md)).
- `unit-economics-stack-analyst` — valida que a atração liquida o CAC e escolhe `guarantee_type`.
- `money-model-designer` — atribui o `money_model_role` e ordena a escada.

**Leem**: `vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `ad-creative-factory` (escrevem copy sobre a oferta travada), `funnel-architect` (mapeia páginas por oferta), `events-logistics-coordinator`, `compliance-auditor` (confere garantia exequível) e `offerbook-chief` (DoD do Offer Book).

## Registros

| offer_id | name | version | money_model_role | offer_subtype | mechanism_id | price | price_basis | sophistication_stage | guarantee_type | status | value_eq_score | owner_agent | decided_in | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `core-exemplo-90d` _(EXEMPLO ILUSTRATIVO — apagar)_ | Mentoria 90 Dias (amostra) | 1.0.0 | core | grand-slam | metodo-x | R$ 2497 | value-based | 3 | reembolso-incondicional | active | 82 | money-model-designer | `dec-exemplo-0001` | 2026-06-02 |

<!-- Tabela semeada VAZIA. A linha acima é um exemplo ilustrativo, marcada como (EXEMPLO ILUSTRATIVO). Os agentes apagam o exemplo e escrevem registros reais. -->
