---
id: checklist.market.market-awareness-gate
title: "Gate — Nível de Consciência do Mercado Diagnosticado com Evidência (nível 1-5 defensável)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
frameworks: [awareness-x-sophistication]
registries: [offer-registry]
tags: [gate, market, consciencia, schwartz, d1, lead, voc]
---

# Gate — Nível de Consciência do Mercado Diagnosticado

## Propósito
Este gate prova que o `market-sophistication-analyst` declarou o nível de consciência do mercado (1-5) com evidência da voz do prospect. Existe porque a consciência define **onde a copy começa**: um inconsciente do problema (nível 1) precisa de uma abertura longa e indireta; um consciente do produto (nível 4) precisa de diferenciação e prova direta. Errar o nível faz a copy falar cedo demais ou tarde demais — e a venda não acontece. É o segundo número-mãe do squad, par do estágio de sofisticação, e juntos formam a célula da matriz que orienta avatar, mecanismo e posicionamento. Sem este número com lastro, a abertura da copy é chute.

## Dono & Escopo
- **owner_agent:** `market-sophistication-analyst` (dono da taxonomia [`awareness-levels`](../../lib/taxonomies/awareness-levels.md)).
- **Artefato inspecionado:** o **bloco de consciência** do market-brief, com o nível e a célula da matriz (consciência × sofisticação) citados, referenciado pelo [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O mercado tem um nível de consciência (1-5) declarado, com o lead recomendado e ao menos duas evidências de VOC que o sustentam.

## Itens
1. **Nível declarado (1-5).** Verificar: o brief diz exatamente um nível com o termo da taxonomia (`inconsciente · problema · solução · produto · mais-consciente`).
2. **≥2 evidências de VOC.** Verificar: o nível é sustentado por ao menos duas fontes de como o prospect fala/busca (verbatims, termos de busca, posts), cada uma citada.
3. **Como o prospect descreve a situação.** Verificar: o brief mostra a linguagem real do prospect que indica o nível (ex.: "não sei o que fazer" = nível 2; "qual método é melhor" = nível 3-4).
4. **Célula da matriz definida.** Verificar: o brief cruza consciência × sofisticação numa célula (ex.: C3×S4), conforme [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md).
5. **Lead recomendado derivado.** Verificar: o nível gera um lead recomendado (história, problema-solução, promessa/segredo, oferta, oferta direta).
6. **Abertura da copy definida.** Verificar: o brief diz se a abertura deve ser longa/indireta (consciência baixa) ou curta/direta (consciência alta).
7. **Coerência com a sofisticação.** Verificar: o nível de consciência não contradiz o estágio do [`market-sophistication-gate`](market-sophistication-gate.md) sem explicação (a célula precisa fazer sentido).

## Evidência Exigida
Para marcar cada item ✅, linkar o bloco de diagnóstico do market-brief com o nível, a célula da matriz e o lead recomendado. Cada uma das ≥2 evidências de VOC precisa ter fonte rastreável (citação literal + origem). A consistência com o estágio de sofisticação é verificada contra o gate par. O permalink do brief e da linha do registry contam como evidência.

## Protocolo de Falha
Item vermelho → o `market-sophistication-analyst` volta à VOC e coleta mais evidência; nível sem ≥2 fontes não passa. Nível por palpite → refaz a partir da linguagem real do prospect. Célula incoerente (consciência alta com sofisticação 1 sem explicação) → o analista revisa os dois números juntos. Sem VOC acessível → o brief sai com **confiança rebaixada** e pedido de pesquisa registrado, sinalizado ao `offerbook-chief`. Re-entrada: reunidas as evidências de VOC, o gate é re-submetido. O analista não tem veto; sinaliza, e o chief decide.

## Links
- Frameworks: [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · taxonomia [`awareness-levels`](../../lib/taxonomies/awareness-levels.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md)
- Gate par (mesma fase): [`market-sophistication-gate`](market-sophistication-gate.md)
- Consome a jusante: [`avatar-dominant-emotion-gate`](../avatar/avatar-dominant-emotion-gate.md)
