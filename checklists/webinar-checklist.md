---
id: checklist.webinar-checklist
title: "Checklist — Webinar (3 blocos, conteúdo grátis → oferta paga → urgência)"
type: checklist
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [launch/perfect-webinar, copy/vsl-structure, copy/pastor]
registries: [control-registry, proof-registry, objection-registry]
tags: [checklist, copy, webinar, perfect-webinar, urgencia, d4]
---

# Checklist — Webinar

## Propósito
Este checklist prova que o roteiro de webinar tem os **três blocos** na ordem que vende: conteúdo grátis que entrega valor real, transição para a oferta paga e fechamento com urgência verdadeira. Existe porque um webinar que ensina e nunca vende deixa dinheiro na mesa, e um que vende sem ensinar perde a sala. O conteúdo grátis quebra as falsas crenças que travam a compra; a oferta segue na sequência natural; a urgência fecha com prazo real. Sem este checklist verde, o webinar vira aula sem conversão ou pitch sem valor. Ele só nasce com o HARD STOP liberado e executa a Big Idea travada ao vivo. É a peça de copy de maior alavancagem em lançamentos por evento.

## Dono & Escopo
- **owner_agent:** `vsl-webinar-scriptwriter` (escreve o roteiro do webinar); o [`voice-style-guardian`](../agents/voice-style-guardian.md) co-assina a voz.
- **Artefato inspecionado:** o `artifact.webinar-script` (e o `artifact.recap-vsl` derivado), registrado no [`control-registry`](../data/registries/control-registry.md), sustentado pelo [`proof-registry`](../data/registries/proof-registry.md) e pelo [`objection-registry`](../data/registries/objection-registry.md).

## Condição de Passagem
O roteiro tem os 3 blocos sequenciados (conteúdo grátis → oferta paga → urgência), quebra as falsas crenças no bloco grátis, fecha com urgência verdadeira e CTA único — e a voz está aprovada.

## Itens
1. **HARD STOP liberado.** Como verificar: o [`offer-book-checklist`](offer-book-checklist.md) está ✅ — sem ele, o roteiro não nasce.
2. **Bloco 1 — conteúdo grátis.** Como verificar: o primeiro bloco entrega valor real e ensinável, não um teaser vazio, conforme `perfect-webinar`.
3. **Falsas crenças quebradas.** Como verificar: o bloco grátis derruba as 3 falsas crenças centrais (no veículo, em si, nas circunstâncias) mapeadas no `objection-registry`.
4. **Bloco 2 — oferta paga.** Como verificar: a transição do conteúdo para a oferta é natural e a oferta aparece com mecanismo, stack e valor antes do preço.
5. **Bloco 3 — urgência.** Como verificar: o fechamento traz urgência verdadeira (prazo/bônus/vagas reais), conforme `perfect-webinar`.
6. **Valor antes do preço.** Como verificar: ler o roteiro — desejo e prova vêm antes do número, conforme `vsl-structure` e `pastor`.
7. **Prova ancorada.** Como verificar: cada claim forte aponta para um `proof_id` no `proof-registry`.
8. **CTA único por bloco de fechamento.** Como verificar: o fechamento tem UMA chamada clara, com o próximo passo óbvio.
9. **Escassez verdadeira.** Como verificar: o prazo/limite da urgência é real e rastreável; escassez falsa = veto do `compliance-auditor`.
10. **Voz aprovada.** Como verificar: o `voice-style-guardian` deu `voice-verdict` APROVADO.

## Evidência Exigida
Para marcar ✅: linkar o roteiro no `control-registry`, o mapa dos 3 blocos (itens 2, 4, 5), a tabela das 3 falsas crenças quebradas com origem no `objection-registry` (item 3), a tabela claim→proof (item 7), o limite real da urgência (item 9) e o `voice-verdict` APROVADO (item 10).

## Protocolo de Falha
Item vermelho → o roteiro volta ao `vsl-webinar-scriptwriter` com o defeito nomeado e **não vai ao ar**. Bloco grátis vazio, preço antes do valor ou urgência falsa reabre o roteiro; claim órfão e escassez falsa acionam veto do `compliance-auditor`. Re-entrada: reescrever o bloco, atualizar o `control-registry`, re-submeter. Mudança na oferta ou na Big Idea reabre este checklist.

## Links
- Frameworks: [`perfect-webinar`](../frameworks/launch/perfect-webinar.md) · [`vsl-structure`](../frameworks/copy/vsl-structure.md) · [`pastor`](../frameworks/copy/pastor.md)
- Registries: [`control-registry`](../data/registries/control-registry.md) · [`proof-registry`](../data/registries/proof-registry.md) · [`objection-registry`](../data/registries/objection-registry.md)
- Agentes: [`vsl-webinar-scriptwriter`](../agents/vsl-webinar-scriptwriter.md) · [`voice-style-guardian`](../agents/voice-style-guardian.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Gates relacionados: [`vsl/vsl-value-before-price-gate`](vsl/vsl-value-before-price-gate.md) · [`vsl/vsl-cta-strength-gate`](vsl/vsl-cta-strength-gate.md)
- Checklists vizinhos: [`vsl-script-checklist`](vsl-script-checklist.md) · Agrega para: [`launch-blackbook-checklist`](launch-blackbook-checklist.md)
