---
id: checklist.blackbook-stack.blackbook-dod-gate
title: "★ Gate — Definition of Done do Blackbook (copy + funil + ops + growth + compliance)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [offer-to-funnel-mapping, proof-to-claim-chain, scarcity-urgency-engine, money-model-sequence]
registries: [offer-registry, control-registry, decision-registry, claim-registry, proof-registry, lessons-learned-registry]
tags: [gate, blackbook, dod, compliance, d7, aggregator, final-barrier]
---

# ★ Gate — Definition of Done do Blackbook

## Propósito
Este gate prova que o **Launch Blackbook está pronto para execução ponta-a-ponta**. É a última barreira antes do lançamento ir ao ar. Existe porque um lançamento só é confiável quando estratégia, copy, funil, logística e growth fecham juntos — e quando o `compliance-auditor` confirma que nada engana o cliente. Ele **agrega** os quatro gates de D4–D6 — [`copy-coverage-gate`](copy-coverage-gate.md), [`funnel-tech-gate`](funnel-tech-gate.md), [`ops-events-gate`](ops-events-gate.md) e [`growth-affiliate-pr-gate`](growth-affiliate-pr-gate.md) — e adiciona a auditoria final de compliance. Pressupõe o HARD STOP a montante: o [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) já está verde.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (a última barreira; pode **vetar** qualquer claim sem lastro ou escassez falsa); o `offerbook-chief` co-assina a entrega final e o `knowledge-librarian` registra a memória.
- **Artefato inspecionado:** o **Launch Blackbook consolidado** (`templates/core/launch-blackbook-skeleton` preenchido), agregando [`offer-registry`](../../data/registries/offer-registry.md), [`control-registry`](../../data/registries/control-registry.md) e [`decision-registry`](../../data/registries/decision-registry.md), via a task `assemble-blackbook`.

## Condição de Passagem
Os quatro gates D4–D6 estão verdes, a auditoria de compliance passou (claims com lastro, escassez verdadeira, T&Cs/disclaimers/LGPD/FTC), e o Blackbook consolidado existe sem lacuna — logo o lançamento pode ir ao ar.

## Itens
1. **Copy completa e na voz.** Verificar: [`copy-coverage-gate`](copy-coverage-gate.md) marcado ✅ (todos os degraus + voz aprovada).
2. **Funil e tech prontos.** Verificar: [`funnel-tech-gate`](funnel-tech-gate.md) marcado ✅ (mapa + URLs + load test + deliverability).
3. **Ops e eventos prontos.** Verificar: [`ops-events-gate`](ops-events-gate.md) marcado ✅ (run-of-show + entregáveis com dono/hosting/data).
4. **Growth pronto.** Verificar: [`growth-affiliate-pr-gate`](growth-affiliate-pr-gate.md) marcado ✅ (afiliados + PR).
5. **Claims com lastro (auditoria final).** Verificar: o `compliance-auditor` re-confere todo `claim_id` contra `proof_id`; zero órfão.
6. **Escassez verdadeira (auditoria final).** Verificar: cada gatilho de escassez/urgência aponta para limite real; escassez falsa = veto.
7. **T&Cs, disclaimers e privacidade.** Verificar: termos, isenções e base legal (LGPD/FTC) presentes e corretos nas peças e páginas.
8. **Blackbook consolidado existe.** Verificar: o documento-mestre está completo, sem seção em branco, com todos os links resolvendo.
9. **Memória atualizada.** Verificar: o `knowledge-librarian` registrou controles e lições no `lessons-learned-registry`.

## Evidência Exigida
Para marcar ✅: linkar os quatro gates upstream verdes (itens 1–4), o relatório de auditoria de compliance com a tabela claim→proof e o checklist de escassez (itens 5–6), os T&Cs/disclaimers/privacidade aprovados (item 7), o Blackbook consolidado completo (item 8) e as entradas de memória (item 9). A assinatura conjunta `compliance-auditor` + `offerbook-chief` é gravada no `decision-registry`.

## Protocolo de Falha
Qualquer item vermelho mantém o gate fechado e o lançamento **não vai ao ar**: o `compliance-auditor` devolve ao gate/agente dono (copy/funil/ops/growth) com o defeito nomeado. Claim sem lastro ou escassez falsa é **veto** — não há override por prazo. Re-entrada: o gate que falhou volta ao seu agente, corrige, atualiza o registry e re-submete a este gate. Mudança em qualquer insumo reabre este gate.

## Links
- Gates agregados: [`copy-coverage-gate`](copy-coverage-gate.md) · [`funnel-tech-gate`](funnel-tech-gate.md) · [`ops-events-gate`](ops-events-gate.md) · [`growth-affiliate-pr-gate`](growth-affiliate-pr-gate.md)
- Pré-requisito (HARD STOP): [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`money-model-sequence`](../../frameworks/money-model-sequence.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`control-registry`](../../data/registries/control-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md) · [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md)
- Agentes: [`compliance-auditor`](../../agents/compliance-auditor.md) · [`offerbook-chief`](../../agents/offerbook-chief.md) · [`knowledge-librarian`](../../agents/knowledge-librarian.md)
