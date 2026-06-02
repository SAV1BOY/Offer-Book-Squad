---
id: checklist.events-logistics-checklist
title: "Checklist — Logística de Eventos (todo entregável com dono/hosting/data)"
type: checklist
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: events-logistics-coordinator
frameworks: [money-model-sequence, launch/runway-and-phases]
registries: [offer-registry, decision-registry]
tags: [checklist, eventos, logistica, entregavel, dono, hosting, data, d6]
---

# Checklist — Logística de Eventos

## Propósito
Este checklist prova que **todo entregável de evento tem dono, hospedagem e data** — nada fica órfão. Existe porque logística é onde lançamento trava no detalhe: o vídeo de aquecimento sem onde ser hospedado, o e-mail de lembrete sem dono, a página de inscrição sem data de publicação. Um entregável sem responsável é um entregável que não acontece. Um sem hosting é um que não está no ar. Um sem data é um que atrasa. O coordenador transforma o plano em um inventário rastreável. Sem este checklist verde, o evento chega com furos. Ele garante `traceability_before_eloquence` na operação: cada peça tem nome de dono, lugar de hospedagem e data de entrega — visível num só inventário.

## Dono & Escopo
- **owner_agent:** `events-logistics-coordinator` (mantém o inventário e responde pela entrega); o [`launch-producer`](../agents/launch-producer.md) define as fases e o [`tech-links-deliverability-engineer`](../agents/tech-links-deliverability-engineer.md) confirma o hosting técnico.
- **Artefato inspecionado:** o **inventário de ativos e calendário de eventos** (`templates/ops/asset-inventory-tracker-template` e `templates/ops/events-calendar-template` preenchidos), registrados no [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
Cada entregável de evento aparece no inventário com dono, local de hospedagem e data de entrega — zero linha sem um desses três campos.

## Itens
1. **Inventário completo.** Como verificar: cada peça do evento (vídeos, páginas, e-mails, slides, ativos de afiliado) tem uma linha no inventário; nada de peça citada e não listada.
2. **Dono por entregável.** Como verificar: toda linha tem um nome responsável; nenhuma fica "a definir".
3. **Hosting por entregável.** Como verificar: cada peça declara onde será hospedada/publicada (plataforma, URL, repositório).
4. **Data por entregável.** Como verificar: cada linha tem data de entrega coerente com a fase do lançamento, conforme [`launch/runway-and-phases`](../frameworks/launch/runway-and-phases.md).
5. **Casamento com o money model.** Como verificar: ativos ligados a uma oferta apontam o degrau correto do [`offer-registry`](../data/registries/offer-registry.md), conforme [`money-model-sequence`](../frameworks/money-model-sequence.md).
6. **Dependências e ordem.** Como verificar: peças que dependem de outra (ex.: e-mail que linka uma página) têm a dependência marcada e datas coerentes.
7. **Status rastreável.** Como verificar: cada linha tem status (a fazer/em produção/pronto) atualizável.
8. **Backup e acesso.** Como verificar: ativos críticos têm cópia de segurança e os donos têm acesso de edição/publicação.

## Evidência Exigida
Para marcar ✅: linkar o inventário no `decision-registry`, a verificação de que cada peça citada no plano tem linha (item 1) e a varredura das colunas dono/hosting/data sem campo vazio (itens 2–4). O calendário com datas coerentes às fases (item 4) e o mapa de dependências (item 6) ficam linkados. O casamento ativo→degrau (item 5) aponta o `offer-registry`.

## Protocolo de Falha
Item vermelho → o inventário volta ao `events-logistics-coordinator` com a linha incompleta nomeada e **a fase não é dada como pronta**. Entregável sem dono ganha um responsável antes de seguir. Sem hosting reabre conversa com o `tech-links-deliverability-engineer`. Sem data reabre conversa com o `launch-producer`. Re-entrada: completar a linha, atualizar o `decision-registry`, re-submeter. Mudança nas fases do launch memo reabre as datas afetadas.

## Links
- Frameworks: [`money-model-sequence`](../frameworks/money-model-sequence.md) · [`launch/runway-and-phases`](../frameworks/launch/runway-and-phases.md)
- Registries: [`offer-registry`](../data/registries/offer-registry.md) · [`decision-registry`](../data/registries/decision-registry.md)
- Agentes: [`events-logistics-coordinator`](../agents/events-logistics-coordinator.md) · [`launch-producer`](../agents/launch-producer.md) · [`tech-links-deliverability-engineer`](../agents/tech-links-deliverability-engineer.md)
- Checklists vizinhos: [`launch-memo-checklist`](launch-memo-checklist.md) · [`run-of-show-checklist`](run-of-show-checklist.md) · [`affiliate-program-checklist`](affiliate-program-checklist.md)
