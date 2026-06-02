---
id: checklist.affiliate.affiliate-leaderboard-gate
title: "Gate — Leaderboard (motiva volume sem incentivar engano)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
frameworks: [launch/affiliate-army, launch/cart-open-close]
registries: [decision-registry]
tags: [gate, afiliados, leaderboard, premios, ranking, escassez, d6]
---

# Gate — Leaderboard

## Propósito
Este gate prova que o **leaderboard motiva volume real sem incentivar comportamento enganoso** — para que a competição entre afiliados some vendas saudáveis, não promessas infladas nem reembolsos disfarçados de venda. Ele existe porque um ranking premiado só por volume bruto convida o parceiro a empurrar a oferta a qualquer custo, e isso volta como churn, estorno e risco de marca. O `affiliate-program-architect` desenha o placar como motor de prova social e urgência, mas com freios. O gate exige que a métrica de ranqueamento seja clara, que os prêmios por posição estejam definidos, que exista critério de qualidade (líquido de reembolso) e que a escassez explorada no fechamento seja **verdadeira**. Prova também que o placar é atualizado por uma fonte confiável e que micro-afiliados enxergam ganho, não só os gigantes. Competição que puxa volume limpo passa; competição que premia o engano é barrada aqui.

## Dono & Escopo
- **owner_agent:** [`affiliate-program-architect`](../../agents/affiliate-program-architect.md), dono das regras do leaderboard.
- **Artefato inspecionado:** o bloco de prêmios/leaderboard do `affiliate-program` (métrica, prêmios por ranking, mecânica de atualização), registrado no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
O leaderboard motiva volume com regras claras e critério de qualidade, sem incentivar promessa enganosa nem escassez falsa.

## Itens
1. **Métrica de ranking clara.** Verificar: o que conta para subir no placar (vendas líquidas, EPC, receita) está definido sem ambiguidade.
2. **Prêmios por posição.** Verificar: os prêmios para top 1/3/10 estão escritos e cabem no teto econômico (cruza com o gate de prêmios).
3. **Critério de qualidade.** Verificar: o ranking desconta reembolsos/estornos — volume bruto sozinho não premia.
4. **Escassez verdadeira.** Verificar: a urgência de fechamento que o leaderboard explora é real (não há prazo falso).
5. **Fonte de atualização confiável.** Verificar: o placar é alimentado pelo tracking oficial, não por autorreporte do afiliado.
6. **Justiça percebida.** Verificar: micro-afiliados têm reconhecimento/faixa própria, não só os grandes.

## Evidência Exigida
Para marcar ✅: linkar a definição da métrica de ranqueamento (item 1), a tabela de prêmios por posição (item 2), a regra de desconto de reembolso (item 3), a prova de que o prazo de fechamento é real (item 4) e a fonte de dados do placar (item 5). As regras do leaderboard apontam para o [`decision-registry`](../../data/registries/decision-registry.md).

## Protocolo de Falha
Item vermelho → o `affiliate-program-architect` **não libera** o leaderboard. Ranking premiado só por volume bruto ganha critério de qualidade (líquido de reembolso) antes de ir ao ar. Escassez falsa de fechamento é removida — o prazo precisa ser verdadeiro. Prêmios que estouram o teto voltam ao [`affiliate-prizes-aligned-gate`](affiliate-prizes-aligned-gate.md). Risco de promessa enganosa no placar sinaliza-se ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto. Re-entrada: corrigir a métrica e o critério de qualidade, confirmar a fonte de atualização, atualizar o [`decision-registry`](../../data/registries/decision-registry.md) e re-submeter.

## Links
- Frameworks: [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md) · [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`affiliate-program-architect`](../../agents/affiliate-program-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Checklist do programa: [`affiliate-program-checklist`](../affiliate-program-checklist.md)
- Gates irmãos: [`affiliate-prizes-aligned-gate`](affiliate-prizes-aligned-gate.md) · [`affiliate-referral-tracking-gate`](affiliate-referral-tracking-gate.md) · [`affiliate-funnel-gate`](affiliate-funnel-gate.md) · [`affiliate-swipe-kit-gate`](affiliate-swipe-kit-gate.md)
