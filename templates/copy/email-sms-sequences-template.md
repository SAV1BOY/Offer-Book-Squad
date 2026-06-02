---
id: template.copy.email-sms-sequences
title: "Email & SMS Sequences — Redação das Mensagens da Sequência"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
consumes: [template.copy.sequence-matrix, template.core.offer-book-master, template.strategy.big-idea, template.strategy.proof-bank]
produces: [data.registry.control]
frameworks: [copy.email-sequence-architecture, copy.aida, copy.slippery-slide, copy.close-frameworks, copy.hook-frameworks, launch.cart-open-close, awareness-x-sophistication]
checklists: [email-sms/email-step-coverage-gate, email-sms/email-segmentation-gate, email-sms/email-timing-gate, email-sms/email-subject-gate, email-sms/email-urgency-coherence-gate]
registries: [control-registry, objection-registry, proof-registry]
tags: [template, copy, email, sms, sequence, launch]
---

# Email & SMS Sequences — Redação das Mensagens da Sequência

Este template redige cada mensagem da sequência de e-mail/SMS depois que o plano já está na matriz ([`sequence-matrix`](sequence-matrix-template.md)). Uma sequência não é uma pilha de mensagens: é uma **narrativa em parcelas** ([`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md)), cada uma com **um** trabalho (indoutrinação, conteúdo-prova, mecanismo, transição, oferta, fechamento) e **um** CTA. A régua de Collier: entre na conversa que já acontece na mente do leitor. Cada mensagem é um arco curto ([`aida`](../../frameworks/copy/aida.md)) — assunto que para, corpo de uma ideia, um CTA. Toda a redação passa pela voz padrão ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)). É o entregável de copy do `email-sms-sequence-writer`.

## Como usar
- **Agente dono:** `email-sms-sequence-writer` (camada D4). A matriz e o calendário casam com o `funnel-architect`; a prova vem do `proof-credibility-curator`; a voz, do `voice-style-guardian`; a escassez do fechamento é validada pelo `compliance-auditor`.
- **Task:** `write-email-sms-sequences`. Preencha a [`sequence-matrix`](sequence-matrix-template.md) **primeiro** (o plano: timing, segmento, assunto), depois redija aqui cada mensagem. Consome o [`offer-book-master`](../core/offer-book-master.md), a [`big-idea`](../strategy/big-idea-template.md) e o [`proof-bank`](../strategy/proof-bank-template.md).
- **Quando:** na D4, para lançamento, carrinho aberto-fechado, indoutrinação, abandono e pós-compra. Segue o calendário de [`cart-open-close`](../../frameworks/launch/cart-open-close.md).
- Regra: **um** trabalho e **um** CTA por mensagem. Segmente por comportamento (quem comprou sai da lista de oferta). Acelere a frequência no último dia. Todo "fecha hoje" fecha de verdade. Leia a sequência **corrida** — tem que contar uma história contínua.

## Campos & Instruções
- **{{ASSUNTO}}** — a linha de assunto: o gancho que decide a abertura ([`hook-frameworks`](../../frameworks/copy/hook-frameworks.md)). Sem abertura, o corpo não importa (gate `email-subject-gate`).
- **{{PREVIEW}}** — o texto de pré-visualização que puxa para o corpo (complementa o assunto, não repete).
- **{{TRABALHO}}** — o trabalho único da mensagem (indoutrinação, conteúdo-prova, mecanismo, transição, oferta, fechamento).
- **{{OBJECAO_ATACADA}}** — a objeção do [`objection-registry`](../../data/registries/objection-registry.md) que esta mensagem mata (uma por mensagem de conteúdo).
- **{{CORPO}}** — uma ideia, um arco AIDA curto, na voz do avatar; costura assunto→preview→corpo sem atrito ([`slippery-slide`](../../frameworks/copy/slippery-slide.md)).
- **{{PROVA}}** — o depoimento/dado que sustenta o claim (nome + número), do [`proof-bank`](../strategy/proof-bank-template.md).
- **{{CTA}}** — a ação única da mensagem; no fechamento, o fecho de objeções + CTA final ([`close-frameworks`](../../frameworks/copy/close-frameworks.md)).
- **{{CANAL}}** / **{{SEGMENTO}}** / **{{TIMING}}** — espelham a matriz (email/sms/whatsapp; o segmento por comportamento; o dia/hora relativo, D0 = fechamento).
- **{{ESCASSEZ_FECHAMENTO}}** — no(s) e-mail(s) de fechamento, o limite real (gate `email-urgency-coherence-gate`).

## O Template
Redija **um bloco por mensagem**, na ordem da matriz.
```
# EMAIL & SMS SEQUENCES — {{NOME_DA_SEQUENCIA}}
Owner: email-sms-sequence-writer · Voz: brand-default-hormozi-style · Data: {{DATA}}
Calendário: {{TIPO}} (ex.: carrinho aberto-fechado) · matriz: sequence-matrix.csv

--- MENSAGEM {{N}} ---
Canal: {{CANAL}} · Segmento: {{SEGMENTO}} · Timing: {{TIMING}}
Trabalho: {{TRABALHO}}  · Objeção atacada: {{OBJECAO_ATACADA}}
Assunto: {{ASSUNTO}}
Preview: {{PREVIEW}}
Corpo:
{{CORPO}}
Prova: {{PROVA}}
CTA (único): {{CTA}}
[se fechamento] Escassez verdadeira: {{ESCASSEZ_FECHAMENTO}} (motivo real: {{MOTIVO_REAL}})
--- fim mensagem {{N}} ---
```

## Exemplo preenchido
> **# EMAIL & SMS SEQUENCES — Lançamento Aprovado em Inglês** · Voz: brand-default-hormozi-style · Calendário: carrinho aberto-fechado
>
> **--- MENSAGEM 1 ---** Canal: email · Segmento: lista-quente · Timing: D-5 09h · Trabalho: indoutrinação/história · Objeção: "inglês é decoreba". Assunto: "Por que devs fluentes em leitura travam na call." Preview: "O problema não é o seu inglês — é o método." Corpo: história curta do fundador travando na entrevista e descobrindo que falar não vem de gramática. Prova: "37 alunos contratados em 2025." CTA: "Responda: qual sua stack?" (engajamento).
> **--- MENSAGEM 5 ---** Canal: email · Segmento: lista-quente · Timing: D-1 09h · Trabalho: oferta (abre carrinho) · Objeção: "vai funcionar comigo?". Assunto: "Vagas abertas: método + 120 falas + roleplay 1:1." Preview: "40 vagas. Abre agora." Corpo: value stack com valor antes do preço (R$2.400 → R$597) + garantia. Prova: "Rafael: R$8k → US$7k/mês." CTA: "Garantir Minha Vaga." 
> **--- MENSAGEM 7 ---** Canal: sms · Segmento: clicou-e5-nao-comprou · Timing: D0 20h · Trabalho: fechamento · Objeção: "depois eu vejo". Assunto/corpo: "Últimas 4h. Depois fecha de verdade e a próxima turma só em 90 dias." CTA: "Garanta agora: [link]." Escassez verdadeira: "restam 9 vagas; roleplay 1:1 limita a 40/mês" (motivo real).
>
> Segmentação: quem comprou na M5 sai da lista; só quem clicou e não comprou recebe M6/M7. Frequência sobe no D0 (manhã + noite).

## DoD do entregável
A sequência está pronta quando: (1) há **uma mensagem redigida por linha** da [`sequence-matrix`](sequence-matrix-template.md), na ordem do `timing`; (2) cada mensagem tem **um** trabalho único e **um** CTA — nenhuma tenta fazer história + prova + oferta de uma vez; (3) a **cobertura do arco** está completa (indoutrinação/história, conteúdo-prova, mecanismo, oferta, fechamento — `email-step-coverage-gate`); (4) cada objeção dominante do [`objection-registry`](../../data/registries/objection-registry.md) é morta por alguma mensagem de conteúdo, com prova (nome + número); (5) a **segmentação** por comportamento está aplicada — quem comprou não recebe oferta/fechamento (`email-segmentation-gate`); (6) o **timing** acelera no fechamento (≥2 envios no D0) e respeita [`cart-open-close`](../../frameworks/launch/cart-open-close.md) (`email-timing-gate`); (7) todo **assunto** é um gancho que para (`email-subject-gate`) e o preview puxa sem repetir; (8) toda **escassez** de fechamento é coerente e verdadeira — "fecha hoje" fecha (`email-urgency-coherence-gate`, validada pelo `compliance-auditor`); (9) a sequência lida **corrida** conta uma história contínua, costurada sem atrito; (10) a peça passou pela **voz** ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)), aprovada pelo `voice-style-guardian`, e as variações de assunto alimentam o [`control-registry`](../../data/registries/control-registry.md).
