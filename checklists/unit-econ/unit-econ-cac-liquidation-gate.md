---
id: checklist.unit-econ.unit-econ-cac-liquidation-gate
title: "Gate — A Oferta de Atração Liquida o CAC no Front-End"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [offer-stack-builder, guarantee-design, scarcity-urgency-engine, magic-naming, risk-reversal-ladder]
registries: [offer-registry]
tags: [gate, unit-econ, cac-liquidation, front-end, d2, money-model-spine]
---

# Gate — A Oferta de Atração Liquida o CAC no Front-End

## Propósito
Este é o gate-assinatura do `unit-economics-stack-analyst` — a prova aritmética central de Hormozi: **a oferta de atração precisa liquidar o CAC no front-end** para o negócio financiar a própria aquisição. Ele existe porque essa é a diferença entre escalar com caixa próprio e depender de capital externo: se a receita de front (atração + upsells imediatos) cobre o custo de adquirir o cliente, cada nova venda se autofinancia. O gate materializa o KPI `front_end_cac_liquidation` e o princípio `money_model_spine` (o centro é a sequência, não a oferta avulsa). Ele exige localizar **onde** na escada o CAC é liquidado e provar que a soma de margem do front o cobre. Diferente do gate LTV:CAC (longo prazo) e do payback (tempo), este responde uma pergunta binária e imediata: a atração se paga **no front**, ou o negócio fica refém de financiar o CAC? É o alarme que dispara as flags para o money-model reconfigurar a espinha.

## Dono & Escopo
- **owner_agent:** `unit-economics-stack-analyst` (o alarme aritmético; sem veto, aciona o money-model e o chief).
- **Artefato inspecionado:** o veredito `cac_liquidado` e o `ponto_de_liquidacao` na `unit-economics-sheet` no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
A margem do front-end (atração + upsells imediatos) cobre o CAC, o ponto de liquidação está localizado na escada, e o veredito está declarado (sim/não/estimado).

## Itens
1. **CAC vs receita de front confrontados.** Verificar: a soma de margem do front (atração + take-rate dos upsells imediatos) é comparada ao CAC.
2. **Liquidação localizada.** Verificar: o `ponto_de_liquidacao` aponta **onde** na escada (qual upsell/bump) o CAC passa a ser coberto.
3. **Veredito declarado.** Verificar: `cac_liquidado` está marcado `sim | não | estimado` no [`offer-registry`](../../data/registries/offer-registry.md).
4. **Take-rate defensável.** Verificar: os take-rates de upsell que sustentam a liquidação são realistas (não otimistas sem base).
5. **Alavancas testadas se não liquida.** Verificar: quando não liquida, ≥3 alavancas de correção foram geradas e pontuadas (bump de velocidade, upsell mais cedo, continuidade no checkout).
6. **Sem maquiagem por escassez falsa.** Verificar: nenhuma alavanca que depende de escassez/urgência falsa foi usada para fechar a conta — `truthful_scarcity` respeitado.
7. **Sensibilidade quando estimado.** Verificar: se o CAC é `estimado`, há o CAC-limite (até que CAC a atração ainda liquida).

## Evidência Exigida
Para marcar cada item ✅, linkar a `unit-economics-sheet` no [`offer-registry`](../../data/registries/offer-registry.md) (`cac`, `aov_front`, `cac_liquidado`, `ponto_de_liquidacao`), o cálculo de margem do front com os take-rates usados, e — quando não liquida na primeira passada — a tabela de alavancas pontuadas. O CAC-limite (quando `estimado`) é a evidência-resumo de até onde a liquidação se sustenta.

## Protocolo de Falha
Item vermelho → não declara liquidação. Não liquida → testa ≥3 alavancas e devolve ao [`money-model-designer`](../../agents/money-model-designer.md) a que recupera a liquidação com menor dano à conversão; o que está fora do escopo (baixar CAC trocando canal) vira flag ao tráfego. Take-rate otimista → ajusta para defensável e recalcula. Tentação de maquiar com escassez falsa → **recusa**; reporta que a oferta não fecha e propõe alavanca honesta. CAC estimado sem CAC-limite → adiciona a sensibilidade. O analista **não tem veto**, mas é o alarme: atração que não liquida → flag forte ao [`money-model-designer`](../../agents/money-model-designer.md) (que pode reconfigurar a espinha) e ao [`offerbook-chief`](../../agents/offerbook-chief.md); escassez sem lastro → flag ao [`compliance-auditor`](../../agents/compliance-auditor.md). Re-entrada: recuperada a liquidação, o gate é re-submetido.

## Links
- Frameworks: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`guarantee-design`](../../frameworks/guarantee-design.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`magic-naming`](../../frameworks/magic-naming.md) · [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`money-model-designer`](../../agents/money-model-designer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gate espelho (money model): [`money-model-cac-liquidation-gate`](../money-model/money-model-cac-liquidation-gate.md)
- Gates irmãos: [`unit-econ-ltv-cac-gate`](unit-econ-ltv-cac-gate.md) · [`unit-econ-payback-gate`](unit-econ-payback-gate.md) · [`unit-econ-breakeven-gate`](unit-econ-breakeven-gate.md) · [`unit-econ-margin-gate`](unit-econ-margin-gate.md)
