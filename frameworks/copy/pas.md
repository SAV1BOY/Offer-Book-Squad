---
id: framework.copy.pas
title: "PAS — Problema, Agitação, Solução"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [copy.aida, copy.pastor, copy.hook-frameworks, copy.close-frameworks, awareness-x-sophistication]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
  - "Dan S. Kennedy, *The Ultimate Sales Letter* (4ª ed., 2011)."
tags: [copy, pas, problem, agitation, solution, structure]
---

# PAS — Problema, Agitação, Solução

## TL;DR
PAS é o esqueleto mais rápido para mercado **consciente do problema**. Três movimentos: **Problema** (nomeie a dor na voz do avatar), **Agitação** (aprofunde a consequência até doer), **Solução** (apresente a saída — seu mecanismo e oferta). Vence quando a dor é latente, real e nomeável, e o público frio precisa sentir o custo de não agir antes de querer a cura. Não é o melhor esqueleto para público quente que já quer comprar — aí use [`aida`](aida.md) ou um lead de Oferta direto.

## Quando usar / Quando não
**Use** com consciência 1-3 (Inconsciente, Consciente do problema, Consciente da solução — ver [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md)): o público sente a dor mas ainda não decidiu agir.
**Use** em anúncios de tráfego frio, e-mails de reativação, aberturas de VSL e cartas onde a dor é o gatilho de leitura.
**Use** quando a emoção dominante do avatar é frustração, medo ou vergonha — emoções que a Agitação amplifica.
**Não use** sozinho com consciência 4-5: quem já quer comprar não precisa de agitação, precisa de oferta e prova. Migre para [`aida`](aida.md) ou [`close-frameworks`](close-frameworks.md).
**Não use** quando a dor não é nomeável ou socialmente admitida — aí a agitação soa manipuladora. Prefira [`pastor`](pastor.md), que abre por história e empatia.

## Inputs
- A **dor dominante** em verbatim do banco de VOC do `avatar-voc-investigator` (ver [`../avatar-voc-investigator/voc-mining.md`](../avatar-voc-investigator/voc-mining.md)).
- A **emoção dominante** validada (frustração, medo, vergonha, raiva).
- O **nível de consciência** travado ([`awareness-levels`](../../lib/taxonomies/awareness-levels.md)) e o **lead** ([`lead-types`](../../lib/taxonomies/lead-types.md)).
- O **mecanismo único** e a **oferta** desenhados (saem do Offer Book).
- Pelo menos uma **prova** por claim da Solução ([`../proof-to-claim-chain.md`](../proof-to-claim-chain.md) — forward-ref).
- O **mapa de objeção-crença** para não agitar a dor errada ([`../avatar-voc-investigator/objection-belief-mapping.md`](../avatar-voc-investigator/objection-belief-mapping.md)).

## Procedimento
1. **Problema** — nomeie a dor exatamente como o avatar a descreve. Use o verbatim literal do VOC. Teste de espelho: o leitor pensa "é isso, é comigo"? Se ele não se reconhece, o resto não importa.
2. **Agitação** — aprofunde a consequência. Mostre o que a dor custa hoje, amanhã e em um ano se nada mudar. Use cenários concretos, não adjetivos. A agitação é verdade desconfortável, nunca medo inventado.
3. **Vire a chave** — no pico da dor, faça a ponte: "e se não tivesse que ser assim?". Esse é o momento de máxima tensão, onde a Solução entra com alívio.
4. **Solução** — apresente o mecanismo único nomeado como a saída específica. Empilhe valor, traga prova (depoimento, dado, demonstração) e mostre o "depois". Aqui você sobe as alavancas da [Value Equation](../value-equation.md): resultado e probabilidade percebida sobem, tempo e esforço caem.
5. **Feche** — um CTA único com reversão de risco e escassez/urgência **verdadeira**. Use os fechos de [`close-frameworks`](close-frameworks.md).
6. **Calibre a dose de agitação** — leia em voz alta. Frio pede mais agitação; quente pede menos. Corte qualquer agitação que não seja verdade verificável (risco de veto de compliance).

## Outputs
- Uma peça (ad, e-mail, abertura de VSL, carta) estruturada nos 3 blocos P-A-S rotulados.
- A dor mapeada ao verbatim de origem (rastreabilidade para o `compliance-auditor`).
- Mapa prova → claim no bloco Solução.
- Variações do bloco Problema (3-5 aberturas de dor) para teste, alimentando o `control-registry`.

## Exemplo
Oferta de amostra: programa de organização financeira para autônomos (consciência 2, emoção dominante = vergonha).
- **Problema**: "Você fatura bem, mas todo fim de mês a conta não fecha. E você não faz ideia para onde o dinheiro foi."
- **Agitação**: "Aí vem o boleto que você esqueceu. O cartão que estourou. A conversa que você evita ter em casa. Mais um ano assim e você trabalha o dobro pra ganhar o mesmo — sem reserva, sem sono, com a sensação de que está sempre devendo a si mesmo."
- **Solução**: "O Caixa no Azul é um método de 3 contas que separa o dinheiro **antes** de você gastar. Como a Letícia, designer, que saiu do vermelho em 6 semanas e hoje tem 4 meses de reserva." (mecanismo nomeado; depoimento = prova.)
- **Fecho**: "Comece o Caixa no Azul hoje. Primeira semana grátis. Se em 30 dias você não souber exatamente para onde vai cada real, devolvo seu dinheiro. Clique em Quero Sair do Vermelho."

## Armadilhas
- **Problema genérico.** "Você quer mais sucesso?" não espelha ninguém. Use o verbatim exato; especificidade é reconhecimento.
- **Agitação falsa ou exagerada.** Inventar consequência catastrófica vira manipulação e veto de compliance. Agite só o que é verdade.
- **Pular a Agitação.** Ir direto de Problema para Solução perde o público que ainda não sente urgência de mudar.
- **Solução sem prova.** Depois de abrir a ferida, prometer cura sem lastro aumenta o ceticismo. Cada claim precisa de prova.
- **Agitar a dor errada.** Sem o mapa de objeção-crença, você amplifica uma dor secundária e perde a principal.
- **PAS em público quente.** Quem já quer comprar se irrita com agitação. Detecte consciência 4-5 e migre para oferta direta.

## Interações
- **Agentes**: `vsl-webinar-scriptwriter` (PAS como abertura de VSL para tráfego frio), `email-sms-sequence-writer` (e-mails de reativação e de dor), `ad-creative-factory` (anúncios de problema para tráfego frio), `avatar-voc-investigator` (fornece a dor e a emoção dominante), `big-idea-architect` (a Big Idea reformula o Problema como tese).
- **Frameworks que pareiam**: [`aida`](aida.md) (transição depois que a dor é aceita), [`pastor`](pastor.md) (quando a dor precisa de história e empatia antes da agitação), [`hook-frameworks`](hook-frameworks.md) (variações do bloco Problema), [`fascination-bullets`](fascination-bullets.md) (constroem a Solução), [`close-frameworks`](close-frameworks.md) (o fecho), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md) (calibra a dose de agitação por célula).

## Fontes
> **Fonte:** Estrutura Problema-Agitação-Solução consolidada na copy de resposta direta; fundamentos de consciência em Eugene M. Schwartz, *Breakthrough Advertising* (1966), e de carta de vendas em Dan S. Kennedy, *The Ultimate Sales Letter* (4ª ed., 2011) — via [`../../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../../reference/books/copywriting/schwartz-breakthrough-advertising.md) e [`../../reference/books/copywriting/kennedy-ultimate-sales-letter.md`](../../reference/books/copywriting/kennedy-ultimate-sales-letter.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
