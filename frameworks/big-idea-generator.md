---
id: framework.big-idea-generator
title: "Big Idea Generator — Nova, Grande, Crível, Relevante, Proprietária"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [power-of-one, awareness-x-sophistication, unique-mechanism, lead-types, meta-launch-principle]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966) — a Grande Ideia."
  - "David Ogilvy, *Ogilvy on Advertising* (1983) — 'big ideas'."
tags: [big-idea, ideation, new-big-credible, proprietary, hook]
---

# Big Idea Generator — Gerando a Grande Ideia

## TL;DR
A Grande Ideia é a única tese que carrega o lançamento — o gancho central que faz o mercado parar e prestar atenção. Uma Big Idea forte passa em cinco testes: é **Nova** (fresca, não batida), **Grande** (importa de verdade), **Crível** (o avatar acredita), **Relevante** (fala da dor dele) e **Proprietária** (só você pode dizer). Você gera muitas e seleciona **uma** ([Power of One](power-of-one.md)). O `big-idea-architect` é o dono; entrega UMA tese — múltiplas reprovam.

## Quando usar / Quando não
**Use** depois do diagnóstico de mercado e do mecanismo, antes de copy e posicionamento.
**Use** quando o controle atual cansou: nova Big Idea é o caminho para reanimar uma oferta saturada (sofisticação 4-5).
**Não use** para gerar dez ideias e usar todas — o output é **uma** (`one_big_idea`).
**Não use** ideia "nova" que o avatar não acredita: novidade sem credibilidade vira curiosidade vazia, não conversão.

## Inputs
- O **mecanismo único** nomeado ([`unique-mechanism.md`](unique-mechanism.md)) — costuma ser a fonte da novidade.
- A célula de [consciência × sofisticação](awareness-x-sophistication.md) (define quão "nova" a ideia precisa ser).
- A dor e o desejo dominantes (banco de VOC) — para a Relevância.
- A prova disponível ([`proof-to-claim-chain.md`](proof-to-claim-chain.md)) — para a Credibilidade.
- O que **só você** tem (história, dado, método) — para a propriedade.

## Procedimento
1. **Reúna a matéria-prima**: mecanismo, VOC, prova, sua história única. A Big Idea nasce do cruzamento desses, não do nada.
2. **Gere em quantidade (divergir)**: produza 15-30 ângulos de Big Idea. Use gatilhos: "e se o problema real fosse X?", "o inimigo escondido", "o segredo do mecanismo", "a nova oportunidade". Quantidade primeiro, julgamento depois.
3. **Pontue cada candidata nos 5 testes** (0-5 cada): Nova, Grande, Crível, Relevante, Proprietária. Some.
4. **Filtre a Credibilidade com prova**: corte toda ideia cuja crença a prova não sustenta — por mais sedutora que seja.
5. **Filtre a Relevância com VOC**: a ideia fala da dor que o avatar **realmente** tem (em verbatim)? Se não, descarte.
6. **Cheque a Propriedade**: a ideia poderia sair da boca do concorrente igual? Se sim, não é proprietária — afie até só você poder dizê-la (ancore no seu mecanismo/história).
7. **Ajuste a Novidade à célula**: sofisticação baixa tolera ideia simples; alta exige reenquadramento (novo mecanismo, novo inimigo, nova categoria).
8. **Selecione UMA** (a de maior soma que passa em todos os pisos) e formule em uma frase-tese. As demais vão para o banco.
9. **Registre** a vencedora e as descartadas no `big-idea-registry`; rode `big-idea/big-idea-new-big-credible-gate` e `big-idea/big-idea-single-gate`.

## Outputs
- **A Big Idea única**, em uma frase-tese, ancorada no mecanismo/história.
- A **tabela de pontuação** (candidata × 5 testes) que justifica a escolha.
- Banco de ideias descartadas (matéria para outras peças/testes).
- Veredito dos gates de Big Idea (nova-grande-crível + única).

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI. Mercado em sofisticação 4 (muitos métodos).
- Candidatas geradas (amostra): (a) "fluência em 30 dias", (b) "inglês com IA", (c) **"você não precisa de fluência — precisa passar na entrevista"**, (d) "o inglês que as big techs testam".
- Pontuação: (a) Nova 1 / Crível 2 — batida e exagerada → descarte. (b) Nova 3 / Proprietária 1 — todo mundo já diz "IA" → descarte. (c) Nova 5 / Grande 5 / Crível 5 / Relevante 5 / Proprietária 4 → **vencedora**. (d) forte, mas vira **apoio** de (c).
- **Por que (c) vence**: reenquadra o problema (entrevista > fluência genérica), é crível (o dev sabe que trava na entrevista), relevante (a dor é a vaga) e proprietária (ancorada no mecanismo "Shadowing Técnico").
- **Frase-tese**: "Pare de tentar virar fluente. Aprenda a passar na entrevista técnica em inglês com Shadowing Técnico."

## Armadilhas
- **Confundir 'nova' com 'estranha'.** Novidade que o avatar não entende nem acredita não converte.
- **Sacrificar credibilidade pela ousadia.** A ideia mais "uau" que a prova não sustenta queima o lançamento.
- **Ideia que o concorrente pode copiar igual.** Sem propriedade, vira commodity. Ancore no seu mecanismo/história.
- **Sair com várias Big Ideas.** O output é **uma**. Múltiplas = reprovação.
- **Pular o passo divergente.** Sem gerar muitas, você prende na primeira (e geralmente óbvia).

## Interações
- **Agentes**: `big-idea-architect` (dono — gera e seleciona UMA); `mechanism-architect` (o mecanismo alimenta a novidade e a propriedade); `positioning-lead-strategist` (deriva lead e posicionamento da ideia); `proof-credibility-curator` (sustenta a credibilidade); `vsl-webinar-scriptwriter` e `ad-creative-factory` (transformam a ideia em gancho).
- **Frameworks que pareiam**: [`power-of-one.md`](power-of-one.md), [`awareness-x-sophistication.md`](awareness-x-sophistication.md), [`unique-mechanism.md`](unique-mechanism.md), [`lead-types.md`](lead-types.md), [`meta-launch-principle.md`](meta-launch-principle.md).

## Fontes
> **Fonte:** Eugene M. Schwartz, *Breakthrough Advertising* (1966), a Grande Ideia; David Ogilvy, *Ogilvy on Advertising* (1983), "big ideas" — via [`../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../reference/books/copywriting/schwartz-breakthrough-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
