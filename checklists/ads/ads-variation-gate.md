---
id: checklist.ads.ads-variation-gate
title: "Gate — Variação Real (ângulos distintos, não cosméticos)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
frameworks: [copy/hook-frameworks, lead-types, copy/fascination-bullets]
registries: [control-registry, swipe-registry]
tags: [gate, ads, variacao, angulos, teste, d4]
---

# Gate — Variação Real

## Propósito
Este gate prova que cada variação na matriz de ads é um **ângulo de verdade**, não a mesma abertura com outra cor de botão ou outro emoji. Ele existe porque um teste só aprende quando as variações abrem por eixos diferentes — dor, mecanismo, prova, identidade, medo ou ganho. Trocar cosmético gera dados que não ensinam: o pixel gasta orçamento sem isolar o que move o clique. Vale o princípio `clarity_before_volume`: poucos ângulos reais valem mais que muitas cópias disfarçadas. O gate força a disciplina do Tree-of-Thoughts do `ad-creative-factory`, que poda toda variação cuja diferença de ângulo pontua zero. É a barreira que separa "mais criativos" de "criativos diferentes" e protege o orçamento de mídia de testes estéreis.

## Dono & Escopo
- **owner_agent:** `ad-creative-factory` (gera, pontua e poda as variações por eixo de ângulo). O `voice-style-guardian` co-assina o tom e pode **vetar** o que sai da voz.
- **Artefato inspecionado:** as variações de cada peça da `ad-matrix` no [`control-registry`](../../data/registries/control-registry.md), com o `eixo_de_angulo` declarado por ad e os ganchos reutilizáveis no [`swipe-registry`](../../data/registries/swipe-registry.md).

## Condição de Passagem
Toda variação de um mesmo alvo abre por um eixo de ângulo distinto dos demais, sem nenhuma diferença apenas cosmética.

## Itens
1. **Eixo declarado por variação.** Verificar: cada ad nomeia seu `eixo_de_angulo` no `control-registry` (dor, mecanismo, prova, identidade, medo/ganho).
2. **Eixos não repetidos.** Verificar: para o mesmo alvo (dor ou objeção), dois ads não compartilham o mesmo eixo.
3. **Diferença substantiva.** Verificar: a abertura muda a promessa ou o ângulo de entrada, não só a imagem, a cor ou o emoji.
4. **Candidatos e podas registrados.** Verificar: o registro de decisão lista as variações geradas e as podadas, com o motivo da poda.
5. **Sem clone disfarçado.** Verificar: nenhuma variação é a #1 com sinônimo trocado; o teste isola um ângulo, não cosmético.
6. **Reuso rastreável.** Verificar: variações reaproveitadas de ganchos vencedores apontam para o `swipe-registry` com a categoria e o ângulo.
7. **Voz aprovada.** Verificar: cada variação carrega o selo do `voice-style-guardian`.

## Evidência Exigida
Para marcar ✅: linkar a tabela de variações por alvo com o `eixo_de_angulo` de cada uma (itens 1–2), os exemplos de antes/depois que mostram a diferença substantiva (item 3), o registro de candidatos e podas (itens 4–5) e o selo de voz (item 7). Reusos apontam para o `swipe-registry`.

## Protocolo de Falha
Item vermelho → o `ad-creative-factory` volta ao Tree-of-Thoughts e **regera** a variação por um eixo distinto, ou a **poda** se ela só repete cosmético. Variação que não muda o ângulo é reprovada e removida do teste. Cobertura de ângulos por dor é tratada no [`ads-angle-coverage-gate`](ads-angle-coverage-gate.md); força de abertura no [`ads-hook-strength-gate`](ads-hook-strength-gate.md). Re-entrada: substituir a variação cosmética por um ângulo novo, atualizar o `control-registry` e re-submeter. Mudança na Big Idea reabre este gate.

## Links
- Frameworks: [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`lead-types`](../../lib/taxonomies/lead-types.md) · [`fascination-bullets`](../../frameworks/copy/fascination-bullets.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`swipe-registry`](../../data/registries/swipe-registry.md)
- Agentes: [`ad-creative-factory`](../../agents/ad-creative-factory.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Gates irmãos: [`ads-angle-coverage-gate`](ads-angle-coverage-gate.md) · [`ads-hook-strength-gate`](ads-hook-strength-gate.md) · [`ads-claim-backing-gate`](ads-claim-backing-gate.md) · [`ads-test-hypothesis-gate`](ads-test-hypothesis-gate.md)
