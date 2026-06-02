---
id: framework.positioning.moore-positioning-formula
title: "Moore Positioning Formula — A Posição em Uma Frase"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [dunford-positioning, ries-trout-positioning, category-design, jtbd]
sources:
  - "Geoffrey A. Moore, *Crossing the Chasm: Marketing and Selling Disruptive Products to Mainstream Customers* (3rd ed., 2014), Harper Business, ISBN 978-0-06-229298-9."
tags: [positioning, moore, positioning-statement, formula, beachhead, one-sentence, b2b]
---

# Moore Positioning Formula — A Posição em Uma Frase

## TL;DR
A fórmula de Moore força a posição a caber numa frase que obriga **decisões reais**: "**Para [cliente-alvo] que [necessidade], o nosso [produto/categoria] é [benefício-chave]. Diferente de [alternativa], nós [diferenciação].**" Cada lacuna exige uma escolha — qual cliente, qual categoria, qual concorrente, qual resultado. Se você não consegue preencher o "diferente de", não tem diferenciação, tem esperança. É a forma curta que destila os 5 componentes de Dunford num claim auditável. O `positioning-lead-strategist` usa para travar a posição antes da copy.

## Quando usar / Quando não
**Use** para **destilar** a posição num claim único depois de mapear os 5 componentes ([`dunford-positioning.md`](dunford-positioning.md)).
**Use mais** quando precisa de uma frase de alinhamento que vendas, copy e produto repitam igual — e como teste de coerência (se não cabe na frase, a posição está vaga).
**Use mais** ao focar um **beachhead** (um nicho estreito para vencer primeiro). Ver [`../starving-crowd.md`](../starving-crowd.md).
**Não use** como **headline** de copy pronta — a frase é interna, de alinhamento; a copy a traduz no nível do avatar.
**Não use** isolada: ela resume o trabalho dos 5 componentes; sem eles, vira frase bonita sem lastro.

## Inputs
- Os 5 componentes preenchidos ([`dunford-positioning.md`](dunford-positioning.md)).
- O **beachhead** escolhido (o segmento estreito a vencer primeiro).
- A **alternativa** de referência mais relevante (o concorrente real ou o status quo).
- O **benefício-chave** provado (de [`../proof-to-claim-chain.md`](../proof-to-claim-chain.md)).
- A **categoria** escolhida ([`category-design.md`](category-design.md)).

## Procedimento
1. **Preencha [cliente-alvo].** Não "empresas" — o beachhead específico ("o dev pleno brasileiro mirando vaga remota"). Quanto mais estreito, mais forte. Liga ao mercado-alvo de Dunford.
2. **Preencha [necessidade].** A dor ou o "job" que esse cliente quer resolver, na linguagem dele ([`jtbd.md`](jtbd.md)). Tem que ser uma necessidade que ele **já sente**.
3. **Preencha [produto/categoria].** O frame em que você quer ser entendido ([`category-design.md`](category-design.md)). A categoria certa torna o benefício óbvio.
4. **Preencha [benefício-chave].** O resultado principal, **provado**. Um só — o que mais importa para o cliente-alvo. Vários benefícios = posição difusa.
5. **Preencha [alternativa].** O que o cliente usaria no seu lugar. Nomeie o concorrente real ou o status quo. Sem isto, não há contraste.
6. **Preencha [diferenciação].** O que **só você** faz e que a alternativa não faz. Esta é a lacuna decisiva: **se não consegue preencher, não tem diferenciação** — volte ao mecanismo único.
7. **Leia a frase inteira em voz alta.** Cheque a coerência: o diferenciador entrega o benefício? O benefício resolve a necessidade? A alternativa é a certa? Se algo soa vago, o componente correspondente está fraco.
8. **Teste de uma frase.** Se não cabe em uma frase clara, a posição não está decidida. Volte aos 5 componentes.
9. **Valide com vendas e clientes.** Eles "captam" em segundos? Eles concordam com o "diferente de"?
10. **Trave e registre** a frase no `decision-registry`; ela vira o contrato de posição para a Big Idea e a copy.

## Outputs
- A **frase de posicionamento** completa, preenchida e validada.
- Um **teste de coerência** dos 5 componentes (lacunas vagas viram tarefas de volta).
- O **contrato de posição** que alinha vendas, copy e produto.
- Insumo direto para a Big Idea ([`../big-idea-generator.md`](../big-idea-generator.md)).

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **[cliente-alvo]**: o desenvolvedor brasileiro pleno ou sênior
- **[necessidade]**: que quer ser contratado por uma empresa internacional remota mas trava na entrevista em inglês
- **[produto/categoria]**: nossa **preparação de entrevista técnica em inglês**
- **[benefício-chave]**: te aprova na entrevista e na vaga em 60 dias
- **[alternativa]**: diferente de apps de idioma genéricos
- **[diferenciação]**: que ensinam inglês de turista — nós treinamos exatamente a call técnica que decide a vaga, com simulação 1:1 com recrutador real.
- **Frase final**: "Para o dev brasileiro que trava na entrevista em inglês da vaga remota, a [Nome] é a preparação de entrevista técnica em inglês que te aprova em 60 dias. Diferente de apps genéricos, treinamos a call técnica real com recrutador 1:1."

## Armadilhas
- **Cliente-alvo largo.** "Profissionais" não força decisão. Estreite até o beachhead.
- **Benefícios demais.** Listar três benefícios dilui. Escolha **o** que mais importa.
- **"Diferente de" vazio.** Se não há diferenciação real, a frase expõe isso. Não maquie — conserte o produto/mecanismo.
- **Categoria genérica.** Cair na categoria default esconde o valor. Escolha o frame que favorece você.
- **Usar a frase como headline literal.** Ela é interna; a copy a traduz para a linguagem e o nível de consciência do avatar ([`../awareness-x-sophistication.md`](../awareness-x-sophistication.md)).
- **Frase sem lastro.** Cada parte (benefício, diferenciação) precisa de prova. Frase bonita sem evidência = veto.

## Interações
- **Agentes**: `positioning-lead-strategist` (dono — preenche e trava a frase); `big-idea-architect` (transforma a posição em UMA tese de lançamento); `mechanism-architect` (fornece o "diferente de"); `proof-credibility-curator` (sustenta o benefício-chave); `pricing-wtp-strategist` (a "alternativa" da frase é a mesma referência do preço por valor); `unit-economics-stack-analyst` (valida que o beachhead da frase tem unit economics viável); `vsl-webinar-scriptwriter` e `ad-creative-factory` (traduzem a frase em ganchos no nível do avatar); `compliance-auditor` (confere que o benefício e a diferenciação têm lastro).
- **Frameworks que pareiam**: [`dunford-positioning.md`](dunford-positioning.md) (os 5 componentes que a frase destila), [`category-design.md`](category-design.md) (o frame de categoria), [`jtbd.md`](jtbd.md) (a necessidade na voz do cliente), [`ries-trout-positioning.md`](ries-trout-positioning.md) (a palavra a possuir), [`../power-of-one.md`](../power-of-one.md), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md).

## Fontes
> **Fonte:** Geoffrey A. Moore, *Crossing the Chasm* (3ª ed., 2014; orig. 1991), Harper Business, cap. 6 — via [`../../reference/books/positioning/moore-crossing-the-chasm.md`](../../reference/books/positioning/moore-crossing-the-chasm.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
