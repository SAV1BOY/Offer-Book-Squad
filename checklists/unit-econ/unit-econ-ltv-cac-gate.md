---
id: checklist.unit-econ.unit-econ-ltv-cac-gate
title: "Gate — Razão LTV:CAC Conhecida e Saudável"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [offer-stack-builder, guarantee-design, scarcity-urgency-engine, magic-naming, risk-reversal-ladder]
registries: [offer-registry]
tags: [gate, unit-econ, ltv, cac, razao, d2, economia]
---

# Gate — Razão LTV:CAC Conhecida e Saudável

## Propósito
Este gate prova que a **razão LTV:CAC** da oferta foi calculada com números reais (ou estimados com suposição explícita) e está num patamar saudável. Ele existe porque a aritmética dura de Hormozi é inegociável: um negócio que gasta mais para adquirir um cliente do que ganha com ele ao longo da vida quebra, por mais linda que a oferta pareça. O gate materializa o KPI `ltv_cac_ratio` do `config.yaml` e impede o **falso positivo** mais comum — confundir LTV inflado (receita bruta) com caixa real (LTV com margem). Ele exige que o CAC esteja conhecido (ou estimado por proxy de canal, marcado `estimado`) e que o LTV use margem de contribuição, não faturamento. Diferente do gate de payback (que mede **quando** o CAC volta) e do de liquidação (que mede se a **atração** cobre o CAC), este mede a **proporção de longo prazo**: cada real de aquisição traz quantos reais de margem? É o gate que prova que a unidade econômica fecha antes de a oferta virar copy.

## Dono & Escopo
- **owner_agent:** `unit-economics-stack-analyst` (o alarme aritmético; sem veto, sinaliza ao money-model e ao chief).
- **Artefato inspecionado:** a **`unit-economics-sheet`** — `cac`, `ltv`, `ltv_cac_ratio` e a margem usada — no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
LTV e CAC estão calculados (ou estimados com suposição), o LTV usa margem de contribuição e não receita bruta, e a razão LTV:CAC está num patamar saudável e declarado.

## Itens
1. **CAC conhecido ou estimado.** Verificar: o `cac` está calculado com custo real de aquisição, ou estimado por proxy de canal e marcado `estimado` com a suposição declarada.
2. **LTV com margem, não receita.** Verificar: o `ltv` usa **margem de contribuição** ao longo da escada (não faturamento bruto) — sem LTV inflado.
3. **Razão calculada.** Verificar: `ltv_cac_ratio` está computada e registrada no [`offer-registry`](../../data/registries/offer-registry.md).
4. **Patamar saudável declarado.** Verificar: a razão está acima do piso saudável do caso (alvo típico ≥ 3:1) ou o desvio está justificado e sinalizado.
5. **Sensibilidade quando estimado.** Verificar: se o CAC é `estimado`, há a curva de sensibilidade (a que CAC a razão deixa de ser saudável).
6. **Sem falso positivo de caixa.** Verificar: a razão não esconde estouro de caixa — confronta-se LTV:CAC com o payback (uma razão bonita com payback longo é alertada).
7. **Economia registrada.** Verificar: `cac`, `ltv`, margem e razão estão no [`offer-registry`](../../data/registries/offer-registry.md) com `owner_agent: unit-economics-stack-analyst`.

## Evidência Exigida
Para marcar cada item ✅, linkar a `unit-economics-sheet` no [`offer-registry`](../../data/registries/offer-registry.md) (campos `cac`, `ltv`, `margem_contrib`, `ltv_cac_ratio`), a fórmula usada para o LTV (mostrando que usa margem), e — quando `estimado` — a curva de sensibilidade do CAC. O confronto LTV:CAC × payback é a evidência-resumo de que a razão não é um falso positivo de caixa.

## Protocolo de Falha
Item vermelho → não fecha o cálculo. CAC desconhecido → estima por proxy, marca `estimado` e entrega a sensibilidade (a que CAC a razão quebra). LTV inflado (usa receita bruta) → recalcula com margem de contribuição. Razão abaixo do piso → testa ≥3 alavancas (subir AOV, continuidade, baixar CAC via canal) e devolve ao [`money-model-designer`](../../agents/money-model-designer.md) a que recupera com menor dano. Razão bonita com payback longo → alerta o estouro de caixa. O analista **não tem veto**: se a margem não comporta nenhum CAC plausível, **sinaliza** ao [`money-model-designer`](../../agents/money-model-designer.md) e ao [`offerbook-chief`](../../agents/offerbook-chief.md) — a espinha precisa mudar. Re-entrada: recalculada a economia, o gate é re-submetido.

## Links
- Frameworks: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`guarantee-design`](../../frameworks/guarantee-design.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`magic-naming`](../../frameworks/magic-naming.md) · [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Template: [`unit-economics-template`](../../templates/strategy/unit-economics-template.md)
- Gate relacionado (money model): [`money-model-cac-liquidation-gate`](../money-model/money-model-cac-liquidation-gate.md)
- Gates irmãos: [`unit-econ-payback-gate`](unit-econ-payback-gate.md) · [`unit-econ-breakeven-gate`](unit-econ-breakeven-gate.md) · [`unit-econ-cac-liquidation-gate`](unit-econ-cac-liquidation-gate.md) · [`unit-econ-margin-gate`](unit-econ-margin-gate.md)
