---
id: template.strategy.mechanism-sheet
title: "Mechanism Sheet — A Folha do Mecanismo Único"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
consumes: [template.strategy.market-brief, template.strategy.avatar-icp, template.strategy.proof-bank]
produces: [template.core.offer-book-master]
frameworks: [unique-mechanism, value-equation]
checklists: [mechanism/mechanism-naming-gate, mechanism/mechanism-proof-gate, mechanism/mechanism-one-sentence-gate]
registries: [offer-registry]
tags: [template, mechanism, unique-mechanism, naming, strategy]
---

# Mechanism Sheet — A Folha do Mecanismo Único

Este template isola e nomeia o **mecanismo único**: a explicação de **por que** a oferta funciona quando tudo o que o avatar já tentou falhou. Em mercado sofisticação 3-4, é o que separa "mais uma promessa" de "uma razão nova para acreditar". O mecanismo não é o produto — é o princípio que faz o produto entregar. Sem ele nomeado, a oferta é genérica e invisível no mercado maduro.

## Como usar
- **Agente dono:** `mechanism-architect` (camada D2).
- **Task:** `define-mechanism`. Consome o [`market-brief`](market-brief-template.md) (sofisticação/gap), o [`avatar-icp`](avatar-icp-template.md) (tentativas falhas) e o [`proof-bank`](proof-bank-template.md).
- **Quando:** primeira peça da arquitetura de oferta, depois da inteligência. Alimenta o bloco 3 ("MECANISMO") do [`offer-book-master`](../core/offer-book-master.md). Validado por três gates: [`mechanism-naming-gate`](../../checklists/mechanism/mechanism-naming-gate.md), [`mechanism-proof-gate`](../../checklists/mechanism/mechanism-proof-gate.md) e [`mechanism-one-sentence-gate`](../../checklists/mechanism/mechanism-one-sentence-gate.md).
- Regra: o mecanismo precisa de **nome próprio**, caber em **uma frase**, e ter **prova**. Use o framework [`unique-mechanism`](../../frameworks/unique-mechanism.md).

## Campos & Instruções
- **{{MECANISMO_NOME}}** — o nome próprio e magnético do mecanismo (o "como" virou marca). Ex.: "Janela 72h". Gate `mechanism-naming-gate`.
- **{{MECANISMO_UMA_FRASE}}** — o mecanismo em **uma** frase: o princípio que explica por que funciona quando o resto falhou. Gate `mechanism-one-sentence-gate`.
- **{{PORQUE_OUTROS_FALHAM}}** — o motivo real pelo qual as tentativas anteriores do avatar não funcionaram (o "inimigo" do mecanismo). Vem da VOC.
- **{{INSIGHT_CENTRAL}}** — a descoberta/princípio que ninguém no mercado nomeia (o gap do [`market-brief`](market-brief-template.md)).
- **{{COMO_FUNCIONA}}** — os 3-4 passos concretos de como o mecanismo opera (a engrenagem por dentro).
- **{{PROVA_DO_MECANISMO}}** — a evidência de que o mecanismo é real (não só a oferta) — dado, demonstração, lógica defensável. Liga ao [`proof-bank`](proof-bank-template.md). Gate `mechanism-proof-gate`.
- **{{ALAVANCAS_VALOR}}** — quais alavancas da [`value-equation`](../../frameworks/value-equation.md) o mecanismo move (sobe probabilidade? reduz tempo? reduz esforço?).
- **{{FIT_SOFISTICACAO}}** — por que este mecanismo encaixa no estágio de sofisticação do mercado (introduz vs eleva).
- **{{NOME_DESCARTADOS}}** — 1-2 nomes considerados e por que o escolhido vence (clareza > esperteza).

## O Template
```
# MECHANISM SHEET — {{NOME_DA_OFERTA}}
Owner: mechanism-architect · Data: {{DATA}}

## 1. O MECANISMO  (framework: unique-mechanism)
Nome: {{MECANISMO_NOME}}
Em uma frase: {{MECANISMO_UMA_FRASE}}

## 2. POR QUE O RESTO FALHA
O que o avatar já tentou e não deu certo: {{TENTATIVAS_FALHAS}}
O motivo real da falha (o inimigo): {{PORQUE_OUTROS_FALHAM}}

## 3. O INSIGHT
A descoberta que ninguém nomeia: {{INSIGHT_CENTRAL}}
Como funciona (engrenagem):
  1. {{PASSO_1}}
  2. {{PASSO_2}}
  3. {{PASSO_3}}

## 4. PROVA DO MECANISMO  (liga: proof-bank · gate: mechanism-proof-gate)
Evidência de que é real: {{PROVA_DO_MECANISMO}}
Rastro: {{FONTE_PROOF_REGISTRY}}

## 5. VALOR & FIT  (framework: value-equation)
Alavancas que move: {{ALAVANCAS_VALOR}}
Fit com a sofisticação ({{ESTAGIO}}): {{FIT_SOFISTICACAO}}

## 6. NOMES DESCARTADOS
{{NOME_DESCARTADOS}} → escolhido por: {{RAZAO}}
```

## Exemplo preenchido
> **# MECHANISM SHEET — Motor de Recuperação 72h**
> Owner: mechanism-architect · Data: 2026-06-02
>
> **1. O MECANISMO** — Nome: **Janela 72h**. Em uma frase: **as primeiras 72 horas após o abandono concentram 80% da receita recuperável, e uma sequência cronometrada para essa janela captura o que o e-mail genérico perde.**
> **2. POR QUE O RESTO FALHA** — Tentativas: e-mail único no dia seguinte, ou app que dispara torto. Inimigo real: **mensagem fora de hora — o e-mail chega quando a intenção de compra já esfriou**.
> **3. O INSIGHT** — Ninguém no mercado nomeia a **janela de tempo**: prometem "recuperar", mas ignoram **quando**. Engrenagem: 1. dispara em minutos, não dias; 2. cadência cresce em 3 toques dentro de 72h; 3. cada toque ataca uma objeção diferente.
> **4. PROVA DO MECANISMO** — Dado de 142 lojas: 80% da receita recuperada cai nas primeiras 72h; sequências fora dessa janela rendem 1/3. Rastro: proof-registry #PR-031.
> **5. VALOR & FIT** — Move: **probabilidade ↑** (timing certo = crença "vai funcionar") e **tempo ↓** (resultado em dias). Fit com sofisticação **3**: o mercado cansou de "recupere vendas" — a janela **introduz** um mecanismo onde só havia promessa.
> **6. NOMES DESCARTADOS** — "Sequência Inteligente" (vago), "Recuperador Pro" (genérico) → escolhido "Janela 72h" por **nomear o insight** e ser concreto.

## DoD do entregável
O Mechanism Sheet está pronto quando: (1) o mecanismo tem **nome próprio** magnético e concreto (gate `mechanism-naming-gate`); (2) cabe em **uma** frase que explica por que funciona quando o resto falhou (gate `mechanism-one-sentence-gate`); (3) o motivo real da falha das alternativas (o inimigo) está nomeado a partir da VOC; (4) o insight central ocupa o gap do [`market-brief`](market-brief-template.md) — algo que nenhum concorrente nomeia; (5) há prova de que o mecanismo é **real**, não só a oferta repintada, com rastro no [`proof-bank`](proof-bank-template.md) (gate `mechanism-proof-gate`); (6) está claro quais alavancas da [`value-equation`](../../frameworks/value-equation.md) ele move e por que encaixa na sofisticação diagnosticada. Só então alimenta o bloco "MECANISMO" do [`offer-book-master`](../core/offer-book-master.md) e vira a espinha da Big Idea e da copy de D4.
