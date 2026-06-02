---
id: checklist.affiliate.affiliate-referral-tracking-gate
title: "Gate — Rastreamento de Indicação (cada venda de afiliado é atribuída ao parceiro certo)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
frameworks: [launch/affiliate-army, launch/runway-and-phases]
registries: [decision-registry]
tags: [gate, afiliados, rastreamento, atribuicao, links, epc, d6]
---

# Gate — Rastreamento de Indicação

## Propósito
Este gate prova que **cada venda de afiliado é rastreada e atribuída ao parceiro certo, e que o leaderboard se alimenta de números reais**. Ele existe porque comissão sem rastreamento confiável gera disputa, pagamento errado e desconfiança que afasta o afiliado. O `affiliate-program-architect` garante que cada parceiro recebe um link rastreável próprio, que a conversão é atribuída por uma fonte única de verdade, e que dá para medir o EPC por parceiro (quanto cada um converte). Vale o princípio `traceability_before_eloquence`: a indicação tem dono conhecido, do clique à venda líquida. O rastreamento se integra ao plano de links/UTM do `tech-links-deliverability-engineer` — os links de afiliado seguem a mesma instrumentação. Este gate é a base de dados do `affiliate-leaderboard-gate` (que ranqueia) e do `affiliate-prizes-aligned-gate` (que paga): sem atribuição correta, ranking e comissão mentem. Este gate julga **só a atribuição e a medição da indicação** — a mecânica do ranking é do leaderboard, e o conteúdo das peças é do `affiliate-swipe-kit-gate`. Venda que não dá para atribuir ao parceiro certo não passa.

## Dono & Escopo
- **owner_agent:** `affiliate-program-architect` (define o esquema de atribuição e a medição por parceiro). O [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) instrumenta os links.
- **Artefato inspecionado:** a parte de rastreamento do `affiliate-program` (links rastreáveis, atribuição, reporte), cruzada com o plano de links/UTM técnico. As regras de atribuição vão ao [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
Cada venda de afiliado é atribuída ao parceiro certo por uma fonte única, com EPC mensurável por parceiro e líquido de reembolso.

## Itens
1. **Link por parceiro.** Verificar: cada afiliado tem um link rastreável próprio e único.
2. **Atribuição única.** Verificar: há uma fonte única de verdade que credita a venda ao parceiro certo.
3. **Sem venda órfã.** Verificar: nenhuma venda de afiliado fica sem atribuição ou com dono ambíguo.
4. **EPC por parceiro.** Verificar: dá para medir earnings-per-click ou conversão por parceiro.
5. **Líquido de reembolso.** Verificar: o rastreamento desconta estorno/reembolso na atribuição final.
6. **Integrado ao tech.** Verificar: os links de afiliado seguem a convenção UTM/rastreamento do tech-engineer.

## Evidência Exigida
Para marcar ✅: linkar as regras de atribuição no [`decision-registry`](../../data/registries/decision-registry.md) (link por parceiro, fonte única, líquido de reembolso), mais o teste de atribuição mostrando a venda creditada ao parceiro certo e o EPC por parceiro. O plano de links/UTM do tech-engineer que instrumenta os links fica citado.

## Protocolo de Falha
Item vermelho → o `affiliate-program-architect` **não libera** o programa até a atribuição estar confiável; venda órfã ou dono ambíguo ele corrige com link único e fonte única. Rastreamento que não desconta reembolso ele ajusta para o líquido. O arquiteto **não tem veto**, mas recusa pagar/ranquear sobre dados não confiáveis. Link de afiliado mal instrumentado volta ao [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) para padronizar a UTM/rastreamento. O ranking que consome esses dados é do [`affiliate-leaderboard-gate`](affiliate-leaderboard-gate.md). Re-entrada: corrigir a atribuição, validar o EPC por parceiro e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`affiliate-program-architect`](../../agents/affiliate-program-architect.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md)
- Gates irmãos: [`affiliate-prizes-aligned-gate`](affiliate-prizes-aligned-gate.md) · [`affiliate-leaderboard-gate`](affiliate-leaderboard-gate.md) · [`affiliate-funnel-gate`](affiliate-funnel-gate.md) · [`affiliate-swipe-kit-gate`](affiliate-swipe-kit-gate.md)
