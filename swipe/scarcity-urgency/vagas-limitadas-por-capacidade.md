---
id: swipe.scarcity-urgency.vagas-limitadas-por-capacidade
title: "Padrão: Vagas Limitadas por Capacidade Real"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [scarcity-urgency-engine, value-equation, offer-to-funnel-mapping, proof-to-claim-chain]
sources:
  - "Robert Cialdini, *Influence* (1984) — princípio da Escassez."
  - "Alex Hormozi, *$100M Offers* (2021), seções de Escassez."
tags: [swipe, scarcity, capacity, cohort, truthful, quantity, compliance]
---

# Padrão: Vagas Limitadas por Capacidade Real

## O que é
Este é o **padrão estrutural de escassez de quantidade ancorada na capacidade real** de atendimento. O limite não é inventado para pressionar: ele **existe porque a operação só consegue atender bem um número** — X alunos por turma, Y clientes 1:1, estoque que de fato acaba. Aqui guardamos só a **anatomia** da redação — como declarar o número, o motivo honesto e o custo de ficar de fora — em redação original, nunca copy literal de campanha alheia.

É escassez **verdadeira** por construção: quando bate o limite, a operação **para de vender**. O motivo honesto ("atendo 30 para manter o 1:1") faz dobro: comunica o limite **e** reforça o valor. Sem essa verdade, vira fraude — veto do `compliance-auditor`. Ver [`../../frameworks/scarcity-urgency-engine.md`](../../frameworks/scarcity-urgency-engine.md).

## Anatomia
A sequência de elementos que sustenta o padrão:
1. **O número real** — a quantidade exata de vagas (ex.: 30). Específico, não "poucas vagas".
2. **O motivo honesto** — por que o limite existe, ligado a valor: "porque cada aluno recebe {{entrega_personalizada}} e eu não atendo mais que isso".
3. **O custo de ficar de fora** — o que o avatar perde ao não entrar agora: a próxima turma só em {{prazo}}, o bônus que sai, o preço que sobe de verdade.
4. **A contagem viva** — quando há, a contagem que diminui de verdade conforme as vagas se preenchem (no funil, reflete inscrições reais).
5. **O fechamento real** — a declaração de que, ao bater o número, fecha mesmo: "quando fecha, fecha". E a operação cumpre.

## Por que funciona
A escassez genuína amplifica o **valor já construído** pela [Value Equation](../../frameworks/value-equation.md): torna a inação cara sem mexer no preço. Apoia-se no **princípio da escassez** de Cialdini — o que é limitado e exclusivo é percebido como mais valioso (ver [`../../reference/psychology/scarcity-principle.md`](../../reference/psychology/scarcity-principle.md)) — e na **aversão à perda**: o medo de ficar de fora pesa mais que o desejo de entrar (ver [`../../reference/psychology/loss-aversion.md`](../../reference/psychology/loss-aversion.md)). O **motivo honesto** é o que separa escassez de truque: número com razão crível converte mais que número seco, e ainda comunica valor. A prova do limite é o **cumprimento** ([`../../frameworks/proof-to-claim-chain.md`](../../frameworks/proof-to-claim-chain.md)): se a copy diz 30, a operação para em 30. O funil implementa a contagem real ([`../../frameworks/offer-to-funnel-mapping.md`](../../frameworks/offer-to-funnel-mapping.md)).

## Padrão reutilizável
Esqueleto em redação original, com placeholders para preencher:

```
[NÚMERO] Abro apenas {{N}} vagas nesta turma.
[MOTIVO HONESTO] Não é estratégia de venda: cada vaga recebe {{entrega_personalizada}}, e eu não consigo entregar isso para mais que {{N}}.
[CUSTO DE ADIAR] Quando fecha, a próxima só em {{prazo}} — e {{bônus_ou_condição}} não volta.
[CONTAGEM VIVA] Restam {{vagas_reais_no_momento}} (a contagem reflete inscrições reais).
[FECHAMENTO] Ao bater {{N}}, fecho mesmo. {{ação_de_entrar_agora}}.
```

Antes de publicar: o `money-model-designer` define o número a partir da capacidade real; o `funnel-architect` liga a contagem a inscrições reais; o `compliance-auditor` confirma que a operação **para** no limite (gate de verdade de escassez). Se o número não é real, o padrão **não** se usa.

## Adaptação por sofisticação
Conforme [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md):
- **Sofisticação 1-2** — o número simples já basta: "só {{N}} vagas". O mercado ainda reage ao limite seco.
- **Sofisticação 3** — ligue o limite ao **mecanismo**: "{{N}} vagas porque o {{mecanismo}} exige acompanhamento individual". A escassez reforça por que o método funciona.
- **Sofisticação 4** — o público viu "vagas limitadas" demais; pese o **motivo de qualidade** (por que poucos = melhor entrega) e a prova de que turmas anteriores fecharam de verdade. A razão crível diferencia.
- **Sofisticação 5** — a escassez vira **exclusividade e pertencimento**: "fazer parte deste grupo é raro". O peso sai do número e vai para o status e a prova social de quem já está dentro.

## Fonte
> **Fonte:** Princípio da Escassez de Robert Cialdini, *Influence* (1984); aplicação a vagas/capacidade em Alex Hormozi, *$100M Offers* (2021) — via [`../../reference/books/persuasion-psychology/cialdini-influence.md`](../../reference/books/persuasion-psychology/cialdini-influence.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída. Todo limite redigido por este padrão precisa ser real e cumprido (`truthful_scarcity`).
