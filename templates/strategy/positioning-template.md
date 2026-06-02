---
id: template.strategy.positioning
title: "Positioning Sheet — Dunford 5 Componentes + Frase de Moore + Lead"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
consumes: [template.strategy.big-idea, template.strategy.mechanism-sheet, template.strategy.proof-bank, template.strategy.market-brief]
produces: [template.core.offer-book-master]
frameworks: [positioning.dunford-positioning, positioning.moore-positioning-formula, positioning.category-design, positioning.jtbd, awareness-x-sophistication, power-of-one]
checklists: [positioning-checklist, big-idea/big-idea-awareness-fit-gate]
registries: [decision-registry, claim-registry]
tags: [template, positioning, dunford, moore, lead, category, strategy]
---

# Positioning Sheet — Dunford 5 Componentes + Frase de Moore + Lead

Esta planilha fixa **o contexto** que faz o cliente entender, em segundos, o que a oferta é e por que importa. A pergunta-chave não é "o que isto é?", mas "**comparado a quê?**". Você preenche os **5 componentes de Dunford** ([`dunford-positioning`](../../frameworks/positioning/dunford-positioning.md): alternativas → atributos únicos → valor com prova → mercado-alvo → categoria), destila numa frase com a **fórmula de Moore** ([`moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md)) e escolhe o **lead** (a porta de entrada da copy: oferta, promessa, problema, segredo, proclamação ou história — ver [`lead-types`](../../lib/taxonomies/lead-types.md)) coerente com a célula de consciência. É o último artefato de estratégia antes do HARD STOP do Offer Book. É como o `positioning-lead-strategist` torna a posição concreta e auditável.

## Como usar
- **Agente dono:** `positioning-lead-strategist` (camada D3). Recebe a tese do `big-idea-architect`; "valor com prova" abastecido pelo `proof-credibility-curator`; "diferente de" vem do `mechanism-architect`; lastro checado pelo `compliance-auditor` (pode vetar).
- **Task:** `lock-positioning-lead`. Consome a [`big-idea`](big-idea-template.md), o [`mechanism-sheet`](mechanism-sheet-template.md), o [`proof-bank`](proof-bank-template.md) e o [`market-brief`](market-brief-template.md) (a célula de consciência × sofisticação).
- **Quando:** depois da Big Idea, fecha a camada D3. Alimenta o bloco de posição do [`offer-book-master`](../core/offer-book-master.md) — e o Offer Book completo libera a copy (HARD STOP, ver [`ARCHITECTURE.md`](../../ARCHITECTURE.md) §1).
- Regra: os 5 componentes são uma **cadeia ligada** — pular um (valor sem prova) quebra tudo. Atributo sem valor é ruído; valor sem prova é claim vazio (veto). A frase de Moore é **interna** (alinhamento), não headline literal. O lead casa com o nível de consciência.

## Campos & Instruções
- **{{ALTERNATIVAS}}** — o que o cliente usaria se você não existisse (concorrentes, status quo, planilha, "não fazer nada"). Define o ponto de comparação; tudo é relativo a ele.
- **{{ATRIBUTOS_UNICOS}}** — as capacidades que **só você** tem vs. essas alternativas. Puxe do mecanismo único. Atributo que o concorrente também tem não posiciona.
- **{{VALOR_COM_PROVA}}** — para cada atributo, o "e daí?" (o benefício concreto) **com a prova anexada**. Sem prova = veto de compliance.
- **{{MERCADO_ALVO}}** — quem se importa **muito** com esse valor, a ponto de comprar rápido (o beachhead estreito). Não tente agradar todos.
- **{{CATEGORIA}}** — o frame que faz o valor parecer **óbvio** ([`category-design`](../../frameworks/positioning/category-design.md)). A categoria é a alavanca mais forte e mais ignorada.
- **{{TENDENCIA}}** — (opcional) uma onda atual que torna a oferta oportuna. Use com cuidado: tendência demais soa oportunista.
- **{{FRASE_MOORE}}** — "Para [cliente-alvo] que [necessidade], o nosso [categoria] é [benefício-chave]. Diferente de [alternativa], nós [diferenciação]." Se não cabe na frase, a posição está vaga.
- **{{LEAD}}** — o tipo de lead escolhido ([`lead-types`](../../lib/taxonomies/lead-types.md)) e por que casa com a célula de consciência (público frio pede lead de problema/história; quente pede lead de oferta).

## O Template
```
# POSITIONING SHEET — {{NOME_DA_OFERTA}}
Owner: positioning-lead-strategist · Data: {{DATA}}
Pergunta-mestre: "comparado a quê?"

## 1. OS 5 COMPONENTES (Dunford) — cadeia ligada
[1] Alternativas competitivas: {{ALTERNATIVAS}}
[2] Atributos únicos (só você): {{ATRIBUTOS_UNICOS}}
[3] Valor + PROVA: {{VALOR_COM_PROVA}}
[4] Mercado-alvo (beachhead): {{MERCADO_ALVO}}
[5] Categoria de mercado: {{CATEGORIA}}
(+1) Tendência relevante (opcional): {{TENDENCIA}}

## 2. CHECK DE COERÊNCIA
O atributo único entrega o valor? {{SIM/NAO}}
O mercado-alvo quer esse valor? {{SIM/NAO}}
A categoria deixa o valor óbvio? {{SIM/NAO}}

## 3. A POSIÇÃO EM UMA FRASE (Moore — interna)
{{FRASE_MOORE}}

## 4. O LEAD DA COPY
Tipo de lead: {{LEAD}}
Por que casa com a célula de consciência: {{JUSTIFICATIVA_LEAD}}

## 5. GATES
Posição auditável (positioning-checklist): {{STATUS_POSICAO}}
Fit com a consciência (big-idea-awareness-fit-gate): {{STATUS_FIT}}
```

## Exemplo preenchido
> **# POSITIONING SHEET — Aprovado em Inglês (curso para devs)**
> Owner: positioning-lead-strategist · Data: 2026-06-02
>
> **1. OS 5 COMPONENTES** —
> [1] Alternativas: apps de idioma genéricos, escola de inglês tradicional, estudar sozinho no YouTube, não fazer nada.
> [2] Atributos únicos: método de Shadowing focado em **entrevista técnica**; simulação 1:1 com recrutador real; banco de vocabulário por stack.
> [3] Valor + prova: "aprovado na entrevista em inglês e na vaga remota" — 37 alunos contratados por empresas internacionais em 2025 (proof-registry).
> [4] Mercado-alvo: dev pleno/sênior brasileiro mirando vaga remota internacional, que trava na call em inglês.
> [5] Categoria: não "curso de inglês", mas **"preparação para entrevista técnica em inglês"** — tira do balaio dos apps e torna o método óbvio.
> (+1) Tendência: explosão de vagas remotas internacionais pagas em dólar.
> **2. COERÊNCIA** — Atributo entrega o valor? Sim. Mercado quer? Sim. Categoria deixa óbvio? Sim.
> **3. FRASE (Moore, interna)** — "Para o dev brasileiro que trava na entrevista em inglês da vaga remota, a Aprovado em Inglês é a preparação de entrevista técnica em inglês que te aprova em 60 dias. Diferente de apps genéricos, treinamos a call técnica real com recrutador 1:1."
> **4. O LEAD** — Lead de **problema** ("você lê tudo em inglês mas trava na call"). Casa com a célula 2×4: público consciente do problema, cético com soluções, frio para oferta direta — entra pela dor, não pelo preço.
> **5. GATES** — Posição auditável: **VERDE**. Fit com a consciência: **VERDE**.

## DoD do entregável
A Positioning Sheet está pronta quando: (1) os **5 componentes** de Dunford estão preenchidos como uma cadeia ligada (alternativas → atributos → valor+prova → mercado → categoria), nenhum pulado; (2) os atributos vêm do mecanismo único e são de fato **únicos** vs. as alternativas; (3) cada valor traz **prova** anexada (atributo sem valor é ruído; valor sem prova é veto de compliance); (4) o mercado-alvo é um beachhead **estreito** (não "todos"); (5) a categoria escolhida torna o valor óbvio, com justificativa (não a categoria default); (6) o check de coerência passa (o atributo entrega o valor, o mercado quer o valor, a categoria deixa óbvio); (7) a **frase de Moore** está preenchida e cabe em uma frase clara — incluindo o "diferente de" (se não há diferenciação, conserte o mecanismo, não maquie); (8) o **lead** está escolhido e justificado contra a célula de consciência × sofisticação do [`market-brief`](market-brief-template.md) (`big-idea-awareness-fit-gate`); (9) a posição é auditável (`positioning-checklist`) e está registrada no [`decision-registry`](../../data/registries/decision-registry.md), com os claims de valor no [`claim-registry`](../../data/registries/claim-registry.md). Só então a posição fecha a D3, alimenta o [`offer-book-master`](../core/offer-book-master.md) e o Offer Book completo libera a copy (HARD STOP).
