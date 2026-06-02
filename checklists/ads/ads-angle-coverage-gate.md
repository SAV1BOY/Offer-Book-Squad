---
id: checklist.ads.ads-angle-coverage-gate
title: "Gate — Cobertura de Ângulos (cada dor por múltiplos ângulos distintos)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
frameworks: [copy/hook-frameworks, lead-types, copy/fascination-bullets]
registries: [control-registry, swipe-registry]
tags: [gate, ads, angulos, cobertura, retargeting, continuidade, d4]
---

# Gate — Cobertura de Ângulos

## Propósito
Este gate prova que a matriz de ads ataca **cada dor dominante do avatar por múltiplos ângulos distintos** — e não a mesma abertura repetida. Ele existe porque "mais criativos" não é o mesmo que "criativos diferentes": um teste só aprende quando os ângulos abrem por eixos reais (dor, mecanismo, prova, identidade, medo/ganho). Sem cobertura, o pixel queima orçamento sem isolar o que converte. O gate também garante as três camadas da matriz: **frio** (descoberta por dor), **retargeting** (uma reversão por objeção dominante) e **continuidade** (ângulos de retenção/recompra para a recorrência do money model). É a barreira que separa volume de variação real e fecha o ciclo da escada de receita.

## Dono & Escopo
- **owner_agent:** `ad-creative-factory` (monta e verifica a cobertura por dor, objeção e fase). O `voice-style-guardian` co-assina o tom de cada peça e pode **vetar** o que sai da voz.
- **Artefato inspecionado:** a `ad-matrix` registrada no [`control-registry`](../../data/registries/control-registry.md), cruzada com o [`objection-registry`](../../data/registries/objection-registry.md) (dores e objeções em verbatim) e o [`swipe-registry`](../../data/registries/swipe-registry.md) (ganchos reutilizáveis).

## Condição de Passagem
Cada dor dominante é coberta por pelo menos três ângulos distintos, cada objeção dominante tem um ad de retargeting, e a camada de continuidade existe para a recorrência.

## Itens
1. **Dores dominantes mapeadas.** Verificar: cada dor do `objection-registry`/VOC vira uma linha na camada frio da `ad-matrix`.
2. **≥3 ângulos por dor.** Verificar: contar os ângulos por dor — cada um abre por um eixo diferente (dor≠mecanismo≠identidade), não cosmético.
3. **Eixos declarados.** Verificar: cada ad nomeia seu `eixo_de_angulo` no `control-registry`, sem dois iguais para a mesma dor.
4. **Retargeting por objeção.** Verificar: cada objeção dominante do `objection-registry` tem um ad de retargeting que a reverte (mecanismo + garantia).
5. **Continuidade presente.** Verificar: existe ≥1 ângulo que fala a quem já teve o primeiro resultado (retenção/recompra).
6. **Casamento de consciência.** Verificar: a abertura de cada camada casa com a temperatura (frio≠retarget≠continuidade) via `lead-types`.
7. **Sem buraco de cobertura.** Verificar: nenhuma dor sem ângulo, nenhuma objeção sem retarget, continuidade não-ausente.

## Evidência Exigida
Para marcar ✅: linkar a `ad-matrix` no `control-registry` com a contagem de ângulos por dor (itens 1–3), a tabela objeção→ad de retargeting (item 4), os ângulos de continuidade (item 5) e o cruzamento temperatura→lead (item 6). Ganchos reutilizados apontam para o `swipe-registry`.

## Protocolo de Falha
Item vermelho → o `ad-creative-factory` volta ao Tree-of-Thoughts no sub-objetivo da lacuna e **recria o ângulo faltante** em vez de inflar variações redundantes. Dor sem ângulo, objeção sem retarget ou continuidade ausente reabrem o gate. Se a lacuna é de verbatim, aciona-se o [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md). Re-entrada: completar a matriz, atualizar o `control-registry` e re-submeter. Mudança na Big Idea ou no money model reabre este gate.

## Links
- Frameworks: [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`lead-types`](../../lib/taxonomies/lead-types.md) · [`fascination-bullets`](../../frameworks/copy/fascination-bullets.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`swipe-registry`](../../data/registries/swipe-registry.md) · [`objection-registry`](../../data/registries/objection-registry.md)
- Agentes: [`ad-creative-factory`](../../agents/ad-creative-factory.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Gates irmãos: [`ads-hook-strength-gate`](ads-hook-strength-gate.md) · [`ads-claim-backing-gate`](ads-claim-backing-gate.md) · [`ads-variation-gate`](ads-variation-gate.md) · [`ads-test-hypothesis-gate`](ads-test-hypothesis-gate.md)
