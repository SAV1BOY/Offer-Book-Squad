---
id: template.strategy.avatar-icp
title: "Avatar / ICP — O Cliente Ideal em Uma Página"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
consumes: [template.strategy.market-brief]
produces: [template.core.offer-book-master]
frameworks: [avatar-voc-investigator/voc-mining, avatar-voc-investigator/objection-belief-mapping, positioning/jtbd]
checklists: [avatar/avatar-voc-verbatim-gate, avatar/avatar-dominant-emotion-gate, avatar/avatar-objection-map-gate]
registries: [objection-registry]
tags: [template, avatar, icp, jtbd, objection, strategy]
---

# Avatar / ICP — O Cliente Ideal em Uma Página

Este template descreve **uma pessoa real**, não um intervalo demográfico. Quem é, o que sente, o que tenta a fazer (job-to-be-done), e o que o impede de comprar. Vem da voz do cliente — fala literal, não suposição. É a base de toda copy: sem o avatar nítido, a oferta atira no escuro.

## Como usar
- **Agente dono:** `avatar-voc-investigator` (camada D1).
- **Task:** `build-avatar-voc`. Consome o [`market-brief`](market-brief-template.md) e a pesquisa de VOC.
- **Quando:** depois do diagnóstico de mercado. Alimenta o bloco 2 ("AVATAR") do [`offer-book-master`](../core/offer-book-master.md), junto do [`voc-verbatim-bank`](voc-verbatim-bank-template.md). Validado por três gates: [`avatar-voc-verbatim-gate`](../../checklists/avatar/avatar-voc-verbatim-gate.md), [`avatar-dominant-emotion-gate`](../../checklists/avatar/avatar-dominant-emotion-gate.md) e [`avatar-objection-map-gate`](../../checklists/avatar/avatar-objection-map-gate.md).
- Regra: dor, desejo e objeção em **verbatim** (fala literal do cliente). Cada objeção vira uma linha do [`objection-registry`](../../data/registries/objection-registry.md).

## Campos & Instruções
- **{{AVATAR_UMA_LINHA}}** — quem é o avatar em uma frase (papel + situação + ambição). Vira o `{{AVATAR_UMA_LINHA}}` do offer-book-master.
- **{{DEMOGRAFIA}}** — só o que muda a mensagem (renda, fase de negócio, ferramentas que usa). Sem dado decorativo.
- **{{SITUACAO_ATUAL}}** / **{{SITUACAO_DESEJADA}}** — o "antes → depois": onde está hoje e onde quer chegar.
- **{{JOB_TO_BE_DONE}}** — o progresso que o avatar tenta fazer (o "trabalho" que ele contrata a oferta para realizar), via [`jtbd`](../../frameworks/positioning/jtbd.md). Funcional + emocional + social.
- **{{DOR_DOMINANTE}}** — a dor que mais pesa, em verbatim. Casa com a consciência do [`market-brief`](market-brief-template.md).
- **{{DESEJO_DOMINANTE}}** — o desejo/resultado dos sonhos, em verbatim.
- **{{EMOCAO_DOMINANTE}}** — a emoção que move a decisão (medo, frustração, esperança, orgulho). É o gate `avatar-dominant-emotion-gate`.
- **{{TOP_OBJECOES}}** — as 3 objeções de compra mais fortes, cada uma em verbatim + a crença por trás + a resposta/prova que a mata. Via [`objection-belief-mapping`](../../frameworks/avatar-voc-investigator/objection-belief-mapping.md).
- **{{CRITERIO_FIT}}** / **{{CRITERIO_EXCLUSAO}}** — para quem a oferta **é** e para quem **não é** (alimenta o [`offer-block`](../../lib/components/offer-block.md)).
- **{{DIA_NA_VIDA}}** — um gatilho real onde a dor aparece (o momento de comprar).

## O Template
```
# AVATAR / ICP — {{AVATAR_NOME_DE_TRABALHO}}
Owner: avatar-voc-investigator · Data: {{DATA}}

## 1. QUEM É
Em uma linha: {{AVATAR_UMA_LINHA}}
Demografia que importa: {{DEMOGRAFIA}}
Situação atual: {{SITUACAO_ATUAL}}
Situação desejada: {{SITUACAO_DESEJADA}}

## 2. JOB-TO-BE-DONE  (framework: jtbd)
Funcional (o que resolver): {{JTBD_FUNCIONAL}}
Emocional (como quer se sentir): {{JTBD_EMOCIONAL}}
Social (como quer ser visto): {{JTBD_SOCIAL}}

## 3. DOR, DESEJO, EMOÇÃO  (verbatim)
Dor dominante: "{{DOR_DOMINANTE}}"
Desejo dominante: "{{DESEJO_DOMINANTE}}"
Emoção dominante: {{EMOCAO_DOMINANTE}}

## 4. TOP 3 OBJEÇÕES  (framework: objection-belief-mapping → objection-registry)
1. "{{OBJECAO_1}}" → crença: {{CRENCA_1}} → resposta/prova: {{RESPOSTA_1}}
2. "{{OBJECAO_2}}" → crença: {{CRENCA_2}} → resposta/prova: {{RESPOSTA_2}}
3. "{{OBJECAO_3}}" → crença: {{CRENCA_3}} → resposta/prova: {{RESPOSTA_3}}

## 5. FIT / EXCLUSÃO
É para você se: {{CRITERIO_FIT}}
NÃO é se: {{CRITERIO_EXCLUSAO}}

## 6. GATILHO DE COMPRA
Dia na vida (onde a dor aparece): {{DIA_NA_VIDA}}
```

## Exemplo preenchido
> **# AVATAR / ICP — Carla, dona de e-commerce que estagnou**
> Owner: avatar-voc-investigator · Data: 2026-06-02
>
> **1. QUEM É** — Em uma linha: **dona de e-commerce que fatura R$50 mil/mês e quer dobrar o lucro sem aumentar o tráfego**. Demografia: 1-3 anos de loja, usa Shopify + e-mail básico, faz os próprios anúncios. Atual: cresce no grito, lucro estagnado. Desejada: lucro previsível sem gastar mais em ads.
> **2. JOB-TO-BE-DONE** — Funcional: **recuperar a receita que escapa no checkout**. Emocional: **parar de sentir que "deixa dinheiro na mesa"**. Social: **ser vista como uma operação séria, não amadora**.
> **3. DOR / DESEJO / EMOÇÃO** — Dor: *"vejo o dinheiro escapar no carrinho e não sei recuperar"*. Desejo: *"quero lucrar mais sem gastar mais em anúncio"*. Emoção: **frustração**.
> **4. OBJEÇÕES** — 1. *"já tentei e-mail e não funcionou"* → crença: "isso não serve pro meu caso" → 142 lojas, mediana +21%; 2. *"não tenho tempo de configurar"* → crença: "é complicado" → setup feito-para-você em 72h; 3. *"meu nicho é diferente"* → crença: "comigo não vai dar" → casos em 9 nichos.
> **5. FIT / EXCLUSÃO** — É para você se **já vende todo dia**. NÃO é se **ainda não tem tráfego pago rodando**.
> **6. GATILHO** — Abre o painel de manhã, vê 200 carrinhos abandonados na semana e nenhum recuperado.

## DoD do entregável
O Avatar/ICP está pronto quando: (1) o avatar cabe em **uma** pessoa e uma linha, sem virar "intervalo demográfico"; (2) dor, desejo e emoção estão em **verbatim** — fala literal do cliente, não paráfrase do redator (gate `avatar-voc-verbatim-gate`); (3) existe **uma** emoção dominante nomeada (gate `avatar-dominant-emotion-gate`); (4) há exatamente 3 objeções, cada uma com a crença por trás **e** uma resposta com prova, todas espelhadas no [`objection-registry`](../../data/registries/objection-registry.md) (gate `avatar-objection-map-gate`); (5) o JTBD cobre as três dimensões (funcional, emocional, social); (6) fit e exclusão estão honestos. Só então alimenta o bloco "AVATAR" do [`offer-book-master`](../core/offer-book-master.md) e o [`voc-verbatim-bank`](voc-verbatim-bank-template.md) confirma os verbatims em volume.
