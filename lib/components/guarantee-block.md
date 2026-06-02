---
id: lib.component.guarantee-block
title: "Bloco de Garantia (reversão de risco)"
type: component
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [guarantee-design, risk-reversal-ladder, offer-stack-builder]
tags: [component, guarantee, risk-reversal, conversion, reuse]
---

# Bloco de Garantia (reversão de risco)

## O que é
O bloco de garantia tira o risco das costas do cliente e põe nas suas. Diz, em poucas palavras: o que prometo, o que acontece se eu falhar, e o que o cliente faz para acionar. É a alavanca mais barata para subir a conversão sem mexer no preço.

Escolha o tipo de garantia na taxonomia [`guarantee-types`](../taxonomies/guarantee-types.md) — são 13, em 4 categorias. A regra de ouro: a garantia precisa ser **real e exequível**. Promessa que a operação não honra é veto do `compliance-auditor` e destrói a marca. O bloco é reutilizável porque qualquer um dos 13 tipos encaixa no mesmo esqueleto — só o nome e a condição mudam.

## Quando usar
- Depois do valor, **antes** do preço — é onde derruba a última muralha de medo.
- Em toda oferta núcleo. Quanto mais cético o mercado, mais forte a reversão.
- Junto da [escada de reversão de risco](../../frameworks/risk-reversal-ladder.md) quando você empilha mais de uma garantia.

Cuidado: uma anti-garantia ("todas as vendas são finais") só entra com um motivo forte e honesto.

## Bloco
```
{{NOME_DA_GARANTIA}} ({{TIPO_DA_TAXONOMIA}})

Eu prometo: {{RESULTADO_GARANTIDO}} em {{PRAZO}}.
Se isso não acontecer: {{O_QUE_VOCÊ_FAZ}} — {{REEMBOLSO/REFAZER/CRÉDITO}}.
Você só precisa: {{CONDIÇÃO_JUSTA_E_SIMPLES}}.
Por que eu posso fazer isso: {{LASTRO_DE_CONFIANÇA}}.

(Operação confirma que pode honrar: {{SIM/NÃO}} — owner: unit-economics-stack-analyst)
```

Preencha cada `{{...}}`. O último campo é o trava-segurança: sem o "sim" da operação, o bloco não vai para a copy. O campo `{{TIPO_DA_TAXONOMIA}}` deve citar um dos 13 tipos pelo nome.

## Exemplo preenchido
> **Garantia Dobro ou Nada** (condicional — dobro do dinheiro)
> Eu prometo: **+15% de receita recuperada** em **60 dias**.
> Se isso não acontecer: **eu devolvo o dobro do que você pagou**.
> Você só precisa: **instalar a sequência e rodar por 60 dias** (a gente mostra como).
> Por que eu posso fazer isso: **142 lojas rodaram e a média foi +21%** (ver proof-registry).
> (Operação confirma que pode honrar: **SIM** — margem absorve até 4% de acionamento.)

A condição é justa, o lastro é um número real, e a operação assinou embaixo. Reversão forte e honesta.

## Liga com
- **Frameworks:** [`guarantee-design`](../../frameworks/guarantee-design.md) (como desenhar), [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md) (empilhar reversões), [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) (a garantia na pilha).
- **Taxonomias:** [`guarantee-types`](../taxonomies/guarantee-types.md) (os 13 tipos — escolha aqui).
- **Agentes:** `unit-economics-stack-analyst` (dono — escolhe o tipo e confirma exequibilidade), `compliance-auditor` (veta garantia insustentável), `vsl-webinar-scriptwriter` (posiciona depois do valor, antes do preço).
