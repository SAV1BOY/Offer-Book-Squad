---
id: framework.pricing.packaging-good-better-best
title: "Packaging Good-Better-Best — Empacotamento em Três Degraus"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [kano-model, conjoint-cbc, decoy-effect, value-based-pricing, gabor-granger, price-anchoring]
sources:
  - "Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (Wiley, 2016), cap. sobre bundling e configuração."
  - "Rafi Mohammed, *The 1% Windfall* (HarperBusiness, 2010)."
tags: [pricing, packaging, bundling, good-better-best, tiers, versioning, leaders-fillers-killers]
---

# Packaging Good-Better-Best — Empacotamento em Três Degraus

## TL;DR
Um preço único subcobra os clientes de WTP alta e afasta os de WTP baixa. O empacotamento resolve: você cria **três versões** — Good, Better, Best — para que cada bolso ache a sua. O Good captura quem é sensível a preço; o Best captura quem quer tudo e paga mais; o Better é desenhado para ser o **mais escolhido**. A regra de ouro: a maioria não compra o mais barato — ela compra o do **meio**. Empacotar bem aumenta o ticket médio sem mudar o produto. É como o `pricing-wtp-strategist` transforma WTP segmentada em receita.

## Quando usar / Quando não
**Use** quando há **segmentos com WTP diferente** (quase sempre) e features que dá para distribuir em degraus.
**Use mais** depois de medir WTP por feature ([`conjoint-cbc.md`](conjoint-cbc.md)) e classificar features ([`kano-model.md`](kano-model.md)) — eles dizem o que entra em cada degrau.
**Não use** com produto de feature única e indivisível: aí o jogo é preço único + curva de demanda ([`gabor-granger.md`](gabor-granger.md)).
**Não use** criando degraus demais: 3 (até 4) é o ideal. Mais opções paralisam a escolha e derrubam a conversão.
**Não use** sem um **âncora**: sem um Best caro, o Better não parece bom negócio.

## Inputs
- A WTP por segmento e por feature (de [`conjoint-cbc.md`](conjoint-cbc.md) / [`gabor-granger.md`](gabor-granger.md)).
- A classificação Kano das features (must-be / performance / attractive) — ver [`kano-model.md`](kano-model.md).
- O custo incremental de cada feature (para garantir margem por degrau).
- O perfil dos segmentos-alvo (sensível a preço, mediano, premium).

## Procedimento
1. **Defina o eixo de versão.** Escolha o que escala entre os degraus: volume (mais horas/usuários), funcionalidade (mais features), serviço (mais suporte/proximidade) ou velocidade. Um eixo claro evita confusão.
2. **Aloque features por degrau usando Kano:**
   - **Must-be** → entram em **todos** os degraus (inclusive o Good). Faltar = perde a venda.
   - **Performance** → escalam: pouco no Good, mais no Better, máximo no Best.
   - **Attractive** → concentram-se no Better/Best como o "uau" que justifica subir.
3. **Desenhe o Good como porta de entrada.** Funcional e honesto, mas com uma "falta" sentida que dá vontade de subir. Nunca capenga demais (vira reverse), nunca completo demais (canibaliza o Better).
4. **Desenhe o Best como âncora.** Carregado, premium, para quem quer tudo. Ele existe tanto para vender quanto para **ancorar** o preço e fazer o Better parecer barato ([`price-anchoring.md`](../price-anchoring.md)).
5. **Desenhe o Better como o alvo.** É onde você quer a maioria. Coloca a melhor relação valor/preço e o "uau" certo. Mire ~60-70% das vendas aqui.
6. **Precifique os degraus** com base no valor de cada um ([`value-based-pricing.md`](value-based-pricing.md)), não em custo. Use saltos que tornem o Better o ponto óbvio (regra prática: Better ≈ 1,5-2× Good; Best ≈ 1,5-2× Better).
7. **Considere um decoy.** Se quer empurrar para o Best, adicione uma opção dominada que faça o Best parecer óbvio ([`decoy-effect.md`](decoy-effect.md)).
8. **Nomeie os pacotes** com nomes que sinalizam o público (não "Plano 1/2/3"). Ver [`../magic-naming.md`](../magic-naming.md).
9. **Simule a linha inteira.** Use o simulador do conjoint para checar share e **canibalização** — um degrau não pode roubar margem demais do outro.
10. **Teste e registre.** Lance, meça o mix de vendas por degrau, ajuste. Registre os pacotes e preços no `price-test-registry`; passe o gate `pricing/pricing-packaging-gate`.

## Outputs
- **Tabela Good-Better-Best**: conteúdo, preço e público-alvo de cada degrau.
- **Mix-alvo de vendas** (% esperado em cada degrau) e mix real para ajustar.
- Margem por degrau validada com unit economics.
- Recomendação de decoy/âncora se necessário.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- Eixo: **serviço + velocidade**.
- **Good — "Self" (R$990)**: plataforma + comunidade (must-be). Sem 1:1. Porta de entrada para o sensível a preço.
- **Better — "Pro" (R$1.990)**: tudo do Self + 5h de 1:1 + garantia aprovado-ou-grátis (attractive). **O alvo** — melhor valor/preço. Mira 65% das vendas.
- **Best — "Elite" (R$3.990)**: tudo do Pro + 20h de 1:1 + simulação com recrutador real + revisão de currículo. Âncora premium.
- Resultado: a maioria escolhe o "Pro" porque parece o equilíbrio óbvio; o "Elite" ancora e captura os devs sênior de WTP alta; o "Self" pega quem não fecharia a R$1.990. Ticket médio sobe sem mexer no produto-núcleo.

## Armadilhas
- **Good bom demais.** Se o barato já entrega quase tudo, ninguém sobe. Deixe uma falta proposital.
- **Diferenças confusas entre degraus.** Se o cliente não entende o que muda, ele trava ou compra o mais barato. Um eixo claro, poucas linhas de diferença.
- **Degraus demais.** 5+ opções paralisam. Fique em 3 (máx 4).
- **Sem âncora.** Sem um Best caro, o Better não brilha. O premium ancora mesmo que venda pouco.
- **Precificar por custo.** Cada degrau tem preço pelo **valor** que entrega, não pelo custo das features.
- **Ignorar canibalização.** Um degrau pode roubar margem de outro. Simule a linha inteira.
- **Mix não medido.** Se a maioria compra o Good, o empacotamento falhou. Meça e reconfigure.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — desenha e precifica os degraus); `unit-economics-stack-analyst` (valida margem e payback de cada degrau e a linha consolidada); `money-model-designer` (os degraus viram pontos da escada e habilitam upsell Good→Better→Best); `value-equation-engineer` (cada degrau move alavancas distintas); `mechanism-architect` (o "uau" do Better/Best costuma ser o mecanismo nomeado); `positioning-lead-strategist` (os nomes e o público de cada degrau espelham a posição e a categoria escolhidas).
- **Frameworks que pareiam**: [`kano-model.md`](kano-model.md) (aloca features por degrau), [`conjoint-cbc.md`](conjoint-cbc.md) (WTP por feature e simulação de share), [`decoy-effect.md`](decoy-effect.md) (empurra para o degrau-alvo), [`value-based-pricing.md`](value-based-pricing.md) (preço por valor de cada degrau), [`gabor-granger.md`](gabor-granger.md), [`price-anchoring.md`](../price-anchoring.md), [`../offer-stack-builder.md`](../offer-stack-builder.md), [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md).

## Fontes
> **Fonte:** Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016), cap. sobre bundling e configuração; Rafi Mohammed, *The 1% Windfall* (2010) — via [`../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
