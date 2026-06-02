---
id: checklist.launch-memo-checklist
title: "Checklist — Launch Memo (objetivo, papéis, ad spend, venue, fases com dono/prazo)"
type: checklist
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [launch/product-launch-formula, launch/runway-and-phases, launch/surge-ops]
registries: [decision-registry, offer-registry]
tags: [checklist, launch, memo, objetivo, papeis, ad-spend, venue, fases, d6]
---

# Checklist — Launch Memo

## Propósito
Este checklist prova que o launch memo responde **quem faz o quê, quando e com qual verba** antes de o lançamento começar. Existe porque lançamento sem memo vira improviso: ninguém sabe o objetivo de receita, papéis se sobrepõem, o ad spend não tem teto, a venue não está reservada e as fases não têm dono nem prazo. O memo é o documento-mãe que alinha a tropa. Cada fase — runway, pré-lançamento, abertura, fechamento — precisa de um responsável e uma data. Sem este checklist verde, o lançamento começa sem rumo e queima verba. Ele garante `clarity_before_volume`: uma linha de objetivo, papéis claros e fases com dono valem mais que um plano de cem páginas que ninguém segue.

## Dono & Escopo
- **owner_agent:** `launch-producer` (escreve o memo e responde pela execução); o [`offerbook-chief`](../agents/offerbook-chief.md) aprova o objetivo e o [`events-logistics-coordinator`](../agents/events-logistics-coordinator.md) recebe os entregáveis de logística.
- **Artefato inspecionado:** o **launch memo** (`templates/ops/launch-memo-template` preenchido) e o `templates/ops/launch-phases-template`, registrados no [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
O memo declara objetivo mensurável, papéis sem sobreposição, ad spend com teto, venue definida e cada fase com dono e prazo — pronto para a tropa executar.

## Itens
1. **Objetivo mensurável.** Como verificar: o memo abre com UMA meta numérica (receita, unidades, leads) e a data-alvo; meta vaga reprova.
2. **Papéis sem sobreposição.** Como verificar: cada função (produtor, copy, tech, afiliados, suporte) tem um nome dono; nenhuma tarefa fica sem responsável nem com dois.
3. **Ad spend com teto.** Como verificar: orçamento de mídia declarado com teto e fase de gasto, coerente com as unit economics do `offer-registry`.
4. **Venue definida.** Como verificar: o canal/local do evento (webinar, ao vivo, sala) está nomeado e reservado, com data e capacidade.
5. **Fases com dono e prazo.** Como verificar: cada fase do lançamento (runway, pré, abertura, fechamento) tem responsável e janela de data, conforme [`launch/runway-and-phases`](../frameworks/launch/runway-and-phases.md).
6. **Dependências mapeadas.** Como verificar: o que cada fase precisa receber da anterior está listado; nenhuma fase começa sem seu insumo.
7. **Plano de surge.** Como verificar: o memo aponta o pico esperado e quem responde por escala/suporte, conforme [`launch/surge-ops`](../frameworks/launch/surge-ops.md).
8. **Critério de go/no-go.** Como verificar: o memo define a condição que libera a abertura (tech verde, copy aprovada, oferta travada).

## Evidência Exigida
Para marcar ✅: linkar o memo no `decision-registry`, a meta numérica com data (item 1), a matriz papel→dono (item 2), a linha de ad spend com teto rastreada às unit economics (item 3), a reserva da venue (item 4) e a tabela fase→dono→prazo (item 5). O critério de go/no-go (item 8) aparece explícito no topo do memo.

## Protocolo de Falha
Item vermelho → o memo volta ao `launch-producer` com o gap nomeado e **o lançamento não é agendado**. Objetivo vago ou fase sem dono é resolvido antes de qualquer convocação de tropa. Ad spend sem lastro nas unit economics reabre conversa com o `unit-economics-stack-analyst`. Re-entrada: corrigir o memo, atualizar o `decision-registry`, re-submeter. Mudança no objetivo ou na venue reabre as fases dependentes.

## Links
- Gate relacionado: [`launch/launch-phase-readiness-gate`](launch/launch-phase-readiness-gate.md)
- Frameworks: [`launch/product-launch-formula`](../frameworks/launch/product-launch-formula.md) · [`launch/runway-and-phases`](../frameworks/launch/runway-and-phases.md) · [`launch/surge-ops`](../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../data/registries/decision-registry.md) · [`offer-registry`](../data/registries/offer-registry.md)
- Agentes: [`launch-producer`](../agents/launch-producer.md) · [`offerbook-chief`](../agents/offerbook-chief.md) · [`events-logistics-coordinator`](../agents/events-logistics-coordinator.md)
- Checklists vizinhos: [`run-of-show-checklist`](run-of-show-checklist.md) · [`events-logistics-checklist`](events-logistics-checklist.md)
