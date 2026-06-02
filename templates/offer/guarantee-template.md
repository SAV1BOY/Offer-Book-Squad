---
id: template.offer.guarantee
title: "Garantia — Reversão de Risco Real e Exequível"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: money-model-designer
consumes: [template.strategy.proof-bank, template.strategy.unit-economics, template.strategy.avatar-icp]
produces: [template.offer.offer-stack, template.core.offer-book-master]
frameworks: [guarantee-design, risk-reversal-ladder, offer-stack-builder]
checklists: [guarantee/guarantee-real-and-feasible-gate, compliance/truthful-scarcity-and-claims-gate]
registries: [offer-registry, objection-registry, proof-registry]
tags: [template, guarantee, risk-reversal, conversion, compliance]
---

# Garantia — Reversão de Risco Real e Exequível

A garantia **reverte o risco** do comprador para o vendedor — a alavanca mais barata para subir a conversão sem mexer no preço. Este template escolhe um dos 13 [tipos de garantia](../../lib/taxonomies/guarantee-types.md), escreve a reversão na voz do avatar, e força a confirmação de que a operação **pode honrar**. Regra dura: garantia que a operação não sustenta é veto do `compliance-auditor` (`truthful_scarcity`/claims) e destrói marca e LTV. Usa o componente reutilizável [`guarantee-block`](../../lib/components/guarantee-block.md).

## Como usar
- **Agente dono:** `money-model-designer` desenha; o `unit-economics-stack-analyst` confirma que a margem absorve o acionamento; o `compliance-auditor` valida que é honrável.
- **Task:** `design-guarantee`. Roda no D2 junto do offer stack; a garantia entra na pilha **sem preço**, posicionada **depois do valor e antes do preço** na copy.
- **Quando:** toda oferta núcleo tem garantia. Quanto mais cético o [mercado](../../lib/taxonomies/sophistication-levels.md), mais forte a reversão. Escolha o tipo na [taxonomia](../../lib/taxonomies/guarantee-types.md) (13 tipos, 4 categorias) e empilhe mais de uma com a [escada de reversão de risco](../../frameworks/risk-reversal-ladder.md) se fizer sentido.
- Mapeie a garantia à **objeção dominante** do [`objection-registry`](../../data/registries/objection-registry.md): a melhor garantia mata o medo número 1 ("e se não funcionar comigo?").

## Campos & Instruções
- **{{NOME_GARANTIA}}** — o nome de trabalho da garantia ("Dobro ou Nada", "Resultado ou Não Paga").
- **{{TIPO_TAXONOMIA}}** — um dos 13 [tipos](../../lib/taxonomies/guarantee-types.md), citado pelo nome (ex.: "condicional — dobro do dinheiro"; "incondicional — reembolso sem perguntas"; "implícita — performance").
- **{{RESULTADO_GARANTIDO}}** / **{{PRAZO}}** — o que prometo e em quanto tempo. Específico e mensurável.
- **{{O_QUE_ACONTECE_NO_FAIL}}** — o que o cliente recebe se falhar (reembolso, refazer, crédito, dobro).
- **{{CONDICAO}}** — o que o cliente precisa fazer (justa e simples). Em garantia incondicional, "nada".
- **{{LASTRO_DE_CONFIANCA}}** — o número/prova que torna a promessa crível ([`proof-registry`](../../data/registries/proof-registry.md)).
- **{{OBJECAO_QUE_MATA}}** — a objeção dominante que a garantia derruba.
- **{{OPERACAO_HONRA}}** — sim/não da operação: a margem absorve a taxa de acionamento esperada? Sem "sim", a garantia **não** vai para a copy.
- **{{TAXA_ACIONAMENTO}}** — a taxa de acionamento estimada e a margem que a cobre.

## O Template
```
# GARANTIA — {{NOME_GARANTIA}} ({{TIPO_TAXONOMIA}})

Eu prometo: {{RESULTADO_GARANTIDO}} em {{PRAZO}}.
Se isso não acontecer: {{O_QUE_ACONTECE_NO_FAIL}}.
Você só precisa: {{CONDICAO}}.
Por que eu posso fazer isso: {{LASTRO_DE_CONFIANCA}}.

Objeção que derruba: "{{OBJECAO_QUE_MATA}}"
Posição na copy: depois do valor, antes do preço.

## TRAVA DE SEGURANÇA (operação)
A operação confirma que pode honrar: {{OPERACAO_HONRA}}
Taxa de acionamento estimada: {{TAXA_ACIONAMENTO}} — coberta pela margem? {{SIM/NAO}}
Compliance (truthful-scarcity-and-claims-gate): {{STATUS}}
```

## Exemplo preenchido
> **# GARANTIA — Dobro ou Nada (condicional — dobro do dinheiro)**
>
> Eu prometo: **+15% de receita recuperada** em **60 dias**.
> Se isso não acontecer: **eu devolvo o dobro do que você pagou**.
> Você só precisa: **instalar a sequência e rodar por 60 dias** (a gente mostra como).
> Por que eu posso fazer isso: **142 lojas rodaram e a mediana foi +21%** (proof-registry #PR-031).
>
> Objeção que derruba: *"já tentei e-mail e não funcionou comigo"*.
> Posição na copy: depois do value stack, antes de revelar os R$497.
>
> **TRAVA DE SEGURANÇA** — A operação confirma que pode honrar: **SIM**. Taxa de acionamento estimada: **<4%** — coberta pela margem (oferta de R$497 com custo marginal baixo)? **SIM**. Compliance: **VERDE**.

A condição é justa, o lastro é um número real (mediana, não cereja), a operação assinou embaixo e a garantia mata a objeção número 1. Reversão forte e honesta.

## DoD do entregável
A garantia está pronta quando: (1) o tipo cita um dos 13 [tipos da taxonomia](../../lib/taxonomies/guarantee-types.md) pelo nome; (2) promessa, prazo, o-que-acontece-no-fail e condição estão escritos, claros e justos; (3) existe **lastro de confiança** rastreável no [`proof-registry`](../../data/registries/proof-registry.md) e o resultado garantido não excede o que a prova sustenta; (4) a garantia mapeia uma **objeção dominante** do [`objection-registry`](../../data/registries/objection-registry.md); (5) a operação confirma por escrito que **pode honrar** e a margem absorve a taxa de acionamento estimada (`guarantee-real-and-feasible-gate` verde); (6) o `compliance-auditor` aprova (sem promessa que a operação não sustenta — `truthful-scarcity-and-claims-gate` verde); (7) a posição na copy é "depois do valor, antes do preço"; (8) a garantia entra sem preço na pilha do [`offer-stack`](offer-stack-template.md) e preenche `garantia_tipo` na planilha [`products-and-offers`](products-and-offers-template.csv). Nenhum `{{PLACEHOLDER}}` solto.
