---
id: checklist.value-equation-checklist
title: "Checklist — Equação de Valor (cada alavanca com ação concreta, zero alavanca órfã)"
type: checklist
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [value-equation, value-equation-engineer/dream-outcome-amplification, value-equation-engineer/likelihood-of-achievement, value-equation-engineer/time-delay-compression, value-equation-engineer/effort-sacrifice-reduction]
registries: [offer-registry]
tags: [checklist, value-equation, alavancas, sonho, probabilidade, tempo, esforco, d2]
---

# Checklist — Equação de Valor

## Propósito
Este checklist prova que a oferta **move as quatro alavancas de valor** com ação concreta, e não com adjetivo. Existe porque valor percebido sobe quando o sonho e a probabilidade sobem e quando tempo e esforço caem — e cada componente da oferta (peça, bônus, garantia, feature) precisa puxar pelo menos uma dessas alavancas. Componente que não move alavanca é peso morto que dilui valor e confunde o cliente. Sem este checklist verde, a oferta acumula itens sem aumentar o desejo. Ele encarna `value_equation_test`: toda peça move ≥1 alavanca, ou sai. É o filtro que separa oferta densa de oferta inchada.

## Dono & Escopo
- **owner_agent:** `value-equation-engineer` (pontua o valor e pode **vetar** componente que não mova alavanca — HARD STOP do componente).
- **Artefato inspecionado:** o `artifact.value-equation-scorecard` e a `decision.lever-assignment`, com os componentes registrados no [`offer-registry`](../data/registries/offer-registry.md).

## Condição de Passagem
As quatro alavancas (sonho, probabilidade, tempo, esforço) têm ação concreta atribuída, cada componente da oferta move ≥1 alavanca, e nenhuma alavanca está órfã nem nenhum componente é peso morto.

## Itens
1. **Sonho amplificado.** Como verificar: a alavanca "resultado dos sonhos" tem ação concreta no scorecard (o que eleva o resultado desejado), conforme `dream-outcome-amplification`.
2. **Probabilidade elevada.** Como verificar: a alavanca "probabilidade de atingir" tem ação concreta (prova, garantia, mecanismo) que sobe a crença, conforme `likelihood-of-achievement`.
3. **Tempo comprimido.** Como verificar: a alavanca "tempo até o resultado" tem ação concreta que encurta a espera, conforme `time-delay-compression`.
4. **Esforço reduzido.** Como verificar: a alavanca "esforço e sacrifício" tem ação concreta que diminui o trabalho do cliente, conforme `effort-sacrifice-reduction`.
5. **Zero alavanca órfã.** Como verificar: as quatro alavancas têm ação listada — nenhuma está vazia ou descrita só com adjetivo.
6. **Cada componente move alavanca.** Como verificar: percorrer a oferta item a item — cada peça/bônus/garantia aponta para a alavanca que move; item sem alavanca é cortado.
7. **Sem inchaço de valor.** Como verificar: nenhum componente repete a mesma função sem somar valor; densidade, não volume.
8. **Sonho sem destruir probabilidade.** Como verificar: nenhuma ação infla o sonho derrubando a credibilidade — o `value-equation-engineer` veta a promessa que baixa a probabilidade percebida.

## Evidência Exigida
Para marcar ✅: linkar o `value-equation-scorecard` com a ação concreta de cada uma das quatro alavancas (itens 1–4), o mapa componente→alavanca no `offer-registry` sem órfãos (itens 5–6) e a nota de veto/aprovação por componente (item 8). A densidade aparece no scorecard como ausência de itens redundantes (item 7).

## Protocolo de Falha
Item vermelho → o scorecard volta ao `value-equation-engineer` e o componente sem alavanca é **vetado** (sai da oferta) — este é o HARD STOP do componente. Alavanca órfã reabre o desenho da oferta. Re-entrada: atribuir ação à alavanca ou cortar o componente, atualizar o `offer-registry`, re-submeter. Mudança de componente reabre os checklists downstream (preço, money model) que dependem do valor.

## Links
- Frameworks: [`value-equation`](../frameworks/value-equation.md) · [`dream-outcome-amplification`](../frameworks/value-equation-engineer/dream-outcome-amplification.md) · [`likelihood-of-achievement`](../frameworks/value-equation-engineer/likelihood-of-achievement.md) · [`time-delay-compression`](../frameworks/value-equation-engineer/time-delay-compression.md) · [`effort-sacrifice-reduction`](../frameworks/value-equation-engineer/effort-sacrifice-reduction.md)
- Registries: [`offer-registry`](../data/registries/offer-registry.md)
- Agentes: [`value-equation-engineer`](../agents/value-equation-engineer.md) · [`mechanism-architect`](../agents/mechanism-architect.md) · [`money-model-designer`](../agents/money-model-designer.md)
- Gate por agente: [`value/value-no-orphan-lever-gate`](value/value-no-orphan-lever-gate.md)
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate relacionado: [`offer-book-stack/offer-architecture-gate`](offer-book-stack/offer-architecture-gate.md)
