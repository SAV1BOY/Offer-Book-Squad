---
id: archive.losing-controls.autopsy-cold-vsl-offer-lead
title: "Autópsia — VSL com lead de Oferta em tráfego frio"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
registries: [data.registry.control-registry, data.registry.lessons-learned-registry, data.registry.swipe-registry]
tags: [autopsy, losing-control, lead-types, awareness, vsl]
---

# Autópsia — VSL "Oferta-direto" (tráfego frio)

- **control_id:** vsl-offer-lead-cold-v1
- **asset_type:** vsl
- **Perdeu para:** vsl-history-lead-cold-v2
- **Métrica:** vsl_conversion_rate — 0,6% vs 3,8%
- **Lançamento:** ingles-tech-2026-q1 (representativo)

## Hipótese
Abrir a VSL **direto com a oferta** (preço + stack de bônus nos primeiros 15s) converteria o tráfego frio de anúncios, porque "a oferta é forte o suficiente para falar por si".

## O que falhou
O **lead de Oferta** exige consciência **4–5** (já conhece o produto / mais consciente). O tráfego de topo era **inconsciente / consciente-do-problema (1–2)**: ainda sem desejo formado. A oferta no segundo 5 bateu numa audiência sem dor nomeada → abandono massivo antes do mecanismo. É um descasamento clássico de [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) × [`lead-types`](../../lib/taxonomies/lead-types.md): frio pede **História/Proclamação**, não Oferta.

## Evidência
| Sinal | Perdedor | Vencedor | Delta |
|---|---|---|---|
| Retenção @60s | 12% | 47% | −35 p.p. |
| vsl_conversion_rate | 0,6% | 3,8% | −3,2 p.p. |
| CPA | R$ 1.910 | R$ 410 | +366% |

## Lição
Casar o **lead ao nível de consciência** antes de escrever o primeiro segundo (gate [`positioning-awareness-fit`](../../checklists/positioning/positioning-awareness-fit.md)). Tráfego frio → lead de **História** que constrói o desejo, depois mecanismo, depois oferta. → lição `ll-2026q1-lead-awareness-fit`.

## Links
- vencedor: vsl-history-lead-cold-v2 · lição: `ll-2026q1-lead-awareness-fit` · swipe: [`swipe/leads-openers`](../../swipe/leads-openers/index.md)
- framework violado: [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · agente: [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md)
