---
id: checklist.affiliate.affiliate-funnel-gate
title: "Gate — Funil de Afiliado (o parceiro recebe tudo pronto para promover sem fricção)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
frameworks: [launch/affiliate-army, launch/runway-and-phases]
registries: [decision-registry]
tags: [gate, afiliados, funil, onboarding, plug-and-play, blackbook, d6]
---

# Gate — Funil de Afiliado

## Propósito
Este gate prova que **o funil de afiliado está pronto para o parceiro promover sem fricção, no dia certo da sequência**. Ele existe porque um afiliado motivado que não acha o link, a data ou o material desiste — e o alcance prometido evapora. O `affiliate-program-architect` monta o caminho completo: página de recrutamento (com a economia e os prêmios), onboarding com as datas das Fases, área com links rastreáveis + swipe + e-mails por fase, e reporte de desempenho. A cadência de promoção herda do `runway-and-phases` via o run-of-show — o swipe cobre exatamente as janelas em que os afiliados entram (abertura e fechamento). Vale o princípio `clarity_before_volume`: o parceiro entende o que fazer e quando, sem fricção. Este gate consolida a prontidão do `affiliate-blackbook` (o entregável navegável: datas, links, swipe, regras, disclosure, FAQ). Este gate julga **só a prontidão do funil/blackbook** — o fit econômico é do `affiliate-prizes-aligned-gate`, a atribuição é do `affiliate-referral-tracking-gate`, e o conteúdo do swipe + disclosure é do `affiliate-swipe-kit-gate`. Funil incompleto (sem links ou datas) não libera o blackbook.

## Dono & Escopo
- **owner_agent:** `affiliate-program-architect` (monta o funil de afiliado e empacota o blackbook).
- **Artefato inspecionado:** o `affiliate-program` (funil) e o `affiliate-blackbook`, cruzados com o `run-of-show`/`events-calendar` (as janelas de promoção) e o `offer-book` (a oferta promovida). As decisões de estrutura vão ao [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
O funil de afiliado tem recrutamento, onboarding com datas, área com links e material, e reporte — pronto para promover sem fricção.

## Itens
1. **Página de recrutamento.** Verificar: existe página que mostra a economia, os prêmios e como entrar.
2. **Onboarding com datas.** Verificar: o onboarding traz o calendário das Fases (quando promover).
3. **Área do afiliado.** Verificar: há área com links rastreáveis, swipe e e-mails prontos por fase.
4. **Swipe nas janelas certas.** Verificar: o material cobre as janelas em que afiliados entram (abertura, fechamento).
5. **Reporte de desempenho.** Verificar: o parceiro vê o próprio resultado (cliques, vendas, comissão).
6. **Blackbook completo.** Verificar: o affiliate blackbook reúne datas, links, swipe, regras, disclosure e FAQ.

## Evidência Exigida
Para marcar ✅: linkar o `affiliate-blackbook` mostrando recrutamento → onboarding (datas) → área (links + swipe + e-mails) → reporte, mais a confirmação de que cada parte está pronta (links ativos, datas das Fases, material por janela). As janelas do `run-of-show` que definem a cadência ficam citadas. As decisões de estrutura ficam no [`decision-registry`](../../data/registries/decision-registry.md).

## Protocolo de Falha
Item vermelho → o `affiliate-program-architect` **não libera** o blackbook até o funil estar plug-and-play (links, datas, swipe, reporte). Funil incompleto (sem links ou datas) ele completa antes de entregar. O arquiteto **não tem veto**, mas recusa entregar um funil que gera fricção para o parceiro. Conteúdo de swipe sem disclosure ou com claim sem lastro é tratado no [`affiliate-swipe-kit-gate`](affiliate-swipe-kit-gate.md) e sinalizado ao [`compliance-auditor`](../../agents/compliance-auditor.md). A atribuição dos links é do [`affiliate-referral-tracking-gate`](affiliate-referral-tracking-gate.md). Re-entrada: completar cada parte do funil, fechar o blackbook e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`affiliate-program-architect`](../../agents/affiliate-program-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`affiliate-prizes-aligned-gate`](affiliate-prizes-aligned-gate.md) · [`affiliate-leaderboard-gate`](affiliate-leaderboard-gate.md) · [`affiliate-referral-tracking-gate`](affiliate-referral-tracking-gate.md) · [`affiliate-swipe-kit-gate`](affiliate-swipe-kit-gate.md)
