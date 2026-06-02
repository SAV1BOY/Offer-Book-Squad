---
id: framework.power-of-one
title: "Power of One — UMA Big Idea, UM Avatar, UMA Promessa, UM CTA"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [big-idea-generator, awareness-x-sophistication, lead-types, value-equation, grand-slam-offer]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966) — 'one desire' por anúncio."
  - "Russell Brunson, *Expert Secrets* (2017) — 'The One Thing'."
tags: [focus, one-big-idea, single-cta, clarity, conversion]
---

# Power of One — A Força do Um

## TL;DR
Toda peça vence quando carrega **uma** coisa: **uma Big Idea, um avatar, uma promessa, um CTA**. A mente do prospect não compra confusão. Cada "e também" que você adiciona divide a atenção e derruba a conversão. É o princípio `one_big_idea` do squad: múltiplas ideias = reprovação. O `big-idea-architect` força o foco; o `voice-style-guardian` e os redatores cortam tudo que pluraliza a mensagem. Clareza vence volume (`clarity_before_volume`).

## Quando usar / Quando não
**Use** em toda peça de copy, página, e-mail, ad e na própria oferta — o teste do "Um" é universal.
**Use** como filtro de poda: quando a oferta ou a copy parece "rica demais", aplique o Power of One e corte.
**Não use** como desculpa para empobrecer a oferta: **um** núcleo pode ter vários componentes — o "um" é a **ideia/promessa/CTA**, não a contagem de entregáveis.
**Não use** o mesmo "um" para públicos em células de consciência diferentes — segmente e dê a cada segmento o **seu** único foco.

## Inputs
- A lista de Big Ideas candidatas (do `big-idea-architect`).
- O avatar dominante e a dor dominante (banco de VOC).
- A promessa central (Resultado dos Sonhos da [Value Equation](value-equation.md)).
- A célula de [consciência × sofisticação](awareness-x-sophistication.md) do público.
- O objetivo de conversão da peça (o que a ação deve ser).

## Procedimento
1. **Escolha UMA Big Idea**: das candidatas, selecione a mais forte (ver [`big-idea-generator.md`](big-idea-generator.md)). As outras viram material de outra peça ou são arquivadas — não entram juntas.
2. **Fixe UM avatar**: a pessoa exata para quem a peça fala. Se há dois públicos, há duas peças.
3. **Declare UMA promessa**: o resultado central, em uma frase, na voz do avatar. Uma promessa dominante; benefícios secundários **apoiam**, não competem.
4. **Defina UM CTA**: uma única ação pedida (comprar, agendar, assinar). Remova links e pedidos concorrentes.
5. **Faça a varredura do "e também"**: leia a peça caçando cada segunda ideia, segundo avatar, segunda promessa ou segundo CTA. Cada um é candidato a corte.
6. **Teste do título único**: a manchete consegue carregar a Big Idea sozinha? Se precisa de duas manchetes, há duas ideias — escolha uma.
7. **Verifique o fio condutor**: cada seção da peça deve reforçar o mesmo "um". O que não reforça, sai ou vira nota de rodapé.
8. **Registre** a Big Idea única escolhida e os descartes no `big-idea-registry`; rode `big-idea/big-idea-single-gate`.

## Outputs
- A **declaração do Um**: a Big Idea, o avatar, a promessa e o CTA, cada um em uma linha.
- Lista de ideias/CTAs **descartados** (com onde reaproveitar).
- Peça podada: cada seção mapeada ao único foco.
- Veredito do gate de Big Idea única (passa só com um).

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI. Rascunho inicial (errado) prometia: "fale inglês fluente, **e também** passe em entrevistas, **e também** viaje sem medo, **e também** ganhe em dólar" — quatro promessas, três avatares, dois CTAs ("compre" e "baixe o e-book").
- **UMA Big Idea**: "o método que prepara o dev para a **entrevista** em inglês — não para a fluência genérica".
- **UM avatar**: o dev que quer a vaga remota internacional.
- **UMA promessa**: "aprovado na entrevista técnica em inglês em 60 dias".
- **UM CTA**: "entre na turma".
- **Cortes**: "viaje sem medo" e "ganhe em dólar" viram benefícios de apoio, não promessas; o CTA "baixe o e-book" sai da página de vendas (é da Atração). A peça fica afiada e converte mais.

## Armadilhas
- **Empilhar Big Ideas "porque todas são boas".** Duas ideias = nenhuma. Escolha uma; arquive o resto.
- **Dois CTAs na mesma peça.** Dividem a decisão. Um pedido por peça.
- **Confundir foco com pobreza.** Um núcleo pode ter muitos componentes; o "um" é a mensagem, não a entrega.
- **Mesma peça para públicos diferentes.** Cada célula de consciência pede o seu próprio foco — segmente.
- **Benefícios secundários que viram promessas paralelas.** Eles apoiam a promessa central; não competem com ela.

## Interações
- **Agentes**: `big-idea-architect` (dono — entrega UMA tese; múltiplas = reprovação); `positioning-lead-strategist` (alinha o lead ao único foco); `vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `ad-creative-factory` (aplicam um CTA por peça); `voice-style-guardian` (corta o "e também").
- **Frameworks que pareiam**: [`big-idea-generator.md`](big-idea-generator.md), [`awareness-x-sophistication.md`](awareness-x-sophistication.md), [`lead-types.md`](lead-types.md), [`value-equation.md`](value-equation.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md).

## Fontes
> **Fonte:** Eugene M. Schwartz, *Breakthrough Advertising* (1966), "um desejo por anúncio"; reforço em Russell Brunson, *Expert Secrets* (2017) — via [`../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../reference/books/copywriting/schwartz-breakthrough-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
