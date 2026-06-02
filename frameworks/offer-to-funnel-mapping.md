---
id: framework.offer-to-funnel-mapping
title: "Offer-to-Funnel Mapping — Cada Degrau do Money Model → Páginas → Sequências"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, offer-stack-builder, scarcity-urgency-engine, proof-to-claim-chain, grand-slam-offer]
sources:
  - "Russell Brunson, *DotCom Secrets* (2015) — value ladder e funis."
  - "Alex Hormozi, *$100M Money Models* (2025) — sequência de ofertas."
tags: [funnel, mapping, money-model, pages, sequences, handoff]
---

# Offer-to-Funnel Mapping — Da Escada ao Funil

## TL;DR
A [escada do money model](money-model-sequence.md) é a estratégia; o funil é a **execução**. Este framework traduz **cada degrau** (Atração, Núcleo, Upsell, Downsell, Continuidade) em **páginas** concretas (captura, vendas, checkout, upsell, obrigado) e **sequências** (e-mail/SMS de aquecimento, carrinho, abandono, pós-compra). A regra: **um degrau órfão** — sem página e sem sequência — é dinheiro deixado na mesa. O `money-model-designer` define o mapa; o `funnel-architect` o constrói. Sem becos sem saída: todo "sim" e todo "não" têm próximo passo.

## Quando usar / Quando não
**Use** logo após a escada do money model existir e antes de o `funnel-architect` desenhar telas.
**Use** como ponte do Offer Book para a camada de funil/tech (D5) — é o handoff que evita reconstrução.
**Não use** antes da escada estar fechada: mapear funil de uma sequência incompleta gera retrabalho.
**Não use** para inventar degraus que a escada não tem — o mapa **serve** a escada, não a expande.

## Inputs
- A **escada do money model** completa (degraus, ofertas, preços, gatilhos).
- Os **CTAs por degrau** e os mecanismos de [escassez/urgência](scarcity-urgency-engine.md) reais.
- A **pilha de valor** e a prova por componente ([`offer-stack-builder.md`](offer-stack-builder.md), [`proof-to-claim-chain.md`](proof-to-claim-chain.md)).
- O lead/abertura por segmento (da [matriz de consciência](awareness-x-sophistication.md)).
- As regras de carrinho (datas de abertura/fechamento).

## Procedimento
1. **Liste os degraus** da escada em ordem (Atração → Núcleo → Upsell → Downsell → Continuidade).
2. **Mapeie cada degrau para suas páginas**: Atração → página de captura/tripwire; Núcleo → página de vendas/VSL + checkout; Upsell → página de upsell pós-checkout (1-clique); Downsell → página de downsell; Continuidade → página de assinatura/portal.
3. **Mapeie cada degrau para suas sequências**: aquecimento (pré-carrinho), carrinho aberto, últimas horas, abandono de checkout, pós-compra/onboarding, recuperação.
4. **Defina o caminho do "sim" e do "não"** em cada nó: quem compra vai para o upsell; quem recusa vai para o downsell; quem abandona entra na recuperação. **Nenhum beco sem saída** (gate `funnel/funnel-no-dead-end-gate`).
5. **Posicione a prova e a escassez** em cada página/sequência (prova ligada ao claim daquele degrau; contador refletindo a data real).
6. **Especifique cada página** (objetivo, único CTA, elementos de valor/prova/garantia) para o `funnel-architect`.
7. **Cubra o backend**: garanta que Upsell, Downsell e Continuidade existem de fato no funil (gate `funnel/funnel-backend-gate`) — é onde mora a margem.
8. **Verifique a cobertura**: toda oferta da escada tem ao menos uma página **e** uma sequência? Marque órfãos.
9. **Registre** o mapa degrau→página→sequência no `decision-registry` e passe para D5.

## Outputs
- **Matriz de mapeamento**: degrau × páginas × sequências × CTA × prova × escassez.
- Diagrama do caminho do "sim"/"não" (sem becos sem saída).
- Specs de página prontas para o `funnel-architect`.
- Lista de órfãos (degraus sem página/sequência) — zerada antes do handoff.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Atração** (e-book R$27) → *página de captura + checkout simples*; *sequência*: 3 e-mails de entrega + 2 de transição para o núcleo.
- **Núcleo** (programa R$1.997) → *VSL + página de vendas + checkout*; *sequências*: aquecimento (5 dias), carrinho aberto, últimas 3 horas.
- **Upsell** (simulador 1:1 R$897) → *página de upsell 1-clique* pós-checkout; sem nova cobrança de dados.
- **Downsell** (12× sem 1:1) → *página de downsell* exibida no "não" do checkout à vista.
- **Continuidade** (clube R$97/mês) → *página de assinatura + portal*; *sequência*: onboarding + retenção mensal.
- **Caminho do não**: recusou o núcleo → downsell; abandonou o checkout → sequência de recuperação (gate de não-beco).
- **Resultado**: cada degrau tem página **e** sequência; nenhum "sim" ou "não" fica sem próximo passo. O handoff para D5 não exige reconstruir a estratégia.

## Armadilhas
- **Degrau órfão.** Upsell ou Continuidade sem página/sequência = margem perdida no backend.
- **Beco sem saída.** "Não" sem downsell e abandono sem recuperação descartam vendas recuperáveis.
- **Mapear antes de fechar a escada.** Funil de sequência incompleta vira retrabalho.
- **Prova/escassez genéricas.** Cada página precisa da prova **daquele** claim e do contador **real** daquele carrinho.
- **Dois CTAs por página.** Quebra o foco; um pedido por página.

## Interações
- **Agentes**: `money-model-designer` (dono — define o mapa); `funnel-architect` (constrói páginas e checa não-becos/backend); `email-sms-sequence-writer` (escreve as sequências mapeadas); `vsl-webinar-scriptwriter` (produz a VSL do núcleo); `tech-links-deliverability-engineer` (URLs e entregabilidade das sequências); `compliance-auditor` (escassez real nas páginas).
- **Frameworks que pareiam**: [`money-model-sequence.md`](money-model-sequence.md), [`offer-stack-builder.md`](offer-stack-builder.md), [`scarcity-urgency-engine.md`](scarcity-urgency-engine.md), [`proof-to-claim-chain.md`](proof-to-claim-chain.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md).

## Fontes
> **Fonte:** Russell Brunson, *DotCom Secrets* (2015), value ladder e funis; Alex Hormozi, *$100M Money Models* (2025) — via [`../reference/books/launches-and-funnels/brunson-dotcom-secrets.md`](../reference/books/launches-and-funnels/brunson-dotcom-secrets.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
