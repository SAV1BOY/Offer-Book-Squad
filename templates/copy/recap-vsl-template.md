---
id: template.copy.recap-vsl
title: "Recap VSL — Roteiro de Recapitulação e Fechamento"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes: [template.copy.vsl-webinar-script, template.core.offer-book-master, template.strategy.proof-bank]
produces: [data.registry.control]
frameworks: [copy.close-frameworks, copy.pas, copy.fascination-bullets, copy.slippery-slide, awareness-x-sophistication]
checklists: [vsl/vsl-value-before-price-gate, vsl/vsl-cta-strength-gate, vsl/vsl-urgency-gate, vsl/vsl-risk-reversal-gate]
registries: [control-registry, objection-registry, proof-registry]
tags: [template, copy, recap, vsl, closing, replay]
---

# Recap VSL — Roteiro de Recapitulação e Fechamento

A Recap VSL é o vídeo **curto** que reapresenta a oferta para quem já viu a VSL/webinar principal e ainda não comprou: replay de fechamento, e-mail de "última chamada", retargeting. Ela não reconta a história inteira — ela **recapitula a oferta**, reforça a prova mais forte, repete o valor antes do preço, reforça a garantia e a escassez verdadeira, derruba as 2-3 objeções que mais travam a compra e pede a ação uma última vez. É o beat de fecho de objeções da [`vsl-structure`](../../frameworks/copy/vsl-structure.md) isolado em peça própria, na voz padrão ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)). É a peça de maior retorno por minuto que o `vsl-webinar-scriptwriter` escreve.

## Como usar
- **Agente dono:** `vsl-webinar-scriptwriter` (camada D4). Voz fiscalizada pelo `voice-style-guardian`; escassez validada pelo `compliance-auditor`.
- **Task:** `write-recap-vsl`. Consome a [`vsl-webinar-script`](vsl-webinar-script-template.md) principal (reaproveita o value stack, a garantia e a escassez já travados) e o [`proof-bank`](../strategy/proof-bank-template.md) (a prova mais forte).
- **Quando:** depois da VSL/webinar principal, para o público de fechamento (assistiu e não comprou, abriu carrinho e abandonou). Vai no replay, no último e-mail e no retargeting.
- Regra: **curta e direta**. Público já é morno/quente — comprima a história, vá direto à oferta e ao fecho. **Valor antes do preço** mesmo no recap. **Um** CTA. Escassez real (e ainda dentro do prazo verdadeiro). Use [`close-frameworks`](../../frameworks/copy/close-frameworks.md), [`scarcity-block`](../../lib/components/scarcity-block.md), [`cta-block`](../../lib/components/cta-block.md).

## Campos & Instruções
- **{{ABERTURA_RECAP}}** — uma linha que situa o espectador ("você viu o método; deixa eu resumir antes de fechar"). Sem regancho longo.
- **{{RESUMO_OFERTA}}** — o value stack condensado: o que ele leva, em bullets curtos ([`fascination-bullets`](../../frameworks/copy/fascination-bullets.md)).
- **{{PROVA_FORTE}}** — a prova **única** mais persuasiva (o melhor caso, com nome + número).
- **{{ANCORA}}** / **{{PRECO}}** — o valor total relembrado, **depois** o preço (gate `vsl-value-before-price-gate`).
- **{{GARANTIA}}** — a reversão de risco relembrada em uma frase.
- **{{ESCASSEZ}}** — o limite real que ainda vale (vagas restantes, horas até fechar) com motivo honesto.
- **{{OBJECOES_FINAIS}}** — as 2-3 objeções que mais travam a compra agora, respondidas curto ([`close-frameworks`](../../frameworks/copy/close-frameworks.md)).
- **{{CTA}}** — a ação única, com instrução exata e o que acontece ao clicar.

## O Template
```
# RECAP VSL — {{NOME_DA_OFERTA}}
Owner: vsl-webinar-scriptwriter · Voz: brand-default-hormozi-style · Data: {{DATA}}
Público: assistiu/abriu carrinho e NÃO comprou (morno/quente) · Duração-alvo: curta

[ABERTURA] {{ABERTURA_RECAP}}

## 1. RESUMO DA OFERTA (value stack condensado)
{{RESUMO_OFERTA}}

## 2. A PROVA MAIS FORTE
{{PROVA_FORTE}}

## 3. VALOR → PREÇO
Âncora (valor total): R$ {{ANCORA}}  →  PREÇO: R$ {{PRECO}}   [valor ANTES do preço]
Garantia (relembrada): {{GARANTIA}}

## 4. ESCASSEZ VERDADEIRA (ainda no prazo)
{{ESCASSEZ}}  (motivo real: {{MOTIVO_REAL}})

## 5. OBJEÇÕES FINAIS (2-3, curtas)
  - {{OBJECAO_1}} → {{RESPOSTA_1}}
  - {{OBJECAO_2}} → {{RESPOSTA_2}}

## 6. CTA ÚNICO
{{CTA}}
```

## Exemplo preenchido
> **# RECAP VSL — Aprovado em Inglês** · Voz: brand-default-hormozi-style · Público: assistiu e não comprou
>
> **[ABERTURA]** "Você já viu como o Shadowing Técnico funciona. Antes de as vagas fecharem, deixa eu resumir o que você leva."
> **1. RESUMO DA OFERTA** — método Shadowing Técnico; 120 falas de entrevista por stack; roleplay 1:1 com recrutador; correção de pronúncia.
> **2. A PROVA MAIS FORTE** — "O Rafael saiu de R$8k para uma oferta de US$7k/mês em 4 meses. Mesmo método, mesmo roleplay que você recebe."
> **3. VALOR → PREÇO** — Âncora R$2.400 → **R$597**. Garantia: "Não passou numa entrevista em 60 dias? Seguimos de graça até passar."
> **4. ESCASSEZ** — "Restam 9 das 40 vagas e o carrinho fecha hoje às 23h59. O limite é real: o roleplay 1:1 só cabe 40 por mês."
> **5. OBJEÇÕES FINAIS** — "Não tenho tempo" → "São 20 min/dia de shadowing." "Meu inglês é básico" → "O método começa do seu nível; a Paula entrou travando e passou na Shopify."
> **6. CTA** — "Clique em Garantir Minha Vaga agora. Você vai ao checkout de 2 campos e o acesso libera na hora."

## DoD do entregável
A Recap VSL está pronta quando: (1) ela **recapitula** a oferta sem reabrir a história longa — abertura curta que situa o espectador morno/quente; (2) o value stack aparece condensado em bullets; (3) há **uma** prova forte (o melhor caso, com nome + número, do [`proof-bank`](../strategy/proof-bank-template.md)); (4) o **valor vem antes do preço** mesmo no formato curto (`vsl-value-before-price-gate`); (5) a **garantia** é relembrada em uma frase (`vsl-risk-reversal-gate`); (6) a **escassez** ainda é verdadeira e dentro do prazo real, com motivo honesto (`vsl-urgency-gate`, validada pelo `compliance-auditor`) — recap que diz "fecha hoje" tem que fechar; (7) as 2-3 objeções que mais travam a compra estão respondidas curto; (8) há **um** CTA com instrução exata e próximo passo claro (`vsl-cta-strength-gate`); (9) a peça passou pela **voz** ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)), aprovada pelo `voice-style-guardian`; (10) as variações alimentam o [`control-registry`](../../data/registries/control-registry.md). Ela reaproveita o que a [`vsl-webinar-script`](vsl-webinar-script-template.md) já travou — não cria oferta nova.
