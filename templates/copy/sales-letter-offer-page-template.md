---
id: template.copy.sales-letter-offer-page
title: "Sales Letter / Offer Page — Carta de Vendas Longa em Seções"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes: [template.core.offer-book-master, template.strategy.big-idea, template.strategy.positioning, template.strategy.proof-bank, template.strategy.value-equation]
produces: [data.registry.control]
frameworks: [copy.pastor, copy.pas, copy.aida, copy.fascination-bullets, copy.close-frameworks, copy.hook-frameworks, copy.slippery-slide, awareness-x-sophistication]
checklists: [vsl/vsl-value-before-price-gate, vsl/vsl-risk-reversal-gate, vsl/vsl-cta-strength-gate, vsl/vsl-urgency-gate]
registries: [control-registry, proof-registry, objection-registry, claim-registry]
tags: [template, copy, sales-letter, offer-page, long-form, pastor]
---

# Sales Letter / Offer Page — Carta de Vendas Longa em Seções

Este template estrutura a página de oferta (ou carta de vendas longa em texto) nas seções que carregam o arco [`pastor`](../../frameworks/copy/pastor.md): headline + lead, problema/amplificação, história + mecanismo, prova/transformação, oferta (value stack), preço ancorado, garantia, escassez verdadeira, FAQ/fecho de objeções e CTA repetido. É a versão **lida**, não falada, da VSL — mesma lógica de persuasão, formatada para a tela. Toda a redação passa pela voz padrão ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)) e cada seção entrega o leitor à próxima sem atrito ([`slippery-slide`](../../frameworks/copy/slippery-slide.md)). Como a VSL, só nasce depois do Offer Book passar no DoD (HARD STOP).

## Como usar
- **Agente dono:** `vsl-webinar-scriptwriter` (camada D4, copy de venda). Voz fiscalizada pelo `voice-style-guardian`; prova do `proof-credibility-curator`; claims e escassez validados pelo `compliance-auditor`; o destino do CTA é definido pelo `funnel-architect`.
- **Task:** `write-sales-letter-offer-page`. Consome o [`offer-book-master`](../core/offer-book-master.md), a [`big-idea`](../strategy/big-idea-template.md) (headline), a [`positioning`](../strategy/positioning-template.md) (lead), o [`proof-bank`](../strategy/proof-bank-template.md) e o [`value-equation`](../strategy/value-equation-template.md).
- **Quando:** na D4, em paralelo ou no lugar da VSL para público mais quente (consciência 4-5), onde a página direta converte melhor que o vídeo longo.
- Regra: **valor antes do preço**, sempre. **Um** CTA, repetido em pontos-chave — sempre a **mesma** ação. Escassez 100% real. Use os componentes [`offer-block`](../../lib/components/offer-block.md), [`value-stack-block`](../../lib/components/value-stack-block.md), [`guarantee-block`](../../lib/components/guarantee-block.md), [`scarcity-block`](../../lib/components/scarcity-block.md), [`cta-block`](../../lib/components/cta-block.md). Cada claim aponta para o [`proof-registry`](../../data/registries/proof-registry.md).

## Campos & Instruções
- **{{HEADLINE}}** — a manchete que para o leitor, derivada da Big Idea. A maior alavanca da página ([`hook-frameworks`](../../frameworks/copy/hook-frameworks.md)).
- **{{SUBHEAD}}** — a promessa específica que confirma a headline e puxa para o lead.
- **{{LEAD}}** — a abertura no nível de consciência do avatar ([`lead-types`](../../lib/taxonomies/lead-types.md)): problema, promessa, segredo, história…
- **{{PROBLEMA_AMPLIFICACAO}}** — a dor em verbatim + o custo real de não resolver (verdade desconfortável, não medo inventado).
- **{{HISTORIA_MECANISMO}}** — a virada que revela e **nomeia** o mecanismo único como a causa.
- **{{PROVA}}** — depoimentos com nome + número, dados, prints; cada um mata uma objeção do [`objection-registry`](../../data/registries/objection-registry.md).
- **{{VALUE_STACK}}** — cada componente com seu valor, empilhado ([`value-stack-block`](../../lib/components/value-stack-block.md), [`fascination-bullets`](../../frameworks/copy/fascination-bullets.md)).
- **{{ANCORA}}** / **{{PRECO}}** — valor total somado, **depois** o preço (gate `vsl-value-before-price-gate`).
- **{{GARANTIA}}** — a reversão de risco antes do preço.
- **{{ESCASSEZ}}** — o limite real com motivo honesto (falsa = veto).
- **{{FAQ}}** — as objeções finais respondidas ([`close-frameworks`](../../frameworks/copy/close-frameworks.md)).
- **{{CTA}}** — a ação única, repetida; o que acontece ao clicar.

## O Template
```
# SALES LETTER / OFFER PAGE — {{NOME_DA_OFERTA}}
Owner: vsl-webinar-scriptwriter · Voz: brand-default-hormozi-style · Data: {{DATA}}
Célula de consciência × sofisticação: {{CELULA}}

[HEADLINE] {{HEADLINE}}
[SUBHEAD]  {{SUBHEAD}}

## 1. LEAD  {{LEAD}}
## 2. PROBLEMA & AMPLIFICAÇÃO  {{PROBLEMA_AMPLIFICACAO}}
## 3. HISTÓRIA + MECANISMO (nomeado)  {{HISTORIA_MECANISMO}}
## 4. PROVA / TRANSFORMAÇÃO
  - {{PROVA_1}} → mata {{OBJECAO_1}}
  - {{PROVA_2}} → mata {{OBJECAO_2}}
## 5. OFERTA (value stack)  {{VALUE_STACK}}
## 6. PREÇO  Âncora R$ {{ANCORA}} → PREÇO R$ {{PRECO}}   [valor ANTES do preço]
## 7. GARANTIA  {{GARANTIA}}
## 8. ESCASSEZ VERDADEIRA  {{ESCASSEZ}} (motivo real: {{MOTIVO_REAL}})
## 9. FAQ / FECHO DE OBJEÇÕES  {{FAQ}}
## 10. CTA (único, repetido)  {{CTA}}
```

## Exemplo preenchido
> **# SALES LETTER / OFFER PAGE — Aprovado em Inglês** · Voz: brand-default-hormozi-style · Célula 4×4
>
> **[HEADLINE]** "Você lê inglês melhor que muita gente nativa. Então por que você trava na entrevista?"
> **[SUBHEAD]** "O método que aprova devs brasileiros em vagas remotas de dólar — em 60 dias."
> **1. LEAD** (oferta, público quente): "Se você já tentou app de idioma e ainda gela na call técnica, leia isto até o fim."
> **2. PROBLEMA & AMPLIFICAÇÃO**: "Toda call em inglês que você evita é uma vaga de US$7k/mês que vai para outro. E cada mês parado, a próxima entrevista parece mais distante."
> **3. HISTÓRIA + MECANISMO**: "Eu travava igual. Até descobrir o **Shadowing Técnico**: imitar em voz alta falas reais de devs, na sua stack. Fala não vem de gramática, vem de repetição guiada."
> **4. PROVA**: Rafael R$8k → US$7k/mês → mata "não funciona comigo". Paula passou na Shopify → mata "minha pronúncia é ruim".
> **5. OFERTA**: método + 120 falas por stack + roleplay 1:1 + correção de pronúncia.
> **6. PREÇO**: Âncora R$2.400 → **R$597**.
> **7. GARANTIA**: "Não passou numa entrevista em 60 dias? Seguimos de graça até passar."
> **8. ESCASSEZ**: 40 vagas por turma (roleplay 1:1 limita a 40/mês).
> **9. FAQ**: "não tenho tempo", "meu nível é básico", "funciona para QA/dados?".
> **10. CTA**: "Garantir Minha Vaga" — vai ao checkout de 2 campos; acesso na hora. (Repetido após a oferta, após a garantia e no fim.)

## DoD do entregável
A página de oferta está pronta quando: (1) a **headline** para o leitor e deriva da Big Idea, com subhead que confirma a promessa; (2) o **lead** abre no nível de consciência do avatar; (3) problema e amplificação usam verbatim e verdade (não medo inventado); (4) a história **nomeia o mecanismo único** como causa; (5) cada prova ataca uma objeção do [`objection-registry`](../../data/registries/objection-registry.md), com nome e número, e cada claim aponta para o [`proof-registry`](../../data/registries/proof-registry.md); (6) o **valor vem antes do preço** — âncora exibida antes do preço real (`vsl-value-before-price-gate`); (7) há **reversão de risco** (`vsl-risk-reversal-gate`) e **escassez 100% verdadeira** com motivo honesto (`vsl-urgency-gate`, validada pelo `compliance-auditor`); (8) há **um** CTA, repetido em pontos-chave, sempre a mesma ação, com o próximo passo claro (`vsl-cta-strength-gate`); (9) o FAQ responde as objeções finais; (10) a peça passou pela **voz** ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)), aprovada pelo `voice-style-guardian`, e flui como um escorregador (lida corrida, sem atrito); (11) as variações de headline alimentam o [`control-registry`](../../data/registries/control-registry.md).
