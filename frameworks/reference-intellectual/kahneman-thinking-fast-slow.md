---
id: framework.reference-intellectual.kahneman-thinking-fast-slow
title: "Kahneman — Vieses na Decisão de Compra (Sistema 1 e 2)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [price-anchoring, scarcity-urgency-engine, guarantee-design, proof-to-claim-chain]
sources:
  - "Daniel Kahneman, *Thinking, Fast and Slow* (2011), Farrar, Straus and Giroux, ISBN 978-0-374-27563-1."
tags: [kahneman, system-1, system-2, anchoring, loss-aversion, availability, wysiati, biases, pricing]
---

# Kahneman — Vieses na Decisão de Compra (Sistema 1 e 2)

## TL;DR
A mente tem duas marchas. O **Sistema 1** é rápido, automático e emocional — responde antes de você pensar. O **Sistema 2** é lento, deliberado e preguiçoso — só entra quando chamado, e muitas vezes apenas endossa o que o Sistema 1 já decidiu. O comprador acredita que escolhe com a razão; na prática, sente primeiro e justifica depois. Isso abre vieses **previsíveis**: ancoragem, aversão à perda, disponibilidade, WYSIATI. Este framework é a base cognitiva do squad para projetar oferta, preço e prova: escreva fácil para o Sistema 1 e dê ao Sistema 2 a prova que ele pede. Vence quando a decisão é emocional e a régua ética precisa segurar.

## Quando usar / Quando não
**Use** ao desenhar ancoragem de preço, escassez/garantia honestas e a entrega de prova no ponto certo.
**Use** para diagnosticar **atrito cognitivo**: onde a peça exige demais do Sistema 2 e cansa o comprador.
**Use** para escolher histórias vívidas (disponibilidade) em vez de só médias, e para controlar o frame (WYSIATI).
**Não use** para fabricar o gatilho: o Sistema 1 é fácil de enganar, e enganar é exatamente o que o `compliance-auditor` veta.
**Não use** como substituto da oferta ou do diagnóstico de mercado — Kahneman explica **por que** as alavancas funcionam, não monta o stack.
**Fit:** universal; sustenta cognitivamente Cialdini, Voss e a ancoragem de preço de Ramanujam/Nagle.

## Inputs
- A faixa de preço derivada de WTP e a referência de **âncora alta verdadeira**.
- A escassez/urgência **real** (vagas, prazos) e a garantia disponível.
- O `proof-registry` com histórias vívidas e verificáveis (não só estatísticas).
- A voz padrão de 3ª série (fluência alta) — ver [`../../docs/style-guide.md`](../../docs/style-guide.md).
- O mapa de objeções (o momento em que o Sistema 2 desperta para objetar).

## Procedimento
1. **Escreva para o Sistema 1.** Use clareza de 3ª série, frases curtas e alta **fluência** — o que é fácil de ler e pronunciar parece mais crível. Simplicidade é persuasão.
2. **Antecipe o despertar do Sistema 2.** No instante em que o comprador para para objetar, entregue a **prova** que ele pede, para que ele não reclame.
3. **Ancore com referência alta verdadeira.** Mostre o valor total e o "preço justo" **antes** do preço real. O primeiro número molda a faixa toda — mesmo sabido arbitrário, ele desloca o julgamento.
4. **Acione aversão à perda (honesta).** Perder pesa cerca de **duas vezes** mais que ganhar o equivalente. Use o medo real de perder a vaga e a remoção do risco (garantia) — ambos lastreados.
5. **Use disponibilidade com histórias.** Casos vívidos e recentes pesam mais que a média correta. A prova social usa **histórias concretas**, não só números.
6. **Controle o frame (WYSIATI).** A mente conclui com a informação à mão e ignora o que falta. Apresente o frame certo, com fato — controle o que está à vista e você inclina a conclusão.
7. **Audite a régua ética.** Para cada viés acionado, aponte o fato que o sustenta. Âncora inflada sem base, escassez inventada ou caso fabricado → corte (red-team do `compliance-auditor`).
8. **Registre** a âncora, a história e a objeção tratada nos registries correspondentes.

## Outputs
- O **mapa de vieses → mecânica da oferta**: ancoragem, aversão à perda, disponibilidade, WYSIATI, cada um com o fato que o lastreia.
- A **estrutura de ancoragem de preço** (sequência valor total → justo → real).
- A **seleção de provas vívidas** para a disponibilidade.
- A **nota de fluência**: onde a peça foi simplificada para o Sistema 1.

## Exemplo
Oferta de amostra: programa de preparação para concurso público.
- **Sistema 1 (fluência)**: a página abre com frase curta — "Estudar muito não é estudar certo." Fácil de ler, soa verdadeira.
- **Sistema 2 (prova no ponto)**: quando surge a dúvida "será que funciona pra mim?", entra o caso de aprovados com perfil igual ao do avatar.
- **Ancoragem**: mostra primeiro o custo de **mais um ano** reprovado (tempo, salário perdido) — âncora alta real — depois o preço do curso, que parece pequeno.
- **Aversão à perda**: turma com data real de fechamento e garantia "passou de fase ou seguimos juntos" — remove o risco de perder o dinheiro.
- **Disponibilidade**: depoimento vívido de quem passou após três reprovações, não só "85% de aprovação".
- **WYSIATI**: o frame destaca o método (o que está à vista), com prova — sem esconder o esforço necessário.
- **Resultado**: o `compliance-auditor` aprova porque cada viés aponta para um fato.

## Armadilhas
- **Exigir muito do Sistema 2.** Copy densa e jargão cansam e perdem a venda; simplifique.
- **Âncora sem base.** Número alto inventado para inflar a percepção é viés sobre fato falso — veto.
- **Só estatística.** A média correta perde para a história lembrada; use casos vívidos **verdadeiros**.
- **Escassez fabricada.** Aversão à perda só é honesta sobre limite real (vaga, prazo).
- **Frame que esconde.** WYSIATI manipulado — omitir o que importa para forçar a conclusão — quebra a confiança.
- **Confiar no Sistema 1 do comprador para enganar.** O mesmo atalho que persuade também engana; a régua ética é inegociável.

## Interações
- **Agentes** (de `config.yaml`): `pricing-wtp-strategist` (ancoragem com âncora alta verdadeira antes do preço real); `vsl-webinar-scriptwriter` (escreve para o Sistema 1 e entrega prova quando o Sistema 2 desperta); `email-sms-sequence-writer` (aversão à perda no fechamento com prazos e vagas reais); `proof-credibility-curator` (abastece a disponibilidade com histórias vívidas e verificáveis); `compliance-auditor` (**veta** viés sobre fato falso — âncora inflada, escassez inventada, caso fabricado).
- **Frameworks que pareiam**: [`../price-anchoring.md`](../price-anchoring.md) (a âncora como ferramenta de preço), [`../scarcity-urgency-engine.md`](../scarcity-urgency-engine.md) (aversão à perda honesta), [`../guarantee-design.md`](../guarantee-design.md) (remover o risco), [`../proof-to-claim-chain.md`](../proof-to-claim-chain.md) (disponibilidade rastreável); e as referências [`cialdini-influence-presuasion.md`](cialdini-influence-presuasion.md) (as armas que operam sobre o Sistema 1) e [`voss-never-split-difference.md`](voss-never-split-difference.md) (ancoragem e perda na negociação).

## Fontes
> **Fonte:** Daniel Kahneman, *Thinking, Fast and Slow* (2011), Farrar, Straus and Giroux, ISBN 978-0-374-27563-1 — via [`../../reference/books/persuasion-psychology/kahneman-thinking-fast-slow.md`](../../reference/books/persuasion-psychology/kahneman-thinking-fast-slow.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
