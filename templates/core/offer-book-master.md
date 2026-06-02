---
id: template.core.offer-book-master
title: "Offer Book Master — O Mapa-Mestre de Pré-Requisitos da Oferta"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes: [template.strategy.market-brief, template.strategy.avatar-icp, template.strategy.voc-verbatim-bank, template.strategy.proof-bank, template.strategy.mechanism-sheet, template.strategy.value-equation, template.strategy.pricing-wtp, template.strategy.unit-economics, template.strategy.big-idea, template.strategy.positioning]
produces: [template.core.launch-blackbook-skeleton]
frameworks: [power-of-one, value-equation, money-model-sequence, unique-mechanism, proof-to-claim-chain, offer-to-funnel-mapping, awareness-x-sophistication]
checklists: [offer-book-stack/offer-book-dod-gate, chief/chief-offer-book-readiness-gate]
registries: [offer-registry, decision-registry]
tags: [template, offer-book, master, input-spec, hard-stop, core]
---

# Offer Book Master — O Mapa-Mestre de Pré-Requisitos da Oferta

Este é o documento-núcleo do squad. Ele junta, num só lugar, **tudo que precisa estar pronto antes da primeira palavra de copy**: mercado, avatar, mecanismo, prova, valor, money model, preço, unit economics, big idea e posição. Cada bloco é o destilado de um agente D1-D3. É contra este arquivo que o `offer-book-dod-gate` decide se o lançamento pode cruzar o HARD STOP para D4. Sem este mapa cheio e verde, ninguém escreve.

## Como usar
- **Agente dono:** `offerbook-chief`. Co-monta com o `offer-squad-architect` e é auditado pelo `compliance-auditor`.
- **Tasks:** abre em `intake-and-scope` (esqueleto + escopo) e fecha em `assemble-offer-book` (todos os blocos preenchidos e validados).
- **Quando:** o Chief cria este arquivo no D0. Cada agente D1-D3 entrega seu template de estratégia e o Chief **transcreve o destilado** para o bloco correspondente aqui — este arquivo não duplica os templates-fonte, ele os resume e os linka. No fim do D3, o Chief roda o [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md). Verde libera D4; vermelho devolve ao agente dono do bloco que falhou.
- Use a voz do avatar nos campos de dor, desejo e objeção. Use número e prova nos campos de valor e economia. Campo vazio = bloco incompleto = gate vermelho.

## Campos & Instruções
- **{{NOME_DA_OFERTA}}** — o nome de trabalho da oferta núcleo. Vem do `mechanism-sheet`/`positioning`.
- **{{PROJECT_TYPE}}** — o tipo de projeto travado pelo Chief (offer-book, full-launch, single-promo, enterprise-deal-book). Define quais composições rodam.
- **{{MERCADO_SOFISTICACAO}}** / **{{MERCADO_CONSCIENCIA}}** — o estágio (1-5) de [sofisticação](../../lib/taxonomies/sophistication-levels.md) e o nível (1-5) de [consciência](../../lib/taxonomies/awareness-levels.md), cada um com a evidência que o sustenta. Vem do `market-brief`.
- **{{STARVING_CROWD}}** — a prova de que existe uma multidão faminta (dor + poder de compra + facilidade de alcance). Link para o `market-brief`.
- **{{AVATAR_UMA_LINHA}}** — quem é o avatar, em uma frase. Vem do `avatar-icp`.
- **{{DOR_DOMINANTE}}** / **{{DESEJO_DOMINANTE}}** / **{{EMOCAO_DOMINANTE}}** — a dor, o desejo e a emoção que mais pesam, em **verbatim** do avatar. Vêm do `voc-verbatim-bank`.
- **{{TOP_OBJECOES}}** — as 3 objeções de compra mais fortes, cada uma com a resposta/prova que a mata. Vem do `avatar-icp` + `objection-registry`.
- **{{MECANISMO_NOME}}** / **{{MECANISMO_UMA_FRASE}}** — o mecanismo único nomeado e explicado em uma frase ("por que funciona quando o resto falhou"). Vem do `mechanism-sheet`.
- **{{PROVA_RESUMO}}** — o estado da cobertura de prova: quantos claims têm lastro, força média, e o link para o `proof-bank`. Nenhum claim grande pode estar órfão.
- **{{VALUE_EQUATION_LEITURA}}** — a leitura das 4 alavancas (Resultado dos Sonhos, Probabilidade, Tempo, Esforço) e a confirmação de que nenhum componente é órfão de alavanca. Vem do `value-equation`.
- **{{MONEY_MODEL_ESPINHA}}** — a sequência de ofertas (atração → núcleo → upsell → downsell → continuidade), com quantas das 4 partes existem. Usa [`offer-types`](../../lib/taxonomies/offer-types.md). Vem do desenho do `money-model-designer`.
- **{{PRECO_E_METODO}}** — o preço da oferta núcleo e o **método de WTP** que o derivou (van Westendorp, Gabor-Granger, value-based, etc.). Nunca derivado de custo. Vem do `pricing-wtp`.
- **{{UNIT_ECONOMICS}}** — LTV, CAC, razão LTV:CAC, payback e se a oferta de atração **liquida o CAC** no front-end. Vem do `unit-economics`.
- **{{BIG_IDEA}}** — A UMA Grande Ideia (Power of One), com promessa, gancho e vilão. Vem do `big-idea`.
- **{{POSICAO_E_LEAD}}** — a frase de posicionamento e o tipo de [lead](../../lib/taxonomies/lead-types.md) travado pela matriz consciência × sofisticação. Vem do `positioning`.
- **{{GARANTIA}}** — a reversão de risco principal (um dos 13 [tipos](../../lib/taxonomies/guarantee-types.md)), confirmada exequível pela operação. Usa o [`guarantee-block`](../../lib/components/guarantee-block.md).
- **{{ESCASSEZ_VERDADEIRA}}** — o limite real (vagas/prazo) com o motivo honesto, confirmado pelo `compliance-auditor`. Usa o [`scarcity-block`](../../lib/components/scarcity-block.md).
- **{{STATUS_GATE}}** — verde/vermelho do `offer-book-dod-gate`, com data e o que falta.

## O Template
```
# OFFER BOOK MASTER — {{NOME_DA_OFERTA}}
Project type: {{PROJECT_TYPE}} · Owner: offerbook-chief · Data: {{DATA}}

## 1. MERCADO  (fonte: strategy/market-brief)
Sofisticação: estágio {{MERCADO_SOFISTICACAO}} — evidência: {{EVIDENCIA_SOFISTICACAO}}
Consciência:  nível {{MERCADO_CONSCIENCIA}} — evidência: {{EVIDENCIA_CONSCIENCIA}}
Multidão faminta: {{STARVING_CROWD}}

## 2. AVATAR  (fonte: strategy/avatar-icp + voc-verbatim-bank)
Avatar: {{AVATAR_UMA_LINHA}}
Dor dominante (verbatim): "{{DOR_DOMINANTE}}"
Desejo dominante (verbatim): "{{DESEJO_DOMINANTE}}"
Emoção dominante: {{EMOCAO_DOMINANTE}}
Top 3 objeções → resposta/prova:
  1. "{{OBJECAO_1}}" → {{RESPOSTA_1}}
  2. "{{OBJECAO_2}}" → {{RESPOSTA_2}}
  3. "{{OBJECAO_3}}" → {{RESPOSTA_3}}

## 3. MECANISMO  (fonte: strategy/mechanism-sheet)
Nome: {{MECANISMO_NOME}}
Em uma frase: {{MECANISMO_UMA_FRASE}}

## 4. PROVA  (fonte: strategy/proof-bank)
Claims com lastro: {{N_CLAIMS_OK}} / {{N_CLAIMS_TOTAL}} · Força média: {{FORCA_MEDIA}}
Claims órfãos (sem prova): {{LISTA_ORFAOS_OU_NENHUM}}

## 5. VALOR  (fonte: strategy/value-equation)
Resultado dos Sonhos: {{RESULTADO_SONHOS}}
Probabilidade ↑ por: {{O_QUE_SOBE_PROBABILIDADE}}
Tempo ↓ por: {{O_QUE_REDUZ_TEMPO}}
Esforço ↓ por: {{O_QUE_REDUZ_ESFORCO}}
Componentes órfãos de alavanca: {{NENHUM_OU_LISTA}}

## 6. MONEY MODEL  (fonte: money-model-designer)
Atração: {{OFERTA_ATRACAO}} (liquida CAC? {{SIM/NAO}})
Núcleo: {{OFERTA_NUCLEO}}
Upsell: {{OFERTA_UPSELL}}
Downsell: {{OFERTA_DOWNSELL}}
Continuidade: {{OFERTA_CONTINUIDADE}}
Partes preenchidas: {{N}}/4

## 7. PRICING & UNIT ECONOMICS  (fonte: strategy/pricing-wtp + unit-economics)
Preço núcleo: R$ {{PRECO}} — método de WTP: {{METODO}}
LTV: R$ {{LTV}} · CAC: R$ {{CAC}} · LTV:CAC: {{RAZAO}} · Payback: {{PAYBACK}}

## 8. BIG IDEA & POSIÇÃO  (fonte: strategy/big-idea + positioning)
Big Idea (a ÚNICA): {{BIG_IDEA}}
  Promessa: {{PROMESSA}} · Gancho: {{GANCHO}} · Vilão: {{VILAO}}
Posicionamento: {{POSICAO_E_LEAD}}
Lead travado: {{TIPO_DE_LEAD}}

## 9. REVERSÃO DE RISCO & ESCASSEZ
Garantia: {{GARANTIA}} (exequível? {{SIM/NAO}})
Escassez verdadeira: {{ESCASSEZ_VERDADEIRA}} (compliance OK? {{SIM/NAO}})

## 10. STATUS DO HARD STOP
offer-book-dod-gate: {{STATUS_GATE}} — em {{DATA_GATE}}
Pendências: {{O_QUE_FALTA_OU_NENHUMA}}
```

## Exemplo preenchido
> **# OFFER BOOK MASTER — Motor de Recuperação 72h**
> Project type: single-promo · Owner: offerbook-chief · Data: 2026-06-02
>
> **1. MERCADO** — Sofisticação: estágio **3** (ads dos concorrentes só prometem "recupere vendas", sem mecanismo). Consciência: nível **3** (lojistas sabem que carrinho abandonado existe, comparam apps vs agências). Multidão faminta: **donos de e-commerce R$50k+/mês com >60% de abandono — dor cara, fácil de achar no Meta**.
> **2. AVATAR** — Dono de e-commerce que fatura R$50 mil/mês e quer dobrar o lucro sem mais tráfego. Dor: *"vejo o dinheiro escapar no carrinho e não sei recuperar"*. Desejo: *"quero lucrar mais sem gastar mais em anúncio"*. Emoção: frustração. Objeções: 1. *"já tentei e-mail e não funcionou"* → 142 lojas, mediana +21%; 2. *"não tenho tempo de configurar"* → setup feito-para-você em 72h; 3. *"meu nicho é diferente"* → casos em 9 nichos.
> **3. MECANISMO** — Nome: **Janela 72h**. Em uma frase: **as primeiras 72 horas após o abandono concentram 80% da receita recuperável, e uma sequência cronometrada captura essa janela**.
> **4. PROVA** — Claims com lastro: **6/6** · Força média: **forte**. Órfãos: **nenhum**.
> **5. VALOR** — Resultado: recuperar receita perdida sem novo tráfego. Probabilidade ↑ por garantia dobro e 142 casos. Tempo ↓: primeiro resultado em 7 dias. Esforço ↓: setup feito-para-você. Órfãos: **nenhum**.
> **6. MONEY MODEL** — Atração: diagnóstico pago R$47 (liquida CAC: sim). Núcleo: Motor 72h R$497. Upsell: gestão mensal. Downsell: parcelado 3x. Continuidade: otimização recorrente. Partes: **4/4**.
> **7. PRICING & UNIT ECONOMICS** — Preço: R$497 — método **van Westendorp** (faixa R$390-590). LTV R$1.840 · CAC R$210 · LTV:CAC **8,8** · Payback **<30d**.
> **8. BIG IDEA & POSIÇÃO** — Big Idea: **"A janela de 72 horas que devolve o lucro que seu checkout esconde."** Promessa: +15% de receita. Gancho: a janela de 72h. Vilão: o carrinho que "engole" vendas. Posição: o único motor cronometrado pela janela 72h. Lead: **Segredo**.
> **9. REVERSÃO & ESCASSEZ** — Garantia: Dobro ou Nada em 60 dias (exequível: sim). Escassez: 40 vagas/turma por capacidade real de setup (compliance OK: sim).
> **10. STATUS** — offer-book-dod-gate: **VERDE** — em 2026-06-02. Pendências: **nenhuma** → liberado para D4.

## DoD do entregável
O Offer Book Master está pronto quando: (1) os 10 blocos estão preenchidos, sem `{{PLACEHOLDER}}` solto; (2) mercado declara sofisticação **e** consciência **com evidência**; (3) avatar traz dor, desejo e emoção em verbatim, e as 3 objeções têm resposta com prova; (4) o mecanismo está nomeado e cabe em uma frase; (5) nenhum claim grande está órfão de prova; (6) toda alavanca da Value Equation tem ação concreta e nenhum componente é órfão; (7) o Money Model tem ≥2 partes (alvo 4) e a oferta de atração liquida o CAC; (8) o preço deriva de um método de WTP nomeado e LTV:CAC + payback são conhecidos; (9) existe **UMA** Big Idea com promessa, gancho e vilão, e o lead casa com a matriz consciência × sofisticação; (10) garantia e escassez são confirmadas reais e exequíveis. Só então o [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) fica verde e o lançamento cruza o HARD STOP para [`launch-blackbook-skeleton`](launch-blackbook-skeleton.md) e a copy de D4.
