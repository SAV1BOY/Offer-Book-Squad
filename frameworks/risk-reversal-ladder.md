---
id: framework.risk-reversal-ladder
title: "Risk Reversal Ladder — Do Condicional ao 'Melhor que Grátis'"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [guarantee-design, value-equation, offer-stack-builder, proof-to-claim-chain, grand-slam-offer]
sources:
  - "Alex Hormozi, *$100M Offers* (2021), garantias e reversão de risco."
  - "Jay Abraham — conceito de risk reversal (popularizado em marketing direto)."
tags: [risk-reversal, guarantee-ladder, probability, conversion, better-than-free]
---

# Risk Reversal Ladder — A Escada de Reversão de Risco

## TL;DR
Reversão de risco não é "ter garantia ou não". É uma **escada**: do degrau mais simples (garantia condicional) ao mais ousado ("melhor que grátis" — você sai ganhando mesmo se pedir reembolso). Quanto mais alto o degrau, mais a **Probabilidade percebida** sobe — desde que a operação **sustente** aquele degrau. Você sobe a escada à medida que a confiança no resultado e a margem permitem. O `unit-economics-stack-analyst` escolhe o degrau; o `compliance-auditor` confirma que ele é honrável.

## Quando usar / Quando não
**Use** para decidir **quão longe** ir na garantia — não só qual tipo, mas qual **nível de ousadia**.
**Use** para escalar a reversão entre versões/testes: comece num degrau e suba conforme a prova de resultado cresce.
**Não use** um degrau que a margem não absorve ou a entrega não controla — subir alto demais quebra o negócio (veto).
**Não use** a escada como enfeite de copy: cada degrau é uma promessa operacional real.

## Inputs
- Os 13 tipos de garantia — ver [`../lib/taxonomies/guarantee-types.md`](../lib/taxonomies/guarantee-types.md).
- A **taxa de acionamento estimada** e a **margem** por degrau (do `unit-economics-stack-analyst`).
- O **grau de controle** sobre o resultado (quanto depende de você vs do cliente).
- A objeção/risco dominante do avatar.
- A prova de resultado disponível ([`proof-to-claim-chain.md`](proof-to-claim-chain.md)) — quanto mais forte, mais alto dá para subir.

## Procedimento
1. **Defina os degraus** da escada, do mais conservador ao mais ousado:
   1. **Condicional simples** — reembolso se o cliente cumprir a parte dele.
   2. **Incondicional** — reembolso sem perguntas no prazo.
   3. **Garantia de serviço** — seguimos trabalhando de graça até o resultado.
   4. **Dobro/ampliada** — devolve mais que o pago se falhar.
   5. **Melhor que grátis** — além do reembolso, o cliente fica com um bônus de valor (você "paga" para ele ter tentado).
   6. **Performance/implícita** — você só ganha se o cliente ganhar.
2. **Posicione sua oferta no degrau atual**: dado o controle sobre o resultado e a prova, onde você consegue ficar **hoje** com honestidade?
3. **Simule o pior caso de cada degrau acima**: se X% aciona, a margem aguenta? Qual o impacto no LTV?
4. **Escolha o degrau mais alto sustentável**: a maior reversão que a operação honra sem quebrar.
5. **Reforce com prova**: cada degrau ousado precisa de prova proporcional — "dobro do dinheiro" exige histórico forte de resultado.
6. **Defina as condições** (prazo, marcos) para fechar brechas, sobretudo nos degraus condicionais.
7. **Planeje a subida**: defina o gatilho para subir um degrau no próximo ciclo (mais depoimentos, churn de refund estável).
8. **Acople à pilha e ao preço**: a reversão entra após o valor, antes do número ([`offer-stack-builder.md`](offer-stack-builder.md), [`price-anchoring.md`](price-anchoring.md)).
9. **Registre** o degrau e a simulação no `offer-registry`; rode `guarantee-checklist` e o gate de compliance.

## Outputs
- **Degrau escolhido** + os degraus acima/abaixo mapeados.
- Simulação de pior caso por degrau (sustentável: sim/não).
- Condições e prova exigidas para o degrau atual.
- Plano de subida (gatilho para o próximo nível).

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Degrau 1 (atual no lançamento-piloto)**: "aprovado em 60 dias **ou seguimos juntos** até passar" (garantia de serviço condicional). Controle parcial → começa aqui.
- **Simulação degrau 4 (dobro)**: "não passou? devolvo o dobro" — exigiria taxa de aprovação comprovada >90%; ainda não há histórico. **Não subir agora.**
- **Simulação degrau 5 (melhor que grátis)**: "não passou? devolvo + você fica com o Banco de Frases (R$497)". Custo marginal baixo, reversão enorme. **Candidato ao próximo ciclo**, quando os depoimentos crescerem.
- **Escolha**: fica no degrau 1 (serviço) no piloto; gatilho de subida = 30 aprovações documentadas → sobe para o degrau 5.
- **Resultado**: a Probabilidade percebida sobe sem arriscar a margem; a escada dá um caminho de evolução, não uma aposta única.

## Armadilhas
- **Subir alto demais cedo.** "Dobro do dinheiro" sem histórico de resultado quebra a margem e a confiança.
- **Degrau sem prova proporcional.** Quanto mais ousado, mais prova ele exige; sem isso, soa a desespero.
- **Ignorar o controle do resultado.** Se o resultado depende do cliente, degraus incondicionais convidam ao abuso — use condicional com marcos.
- **Tratar como enfeite.** Cada degrau é promessa operacional; o compliance veta o que a operação não honra.
- **Não planejar a subida.** Ficar no degrau 1 para sempre desperdiça conversão que a prova já permitiria.

## Interações
- **Agentes**: `unit-economics-stack-analyst` (dono — escolhe e simula o degrau); `compliance-auditor` (**veta** degrau inexequível); `value-equation-engineer` (mede o ganho de Probabilidade por degrau); `pricing-wtp-strategist` (posiciona a reversão na ancoragem); `proof-credibility-curator` (fornece a prova que destrava degraus altos); `vsl-webinar-scriptwriter` (apresenta a reversão após o valor).
- **Frameworks que pareiam**: [`guarantee-design.md`](guarantee-design.md), [`value-equation.md`](value-equation.md), [`offer-stack-builder.md`](offer-stack-builder.md), [`proof-to-claim-chain.md`](proof-to-claim-chain.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Offers* (2021), garantias e reversão de risco; conceito de risk reversal popularizado por Jay Abraham no marketing direto — via [`../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
