---
id: framework.copy.hook-frameworks
title: "Hook Frameworks — Ganchos de Abertura por Ângulo"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
frameworks: [copy.aida, copy.vsl-structure, copy.fascination-bullets, lead-types, awareness-x-sophistication]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
  - "Michael Masterson & John Forde, *Great Leads* (2011)."
  - "John Caples, *Tested Advertising Methods* (5ª ed.)."
tags: [copy, hook, opening, angle, ad, scroll-stop]
---

# Hook Frameworks — Ganchos de Abertura por Ângulo

## TL;DR
O gancho são os primeiros 1-3 segundos (ou a primeira linha) que decidem se o público para ou rola. Um repertório de **padrões de gancho** — pergunta na dor, proclamação ousada, segredo, contraste, estatística chocante, história, demonstração, mito derrubado — dá ao criativo várias portas de entrada para o mesmo público. O gancho **deve casar com o lead e a consciência** (ver [`../../lib/taxonomies/lead-types.md`](../../lib/taxonomies/lead-types.md)). Vence em anúncios, aberturas de VSL e linhas de assunto de e-mail. É a matéria-prima da matriz de criativos do `ad-creative-factory`.

## Quando usar / Quando não
**Use** para gerar **variações de abertura** para teste: anúncios, thumbnails, primeiras linhas de VSL, assuntos de e-mail.
**Use** quando você precisa cobrir vários ângulos do mesmo público (matriz de criativos) — cada gancho testa uma porta.
**Use** o tipo de gancho **calibrado pela consciência**: frio pede gancho indireto (história, segredo, proclamação); quente tolera gancho direto (oferta, promessa). Ver [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md).
**Não use** gancho de curiosidade pura sem conexão com a oferta — atrai cliques que não convertem (tráfego caro e frio).
**Não use** o mesmo gancho para todos os segmentos: o gancho que para o frio entedia o quente.

## Inputs
- O **lead** travado pelo `positioning-lead-strategist` ([`lead-types`](../../lib/taxonomies/lead-types.md)) e a **célula** de consciência × sofisticação ([`../awareness-x-sophistication.md`](../awareness-x-sophistication.md)).
- A **dor**, o **resultado dos sonhos** e os **verbatims** do `avatar-voc-investigator`.
- A **Big Idea** travada ([`../big-idea-architect/promise-hook-villain.md`](../big-idea-architect/promise-hook-villain.md)) — fonte do gancho-mãe.
- O **mecanismo único** nomeado e a **prova** mais forte disponível.
- O **mapa de objeção-crença** ([`../avatar-voc-investigator/objection-belief-mapping.md`](../avatar-voc-investigator/objection-belief-mapping.md)) para ganchos que atacam a crença bloqueadora.

## Procedimento
1. **Escolha o eixo da consciência**: frio → ganchos indiretos; quente → ganchos diretos. Esse filtro elimina padrões que queimariam o tráfego.
2. **Gere ganchos por padrão** (use vários por campanha):
   - **Pergunta na dor** — "Por que você trava na hora de falar inglês mesmo entendendo tudo?"
   - **Proclamação ousada** — "Demita seu personal. Você nunca precisou dele."
   - **Segredo/Curiosidade** — "Existe um motivo pelo qual seu bebê acorda às 3h. E não é fome."
   - **Contraste/Inimigo comum** — "Não é falta de disciplina. É a dieta que te ensinaram errado." (ver vilão em [`promise-hook-villain`](../big-idea-architect/promise-hook-villain.md)).
   - **Estatística chocante** — "87% dos autônomos não fazem ideia de quanto realmente lucram."
   - **História/Identificação** — "Eu emiti minha primeira nota fiscal chorando no banheiro do trabalho."
   - **Demonstração/Mostrar** — abrir mostrando o resultado em ação (print, antes-depois, tela).
   - **Mito derrubado** — "Tudo que você ouviu sobre poupar dinheiro está errado."
   - **Se/Então específico** — "Se você acorda cansado mesmo dormindo 8h, isto é para você."
3. **Ancore no específico**: número, prazo, nome, lugar. Específico para o scroll; vago é ignorado.
4. **Cheque o casamento gancho ↔ corpo**: o gancho promete e o corpo entrega. Gancho desconectado da oferta = clique caro sem conversão.
5. **Verifique o lastro**: gancho que faz claim mensurável precisa de prova. Estatística precisa de fonte. (Veto de compliance se inventado.)
6. **Gere 5-10 variações por ângulo** e marque qual padrão e qual objeção cada uma ataca, para o teste e o `control-registry`.

## Outputs
- Um **banco de ganchos** (5-10 por ângulo) marcado por padrão, lead e objeção atacada.
- Os ganchos prontos para a **matriz de criativos** do `ad-creative-factory` (gate `ads/ads-angle-coverage-gate`).
- A primeira linha da VSL e os assuntos de e-mail derivados do mesmo banco.
- Mapa **gancho → claim → prova** para o `compliance-auditor`.

## Exemplo
Oferta de amostra: app de finanças para autônomos (consciência 2, célula 2×4). Ganchos por padrão:
- **Pergunta na dor**: "Você fatura R$10 mil por mês e ainda assim a conta não fecha. Por quê?"
- **Estatística chocante**: "9 em cada 10 autônomos misturam o dinheiro da empresa com o pessoal — e nem percebem."
- **Inimigo comum**: "O problema não é você gastar demais. É não ter um sistema que separa o dinheiro antes."
- **História**: "Eu já cheguei a pedir dinheiro emprestado no mês em que mais faturei na vida."
- **Demonstração**: vídeo abrindo o app e mostrando 3 contas se separarem em 1 toque.
- Cada gancho leva ao mesmo corpo (mecanismo "3 contas") e é marcado para teste A/B.

## Armadilhas
- **Gancho direto em público frio.** Abrir com oferta/preço para quem não sente a dor queima o tráfego. Frio pede gancho indireto.
- **Curiosidade desconectada.** Gancho intrigante que não liga à oferta gera clique caro e bounce. O corpo precisa pagar a promessa do gancho.
- **Claim sem prova.** Estatística ou resultado no gancho sem fonte/lastro é veto de compliance.
- **Vago.** "Transforme sua vida" não para ninguém. Específico (número, prazo, nome) é o que interrompe o scroll.
- **Um gancho só.** Sem variação de ângulo, você não descobre a porta que converte. Gere muitos, teste, mantenha os vencedores.
- **Gancho que não casa com a Big Idea.** Ganchos dispersos diluem a tese. Todos devem orbitar a UMA Big Idea.

## Interações
- **Agentes**: `ad-creative-factory` (dono — gera a matriz de ganchos), `vsl-webinar-scriptwriter` (o gancho abre a VSL), `email-sms-sequence-writer` (ganchos viram assuntos), `big-idea-architect` (a Big Idea é o gancho-mãe), `avatar-voc-investigator` (fornece dor e verbatim), `positioning-lead-strategist` (trava o lead que limita os padrões).
- **Frameworks que pareiam**: [`lead-types`](../../lib/taxonomies/lead-types.md) (cada lead = uma família de ganchos), [`aida`](aida.md) (gancho = Atenção), [`vsl-structure`](vsl-structure.md) (gancho = beat 1), [`fascination-bullets`](fascination-bullets.md) (um bullet forte vira gancho), [`promise-hook-villain`](../big-idea-architect/promise-hook-villain.md) (o gancho da Big Idea), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md).

## Fontes
> **Fonte:** Padrões de gancho derivados da teoria de leads de Michael Masterson & John Forde, *Great Leads* (2011), dos estados de consciência de Eugene M. Schwartz (1966) e dos testes de manchete de John Caples, *Tested Advertising Methods* — via [`../../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../../reference/books/copywriting/schwartz-breakthrough-advertising.md) e [`../../reference/books/copywriting/caples-tested-advertising.md`](../../reference/books/copywriting/caples-tested-advertising.md), acesso 2026-06-02. Tipos de lead em [`../../lib/taxonomies/lead-types.md`](../../lib/taxonomies/lead-types.md).
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
