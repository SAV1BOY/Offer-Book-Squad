---
id: framework.reference-intellectual.ogilvy-on-advertising
title: "Ogilvy — Big Idea, Pesquisa e Headline"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [big-idea-generator, power-of-one, proof-to-claim-chain, hook-frameworks]
sources:
  - "David Ogilvy, *Ogilvy on Advertising* (Crown/Vintage, 1983), ISBN 978-0-394-72903-7."
tags: [ogilvy, big-idea, brand-image, headlines, research, advertising]
---

# Ogilvy — Big Idea, Pesquisa e Headline

## TL;DR
Ogilvy une o rigor mensurável da resposta direta com a construção de **marca**. A tese central: campanhas que vendem nascem de uma **Big Idea** — um conceito grande, simples e diferente o bastante para furar a indiferença e durar anos. Sem ela, a propaganda "passa como um navio na noite". Mas a Big Idea não vem de inspiração; vem de **pesquisa**. E o **título** é a peça mais lida (Ogilvy afirma que cinco vezes mais gente lê o título do que o corpo). Este framework é a ponte do squad entre `one_big_idea` e prova: pesquise muito, destile UMA ideia grande, escreva títulos de benefício, proteja a marca. Vence quando a peça precisa converter **e** construir ativo de marca.

## Quando usar / Quando não
**Use** ao destilar a Big Idea de um lançamento e ao escrever a headline de qualquer peça-âncora.
**Use** para forçar a pesquisa antes da criação: produto, cliente e os controles que já venderam.
**Use** para proteger a imagem de marca de longo prazo contra truques de conversão de curto prazo.
**Não use** para montar a oferta ou a sequência — isso é Hormozi; Ogilvy entrega a **ideia** e o **título**, não o stack.
**Não use** para fabricar uma ideia "criativa" descolada do fato — a Big Idea deriva de pesquisa, não de palpite.
**Fit:** universal; em mercado maduro, a Big Idea decide se aposta no mecanismo ou na identidade — pareie com Schwartz.

## Inputs
- A pesquisa de produto: o que ele faz, prova-real, diferencial verificável.
- A pesquisa de cliente: VOC, desejo e linguagem do avatar ("o consumidor não é idiota").
- Os **controles** que já venderam na categoria (swipe, breakdowns).
- A leitura de consciência/sofisticação — ver [`schwartz-breakthrough-advertising.md`](schwartz-breakthrough-advertising.md).
- O `proof-registry` para lastrear o benefício do título.

## Procedimento
1. **Pesquise antes de criar.** Mergulhe no produto, no cliente e nos controles vencedores. A Big Idea e a copy **derivam de fatos**, não de inspiração solta.
2. **Destile UMA Big Idea.** Busque o conceito **grande, simples, distinto e durável** que carrega a campanha. Teste: é grande o bastante para furar a indiferença? Dura anos? É diferente?
3. **Reprove a multiplicidade.** Se há duas ou três ideias, ainda não há uma Big Idea. Force a escolha de **uma** (`one_big_idea`, Power of One).
4. **Escreva a headline de benefício.** O título é o mais lido; entregue um **benefício específico e crível** e, quando possível, a marca dentro dele.
5. **Lastreie o benefício.** Cada promessa do título aponta para prova rastreável no `proof-registry` — Ogilvy respeita o consumidor com fatos, não esperteza.
6. **Proteja a imagem de marca.** Confira que a peça constrói a **personalidade de longo prazo** da marca, e não a queima por um truque de conversão imediata.
7. **Meça.** Trate a resposta direta como a melhor escola: meça o que a peça gera, porque o número ensina o que de fato vende.
8. **Registre a Big Idea** no `big-idea-registry` e a headline vencedora no `control-registry`.

## Outputs
- A **Big Idea** única (grande, simples, distinta, durável), com a pesquisa que a sustenta.
- A **headline de benefício** com a prova que a lastreia.
- O **dossiê de pesquisa** (produto + cliente + controles) que originou a ideia.
- A **nota de marca**: como a peça protege a personalidade de longo prazo.

## Exemplo
Oferta de amostra: seguro de vida para pais jovens.
- **Pesquisa**: VOC mostra o medo dominante — "se eu faltar, quem cuida das crianças?"; controles da categoria vendem com "tranquilidade".
- **Big Idea**: "Um pai presente, mesmo quando não estiver." Grande, simples, distinta, durável — vai além do produto e fura o clichê de "proteção".
- **Reprova da multiplicidade**: descartadas "economize no seguro" e "cobertura completa" — diluíam o foco. Fica **uma**.
- **Headline**: "O bilhete que garante que seus filhos nunca ouçam ‘não dá'." Benefício específico e crível.
- **Lastro**: a promessa de continuidade financeira aponta para o valor de cobertura e os depoimentos reais de beneficiários.
- **Marca**: o tom protege uma imagem de cuidado sério, não de venda agressiva.
- **Resultado**: o `big-idea-architect` aprova UMA ideia durável; a headline entrega benefício com prova.

## Armadilhas
- **Nenhuma Big Idea.** Sem o conceito grande, a peça passa despercebida — "navio na noite".
- **Múltiplas ideias.** Duas ou três tese é zero tese; o `big-idea-architect` reprova.
- **Ideia sem pesquisa.** "Criatividade" descolada do fato não vende e não dura.
- **Headline vaga.** Título sem benefício específico não para ninguém (eco de Caples).
- **Queimar a marca por um truque.** Conversão de hoje que destrói a personalidade de amanhã é prejuízo disfarçado.
- **Benefício sem lastro.** Promessa no título sem prova é claim infundado — risco de veto.

## Interações
- **Agentes** (de `config.yaml`): `big-idea-architect` (destila UMA Big Idea durável; múltiplas = reprovação, `one_big_idea`); `positioning-lead-strategist` (cuida da imagem de marca e do enquadramento de categoria); `ad-creative-factory` e `vsl-webinar-scriptwriter` (escrevem títulos de benefício e protegem consistência de marca); `avatar-voc-investigator` e `proof-credibility-curator` (fornecem a pesquisa de onde a Big Idea e os claims derivam); `voice-style-guardian` (mantém a personalidade de marca).
- **Frameworks que pareiam**: [`../big-idea-generator.md`](../big-idea-generator.md) e [`../power-of-one.md`](../power-of-one.md) (a destilação de UMA ideia), [`../proof-to-claim-chain.md`](../proof-to-claim-chain.md) (lastro do benefício), [`../copy/hook-frameworks.md`](../copy/hook-frameworks.md) (geração de manchetes); e as referências [`caples-tested-advertising.md`](caples-tested-advertising.md) (o culto ao título e ao teste) e [`schwartz-breakthrough-advertising.md`](schwartz-breakthrough-advertising.md) (mecanismo vs. identidade por estágio).

## Fontes
> **Fonte:** David Ogilvy, *Ogilvy on Advertising* (Crown/Vintage, 1983), ISBN 978-0-394-72903-7 — via [`../../reference/books/copywriting/ogilvy-on-advertising.md`](../../reference/books/copywriting/ogilvy-on-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
