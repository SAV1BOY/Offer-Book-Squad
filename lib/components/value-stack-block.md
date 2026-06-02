---
id: lib.component.value-stack-block
title: "Bloco de Pilha de Valor (value stack)"
type: component
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [offer-stack-builder, value-equation, magic-naming]
tags: [component, value-stack, offer, anchoring, reuse]
---

# Bloco de Pilha de Valor (value stack)

## O que é
A pilha de valor lista cada item que o cliente recebe, dá um **nome** a cada um, atribui um **valor** a cada um, e soma tudo. No fim, mostra o **preço real** muito abaixo da soma. O objetivo: o cérebro do cliente sente que paga pouco por muito.

Cada linha tem três partes: nome magnético, o que resolve, e o valor ancorado. O valor de cada item deve ser defensável — um preço que aquele item teria sozinho no mercado, o custo de fazer sozinho, ou o custo de não resolver. Valor inflado e falso quebra a confiança e vira risco de compliance. O bloco é reutilizável: o esqueleto da tabela é fixo, só os itens e números mudam por oferta.

## Quando usar
- Logo depois do [bloco de oferta](offer-block.md), na página ou VSL.
- Quando a oferta tem 3+ componentes e você precisa fazer o todo parecer maior que a soma.
- Antes de revelar o preço — a pilha é o âncora alto contra o qual o preço parece pequeno.

Não use para uma oferta de um item só. Sem múltiplas partes, não há pilha. Para uma oferta avulsa, fique no [`offer-block`](offer-block.md) + [`cta-block`](cta-block.md).

## Bloco
```
{{NOME_OFERTA_NÚCLEO}} — resolve {{DOR}} ............ valor R$ {{VALOR_1}}
{{NOME_BÔNUS_1}} — resolve {{DOR}} ................... valor R$ {{VALOR_2}}
{{NOME_BÔNUS_2}} — resolve {{DOR}} ................... valor R$ {{VALOR_3}}
{{NOME_FERRAMENTA}} — resolve {{DOR}} ................ valor R$ {{VALOR_4}}
{{NOME_GARANTIA}} — remove o risco ................. (sem preço)
---------------------------------------------------
VALOR TOTAL .......................................... R$ {{SOMA}}
HOJE VOCÊ INVESTE .................................... R$ {{PREÇO_REAL}}
VOCÊ ECONOMIZA ....................................... R$ {{ECONOMIA}} ({{%}})
```

Preencha cada `{{...}}`. O valor de cada item precisa de uma justificativa por trás. Anote a justificativa de cada linha numa nota lateral — o `compliance-auditor` pode pedir o lastro.

## Exemplo preenchido
> **Método Lucro 2x** — o passo a passo para dobrar o lucro ... valor R$ 2.000
> **Planilha de Recuperação Automática** — recupera carrinhos ... valor R$ 600
> **10 Modelos de E-mail Prontos** — você só copia e cola ... valor R$ 400
> **Aula de Tráfego que Liquida o CAC** — paga a aquisição ... valor R$ 800
> **Garantia Dobro do Dinheiro** — risco zero ... (sem preço)
> **VALOR TOTAL: R$ 3.800 — HOJE: R$ 497 — VOCÊ ECONOMIZA R$ 3.303 (87%)**

Cada item tem nome próprio, resolve uma dor nomeada, e tem valor com lastro. A soma alta torna R$ 497 quase trivial.

## Liga com
- **Frameworks:** [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) (a pilha é a saída direta deste framework), [`value-equation`](../../frameworks/value-equation.md) (cada item deve mover uma alavanca), [`magic-naming`](../../frameworks/magic-naming.md) (nomes magnéticos por linha).
- **Taxonomias:** [`offer-types`](../taxonomies/offer-types.md), [`guarantee-types`](../taxonomies/guarantee-types.md) (a linha da garantia).
- **Agentes:** `unit-economics-stack-analyst` (dono — monta e valida o lastro do valor), `value-equation-engineer` (reprova item que não move alavanca), `vsl-webinar-scriptwriter` (apresenta a pilha antes do preço).
