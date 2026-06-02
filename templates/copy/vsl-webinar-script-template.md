---
id: template.copy.vsl-webinar-script
title: "VSL / Webinar Script — Roteiro em 3 Blocos (PASTOR nos Beats)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes: [template.core.offer-book-master, template.strategy.big-idea, template.strategy.positioning, template.strategy.proof-bank, template.strategy.value-equation]
produces: [template.copy.recap-vsl, data.registry.control]
frameworks: [copy.vsl-structure, copy.pastor, copy.pas, copy.slippery-slide, copy.fascination-bullets, copy.close-frameworks, copy.hook-frameworks, awareness-x-sophistication]
checklists: [vsl/vsl-formula-fit-gate, vsl/vsl-value-before-price-gate, vsl/vsl-risk-reversal-gate, vsl/vsl-urgency-gate, vsl/vsl-cta-strength-gate]
registries: [control-registry, proof-registry, objection-registry]
tags: [template, copy, vsl, webinar, script, pastor, three-blocks]
---

# VSL / Webinar Script — Roteiro em 3 Blocos (PASTOR nos Beats)

Este template monta o roteiro de uma VSL ou webinar em **3 blocos** que carregam os beats de [`vsl-structure`](../../frameworks/copy/vsl-structure.md) e mapeiam o arco [`pastor`](../../frameworks/copy/pastor.md): **Bloco 1 — Atração** (gancho, dor, promessa, história), **Bloco 2 — Conteúdo/Mecanismo** (revela e nomeia o mecanismo único, empilha prova), **Bloco 3 — Oferta & Fecho** (value stack, preço ancorado, garantia, escassez verdadeira, CTA único, fecho de objeções). Toda a redação passa pela voz padrão ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)). É o entregável-mestre do `vsl-webinar-scriptwriter` — e ele só nasce **depois** do Offer Book passar no DoD (HARD STOP).

## Como usar
- **Agente dono:** `vsl-webinar-scriptwriter` (camada D4). Voz fiscalizada pelo `voice-style-guardian`; prova por beat do `proof-credibility-curator`; claims e escassez validados pelo `compliance-auditor`.
- **Task:** `write-vsl-webinar-script`. Consome o [`offer-book-master`](../core/offer-book-master.md) completo, a [`big-idea`](../strategy/big-idea-template.md) (vira o gancho), a [`positioning`](../strategy/positioning-template.md) (o lead), o [`proof-bank`](../strategy/proof-bank-template.md) e o [`value-equation`](../strategy/value-equation-template.md).
- **Quando:** abre a D4, depois do HARD STOP. Vira insumo do [`recap-vsl`](recap-vsl-template.md) e alimenta variações de gancho no [`control-registry`](../../data/registries/control-registry.md).
- Regra: **valor sempre antes do preço** (gate dedicado). Mecanismo nomeado no Bloco 2 — sem ele, é só promessa. **Um** CTA. Escassez 100% real. Use os componentes [`offer-block`](../../lib/components/offer-block.md), [`guarantee-block`](../../lib/components/guarantee-block.md), [`scarcity-block`](../../lib/components/scarcity-block.md), [`cta-block`](../../lib/components/cta-block.md). Leia em voz alta cronometrado e corte todo atrito (escorregador).

## Campos & Instruções
- **{{GANCHO}}** — os primeiros 0-30s que param o espectador. Use a Big Idea/lead travado. Via [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md). Gancho fraco mata a VSL inteira.
- **{{DOR}}** — a dor dominante espelhada em verbatim do avatar ("é comigo"). Beat de [`pas`](../../frameworks/copy/pas.md).
- **{{PROMESSA}}** — o resultado dos sonhos: grande e crível, com a saída específica.
- **{{HISTORIA}}** — a virada (do fundador ou de um cliente) que baixa a guarda e prepara o mecanismo.
- **{{MECANISMO}}** — a causa nomeada do resultado: o "por que isto funciona quando o resto falhou". O coração da peça (Bloco 2).
- **{{PROVA}}** — depoimentos (nome + número), dados, demonstrações; cada prova mata uma objeção do [`objection-registry`](../../data/registries/objection-registry.md).
- **{{VALUE_STACK}}** — cada componente da oferta com seu valor, somando até o valor total superar muito o preço ([`fascination-bullets`](../../frameworks/copy/fascination-bullets.md)).
- **{{ANCORA_PRECO}}** / **{{PRECO}}** — o valor total somado, **depois** o preço real (gate `vsl-value-before-price-gate`).
- **{{GARANTIA}}** — a reversão de risco ([`guarantee-block`](../../lib/components/guarantee-block.md)); derruba "e se não funcionar".
- **{{ESCASSEZ}}** — o motivo real para agir agora ([`scarcity-block`](../../lib/components/scarcity-block.md)); falsa = veto.
- **{{CTA}}** — um pedido claro, instrução exata, ação única ([`cta-block`](../../lib/components/cta-block.md)).
- **{{FECHO_OBJECOES}}** — recapitulação + as 3-5 objeções finais respondidas + repetição do CTA ([`close-frameworks`](../../frameworks/copy/close-frameworks.md)).

## O Template
```
# VSL / WEBINAR SCRIPT — {{NOME_DA_OFERTA}}
Owner: vsl-webinar-scriptwriter · Voz: brand-default-hormozi-style · Data: {{DATA}}
Célula de consciência × sofisticação: {{CELULA}} (comprimir Bloco 1 se quente)

## BLOCO 1 — ATRAÇÃO  (PASTOR: Problema · Amplificação)
[0-30s] Gancho: {{GANCHO}}
Dor (verbatim): {{DOR}}
Promessa: {{PROMESSA}}
História/virada: {{HISTORIA}}

## BLOCO 2 — CONTEÚDO / MECANISMO  (PASTOR: Solução · Transformação)
Mecanismo único (nomeado): {{MECANISMO}}
Prova → objeção:
  - {{PROVA_1}} → mata {{OBJECAO_1}}
  - {{PROVA_2}} → mata {{OBJECAO_2}}
Transição para a oferta: {{TRANSICAO}}

## BLOCO 3 — OFERTA & FECHO  (PASTOR: Oferta · Resposta)
Value stack: {{VALUE_STACK}}
Âncora (valor total): R$ {{ANCORA_PRECO}}  →  PREÇO: R$ {{PRECO}}   [valor ANTES do preço]
Garantia: {{GARANTIA}}
Escassez verdadeira: {{ESCASSEZ}}  (motivo real: {{MOTIVO_REAL}})
CTA único: {{CTA}}
Fecho de objeções: {{FECHO_OBJECOES}}
```

## Exemplo preenchido
> **# VSL / WEBINAR SCRIPT — Aprovado em Inglês**
> Owner: vsl-webinar-scriptwriter · Voz: brand-default-hormozi-style · Data: 2026-06-02 · Célula: 2×4
>
> **BLOCO 1 — ATRAÇÃO** — Gancho: "Você programa em inglês o dia todo. Mas trava na entrevista falada. O problema não é o seu inglês." Dor: "Você entende tudo, lê documentação, e na hora de falar a mente trava. A vaga remota de dólar escapa." Promessa: "Em 60 dias você responde qualquer pergunta de entrevista em inglês sem gelar." História: "Eu também travava — até descobrir que falar não vem de gramática."
> **BLOCO 2 — MECANISMO** — Mecanismo: **Shadowing Técnico** — imitar em voz alta falas reais de devs, na sua stack. Prova: Rafael saiu de R$8k para US$7k/mês em 4 meses → mata "não funciona comigo". Paula passou na Shopify no 2º round → mata "minha pronúncia é ruim". Transição: "Se funcionou para eles, veja o que preparei para você."
> **BLOCO 3 — OFERTA & FECHO** — Value stack: método Shadowing + 120 falas de entrevista por stack + roleplay 1:1 + correção de pronúncia (valor total R$2.400). Âncora R$2.400 → **PREÇO R$597**. Garantia: "Se não passar numa entrevista em 60 dias, seguimos juntos de graça até passar." Escassez: 40 vagas por turma (motivo real: roleplay 1:1 limita a 40/mês). CTA: "Clique em Garantir Minha Vaga." Fecho: responde "não tenho tempo", "meu inglês é fraco", "e se eu não passar" e repete o CTA.

## DoD do entregável
O roteiro está pronto quando: (1) os **3 blocos** existem e carregam os beats — Atração (gancho que para, dor em verbatim, promessa, história), Conteúdo/Mecanismo, Oferta & Fecho — mapeando PASTOR (`vsl-formula-fit-gate`); (2) o **mecanismo único** é revelado e **nomeado** no Bloco 2 (sem ele, é só promessa empilhada); (3) cada prova ataca uma objeção do [`objection-registry`](../../data/registries/objection-registry.md), com nome e número; (4) o **valor vem antes do preço** — âncora de valor total exibida antes do preço real (`vsl-value-before-price-gate`); (5) há **reversão de risco** explícita (`vsl-risk-reversal-gate`) e **escassez 100% verdadeira** com motivo real (`vsl-urgency-gate`, validada pelo `compliance-auditor`); (6) há **um** CTA claro com instrução exata (`vsl-cta-strength-gate`); (7) o fecho responde as 3-5 objeções finais e repete o CTA; (8) a peça passou pela **voz** ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)) — frases curtas, voz ativa, presente, sem firula — aprovada pelo `voice-style-guardian`; (9) lida em voz alta cronometrada, sem beat que faça o espectador parar (escorregador); (10) as variações de gancho alimentam o [`control-registry`](../../data/registries/control-registry.md). Só então vira insumo do [`recap-vsl`](recap-vsl-template.md).
