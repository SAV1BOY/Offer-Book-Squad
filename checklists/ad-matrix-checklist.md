---
id: checklist.ad-matrix-checklist
title: "Checklist — Matriz de Ads (um ângulo por ad, sem claim sem lastro)"
type: checklist
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
frameworks: [copy/hook-frameworks, lead-types, copy/fascination-bullets, proof-to-claim-chain]
registries: [control-registry, swipe-registry, claim-registry, proof-registry]
tags: [checklist, copy, ads, matriz, angulos, hook, claim-backing, d4]
---

# Checklist — Matriz de Ads

## Propósito
Este checklist prova que a matriz de ads cobre os ângulos certos, com **um ângulo claro por anúncio** e **nenhum claim sem lastro**. Existe porque tráfego pago amplifica tudo — inclusive o erro: um ad com claim sem prova vira risco de compliance e desperdício de verba; uma matriz que repete o mesmo ângulo em dez variações não aprende nada. Cada ad é um teste; o ângulo é a hipótese. Sem este checklist verde, a matriz vira ruído caro. Ele garante `evidence_before_opinion` no criativo: cada promessa de anúncio aponta para prova, e cada ângulo mapeia uma dor ou estágio de consciência real do avatar.

## Dono & Escopo
- **owner_agent:** `ad-creative-factory` (gera a matriz e responde pelos ângulos); o [`voice-style-guardian`](../agents/voice-style-guardian.md) co-assina a voz e o `compliance-auditor` veta claim sem lastro.
- **Artefato inspecionado:** o entregável `artifact.ad-matrix` (matriz de ângulos × variações), registrado no [`control-registry`](../data/registries/control-registry.md) e no [`swipe-registry`](../data/registries/swipe-registry.md).

## Condição de Passagem
Cada ad carrega UM ângulo nomeado ligado a uma dor/consciência do avatar, todo claim tem prova, e a matriz cobre os ângulos prioritários sem repetição cega.

## Itens
1. **Um ângulo por ad.** Como verificar: cada linha da matriz declara UM ângulo (dor, desejo, objeção, mecanismo); um ad que mistura dois ângulos é dividido em dois.
2. **Cobertura de ângulos.** Como verificar: a matriz cobre os ângulos prioritários do avatar/objeções (ligados ao [`objection-registry`](../data/registries/objection-registry.md)); nenhum ângulo-chave fica de fora.
3. **Claim com lastro.** Como verificar: todo número/promessa no ad tem `proof_id` no [`proof-registry`](../data/registries/proof-registry.md); claim sem prova sai do ad.
4. **Hook na primeira linha.** Como verificar: cada ad abre com um hook que para o scroll, coerente com o ângulo e o tipo de lead.
5. **Fit por consciência (lead-type).** Como verificar: o ângulo casa com o estágio de consciência do público-alvo do ad (direto vs indireto), conforme [`lead-types`](../frameworks/lead-types.md).
6. **Variação com propósito.** Como verificar: variações do mesmo ângulo mudam UMA coisa por vez (hook, prova, formato) para que o teste ensine.
7. **Voz aprovada.** Como verificar: o `voice-style-guardian` deu `voice-verdict` APROVADO.
8. **Rastreio de criativo.** Como verificar: cada ad tem id de criativo e está registrado no `control-registry`/`swipe-registry` para reuso e leitura de resultado.

## Evidência Exigida
Para marcar ✅: linkar a matriz no `control-registry`, o mapa ângulo→objeção/avatar (itens 1–2), a tabela claim→proof sem órfãos (item 3), a regra de variação documentada (item 6) e o `voice-verdict` APROVADO (item 7). Cada criativo precisa de id rastreável (item 8).

## Protocolo de Falha
Item vermelho → a matriz volta ao `ad-creative-factory` com o defeito nomeado e **não vai para veiculação**. Claim sem lastro aciona veto do `compliance-auditor`. Ângulo sem dor real ou variação sem propósito é reescrito. Re-entrada: corrigir a matriz, atualizar o `control-registry`/`swipe-registry`, re-submeter. Mudança na Big Idea ou nas objeções reabre este checklist.

## Links
- Frameworks: [`copy/hook-frameworks`](../frameworks/copy/hook-frameworks.md) · [`lead-types`](../frameworks/lead-types.md) · [`copy/fascination-bullets`](../frameworks/copy/fascination-bullets.md) · [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md)
- Registries: [`control-registry`](../data/registries/control-registry.md) · [`swipe-registry`](../data/registries/swipe-registry.md) · [`claim-registry`](../data/registries/claim-registry.md) · [`proof-registry`](../data/registries/proof-registry.md) · [`objection-registry`](../data/registries/objection-registry.md)
- Agentes: [`ad-creative-factory`](../agents/ad-creative-factory.md) · [`voice-style-guardian`](../agents/voice-style-guardian.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Checklists vizinhos: [`compliance-checklist`](compliance-checklist.md) · [`funnel-map-checklist`](funnel-map-checklist.md)
