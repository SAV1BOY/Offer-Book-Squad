---
id: lib.pattern.continuity-patterns
title: "Padrões de Continuidade (receita recorrente e LTV)"
type: pattern
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, money-model-designer/continuity-design]
tags: [pattern, continuity, recurring-revenue, ltv, retention, reuse]
---

# Padrões de Continuidade (receita recorrente e LTV)

## O que é
A continuidade é a parte da escada onde mora a **receita recorrente** e o **LTV** — assinatura, comunidade, consumível que se recompra. Sem continuidade, todo lançamento recomeça do zero a cada mês. Com ela, a base paga repetidamente e o negócio fica previsível. Este padrão organiza os modelos de continuidade e a lógica de **retenção** (porque vender a assinatura é fácil; manter é o jogo).

A premissa do squad: o centro é a sequência (princípio `money_model_spine`), e a continuidade é o último degrau que multiplica o valor de cada cliente. Ver [`offer-types`](../taxonomies/offer-types.md) e [`money-model-sequence`](../../frameworks/money-model-sequence.md). Reutilizável em qualquer modelo — info, serviço, físico, SaaS.

## Estrutura do padrão
A regra de ouro da continuidade: **o cliente fica enquanto recebe valor que ele sentiria falta**. Três modelos e três alavancas de retenção:

**Modelos:**
1. **Assinatura de acesso** — conteúdo, ferramenta ou software contínuo (libera enquanto entrega; ver garantia "liberação de serviço" em [`guarantee-types`](../taxonomies/guarantee-types.md)).
2. **Comunidade** — pertencimento, suporte de pares, atualização constante. A retenção vem do vínculo, não só do conteúdo.
3. **Consumível / recompra** — produto físico ou crédito que acaba e se repõe (a recorrência é natural).

**Alavancas de retenção:**
- **Resultado contínuo:** a cada ciclo, um novo ganho (o cliente vê progresso).
- **Vínculo:** rituais, presença, identidade de grupo.
- **Custo de troca:** dados, histórico, integrações que tornam sair caro.

Sequência: a continuidade é **oferecida no auge do resultado** do núcleo, não no checkout frio. "Você atingiu o primeiro resultado — agora mantenha e amplie."

## Quando aplicar
- Como degrau final da escada, depois que o núcleo entregou a primeira transformação.
- Quando o produto tem valor recorrente real (não force assinatura em produto de uso único).
- Para transformar um pico de lançamento em receita previsível mês a mês.

Não venda continuidade antes do primeiro resultado. Recorrência sem valor percebido vira cancelamento e chargeback.

## Exemplo
> **Núcleo entregue:** o cliente recuperou +21% de receita no primeiro mês.
> **Oferta de continuidade — Comunidade de Otimização (R$ 197/mês):** *"Você já tem o motor rodando. Agora, toda semana, a gente revisa juntos os números e ajusta a sequência. Atualizações novas entram automático."*
> **Retenção:** resultado contínuo (novo ajuste por semana) + vínculo (grupo ativo) + custo de troca (histórico de campanhas mora lá).
> Garantia atrelada: *"Cancele quando quiser; você só paga enquanto recebe valor."* (liberação de serviço).

A continuidade é oferecida no auge, entrega ganho recorrente, e a garantia honesta reduz o atrito de entrar.

## Variações
- **Anuidade com desconto:** versão anual que melhora o cashflow e a retenção (menos pontos de cancelamento).
- **Continuidade por níveis:** básico → pro → mastermind, subindo acesso e proximidade.
- **Win-your-money-back recorrente:** o cliente recupera a mensalidade ao atingir um marco — alinha incentivo (ver [`offer-types`](../taxonomies/offer-types.md)).
- **Consumível auto-recompra:** assinatura de reposição com cancelamento fácil.
- **Comunidade como fosso:** quando o vínculo de pares é o produto, a retenção independe de conteúdo novo.

## Liga com
- **Frameworks:** [`money-model-sequence`](../../frameworks/money-model-sequence.md) (a escada), [`money-model-designer/continuity-design`](../../frameworks/money-model-designer/continuity-design.md).
- **Taxonomias:** [`offer-types`](../taxonomies/offer-types.md) (papel de continuidade), [`guarantee-types`](../taxonomies/guarantee-types.md) (liberação de serviço).
- **Padrões:** [`upsell-patterns`](upsell-patterns.md) (degrau anterior), [`close-patterns`](close-patterns.md).
- **Utilities:** [`roi-calculator`](../utilities/roi-calculator.md) (o LTV que a continuidade gera).
- **Agentes:** `money-model-designer` (dono — desenha o degrau de continuidade), `unit-economics-stack-analyst` (modela LTV e churn), `events-logistics-coordinator` (logística da comunidade/entrega recorrente).
