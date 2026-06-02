---
id: framework.scarcity-urgency-engine
title: "Scarcity & Urgency Engine — Escassez e Urgência VERDADEIRAS"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [value-equation, guarantee-design, offer-to-funnel-mapping, proof-to-claim-chain, grand-slam-offer]
sources:
  - "Robert Cialdini, *Influence* (1984) — princípio da Escassez."
  - "Alex Hormozi, *$100M Offers* (2021), seções de Escassez e Urgência."
tags: [scarcity, urgency, cialdini, truthful, compliance, cta]
---

# Scarcity & Urgency Engine — Escassez e Urgência Verdadeiras

## TL;DR
Escassez (quantidade limitada) e urgência (tempo limitado) criam o **custo de adiar** — a razão para agir **agora**. Elas amplificam a [Value Equation](value-equation.md) ao tornar a inação cara. A regra inegociável do squad é `truthful_scarcity`: toda escassez/urgência é **100% real**. Limite fabricado é **veto** do `compliance-auditor`. O `money-model-designer` projeta mecanismos de escassez genuínos (capacidade, cohort, bônus que expira de fato) e o sistema os aplica no funil sem mentir.

## Quando usar / Quando não
**Use** no fechamento de toda oferta com público consciente (sofisticação/consciência altas) — é o empurrão final.
**Use** sobretudo na Continuidade e em lançamentos por cohort, onde a escassez é estrutural e verdadeira.
**Não use** escassez falsa, nunca: contador que reinicia, "últimas vagas" perpétuas, "só hoje" que se repete toda semana. Veto imediato.
**Não use** como muleta para oferta fraca: escassez não conserta valor ruim; só acelera uma decisão que já faria sentido.

## Inputs
- A **restrição real** do negócio: capacidade de atendimento, vagas por cohort, estoque, janela de evento, custo de bônus.
- O cronograma do lançamento (datas de abertura/fechamento de carrinho).
- A objeção "vou pensar depois" no mapa de objeções.
- O bônus/garantia que pode legitimamente expirar ([`guarantee-design.md`](guarantee-design.md)).
- Regras legais de publicidade (FTC/LGPD/CDC) sobre prazos e quantidades.

## Procedimento
1. **Liste as restrições reais** do negócio: quantas pessoas você consegue atender bem? quando a turma fecha? o que de fato acaba? Só o que é verdade entra.
2. **Escolha o tipo de escassez genuína**: quantidade (vagas/estoque), tempo (carrinho fecha em data real), bônus que expira (de fato sai do estoque), ou acesso (cohort que começa junto).
3. **Defina o motivo honesto**: por que limita? "Atendo 30 para manter o 1:1" é real e ainda comunica valor. Escassez com razão crível converte mais que número seco.
4. **Cronometre a urgência** no calendário real: data e hora de fechamento, sequência de avisos (D-3, D-1, últimas horas).
5. **Conecte ao custo de adiar**: explicite o que o avatar **perde** ao esperar (o resultado adiado, o bônus que some, o preço que sobe de verdade).
6. **Mapeie no funil**: cada gatilho de escassez vira elemento de página e e-mail ([`offer-to-funnel-mapping.md`](offer-to-funnel-mapping.md)) — contador que reflete a data real, contagem de vagas que diminui de verdade.
7. **Prove o limite**: se diz "30 vagas", a operação tem que **parar** em 30. A prova é o cumprimento ([`proof-to-claim-chain.md`](proof-to-claim-chain.md)).
8. **Passe pelo compliance**: rode `compliance/compliance-scarcity-truth-gate`. Qualquer elemento sem lastro é removido.
9. **Registre** os mecanismos de escassez e suas fontes de verdade no `offer-registry`.

## Outputs
- **Lista de mecanismos de escassez/urgência reais**, cada um com sua fonte de verdade.
- Motivo honesto declarado por mecanismo.
- Cronograma de urgência (datas, horários, sequência de avisos).
- Especificação dos elementos de funil (contador, contagem de vagas) atrelados ao real.
- Veredito do gate de verdade de escassez.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Escassez real**: a turma é por **cohort** — 40 alunos, porque cada um recebe 8 simulações 1:1 e o mentor não atende mais que isso. Motivo honesto, ligado a valor.
- **Urgência real**: o carrinho abre por **5 dias** e fecha porque a turma começa junto numa data fixa. Avisos em D-3, D-1 e nas últimas 3 horas.
- **Custo de adiar**: quem espera entra só na próxima turma (3 meses depois) e perde o bônus "Simulador extra" que sai do pacote no fechamento.
- **Funil**: o contador de vagas reflete inscrições reais; ao bater 40, a página troca para "turma fechada — entre na lista".
- **Resultado**: a urgência move a decisão sem nenhuma mentira. Se fabricasse "só restam 3 vagas" sem ser verdade, seria veto e dano de marca.

## Armadilhas
- **Contador que reinicia / "só hoje" perpétuo.** Mentira clássica — veto e perda de confiança quando descoberta.
- **"Últimas vagas" sem limite real.** Se você sempre tem mais vagas, não há escassez; há fraude.
- **Escassez sem motivo.** Número seco converte menos e cheira a truque; dê a razão verdadeira.
- **Escassez para salvar oferta fraca.** Acelera um "não". Conserte o valor primeiro.
- **Funil que não cumpre o limite.** Dizer "30 vagas" e vender 200 destrói a prova e o gate de compliance.

## Interações
- **Agentes**: `money-model-designer` (dono — projeta a escassez estrutural); `compliance-auditor` (**veta** escassez/urgência falsa — `compliance/compliance-scarcity-truth-gate`); `value-equation-engineer` (escassez amplifica o valor já construído); `funnel-architect` (implementa contadores/contagens reais); `email-sms-sequence-writer` (sequência de avisos de fechamento); `launch-producer` (cronograma de carrinho).
- **Frameworks que pareiam**: [`value-equation.md`](value-equation.md), [`guarantee-design.md`](guarantee-design.md), [`offer-to-funnel-mapping.md`](offer-to-funnel-mapping.md), [`proof-to-claim-chain.md`](proof-to-claim-chain.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md).

## Fontes
> **Fonte:** Robert Cialdini, *Influence* (1984), princípio da Escassez; aplicação em Alex Hormozi, *$100M Offers* (2021) — via [`../reference/books/persuasion-psychology/cialdini-influence.md`](../reference/books/persuasion-psychology/cialdini-influence.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
