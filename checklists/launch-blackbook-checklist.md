---
id: checklist.launch-blackbook-checklist
title: "Checklist — Definition of Done do Launch Blackbook (completo)"
type: checklist
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [offer-to-funnel-mapping, proof-to-claim-chain, scarcity-urgency-engine]
registries: [offer-registry, control-registry, decision-registry, claim-registry, lessons-learned-registry]
tags: [checklist, blackbook, dod, d7, aggregator, final-delivery]
---

# Checklist — Definition of Done do Launch Blackbook

## Propósito
Este checklist prova que o **Launch Blackbook está completo** — o pacote de execução ponta-a-ponta que qualquer equipe consegue rodar sem o autor presente. Existe porque um lançamento morre nos buracos: um degrau sem copy, um funil com beco sem saída, uma logística sem fallback, um claim sem lastro. Ele **agrega** D4 (copy), D5 (funil/tech), D6 (ops/eventos/afiliados/PR) e D7 (compliance/memória) sobre a fundação já travada do Offer Book. Só fecha quando cada domínio passou no seu gate e a memória reutilizável foi registrada. É o último portão antes da entrega.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (última barreira; pode vetar claim sem lastro ou escassez falsa); o `offerbook-chief` co-assina a definição de pronto e o `knowledge-librarian` confirma a memória.
- **Artefato inspecionado:** o **Launch Blackbook consolidado** (`templates/core/launch-blackbook-skeleton` preenchido), que reúne copy ([`control-registry`](../data/registries/control-registry.md)), funil, ops e as decisões do [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
O Offer Book está travado, copy/funil/ops/growth passaram nos seus gates, compliance está verde, a memória foi registrada — e o Blackbook consolidado existe sem seção em branco.

## Itens
1. **HARD STOP verde.** Como verificar: o [`offer-book-checklist`](offer-book-checklist.md) está ✅ — nada de Blackbook sem a fundação travada.
2. **VSL/webinar pronto.** Como verificar: o [`vsl-script-checklist`](vsl-script-checklist.md) e o [`webinar-checklist`](webinar-checklist.md) (se no escopo) estão ✅.
3. **Sequências de email/SMS prontas.** Como verificar: o [`email-sequence-checklist`](email-sequence-checklist.md) e o [`sms-checklist`](sms-checklist.md) estão ✅.
4. **Cobertura de copy por degrau.** Como verificar: o gate [`blackbook-stack/copy-coverage-gate`](blackbook-stack/copy-coverage-gate.md) está ✅ — zero degrau do money model sem copy.
5. **Funil sem beco sem saída.** Como verificar: o gate [`blackbook-stack/funnel-tech-gate`](blackbook-stack/funnel-tech-gate.md) está ✅ (cada página tem próximo passo + backend).
6. **Ops e eventos com run-of-show.** Como verificar: run-of-show e calendário existem no `decision-registry`, cada fase com responsável e horário.
7. **Afiliados e PR (se no escopo).** Como verificar: programa de afiliados e plano de PR existem ou estão marcados `não-aplicável` com motivo.
8. **Escassez 100% verdadeira na execução.** Como verificar: cada prazo/limite usado em copy e funil aponta para restrição real; o `compliance-auditor` confirma — falsa = veto.
9. **Compliance verde.** Como verificar: T&Cs, disclaimers e LGPD/FTC presentes; nenhum claim usado em copy está órfão no `claim-registry`.
10. **Memória registrada.** Como verificar: controles vencedores no `control-registry`, swipes reutilizáveis no `swipe-registry` e lições no [`lessons-learned-registry`](../data/registries/lessons-learned-registry.md).
11. **Blackbook consolidado existe.** Como verificar: o skeleton preenchido está completo, navegável e sem seção em branco.

## Evidência Exigida
Para marcar ✅: linkar o `offer-book-checklist` verde (item 1), cada checklist e gate de domínio verde (itens 2–7), a confirmação de escassez e compliance do `compliance-auditor` (itens 8–9), os registros de memória (item 10) e o Blackbook consolidado completo (item 11). A assinatura conjunta `compliance-auditor` + `offerbook-chief` é gravada no `decision-registry`.

## Protocolo de Falha
Item vermelho → o `compliance-auditor` **não libera a entrega** e nomeia o defeito (peça faltante, beco no funil, claim órfão, escassez falsa). Re-entrada: o domínio que falhou volta ao seu agente dono (D4/D5/D6/D7) com o item nomeado; após correção e atualização do registry, re-submete-se. Veto de compliance é absoluto — só humano sênior reverte, com decisão gravada no `decision-registry`. Mudança no Offer Book reabre este checklist por inteiro.

## Links
- Gate-espelho: [`blackbook-stack/blackbook-dod-gate`](blackbook-stack/blackbook-dod-gate.md)
- Checklists agregados: [`offer-book-checklist`](offer-book-checklist.md) · [`vsl-script-checklist`](vsl-script-checklist.md) · [`webinar-checklist`](webinar-checklist.md) · [`email-sequence-checklist`](email-sequence-checklist.md) · [`sms-checklist`](sms-checklist.md)
- Gates de domínio: [`blackbook-stack/copy-coverage-gate`](blackbook-stack/copy-coverage-gate.md) · [`blackbook-stack/funnel-tech-gate`](blackbook-stack/funnel-tech-gate.md)
- Frameworks: [`offer-to-funnel-mapping`](../frameworks/offer-to-funnel-mapping.md) · [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md) · [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md)
- Registries: [`control-registry`](../data/registries/control-registry.md) · [`decision-registry`](../data/registries/decision-registry.md) · [`claim-registry`](../data/registries/claim-registry.md) · [`lessons-learned-registry`](../data/registries/lessons-learned-registry.md)
- Agentes: [`compliance-auditor`](../agents/compliance-auditor.md) · [`offerbook-chief`](../agents/offerbook-chief.md) · [`knowledge-librarian`](../agents/knowledge-librarian.md)
