---
id: checklist.market.market-competitor-evidence-gate
title: "Gate — Inteligência Competitiva Coletada e Citada (claims dos concorrentes lastreiam o estágio)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
frameworks: [awareness-x-sophistication, starving-crowd]
registries: [offer-registry]
tags: [gate, market, competidor, evidencia, d1, claims, schwartz]
---

# Gate — Inteligência Competitiva Coletada e Citada

## Propósito
Este gate prova que o `market-sophistication-analyst` reuniu a inteligência competitiva que **lastreia** o estágio de sofisticação, em vez de declará-lo no escuro. Existe porque a regra de Schwartz manda inferir o estágio dos **claims que os concorrentes já fizeram** — sem ler o terreno competitivo, o número de sofisticação é palpite. Este gate é o alicerce de evidência por baixo do [`market-sophistication-gate`](market-sophistication-gate.md): ele garante que os anúncios, posicionamentos e mecanismos dos concorrentes foram catalogados e citados, e que o `mechanism-architect` receberá a lista do que **não** repetir. Sem este inventário, o squad arrisca recriar um mecanismo que já saturou o mercado.

## Dono & Escopo
- **owner_agent:** `market-sophistication-analyst` (cataloga a inteligência do handoff de pesquisa ou de coleta própria).
- **Artefato inspecionado:** o **inventário competitivo** anexado ao market-brief (concorrentes, claims dominantes, mecanismos nomeados, antigo vs novo), referenciado pelo [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
A inteligência competitiva está catalogada com fontes citadas, os claims e mecanismos dominantes estão mapeados, e a lista alimenta o diagnóstico de sofisticação e o mecanismo a jusante.

## Itens
1. **Concorrentes identificados.** Verificar: o brief lista os concorrentes diretos relevantes do recorte (não "o mercado em geral").
2. **Claims dominantes catalogados.** Verificar: para cada concorrente, o brief registra o que o anúncio/oferta promete — o claim de superfície.
3. **Mecanismos nomeados mapeados.** Verificar: o brief registra quais concorrentes já nomeiam um mecanismo ("método X", "técnica Y") e quais ainda vendem só o resultado.
4. **Antigo vs novo documentado.** Verificar: há comparação de anúncios antigos e recentes do mesmo concorrente, mostrando o movimento do mercado.
5. **Fontes rastreáveis.** Verificar: cada item de inteligência tem fonte (URL do anúncio, captura, página de vendas), não memória.
6. **Lista de "não repetir" derivada.** Verificar: o brief produz a lista de mecanismos/ângulos já saturados que o `mechanism-architect` deve evitar.
7. **Confiança marcada.** Verificar: se a inteligência é fraca (poucos concorrentes acessíveis), o brief rebaixa a confiança do estágio explicitamente.

## Evidência Exigida
Para marcar cada item ✅, linkar o inventário competitivo do market-brief com a tabela de concorrentes/claims/mecanismos e as fontes de cada linha. Cada claim e cada mecanismo precisa ter origem rastreável (link ou captura), não paráfrase de memória. O permalink do brief e a referência no [`offer-registry`](../../data/registries/offer-registry.md) contam como evidência; a lista de "não repetir" precisa estar explícita para o handoff.

## Protocolo de Falha
Item vermelho → o `market-sophistication-analyst` coleta mais inteligência antes de travar o estágio; claim sem fonte não conta. Sem competitive intel acessível → o analista declara o estágio mais provável **com a incerteza explícita** e pede reforço de pesquisa, sinalizando ao `offerbook-chief`. Inteligência contradiz o escopo (mercado minúsculo, concorrentes em fuga) → sinaliza o risco ao chief. Re-entrada: reunidas as fontes, o gate é re-submetido e o [`market-sophistication-gate`](market-sophistication-gate.md) ganha lastro. O analista não tem veto; a decisão de prosseguir é do chief.

## Links
- Frameworks: [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`starving-crowd`](../../frameworks/starving-crowd.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md) · [`mechanism-architect`](../../agents/mechanism-architect.md)
- Lastreia: [`market-sophistication-gate`](market-sophistication-gate.md)
- Consome a jusante (não repetir mecanismo): [`mechanism-old-vs-new-gate`](../mechanism/mechanism-old-vs-new-gate.md)
