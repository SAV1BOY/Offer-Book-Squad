---
id: checklist.blackbook-stack.copy-coverage-gate
title: "Gate — Cobertura de Copy (todos os degraus + voz aprovada)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [offer-to-funnel-mapping, vsl-structure, email-sequence-architecture, hook-frameworks, proof-to-claim-chain]
registries: [control-registry, claim-registry, swipe-registry]
tags: [gate, copy, coverage, voice, d4, d7, dod-input]
---

# Gate — Cobertura de Copy

## Propósito
Este gate prova que **toda peça de copy exigida pelo money model existe e passou na voz**. Ele existe porque um lançamento falha quando um degrau da escada fica sem copy: um upsell sem script, um carrinho sem sequência de fechamento, um anúncio sem ângulo. Cada degrau do money model precisa de copy que mova ≥1 alavanca de valor (`value_equation_test`) e que soe na voz da marca. É o primeiro insumo do [`blackbook-dod-gate`](blackbook-dod-gate.md): sem copy completa e na voz, o Blackbook não fecha.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (audita cobertura e lastro); o `voice-style-guardian` co-assina a voz e pode **vetar** qualquer peça fora de tom.
- **Artefato inspecionado:** o conjunto de copy registrado no [`control-registry`](../../data/registries/control-registry.md) — VSL/webinar, sequências de email/SMS, mailers/inserts e a matriz de anúncios — produzido em D4 por `vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `direct-mail-insert-writer` e `ad-creative-factory`.

## Condição de Passagem
Cada degrau do money model tem todas as peças de copy exigidas, cada peça move ≥1 alavanca de valor, e todas passaram na revisão de voz do `voice-style-guardian`.

## Itens
1. **HARD STOP verde.** Verificar: o [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) está ✅ — nenhuma copy é avaliada antes disso.
2. **VSL/webinar presente.** Verificar: script no `control-registry` com valor antes do preço, reversão de risco e CTA forte.
3. **Sequências de email/SMS completas.** Verificar: cada etapa (abertura→fechamento de carrinho→recuperação) existe, com segmentação e timing.
4. **Mailers/inserts (se no escopo).** Verificar: cada peça impressa exigida pelo funil existe ou está marcada `não-aplicável` com motivo.
5. **Matriz de anúncios cobre ângulos.** Verificar: ≥1 variação por ângulo/tipo de lead, cada uma com claim lastreado.
6. **Cobertura por degrau.** Verificar: cruzar a escada do money model contra o `control-registry` — zero degrau sem a copy que ele exige.
7. **Voz aprovada.** Verificar: cada peça tem o selo de revisão do `voice-style-guardian` (3ª série, voz ativa, presente, sem jargão).
8. **Claims lastreados.** Verificar: todo claim usado em copy tem `proof_id` no `claim-registry`.

## Evidência Exigida
Para marcar ✅: linkar cada peça no `control-registry` (itens 2–5), a tabela degrau→peça sem buracos (item 6), o registro de aprovação de voz (item 7) e a tabela claim→proof (item 8). Peças reutilizadas de swipe apontam para o `swipe-registry`.

## Protocolo de Falha
Item vermelho → o `compliance-auditor` devolve à célula de copy (D4) com a peça faltante ou o claim órfão nomeado e **não libera o blackbook-dod-gate**. Peça fora de voz volta ao `voice-style-guardian` e ao autor. Re-entrada: o agente de copy escreve/corrige, o guardião re-aprova, atualiza-se o `control-registry` e re-submete. Degrau novo no money model reabre este gate.

## Links
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`vsl-structure`](../../frameworks/copy/vsl-structure.md) · [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md) · [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md) · [`swipe-registry`](../../data/registries/swipe-registry.md)
- Agentes: [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) · [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) · [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md) · [`ad-creative-factory`](../../agents/ad-creative-factory.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) · Agrega para: [`blackbook-dod-gate`](blackbook-dod-gate.md)
