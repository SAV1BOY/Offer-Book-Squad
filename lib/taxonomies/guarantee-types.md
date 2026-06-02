---
id: taxonomy.guarantee-types
title: "Os 13 Tipos de Garantia (reversão de risco)"
type: taxonomy
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
sources:
  - "Alex Hormozi, *$100M Offers* (2021), seção sobre Garantias"
tags: [guarantee, risk-reversal, offer-stack, conversion]
---

# Os 13 Tipos de Garantia

> **Fonte:** Alex Hormozi, *$100M Offers* (2021), capítulo de Garantias. **Anti-verbatim:** estrutura e princípios em redação original.

A garantia **reverte o risco** do comprador para o vendedor — a alavanca mais barata para subir a conversão sem mexer no preço. Hormozi organiza em **4 categorias**. Use junto do [offer stack](../../frameworks/offer-stack-builder.md) e da [escada de reversão de risco](../../frameworks/risk-reversal-ladder.md). Regra: a garantia precisa ser **real e exequível** — promessa que você não pode honrar é veto do `compliance-auditor`.

| Categoria | Ideia | Tipos |
|---|---|---|
| **Incondicional** | Sem condições | 1. Reembolso sem perguntas |
| **Condicional** | Cliente cumpre algo | 2-11 (abaixo) |
| **Anti-garantia** | "Todas as vendas são finais" | 12. All-sales-final (com motivo) |
| **Implícita** | Pagamento atrelado a resultado | 13. Performance/parceria |

## Incondicional
1. **Reembolso sem perguntas** — devolução total dentro de um prazo, sem justificar. Máxima reversão de risco; exige produto sólido e margem para absorver.

## Condicional (o cliente faz a parte dele)
2. **Garantia ampliada / dobro do dinheiro** — devolve mais que o pago se não funcionar (ancoragem poderosa).
3. **Garantia de serviço** — continuamos trabalhando de graça até você atingir o resultado.
4. **Serviço modificado** — entregamos uma versão alternativa se a primeira não servir.
5. **Crédito** — em vez de dinheiro, crédito para outro produto/serviço.
6. **Serviço pessoal** — atenção 1:1 até o marco combinado.
7. **Extravagante** — "se não funcionar, pago sua passagem + hotel" (prova de confiança extrema).
8. **Pagamento de salário/tempo** — compensamos seu tempo perdido se não entregar.
9. **Liberação de serviço** — você só continua pagando enquanto entregamos valor; pode sair.
10. **Segundo pagamento adiado** — só cobra a 2ª parcela após o primeiro resultado.
11. **Primeiro resultado / "não pagamos até..."** — cobrança só dispara quando o marco é atingido.

## Anti-garantia
12. **Todas as vendas são finais** — sem reembolso, **com um motivo forte e honesto** (ex.: exclusividade, custo de revelação). Filtra curiosos e eleva o compromisso. Use só quando o motivo é verdadeiro.

## Implícita (performance / parceria)
13. **Performance / revenue-share** — você só ganha se o cliente ganhar (% do resultado, equity, comissão). Alinha 100% dos incentivos; exige seleção de cliente.

## Como o squad usa
- `unit-economics-stack-analyst`: escolhe o tipo no [offer stack](../../templates/offer/offer-stack-template.md); o gate `guarantee-checklist` valida que a reversão é **real e exequível**.
- `compliance-auditor`: **veta** garantia que a operação não pode honrar ou que viola regra setorial.
- `vsl-webinar-scriptwriter`: posiciona a garantia **depois** do valor, **antes** do preço (gate `vsl/vsl-risk-reversal-gate`).

**Armadilha:** empilhar uma garantia que parece ótima na copy mas a operação não sustenta — destrói LTV e marca, além de risco legal.
