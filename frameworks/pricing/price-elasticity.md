---
id: framework.pricing.price-elasticity
title: "Price Elasticity — Sensibilidade da Demanda ao Preço"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [gabor-granger, van-westendorp, value-based-pricing, conjoint-cbc, packaging-good-better-best]
sources:
  - "Thomas T. Nagle, John E. Hogan & Joseph Zale, *The Strategy and Tactics of Pricing* (Routledge), cap. sobre sensibilidade ao preço."
tags: [pricing, elasticity, demand, price-sensitivity, revenue, margin, optimization]
---

# Price Elasticity — Sensibilidade da Demanda ao Preço

## TL;DR
Elasticidade mede **quanto a demanda muda quando o preço muda**. É a variação % das unidades dividida pela variação % do preço. Se subir 10% o preço derruba 5% as vendas, a elasticidade é -0,5 (**inelástico**: pode subir preço sem perder muito). Se derruba 20%, é -2,0 (**elástico**: cuidado ao subir). Saber isso diz se um aumento de preço **ganha ou perde** receita e lucro. O `pricing-wtp-strategist` usa a elasticidade para escolher a direção do preço e para entender os drivers que tornam o cliente menos sensível.

## Quando usar / Quando não
**Use** quando precisa decidir **a direção e o tamanho** de um movimento de preço (subir, descer, quanto) e quer saber o impacto em receita e lucro.
**Use mais** quando já tem a curva de demanda (do [`gabor-granger.md`](gabor-granger.md)) ou dados reais de vendas a preços diferentes (histórico, testes A/B, mercados distintos).
**Não use** como número fixo: elasticidade é **local** (vale perto do preço atual) e muda por segmento, por estágio e por como o valor é comunicado.
**Não use** para fixar preço do zero: ela ajusta um preço existente; o **nível** vem do valor ([`value-based-pricing.md`](value-based-pricing.md)).

## Inputs
- Pelo menos dois pares (preço, quantidade) — de histórico de vendas, teste A/B, ou da curva de [`gabor-granger.md`](gabor-granger.md).
- A **margem** por unidade (preço − custo incremental), para passar de receita a lucro.
- Os **drivers de sensibilidade** do produto (ver passo 5) para interpretar o número.
- Segmentação, pois a elasticidade difere por avatar.

## Procedimento
1. **Reúna os pontos (preço, quantidade).** Quanto mais pares, melhor. Fontes: vendas históricas a preços distintos, testes A/B de preço, ou a curva de Gabor-Granger.
2. **Calcule a elasticidade-arco** entre dois pontos: E = (%ΔQuantidade) ÷ (%ΔPreço), usando a média dos dois pontos como base (fórmula do ponto médio). O sinal é negativo; o que importa é o **módulo**.
3. **Classifique:** |E| < 1 = **inelástico** (demanda pouco sensível → subir preço aumenta receita); |E| > 1 = **elástico** (subir preço derruba receita); |E| ≈ 1 = receita estável.
4. **Calcule o efeito em receita.** Receita sobe quando você sobe preço **e** a demanda é inelástica; cai quando é elástica. Faça a conta com os números reais, não só com a regra.
5. **Avalie os drivers de sensibilidade** (de Nagle) para entender **por que** o cliente é (in)elástico e como mudar isso:
   - **Valor único**: quanto mais único o produto, menos elástico (sem substituto).
   - **Consciência de substituto**: se o cliente não conhece alternativas, é inelástico.
   - **Comparação difícil**: se é difícil comparar preços, a sensibilidade cai.
   - **Custo total vs. renda**: itens baratos (relativo ao bolso) são inelásticos.
   - **Benefício compartilhado/ROI**: se outro paga ou o ROI é claro, menos sensível.
   - **Custo de troca (sunk)**: quem já investiu na sua solução é menos elástico.
6. **Passe para o lucro.** Receita máxima ≠ lucro máximo. Calcule lucro = (preço − custo) × quantidade em cada preço; o ótimo de lucro fica **acima** do de receita quando há custo variável.
7. **Aja na elasticidade, não só meça.** Reduza a sensibilidade comunicando valor único, dificultando comparação (bundling), ancorando preço alto — daí o link com [`packaging-good-better-best.md`](packaging-good-better-best.md) e [`price-anchoring.md`](../price-anchoring.md).
8. **Segmente.** Calcule por avatar; um pode ser elástico (versão Good barata) e outro inelástico (Best premium).
9. **Registre** a elasticidade, os drivers e a recomendação no `price-test-registry`.

## Outputs
- **Coeficiente de elasticidade** (por segmento) e a classificação elástico/inelástico.
- Projeção do **efeito de um movimento de preço** em receita **e** lucro.
- Lista de **drivers de sensibilidade** acionáveis (o que tornar o cliente menos elástico).
- Recomendação de direção e tamanho do ajuste de preço.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- Dois testes: a R$1.490 vende 100 vagas/mês; a R$1.790 vende 88.
- %ΔP ≈ +18,4%; %ΔQ ≈ -12,8% → **E ≈ -0,70 (inelástico)**.
- Efeito receita: 100×1.490 = R$149k → 88×1.790 = R$157,5k. **Subir preço aumentou receita.**
- Lucro (custo R$300/aluno): (1.490-300)×100 = R$119k → (1.790-300)×88 = R$131k. **Lucro também subiu.**
- Drivers: produto único (método próprio), ROI altíssimo (salário remoto), comparação difícil (ninguém tem pacote igual) → tudo empurra para inelástico.
- Decisão: há espaço para subir mais. Próximo teste a R$1.990. E reforçar a unicidade na copy mantém a baixa elasticidade.

## Armadilhas
- **Tratar elasticidade como constante.** Ela é local e muda longe do preço atual. Não extrapole um aumento de 5% para um de 50%.
- **Confundir correlação com causa.** Vendas caíram após subir preço — ou foi sazonalidade? Isole a variável (teste controlado).
- **Otimizar receita e esquecer lucro.** Com custo variável, o preço de lucro máximo é mais alto que o de receita.
- **Um número para todo mundo.** Segmentos têm elasticidades opostas. Calcule por avatar.
- **Só medir, nunca agir.** A elasticidade é **gerenciável**: valor único e bundling reduzem a sensibilidade.
- **Amostra de um ponto só.** Sem dois pares (preço, quantidade) não há elasticidade. Gere o segundo ponto via teste ou Gabor-Granger.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — calcula e interpreta a elasticidade); `unit-economics-stack-analyst` (converte o efeito de preço em impacto de **lucro** e payback); `value-equation-engineer` (alavancas de valor único reduzem a elasticidade); `money-model-designer` (define quais degraus podem subir preço sem perder volume); `positioning-lead-strategist` (uma posição única e uma categoria própria reduzem a elasticidade ao apagar comparações diretas).
- **Frameworks que pareiam**: [`gabor-granger.md`](gabor-granger.md) (a curva de demanda fornece os pares preço-quantidade), [`value-based-pricing.md`](value-based-pricing.md) (o nível de preço; a elasticidade só ajusta), [`conjoint-cbc.md`](conjoint-cbc.md) (elasticidade por feature via simulador), [`packaging-good-better-best.md`](packaging-good-better-best.md) (bundling reduz sensibilidade), [`price-anchoring.md`](../price-anchoring.md).

## Fontes
> **Fonte:** Thomas T. Nagle et al., *The Strategy and Tactics of Pricing* (Routledge), capítulos sobre gestão da sensibilidade ao preço — via [`../../reference/books/offers-and-monetization/nagle-strategy-tactics-pricing.md`](../../reference/books/offers-and-monetization/nagle-strategy-tactics-pricing.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
