---
id: lib.component.scarcity-block
title: "Bloco de Escassez & Urgência (100% verdadeira)"
type: component
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [scarcity-urgency-engine, offer-stack-builder]
tags: [component, scarcity, urgency, truthful, compliance, reuse]
---

# Bloco de Escassez & Urgência (100% verdadeira)

## O que é
A escassez (quantidade limitada) e a urgência (tempo limitado) empurram a decisão **agora** em vez de "depois" — e "depois" quase sempre vira "nunca". Mas só funcionam, e só são legais, quando são **reais**. Escassez falsa é veto automático do `compliance-auditor` (princípio `truthful_scarcity`) e queima a confiança para sempre.

Este bloco força você a declarar o **motivo verdadeiro** do limite antes de usá-lo. Se você não consegue nomear um motivo honesto, não há escassez — há manipulação. É reutilizável: o esqueleto vale para vagas, prazo, bônus que expira ou preço que sobe, sempre exigindo a prova do limite. Ver a taxonomia de mecanismos no [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md).

## Quando usar
- No fim da oferta, perto do [CTA](cta-block.md), depois que o valor já foi construído.
- Em fechamento de carrinho, lote que esgota, turma com vagas limitadas, bônus de ação rápida.
- Sempre que o limite for **operacionalmente real** (capacidade, data de evento, estoque, cronograma).

Nunca use contador falso, "últimas vagas" perpétuo, ou "preço sobe hoje" que nunca sobe. Isso é fraude e veto.

## Bloco
```
TIPO: {{ESCASSEZ_QUANTIDADE | URGÊNCIA_TEMPO | BÔNUS_EXPIRA | PREÇO_SOBE}}
O limite: {{NÚMERO_OU_DATA_EXATA}}
Motivo VERDADEIRO do limite: {{POR_QUE_É_REAL}}
O que acontece quando bate o limite: {{CONSEQUÊNCIA_CONCRETA_E_REAL}}
Prova do limite: {{COMO_O_CLIENTE_VERIFICA}}

(Compliance confirma que o limite é real: {{SIM/NÃO}} — owner: compliance-auditor)
```

Preencha cada `{{...}}`. Sem o "sim" do compliance e sem motivo verdadeiro, o bloco não entra na copy.

## Exemplo preenchido
> TIPO: **ESCASSEZ_QUANTIDADE**
> O limite: **40 vagas nesta turma**.
> Motivo verdadeiro: **cada aluno recebe revisão 1:1 e eu reviso no máximo 40 por mês**.
> O que acontece ao bater 40: **o carrinho fecha e a próxima turma só abre em 90 dias**.
> Prova do limite: **contador de vagas restantes atualizado em tempo real na página**.
> (Compliance confirma que o limite é real: **SIM** — capacidade de revisão documentada.)

O limite tem número exato, motivo honesto (capacidade real de mentoria), consequência verdadeira e prova. Escassez que aguenta auditoria.

## Liga com
- **Frameworks:** [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) (os mecanismos verdadeiros de escassez/urgência), [`offer-stack-builder`](../../frameworks/offer-stack-builder.md).
- **Componentes:** [`cta-block`](cta-block.md) (a escassez precede o CTA), [`bonus-block`](bonus-block.md) (bônus de ação rápida).
- **Agentes:** `unit-economics-stack-analyst` (dono — define o limite operacional), `compliance-auditor` (**veta** escassez falsa), `vsl-webinar-scriptwriter` e `email-sms-sequence-writer` (aplicam no fechamento).
