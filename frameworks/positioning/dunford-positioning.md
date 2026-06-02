---
id: framework.positioning.dunford-positioning
title: "Dunford Positioning — Os 5 Componentes do Posicionamento"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [moore-positioning-formula, ries-trout-positioning, category-design, jtbd, perceived-value-stack]
sources:
  - "April Dunford, *Obviously Awesome: How to Nail Product Positioning so Customers Get It, Buy It, Love It* (2019), Ambient Press, ISBN 978-1-9990230-0-3."
tags: [positioning, dunford, competitive-alternatives, unique-attributes, value, market-category, b2b]
---

# Dunford Positioning — Os 5 Componentes do Posicionamento

## TL;DR
Posicionamento é o **contexto** que faz o cliente entender, em segundos, o que você é e por que importa. Dunford o decompõe em **5 componentes encadeados**: alternativas competitivas → atributos únicos → valor (com prova) → mercado-alvo → categoria. A pergunta-chave não é "o que isto é?", mas "**comparado a quê?**". O melhor posicionamento escolhe a categoria certa e mostra como seus pontos fortes únicos entregam um valor que o cliente-alvo realmente quer. É como o `positioning-lead-strategist` torna a posição **concreta e auditável** — uma cadeia ligada, não um slogan.

## Quando usar / Quando não
**Use** sempre que precisa fixar a posição **antes da copy** — é o método-base do `lock-positioning-lead`.
**Use mais** quando o produto é difícil de explicar, cai em várias categorias possíveis, ou os clientes "não captam" o que ele é.
**Use mais** em B2B e em mercados de sofisticação 3-5, onde a categoria e a alternativa pesam mais que a promessa. Ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md).
**Não use** como frase de efeito isolada: os 5 componentes formam uma cadeia; pular um (ex.: valor sem prova) quebra tudo.
**Não use** sem a [`moore-positioning-formula.md`](moore-positioning-formula.md) para destilar o resultado em uma frase, nem sem [`category-design.md`](category-design.md) para a escolha da categoria.

## Inputs
- A lista real de **alternativas** do cliente (concorrentes, status quo, planilha, "não fazer nada").
- O **mecanismo único** nomeado ([`../unique-mechanism.md`](../unique-mechanism.md)) — fonte dos atributos únicos.
- A **prova** por atributo (depoimento, dado, demonstração) — de [`../proof-to-claim-chain.md`](../proof-to-claim-chain.md).
- O diagnóstico de mercado e o banco de VOC (quem se importa com qual valor).
- As categorias candidatas e as associações que cada uma dispara.

## Procedimento
1. **Liste as alternativas competitivas.** O que o cliente usaria se você não existisse? Inclua o status quo, a planilha e "não fazer nada". Isto define o **ponto de comparação** — todo o resto é relativo a ele.
2. **Isole os atributos únicos.** Liste as capacidades que **só você** tem em relação a essas alternativas. Puxe do mecanismo único. Atributo que o concorrente também tem não posiciona.
3. **Traduza atributos em valor — com prova.** Para cada atributo único, responda "e daí?": que benefício concreto ele entrega ao cliente? Anexe a prova. **Atributo sem valor é ruído; valor sem prova é claim vazio** (veto de compliance).
4. **Defina o mercado-alvo.** Quem se importa **muito** com esse valor, a ponto de comprar rápido? Estreite até o segmento que mais sente a dor. Não tente agradar todos — isso enfraquece a posição. Liga a [`../starving-crowd.md`](../starving-crowd.md).
5. **Escolha a categoria de mercado.** Qual frame faz o valor parecer **óbvio** e dispara as associações certas? A categoria é a alavanca mais forte e mais ignorada: a certa torna os atributos evidentes, a errada esconde o valor. Use [`category-design.md`](category-design.md).
6. **(+1) Identifique uma tendência relevante** (opcional). Uma onda atual que torna o produto oportuno. Use com cuidado — tendência demais soa oportunista.
7. **Monte a posição encadeada.** Escreva os 5 componentes como uma cadeia ligada. Cheque a coerência: o atributo único entrega o valor? O mercado-alvo quer esse valor? A categoria deixa isso óbvio?
8. **Destile em uma frase** com a [`moore-positioning-formula.md`](moore-positioning-formula.md) ("Para X que Y, nosso Z é W").
9. **Valide com vendas/clientes.** Teste se o time e os clientes "captam" rápido. Posicionamento é escolha de **equipe**, viva e revisável.
10. **Registre** a posição no `decision-registry` e passe o gate `positioning/positioning-awareness-fit`.

## Outputs
- **Quadro dos 5 componentes** preenchido (alternativas, atributos, valor+prova, mercado, categoria) + tendência opcional.
- A **posição em uma frase** (via Moore).
- A **categoria escolhida** e a justificativa.
- Insumo direto para a Big Idea, a copy e a página de vendas.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
1. **Alternativas**: apps de idioma genéricos, escola de inglês tradicional, "estudar sozinho no YouTube", não fazer nada.
2. **Atributos únicos**: método de *shadowing* focado em **entrevista técnica**; simulação 1:1 com recrutador real; banco de vocabulário de stack.
3. **Valor + prova**: "aprovado na entrevista em inglês e na vaga remota" — prova: 37 alunos contratados por empresas internacionais em 2025 (link no proof-registry).
4. **Mercado-alvo**: dev pleno/sênior brasileiro mirando vaga remota internacional — sente a dor de "travar na call em inglês".
5. **Categoria**: não "curso de inglês", mas "**preparação para entrevista técnica em inglês**" — frame que torna o método óbvio e tira do balaio dos apps.
- Frase (Moore): "Para o dev brasileiro que quer a vaga remota internacional, o [Nome] é a preparação de entrevista técnica em inglês que te aprova em 60 dias — diferente de apps de idioma, que ensinam inglês de turista."

## Armadilhas
- **Posicionar pelo produto, não pelo mercado.** Começar por "o que isto é" em vez de "comparado a quê" gera a posição que o fundador imaginou, não a que o cliente entende.
- **Atributo sem valor.** Listar features únicas sem o "e daí?". O cliente não compra atributo, compra benefício.
- **Valor sem prova.** Diferenciação sem lastro é veto de compliance. Toda promessa de valor traz evidência.
- **Mercado largo demais.** Tentar agradar todos dilui a posição. Mire o segmento que mais se importa.
- **Categoria por inércia.** Aceitar a categoria default (a mais genérica) esconde o valor. Escolher a categoria é a maior alavanca.
- **Posição congelada.** O mercado muda; a posição é viva. Revise por ciclo, com o time.

## Interações
- **Agentes**: `positioning-lead-strategist` (dono — preenche os 5 componentes e escolhe a categoria); `mechanism-architect` (fornece os atributos únicos); `proof-credibility-curator` (abastece o valor com prova); `market-sophistication-analyst` e `avatar-voc-investigator` (definem o mercado-alvo com evidência); `pricing-wtp-strategist` (a alternativa competitiva vira a referência de preço por valor); `unit-economics-stack-analyst` (confere que o segmento-alvo escolhido fecha em margem e payback); `big-idea-architect` (destila a posição em UMA tese); `compliance-auditor` (veta atributo ou valor sem lastro).
- **Frameworks que pareiam**: [`moore-positioning-formula.md`](moore-positioning-formula.md) (destila em uma frase), [`category-design.md`](category-design.md) (componente 5), [`jtbd.md`](jtbd.md) (o "job" do cliente afina o mercado e o valor), [`ries-trout-positioning.md`](ries-trout-positioning.md) (a palavra a possuir na mente), [`perceived-value-stack.md`](perceived-value-stack.md), [`../unique-mechanism.md`](../unique-mechanism.md), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md).

## Fontes
> **Fonte:** April Dunford, *Obviously Awesome* (2019), Ambient Press, cap. 4-6 — via [`../../reference/books/positioning/dunford-obviously-awesome.md`](../../reference/books/positioning/dunford-obviously-awesome.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
