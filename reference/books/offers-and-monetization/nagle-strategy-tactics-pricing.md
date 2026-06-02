---
id: reference.book.nagle-strategy-tactics-pricing
title: "The Strategy and Tactics of Pricing — Thomas Nagle"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Thomas T. Nagle, John E. Hogan & Joseph Zale, *The Strategy and Tactics of Pricing: A Guide to Growing More Profitably* (1ª ed. 1987; eds. recentes Routledge), ISBN 978-0-13-610681-4."
tags: [pricing, value-based-pricing, price-value-communication, strategy, nagle]
---

# The Strategy and Tactics of Pricing — Thomas Nagle

## Citação
> **Fonte:** Thomas T. Nagle, John E. Hogan & Joseph Zale, *The Strategy and Tactics of Pricing* (1ª ed. 1987; eds. recentes Routledge), ISBN 978-0-13-610681-4.
> **Anti-verbatim:** princípios em redação original; citação literal ≤25 palavras, atribuída.

## Tese central
Este é o tratado de referência do **preço por valor**. A tese central ataca três formas comuns e perdedoras de precificar: pelo **custo** (some uma margem ao custo), pela **concorrência** (copie o preço do rival) e pela **participação de mercado** (baixe para vender mais). As três entregam o controle do preço para fora. A alternativa é precificar pelo **valor econômico** que o produto cria para o cliente — o quanto ele ganha ou economiza ao usar a sua solução em vez da melhor alternativa. Nagle separa dois conceitos que a maioria confunde: o **valor econômico total** (medível, objetivo) e o **valor percebido** (o que o cliente enxerga). Preço alto sem comunicação de valor falha; por isso, precificar é metade cálculo e metade **comunicação**. O livro também ensina a distinguir custos relevantes (incrementais e evitáveis) dos irrelevantes (afundados), e a gerir a sensibilidade ao preço — porque cortar preço quase nunca compensa em volume o que se perde em margem.

## Frameworks/Modelos

### Value-Based Pricing (Preço Baseado em Valor)
O método central: medir o **valor econômico** (valor de referência da melhor alternativa + valor de diferenciação) e capturar uma fatia dele no preço. Substitui custo e concorrência como base. Operacionalizamos isso em [`../../frameworks/pricing/value-based-pricing.md`](../../frameworks/pricing/value-based-pricing.md), que orienta o `pricing-wtp-strategist`.

### Value Cascade (Cascata Estratégia → Tática)
Preço não é um número solto; desce de uma cascata: **criar** valor → **comunicar** valor → **estabelecer** a estrutura/política de preço → **persuadir** (convencer o cliente do valor) → **precificar** o nível final. Pular um degrau (ex.: definir o número sem comunicar o valor) quebra a captura. Mapeia para a comunicação preço-valor em [`../../frameworks/price-anchoring.md`](../../frameworks/price-anchoring.md).

### Gestão da Sensibilidade ao Preço & Custos Relevantes
Antes de mexer no preço, entenda os **efeitos de sensibilidade** (efeito do valor único, do custo compartilhado, do gasto total, da comparação difícil) e use só **custos incrementais e evitáveis** para decidir margem. Vira disciplina de unit economics no `unit-economics-stack-analyst`. Ver [`../../frameworks/pricing/packaging-good-better-best.md`](../../frameworks/pricing/packaging-good-better-best.md).

## Princípios
- Precifique pelo **valor**, não pelo custo nem pela concorrência; custo é piso, valor é teto.
- Comunique o valor **antes** do preço; preço sem percepção de valor parece caro, com ela parece justo.
- Use só custos **incrementais e evitáveis** na decisão; custos afundados não são relevantes.
- Cortar preço raramente compensa: o volume extra exigido para empatar margem quase sempre é irreal.
- Entenda os drivers de sensibilidade ao preço por segmento; nem todo cliente reage igual.
- Estratégia antes de tática: política e estrutura de preço guiam o número, não o contrário.

## Como o squad usa
- `pricing-wtp-strategist`: deriva a faixa de preço do valor econômico medido e declara o método (`pricing_method_declared`).
- `value-equation-engineer`: liga as alavancas de valor à percepção que justifica o preço premium.
- `unit-economics-stack-analyst`: aplica a disciplina de custos relevantes ao LTV:CAC e à margem por degrau.
- `positioning-lead-strategist`: usa a comunicação preço-valor para enquadrar o produto contra a melhor alternativa.
- `compliance-auditor`: confere que a comunicação de valor não vira claim sem lastro (`claim_backing`).

## Cross-refs
- [`ramanujam-monetizing-innovation.md`](ramanujam-monetizing-innovation.md) — a prática de levantar WTP que alimenta o valor econômico.
- [`hormozi-100m-offers.md`](hormozi-100m-offers.md) — preço premium ancorado como prova de valor.
- [`hormozi-100m-money-models.md`](hormozi-100m-money-models.md) — preço por valor que sustenta o LTV da continuidade.
- [`../persuasion-psychology/ariely-predictably-irrational.md`](../persuasion-psychology/ariely-predictably-irrational.md) — ancoragem e relatividade na percepção de preço.
