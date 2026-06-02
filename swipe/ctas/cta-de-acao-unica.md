---
id: swipe.ctas.cta-de-acao-unica
title: "Padrão: CTA de Ação Única"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [copy.close-frameworks, copy.aida, scarcity-urgency-engine, awareness-x-sophistication]
sources:
  - "Dan S. Kennedy, *The Ultimate Sales Letter* (4ª ed., 2011)."
  - "Joseph Sugarman, *The Adweek Copywriting Handbook* (2007)."
tags: [swipe, cta, single-ask, close, conversion, most-aware]
---

# Padrão: CTA de Ação Única

## O que é
Este é o **padrão estrutural do pedido único** — uma só ação, clara e ousada, com instrução exata do que fazer. O arquétipo-fonte é o fecho de resposta direta: nada de "saiba mais" ou dois caminhos, apenas **um** pedido que o leitor convencido executa. Aqui guardamos só a **anatomia** — como recapitular, pedir e instruir — em redação original, nunca copy literal de campanha alheia.

Calibrado para público **consciente do produto ou mais consciente** (consciência 4-5 — ver [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md)): a pessoa já quer; só falta a instrução para agir. É o fecho de páginas de oferta, e-mails quentes e anúncios de conversão, onde a jornada de persuasão já aconteceu e a CTA só precisa ser inequívoca.

## Anatomia
A sequência de elementos que sustenta o padrão:
1. **Recapitulação curta de valor** — uma frase que reancora o que ele leva e o valor total, para o preço parecer pequeno diante do ganho.
2. **O pedido único** — um verbo de ação e um só caminho: "clique em {{botão}}", "responda com SIM". Sem alternativa concorrente.
3. **A instrução exata** — o passo literal seguinte: onde clicar, o que digitar, o que acontece depois do clique. Remove qualquer dúvida operacional.
4. **A razão para agir agora** — um gatilho de urgência **verdadeira** (vaga real, prazo real, bônus que de fato expira), quando existir.
5. **A repetição do pedido** — o mesmo CTA único repetido ao final, idêntico, sem novo caminho.

A regra: **um** pedido por peça. Dois botões dividem a decisão e derrubam a conversão.

## Por que funciona
Um pedido único reduz a **fricção de decisão**: quanto menos escolhas, mais ação (ver [`../../reference/psychology/decision-fatigue-and-friction.md`](../../reference/psychology/decision-fatigue-and-friction.md)). É o beat de Ação do [`../../frameworks/copy/aida.md`](../../frameworks/copy/aida.md) e a régua central de [`../../frameworks/copy/close-frameworks.md`](../../frameworks/copy/close-frameworks.md): um pedido claro, com valor recapitulado antes do número. A **instrução exata** explora a fluência cognitiva — o que é fácil de fazer é mais provável de ser feito (ver [`../../reference/psychology/cognitive-ease-fluency.md`](../../reference/psychology/cognitive-ease-fluency.md)). A urgência verdadeira ([`../../frameworks/scarcity-urgency-engine.md`](../../frameworks/scarcity-urgency-engine.md)) adiciona o custo de adiar sem mentir. Kennedy e Sugarman mostraram que a venda se perde no pedido tímido: a clareza ousada converte mais que a sugestão educada.

## Padrão reutilizável
Esqueleto em redação original, com placeholders para preencher:

```
[RECAP] Você leva {{componentes_da_oferta}} — um valor de {{valor_total_ancorado}}.
[PEDIDO ÚNICO] {{verbo_de_ação}} em {{nome_do_botão_ou_canal}}.
[INSTRUÇÃO] Ao {{ação}}, você {{o_que_acontece_em_seguida}} — leva {{tempo_curto}}.
[RAZÃO AGORA] {{gatilho_de_urgência_verdadeira: vaga real / prazo real / bônus que expira}}.
[REPETE] {{mesmo_verbo}} em {{mesmo_botão}} e {{benefício_imediato}}.
```

Gere variações do verbo e do rótulo do botão para teste A/B, alimentando o `control-registry`. Toda urgência citada passa pelo `compliance-auditor`. Mantenha **um** caminho — se aparecer um segundo CTA, corte.

## Adaptação por sofisticação
Conforme [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md):
- **Sofisticação 1-2** — o pedido direto basta: "{{verbo}} agora". O mercado age sem muita reancoragem.
- **Sofisticação 3** — amarre o CTA ao **mecanismo**: "comece o {{mecanismo}} agora". O pedido reforça o que o diferencia.
- **Sofisticação 4** — o público viu CTAs demais; pese a **recapitulação de valor e a reversão de risco** antes do pedido, e use o rótulo de botão mais específico ("Quero {{resultado}}", não "Comprar").
- **Sofisticação 5** — o CTA vira **convite de pertencimento**: "entre para {{grupo/identidade}}". O peso sai da transação e vai para o status de fazer parte.

## Fonte
> **Fonte:** Mecânica de pedido único derivada do fechamento de carta de vendas de Dan S. Kennedy, *The Ultimate Sales Letter* (4ª ed., 2011) e dos gatilhos de Joseph Sugarman, *The Adweek Copywriting Handbook* (2007) — via [`../../reference/books/copywriting/kennedy-ultimate-sales-letter.md`](../../reference/books/copywriting/kennedy-ultimate-sales-letter.md) e [`../../reference/books/copywriting/sugarman-adweek-copywriting.md`](../../reference/books/copywriting/sugarman-adweek-copywriting.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
