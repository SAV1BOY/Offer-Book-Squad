---
id: checklist.launch.launch-objective-gate
title: "Gate — Objetivo do Lançamento (tese, datas-âncora e meta claras)"
type: gate
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [launch/product-launch-formula, launch/runway-and-phases, launch/surge-ops]
registries: [decision-registry]
tags: [gate, launch, objetivo, launch-memo, meta, datas, d6]
---

# Gate — Objetivo do Lançamento

## Propósito
Este gate prova que o **launch memo define com clareza a tese do lançamento, as datas-âncora e a meta** antes de qualquer fase ser desenhada. Ele existe porque um lançamento sem objetivo nítido vira uma agenda de eventos avulsos: ninguém sabe o que se está provando, quando o carrinho abre e fecha, nem qual número significa sucesso. Vale o princípio `decision_before_ornament`: cada fase do run-of-show serve à meta, e a meta precisa existir primeiro. O gate exige que a tese caiba em uma frase, que as datas-âncora (pré-lançamento, abertura e fechamento de carrinho) estejam cravadas, e que a meta seja um número — receita, vendas ou aplicações. É a barreira de entrada do `launch-producer`: sem objetivo travado, o sequenciamento não começa, porque uma sequência sem alvo não constrói desejo, só ocupa o calendário.

## Dono & Escopo
- **owner_agent:** `launch-producer` (escreve e trava o launch memo). O `offerbook-chief` aprova o objetivo e a prioridade do lançamento.
- **Artefato inspecionado:** o `launch-memo` com a tese, datas-âncora, meta e papéis, registrado no [`decision-registry`](../../data/registries/decision-registry.md), derivado do `offer-book` (Big Idea, janela pretendida) e do `money-model` (a espinha a executar).

## Condição de Passagem
O launch memo declara a tese em uma frase, as datas-âncora de pré-lançamento e de abertura e fechamento de carrinho, e uma meta numérica.

## Itens
1. **Tese em uma frase.** Verificar: o memo resume o lançamento em uma frase ("Prove no webinar, feche em 4 dias"), derivada da Big Idea.
2. **Datas-âncora cravadas.** Verificar: pré-lançamento, abertura de carrinho e fechamento têm data/hora explícitas.
3. **Meta numérica.** Verificar: a meta é um número (receita, vendas ou aplicações), não "vender bem".
4. **Espinha respeitada.** Verificar: o objetivo executa a sequência do `money-model` (atração→upsell→downsell→continuidade) na ordem.
5. **Papéis atribuídos.** Verificar: o memo nomeia quem faz o quê (quem dispara e-mail, quem opera a live, quem monitora).
6. **Janela coerente com a oferta.** Verificar: a janela e o formato pretendido combinam com o preço e a complexidade do núcleo.
7. **Escassez ancorada em realidade.** Verificar: a meta e as datas não dependem de deadline ou vaga falsa (pré-checagem do `compliance-auditor`).

## Evidência Exigida
Para marcar ✅: linkar o `launch-memo` com a tese, as datas-âncora e a meta (itens 1–3), o mapa que liga o objetivo à espinha do `money-model` (item 4) e a tabela de papéis (item 5). A decisão de objetivo aponta para o `decision-registry`.

## Protocolo de Falha
Item vermelho → o `launch-producer` **reescreve o memo** até a tese, as datas e a meta ficarem nítidas; sem objetivo travado não se desenha fase. Meta vaga ou data ausente reabre o gate. Conflito de prioridade ou janela escala-se ao [`offerbook-chief`](../../agents/offerbook-chief.md). Escassez não-lastreada na meta é sinalizada ao [`compliance-auditor`](../../agents/compliance-auditor.md), que detém o veto. A prontidão de cada fase é tratada no [`launch-phase-readiness-gate`](launch-phase-readiness-gate.md). Re-entrada: travar tese/datas/meta, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`launch/product-launch-formula`](../../frameworks/launch/product-launch-formula.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md) · [`launch/surge-ops`](../../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`launch-producer`](../../agents/launch-producer.md) · [`offerbook-chief`](../../agents/offerbook-chief.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`launch-roles-gate`](launch-roles-gate.md) · [`launch-phase-readiness-gate`](launch-phase-readiness-gate.md) · [`launch-surge-gate`](launch-surge-gate.md) · [`launch-fallback-gate`](launch-fallback-gate.md)
