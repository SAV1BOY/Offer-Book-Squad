---
id: template.strategy.market-brief
title: "Market Brief — Diagnóstico de Mercado (Sofisticação × Consciência)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
consumes: []
produces: [template.core.offer-book-master]
frameworks: [awareness-x-sophistication, starving-crowd]
checklists: [market/market-sophistication-gate, market/market-awareness-gate, market/market-starving-crowd-gate]
registries: [offer-registry]
tags: [template, market, sophistication, awareness, starving-crowd, strategy]
---

# Market Brief — Diagnóstico de Mercado

Este template é o **primeiro diagnóstico** do pipeline, antes de qualquer palavra de copy. Ele responde três perguntas com evidência: quão cansado o mercado está dos claims (sofisticação), quanto o prospect já sabe (consciência), e se existe uma multidão faminta de verdade. Sem este brief verde, o Offer Book não começa.

## Como usar
- **Agente dono:** `market-sophistication-analyst` (camada D1). Co-roda com o `offer-squad-architect`.
- **Task:** `run-market-intel`. Consome a pesquisa de mercado vinda do squad de deepresearch (sizing, intel de concorrentes).
- **Quando:** logo após o intake do Chief. É o input do bloco 1 ("MERCADO") do [`offer-book-master`](../core/offer-book-master.md). Validado por três gates: [`market-sophistication-gate`](../../checklists/market/market-sophistication-gate.md), [`market-awareness-gate`](../../checklists/market/market-awareness-gate.md) e [`market-starving-crowd-gate`](../../checklists/market/market-starving-crowd-gate.md).
- Regra de ouro: **inferir o estágio da evidência, não do palpite**. Toda nota de sofisticação e consciência precisa de uma prova (ad do concorrente, review, anúncio antigo vs novo).

## Campos & Instruções
- **{{MERCADO_NOME}}** — o mercado-alvo em uma frase (nicho + sub-nicho). Quanto mais estreito, melhor o diagnóstico.
- **{{SOFISTICACAO_ESTAGIO}}** — o estágio 1-5 da taxonomia [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md). É o quanto o mercado já ouviu (e cansou) dos claims.
- **{{SOFISTICACAO_EVIDENCIA}}** — a prova do estágio: o que os ads dos concorrentes prometem hoje, se já usam mecanismo, se há fadiga de claim.
- **{{CONSCIENCIA_NIVEL}}** — o nível dominante 1-5 da taxonomia [`awareness-levels`](../../lib/taxonomies/awareness-levels.md). É o quanto o prospect sabe do problema, da solução e do produto.
- **{{CONSCIENCIA_EVIDENCIA}}** — a prova do nível: como o prospect fala (busca? compara categorias? pede o link?), o que a VOC mostra.
- **{{MOVIMENTO_VENCEDOR}}** — o movimento de copy que o cruzamento exige (claim direto, ampliar claim, introduzir mecanismo, elevar mecanismo, identidade), via [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md).
- **{{LEAD_RECOMENDADO}}** — o tipo de [lead](../../lib/taxonomies/lead-types.md) que o nível de consciência pede (recomendação; o `positioning-lead-strategist` trava depois).
- **{{STARVING_CROWD}}** — a multidão faminta: dor intensa + poder de compra + facilidade de alcance, cada um com prova. Via [`starving-crowd`](../../frameworks/starving-crowd.md).
- **{{CONCORRENTES}}** — os 3 concorrentes dominantes e o que cada um promete (o "claim atual do mercado").
- **{{GAP_DE_MERCADO}}** — a brecha que ninguém ocupa (a abertura para o mecanismo único e a Big Idea).
- **{{TAMANHO_E_ALCANCE}}** — o tamanho estimado e por onde se alcança o avatar (canal, custo de alcance).

## O Template
```
# MARKET BRIEF — {{MERCADO_NOME}}
Owner: market-sophistication-analyst · Data: {{DATA}}

## 1. SOFISTICAÇÃO  (taxonomia: sophistication-levels)
Estágio: {{SOFISTICACAO_ESTAGIO}} / 5
Evidência: {{SOFISTICACAO_EVIDENCIA}}
Implicação de copy: {{O_QUE_A_COPY_PRECISA_FAZER}}

## 2. CONSCIÊNCIA  (taxonomia: awareness-levels)
Nível dominante: {{CONSCIENCIA_NIVEL}} / 5
Evidência (VOC/comportamento): {{CONSCIENCIA_EVIDENCIA}}
Onde a copy começa: {{PONTO_DE_PARTIDA}}

## 3. MOVIMENTO VENCEDOR  (matriz awareness × sophistication)
Movimento: {{MOVIMENTO_VENCEDOR}}
Lead recomendado: {{LEAD_RECOMENDADO}}

## 4. MULTIDÃO FAMINTA  (framework: starving-crowd)
Dor intensa: {{PROVA_DA_DOR}}
Poder de compra: {{PROVA_DE_RENDA/ORCAMENTO}}
Facilidade de alcance: {{ONDE_E_QUANTO_CUSTA_ALCANCAR}}
Veredito: {{FAMINTA_SIM/NAO}}

## 5. CONCORRÊNCIA & GAP
Concorrentes dominantes:
  1. {{CONCORRENTE_1}} → promete: {{CLAIM_1}}
  2. {{CONCORRENTE_2}} → promete: {{CLAIM_2}}
  3. {{CONCORRENTE_3}} → promete: {{CLAIM_3}}
Gap de mercado (a brecha): {{GAP_DE_MERCADO}}

## 6. TAMANHO & ALCANCE
Tamanho estimado: {{TAMANHO_E_ALCANCE}}
Canal principal de alcance: {{CANAL}}
```

## Exemplo preenchido
> **# MARKET BRIEF — Recuperação de carrinho para e-commerce PME (R$50k+/mês)**
> Owner: market-sophistication-analyst · Data: 2026-06-02
>
> **1. SOFISTICAÇÃO** — Estágio **3/5**. Evidência: os 3 apps líderes só prometem "recupere vendas abandonadas", sem explicar **como**; nenhum nomeia mecanismo. Mercado cansado da promessa pura. Implicação: a copy precisa **introduzir um mecanismo único**, não só prometer mais.
> **2. CONSCIÊNCIA** — Nível dominante **3/5** (consciente da solução). Evidência: nos grupos, lojistas comparam "app vs agência vs e-mail manual" — sabem que dá para recuperar, não conhecem a abordagem certa. Copy começa provando a superioridade da nossa categoria.
> **3. MOVIMENTO VENCEDOR** — Movimento: **introduzir o mecanismo** (sofisticação 3). Lead recomendado: **Segredo** (casa com consciência 3 + mecanismo novo).
> **4. MULTIDÃO FAMINTA** — Dor: >60% de abandono médio = receita visível escapando. Poder de compra: faturam R$50k+/mês, já gastam em apps. Alcance: concentrados em grupos de e-commerce e no Meta, CPM baixo. Veredito: **faminta sim**.
> **5. CONCORRÊNCIA & GAP** — 1. AppX → "recupere vendas perdidas"; 2. AgênciaY → "a gente cuida do seu e-mail"; 3. Planilha manual → "faça você mesmo". Gap: ninguém nomeia a **janela de tempo** em que a recuperação acontece.
> **6. TAMANHO & ALCANCE** — ~40 mil lojas no Brasil na faixa de receita. Canal principal: Meta + grupos de nicho.

## DoD do entregável
O Market Brief está pronto quando: (1) sofisticação **e** consciência estão declaradas com nota numérica **e** evidência concreta (não palpite) — sem isso, os gates de sofisticação e consciência reprovam; (2) o movimento vencedor e o lead recomendado derivam do cruzamento na matriz, não de preferência; (3) a multidão faminta tem prova nas três dimensões (dor, poder de compra, alcance) e um veredito explícito — sem isso o `market-starving-crowd-gate` reprova; (4) os 3 concorrentes e seus claims estão mapeados e o gap está nomeado; (5) tamanho e canal de alcance estão estimados. Só então o brief alimenta o bloco "MERCADO" do [`offer-book-master`](../core/offer-book-master.md) e libera o `mechanism-architect` para isolar o mecanismo que ocupa o gap.
