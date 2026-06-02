---
id: framework.offer.value-stacking
title: "Value Stacking — Precificar Percepção, Não Custo"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [offer-stack-builder, value-equation, price-anchoring, guarantee-design, grand-slam-offer]
sources:
  - "Alex Hormozi, *$100M Offers* (2021) — value stacking e ancoragem."
  - "Madhavan Ramanujam, *Monetizing Innovation* (2016) — preço pela disposição a pagar, não pelo custo."
tags: [value-stacking, perceived-value, pricing, anchoring, willingness-to-pay]
---

# Value Stacking — Precificar Percepção, Não Custo

## TL;DR
Preço justo não nasce do **custo** de produzir; nasce do **valor percebido** pelo avatar e da disposição a pagar. O value stacking ancora cada componente da oferta pelo que ele **vale** para o cliente (tempo economizado, dinheiro evitado, dor removida) — e empilha esses valores muito acima do preço. Custo é o seu piso; percepção é o seu teto. O `pricing-wtp-strategist` precifica pela percepção e pela WTP; o custo só protege a margem. Quem precifica por custo deixa dinheiro na mesa e compete por número.

## Quando usar / Quando não
**Use** ao definir o valor ancorado de cada item da [pilha](../offer-stack-builder.md) e ao justificar o preço do Núcleo.
**Use** quando a margem é alta e o valor entregue supera de longe o custo (info, software, serviço, transformação).
**Não use** custo como base de preço em oferta de transformação — é o erro que comoditiza.
**Não use** percepção inflada sem lastro: valor ancorado precisa ser **defensável** (real e crível), senão é veto de compliance e quebra a confiança.

## Inputs
- A **pilha de componentes** já montada ([`../offer-stack-builder.md`](../offer-stack-builder.md)).
- A **disposição a pagar (WTP)** por valor e por componente (Van Westendorp/Gabor-Granger do `pricing-wtp-strategist`).
- O **valor econômico** que cada item gera ou poupa para o avatar (tempo, dinheiro, risco evitado).
- **Referências de mercado** reais (o que alternativas custam) para ancorar com honestidade.
- O **custo de entrega** de cada item (para proteger a margem, não para precificar).

## Procedimento
1. **Separe custo de valor**: anote, para cada componente, o **custo de entregar** (piso) e o **valor para o cliente** (teto). São números diferentes; o preço vive entre eles, perto do teto.
2. **Quantifique o valor de cada item** na moeda do avatar: quanto de **tempo** poupa, quanto de **dinheiro** evita, quanto de **dor/risco** remove. Traga para R$ quando possível.
3. **Ancore cada item por uma referência honesta**: o que custaria obter isso sozinho (contratar, comprar avulso, errar e refazer). Real, não inventada ([`../price-anchoring.md`](../price-anchoring.md)).
4. **Some o valor empilhado**: o total das âncoras. Esse número é a referência de comparação do preço.
5. **Cruze com a WTP**: confirme que o preço-alvo está dentro do que o avatar **paga** por esse valor (não só do que ele "acha caro"). O preço deriva de valor + WTP, nunca de custo.
6. **Posicione o preço como fração do valor**: "valor empilhado R$X, seu investimento R$Y" — o delta precisa ser óbvio.
7. **Proteja a margem com o custo**: garanta que o preço cobre o custo de entrega com folga (o `unit-economics-stack-analyst` valida).
8. **Cheque a defensabilidade**: cada valor ancorado resiste a uma checagem do prospect? Corte exageros.
9. **Registre** os valores ancorados e a derivação do preço no `price-test-registry`; rode os gates de pricing.

## Outputs
- **Tabela valor-vs-custo** por componente (piso de custo, teto de valor, âncora honesta).
- Valor total empilhado e o preço como fração dele.
- Derivação do preço a partir de valor + WTP (não de custo) — rastreável.
- Veredito de defensabilidade por âncora.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Banco de 200 frases**: custo de produzir ~R$0 (já existe); valor para o avatar = dezenas de horas de pesquisa + a frase certa na entrevista; âncora honesta R$497 (um curso avulso de "business English" cobra isso).
- **Simulador 1:1**: custo de entrega ~R$200 (tempo do mentor); valor = a diferença entre passar e não passar (a vaga); âncora R$1.500 (5 horas de professor particular).
- **Trilha 20 min/dia**: custo ~R$0; valor = economia de tempo e constância; âncora R$300.
- **Valor empilhado**: R$2.800. **Custo total de entrega**: ~R$200/aluno. **Preço (de WTP)**: R$1.997.
- **Derivação**: o preço vem do valor empilhado e da WTP do dev (que paga R$2.000+ por uma vaga remota), **não** do custo de R$200. Precificar por custo levaria a cobrar R$400 e comoditizar.
- **Resultado**: margem altíssima protegida, preço justificado por valor real e defensável.

## Armadilhas
- **Precificar por custo.** Em oferta de transformação, custo é piso, não preço — precificar por ele joga dinheiro fora.
- **Inflar o valor ancorado sem lastro.** Âncora inacreditável quebra na checagem do prospect e no compliance.
- **Confundir 'acha caro' com WTP.** Disposição a pagar se mede por método (Van Westendorp), não por palpite.
- **Esquecer a margem.** Valor altíssimo com custo de entrega descontrolado ainda quebra o negócio.
- **Ancorar com referências irreais.** Comparar com algo que ninguém compraria desvaloriza a âncora inteira.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — precifica por valor + WTP); `unit-economics-stack-analyst` (fornece custo de entrega e protege margem); `value-equation-engineer` (o valor percebido vem das alavancas); `proof-credibility-curator` (sustenta as âncoras com prova); `vsl-webinar-scriptwriter` (apresenta valor empilhado antes do preço); `compliance-auditor` (**veta** âncora inflada).
- **Frameworks que pareiam**: [`../offer-stack-builder.md`](../offer-stack-builder.md), [`../value-equation.md`](../value-equation.md), [`../price-anchoring.md`](../price-anchoring.md), [`../guarantee-design.md`](../guarantee-design.md), [`grand-slam-offer.md`](grand-slam-offer.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Offers* (2021), value stacking; Madhavan Ramanujam, *Monetizing Innovation* (2016), preço pela disposição a pagar — via [`../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
