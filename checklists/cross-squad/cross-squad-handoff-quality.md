---
id: checklist.cross-squad.cross-squad-handoff-quality
title: "Gate — Qualidade do Handoff Cross-Squad"
type: gate
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [offer-to-funnel-mapping, proof-to-claim-chain, power-of-one]
registries: [decision-registry, offer-registry]
tags: [gate, cross-squad, handoff, integration, contract]
---

# Gate — Qualidade do Handoff Cross-Squad

## Propósito
Este gate prova que **todo pacote que sai deste squad para outro (ou entra de outro) é completo, rastreável e sem ambiguidade**. Existe porque integrações entre squads quebram no contrato: o copy-squad recebe um offer book sem a Big Idea, o advisory recebe uma oferta sem prova, o data-squad entrega pricing sem método. Um handoff só é válido quando o destinatário pode agir sem voltar a perguntar. Protege o princípio `traceability_before_eloquence` na fronteira entre squads, conforme `config.yaml: cross_squad`.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (controla as transições de fronteira); o `compliance-auditor` co-assina quando o pacote leva claims.
- **Artefato inspecionado:** o pacote de handoff (entrada ou saída) entre o Offer Book Squad e os squads vizinhos — deepresearch, copy, brand, traffic, design, data, c-level, advisory — registrado no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
O pacote de handoff nomeia squad de origem e destino, entrega exatamente os artefatos do contrato em `config.yaml: cross_squad`, e o destinatário pode agir sem pedir esclarecimento.

## Itens
1. **Origem e destino nomeados.** Verificar: o pacote declara o squad de origem, o de destino e a direção (entrada/saída).
2. **Contrato do config respeitado.** Verificar: os artefatos entregues batem com `cross_squad.<squad>.handoff_*` ou `shared_assets` do config.
3. **Artefatos completos.** Verificar: cada artefato prometido existe e está acessível por link, não "em progresso".
4. **Rastreabilidade.** Verificar: cada claim ou número no pacote aponta para a fonte (registry/proof) deste squad.
5. **Big Idea/escopo coerentes.** Verificar: o pacote não contradiz a Big Idea travada nem a frase de escopo.
6. **Critério de aceite explícito.** Verificar: o pacote declara o que o destinatário deve conseguir fazer com ele (a definição de "recebido").
7. **Decisão de handoff registrada.** Verificar: `decision_id` com data, conteúdo do pacote e responsável de ambos os lados.

## Evidência Exigida
Para marcar ✅: linkar o manifesto do pacote com origem/destino (itens 1–2), os artefatos acessíveis (item 3), a tabela de rastreabilidade até a fonte (item 4), a checagem contra Big Idea/escopo (item 5), o critério de aceite (item 6) e o `decision_id` (item 7).

## Protocolo de Falha
Item vermelho → o `offerbook-chief` **não libera o handoff** e devolve ao agente dono do artefato faltante com o defeito nomeado. Pacote que contradiz a Big Idea volta ao `big-idea-architect`. Re-entrada: completar/corrigir o artefato, atualizar o manifesto, registrar a decisão e re-submeter. Handoff de entrada incompleto de outro squad é devolvido com perguntas objetivas, sem inventar o que falta.

## Links
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`power-of-one`](../../frameworks/power-of-one.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Config: `cross_squad` (contratos bidirecionais por squad)
- Gates relacionados: [`cross-squad-research-request-quality`](cross-squad-research-request-quality.md) · [`cross-squad-asset-validation`](cross-squad-asset-validation.md)
- Agentes: [`offerbook-chief`](../../agents/offerbook-chief.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
