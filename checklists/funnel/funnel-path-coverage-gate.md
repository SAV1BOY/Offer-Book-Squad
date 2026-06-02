---
id: checklist.funnel.funnel-path-coverage-gate
title: "Gate — Cobertura de Trilhas (cada degrau do money model vira trilha)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
frameworks: [offer-to-funnel-mapping, launch/cart-open-close]
registries: [decision-registry]
tags: [gate, funil, trilhas, money-model, cobertura, temperatura, d5]
---

# Gate — Cobertura de Trilhas

## Propósito
Este gate prova que **cada degrau do money model vira uma trilha real no funil** — atração, núcleo, upsell, downsell e continuidade — e que cada temperatura de tráfego entra pela porta certa. Ele existe por causa do princípio `money_model_spine`: o centro é a sequência, e o funil é a espinha em movimento. Um funil que mapeia só o front-end deixa receita na mesa e não liquida o CAC. O gate força o `funnel-architect` a traduzir a escada inteira em páginas e sequências, sem pular um degrau, e a casar frio, retarget e quente com o destino adequado. É a barreira que garante que o desenho cobre todo o caminho do tráfego, do primeiro clique ao backend de recorrência, antes de o engenheiro de tech receber as specs.

## Dono & Escopo
- **owner_agent:** `funnel-architect` (desenha as trilhas por degrau e casa a temperatura ao destino). O `money-model-designer` é dono da espinha e detém o **veto** sobre a sequência a montante.
- **Artefato inspecionado:** o `funnel-map` e as `page-specs` com as rotas registradas no [`decision-registry`](../../data/registries/decision-registry.md), cruzados com o `money-model` (as 4 partes) e a `ad-matrix` (temperatura por ângulo).

## Condição de Passagem
Cada uma das partes do money model aparece como trilha no mapa e cada temperatura de tráfego entra pelo degrau correto.

## Itens
1. **Atração mapeada.** Verificar: a trilha de entrada existe e casa com a oferta de atração do `money-model`.
2. **Núcleo mapeado.** Verificar: a trilha do núcleo leva da página de oferta ao checkout, com CTA único.
3. **Upsell e downsell mapeados.** Verificar: o "sim" e o "não" do upsell têm trilha (downsell ou oferta menor), nenhuma parte ausente.
4. **Continuidade mapeada.** Verificar: a recorrência (assinatura, comunidade) tem trilha própria pós-primeiro-resultado.
5. **Entrada por temperatura.** Verificar: frio entra por página educativa/VSL; retarget por página de oferta; quente direto ao checkout (via `ad-matrix`).
6. **CTA único por página.** Verificar: cada página tem **um** próximo passo, sem dispersar a decisão.
7. **Sem degrau órfão.** Verificar: nenhuma das 4 partes do money model fica sem trilha no mapa.

## Evidência Exigida
Para marcar ✅: linkar o `funnel-map` com a tabela degrau→trilha (itens 1–4), o cruzamento temperatura→entrada da `ad-matrix` (item 5) e as `page-specs` com o CTA único por página (item 6). As rotas e bifurcações apontam para o `decision-registry`.

## Protocolo de Falha
Item vermelho → o `funnel-architect` volta ao Tree-of-Thoughts e **recria a trilha faltante** em vez de entregar um funil parcial. Degrau do money model sem trilha reabre o gate. Se a escada a montante tem menos que as partes mínimas, escala-se ao [`money-model-designer`](../../agents/money-model-designer.md) via o Chief — sem backend o CAC não liquida. A ausência de próximo passo por página é tratada no [`funnel-no-dead-end-gate`](funnel-no-dead-end-gate.md); o backend ligado no [`funnel-backend-gate`](funnel-backend-gate.md). Re-entrada: completar as trilhas, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`funnel-architect`](../../agents/funnel-architect.md) · [`money-model-designer`](../../agents/money-model-designer.md)
- Gates irmãos: [`funnel-order-bump-gate`](funnel-order-bump-gate.md) · [`funnel-redirect-gate`](funnel-redirect-gate.md) · [`funnel-no-dead-end-gate`](funnel-no-dead-end-gate.md) · [`funnel-backend-gate`](funnel-backend-gate.md)
