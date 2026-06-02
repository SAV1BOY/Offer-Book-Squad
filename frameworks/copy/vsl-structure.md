---
id: framework.copy.vsl-structure
title: "Estrutura de VSL — Os Beats da Carta de Vendas em Vídeo"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [copy.pastor, copy.pas, copy.slippery-slide, copy.fascination-bullets, copy.close-frameworks, copy.hook-frameworks, awareness-x-sophistication]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
  - "Joseph Sugarman, *The Adweek Copywriting Handbook* (2007)."
  - "Dan S. Kennedy, *The Ultimate Sales Letter* (4ª ed., 2011)."
tags: [copy, vsl, video-sales-letter, structure, beats, long-form]
---

# Estrutura de VSL — Os Beats da Carta de Vendas em Vídeo

## TL;DR
A VSL é uma carta de vendas longa transformada em roteiro falado. Funciona por **beats** em sequência: Gancho → Identificação da dor → Promessa → Origem/História → Mecanismo único → Prova → Oferta (value stack) → Preço ancorado → Garantia → Escassez verdadeira → CTA → Fecho de objeções. Cada beat existe para entregar o espectador ao próximo (princípio do escorregador de [`slippery-slide`](slippery-slide.md)). Vence quando você precisa converter tráfego frio a quente num único vídeo de venda. É o esqueleto-mestre do `vsl-webinar-scriptwriter`; mapeia [`pastor`](pastor.md) em beats acionáveis.

## Quando usar / Quando não
**Use** sempre que o entregável for um vídeo de venda (VSL de página, VSL de anúncio longo, webinar gravado, recap).
**Use** quando o público é frio a morno e a oferta exige explicação (mecanismo, prova, preço alto).
**Use** o esqueleto completo para consciência 1-3; **comprima** os beats iniciais (Gancho, Dor) para consciência 4-5, que já quer comprar (ver [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md)).
**Não use** a VSL longa para público quente de remarketing pronto para comprar — uma página de oferta direta converte melhor e mais barato.
**Não use** os beats fora de ordem sem motivo: preço antes de valor, ou prova antes da promessa, quebra a lógica de persuasão.

## Inputs
- O **Offer Book completo**: mecanismo único, oferta (value stack), preço, garantia, escassez verdadeira. **HARD STOP**: a VSL não nasce antes do Offer Book passar no DoD ([`../../ARCHITECTURE.md`](../../ARCHITECTURE.md) §1).
- A **Big Idea** travada ([`../big-idea-architect/promise-hook-villain.md`](../big-idea-architect/promise-hook-villain.md)) — vira o Gancho e o fio condutor.
- A **dor** e o **resultado dos sonhos** em verbatim do `avatar-voc-investigator`.
- O **arsenal de prova** do `proof-credibility-curator` e o **mapa de objeção-crença** ([`../avatar-voc-investigator/objection-belief-mapping.md`](../avatar-voc-investigator/objection-belief-mapping.md)).
- O **nível de consciência × sofisticação** ([`../awareness-x-sophistication.md`](../awareness-x-sophistication.md)) e o **lead** travado ([`../../lib/taxonomies/lead-types.md`](../../lib/taxonomies/lead-types.md)).

## Procedimento
1. **Gancho (0-30s)** — pare o espectador. Use a Big Idea ou o lead travado: promessa específica, proclamação ousada, pergunta na dor ou segredo. Sem o gancho, ninguém vê o resto. Variações em [`hook-frameworks`](hook-frameworks.md).
2. **Identificação da dor** — espelhe a dor dominante em verbatim. O espectador pensa "é comigo". (Beat de [`pas`](pas.md).)
3. **Promessa** — declare o resultado dos sonhos e prometa que há uma saída específica. Grande e crível.
4. **Origem/História** — conte a virada (do fundador ou de um cliente). Baixa a guarda e prepara a revelação do mecanismo.
5. **Mecanismo único** — revele e **nomeie** a causa do resultado. É o coração da VSL: o "por que isto funciona quando o resto falhou". Sem mecanismo nomeado, vira mais uma promessa.
6. **Prova** — empilhe depoimentos (nome + número), dados, demonstrações. Cada prova mata uma objeção do mapa.
7. **Transição para a oferta** — "se isso funcionou para eles, veja o que preparei para você".
8. **Oferta / Value Stack** — apresente cada componente com seu valor. Empilhe até o valor percebido superar muito o preço. Use [`fascination-bullets`](fascination-bullets.md). Suba as alavancas da [Value Equation](../value-equation.md).
9. **Ancoragem de preço** — mostre o valor total somado, depois o preço real (muito menor). Preço **sempre** depois do valor.
10. **Garantia / Reversão de risco** — assuma o risco pelo cliente (devolução, garantia condicional). Derruba a objeção "e se não funcionar".
11. **Escassez / Urgência verdadeira** — motivo real para agir agora (vagas reais, prazo real, bônus que expira de verdade). Falsa = veto de compliance.
12. **CTA** — um pedido claro, com instrução exata do que fazer. Único.
13. **Fecho de objeções** — recapitule, responda as 3-5 objeções finais do mapa, repita o CTA. Use [`close-frameworks`](close-frameworks.md).
14. **Costure o escorregador** — leia o roteiro em voz alta cronometrado. Corte qualquer beat que faça o espectador parar.

## Outputs
- Um **roteiro de VSL** com beats rotulados e marcações de tempo.
- Mapa **prova → claim** e **prova → objeção** por beat (para o `compliance-auditor`).
- A oferta apresentada com valor **antes** do preço (gate `vsl/vsl-value-before-price-gate`).
- CTA único com reversão de risco (gates `vsl/vsl-risk-reversal-gate`, `vsl/vsl-cta-strength-gate`).
- Variações de Gancho para teste, alimentando o `control-registry`.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI (consciência 2-3). Beats resumidos:
- **Gancho**: "Você programa em inglês o dia todo, mas trava na entrevista falada. O problema não é o seu inglês."
- **Dor**: "Você entende tudo, lê documentação, mas na hora de falar a mente trava e a vaga remota de dólar escapa."
- **Promessa**: "Em 60 dias você responde qualquer pergunta de entrevista em inglês sem gelar."
- **História + Mecanismo**: "Eu também travava — até descobrir que fluência de fala não vem de gramática, vem de **Shadowing Técnico**: imitar em voz alta falas reais de devs, na sua área."
- **Prova**: "O Rafael saiu de R$8k para uma oferta de US$7k/mês em 4 meses. A Paula passou na entrevista da Shopify no segundo round."
- **Value Stack**: "Você leva o método Shadowing Técnico, 120 falas de entrevista por stack, roleplay 1:1 e correção de pronúncia. Valor total R$2.400."
- **Preço + Garantia**: "Hoje, R$597. E se não passar numa entrevista em 60 dias, seguimos juntos de graça até passar."
- **Escassez + CTA**: "São 40 vagas por turma para manter o roleplay 1:1. Clique em Garantir Minha Vaga."

## Armadilhas
- **Gancho fraco.** Os primeiros 30 segundos decidem a retenção. Gancho genérico mata a VSL inteira no início.
- **Mecanismo ausente ou vago.** A VSL sem mecanismo nomeado é só promessa empilhada. O beat 5 é o coração — não pule.
- **Preço antes de valor.** Inverter os beats 8-9 derruba a conversão. Valor primeiro, sempre. (Gate dedicado.)
- **Prova genérica.** Depoimento vago não mata objeção. Use nome, número e a crença que cada caso derruba.
- **Escassez falsa.** "Só hoje" que se repete toda semana queima a confiança e dá veto de compliance. Escassez real ou nada.
- **VSL longa para público quente.** Quem já quer comprar abandona a jornada longa. Comprima ou use página direta.
- **Beats sem costura.** Saltos abruptos entre beats fazem o espectador parar. O escorregador precisa ser liso.

## Interações
- **Agentes**: `vsl-webinar-scriptwriter` (dono — monta a VSL beat a beat), `voice-style-guardian` (fiscaliza voz e atrito), `proof-credibility-curator` (fornece prova por beat), `big-idea-architect` (a Big Idea vira o Gancho), `avatar-voc-investigator` (dor e resultado em verbatim), `compliance-auditor` (valida claim e escassez).
- **Frameworks que pareiam**: [`pastor`](pastor.md) (mapeia 1:1 nos beats), [`pas`](pas.md) (beats 1-2), [`slippery-slide`](slippery-slide.md) (a costura), [`hook-frameworks`](hook-frameworks.md) (o Gancho), [`fascination-bullets`](fascination-bullets.md) (o value stack), [`close-frameworks`](close-frameworks.md) (CTA e fecho de objeções), [`launch/perfect-webinar.md`](../launch/perfect-webinar.md) (versão webinar ao vivo), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md).

## Fontes
> **Fonte:** A VSL é a carta de vendas longa de resposta direta em vídeo; estrutura derivada de Eugene M. Schwartz, *Breakthrough Advertising* (1966), Joseph Sugarman, *The Adweek Copywriting Handbook* (2007) e Dan S. Kennedy, *The Ultimate Sales Letter* (2011) — via [`../../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../../reference/books/copywriting/schwartz-breakthrough-advertising.md), [`../../reference/books/copywriting/sugarman-adweek-copywriting.md`](../../reference/books/copywriting/sugarman-adweek-copywriting.md) e [`../../reference/books/copywriting/kennedy-ultimate-sales-letter.md`](../../reference/books/copywriting/kennedy-ultimate-sales-letter.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
