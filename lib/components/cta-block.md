---
id: lib.component.cta-block
title: "Bloco de CTA (uma ação, sem fricção, com motivo)"
type: component
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [offer-to-funnel-mapping, scarcity-urgency-engine, value-equation]
tags: [component, cta, conversion, single-action, reuse]
---

# Bloco de CTA (uma ação, sem fricção, com motivo)

## O que é
O CTA (chamada para ação) diz ao leitor **exatamente o que fazer agora** — uma ação, não três. Um bom CTA é específico ("clique e garanta sua vaga"), tira a fricção (mostra que é simples e seguro), e dá um motivo para agir já (o limite verdadeiro). CTA fraco ou ambíguo é onde a conversão vaza.

A regra de ouro: **um CTA, uma ação**. Dar duas opções divide a atenção e baixa a taxa. Este bloco amarra a ação ao [próximo passo do funil](../../frameworks/offer-to-funnel-mapping.md) e ao [bloco de escassez](scarcity-block.md). É reutilizável: o esqueleto serve para botão de página, fim de VSL, último e-mail da sequência ou card de ad — só muda o verbo e o destino.

## Quando usar
- No fim de toda peça que pede uma ação (página, VSL, e-mail, ad).
- Repetido em pontos-chave de uma página longa — sempre a **mesma** ação.
- Logo depois da garantia e da escassez, quando o medo já caiu e a urgência subiu.

Não termine uma peça de venda sem CTA. E não ofereça duas ações concorrentes ("compre OU agende") no mesmo ponto.

## Bloco
```
AÇÃO ÚNICA: {{VERBO_+_OBJETO}} ({{ex.: "Garanta sua vaga"}})
O QUE ACONTECE AO CLICAR: {{PRÓXIMO_PASSO_CONCRETO_DO_FUNIL}}
POR QUE AGORA: {{MOTIVO_VERDADEIRO — link p/ scarcity-block}}
SEM FRICÇÃO: {{prova de simples/seguro — ex.: "2 min, garantia de 60 dias"}}
REFORÇO DE VALOR: {{o resultado que ele leva, em 1 linha}}
[BOTÃO/LINK]: {{TEXTO_DO_BOTÃO}}
```

Preencha cada `{{...}}`. O campo "AÇÃO ÚNICA" é literal — se houver mais de um verbo concorrendo, escolha um.

## Exemplo preenchido
> AÇÃO ÚNICA: **Garanta sua vaga no Motor de Recuperação 72h**.
> O QUE ACONTECE AO CLICAR: **vai para o checkout de 2 campos; acesso liberado na hora**.
> POR QUE AGORA: **só 40 vagas nesta turma; o carrinho fecha sexta** (escassez real).
> SEM FRICÇÃO: **leva 2 minutos e você tem 60 dias de garantia dobro ou nada**.
> REFORÇO DE VALOR: **comece a recuperar receita perdida já na primeira semana**.
> [BOTÃO]: **QUERO MINHA VAGA AGORA →**

Uma ação, próximo passo claro, motivo verdadeiro, fricção removida e valor reforçado. O leitor sabe o que fazer e por quê.

## Liga com
- **Frameworks:** [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) (o CTA aponta para o próximo passo do funil), [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) (o "por que agora"), [`value-equation`](../../frameworks/value-equation.md) (reforço de valor).
- **Componentes:** [`scarcity-block`](scarcity-block.md), [`guarantee-block`](guarantee-block.md) (precedem o CTA).
- **Agentes:** `vsl-webinar-scriptwriter` (dono — escreve o CTA na copy), `funnel-architect` (define o próximo passo), `email-sms-sequence-writer` (CTA por e-mail), `voice-style-guardian` (valida clareza e voz).
