---
id: reference.psychology.social-proof
title: "Prova Social"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Robert B. Cialdini, *Influence: The Psychology of Persuasion* (New and Expanded, 2021), Harper Business"
  - "Robert B. Cialdini, *Pre-Suasion* (2016), Simon & Schuster"
  - "Solomon Asch, *Opinions and Social Pressure* (1955), Scientific American"
tags: [psychology, social-proof, testimonials, proof, conformity, ethics]
---

# Prova Social

## Conceito
A prova social diz que olhamos para os outros para decidir o que fazer. Quando estamos inseguros, copiamos quem parece com a gente. Se muita gente faz algo, presumimos que é certo. Por isso filas atraem, "mais vendido" vende, e depoimentos convencem mais que promessas do próprio vendedor. A multidão é um atalho para a decisão.

Cialdini listou a prova social entre as armas de influência. Asch mostrou o poder da conformidade: pessoas davam respostas erradas óbvias só para acompanhar o grupo. O efeito é mais forte em duas condições: incerteza (não sei o que fazer) e semelhança (essa gente é como eu). O comprador na dúvida pergunta, sem perceber: "o que pessoas iguais a mim escolheram?".

## Por que funciona (mecanismo cognitivo)
Avaliar tudo sozinho é caro e arriscado. A experiência dos outros é informação grátis. Se mil pessoas compraram e ficaram bem, provavelmente é seguro. O cérebro terceiriza o julgamento para a maioria e poupa energia. É o Sistema 1 economizando análise.

A prova social também reduz o medo do erro e do arrependimento. Se eu seguir o grupo e der errado, a culpa se dilui: todos erraram juntos. Seguir a maioria é seguro mesmo quando é errado. Por isso a prova de pares específicos — gente da mesma profissão, idade ou situação — vence a prova genérica. O comprador não quer saber que "muitos compraram". Quer saber que "alguém como eu comprou e funcionou".

## Aplicação em ofertas & copy
A prova social começa na curadoria. O `proof-credibility-curator` coleta e organiza depoimentos, números e casos, e liga cada prova a um claim e a uma objeção ([`../../frameworks/proof-to-claim-chain.md`](../../frameworks/proof-to-claim-chain.md), [`../../data/registries/proof-registry.md`](../../data/registries/proof-registry.md)). O `avatar-voc-investigator` mapeia as objeções para a copy escolher a prova que derruba cada dúvida específica.

Na VSL, o `vsl-webinar-scriptwriter` posiciona prova social logo após cada promessa grande: a promessa cria a dúvida, o depoimento a resolve ([`../../frameworks/copy/vsl-structure.md`](../../frameworks/copy/vsl-structure.md)). Usa casos de pessoas parecidas com o avatar, com nome, foto e número. O `email-sms-sequence-writer` espalha um caso por e-mail na sequência, cada um mirando uma objeção diferente. O `ad-creative-factory` usa contadores reais ("12 mil alunos") e prints de resultado como gancho, sempre com lastro ([`../../checklists/ads/ads-claim-backing-gate.md`](../../checklists/ads/ads-claim-backing-gate.md)). O `value-equation-engineer` trata a prova como redutor do esforço e da dúvida percebidos: ver outros conseguindo aumenta a probabilidade percebida de sucesso, uma alavanca direta de valor ([`../../frameworks/value-equation.md`](../../frameworks/value-equation.md)).

## Exemplo
Um curso de confeitaria tinha uma VSL cheia de promessas e quase nenhuma prova. A conversão era baixa. O time inseriu três blocos de prova social. Depois da promessa de renda extra, entrou o caso da Dona Marta, 54 anos, dona de casa, que fez 3 mil reais no primeiro mês, com print do pedido. Depois da promessa de facilidade, o caso de um iniciante que nunca tinha assado nada. No fim, o contador real de 8.400 alunas. Cada prova mirava a objeção que vinha logo antes. A conversão subiu porque a aluna viu gente igual a ela vencendo.

## Armadilhas & ética
A prova social só funciona de verdade quando é verdadeira. A linha é uma só: nada de depoimento falso, número inflado ou resultado atípico vendido como típico. O `compliance-auditor` veta prova fabricada e exige a ressalva de que resultados variam, conforme as regras de publicidade ([`../../checklists/compliance/compliance-claim-backing-gate.md`](../../checklists/compliance/compliance-claim-backing-gate.md)). Todo depoimento precisa de consentimento e origem rastreável no `proof-registry`. Mostrar clientes reais que tiveram resultado real é serviço ao próximo comprador. Inventar a multidão é fraude. A prova aponta para fatos verificáveis. Sempre.

## Cross-refs
- [`authority-bias.md`](authority-bias.md) — prova de especialista, irmã da prova de pares.
- [`identity-and-belonging.md`](identity-and-belonging.md) — seguir os pares e pertencer à tribo.
- [`scarcity-principle.md`](scarcity-principle.md) — "todos querem" reforça que é raro e bom.
- [`cognitive-biases-for-offers.md`](cognitive-biases-for-offers.md) — índice geral dos vieses.
- [`../../frameworks/proof-to-claim-chain.md`](../../frameworks/proof-to-claim-chain.md) — cada claim com sua prova.
- [`../books/persuasion-psychology/cialdini-influence.md`](../books/persuasion-psychology/cialdini-influence.md) — a arma da prova social.

## Fontes
> **Fonte:** Robert B. Cialdini, *Influence* (2021), Harper Business — cap. "Social Proof". Robert B. Cialdini, *Pre-Suasion* (2016), Simon & Schuster. Solomon Asch, *Opinions and Social Pressure* (1955), Scientific American — conformidade.
> **Anti-verbatim:** princípios e estrutura em redação original. Citação literal ≤ 25 palavras, atribuída.
