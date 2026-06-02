---
id: checklist.market.market-sophistication-gate
title: "Gate — Sofisticação do Mercado Diagnosticada com Evidência (estágio 1-5 defensável)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
frameworks: [awareness-x-sophistication]
registries: [offer-registry]
tags: [gate, market, sofisticacao, schwartz, d1, diagnostico, mecanismo]
---

# Gate — Sofisticação do Mercado Diagnosticada

## Propósito
Este gate prova que o `market-sophistication-analyst` declarou o estágio de sofisticação do mercado (1-5) com evidência, não por palpite. Existe porque o erro-mãe de Schwartz custa caro: tratar um mercado estágio-4 com copy estágio-2 deixa a oferta **invisível**, e tratar um estágio-2 como estágio-4 gasta esforço de mecanismo à toa. O estágio define o que o `mechanism-architect` precisará fazer (introduzir vs elevar o mecanismo), qual lead a copy usa e quão direta ela começa. É um dos dois números-mãe do squad: todo o trabalho a jusante calibra por ele. Sem este número travado com lastro, o diagnóstico é opinião.

## Dono & Escopo
- **owner_agent:** `market-sophistication-analyst` (dono da taxonomia [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md)).
- **Artefato inspecionado:** o **bloco de sofisticação** do market-brief, com o estágio registrado em `sophistication_stage` no [`offer-registry`](../../data/registries/offer-registry.md) e a evidência citada.

## Condição de Passagem
O mercado tem um estágio de sofisticação (1-5) declarado, com o movimento vencedor nomeado e pelo menos duas evidências independentes que o sustentam.

## Itens
1. **Estágio declarado (1-5).** Verificar: o brief diz exatamente um estágio com o termo da taxonomia (`primeiro claim · amplifica · mecanismo · eleva-mecanismo · identidade`).
2. **≥2 evidências independentes.** Verificar: o estágio é sustentado por ao menos duas fontes distintas (anúncios de concorrentes, claims dominantes, anúncios antigos vs novos), cada uma citada.
3. **Claims dos concorrentes mapeados.** Verificar: o brief lista os claims que os concorrentes já fizeram — base para inferir saturação, conforme a regra de Schwartz.
4. **Antigo vs novo comparado.** Verificar: há comparação entre anúncios antigos e recentes que mostre o movimento do mercado (claim puro → mecanismo → elevação).
5. **Contra-evidência buscada.** Verificar: o brief registra se há sinal que indicaria outro estágio, e por que o estágio escolhido vence (`contradiction_before_conclusion`).
6. **Implicação de mecanismo derivada.** Verificar: o estágio gera uma instrução clara ao `mechanism-architect` (estágio 3 = introduzir; estágio 4 = elevar).
7. **Regra do arredondamento aplicada.** Verificar: na dúvida entre dois estágios, o brief documenta o arredondamento para o mais sofisticado, com o motivo.

## Evidência Exigida
Para marcar cada item ✅, linkar o bloco de diagnóstico do market-brief e a linha do [`offer-registry`](../../data/registries/offer-registry.md) com `sophistication_stage` e a justificativa. Cada uma das ≥2 evidências precisa ter fonte rastreável (URL do anúncio, captura de review, citação do claim). O permalink da linha do registry conta como evidência do número travado.

## Protocolo de Falha
Item vermelho → o `market-sophistication-analyst` **não emite o brief** e volta a coletar evidência; estágio sem ≥2 fontes não passa. Diagnóstico por palpite → o analista refaz a partir da evidência, nunca força o número. Sub-diagnóstico (estágio-4 lido como 2) → na dúvida arredonda para cima e cita o sinal de saturação. Sem nenhuma evidência acessível → o brief sai com **confiança rebaixada** e pedido de pesquisa registrado, sinalizado ao `offerbook-chief`. Re-entrada: reunidas as evidências, o gate é re-submetido. O analista não tem veto; sinaliza ao chief, que decide prosseguir ou parar.

## Links
- Frameworks: [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · taxonomia [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md) · [`mechanism-architect`](../../agents/mechanism-architect.md)
- Gate par (mesma fase): [`market-awareness-gate`](market-awareness-gate.md)
- Consome a jusante: [`mechanism-naming-gate`](../mechanism/mechanism-naming-gate.md)
