---
id: framework.pricing.value-based-pricing
title: "Value-Based Pricing — Preço pelo Valor Econômico"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [van-westendorp, gabor-granger, conjoint-cbc, price-elasticity, packaging-good-better-best, perceived-value-stack]
sources:
  - "Thomas T. Nagle, John E. Hogan & Joseph Zale, *The Strategy and Tactics of Pricing* (Routledge)."
  - "Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (Wiley, 2016)."
tags: [pricing, value-based, economic-value, eva, willingness-to-pay, value-communication]
---

# Value-Based Pricing — Preço pelo Valor Econômico

## TL;DR
Preço por valor não parte do custo nem do concorrente. Parte do **valor econômico** que o produto cria para o cliente: quanto ele ganha ou economiza ao usar você em vez da melhor alternativa. O preço é o **valor de referência** (o que a alternativa custa) **mais** o **valor de diferenciação** (o que você entrega a mais), menos a fatia que você deixa com o cliente como incentivo. Custo é só o piso; valor é o teto. E preço sem **comunicação de valor** parece caro. Este é o princípio mestre do `pricing-wtp-strategist`: preço deriva de valor, sempre.

## Quando usar / Quando não
**Use** sempre como a **espinha** da decisão de preço — antes e acima de qualquer método de WTP. Os outros frameworks de pricing medem percepção e demanda; este define a **lógica** de onde o preço vem.
**Use mais** quando seu diferencial é real e mensurável (economiza tempo, gera receita, evita custo) e o cliente tem uma alternativa clara para ancorar.
**Não use** o custo como base — custo entra só como **piso de margem** ([`../../reference/books/offers-and-monetization/nagle-strategy-tactics-pricing.md`](../../reference/books/offers-and-monetization/nagle-strategy-tactics-pricing.md)).
**Não use** sem comunicar o valor: valor econômico que o cliente não enxerga não sustenta preço. Pareie com [`perceived-value-stack.md`](../positioning/perceived-value-stack.md) e [`price-anchoring.md`](../price-anchoring.md).

## Inputs
- A **melhor alternativa** do cliente (concorrente, status quo, "fazer à mão", planilha) e o que ela custa — o valor de referência.
- O **diferencial** do seu produto vs. essa alternativa, traduzido em ganho/economia mensurável.
- Dados ou estimativas do impacto (tempo poupado × custo da hora, receita extra, risco evitado).
- WTP medida (de [`van-westendorp.md`](van-westendorp.md) / [`gabor-granger.md`](gabor-granger.md) / [`conjoint-cbc.md`](conjoint-cbc.md)) para validar o valor percebido vs. o econômico.
- Seu custo incremental, só para o piso de margem.

## Procedimento
1. **Identifique o concorrente de referência.** Qual a alternativa real do cliente hoje? Anote o **preço dela** — esse é o ponto de partida (valor de referência). Se a alternativa é "não fazer nada", o referência é o custo de continuar com o problema.
2. **Liste os diferenciadores.** O que você faz que a alternativa não faz (a favor) e o que a alternativa faz melhor (contra). Some os dois lados.
3. **Monetize cada diferenciador** (valor de diferenciação). Traduza em reais: horas poupadas × custo da hora; aumento de conversão × ticket; multas/erros evitados. Use dados do cliente ou benchmarks.
4. **Calcule o Valor Econômico Total (EVA)** = valor de referência + valor de diferenciação líquido. Esse é o **teto** lógico do preço: acima disso, a alternativa vence.
5. **Decida a fatia de captura.** Você não cobra 100% do EVA — deixa um "excedente do cliente" como incentivo para trocar. Capture tipicamente uma parte (a fatia depende de poder de mercado, atrito de troca, urgência).
6. **Cheque contra a WTP medida.** Compare o preço derivado do EVA com o preço de receita máxima do [`gabor-granger.md`](gabor-granger.md). Gap grande = problema de **comunicação** de valor, não de valor real.
7. **Cheque contra o piso de custo.** Confirme margem saudável (só custos incrementais e evitáveis). EVA alto não vale se a margem for negativa.
8. **Construa o caso de valor.** Documente o cálculo do EVA para usar na copy e em vendas — o cliente precisa **ver** a conta. Liga a [`perceived-value-stack.md`](../positioning/perceived-value-stack.md).
9. **Defina o preço** e, se há segmentos com EVA distinto, derive pacotes ([`packaging-good-better-best.md`](packaging-good-better-best.md)).
10. **Registre** o EVA, a fatia de captura, o preço e o método no `price-test-registry`; passe o gate `pricing/pricing-value-derived-gate`.

## Outputs
- **Cálculo do Valor Econômico Total (EVA)** por segmento, com referência + diferenciação.
- **Preço derivado de valor** (não de custo), com a fatia de captura explícita.
- **Caso de valor** documentado (a conta que a copy e vendas mostram ao cliente).
- Gap entre valor econômico e percebido → plano de comunicação de valor.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Alternativa**: app de idiomas a R$50/mês × 12 = R$600/ano, mas não prepara para entrevista técnica (status quo: dev não consegue a vaga remota).
- **Diferenciação monetizada**: a vaga remota internacional paga ~R$8.000/mês a mais que a vaga local. Antecipar a aprovação em 4 meses vale ~R$32.000 no primeiro ano.
- **EVA**: referência R$600 + diferenciação enorme (dezenas de milhares). O teto lógico é altíssimo.
- **Captura**: cobrar uma fração pequena do ganho. Preço de R$1.490-R$2.990 captura ~5-9% do ganho do 1º ano — fácil de justificar.
- **Caso de valor na copy**: "R$1.990 para destravar +R$96.000/ano de salário remoto". O preço some diante do ganho.
- Decisão: ancorar o preço no **ganho**, não no custo de produção do curso. Comunicar o EVA é o que sustenta o premium.

## Armadilhas
- **Precificar pelo custo.** O custo não interessa ao cliente; ele compara contra a alternativa dele. Custo é só piso.
- **Esquecer de comunicar o valor.** EVA invisível = preço parece caro. Mostre a conta (anti-claim-sem-lastro: use números reais).
- **Capturar 100% do EVA.** Sem excedente, o cliente não tem motivo para trocar. Deixe ganho para ele.
- **Inventar números de valor.** Valor monetizado tem que ter lastro (dado, benchmark, depoimento), senão é veto de compliance.
- **Um EVA único para mercado heterogêneo.** Segmentos com ganho diferente pedem preços diferentes.
- **Confundir valor econômico com percebido.** O econômico é o teto; o percebido é o que vende. Trabalhe os dois.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — calcula o EVA e deriva o preço); `value-equation-engineer` (as alavancas de valor são os diferenciadores que entram no EVA); `positioning-lead-strategist` (a alternativa de referência é a mesma "alternativa competitiva" do posicionamento); `unit-economics-stack-analyst` (garante margem acima do piso de custo); `compliance-auditor` (confere que cada número de valor tem lastro).
- **Frameworks que pareiam**: [`van-westendorp.md`](van-westendorp.md) e [`gabor-granger.md`](gabor-granger.md) (validam o valor percebido vs. econômico), [`conjoint-cbc.md`](conjoint-cbc.md) (WTP por feature alimenta a diferenciação), [`perceived-value-stack.md`](../positioning/perceived-value-stack.md) (comunica o EVA), [`price-elasticity.md`](price-elasticity.md), [`packaging-good-better-best.md`](packaging-good-better-best.md), [`price-anchoring.md`](../price-anchoring.md), [`../value-equation.md`](../value-equation.md).

## Fontes
> **Fonte:** Thomas T. Nagle et al., *The Strategy and Tactics of Pricing* (Routledge); e Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016) — via [`../../reference/books/offers-and-monetization/nagle-strategy-tactics-pricing.md`](../../reference/books/offers-and-monetization/nagle-strategy-tactics-pricing.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
