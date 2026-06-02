---
id: checklist.pr.pr-timing-gate
title: "Gate — Timing do Plano de PR"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
frameworks: [launch/pr-brand-maximization, launch/runway-and-phases]
registries: [decision-registry]
tags: [pr, timing, sequencing, post-launch]
---

# Gate — Timing do Plano de PR

## Propósito
Garantir que o PR dispara na **janela certa** — depois que a oferta provou conversão e antes que a atenção do lançamento esfrie. PR cedo demais queima sem prova; tarde demais perde o pico.

## Dono & Escopo
Dono: [`pr-brand-strategist`](../../agents/pr-brand-strategist.md). Escopo: o calendário do plano de PR vs. o run-of-show do lançamento.

## Condição de Passagem
**Cada ativo de PR tem data e gatilho definidos, alinhados às fases do lançamento.**

## Itens
1. O PR principal dispara **após** prova de conversão (não antes do carrinho validar)? *Verificar:* a data do PR vem depois do marco de validação.
2. Cada ativo de PR tem **data + gatilho** (o que precisa estar verdadeiro para publicar)? *Verificar:* calendário com data e condição por peça.
3. O timing está alinhado ao [`runway-and-phases`](../../frameworks/launch/runway-and-phases.md) e ao run-of-show? *Verificar:* sobreposição checada com [`launch-producer`](../../agents/launch-producer.md).
4. Há **janela de embargo/coordenação** quando há imprensa envolvida? *Verificar:* embargo definido se aplicável.
5. Existe plano para **capturar o pico** (momentum) e não só o pós-evento? *Verificar:* ao menos 1 ativo no pico.
6. O cronograma tem **dono e fallback** por data? *Verificar:* responsável + plano B por item.

## Evidência Exigida
Calendário de PR com data, gatilho, dono e fallback por ativo, cruzado com o run-of-show do lançamento.

## Protocolo de Falha
PR sem data/gatilho ou desalinhado das fases → devolve ao `pr-brand-strategist`; conflito com o run-of-show → o `offerbook-chief` decide via [`chief-conflict-resolution-gate`](../chief/chief-conflict-resolution-gate.md).

## Links
Frameworks: [`launch/pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md), [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md). Macro: [`pr-plan-checklist`](../pr-plan-checklist.md).
