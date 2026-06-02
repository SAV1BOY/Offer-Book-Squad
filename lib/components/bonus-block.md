---
id: lib.component.bonus-block
title: "Bloco de Bônus (acelera, remove obstáculo, vence objeção)"
type: component
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [offer-stack-builder, value-equation, magic-naming]
tags: [component, bonus, objection-handling, value-stack, reuse]
---

# Bloco de Bônus (acelera, remove obstáculo, vence objeção)

## O que é
Um bônus não é "algo extra de brinde". Um bônus SOTA tem **um trabalho**: ou acelera o resultado, ou remove um obstáculo no caminho, ou mata uma objeção específica de compra. Se um bônus não faz nenhuma dessas três coisas, ele dilui a oferta em vez de fortalecer.

O bloco de bônus nomeia o presente, diz a qual **objeção ou obstáculo** ele responde, e ancora um valor defensável. Reutilizável: o mesmo esqueleto serve para 1 ou 10 bônus, e cada linha vira uma linha do [value stack](value-stack-block.md). O segredo é mapear cada bônus a uma objeção real do [objection-registry](../../data/registries/objection-registry.md) — assim cada bônus "fecha uma porta" que faria o cliente hesitar.

## Quando usar
- Dentro da [pilha de valor](value-stack-block.md), depois da oferta núcleo.
- Quando a pesquisa de VOC revela objeções claras ("não tenho tempo", "não sei por onde começar").
- Para empurrar a decisão **agora** com um bônus de ação rápida (casado com [`scarcity-block`](scarcity-block.md)).

Não empilhe bônus aleatórios para "encher". Bônus sem trabalho definido baixa o valor percebido do conjunto.

## Bloco
```
BÔNUS #{{N}}: {{NOME_MAGNÉTICO}} (valor R$ {{VALOR}})
Trabalho do bônus: {{ACELERA | REMOVE_OBSTÁCULO | VENCE_OBJEÇÃO}}
Objeção/obstáculo que mata: "{{FALA_LITERAL_DO_AVATAR}}"
O que é: {{FORMATO_CONCRETO}} ({{ex.: planilha, aula, template, call}})
Por que tem esse valor: {{LASTRO_DO_PREÇO}}
[Opcional] Só para quem agir até {{PRAZO_VERDADEIRO}}: {{BÔNUS_DE_RAPIDEZ}}
```

Preencha cada `{{...}}`. O campo "Trabalho do bônus" é obrigatório — sem um dos três papéis, corte o bônus.

## Exemplo preenchido
> **BÔNUS #1: Kit Começa Hoje** (valor R$ 600)
> Trabalho do bônus: **remove obstáculo** (paralisia de início).
> Objeção que mata: *"não sei por onde começar"*.
> O que é: **um checklist de 1 página + 3 templates prontos de e-mail**.
> Por que tem esse valor: **substitui 4h de consultoria a R$ 150/h**.
> Só para quem agir até **sexta (fim do carrinho real)**: **call de setup em grupo ao vivo**.

O bônus tem nome, papel claro, fala do avatar, formato concreto e lastro. Ele fecha uma objeção específica.

## Liga com
- **Frameworks:** [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) (cada bônus é uma linha da pilha), [`value-equation`](../../frameworks/value-equation.md) (acelera = comprime tempo/esforço), [`magic-naming`](../../frameworks/magic-naming.md) (nome magnético).
- **Taxonomias:** [`offer-types`](../taxonomies/offer-types.md).
- **Componentes:** [`value-stack-block`](value-stack-block.md), [`scarcity-block`](scarcity-block.md) (bônus de ação rápida).
- **Agentes:** `value-equation-engineer` (dono — valida o papel do bônus), `avatar-voc-investigator` (fornece as objeções), `vsl-webinar-scriptwriter` (apresenta os bônus na pilha).
