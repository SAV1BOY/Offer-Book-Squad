---
id: checklist.ads.ads-test-hypothesis-gate
title: "Gate — Hipótese de Teste (cada ad responde uma pergunta)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
frameworks: [copy/hook-frameworks, lead-types, copy/fascination-bullets]
registries: [control-registry, swipe-registry]
tags: [gate, ads, hipotese, teste, aprendizado, d4]
---

# Gate — Hipótese de Teste

## Propósito
Este gate prova que a matriz de ads é um **experimento desenhado para aprender**, não um amontoado de criativos jogados ao vento. Cada ad — ou cada grupo de ads — carrega uma **hipótese explícita**: qual eixo de ângulo, qual dor ou qual objeção ele testa, e o que um vencedor ensinaria sobre o mercado. Ele existe por causa do princípio `decision_before_ornament`: cada peça serve a uma decisão, e a decisão aqui é "o que escalar e o que cortar". Sem hipótese, o resultado do teste vira ruído — sobe o que teve sorte, não o que ensina. O gate exige que a leitura do teste seja prevista antes da mídia girar: variável isolada, métrica de sucesso e o que o aprendizado alimenta de volta no `swipe-registry`. É a barreira que transforma gasto de mídia em conhecimento reutilizável.

## Dono & Escopo
- **owner_agent:** `ad-creative-factory` (formula a hipótese de cada teste e prevê a leitura). O `voice-style-guardian` co-assina o tom de cada peça.
- **Artefato inspecionado:** o desenho de teste da `ad-matrix` no [`control-registry`](../../data/registries/control-registry.md), cruzado com os eixos de ângulo por dor/objeção e os ganchos vencedores no [`swipe-registry`](../../data/registries/swipe-registry.md).

## Condição de Passagem
Cada ad ou grupo de ads declara a hipótese que testa, a variável isolada e a métrica de sucesso, de modo que o resultado ensine uma decisão clara de escalar ou cortar.

## Itens
1. **Hipótese explícita.** Verificar: cada grupo de teste registra a pergunta que responde ("o eixo-mecanismo bate o eixo-dor para esta dor?") no `control-registry`.
2. **Variável isolada.** Verificar: o grupo varia **um** fator por vez (eixo, lead ou promessa), para o resultado ser atribuível.
3. **Métrica de sucesso definida.** Verificar: cada teste nomeia a métrica que decide o vencedor (CTR, custo por clique qualificado, conversão), não "vibe".
4. **Leitura prevista.** Verificar: o registro antecipa o que um vencedor ensinaria sobre o mercado, dor ou consciência.
5. **Casamento com a camada.** Verificar: a hipótese respeita a camada (frio testa descoberta; retarget testa reversão de objeção; continuidade testa retenção) via `lead-types`.
6. **Aprendizado de volta ao swipe.** Verificar: o desenho prevê gravar o ângulo vencedor e o motivo no `swipe-registry` para reuso.
7. **Sem teste estéril.** Verificar: nenhum grupo testa cosmético sem hipótese; toda variação isola um ângulo que ensina.

## Evidência Exigida
Para marcar ✅: linkar a tabela de grupos de teste com hipótese, variável isolada e métrica de sucesso (itens 1–3), a leitura prevista por teste (item 4), o mapa camada→hipótese (item 5) e o plano de write-back ao `swipe-registry` (item 6).

## Protocolo de Falha
Item vermelho → o `ad-creative-factory` reformula o grupo: nomeia a hipótese, isola a variável e define a métrica antes de a mídia girar. Teste sem hipótese ou com duas variáveis misturadas é reprovado e redesenhado — o resultado seria ininterpretável. A diferença real entre variações é garantida no [`ads-variation-gate`](ads-variation-gate.md); a cobertura de ângulos no [`ads-angle-coverage-gate`](ads-angle-coverage-gate.md). Re-entrada: anexar a hipótese e a métrica, atualizar o `control-registry` e re-submeter. Vencedores apurados voltam ao `swipe-registry` via o [`knowledge-librarian`](../../agents/knowledge-librarian.md).

## Links
- Frameworks: [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`lead-types`](../../lib/taxonomies/lead-types.md) · [`fascination-bullets`](../../frameworks/copy/fascination-bullets.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`swipe-registry`](../../data/registries/swipe-registry.md)
- Agentes: [`ad-creative-factory`](../../agents/ad-creative-factory.md) · [`knowledge-librarian`](../../agents/knowledge-librarian.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Gates irmãos: [`ads-angle-coverage-gate`](ads-angle-coverage-gate.md) · [`ads-hook-strength-gate`](ads-hook-strength-gate.md) · [`ads-claim-backing-gate`](ads-claim-backing-gate.md) · [`ads-variation-gate`](ads-variation-gate.md)
