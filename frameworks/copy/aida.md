---
id: framework.copy.aida
title: "AIDA — Atenção, Interesse, Desejo, Ação"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [copy.pas, copy.pastor, copy.hook-frameworks, copy.close-frameworks, awareness-x-sophistication]
sources:
  - "Elias St. Elmo Lewis, modelo AIDA (c. 1898), formalizado na publicidade do século XX."
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
tags: [copy, aida, attention, interest, desire, action, structure]
---

# AIDA — Atenção, Interesse, Desejo, Ação

## TL;DR
AIDA é o esqueleto mais antigo e universal de persuasão escrita. Quatro estágios em ordem fixa: **Atenção** (pare o leitor), **Interesse** (faça ele querer ler mais), **Desejo** (faça ele querer o resultado), **Ação** (peça a compra). Cada estágio só existe para entregar o leitor ao próximo. Vence quando você precisa de uma estrutura simples e confiável para um anúncio, e-mail ou página curta com público de consciência média a alta. Não é o melhor esqueleto para público frio — aí a dor precisa de mais espaço (use [`pas`](pas.md) ou [`pastor`](pastor.md)).

## Quando usar / Quando não
**Use** em peças curtas e diretas: anúncios, e-mails de uma ideia, headlines+sub, páginas de captura. É a estrutura "porta de entrada" quando você quer movimento rápido sem cair em fórmula longa.
**Use mais** com consciência 3-5 (Solução/Produto/Mais consciente — ver [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md)): o leitor já sente a dor, então Atenção e Interesse podem ser curtos e o peso vai para Desejo e Ação.
**Não use** sozinho em público frio (Inconsciente/Consciente do problema): AIDA pula a agitação da dor que esse público precisa. Combine com PAS ou troque por PASTOR.
**Não use** quando a objeção dominante é confiança ou ceticismo extremo — aí o eixo é prova e história, não o arco AIDA puro.

## Inputs
- O **nível de consciência** dominante do avatar ([`awareness-levels`](../../lib/taxonomies/awareness-levels.md)).
- O **lead** travado pelo `positioning-lead-strategist` ([`lead-types`](../../lib/taxonomies/lead-types.md)).
- A **dor dominante** e o **resultado dos sonhos** em verbatim (banco de VOC do `avatar-voc-investigator`).
- A **oferta** e o **mecanismo único** já desenhados (sai do Offer Book).
- Ao menos uma **prova** por claim ([`../proof-to-claim-chain.md`](../proof-to-claim-chain.md) — forward-ref).

## Procedimento
1. **Atenção** — escreva uma abertura que interrompe. Use o lead travado: promessa específica, pergunta na dor, proclamação ousada ou estatística chocante. Teste: o leitor para de rolar? Sem isso, nada do resto acontece.
2. **Interesse** — entregue o "por que isto importa para você". Conecte a abertura ao mundo do avatar com um fato novo, uma tensão ou uma micro-história. O objetivo único é comprar a **próxima** frase (princípio do escorregador — ver [`slippery-slide`](slippery-slide.md)).
3. **Desejo** — construa a imagem do **resultado dos sonhos** e empilhe valor. Mostre o "depois", nomeie o mecanismo, traga prova (depoimento, dado, demonstração). Aqui você sobe as alavancas da [Value Equation](../value-equation.md): resultado, probabilidade percebida, e derruba tempo e esforço.
4. **Ação** — faça **um** pedido claro com motivo para agir agora: CTA único, reversão de risco (garantia) e escassez/urgência **verdadeira**. Diga exatamente o que clicar/fazer. Use os fechos de [`close-frameworks`](close-frameworks.md).
5. **Revise a costura** — leia em voz alta. Cada estágio precisa entregar o leitor "deslizando" ao próximo sem atrito. Corte qualquer frase que não empurre adiante.
6. **Cheque consciência** — confirme que o peso entre estágios casa com o nível: frio = mais Atenção/Interesse; quente = mais Desejo/Ação.

## Outputs
- Uma peça (ad, e-mail, página curta) estruturada nos 4 blocos rotulados A-I-D-A.
- Um **CTA único** com reversão de risco e gatilho de urgência real.
- Mapa de prova → claim por bloco de Desejo (para o `compliance-auditor`).
- Variações de Atenção (3-5 aberturas) para teste, alimentando o `control-registry`.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI (consciência 3).
- **Atenção**: "Você programa em inglês o dia todo — mas trava na entrevista falada. Não é o seu inglês. É a forma como você treina."
- **Interesse**: "Devs aprovados em vagas remotas não decoraram gramática. Eles usaram um método de imitação ativa chamado Shadowing Técnico."
- **Desejo**: "Em 60 dias, você responde 'tell me about a challenge' sem gelar. Como o Rafael, que saiu de R$8k para uma oferta de US$7k/mês." (depoimento = prova; mecanismo nomeado; tempo curto.)
- **Ação**: "Entre no 'Aprovado em Inglês' hoje. Vagas limitadas a 40 por turma para manter o roleplay 1:1. Não passou na entrevista em 60 dias? Seguimos juntos de graça. Clique em Garantir Minha Vaga."

## Armadilhas
- **Atenção vazia.** Headline criativa que não fala com a dor do avatar gera cliques sem conversão. Atenção serve ao Interesse, não ao ego do copy.
- **Pular o Interesse.** Saltar direto da headline para a oferta perde o leitor que ainda não comprou a premissa.
- **Desejo sem prova.** Empilhar benefícios sem lastro vira ruído cético — e veto de compliance. Cada claim precisa de prova.
- **CTA múltiplo ou tímido.** Dois pedidos dividem a decisão; "saiba mais" desperdiça intenção. Um pedido, claro e ousado.
- **Usar AIDA em público frio.** Sem agitação de dor, o frio não chega ao Desejo. Troque por PASTOR ou plugue PAS no início.

## Interações
- **Agentes**: `vsl-webinar-scriptwriter` (usa AIDA como macroestrutura de seções curtas), `email-sms-sequence-writer` (um e-mail = um arco AIDA), `ad-creative-factory` (anúncios de resposta direta), `big-idea-architect` (a Big Idea vira a Atenção), `avatar-voc-investigator` (fornece verbatim para Atenção/Desejo).
- **Frameworks que pareiam**: [`pas`](pas.md) e [`pastor`](pastor.md) (mais agitação de dor para público frio), [`hook-frameworks`](hook-frameworks.md) (variações de Atenção), [`fascination-bullets`](fascination-bullets.md) (constroem Desejo), [`close-frameworks`](close-frameworks.md) (a Ação), [`slippery-slide`](slippery-slide.md) (a costura entre estágios), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md) (calibra o peso por nível).

## Fontes
> **Fonte:** Modelo AIDA atribuído a Elias St. Elmo Lewis (c. 1898); fundamentos de consciência em Eugene M. Schwartz, *Breakthrough Advertising* (1966) — via [`../../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../../reference/books/copywriting/schwartz-breakthrough-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
