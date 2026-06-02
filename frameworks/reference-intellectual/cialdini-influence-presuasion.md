---
id: framework.reference-intellectual.cialdini-influence-presuasion
title: "Cialdini — 7 Princípios + Pré-Suasão Aplicados a Ofertas"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [proof-to-claim-chain, scarcity-urgency-engine, big-idea-generator, money-model-sequence]
sources:
  - "Robert B. Cialdini, *Influence* (New and Expanded, 2021), Harper Business; *Pre-Suasion* (2016), Simon & Schuster."
tags: [cialdini, persuasion, presuasion, reciprocity, social-proof, authority, scarcity, unity, ethics]
---

# Cialdini — 7 Princípios + Pré-Suasão Aplicados a Ofertas

## TL;DR
Cialdini dá duas coisas ao squad: **7 alavancas** de persuasão ética (reciprocidade, compromisso, prova social, autoridade, afinidade, escassez, unidade) e o **momento privilegiado** da pré-suasão — a janela, antes da mensagem, em que se controla o foco e se inclina a decisão. Este framework mapeia cada princípio a um componente da oferta e cada abertura a um frame que pré-suade. A régra de ouro: a alavanca só é ética quando aponta para um **fato real**. Vence quando você precisa converter sem manipular — gatilho verdadeiro, prova rastreável.

## Quando usar / Quando não
**Use** ao desenhar a sequência de uma VSL/webinar, ao escolher o frame de abertura e ao decidir onde cada prova entra.
**Use** a pré-suasão antes de qualquer pitch: a primeira pergunta, cena ou dado decide quanto do resto será crível.
**Use** os 7 princípios como checklist de "que alavanca esta peça aciona e com que fato".
**Não use** para fabricar o gatilho: escassez sem limite real, autoridade sem lastro e prova social inventada são veto de compliance.
**Não use** como único motor — Cialdini ativa alavancas que já existem; sem oferta forte (Hormozi) e mercado certo (Schwartz/Halbert), não há o que alavancar.
**Fit:** funciona em qualquer sofisticação, mas a **unidade** ganha peso em mercado maduro, onde identidade vence promessa.

## Inputs
- O banco de VOC e o `proof-registry` (prova social e autoridade rastreáveis).
- O mapa de objeções do avatar.
- A escassez/urgência **verdadeira** disponível (datas, estoques, vagas reais).
- A Big Idea e o frame de abertura candidato — ver [`../big-idea-generator.md`](../big-idea-generator.md).
- A categoria e a tribo do produto (para a unidade) — ver positioning.

## Procedimento
1. **Desenhe a pré-suasão primeiro.** Escolha o **abridor** — pergunta, cena ou dado — que eleva em atenção o conceito que você quer vender antes de vendê-lo. O que recebe foco ganha peso.
2. **Ative Reciprocidade.** Entregue valor real **antes** do pedido (lead magnet, conteúdo, amostra). O primeiro gesto genuíno e inesperado cria o dever de retribuir.
3. **Construa Compromisso e Coerência.** Sequencie micro-compromissos (opt-in, pergunta no webinar, pequeno "sim" público) que puxam o "sim" maior.
4. **Posicione Prova Social.** Insira depoimentos e números reais de pares semelhantes ("muitos como você") no momento de maior incerteza do prospect.
5. **Demonstre Autoridade.** Mostre credenciais e resultados verificáveis — e admita uma pequena falha antes do ponto forte, que aumenta a credibilidade.
6. **Cultive Afinidade.** Use a história de origem e a voz que espelha o mercado: gostamos de quem é parecido, coopera e elogia.
7. **Acione Escassez (verdadeira).** No fechamento, limite real de vaga, tempo ou estoque — a aversão à perda faz o trabalho. Ver [`../scarcity-urgency-engine.md`](../scarcity-urgency-engine.md).
8. **Estabeleça Unidade.** Defina o "nós" partilhado: a tribo, a causa, o lugar. Unidade não é "parecido com", é "um dos nossos".
9. **Audite a régua ética.** Para cada alavanca acionada, aponte o fato que a sustenta. Sem fato → corte ou corrija (red-team do `compliance-auditor`).

## Outputs
- O **frame de abertura** pré-suasivo, único, ligado à Big Idea.
- O **mapa de alavancas**: cada princípio → onde entra na sequência → com qual prova/fato.
- A **escada de micro-compromissos** do opt-in ao CTA.
- O veredito ético por alavanca: sustentada por fato / a corrigir / cortada.

## Exemplo
Oferta de amostra: programa para freelancers conseguirem clientes melhores.
- **Pré-suasão**: a VSL abre com a pergunta "Quanto do seu mês some perseguindo cliente que some?" — eleva em atenção a dor de instabilidade antes do pitch.
- **Reciprocidade**: entrega de graça o template de proposta que já fecha contratos.
- **Coerência**: pede um micro-compromisso ("comente sua maior dor de prospecção").
- **Prova social**: três freelancers como o avatar, com prints reais de contratos fechados.
- **Autoridade**: o mentor mostra os números próprios e admite "minha primeira oferta foi um desastre" antes do método.
- **Afinidade**: história de origem de quem já viveu a mesma instabilidade.
- **Escassez**: turma de 20 vagas reais, fecha sexta — data verdadeira.
- **Unidade**: "freelancers que escolhem clientes, não imploram por eles" — a tribo.
- **Resultado**: cada alavanca aponta para um fato verificável; o `compliance-auditor` aprova porque nada foi inventado.

## Armadilhas
- **Gatilho sobre fato falso.** Escassez inventada, autoridade sem lastro, prova social fabricada — veto imediato.
- **Pré-suasão sem entrega.** Frame que promete o que a oferta não cumpre vira isca enganosa e quebra a confiança.
- **Empilhar princípios sem foco.** Acionar os 7 ao mesmo tempo dilui; escolha os que o avatar precisa.
- **Confundir afinidade com unidade.** Afinidade é semelhança; unidade é identidade compartilhada. A segunda pesa mais.
- **"Sim" cedo e frágil.** Compromisso só ganha força se for ativo, público e voluntário.

## Interações
- **Agentes** (de `config.yaml`): `positioning-lead-strategist` (desenha Unidade e Autoridade na posição); `vsl-webinar-scriptwriter` (sequencia Reciprocidade, Coerência e Prova Social; abertura como momento privilegiado); `big-idea-architect` (define o frame de abertura único); `email-sms-sequence-writer` (Escassez verdadeira no fechamento de carrinho); `proof-credibility-curator` (abastece Prova Social e Autoridade rastreáveis); `ad-creative-factory` (testa abridores que pré-suadem o clique); `compliance-auditor` (**veta** princípio sobre fato falso).
- **Frameworks que pareiam**: [`../proof-to-claim-chain.md`](../proof-to-claim-chain.md) (lastro da prova social/autoridade), [`../scarcity-urgency-engine.md`](../scarcity-urgency-engine.md) (escassez verdadeira), [`../big-idea-generator.md`](../big-idea-generator.md) e [`../power-of-one.md`](../power-of-one.md) (o frame pré-suasivo); e as referências [`kahneman-thinking-fast-slow.md`](kahneman-thinking-fast-slow.md) (Sistema 1 sob os atalhos) e [`voss-never-split-difference.md`](voss-never-split-difference.md) (reciprocidade e afinidade na negociação).

## Fontes
> **Fonte:** Robert B. Cialdini, *Influence* (New and Expanded, 2021), Harper Business, e *Pre-Suasion* (2016), Simon & Schuster — via [`../../reference/books/persuasion-psychology/cialdini-influence.md`](../../reference/books/persuasion-psychology/cialdini-influence.md) e [`../../reference/books/persuasion-psychology/cialdini-presuasion.md`](../../reference/books/persuasion-psychology/cialdini-presuasion.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
