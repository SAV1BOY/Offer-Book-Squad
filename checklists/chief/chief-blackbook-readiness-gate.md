---
id: checklist.chief.chief-blackbook-readiness-gate
title: "Gate — Launch Blackbook Pronto para Consolidação (chief co-assina a memória do lançamento)"
type: gate
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [offer-to-funnel-mapping, money-model-sequence, proof-to-claim-chain]
registries: [offer-registry, control-registry, decision-registry, lessons-learned-registry]
tags: [gate, chief, blackbook, readiness, d0, co-assinatura, memoria]
---

# Gate — Launch Blackbook Pronto para Consolidação

## Propósito
Este gate prova que o `offerbook-chief` recebeu todos os artefatos de execução (copy, funil, ops, eventos, afiliados, PR) completos e auditados antes de co-assinar o **Launch Blackbook** — o entregável final que vira memória do squad. Existe porque o Blackbook é o ativo reutilizável: se ele sai com lacunas, o próximo lançamento herda o buraco. Enquanto o agregador [`blackbook-dod-gate`](../blackbook-stack/blackbook-dod-gate.md) soma os gates de D4–D7, este gate é a checagem de comando — o chief confirma que cada degrau do money model tem copy, página e sequência mapeadas, que o compliance passou, e que o `knowledge-librarian` tem o que registrar. É o ponto onde o lançamento vira conhecimento travado.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (co-assina, junto do `compliance-auditor`, a consolidação do Blackbook).
- **Artefato inspecionado:** o **pacote de Launch Blackbook** consolidado a partir de [`control-registry`](../../data/registries/control-registry.md), [`offer-registry`](../../data/registries/offer-registry.md) e [`decision-registry`](../../data/registries/decision-registry.md), via a task `assemble-blackbook`, com o `core/launch-blackbook-skeleton` preenchido.

## Condição de Passagem
Todos os artefatos de execução (D4–D7) chegaram completos e auditados ao chief, cada degrau do money model está mapeado a copy/funil/ops, e o chief confirma que pode co-assinar a consolidação do Blackbook.

## Itens
1. **Copy completa recebida.** Verificar: VSL/webinar, sequências de e-mail/SMS, mailers e matriz de anúncios chegaram e estão linkados no [`control-registry`](../../data/registries/control-registry.md), cada peça aprovada pelo `voice-style-guardian`.
2. **Funil e tech recebidos.** Verificar: o mapa de funil não tem becos sem saída e as URLs/deliverability estão registradas, conforme [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md).
3. **Ops e growth recebidos.** Verificar: run-of-show, logística de eventos, programa de afiliados e plano de PR estão presentes e linkados.
4. **Cada degrau mapeado.** Verificar: cada parte do money model tem copy, página e sequência correspondentes — nenhum degrau órfão sem ativo de execução.
5. **Compliance passou.** Verificar: o `compliance-auditor` carimbou claims com lastro, escassez verdadeira e LGPD/FTC conformes, sem veto pendente.
6. **Lições prontas para registro.** Verificar: o `knowledge-librarian` tem controles vencedores, swipes e lições para gravar em [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md).
7. **Pronto para o agregador.** Verificar: o chief confirma que os gates D4–D7 estão verdes para o [`blackbook-dod-gate`](../blackbook-stack/blackbook-dod-gate.md) virar.

## Evidência Exigida
Para marcar cada item ✅, linkar as linhas do [`control-registry`](../../data/registries/control-registry.md) (copy/controles, itens 1 e 4), o mapa de funil e a tabela de URLs (item 2), os artefatos de ops/growth (item 3), o carimbo do `compliance-auditor` (item 5) e as entradas candidatas de [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) (item 6). A co-assinatura `offerbook-chief` + `compliance-auditor` é gravada no [`decision-registry`](../../data/registries/decision-registry.md). O permalink de cada linha conta como evidência.

## Protocolo de Falha
Item vermelho → o chief **não co-assina** o Blackbook e devolve ao agente dono do artefato faltante (copy/funil/ops/growth) com o defeito nomeado, conforme o roteamento do `config.yaml`. Degrau do money model sem copy/página → bloqueia até o ativo existir. Veto de compliance pendente → o pacote não avança até o `compliance-auditor` liberar. Re-entrada: corrigido o artefato e atualizado o registry, o gate é re-submetido e, com tudo verde, o chief co-assina o [`blackbook-dod-gate`](../blackbook-stack/blackbook-dod-gate.md). Override só por decisão humana registrada.

## Links
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`money-model-sequence`](../../frameworks/money-model-sequence.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md) · [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md)
- Agentes: [`offerbook-chief`](../../agents/offerbook-chief.md) · [`compliance-auditor`](../../agents/compliance-auditor.md) · [`knowledge-librarian`](../../agents/knowledge-librarian.md)
- HARD STOP agregador: [`blackbook-dod-gate`](../blackbook-stack/blackbook-dod-gate.md)
- Gate anterior (Offer Book): [`chief-offer-book-readiness-gate`](chief-offer-book-readiness-gate.md)
