---
id: framework.pricing.kano-model
title: "Kano Model — Classificar Features por Tipo de Satisfação"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [maxdiff, conjoint-cbc, value-based-pricing, packaging-good-better-best]
sources:
  - "Noriaki Kano et al., *Attractive Quality and Must-Be Quality*, Journal of the Japanese Society for Quality Control, vol. 14 (1984)."
tags: [kano, features, satisfaction, must-be, performance, delighter, prioritization, packaging]
---

# Kano Model — Classificar Features por Tipo de Satisfação

## TL;DR
O modelo Kano mostra que **nem toda feature mexe na satisfação do mesmo jeito**. Algumas são **obrigatórias** (faltou, o cliente odeia; teve, ninguém nota). Outras são **lineares** (quanto mais, melhor). Outras são **encantadoras** (surpreendem para cima; faltou, ninguém reclama). E há as **indiferentes** e as **reversas** (presença atrapalha). Você classifica cada feature com duas perguntas — uma funcional, uma disfuncional — e usa o resultado para decidir o que é piso de mercado, o que cobrar mais e o que vira o "uau". É como o `pricing-wtp-strategist` separa o que **inclui** do que **monetiza**.

## Quando usar / Quando não
**Use** quando tem uma lista de features candidatas e precisa decidir **o que é obrigatório, o que diferencia e o que encanta** — base para empacotar e precificar.
**Use mais** ao montar Good-Better-Best: as obrigatórias entram em todos os pacotes; as lineares e encantadoras escalam por degrau. Pareia com [`packaging-good-better-best.md`](packaging-good-better-best.md).
**Não use** para achar **preço** ou WTP em reais — Kano classifica satisfação, não disposição a pagar; cruze com [`conjoint-cbc.md`](conjoint-cbc.md).
**Não use** como verdade eterna: o que encanta hoje vira obrigatório amanhã (o cliente se acostuma). Reavalie por ciclo de mercado.

## Inputs
- A lista de features candidatas (do VOC, do roadmap, do concorrente).
- Amostra do avatar-alvo (~100-200), segmentável.
- A tabela de avaliação Kano (matriz funcional × disfuncional) para classificar as respostas.
- Idealmente, uma pergunta de **importância** ou auto-relato de WTP por feature, para cruzar com a classificação.

## Procedimento
1. **Liste as features** a classificar (10-20 itens claros e independentes).
2. **Escreva o par de perguntas Kano** para cada feature, com escala de 5 opções (gosto / espero / neutro / tolero / desgosto):
   - **Funcional**: "Se [a feature] **existir**, como você se sente?"
   - **Disfuncional**: "Se [a feature] **não existir**, como você se sente?"
3. **Aplique a pesquisa.** Cada feature gera duas respostas por pessoa. Mantenha a lista curta para não cansar.
4. **Classifique cada resposta** cruzando funcional × disfuncional na tabela Kano, que devolve uma categoria:
   - **Must-be (obrigatória)**: ausência gera raiva; presença é esperada e não encanta. (Ex.: "espero" na funcional + "desgosto" na disfuncional.)
   - **Performance (linear)**: mais é melhor, menos é pior. ("gosto" + "desgosto".)
   - **Attractive (encantadora)**: presença encanta; ausência não incomoda. ("gosto" + "neutro/tolero".)
   - **Indifferent (indiferente)**: tanto faz nos dois lados → candidata a cortar.
   - **Reverse (reversa)**: o cliente **não quer**; a presença piora. → remover.
   - **Questionable**: resposta incoerente → descartar.
5. **Agregue por feature.** Conte qual categoria venceu (moda) em cada feature. Em empate, a regra clássica prioriza Must-be > Performance > Attractive > Indifferent.
6. **Plote no eixo Kano** (satisfação × funcionalidade): obrigatórias na curva de baixo, lineares na diagonal, encantadoras na curva de cima.
7. **Decida por categoria:**
   - **Must-be** → entra em **todos** os pacotes; não cobre extra, mas nunca falte (faltar = perde a venda).
   - **Performance** → escala por degrau; é o que **justifica preço maior** (mais suporte, mais velocidade).
   - **Attractive** → vira o "uau" do pacote premium ou um bônus-surpresa; alto valor percebido, baixo custo de incluir.
   - **Indifferent / Reverse** → **corte** (evita feature shock, [`../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../../reference/books/offers-and-monetization/ramanujam-monetizing-innovation.md)).
8. **Segmente.** A mesma feature pode ser obrigatória para um avatar e encantadora para outro → empacotamento por segmento.
9. **Registre** a classificação e o método no `price-test-registry`; alimente o gate `pricing/pricing-packaging-gate`.

## Outputs
- **Mapa de features por categoria** (must-be / performance / attractive / indifferent / reverse).
- Regra de **inclusão por pacote**: o que é piso, o que escala, o que encanta, o que sai.
- Lista de **cortes** (indifferent/reverse) que enxuga o produto.
- Insumo direto para o empacotamento e para escolher atributos do conjoint.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Plataforma estável / acesso vitalício** → **must-be**: ninguém paga a mais, mas se cair, o cliente abandona. Entra em todos os pacotes.
- **Horas de suporte 1:1** → **performance**: mais horas, mais satisfação e mais WTP. Escala Good→Better→Best.
- **Simulação de entrevista com recrutador real** → **attractive**: surpreende, vira o "uau" do Best. Custo moderado, valor percebido alto.
- **Certificado em PDF** → **indifferent**: ninguém liga. **Cortado.**
- **Gamificação obrigatória com ranking público** → **reverse**: parte do ICP detesta exposição. **Removido** ou opcional.
- Decisão: Good (plataforma + grupo), Better (+ 5h 1:1), Best (+ 20h 1:1 + simulação com recrutador). Certificado e ranking fora.

## Armadilhas
- **Tratar tudo como performance.** Empilhar feature linear infinitamente incha o produto sem subir WTP. Separe os tipos.
- **Cobrar a mais por must-be.** O cliente espera; cobrar gera revolta. Must-be é entrada, não diferencial.
- **Ignorar reverse features.** Incluir algo que parte do público odeia derruba a conversão. O lado disfuncional revela isso.
- **Classificação estática.** Encantadoras viram obrigatórias com o tempo. Reavalie a cada ciclo.
- **Lista heterogênea sem segmentar.** A média mistura avatares; classifique por segmento.
- **Confundir Kano com preço.** Ele diz **o que** incluir, não **quanto** cobrar. Cruze com conjoint/Gabor-Granger.

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — classifica features e define inclusão por pacote); `unit-economics-stack-analyst` (cruza categoria com custo: encantadora de baixo custo é ouro, performance cara precisa de margem); `mechanism-architect` (a feature encantadora costuma ser o mecanismo único nomeado); `value-equation-engineer` (must-be sustenta Probabilidade; encantadora amplia o Resultado dos Sonhos); `positioning-lead-strategist` (a feature encantadora costuma ser o atributo único que ancora a categoria e a posição).
- **Frameworks que pareiam**: [`maxdiff.md`](maxdiff.md) (prioriza a lista antes de classificar), [`conjoint-cbc.md`](conjoint-cbc.md) (mede a WTP das features classificadas), [`packaging-good-better-best.md`](packaging-good-better-best.md) (a regra de inclusão por degrau), [`value-based-pricing.md`](value-based-pricing.md), [`../value-equation.md`](../value-equation.md).

## Fontes
> **Fonte:** Noriaki Kano et al., "Attractive Quality and Must-Be Quality", *Journal of the Japanese Society for Quality Control* vol. 14 (1984) — acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
