---
id: framework.lead-types
title: "Lead Types — Como Escolher e Aplicar os 6 Leads"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [awareness-x-sophistication, big-idea-generator, power-of-one, unique-mechanism, proof-to-claim-chain]
sources:
  - "Michael Masterson & John Forde, *Great Leads* (2011)."
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
tags: [lead, copy-opening, awareness, hook, selection]
---

# Lead Types — Escolhendo e Aplicando os 6 Leads

## TL;DR
O **lead** são as primeiras frases — os primeiros 10-20% de uma VSL, carta ou ad — onde o leitor decide ficar ou sair. Existem seis: **Oferta, Promessa, Problema-Solução, Segredo, Proclamação, História**. O lead certo é função do **nível de consciência**: direto para quem já sabe, indireto para quem ainda não. Esta é a parte **operacional** que escolhe e aplica o lead; a taxonomia [`../lib/taxonomies/lead-types.md`](../lib/taxonomies/lead-types.md) é o vocabulário. O `positioning-lead-strategist` trava o lead via a [matriz 5×5](awareness-x-sophistication.md).

## Quando usar / Quando não
**Use** ao abrir qualquer peça de copy (VSL, webinar, ad, e-mail, carta).
**Use** para diagnosticar uma copy que "não engata": quase sempre o lead não casa com a consciência.
**Não use** um lead direto (Oferta) em público frio — queima o tráfego. Frio pede História/Proclamação.
**Não use** o mesmo lead para todos os segmentos de um lançamento — cada célula de consciência pede o seu.

## Inputs
- O **nível de consciência** dominante do segmento — ver [`../lib/taxonomies/awareness-levels.md`](../lib/taxonomies/awareness-levels.md).
- O **nível de sofisticação** (define quanto mecanismo o lead carrega) — ver [`../lib/taxonomies/sophistication-levels.md`](../lib/taxonomies/sophistication-levels.md).
- A **Big Idea** travada ([`big-idea-generator.md`](big-idea-generator.md)) e o [Power of One](power-of-one.md).
- O **mecanismo** nomeado (para leads de Segredo) e a **prova** disponível.
- Verbatims do avatar (para espelhar dor em leads de Problema-Solução e História).

## Procedimento
1. **Leia a célula de consciência × sofisticação** do segmento (da [matriz](awareness-x-sophistication.md)). Ela é o ponto de partida.
2. **Mapeie consciência → diretividade**: 5/4 (quente) → leads diretos (Oferta, Promessa); 3/2 (morno) → semi-diretos (Problema-Solução, Segredo); 2/1 (frio) → indiretos (Proclamação, História).
3. **Ajuste pela sofisticação**: em mercado maduro (3-4), o lead **carrega o mecanismo** (Segredo) em vez de claim seco; em estágio 5, o lead apela à identidade (História).
4. **Escolha o lead** na coluna "lead recomendado" da taxonomia e confirme que casa com a Big Idea única.
5. **Escreva 2-3 aberturas** no lead escolhido. Para cada uma, garanta a **prova logo atrás** (proclamação e segredo morrem sem lastro — ver [`proof-to-claim-chain.md`](proof-to-claim-chain.md)).
6. **Teste o "fica ou sai"**: a primeira frase prende o avatar certo? Leia em voz alta (voz 3ª série). Se não prende em 10 segundos, reescreva.
7. **Garanta o foco único**: o lead carrega **uma** ideia e leva a **um** CTA ([Power of One](power-of-one.md)).
8. **Trave o lead** por segmento e **registre** no `decision-registry`; rode o gate `positioning/positioning-awareness-fit` (reprova lead que não casa com a consciência).

## Outputs
- **Lead travado por segmento** (tipo + 2-3 aberturas candidatas).
- Justificativa de fit (célula de consciência × sofisticação → tipo escolhido).
- Nota de prova exigida por abertura (o que precisa vir logo atrás).
- Veredito do gate de fit de consciência.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Segmento frio (ad)**: consciência 2 × sofisticação 4. Direto seria invisível. **Lead de Segredo** carregando o mecanismo: *"Existe um motivo por que você trava na entrevista em inglês — e não é seu vocabulário."* Prova atrás: depoimento + nome do mecanismo.
- **Segmento morno (lista de e-mail nutrida)**: consciência 3. **Lead de Problema-Solução**: espelha a dor ("você estuda, mas na entrevista a mente apaga"), agita, abre a solução.
- **Segmento quente (compradores da Atração)**: consciência 5. **Lead de Oferta**: *"Turma aberta: 40 vagas, 8 simulações 1:1, aprovado em 60 dias ou seguimos juntos."*
- **Resultado**: três aberturas, um único foco e CTA em cada. Usar o lead de Oferta no frio teria queimado o anúncio.

## Armadilhas
- **Lead direto em público frio.** Oferta/Promessa para quem não conhece o problema = tráfego queimado.
- **Claim seco em mercado maduro.** Sofisticação 4 exige o lead que carrega o mecanismo (Segredo), não promessa pura.
- **Proclamação/Segredo sem prova.** Audácia sem lastro vira clickbait e perde a leitura na segunda frase.
- **Um lead para todos os segmentos.** Cada célula de consciência tem o seu — segmente.
- **Lead que abre uma segunda ideia.** Quebra o Power of One e dispersa a conversão.

## Interações
- **Agentes**: `positioning-lead-strategist` (dono — trava o lead); `market-sophistication-analyst` (fornece a célula); `big-idea-architect` (a Big Idea define o ângulo do lead); `vsl-webinar-scriptwriter`, `ad-creative-factory`, `email-sms-sequence-writer` (aplicam o lead na abertura de cada peça); `proof-credibility-curator` (garante a prova atrás do lead).
- **Frameworks que pareiam**: [`awareness-x-sophistication.md`](awareness-x-sophistication.md), [`big-idea-generator.md`](big-idea-generator.md), [`power-of-one.md`](power-of-one.md), [`unique-mechanism.md`](unique-mechanism.md), [`proof-to-claim-chain.md`](proof-to-claim-chain.md).

## Fontes
> **Fonte:** Michael Masterson & John Forde, *Great Leads* (2011); fundamentos em Eugene M. Schwartz, *Breakthrough Advertising* (1966) — via [`../lib/taxonomies/lead-types.md`](../lib/taxonomies/lead-types.md) e [`../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../reference/books/copywriting/schwartz-breakthrough-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
