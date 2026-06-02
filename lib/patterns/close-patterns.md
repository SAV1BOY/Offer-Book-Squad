---
id: lib.pattern.close-patterns
title: "Padrões de Fechamento (do valor ao 'sim', e do 'não' ao downsell)"
type: pattern
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [copy/pas, copy/pastor, scarcity-urgency-engine, money-model-designer/upsell-downsell-logic]
tags: [pattern, close, objection-handling, downsell, reuse]
---

# Padrões de Fechamento (do valor ao "sim", e do "não" ao downsell)

## O que é
O fechamento é a sequência que leva o leitor da última hesitação até a ação — e que recupera o "não" em vez de deixá-lo ir embora. Um fechamento SOTA não "pressiona": ele **remove o último medo**, **dá um motivo verdadeiro para agir agora**, e tem um **plano B** para quem recusa. Este padrão organiza a ordem dos blocos de fechamento e a lógica do downsell.

A ordem importa. Valor primeiro, depois reversão de risco, depois escassez verdadeira, depois o CTA — nunca o contrário. Apresentar preço antes do valor, ou escassez antes da garantia, derruba a conversão. Reutilizável em VSL, página de venda, último e-mail e call. Usa os componentes [`guarantee-block`](../components/guarantee-block.md), [`scarcity-block`](../components/scarcity-block.md) e [`cta-block`](../components/cta-block.md).

## Estrutura do padrão
A espinha canônica do fechamento (sequência fixa):

1. **Recapitule o valor** — a [pilha](../components/value-stack-block.md) somada, o resultado em uma linha.
2. **Reverta o risco** — a [garantia](../components/guarantee-block.md) real, depois do valor.
3. **Ancore o preço** — preço contra a soma alta da pilha (o preço parece pequeno).
4. **Dê o motivo de agir agora** — a [escassez verdadeira](../components/scarcity-block.md).
5. **CTA único** — uma ação, sem fricção (ver [`cta-block`](../components/cta-block.md)).
6. **Trate as 3 últimas objeções** — preço, ceticismo, tempo — cada uma com [prova](../components/proof-block.md).
7. **Se "não" → downsell:** reduz escopo, parcela, ou oferece a versão menor (ver [`offer-types`](../taxonomies/offer-types.md)).

O downsell salva margem que sumiria: quem disse "não" ao núcleo pode dizer "sim" a um payment plan ou a uma versão enxuta.

## Quando aplicar
- No terço final de toda peça de venda, depois que o valor já foi construído.
- No fechamento de carrinho e nos e-mails finais da sequência.
- Sempre que houver um "não" recuperável — o downsell é regra, não exceção.

Não feche sem reverter risco. E não use escassez antes da garantia: medo antes de segurança trava a decisão.

## Exemplo
> **Recap:** *"Você leva o método, a planilha, os modelos e a aula de tráfego — R$ 3.800 de valor."*
> **Reversão:** *"Se não recuperar +15% em 60 dias, eu devolvo o dobro."*
> **Âncora + preço:** *"Não são R$ 3.800. Hoje, R$ 497."*
> **Escassez real:** *"40 vagas, carrinho fecha sexta."*
> **CTA:** *"Garanta sua vaga agora →."*
> **Objeção (tempo):** *"Leva 2h pra instalar; a gente faz junto na call de setup."* (com prova).
> **Downsell ao "não":** *"Sem caixa pros R$ 497 hoje? Comece com 3x de R$ 197."*

A ordem cria segurança antes de urgência, e o downsell recupera quem ia embora.

## Variações
- **PAS / PASTOR no corpo:** estruture a tensão com [`copy/pas`](../../frameworks/copy/pas.md) ou [`copy/pastor`](../../frameworks/copy/pastor.md) antes do fechamento.
- **Fechamento de webinar:** abre o carrinho ao vivo, empilha bônus de ação rápida, escassez de tempo real.
- **Downsell por parcelamento:** mantém o produto, divide o preço — preserva o resultado prometido.
- **Downsell por escopo:** versão menor do núcleo (menos suporte, menos bônus), preço menor.
- **Take-away close:** reforça a exclusão honesta ("não é pra todo mundo") para subir o desejo de quem é fit.

## Liga com
- **Frameworks:** [`copy/pas`](../../frameworks/copy/pas.md), [`copy/pastor`](../../frameworks/copy/pastor.md), [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md), [`money-model-designer/upsell-downsell-logic`](../../frameworks/money-model-designer/upsell-downsell-logic.md).
- **Taxonomias:** [`offer-types`](../taxonomies/offer-types.md) (downsell), [`guarantee-types`](../taxonomies/guarantee-types.md).
- **Componentes:** [`guarantee-block`](../components/guarantee-block.md), [`scarcity-block`](../components/scarcity-block.md), [`cta-block`](../components/cta-block.md), [`proof-block`](../components/proof-block.md).
- **Padrões:** [`upsell-patterns`](upsell-patterns.md) (o degrau acima), [`lead-patterns`](lead-patterns.md) (a abertura).
- **Agentes:** `vsl-webinar-scriptwriter` (dono — escreve o fechamento), `money-model-designer` (desenha o downsell), `compliance-auditor` (valida escassez e garantia).
