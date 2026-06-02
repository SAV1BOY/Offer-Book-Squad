---
id: checklist.funnel.funnel-backend-gate
title: "Gate — Backend Ligado (upsell, downsell e continuidade no funil)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
frameworks: [offer-to-funnel-mapping, launch/cart-open-close]
registries: [decision-registry]
tags: [gate, funil, backend, upsell, downsell, continuidade, ltv, d5]
---

# Gate — Backend Ligado

## Propósito
Este gate prova que o **money model está inteiro no funil** — não só o front-end. Upsell, downsell e continuidade estão ligados e fluindo, para que o funil liquide o CAC e construa o LTV. Ele existe por causa do princípio `money_model_spine`: um funil que para na página de obrigado é uma página de venda, não um money model em movimento. Sem backend, o CAC não liquida e a margem que existiria some. O gate força o `funnel-architect` a ligar o "sim" e o "não" do upsell, encaixar o downsell e abrir a trilha de continuidade pós-primeiro-resultado. Casa diretamente com o `money-model/money-model-four-parts-gate` a montante. É a barreira que distingue um funil que vende uma vez de um que monetiza a relação inteira, e é gate obrigatório do `funnel-architect` no `config.yaml`.

## Dono & Escopo
- **owner_agent:** `funnel-architect` (liga o backend no funil). O `money-model-designer` é dono da espinha e detém o **veto** sobre a sequência; sem backend suficiente a montante, o funil não fecha.
- **Artefato inspecionado:** as trilhas de pós-compra do `funnel-map` registradas no [`decision-registry`](../../data/registries/decision-registry.md), cruzadas com o `money-model` (upsell/downsell/continuidade) e o objetivo econômico de cada degrau. Gate obrigatório conforme `config.yaml: routing.map-funnel`.

## Condição de Passagem
As trilhas de upsell, downsell e continuidade do money model estão ligadas e fluindo no funil, de modo que o CAC liquida e o LTV se constrói.

## Itens
1. **Upsell ligado.** Verificar: o pós-compra apresenta o upsell com CTA, conforme o `money-model`.
2. **Downsell para o "não".** Verificar: a recusa do upsell cai numa versão menor/parcelada, não no vazio.
3. **Continuidade aberta.** Verificar: a trilha de recorrência (assinatura, comunidade) é oferecida pós-primeiro-resultado.
4. **Objetivo econômico por degrau.** Verificar: cada trilha de backend declara seu papel (subir AOV, recuperar o "não", LTV) no `decision-registry`.
5. **Liquidação do CAC.** Verificar: a soma do front-end + backend sustenta a liquidação do CAC prevista no `money-model`.
6. **Continuidade tardia para o "não" final.** Verificar: quem recusa upsell **e** downsell ainda recebe a oferta de continuidade depois.
7. **Backend não é só front-end disfarçado.** Verificar: existem trilhas reais de monetização pós-núcleo, não uma página de obrigado vazia.

## Evidência Exigida
Para marcar ✅: linkar as trilhas de upsell/downsell/continuidade no `funnel-map` (itens 1–3), o papel econômico de cada degrau no `decision-registry` (item 4), a conta de liquidação do CAC do `money-model` (item 5) e a rota de continuidade tardia (item 6).

## Protocolo de Falha
Item vermelho → o `funnel-architect` **volta ao money model e liga o backend** faltante; sem upsell/downsell/continuidade o CAC não liquida. Funil só de front-end reabre o gate. Se a escada a montante não tem backend suficiente, escala-se ao [`money-model-designer`](../../agents/money-model-designer.md) via o Chief — a decisão de barrar é dele. A cobertura das 4 partes é garantida no [`funnel-path-coverage-gate`](funnel-path-coverage-gate.md); a ausência de próximo passo no [`funnel-no-dead-end-gate`](funnel-no-dead-end-gate.md). Re-entrada: ligar as trilhas de backend, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`funnel-architect`](../../agents/funnel-architect.md) · [`money-model-designer`](../../agents/money-model-designer.md)
- Gates irmãos: [`funnel-path-coverage-gate`](funnel-path-coverage-gate.md) · [`funnel-order-bump-gate`](funnel-order-bump-gate.md) · [`funnel-redirect-gate`](funnel-redirect-gate.md) · [`funnel-no-dead-end-gate`](funnel-no-dead-end-gate.md)
