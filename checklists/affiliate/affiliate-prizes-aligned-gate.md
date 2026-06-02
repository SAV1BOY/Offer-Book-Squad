---
id: checklist.affiliate.affiliate-prizes-aligned-gate
title: "Gate — Prêmios Alinhados (comissão e prêmios cabem na unit economics)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
frameworks: [launch/affiliate-army, launch/runway-and-phases]
registries: [decision-registry]
tags: [gate, afiliados, prizes, comissao, unit-economics, margem, d6]
---

# Gate — Prêmios Alinhados

## Propósito
Este gate prova que **a comissão e os prêmios do programa cabem dentro do teto que a unit economics permite**. Ele existe porque "dar 80% para todo mundo" quebra a margem que não existe: a comissão sai do que o LTV, o CAC e o payback sustentam, nunca de uma margem inventada. O `affiliate-program-architect` lê LTV/CAC/payback da unit economics — **é o teto da comissão** — e decide sobre o quê ela incide (front-end, upsell, continuidade). Vale o princípio `value_equation_test` aplicado à economia do programa: cada real de comissão precisa ainda deixar o LTV:CAC saudável. No ToT do agente, modelos que estouram o teto são podados; mercados com poucos grandes players favorecem tiered + leaderboard, e a comissão pode ser generosa no front quando a continuidade recupera o resto. Este gate julga **só o fit econômico da comissão e dos prêmios** — a mecânica do ranking é do `affiliate-leaderboard-gate`, e a disclosure de afiliação é do `affiliate-swipe-kit-gate`. Estrutura que inverte a unit economics não é publicada: volta ao unit-economics-stack-analyst e ao money-model-designer.

## Dono & Escopo
- **owner_agent:** `affiliate-program-architect` (define comissão e prêmios dentro do teto econômico).
- **Artefato inspecionado:** o `affiliate-program` e o `affiliate-prizes`, cruzados com a `unit-economics` (LTV/CAC/payback) e o `money-model` (sobre o quê a comissão incide). A estrutura escolhida vai ao [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
A comissão e os prêmios cabem no teto da unit economics, mantendo o LTV:CAC saudável após pagar os afiliados.

## Itens
1. **Teto conhecido.** Verificar: LTV, CAC e payback da unit economics estão definidos como teto da comissão.
2. **Comissão dentro do teto.** Verificar: o percentual por venda não inverte o LTV:CAC após o pagamento.
3. **Incidência definida.** Verificar: está claro sobre o quê a comissão incide (front-end, upsell, continuidade).
4. **Prêmios cabem.** Verificar: os prêmios por marco/ranking estão orçados dentro da economia.
5. **Generosidade sustentável.** Verificar: comissão alta no front só ocorre quando upsell/continuidade recuperam o payback.
6. **Estrutura registrada.** Verificar: o modelo escolhido e os podados estão no decision-registry com o motivo.

## Evidência Exigida
Para marcar ✅: linkar a decisão no [`decision-registry`](../../data/registries/decision-registry.md) no formato `{title, chosen_option (comissão/prêmios), alternatives, rationale, trade_off}`, mais o cálculo mostrando o LTV:CAC saudável após pagar afiliados (teto vs comissão). A `unit-economics` e o `money-model` que embasaram o teto ficam citados.

## Protocolo de Falha
Item vermelho → o `affiliate-program-architect` **não publica** a estrutura que inverte a unit economics e devolve ao [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) e ao [`money-model-designer`](../../agents/money-model-designer.md). Comissão que quebra a margem ele rebaixa ao teto e usa prêmios não-percentuais para motivar sem inverter a economia. O arquiteto **não tem veto**, mas recusa publicar o que estoura o teto e escala ao [`offerbook-chief`](../../agents/offerbook-chief.md) o conflito entre generosidade e margem que não resolve com a unit economics. A mecânica do ranking é do [`affiliate-leaderboard-gate`](affiliate-leaderboard-gate.md). Re-entrada: rebaixar a comissão ao teto, re-orçar os prêmios e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`affiliate-program-architect`](../../agents/affiliate-program-architect.md) · [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`money-model-designer`](../../agents/money-model-designer.md)
- Gates irmãos: [`affiliate-leaderboard-gate`](affiliate-leaderboard-gate.md) · [`affiliate-referral-tracking-gate`](affiliate-referral-tracking-gate.md) · [`affiliate-funnel-gate`](affiliate-funnel-gate.md) · [`affiliate-swipe-kit-gate`](affiliate-swipe-kit-gate.md)
