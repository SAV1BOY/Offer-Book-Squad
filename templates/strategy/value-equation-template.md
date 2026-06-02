---
id: template.strategy.value-equation
title: "Value Equation Sheet — Pontuação das 4 Alavancas de Valor"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: value-equation-engineer
consumes: [template.strategy.avatar-icp, template.strategy.mechanism-sheet, template.strategy.proof-bank]
produces: [template.core.offer-book-master]
frameworks: [value-equation, value-equation-engineer/dream-outcome-amplification, value-equation-engineer/time-delay-compression, value-equation-engineer/effort-sacrifice-reduction]
checklists: [value/value-no-orphan-lever-gate]
registries: [offer-registry]
tags: [template, value-equation, dream-outcome, levers, scoring, strategy]
---

# Value Equation Sheet — Pontuação das 4 Alavancas de Valor

Este template pontua o valor percebido da oferta pela equação de Hormozi: **(Resultado dos Sonhos × Probabilidade de Sucesso) ÷ (Tempo até o Resultado × Esforço & Sacrifício)**. Valor não é opinião — é uma conta. Você sobe o numerador e derruba o denominador. A régua é dura: **todo componente da oferta precisa mover ao menos uma alavanca**; o que não move, sai. É o teste que o `value-equation-engineer` usa para aprovar ou reprovar cada peça.

## Como usar
- **Agente dono:** `value-equation-engineer` (camada D2, pode **vetar**).
- **Task:** `score-value-equation`. Consome o [`avatar-icp`](avatar-icp-template.md), o [`mechanism-sheet`](mechanism-sheet-template.md) e o [`proof-bank`](proof-bank-template.md).
- **Quando:** depois do mecanismo, antes do preço. Alimenta o bloco 5 ("VALOR") do [`offer-book-master`](../core/offer-book-master.md). Validado pelo [`value-no-orphan-lever-gate`](../../checklists/value/value-no-orphan-lever-gate.md). Usa o framework [`value-equation`](../../frameworks/value-equation.md).
- Regra: a equação é uma **bússola de decisão**, não calculadora de ROI para a copy. Nada de número inflado. Cada componente vira uma linha na tabela de alavancas.

## Campos & Instruções
- **{{RESULTADO_SONHOS}}** — o "antes → depois" na linguagem do avatar (vívido, não categoria). Via [`dream-outcome-amplification`](../../frameworks/value-equation-engineer/dream-outcome-amplification.md). Sobe o numerador.
- **{{PROBABILIDADE}}** — nota 0-10 de quanto o avatar acredita que **vai funcionar para ele**, com o que derruba (ceticismo, tentativas falhas) e o que sustenta (prova, mecanismo, garantia).
- **{{TEMPO}}** — quanto até o **primeiro** resultado (separe do resultado final). Alto = ruim. Via [`time-delay-compression`](../../frameworks/value-equation-engineer/time-delay-compression.md).
- **{{ESFORCO}}** — o que o avatar precisa fazer, largar ou aguentar. Alto = ruim. Via [`effort-sacrifice-reduction`](../../frameworks/value-equation-engineer/effort-sacrifice-reduction.md).
- **{{TABELA_ALAVANCAS}}** — uma linha por componente da oferta, marcando qual das 4 alavancas ele move e em que direção.
- **{{ORFAOS}}** — componentes que não movem **nenhuma** alavanca. No estado final, têm de ser **zero** (corte ou redesenho). Gate `value-no-orphan-lever-gate`.
- **{{ACAO_POR_ALAVANCA}}** — a ação concreta que sobe cada alavanca (não adjetivo — ação: garantia, demo, feito-para-você).
- **{{SCORE_QUALITATIVO}}** — a leitura geral (forte/médio/fraco) e a alavanca mais fraca a reforçar.

## O Template
```
# VALUE EQUATION SHEET — {{NOME_DA_OFERTA}}
Owner: value-equation-engineer · Data: {{DATA}}
Fórmula: (Resultado × Probabilidade) ÷ (Tempo × Esforço)

## 1. NUMERADOR (subir)
Resultado dos Sonhos (verbatim): {{RESULTADO_SONHOS}}
Probabilidade percebida (0-10): {{PROBABILIDADE}}
  Derruba a crença: {{O_QUE_DERRUBA}}
  Sustenta a crença: {{O_QUE_SUSTENTA}}

## 2. DENOMINADOR (descer)
Tempo até o 1º resultado: {{TEMPO}}
Esforço & sacrifício: {{ESFORCO}}

## 3. TABELA DE ALAVANCAS POR COMPONENTE
| Componente | Resultado↑ | Probabilidade↑ | Tempo↓ | Esforço↓ |
|---|---|---|---|---|
| {{COMP_1}} | {{X_OU_-}} | {{X_OU_-}} | {{X_OU_-}} | {{X_OU_-}} |
| {{COMP_2}} | {{X_OU_-}} | {{X_OU_-}} | {{X_OU_-}} | {{X_OU_-}} |
| {{COMP_3}} | {{X_OU_-}} | {{X_OU_-}} | {{X_OU_-}} | {{X_OU_-}} |

## 4. AÇÕES QUE MOVEM CADA ALAVANCA
Resultado ↑ por: {{ACAO_RESULTADO}}
Probabilidade ↑ por: {{ACAO_PROBABILIDADE}}
Tempo ↓ por: {{ACAO_TEMPO}}
Esforço ↓ por: {{ACAO_ESFORCO}}

## 5. ÓRFÃOS & VEREDITO  (gate: value-no-orphan-lever-gate)
Componentes órfãos (movem nada): {{ORFAOS_OU_NENHUM}}
Score qualitativo: {{SCORE_QUALITATIVO}} — alavanca mais fraca: {{ALAVANCA_FRACA}}
```

## Exemplo preenchido
> **# VALUE EQUATION SHEET — Motor de Recuperação 72h**
> Owner: value-equation-engineer · Data: 2026-06-02
>
> **1. NUMERADOR** — Resultado: *"recuperar a receita que escapa no checkout sem gastar mais em ads"*. Probabilidade: **8/10**. Derruba: "já tentei e-mail e não deu". Sustenta: 142 casos + garantia dobro + mecanismo Janela 72h.
> **2. DENOMINADOR** — Tempo até 1º resultado: **7 dias**. Esforço: **quase zero** (setup feito-para-você em 72h).
> **3. TABELA DE ALAVANCAS**
> | Componente | Resultado↑ | Probabilidade↑ | Tempo↓ | Esforço↓ |
> |---|---|---|---|---|
> | Motor 72h (núcleo) | X | X | X | - |
> | Garantia dobro | - | X | - | - |
> | Setup feito-para-você | - | - | X | X |
> | 142 casos / prova | - | X | - | - |
> | Aula de tráfego (bônus) | X | - | - | - |
>
> **4. AÇÕES** — Resultado ↑ por núcleo + bônus de tráfego. Probabilidade ↑ por garantia + prova. Tempo ↓ por setup em 72h. Esforço ↓ por feito-para-você.
> **5. ÓRFÃOS & VEREDITO** — Órfãos: **nenhum** (todo componente move ≥1 alavanca). Score: **forte** — alavanca mais fraca: esforço já está baixo; manter.

## DoD do entregável
O Value Equation Sheet está pronto quando: (1) o Resultado dos Sonhos está em verbatim do avatar, vívido e não-categoria; (2) a probabilidade tem nota **e** o par "o que derruba / o que sustenta" a crença; (3) tempo e esforço estão estimados, com o tempo separando primeiro resultado de resultado final; (4) existe a tabela de alavancas com **uma linha por componente** marcando o que cada um move; (5) cada alavanca tem uma **ação concreta** que a move (não adjetivo); (6) **nenhum** componente fica órfão de alavanca no estado final — todo órfão foi cortado ou redesenhado (gate `value-no-orphan-lever-gate`); (7) há um score qualitativo e a alavanca mais fraca identificada. Só então alimenta o bloco "VALOR" do [`offer-book-master`](../core/offer-book-master.md). O engenheiro de valor **reprova** qualquer componente que não mova uma alavanca, em qualquer camada posterior.
