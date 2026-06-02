---
id: checklist.ads.ads-hook-strength-gate
title: "Gate — Força do Gancho (para o scroll no primeiro segundo)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
frameworks: [copy/hook-frameworks, lead-types, copy/fascination-bullets]
registries: [control-registry, swipe-registry]
tags: [gate, ads, gancho, hook, paragem-scroll, d4]
---

# Gate — Força do Gancho

## Propósito
Este gate prova que o gancho de cada ad **para o scroll no primeiro segundo** e prende a atenção até a próxima linha. Ele existe porque um ad só vende se for lido: na lógica de Sugarman, cada elemento existe para fazer consumir o próximo, e o primeiro deles é o gancho. Um criativo com ângulo certo mas abertura fraca morre antes de entregar a mensagem. O gate força a disciplina do Tree-of-Thoughts — gerar três ou mais candidatos por gancho e podar os fracos — e exige que a abertura interrompa o padrão sem recorrer a sensacionalismo sem lastro. É a barreira entre um gancho que ganha o clique honesto e um que só grita.

## Dono & Escopo
- **owner_agent:** `ad-creative-factory` (gera, pontua e seleciona os ganchos). O `voice-style-guardian` co-assina o tom e pode **vetar** ganchos fora da voz (advérbio, voz passiva, frase longa).
- **Artefato inspecionado:** os ganchos e corpos de cada peça da `ad-matrix` no [`control-registry`](../../data/registries/control-registry.md), gerados via [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md) e [`fascination-bullets`](../../frameworks/copy/fascination-bullets.md).

## Condição de Passagem
Cada gancho interrompe o padrão no primeiro segundo, venceu uma rubrica de paragem de scroll contra ao menos dois concorrentes podados, e abre na voz da marca sem sensacionalismo.

## Itens
1. **Candidatos gerados.** Verificar: cada gancho final tem ≥3 candidatos no registro de decisão, com os podados nomeados.
2. **Paragem de scroll.** Verificar: a primeira linha/segundo interrompe o padrão (pergunta, tensão, número, contradição), não é genérica.
3. **Promessa específica.** Verificar: o gancho aponta para uma promessa concreta, não vaga ("emagreça" → "a balança travou mesmo treinando?").
4. **Continuidade de leitura.** Verificar: a abertura leva ao corpo via `fascination-bullets` — a primeira linha cobra a segunda.
5. **Sem sensacionalismo vazio.** Verificar: nenhum gancho usa choque sem relação com a oferta nem promessa que o corpo não sustenta.
6. **Voz aprovada.** Verificar: cada gancho tem o selo do `voice-style-guardian` (3ª série, voz ativa, presente, sem advérbio).
7. **Casamento de temperatura.** Verificar: a intensidade do gancho casa com a temperatura do destino (frio abre por dor/segredo; retarget por objeção) via `lead-types`.

## Evidência Exigida
Para marcar ✅: linkar a tabela de candidatos e podas por gancho (itens 1–2), o gancho final com sua promessa e bullets de corpo (itens 3–4), o selo de voz (item 6) e o mapa temperatura→abertura (item 7). Ganchos vencedores reutilizáveis apontam para o `swipe-registry`.

## Protocolo de Falha
Item vermelho → o `ad-creative-factory` volta ao Tree-of-Thoughts e regera os candidatos do gancho fraco; gancho sem paragem de scroll ou com promessa vaga é reprovado. Gancho fora de voz volta ao [`voice-style-guardian`](../../agents/voice-style-guardian.md). Promessa sem lastro é tratada no [`ads-claim-backing-gate`](ads-claim-backing-gate.md), não aqui. Re-entrada: reescrever, re-aprovar a voz, atualizar o `control-registry` e re-submeter.

## Links
- Frameworks: [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`fascination-bullets`](../../frameworks/copy/fascination-bullets.md) · [`lead-types`](../../lib/taxonomies/lead-types.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`swipe-registry`](../../data/registries/swipe-registry.md)
- Agentes: [`ad-creative-factory`](../../agents/ad-creative-factory.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Gates irmãos: [`ads-angle-coverage-gate`](ads-angle-coverage-gate.md) · [`ads-claim-backing-gate`](ads-claim-backing-gate.md) · [`ads-variation-gate`](ads-variation-gate.md) · [`ads-test-hypothesis-gate`](ads-test-hypothesis-gate.md)
