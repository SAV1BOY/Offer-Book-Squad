---
id: lib.pattern.upsell-patterns
title: "Padrões de Upsell (subir o AOV no pico de compra)"
type: pattern
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
frameworks: [money-model-sequence, money-model-designer/upsell-downsell-logic]
tags: [pattern, upsell, aov, money-model, reuse]
---

# Padrões de Upsell (subir o AOV no pico de compra)

## O que é
O upsell é a oferta feita **no momento exato da compra** — o pico de intenção, quando o cliente já decidiu confiar e gastar. Esperar para vender depois desperdiça esse pico. Este padrão organiza os tipos de upsell e a lógica de quando disparar cada um, para subir o ticket médio (AOV) sem irritar o comprador.

A premissa do squad: o centro não é a oferta avulsa, é a **sequência** (princípio `money_model_spine`). Ver [`offer-types`](../taxonomies/offer-types.md) e [`money-model-sequence`](../../frameworks/money-model-sequence.md). O upsell é o degrau que vem logo após a oferta núcleo na escada — e este padrão é reutilizável em qualquer funil de checkout, página de obrigado ou ligação de vendas.

## Estrutura do padrão
A regra de ouro: **o upsell resolve o "e agora?" que a compra acabou de criar**. Cinco famílias, do mais natural ao menos:

1. **Upgrade (mais do mesmo, melhor):** versão premium do que ele comprou.
2. **Velocidade (chega lá mais rápido):** acelera o resultado — done-with-you, acesso prioritário.
3. **Feito-para-você (DFY):** removemos todo o esforço — o salto de valor mais caro.
4. **Volume (mais quantidade):** mais unidades, mais licenças, mais assentos.
5. **Acesso/Proximidade:** mentoria, grupo, contato direto — escassez verdadeira embutida.

Sequência de disparo: oferta núcleo aceita → **upsell #1 (o mais lógico para o resultado)** → se "sim", upsell #2 complementar → se "não", desce para o [downsell](close-patterns.md). Cada degrau tem **um** CTA (ver [`cta-block`](../components/cta-block.md)).

## Quando aplicar
- No checkout, logo após o "sim" da oferta núcleo (one-click upsell).
- Na página de obrigado, quando o cliente está no auge do entusiasmo.
- Em call de vendas, depois do fechamento principal, nunca antes.

Não empilhe 4 upsells em sequência só por ganância — cada "não" esfria o próximo "sim". Pare quando a lógica acaba.

## Exemplo
> **Núcleo: Motor de Recuperação 72h (R$ 497).** Cliente compra.
> **Upsell #1 — Velocidade (R$ 297):** *"Quer que a gente configure tudo pra você na primeira semana, em vez de você fazer sozinho? Adicione o Setup Feito-Para-Você."* (resolve o "e agora começo como?").
> **Upsell #2 — Acesso (R$ 197/mês):** *"Quer revisão mensal das suas campanhas comigo? Entre no grupo de otimização."* (continuidade real).
> Se recusa o #1 → desce para um **payment plan** do próprio setup.

Cada upsell responde a uma pergunta que a compra criou. O AOV sobe de R$ 497 para até R$ 991 + recorrência.

## Variações
- **Bump de checkout:** mini-upsell de baixo preço (um clique, no próprio checkout) antes do upsell principal.
- **Upsell por resultado:** só oferece o próximo degrau quando o cliente atinge um marco (alinha com [`continuity-patterns`](continuity-patterns.md)).
- **Tripwire → núcleo:** quando a entrada foi um [tripwire](../taxonomies/offer-types.md), o "upsell" é a própria oferta núcleo.
- **DFY como teto:** posicione o feito-para-você como o degrau mais caro, ancorando os demais.

## Liga com
- **Frameworks:** [`money-model-sequence`](../../frameworks/money-model-sequence.md) (a escada completa), [`money-model-designer/upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md).
- **Taxonomias:** [`offer-types`](../taxonomies/offer-types.md) (papéis na escada).
- **Componentes:** [`cta-block`](../components/cta-block.md), [`value-stack-block`](../components/value-stack-block.md).
- **Padrões:** [`close-patterns`](close-patterns.md) (o downsell quando o upsell falha), [`continuity-patterns`](continuity-patterns.md).
- **Agentes:** `money-model-designer` (dono — sequencia os degraus), `unit-economics-stack-analyst` (valida margem), `vsl-webinar-scriptwriter` (escreve os upsells da página de obrigado).
