---
id: framework.unique-mechanism
title: "Unique Mechanism — Mecanismo do Problema + da Solução (5 Whys)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
frameworks: [value-equation, awareness-x-sophistication, big-idea-generator, proof-to-claim-chain, magic-naming]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966) — mecanismo na sofisticação 3-4."
  - "Sakichi Toyoda — técnica dos '5 Whys' (Toyota Production System)."
tags: [mechanism, problem-mechanism, solution-mechanism, 5-whys, sophistication]
---

# Unique Mechanism — O Mecanismo Único

## TL;DR
Em mercado saturado, ninguém acredita mais no **claim**. A virada é o **mecanismo**: o *como* e o *porquê* — explicar **por que o problema persiste** (mecanismo do problema) e **por que a sua solução funciona quando o resto falhou** (mecanismo da solução). Você usa os **5 Whys** para cavar a causa-raiz e nomear um mecanismo proprietário. É o que move mais as alavancas de Tempo e Esforço da [Value Equation](value-equation.md). O `mechanism-architect` é o dono; em sofisticação 3-4, sem mecanismo nomeado e provado, a oferta é invisível.

## Quando usar / Quando não
**Use** em sofisticação 3-4 (a maioria dos mercados modernos) — ver [`../lib/taxonomies/sophistication-levels.md`](../lib/taxonomies/sophistication-levels.md).
**Use** sempre que o avatar já tentou e falhou: o mecanismo do problema explica **por que não foi culpa dele**, e isso destrava a crença.
**Não use** mecanismo "de fachada" — nome bonito sem substância real é veto de compliance e quebra na prova.
**Não use** em sofisticação 1-2 com a mesma intensidade: lá o claim direto ainda vence; mecanismo pesado pode complicar à toa.

## Inputs
- O **problema dominante** do avatar e o histórico de tentativas falhas (banco de VOC).
- A **causa-raiz real** do problema (pesquisa, dado, expertise do especialista).
- O **diferencial verdadeiro** da sua solução (o que ela faz que as outras não fazem).
- Prova de que o mecanismo funciona ([`proof-to-claim-chain.md`](proof-to-claim-chain.md)).
- O estágio de [sofisticação](awareness-x-sophistication.md) do mercado.

## Procedimento
1. **Declare o problema na superfície** como o avatar o vê ("não consigo emagrecer", "travo na entrevista").
2. **Aplique os 5 Whys** para descer à causa-raiz: pergunte "por quê?" cinco vezes, cada resposta alimentando a próxima, até chegar ao mecanismo **real** do problema (ex.: "porque sob estresse a memória de recuperação falha", não "porque estudou pouco").
3. **Nomeie o mecanismo do problema**: dê um nome ao inimigo oculto ("o Gargalo da Recuperação"). Isso reenquadra a falha como **sistêmica**, não pessoal — destrava a crença.
4. **Derive o mecanismo da solução**: a sua abordagem que ataca **exatamente** aquela causa-raiz. Por que ela funciona quando o resto não funcionou?
5. **Nomeie o mecanismo da solução** de forma proprietária ("Método Shadowing Técnico"). O nome vira ativo de marca e Magnetic-reason ([`magic-naming.md`](magic-naming.md)).
6. **Conecte às alavancas**: mostre como o mecanismo derruba **Tempo** e **Esforço** e sobe **Probabilidade** na [Value Equation](value-equation.md).
7. **Prove o mecanismo**: cada afirmação sobre o "como" aponta para evidência (estudo, demonstração, resultado). Mecanismo sem prova é só jargão.
8. **Destile em uma frase**: "o problema é X (mecanismo do problema); a solução é Y (mecanismo da solução)". Rode `mechanism/mechanism-one-sentence-gate`.
9. **Registre** os dois mecanismos e suas provas no `offer-registry`; rode `mechanism/mechanism-naming-gate` e `mechanism/mechanism-proof-gate`.

## Outputs
- **Mecanismo do problema** nomeado (o inimigo oculto) + a cadeia dos 5 Whys.
- **Mecanismo da solução** nomeado (proprietário) + por que funciona.
- A frase única que une os dois.
- Mapa mecanismo → alavancas da Value Equation.
- Prova ligada a cada afirmação do mecanismo.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Problema na superfície**: "estudo inglês, mas travo na entrevista".
- **5 Whys**: Por que trava? → fica nervoso. Por quê? → medo de errar ao vivo. Por quê? → nunca praticou o **formato** de entrevista. Por quê? → cursos ensinam gramática, não simulação sob pressão. Por quê? → ninguém treina a **recuperação de vocabulário sob estresse**. → **Causa-raiz**.
- **Mecanismo do problema**: "o **Gargalo da Recuperação**" — sob estresse, a memória passiva não vira fala. Reenquadra: não é falta de inglês, é falta de treino do formato.
- **Mecanismo da solução**: "**Shadowing Técnico**" — repetição sombreada de entrevistas reais que converte memória passiva em fala automática sob pressão.
- **Alavancas**: derruba Tempo (resultado em semanas, não anos) e Esforço (sem decorar gramática), sobe Probabilidade.
- **Frase única**: "Você não trava por saber pouco inglês — trava no Gargalo da Recuperação; o Shadowing Técnico resolve isso."

## Armadilhas
- **Mecanismo de fachada.** Nome bonito sem substância quebra na prova e é veto de compliance.
- **Parar no primeiro 'porquê'.** A causa-raiz costuma estar 4-5 níveis abaixo; pare cedo e o mecanismo fica raso.
- **Nomear só a solução, esquecer o problema.** O mecanismo do **problema** é o que destrava a crença de quem já falhou.
- **Mecanismo sem prova.** Sem evidência, vira jargão e não move Probabilidade.
- **Mecanismo que não muda alavanca.** Se não derruba Tempo/Esforço nem sobe Probabilidade, não é diferencial — é decoração.

## Interações
- **Agentes**: `mechanism-architect` (dono — isola e nomeia os dois mecanismos); `market-sophistication-analyst` (indica quando o mercado exige mecanismo); `value-equation-engineer` (mede o impacto nas alavancas); `big-idea-architect` (o mecanismo alimenta a novidade e a propriedade da Big Idea); `proof-credibility-curator` (sustenta cada afirmação do mecanismo); `vsl-webinar-scriptwriter` (ensina o mecanismo no corpo da copy).
- **Frameworks que pareiam**: [`value-equation.md`](value-equation.md), [`awareness-x-sophistication.md`](awareness-x-sophistication.md), [`big-idea-generator.md`](big-idea-generator.md), [`proof-to-claim-chain.md`](proof-to-claim-chain.md), [`magic-naming.md`](magic-naming.md).

## Fontes
> **Fonte:** Eugene M. Schwartz, *Breakthrough Advertising* (1966), mecanismo na sofisticação 3-4; técnica dos "5 Whys" de Sakichi Toyoda (Toyota) — via [`../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../reference/books/copywriting/schwartz-breakthrough-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
