---
id: checklist.mailer.mailer-offer-coherence-gate
title: "Gate — Coerência da Oferta (gancho, stack e prova batem com a Big Idea e o lead travado)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: direct-mail-insert-writer
frameworks: [offer-stack-builder, scarcity-urgency-engine]
registries: [control-registry, proof-registry, objection-registry]
tags: [gate, mailer, coerencia, big-idea, lead, stack, prova, d4]
---

# Gate — Coerência da Oferta

## Propósito
Este gate prova que **a peça física é fiel à estratégia a montante**: o gancho da frente nasce do lead travado, a oferta resumida condensa o offer-stack aprovado, a garantia reaparece e cada claim impresso tem lastro de prova. Ele existe porque o espaço físico é pequeno e tenta cortar caminho — um gancho que foge do lead, uma oferta inventada no papel ou uma promessa sem prova quebram a congruência com a Big Idea e enganam quem abre o envelope. O `direct-mail-insert-writer` não desenha a oferta: ele **materializa** a que foi aprovada no Offer Book. Vale o princípio `coherence_before_eloquence`: a peça repete a estratégia, não cria uma nova. O gancho casa com a consciência do avatar, a oferta resumida usa o [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) e cada prova vem do `proof-registry`. Este gate julga **só a fidelidade ao Offer Book** — se a urgência impressa é verdadeira e se há claim sem lastro é do `mailer-compliance-gate`, se o insert está no degrau certo é do `mailer-insert-fit-gate`, e se o QR rastreia é do `mailer-cta-trackable-gate`. Claim sem prova reprova aqui: o writer sinaliza ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) e não imprime promessa sem lastro.

## Dono & Escopo
- **owner_agent:** `direct-mail-insert-writer` (garante que a peça é fiel à Big Idea, ao lead travado e ao offer-stack aprovado).
- **Artefato inspecionado:** os campos `gancho_frente`, `oferta_resumida`, `objecao_alvo` e a prova de cada peça em `artifact.mailers-inserts`, cruzados com `artifact.big-idea`, `decision.lead-type-locked` e `artifact.offer-stack`, registrados no [`control-registry`](../../data/registries/control-registry.md). Toda saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md), que tem veto de voz.

## Condição de Passagem
Cada peça abre pelo lead travado, condensa o offer-stack aprovado, traz a garantia e só carrega claims com prova registrada.

## Itens
1. **Gancho do lead.** Verificar: o gancho da frente nasce do lead travado e casa com a consciência do avatar, sem inventar um novo ângulo.
2. **Congruência com a Big Idea.** Verificar: a peça reforça a Big Idea aprovada, não a contradiz nem a substitui.
3. **Oferta fiel ao stack.** Verificar: a oferta resumida condensa o offer-stack aprovado, sem adicionar componentes inexistentes.
4. **Garantia presente.** Verificar: a reversão de risco (garantia) aprovada reaparece na peça quando cabe.
5. **Claim com prova.** Verificar: cada claim impresso tem prova correspondente no `proof-registry`.
6. **Objeção do degrau respondida.** Verificar: a peça responde a objeção dominante lida do `objection-registry`.

## Evidência Exigida
Para marcar ✅: linkar, por peça, os campos `gancho_frente`, `oferta_resumida` e `objecao_alvo` no [`control-registry`](../../data/registries/control-registry.md), cruzados com a `big-idea`, o lead travado e o `offer-stack`. Cada claim aponta para o `proof-ref` no [`proof-registry`](../../data/registries/proof-registry.md); a objeção aponta para o [`objection-registry`](../../data/registries/objection-registry.md).

## Protocolo de Falha
Item vermelho → o `direct-mail-insert-writer` **realinha a peça à estratégia aprovada**: gancho fora do lead ele reescreve dentro do lead travado; oferta inventada ele corta para o offer-stack real. Claim sem prova ele **não imprime** e sinaliza ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). Sem lead travado, ele devolve ao [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md). O writer **não tem veto**; toda saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md), que reprova a voz, e escalona ao [`offerbook-chief`](../../agents/offerbook-chief.md). Se a urgência impressa é falsa é do [`mailer-compliance-gate`](mailer-compliance-gate.md). Re-entrada: realinhar gancho e oferta, anexar a prova e re-submeter ao control-registry.

## Links
- Frameworks: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md) · [`objection-registry`](../../data/registries/objection-registry.md)
- Agentes: [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md) · [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`mailer-spec-gate`](mailer-spec-gate.md) · [`mailer-insert-fit-gate`](mailer-insert-fit-gate.md) · [`mailer-cta-trackable-gate`](mailer-cta-trackable-gate.md) · [`mailer-compliance-gate`](mailer-compliance-gate.md)
