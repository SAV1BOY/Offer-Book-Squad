---
id: template.copy.mailers-inserts
title: "Mailers & Inserts — Mala Direta e Encartes Impressos"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: direct-mail-insert-writer
consumes: [template.core.offer-book-master, template.strategy.big-idea, template.strategy.positioning, template.strategy.proof-bank]
produces: [data.registry.control]
frameworks: [copy.pastor, copy.pas, copy.fascination-bullets, copy.close-frameworks, copy.hook-frameworks, copy.slippery-slide, awareness-x-sophistication]
checklists: [mailer-checklist, vsl/vsl-value-before-price-gate, vsl/vsl-risk-reversal-gate, vsl/vsl-urgency-gate]
registries: [control-registry, objection-registry, proof-registry]
tags: [template, copy, direct-mail, mailer, insert, print, offline]
---

# Mailers & Inserts — Mala Direta e Encartes Impressos

Este template estrutura uma peça de mala direta (carta impressa, autoenvelope, postal) ou um encarte (insert que vai dentro de outra remessa). Mídia impressa segue o mesmo arco de persuasão de [`pastor`](../../frameworks/copy/pastor.md), mas com restrições próprias: o **envelope/teaser** decide se a peça é aberta, o espaço é finito, o **CTA é offline** (telefone, QR code, URL curta, cupom) e a resposta é **rastreável por código**. A peça carrega gancho, problema/amplificação, mecanismo nomeado, prova, oferta com valor antes do preço, garantia, escassez verdadeira, P.S. e CTA com instrução exata. Toda a redação passa pela voz padrão ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)). É o entregável do `direct-mail-insert-writer`.

## Como usar
- **Agente dono:** `direct-mail-insert-writer` (camada D4). A prova vem do `proof-credibility-curator`; a voz, do `voice-style-guardian`; a escassez e os claims, do `compliance-auditor`; o destino do CTA offline (número, QR, código) casa com o `funnel-architect` / `tech-links-deliverability-engineer`.
- **Task:** `write-mailers-inserts`. Consome o [`offer-book-master`](../core/offer-book-master.md), a [`big-idea`](../strategy/big-idea-template.md) (teaser/gancho), a [`positioning`](../strategy/positioning-template.md) (lead) e o [`proof-bank`](../strategy/proof-bank-template.md).
- **Quando:** na D4, para campanhas offline ou híbridas (encarte em revista, mala direta para lista própria, insert em pacote de produto).
- Regra: **valor antes do preço**, mesmo no papel. **Um** CTA offline, com instrução passo a passo e **código de resposta** rastreável (sem rastreio, não dá para medir controle). Escassez 100% real, com prazo/lote verdadeiro. O **P.S.** é a segunda parte mais lida — use-o para repetir a promessa ou a escassez. Use [`guarantee-block`](../../lib/components/guarantee-block.md), [`scarcity-block`](../../lib/components/scarcity-block.md), [`cta-block`](../../lib/components/cta-block.md).

## Campos & Instruções
- **{{TEASER_ENVELOPE}}** — o texto no envelope/topo do encarte que faz abrir/ler. É o gancho da mídia impressa ([`hook-frameworks`](../../frameworks/copy/hook-frameworks.md)).
- **{{HEADLINE}}** — a manchete da peça, derivada da Big Idea.
- **{{ABERTURA}}** — o lead no nível de consciência do avatar ([`lead-types`](../../lib/taxonomies/lead-types.md)).
- **{{PROBLEMA_AMPLIFICACAO}}** — a dor em verbatim + o custo de não agir (verdade, não medo inventado).
- **{{MECANISMO}}** — a causa nomeada do resultado (sem ele, é só promessa).
- **{{PROVA}}** — depoimentos com nome + número; cada um mata uma objeção do [`objection-registry`](../../data/registries/objection-registry.md).
- **{{VALUE_STACK}}** — os componentes com valor, empilhados ([`fascination-bullets`](../../frameworks/copy/fascination-bullets.md)).
- **{{ANCORA}}** / **{{PRECO}}** — valor total, **depois** o preço.
- **{{GARANTIA}}** — a reversão de risco antes do preço.
- **{{ESCASSEZ}}** — o limite real (prazo, lote, cupom que expira) com motivo honesto.
- **{{CTA_OFFLINE}}** — a ação offline (ligar, escanear QR, acessar URL curta, usar cupom) com instrução passo a passo.
- **{{CODIGO_RESPOSTA}}** — o código/URL/telefone rastreável que identifica esta peça (para medir o controle).
- **{{PS}}** — o pós-escrito que repete a promessa ou a escassez (a 2ª coisa mais lida).

## O Template
```
# MAILER / INSERT — {{NOME_DA_OFERTA}}
Owner: direct-mail-insert-writer · Voz: brand-default-hormozi-style · Data: {{DATA}}
Formato: {{CARTA | AUTOENVELOPE | POSTAL | ENCARTE}} · Código de resposta: {{CODIGO_RESPOSTA}}

[TEASER NO ENVELOPE] {{TEASER_ENVELOPE}}
[HEADLINE] {{HEADLINE}}

## 1. ABERTURA / LEAD  {{ABERTURA}}
## 2. PROBLEMA & AMPLIFICAÇÃO  {{PROBLEMA_AMPLIFICACAO}}
## 3. MECANISMO (nomeado)  {{MECANISMO}}
## 4. PROVA
  - {{PROVA_1}} → mata {{OBJECAO_1}}
  - {{PROVA_2}} → mata {{OBJECAO_2}}
## 5. OFERTA (value stack)  {{VALUE_STACK}}
## 6. PREÇO  Âncora R$ {{ANCORA}} → PREÇO R$ {{PRECO}}   [valor ANTES do preço]
## 7. GARANTIA  {{GARANTIA}}
## 8. ESCASSEZ VERDADEIRA  {{ESCASSEZ}} (motivo real: {{MOTIVO_REAL}})
## 9. CTA OFFLINE (instrução passo a passo)  {{CTA_OFFLINE}}  [código: {{CODIGO_RESPOSTA}}]
## 10. P.S.  {{PS}}
```

## Exemplo preenchido
> **# MAILER / INSERT — Clube do Vinho Seleção** · Voz: brand-default-hormozi-style · Formato: AUTOENVELOPE · Código: VINHO-MD7
>
> **[TEASER NO ENVELOPE]** "Dentro: 3 garrafas premium por R$1 (e por que estou fazendo isto)."
> **[HEADLINE]** "Beba vinho de R$120 sem pagar R$120 — e sem virar um chato de adega."
> **1. ABERTURA** (lead de oferta): "Se você gosta de vinho mas se perde na prateleira, esta carta é para você."
> **2. PROBLEMA & AMPLIFICAÇÃO**: "Você compra no escuro, às vezes acerta, quase sempre paga caro por rótulo. E abrir um vinho ruim estraga o jantar."
> **3. MECANISMO**: "Nosso método de **Curadoria às Cegas**: sommeliers provam 400 rótulos por mês e só 6 entram na caixa. Você recebe os que passaram."
> **4. PROVA**: "12 mil assinantes; nota média 4,8/5 nas últimas 10 mil caixas."
> **5. OFERTA**: 6 garrafas curadas/mês + app de harmonização + acesso a lotes raros.
> **6. PREÇO**: Âncora R$720 (varejo) → **primeira caixa por R$1**, depois R$199/mês.
> **7. GARANTIA**: "Não gostou de uma garrafa? A próxima caixa vem com a substituição, sem custo."
> **8. ESCASSEZ**: "Esta condição vale até 30/06 — depois a caixa de boas-vindas volta a R$199" (motivo: lote de boas-vindas limitado).
> **9. CTA OFFLINE**: "Escaneie o QR ou ligue 0800-123-4567 e diga o código **VINHO-MD7**. Leva 2 minutos."
> **10. P.S.**: "Lembre: 3 garrafas premium por R$1 só até 30/06. Depois, R$199. O código VINHO-MD7 garante a condição."

## DoD do entregável
A peça de mala direta/encarte está pronta quando: (1) há um **teaser de envelope/topo** que faz abrir e uma **headline** derivada da Big Idea; (2) a abertura usa o lead certo para a consciência do avatar; (3) problema e amplificação usam verbatim e verdade; (4) o **mecanismo único** é nomeado (sem ele, é só promessa); (5) cada prova ataca uma objeção do [`objection-registry`](../../data/registries/objection-registry.md), com nome e número, e cada claim aponta para o [`proof-registry`](../../data/registries/proof-registry.md); (6) o **valor vem antes do preço** (`vsl-value-before-price-gate`); (7) há **reversão de risco** (`vsl-risk-reversal-gate`) e **escassez 100% verdadeira** com prazo/lote real (`vsl-urgency-gate`, validada pelo `compliance-auditor`); (8) o **CTA é offline e rastreável** — instrução passo a passo (ligar/QR/URL/cupom) **com código de resposta** que identifica a peça para medir o controle; (9) há um **P.S.** que repete a promessa ou a escassez; (10) a peça respeita as restrições da mídia impressa (espaço, sem clique) e passou pela **voz** ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)) e pelo `mailer-checklist`, aprovada pelo `voice-style-guardian`; (11) o código de resposta e as variações alimentam o [`control-registry`](../../data/registries/control-registry.md).
