---
id: framework.launch.runway-and-phases
title: "Runway & Phases — Pista e Fases do Lançamento"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [product-launch-formula, cart-open-close, perfect-webinar, surge-ops, affiliate-army]
sources:
  - "Jeff Walker, *Launch* (2014; ed. atualizada, 2023), Prelaunch / Launch / Postlaunch."
tags: [runway, phases, prelaunch, launch, postlaunch, timeline, calendar, walker]
---

# Runway & Phases — Pista e Fases do Lançamento

## TL;DR
Um lançamento não é um dia — é uma **pista** com fases. A pista é o tempo de aquecimento antes da venda; as fases são **Pré-Pré-Lançamento → Pré-Lançamento → Lançamento (Open Cart) → Pós-Lançamento (Close + entrega)**. Cada fase tem um objetivo, um critério de entrada e um critério de saída. O `launch-producer` usa este mapa para construir o calendário trabalhando **de trás para frente** a partir da data de fechamento. Sem pista suficiente, o público chega frio na abertura e a conversão despenca.

## Quando usar / Quando não
**Use** para planejar a linha do tempo completa de qualquer lançamento por evento — define quanto tempo de aquecimento você precisa e o que acontece em cada janela.
**Use mais** quando a lista está fria, o mecanismo é novo, ou o ticket é alto: mais sofisticação e mais preço exigem pista mais longa.
**Não use** como substituto do [`product-launch-formula.md`](product-launch-formula.md) — este detalha o **calendário e as fases**; a PLF detalha a **sequência psicológica** dentro delas.
**Não use** para improvisar sem data de fechamento fixa: sem o deadline real, não há pista para dimensionar (`truthful_scarcity`).

## Inputs
- Data-alvo de fechamento do carrinho (a âncora de todo o cálculo).
- Offer Book aprovado e Big Idea única definida.
- Tamanho e temperatura da lista (fria, morna, quente).
- Capacidade da equipe e dos parceiros (afiliados, suporte, tech).
- O evento de abertura escolhido ([`perfect-webinar.md`](perfect-webinar.md) ou VSL/página).

## Procedimento
1. **Fixe a data de fechamento** e marque-a no calendário. Tudo se calcula a partir dela (`truthful_scarcity`).
2. **Defina a duração da janela de venda** (Open→Close): tipicamente 4-7 dias. Ticket maior pede janela um pouco maior.
3. **Dimensione a pista de pré-lançamento** (3-12 dias antes da abertura): lista fria + mecanismo novo = pista mais longa; lista quente = pista curta.
4. **Aloque o Pré-Pré-Lançamento** (1-2 contatos antes da pista): tateia o mercado, ativa curiosidade, coleta objeções por enquete.
5. **Posicione os 3 Prelaunch Content (PLC)** na pista, com folga entre eles para consumo e resposta.
6. **Marque os marcos de tech e ops**: checagem de páginas, links, entregabilidade e a janela de [`surge-ops.md`](surge-ops.md) no pico.
7. **Encaixe os parceiros**: as datas de afiliados precisam caber na mesma pista ([`affiliate-army.md`](affiliate-army.md)).
8. **Defina critério de entrada e saída de cada fase**: a fase só avança quando o objetivo dela é atingido (gate `launch/launch-phase-readiness-gate`).
9. **Reserve a fase de Pós-Lançamento**: entrega, onboarding, downsell/continuidade e retrospectiva.

## Outputs
- **Calendário-mestre** com as quatro fases datadas e os marcos de cada uma.
- **Critérios de entrada/saída** por fase (checklist de prontidão).
- Janela de pico marcada para [`surge-ops.md`](surge-ops.md) e marcos de tech.
- Linha do tempo integrada com os parceiros e com a sequência de e-mail/SMS.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI. Fechamento alvo: sábado dia 15.
- **Pós-fechamento → trás**: janela de venda terça(10) a sábado(15) = 5 dias.
- **Pista de pré-lançamento**: lista morna + mecanismo novo → 9 dias. PLC1 dia 1, PLC2 dia 4, PLC3 dia 7.
- **Pré-Pré-Lançamento**: enquete dias -2 e -1 ("seu maior medo na entrevista em inglês?").
- **Tech/ops**: checagem de páginas e links dia 8; [`surge-ops.md`](surge-ops.md) armado para terça (abertura) e sábado (fechamento).
- **Afiliados**: parceiros enviam seus convites do PLC2 em diante, fechando junto no sábado.
- **Pós-lançamento**: domingo entrega + onboarding; segunda downsell para quem não comprou.
- **Resultado**: 9 dias de pista deixam o público aquecido; cada fase só avança após seu critério.

## Armadilhas
- **Pista curta demais.** Abrir para um público frio sem aquecer = conversão baixa. Lista fria precisa de mais dias.
- **Pista longa demais.** Esticar o aquecimento esfria o interesse e cansa a lista. Calibre pela temperatura.
- **Não trabalhar de trás para frente.** Começar pela data de início, não de fechamento, bagunça o deadline.
- **Fases sem critério de saída.** Avançar sem o objetivo cumprido empurra problemas para o pico.
- **Esquecer o Pós-Lançamento.** Sem onboarding e downsell, você perde LTV e a próxima venda.

## Interações
- **Agentes**: `launch-producer` (dono — monta o calendário e os critérios de fase); `email-sms-sequence-writer` (encaixa as sequências nas janelas); `events-logistics-coordinator` (logística do evento de abertura); `affiliate-program-architect` (datas dos parceiros na mesma pista); `value-equation-engineer` (cada fase move uma alavanca rumo à decisão).
- **Frameworks que pareiam**: [`product-launch-formula.md`](product-launch-formula.md) (a sequência dentro das fases), [`cart-open-close.md`](cart-open-close.md) (a fase de venda), [`perfect-webinar.md`](perfect-webinar.md), [`surge-ops.md`](surge-ops.md) (o pico), [`affiliate-army.md`](affiliate-army.md).

## Fontes
> **Fonte:** Jeff Walker, *Launch* (2014; ed. atualizada, 2023) — fases de prelaunch/launch/postlaunch — via [`../../reference/books/launches-and-funnels/walker-launch.md`](../../reference/books/launches-and-funnels/walker-launch.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
