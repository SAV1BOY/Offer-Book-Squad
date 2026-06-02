---
id: checklist.mailer.mailer-compliance-gate
title: "Gate — Compliance da Peça (urgência impressa é real e nenhum claim vai sem lastro)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: direct-mail-insert-writer
frameworks: [scarcity-urgency-engine, offer-stack-builder]
registries: [control-registry, proof-registry]
tags: [gate, mailer, compliance, urgencia-real, escassez, claim, lastro, d4]
---

# Gate — Compliance da Peça

## Propósito
Este gate prova que **toda urgência impressa é verdadeira e nenhum claim vai ao papel sem lastro**: uma data de save-the-date que existe, uma validade de insert real, um "últimas vagas" que bate com o inventário. Ele existe porque papel postado não se corrige — um "última chance" falso ou uma promessa sem prova viram um problema permanente na caixa de correio do cliente e um veto certo. O `direct-mail-insert-writer` não imprime deadline falso nem claim solto; toda escassez impressa aponta para uma data ou um limite real. Vale o princípio `contradiction_before_conclusion`: antes de mandar à gráfica, o writer pergunta "esta urgência é verdadeira?". O veto de escassez falsa e de claim sem prova é do [`compliance-auditor`](../../agents/compliance-auditor.md), e não tem override. Este gate julga **só a honestidade da peça** — a urgência e o claim — separado do `mailer-offer-coherence-gate`, que cuida da fidelidade do gancho e do stack à estratégia. A escassez impressa que depende de inventário de evento cruza com o tracker do [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md). Urgência falsa ou claim sem prova reprovam aqui: o writer remove ou realinha antes do envio.

## Dono & Escopo
- **owner_agent:** `direct-mail-insert-writer` (garante que a urgência impressa é real e que cada claim tem lastro).
- **Artefato inspecionado:** o campo `urgencia_real` e os claims de cada peça em `artifact.mailers-inserts`, cruzados com o `proof-registry` e, quando a escassez é de vagas/lotes, com o inventory tracker do `events-logistics`. Registrado no [`control-registry`](../../data/registries/control-registry.md). O veto de escassez falsa é do [`compliance-auditor`](../../agents/compliance-auditor.md).

## Condição de Passagem
Cada urgência ou escassez impressa aponta para uma data ou um limite real, e nenhum claim vai à gráfica sem prova registrada.

## Itens
1. **Urgência real.** Verificar: todo prazo/data impresso (save-the-date, validade) corresponde a uma data que existe de verdade.
2. **Escassez ancorada.** Verificar: todo "últimas N vagas/lotes" impresso bate com um número real no inventory tracker.
3. **Sem urgência falsa.** Verificar: não há "última chance" ou contagem inventada sem evento real por trás.
4. **Claim com lastro.** Verificar: cada afirmação de resultado/benefício tem prova no `proof-registry`.
5. **Sem promessa irreal.** Verificar: a peça não promete o que a oferta aprovada não entrega.
6. **Pronto para o compliance.** Verificar: a peça está em condição de passar pela auditoria do `compliance-auditor` sem veto.

## Evidência Exigida
Para marcar ✅: linkar, por peça, o campo `urgencia_real` no [`control-registry`](../../data/registries/control-registry.md) apontando para a data/limite verdadeiro, e cada claim ao `proof-ref` no [`proof-registry`](../../data/registries/proof-registry.md). Quando a escassez é de vagas/lotes, fica citado o número real no inventory tracker do [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md).

## Protocolo de Falha
Item vermelho → o `direct-mail-insert-writer` **remove ou realinha a urgência a uma data verdadeira** antes da gráfica — papel postado não se corrige. Escassez que não bate com o inventário ele suspende e sinaliza ao [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md). Claim sem prova ele **não imprime** e sinaliza ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). Qualquer urgência apresentada como escassez falsa é **vetada** pelo [`compliance-auditor`](../../agents/compliance-auditor.md) — não tem override. O writer **não tem veto**; escalona ao [`offerbook-chief`](../../agents/offerbook-chief.md). Se o problema é o gancho ou o stack fora da estratégia é do [`mailer-offer-coherence-gate`](mailer-offer-coherence-gate.md). Re-entrada: realinhar a urgência a uma data real, anexar a prova e re-submeter ao control-registry.

## Links
- Frameworks: [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`offer-stack-builder`](../../frameworks/offer-stack-builder.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md)
- Agentes: [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`mailer-spec-gate`](mailer-spec-gate.md) · [`mailer-insert-fit-gate`](mailer-insert-fit-gate.md) · [`mailer-cta-trackable-gate`](mailer-cta-trackable-gate.md) · [`mailer-offer-coherence-gate`](mailer-offer-coherence-gate.md)
