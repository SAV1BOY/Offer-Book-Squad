---
id: framework.guarantee-design
title: "Guarantee Design — Desenho de Garantia (Reversão de Risco)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [value-equation, risk-reversal-ladder, offer-stack-builder, proof-to-claim-chain, grand-slam-offer]
sources:
  - "Alex Hormozi, *$100M Offers* (2021), capítulo de Garantias."
tags: [guarantee, risk-reversal, probability, conversion, compliance]
---

# Guarantee Design — Desenho de Garantia

## TL;DR
A garantia transfere o risco do comprador para o vendedor — a alavanca mais barata para subir a **Probabilidade percebida** da [Value Equation](value-equation.md) sem mexer no preço. Existem quatro famílias: **incondicional, condicional, anti-garantia e implícita**. Você escolhe a mais forte que a **operação consegue honrar** e que casa com o mercado. O `unit-economics-stack-analyst` desenha; o `compliance-auditor` **veta** qualquer promessa que a operação não sustente. Garantia real é conversão; garantia fictícia é dano de marca e risco legal.

## Quando usar / Quando não
**Use** em toda oferta de núcleo — a reversão de risco é quase sempre a alavanca de conversão de maior ROI.
**Use** a [escada de reversão](risk-reversal-ladder.md) para subir da garantia condicional simples até a "melhor que grátis" conforme a confiança no resultado cresce.
**Não use** garantia que a margem não absorve ou que a entrega não controla — é veto.
**Não use** garantia incondicional em mercado de altíssimo churn de oportunistas sem antes filtrar; às vezes a anti-garantia (com motivo real) eleva o compromisso.

## Inputs
- A taxonomia dos 13 tipos — ver [`../lib/taxonomies/guarantee-types.md`](../lib/taxonomies/guarantee-types.md).
- A **taxa de refund histórica** e a **margem** disponível (do `unit-economics-stack-analyst`).
- O **resultado** que você controla vs o que depende do cliente (define condicional vs incondicional).
- A objeção/risco dominante do avatar (do mapa de objeções).
- Regras setoriais e legais aplicáveis (saúde, finanças, etc.).

## Procedimento
1. **Nomeie o risco dominante** do avatar: "e se não funcionar para mim?", "e se eu perder dinheiro/tempo?". A garantia precisa anular **esse** medo.
2. **Decida a família**: o resultado depende do esforço do cliente? → **condicional** (cliente cumpre a parte dele). Você controla a entrega? → cabe **incondicional**. Exclusividade/custo de revelação? → **anti-garantia** com motivo. Pode atrelar pagamento a resultado? → **implícita/performance**.
3. **Escolha o tipo** na taxonomia (1-13) que dá a maior reversão **honrável**.
4. **Defina condições claras**: prazo, marcos, o que o cliente precisa provar que fez. Condição vaga gera disputa.
5. **Teste a sustentabilidade econômica**: simule o pior caso (X% aciona) contra a margem. Se quebra o LTV, suba a condição ou troque o tipo.
6. **Acople à pilha**: posicione a garantia no [offer stack](offer-stack-builder.md) e na copy **depois** do valor, **antes** do preço.
7. **Conecte à prova**: cada promessa da garantia aponta para evidência ([`proof-to-claim-chain.md`](proof-to-claim-chain.md)).
8. **Passe pelo compliance**: confirme exequibilidade e conformidade legal; rode `guarantee-checklist` e o gate de compliance.
9. **Registre** a garantia escolhida e suas condições no `offer-registry`.

## Outputs
- **Garantia especificada**: tipo, condições, prazo, marcos, exceções.
- Simulação de pior caso vs margem (sustentável: sim/não).
- Posição da garantia na pilha e no roteiro de copy.
- Veredito de exequibilidade e compliance.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Risco dominante**: "já tentei e desisti — e se eu não falar de verdade?".
- **Família**: o resultado depende do cliente fazer as sessões → **condicional de serviço**.
- **Tipo (3)**: "Aprovado na entrevista em 60 dias ou seguimos juntos de graça até você ser aprovado" — exige que o cliente complete as simulações.
- **Condições**: 60 dias, mínimo de 8 simulações concluídas, 1 entrevista real tentada.
- **Pior caso**: estimativa de 8% aciona o "seguir junto"; custo marginal de mentoria absorvido pela margem de 70%. Sustentável.
- **Posição**: entra após a pilha, antes do preço, ancorada em 3 depoimentos de aprovação.
- **Resultado**: a Probabilidade percebida sobe de 4 para 8 sem tocar no preço — e a condição filtra o cliente que não faz a parte dele.

## Armadilhas
- **Garantia que a operação não honra.** Destrói margem, LTV e marca, além de risco legal — veto certo.
- **Condição vaga.** "Se você se esforçar" gera disputa; defina marcos verificáveis.
- **Garantia antes do valor.** Reverter risco antes de construir desejo enfraquece o efeito. Valor primeiro.
- **Copiar a garantia do concorrente sem checar a própria entrega.** O que ele sustenta, você pode não sustentar.
- **Exagerar para impressionar a copy.** "Devolvo 10× se falhar" sem lastro é claim sem prova — risco de compliance.

## Interações
- **Agentes**: `unit-economics-stack-analyst` (dono — desenha e testa a sustentabilidade); `compliance-auditor` (**veta** garantia inexequível ou ilegal); `value-equation-engineer` (mede o ganho de Probabilidade); `proof-credibility-curator` (liga garantia a prova); `vsl-webinar-scriptwriter` (posiciona depois do valor, antes do preço — gate `vsl/vsl-risk-reversal-gate`).
- **Frameworks que pareiam**: [`risk-reversal-ladder.md`](risk-reversal-ladder.md), [`value-equation.md`](value-equation.md), [`offer-stack-builder.md`](offer-stack-builder.md), [`proof-to-claim-chain.md`](proof-to-claim-chain.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Offers* (2021), capítulo de Garantias — via [`../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
