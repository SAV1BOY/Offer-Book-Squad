---
id: checklist.avatar-voc-checklist
title: "Checklist — Avatar & VOC (≥10 verbatims, emoção dominante, objeções mapeadas)"
type: checklist
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
frameworks: [avatar-voc-investigator/voc-mining, avatar-voc-investigator/objection-belief-mapping, positioning/jtbd]
registries: [objection-registry]
tags: [checklist, avatar, icp, voc, verbatim, objecao, emocao-dominante, d1]
---

# Checklist — Avatar & VOC

## Propósito
Este checklist prova que o avatar foi construído **pela voz do cliente** (VOC), não por suposição do time. Existe porque copy que adivinha o cliente erra o tom, a dor e a objeção — e queima verba. O squad só fala a língua do mercado quando minera verbatims reais, isola a **emoção dominante** que move a compra e mapeia as objeções e falsas crenças que travam o "sim". Sem este checklist verde, o mecanismo, a Big Idea e a copy nascem sobre achismo. Ele encarna o princípio `evidence_before_opinion`: cada traço do avatar aponta para uma frase real do cliente, com fonte rastreável. É o alicerce de toda a inteligência (D1) e o insumo direto do mecanismo, da prova e da posição.

## Dono & Escopo
- **owner_agent:** `avatar-voc-investigator` (constrói o avatar/ICP, minera verbatims e mapeia objeções).
- **Artefato inspecionado:** o `artifact.avatar-icp`, o `artifact.voc-verbatim-bank` e o `artifact.objection-belief-map`, com as objeções registradas no [`objection-registry`](../data/registries/objection-registry.md).

## Condição de Passagem
O avatar tem ≥10 verbatims literais com fonte, uma emoção dominante isolada e o mapa de objeções/falsas crenças completo — tudo rastreável no `objection-registry`.

## Itens
1. **≥10 verbatims literais.** Como verificar: contar as citações no banco de VOC — cada uma é frase real do cliente, entre aspas, com fonte (review, entrevista, fórum, comentário) linkada.
2. **Fonte por verbatim.** Como verificar: cada verbatim aponta para origem checável (URL, transcrição, print datado); verbatim sem fonte não conta.
3. **Emoção dominante isolada.** Como verificar: o avatar declara UMA emoção que move a compra (medo, frustração, esperança, vergonha) sustentada por ≥3 verbatims.
4. **Dores e desejos nomeados.** Como verificar: as dores e os desejos centrais aparecem na voz do cliente, não em paráfrase do time, conforme `voc-mining`.
5. **Job-to-be-done declarado.** Como verificar: o "trabalho" que o cliente contrata o produto para fazer está escrito em uma frase, conforme `jtbd`.
6. **Objeções mapeadas.** Como verificar: cada objeção dominante está no `objection-registry` com a falsa crença por trás, conforme `objection-belief-mapping`.
7. **Falsas crenças isoladas.** Como verificar: cada objeção tem a crença-raiz que a sustenta, para a copy poder desarmá-la.
8. **DMU mapeado (se B2B).** Como verificar: em B2B, o comitê de compra (decisor, usuário, bloqueador) está descrito — ou marcado `não-aplicável` em B2C com motivo.
9. **Linguagem reutilizável extraída.** Como verificar: termos e frases do mercado estão marcados para reuso em copy, sem tradução para "marketês".

## Evidência Exigida
Para marcar ✅: linkar o banco de VOC com os ≥10 verbatims e suas fontes (itens 1–2), a seção do avatar que isola a emoção dominante e seus 3 verbatims de apoio (item 3), o mapa de objeções no `objection-registry` com falsas crenças (itens 6–7) e, em B2B, o quadro de DMU (item 8). A linguagem reutilizável aparece no banco marcada como tal.

## Protocolo de Falha
Item vermelho → o avatar volta ao `avatar-voc-investigator` com o defeito nomeado e **bloqueia D1→D2** (mecanismo e prova não avançam sobre avatar incompleto). Menos de 10 verbatims ou verbatim sem fonte reabre a mineração. Re-entrada: completar o banco, atualizar o `objection-registry`, re-submeter. Mudança de mercado-alvo reabre este checklist por inteiro, pois o avatar muda com o segmento.

## Links
- Frameworks: [`voc-mining`](../frameworks/avatar-voc-investigator/voc-mining.md) · [`objection-belief-mapping`](../frameworks/avatar-voc-investigator/objection-belief-mapping.md) · [`jtbd`](../frameworks/positioning/jtbd.md)
- Registries: [`objection-registry`](../data/registries/objection-registry.md)
- Agentes: [`avatar-voc-investigator`](../agents/avatar-voc-investigator.md) · [`market-sophistication-analyst`](../agents/market-sophistication-analyst.md) · [`proof-credibility-curator`](../agents/proof-credibility-curator.md)
- Gates por agente: [`avatar/avatar-voc-verbatim-gate`](avatar/avatar-voc-verbatim-gate.md) · [`avatar/avatar-dominant-emotion-gate`](avatar/avatar-dominant-emotion-gate.md) · [`avatar/avatar-objection-map-gate`](avatar/avatar-objection-map-gate.md)
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate relacionado: [`offer-book-stack/intelligence-complete-gate`](offer-book-stack/intelligence-complete-gate.md)
