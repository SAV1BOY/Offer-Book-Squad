---
id: archive.losing-controls.autopsy-false-countdown-scarcity
title: "Autópsia — contador de escassez falso (evergreen)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
registries: [data.registry.control-registry, data.registry.lessons-learned-registry, data.registry.claim-registry]
tags: [autopsy, losing-control, truthful-scarcity, compliance, email]
---

# Autópsia — contador "últimas horas" perpétuo

- **control_id:** email-evergreen-countdown-v1
- **asset_type:** email
- **Perdeu para:** email-real-cohort-cap-v2
- **Métrica:** cart_close conversion — 1,1% vs 2,9% (+ pico de reembolso/reclamação)
- **Lançamento:** metodo-x-2026-q1 (representativo)

## Hipótese
Um **contador perpétuo** ("a oferta acaba em 2h", que reinicia a cada visita) criaria urgência e subiria a conversão de fechamento.

## O que falhou
A escassez era **falsa**: a lista percebeu que o carrinho **reabre sempre**. Quebrou a confiança no momento de maior intenção e disparou reclamações. Viola `truthful_scarcity` — **veto terminal** do [`compliance-auditor`](../../agents/compliance-auditor.md) ([`compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md)). Urgência fabricada não tem override: destrói LTV e marca.

## Evidência
| Sinal | Perdedor | Vencedor | Delta |
|---|---|---|---|
| cart_close conversion | 1,1% | 2,9% | −1,8 p.p. |
| taxa de reembolso | 9% | 3% | +6 p.p. |
| reclamações/spam | 2,3× | base | +130% |

## Lição
Escassez **só quando real**: cohort cap verdadeiro, data que de fato fecha, bônus que de fato some — ver [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md). Se a resposta a "existe limite físico/data real?" é "não, mas converte melhor", o item **morre** no gate. → lição `ll-2026q1-truthful-scarcity`.

## Links
- vencedor: email-real-cohort-cap-v2 · lição: `ll-2026q1-truthful-scarcity` · swipe: [`swipe/scarcity-urgency`](../../swipe/scarcity-urgency/index.md)
- princípio violado: `truthful_scarcity` · gate: [`compliance-scarcity-truth-gate`](../../checklists/compliance/compliance-scarcity-truth-gate.md)
