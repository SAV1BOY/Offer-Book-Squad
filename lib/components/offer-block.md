---
id: lib.component.offer-block
title: "Bloco de Oferta (o quê + para quem + resultado)"
type: component
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
frameworks: [value-equation, offer-stack-builder, unique-mechanism]
tags: [component, offer, dream-outcome, mechanism, reuse]
---

# Bloco de Oferta (o quê + para quem + resultado)

## O que é
O bloco de oferta diz três coisas em uma respirada: **o quê** você entrega, **para quem** é, e **qual resultado** a pessoa leva. É a unidade mínima de uma oferta clara. Sem essas três peças, o leitor não sabe se a oferta é para ele nem por que deveria querer.

Use frases curtas. Use a voz do avatar. Mostre o resultado, não a categoria do produto. "Você acorda sem dor nas costas" vence "programa de mobilidade de 8 semanas". O bloco amarra o [mecanismo único](../../frameworks/unique-mechanism.md) ao [resultado dos sonhos](../../frameworks/value-equation.md): nomeia o caminho **e** o destino. Ele é reutilizável porque o esqueleto não muda — só os campos. A mesma estrutura serve um SaaS, um curso ou um serviço.

## Quando usar
- No topo de uma página de oferta, VSL ou carta — antes de empilhar valor.
- Em um ad, como gancho de uma frase.
- Toda vez que precisa de um "pitch de elevador" da oferta núcleo (ver [`offer-types`](../taxonomies/offer-types.md)).

Não use para a sequência inteira do Money Model. Este bloco descreve **uma** oferta, não a escada. Para a sequência, use os padrões de [`upsell-patterns`](../patterns/upsell-patterns.md) e [`continuity-patterns`](../patterns/continuity-patterns.md).

## Bloco
```
Para {{AVATAR_ESPECÍFICO}} que quer {{RESULTADO_DOS_SONHOS}}
mas trava em {{OBSTÁCULO_PRINCIPAL}},
o {{NOME_DA_OFERTA}} usa {{MECANISMO_ÚNICO}}
para entregar {{RESULTADO_MENSURÁVEL}} em {{PRAZO}},
sem {{SACRIFÍCIO_OU_ESFORÇO_TEMIDO}}.
É para você se {{CRITÉRIO_DE_FIT}}. Não é se {{CRITÉRIO_DE_EXCLUSÃO}}.
```

Cada `{{...}}` é um campo. Preencha com um fato, um número ou a fala literal do cliente. Campo vazio = bloco incompleto. O par fit/exclusão é o que separa um bloco amador de um bloco SOTA: dizer para quem **não** é aumenta a crença de quem é.

## Exemplo preenchido
> Para **donos de e-commerce que faturam R$50 mil/mês** e querem **dobrar o lucro sem aumentar o tráfego**, mas travam em **carrinhos abandonados**, o **Motor de Recuperação 72h** usa **uma sequência de 7 mensagens cronometradas** para entregar **+18% de receita recuperada** em **30 dias**, sem **contratar mais ninguém**. É para você se **já vende todo dia**. Não é se **ainda não tem tráfego pago rodando**.

Note: avatar específico, resultado em número, prazo concreto, mecanismo nomeado, fit e exclusão honestos. O bloco filtra tanto quanto vende.

## Liga com
- **Frameworks:** [`value-equation`](../../frameworks/value-equation.md) (resultado dos sonhos + esforço/sacrifício), [`unique-mechanism`](../../frameworks/unique-mechanism.md) (o "como"), [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) (onde este bloco vira o topo da pilha).
- **Taxonomias:** [`offer-types`](../taxonomies/offer-types.md) (papel da oferta na escada).
- **Agentes:** `value-equation-engineer` (dono — valida que o resultado move uma alavanca), `mechanism-architect` (preenche o mecanismo), `vsl-webinar-scriptwriter` e `ad-creative-factory` (consomem o bloco na abertura da copy).
