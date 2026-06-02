---
id: swipe.guarantees.condicional-baseada-em-resultado
title: "Padrão: Garantia Condicional Baseada em Resultado"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [guarantee-design, risk-reversal-ladder, value-equation, proof-to-claim-chain]
sources:
  - "Alex Hormozi, *$100M Offers* (2021), capítulo de Garantias."
tags: [swipe, guarantee, conditional, performance, milestone, risk-reversal]
---

# Padrão: Garantia Condicional Baseada em Resultado

## O que é
Este é o **padrão estrutural da garantia condicional** — aquela em que o **cliente cumpre a parte dele** e, se o resultado não vier, você devolve, dobra, dá crédito, ou segue trabalhando de graça até o marco. Cobre os **tipos 2-11** da taxonomia ([`../../lib/taxonomies/guarantee-types.md`](../../lib/taxonomies/guarantee-types.md)), com destaque para a **garantia de serviço** (tipo 3: "seguimos juntos até funcionar") e a de **primeiro resultado** (tipo 11). Aqui guardamos só a **anatomia** da redação — risco, condição verificável e promessa — em redação original, nunca copy literal de oferta alheia.

Cabe quando o **resultado depende do esforço do cliente** (ele precisa fazer as sessões, aplicar o método). A condição não enfraquece a garantia: ela **filtra** o cliente que não faz a parte dele e protege a margem, ao mesmo tempo em que reverte o risco para quem age de boa-fé.

## Anatomia
A sequência de elementos que sustenta o padrão:
1. **Nome do risco dominante** — a copy nomeia o medo exato do avatar ("e se eu fizer tudo e mesmo assim não der?").
2. **A promessa de resultado** — o marco específico e mensurável (não "satisfação", mas "{{resultado}} em {{prazo}}").
3. **A condição clara** — o que o cliente precisa **provar que fez**: marcos verificáveis, não "se esforçar". Condição vaga gera disputa.
4. **A consequência se falhar** — o gesto honrável: devolução, dobro, crédito, ou "seguimos juntos de graça até o marco".
5. **A âncora de prova** — depoimentos de quem cumpriu a condição e atingiu o resultado, mostrando que a condição é justa e alcançável.

Como toda garantia, entra **depois** do valor e **antes** do preço.

## Por que funciona
A condicional sobe a **Probabilidade percebida** da [Value Equation](../../frameworks/value-equation.md) sem expor a margem ao oportunista: o risco vai para o vendedor, mas só para o cliente que age. É o degrau 1 e 3 da [escada de reversão de risco](../../frameworks/risk-reversal-ladder.md). Explora o princípio de **compromisso e coerência** — ao aceitar a condição, o cliente assume um micro-compromisso que aumenta a adesão e o próprio resultado (ver [`../../reference/psychology/commitment-consistency.md`](../../reference/psychology/commitment-consistency.md)). O desenho, a definição de marcos e o teste de pior caso seguem [`../../frameworks/guarantee-design.md`](../../frameworks/guarantee-design.md); cada promessa aponta para evidência ([`../../frameworks/proof-to-claim-chain.md`](../../frameworks/proof-to-claim-chain.md)). A garantia de serviço ("seguimos até funcionar") é especialmente forte porque transfere o risco de **execução**, não só de dinheiro.

## Padrão reutilizável
Esqueleto em redação original, com placeholders para preencher:

```
[RISCO NOMEADO] Talvez você pense: "e se eu {{esforço_do_cliente}} e {{resultado}} não vier?".
[PROMESSA] Em {{prazo}}, você {{resultado_específico_e_mensurável}}.
[CONDIÇÃO] Tudo que peço é que você {{marco_verificável_1}} e {{marco_verificável_2}}.
[CONSEQUÊNCIA] Se cumprir isso e não {{resultado}}, {{gesto: devolvo / dobro / seguimos juntos de graça até você conseguir}}.
[PROVA] Foi o que aconteceu com {{cliente_com_nome}}, que {{cumpriu_e_atingiu_o_resultado}}.
```

Antes de publicar: o `unit-economics-stack-analyst` simula a taxa de acionamento contra a margem; defina marcos verificáveis (sessões concluídas, entregas feitas) para fechar brechas; o `compliance-auditor` confirma exequibilidade.

## Adaptação por sofisticação
Conforme [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md):
- **Sofisticação 1-2** — uma condicional simples basta: "faça as aulas e, se não {{resultado}}, devolvo". O mercado ainda acredita.
- **Sofisticação 3** — ancore a condição no **mecanismo**: "complete as {{N}} sessões de {{mecanismo}} — se não funcionar, seguimos juntos". A condição prova que o mecanismo é o caminho.
- **Sofisticação 4** — eleve para a **garantia de serviço** ("trabalho de graça até você conseguir") ou suba na [escada](../../frameworks/risk-reversal-ladder.md): o público viu garantias demais e a de execução diferencia.
- **Sofisticação 5** — pese a garantia em **performance/parceria** (tipo 13: "só ganho se você ganhar") e em prova social: a condição vira aliança de incentivos, não cláusula.

## Fonte
> **Fonte:** Estrutura das garantias condicionais (serviço, primeiro resultado, dobro) derivada do capítulo de Garantias de Alex Hormozi, *$100M Offers* (2021) — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
