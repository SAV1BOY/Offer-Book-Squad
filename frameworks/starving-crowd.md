---
id: framework.starving-crowd
title: "Starving Crowd — Mercado > Oferta > Persuasão"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
frameworks: [awareness-x-sophistication, value-equation, big-idea-generator, grand-slam-offer, offer-diagnosis]
sources:
  - "Gary Halbert, *The Boron Letters* (1984) — a parábola do 'starving crowd'."
  - "Alex Hormozi, *$100M Offers* (2021), seção 'Starving Crowd / Market'."
tags: [market, demand, starving-crowd, halbert, prioritization]
---

# Starving Crowd — Mercado > Oferta > Persuasão

## TL;DR
Halbert pergunta: se você abrisse uma hamburgueria, qual única vantagem você escolheria? A resposta dele: **uma multidão faminta**. A ordem de alavancagem é **Mercado > Oferta > Persuasão**. Um mercado faminto perdoa uma oferta mediana e copy fraca; um mercado saciado afunda a melhor copy do mundo. Antes de escrever uma palavra, você prova que existe uma multidão com **dor aguda, poder de compra e facilidade de alcance**. O `market-sophistication-analyst` usa este teste como portão de entrada de qualquer projeto.

## Quando usar / Quando não
**Use** no início absoluto — antes de mecanismo, preço ou Big Idea. É o primeiro "vai/não-vai".
**Use** para priorizar entre nichos, segmentos ou ângulos: ataque sempre a fome maior.
**Não use** para justificar pular o diagnóstico de sofisticação/consciência — ele **antecede**, não substitui, a [matriz 5×5](awareness-x-sophistication.md).
**Não use** como veredito permanente: fome muda; reavalie a cada ciclo.

## Inputs
- Lista de mercados/segmentos candidatos.
- Sinais de **dor** (buscas, fóruns, reviews 1-estrela de concorrentes, verbatims do banco de VOC).
- Sinais de **poder de compra** (já gastam nisso? quanto? com que frequência?).
- Sinais de **alcance** (canais onde a multidão já se reúne; custo de mídia).
- Tamanho e crescimento do mercado (do handoff de pesquisa).

## Procedimento
1. **Liste os mercados candidatos** — não comece pelo produto, comece por **quem** sofre.
2. **Pontue a Dor** (0-10): quão aguda e urgente? Mercado que sangra agora > mercado com incômodo morno. Cite verbatims como evidência.
3. **Pontue o Poder de compra** (0-10): a multidão **já paga** por alívio? Histórico de gasto vence promessa de gasto.
4. **Pontue a Facilidade de alcance** (0-10): existe um lugar onde ela já se junta (lista, grupo, plataforma, canal barato)? Mercado faminto mas inalcançável não paga as contas.
5. **Some e ranqueie**: escolha o mercado com a maior soma. Empate, desempate pela Dor.
6. **Confronte o veredito com a sofisticação**: o mercado faminto está em que estágio? Isso já adianta o grau de [mecanismo](unique-mechanism.md) que a oferta vai exigir.
7. **Decida vai/não-vai**: se nenhum candidato passa de um piso mínimo nas três dimensões, **não escreva ainda** — mude o mercado ou a oferta, não a copy.
8. **Registre** o ranking e a evidência no `offer-registry` e a decisão no `decision-registry`; rode `market/market-starving-crowd-gate`.

## Outputs
- **Ranking de mercados** com nota tripla (Dor / Poder / Alcance) e evidência por nota.
- Mercado-alvo escolhido + justificativa.
- Veredito vai/não-vai com a regra de corte.
- Sinal de sofisticação que adianta o trabalho de mecanismo.

## Exemplo
Oferta de amostra: candidatos para um curso de inglês.
- **"Inglês para viajantes"**: Dor 4 (incômodo, não urgente), Poder 6, Alcance 7 → soma 17.
- **"Inglês para profissionais de TI que querem vaga remota internacional"**: Dor 9 (vaga = salário em dólar, dor financeira aguda), Poder 9 (já investem em carreira), Alcance 8 (comunidades dev, LinkedIn) → soma **26**.
- **"Inglês para crianças"**: Dor 5, Poder 7 (pais pagam), Alcance 5 → soma 17.
- **Escolha**: o segmento de TI — a fome é maior e o poder de compra é alto. A mesma oferta venderia mal nos outros dois. O mercado escolhido **antecede** e melhora todo o resto da máquina.

## Armadilhas
- **Começar pelo produto, não pela fome.** "Tenho um curso, quem compra?" inverte a ordem certa.
- **Confundir interesse com fome.** Curiosidade não é dor. Procure quem **já gasta** para aliviar.
- **Ignorar o alcance.** Multidão faminta e inacessível custa caro demais para servir.
- **Tratar o veredito como eterno.** A fome migra; um mercado quente esfria. Reavalie.
- **Usar o teste para pular o diagnóstico de sofisticação.** Ele antecede a matriz, não a dispensa.

## Interações
- **Agentes**: `market-sophistication-analyst` (dono — roda o teste de entrada); `offer-squad-architect` (usa o ranking para desenhar o pipeline do caso); `avatar-voc-investigator` (aprofunda o avatar do mercado escolhido); `big-idea-architect` (ancora a Big Idea na fome dominante); `pricing-wtp-strategist` (poder de compra alimenta WTP).
- **Frameworks que pareiam**: [`awareness-x-sophistication.md`](awareness-x-sophistication.md), [`value-equation.md`](value-equation.md), [`big-idea-generator.md`](big-idea-generator.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md), [`offer/offer-diagnosis.md`](offer/offer-diagnosis.md).

## Fontes
> **Fonte:** Gary Halbert, *The Boron Letters* (1984), parábola do "starving crowd"; reforço em Alex Hormozi, *$100M Offers* (2021) — via [`../reference/books/copywriting/halbert-boron-letters.md`](../reference/books/copywriting/halbert-boron-letters.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
