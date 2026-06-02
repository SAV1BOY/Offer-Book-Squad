---
id: framework.avatar-voc-investigator.dmu-mapping-b2b
title: "DMU Mapping (B2B) — Mapa do Comitê de Compra"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
frameworks: [avatar-voc-investigator.voc-mining, avatar-voc-investigator.objection-belief-mapping, positioning.jtbd, proof-to-claim-chain]
sources:
  - "Matthew Dixon & Brent Adamson, *The Challenger Sale* (2011)."
  - "Neil Rackham, *SPIN Selling* (1988)."
  - "MEDDIC / MEDDPICC (metodologia de qualificação B2B)."
tags: [b2b, dmu, buying-committee, enterprise, stakeholders, roles]
---

# DMU Mapping (B2B) — Mapa da Unidade de Decisão de Compra

## TL;DR
Em B2B, ninguém compra sozinho: decide um **comitê** (a Decision-Making Unit). Cada papel — usuário, comprador econômico, influenciador técnico, campeão, bloqueador, mentor — tem dor, ganho e objeção **diferentes**. O mapa identifica cada papel, captura o VOC de cada um e define a mensagem e a prova por papel. Vence em vendas complexas (deal-book empresarial), onde uma única mensagem genérica perde o comitê. A régua: **o campeão vende por você internamente — dê a ele a munição** para convencer o comprador econômico e neutralizar o bloqueador.

## Quando usar / Quando não
**Use** em todo deal empresarial e no `run-enterprise-deal-book`: ciclos longos, ticket alto, múltiplos decisores.
**Use** quando a oferta exige aprovação de orçamento, segurança/jurídico, ou integração técnica — sinais de comitê.
**Use** junto do [`voc-mining`](voc-mining.md) e do [`objection-belief-mapping`](objection-belief-mapping.md), aplicados **por papel**, não para um avatar único.
**Não use** em B2C ou venda transacional de decisor único — vira complexidade desnecessária. Aí basta o avatar único.
**Não use** uma mensagem só para o comitê todo: o que convence o usuário (facilidade) não convence o CFO (ROI). Segmente por papel.

## Inputs
- O **organograma/ICP da conta** (cargos, área, senioridade) e o handoff de B2B do `deepresearch_squad`.
- O **VOC por papel** ([`voc-mining`](voc-mining.md)): dor, ganho e linguagem de cada cargo.
- A **oferta**, o **mecanismo único**, a **prova** (casos, ROI, segurança) e a **garantia**.
- As **métricas de negócio** que importam ao comprador econômico (custo atual, ROI, payback — do `unit-economics-stack-analyst`).
- O **mapa de objeção-crença** ([`objection-belief-mapping`](objection-belief-mapping.md)) por papel.

## Procedimento
1. **Liste os papéis da DMU** (não cargos, papéis — uma pessoa pode ter dois):
   - **Usuário** — quem vive com o produto no dia a dia; valoriza facilidade e resultado prático.
   - **Comprador econômico** — quem assina o cheque; valoriza ROI, risco e payback.
   - **Influenciador técnico** — quem avalia viabilidade (TI, segurança, jurídico); pode **bloquear** por critério técnico.
   - **Campeão** — quem quer a solução e a defende internamente; precisa de munição.
   - **Bloqueador/Gatekeeper** — quem trava (medo de mudança, política, território).
   - **Mentor/Coach** — quem dá informação interna de bastidor sobre o processo de decisão.
2. **Capture o VOC de cada papel** — dor, ganho desejado, métrica que importa e linguagem própria. O usuário e o CFO falam línguas diferentes.
3. **Mapeie a objeção por papel** — aplique o [`objection-belief-mapping`](objection-belief-mapping.md): a objeção do usuário ("vai dar trabalho aprender") difere da do CFO ("qual o ROI?") e da do técnico ("é seguro? integra?").
4. **Defina a mensagem por papel** — para cada um, a promessa + prova específica: usuário → demonstração e facilidade; CFO → caso de ROI e payback; técnico → segurança, conformidade e integração; campeão → o **kit de venda interna**.
5. **Arme o campeão** — entregue ao campeão o material que ele usa para convencer os outros: one-pager de ROI para o CFO, FAQ de segurança para o TI, prova de adoção para o usuário. O campeão é o seu vendedor interno.
6. **Identifique e neutralize o bloqueador** — descubra a objeção real dele (medo, política) e ou converta, ou contorne com aliados, ou eleve via o comprador econômico.
7. **Mapeie o fluxo de decisão** — com o mentor, entenda a ordem real de aprovação (quem aprova depois de quem) e alinhe a sequência de mensagens a ela.
8. **Cheque a cobertura** — todo papel tem mensagem, prova e objeção tratada? Lacuna num papel-chave (CFO ou técnico) trava o deal.
9. **Registre** no `objection-registry` e no deal-book.

## Outputs
- Um **mapa da DMU**: papel → dor/ganho → métrica → objeção → mensagem → prova.
- O **kit de venda interna** do campeão (one-pagers por papel).
- O **plano de neutralização** do bloqueador.
- O **fluxo de decisão** mapeado (ordem de aprovação).
- Entrada para o deal-book empresarial e o `objection-registry`.

## Exemplo
Oferta de amostra: plataforma de emissão de nota fiscal para uma rede de clínicas (deal empresarial).
- **Usuário (recepcionista)**: dor = "emito nota errado e o paciente reclama"; mensagem = "2 toques, zero erro de tributação"; prova = demo.
- **Comprador econômico (diretor financeiro)**: dor = "multas e horas de retrabalho"; mensagem = "corta 12h/semana de burocracia e o erro tributário, com payback em 2 meses"; prova = caso de ROI de outra rede.
- **Influenciador técnico (TI/segurança)**: objeção = "integra com nosso ERP? é seguro?"; mensagem = "API homologada, LGPD, SSO"; prova = doc técnica + certificação.
- **Campeão (gerente de operações)**: quer reduzir caos; recebe o **kit** = one-pager de ROI para o diretor + FAQ de segurança para o TI.
- **Bloqueador (contador terceirizado)**: teme perder serviço; neutralização = posicionar a ferramenta como aliada que tira o trabalho braçal e mantém a consultoria estratégica dele.

## Armadilhas
- **Tratar o comitê como um avatar.** Uma mensagem genérica perde o CFO ou o técnico. Mensagem e prova **por papel**.
- **Esquecer o comprador econômico.** Encantar o usuário e ignorar quem assina o cheque trava no orçamento. ROI para o CFO é obrigatório.
- **Não armar o campeão.** O campeão quer comprar mas não tem o material para convencer os outros. Sem o kit, ele perde a venda interna.
- **Ignorar o bloqueador.** Um "não" silencioso do TI ou do jurídico mata o deal no fim. Descubra e trate cedo.
- **Confundir cargo com papel.** O mesmo cargo pode ser campeão numa conta e bloqueador noutra. Mapeie o papel real.
- **Pular o fluxo de decisão.** Mandar a mensagem certa na ordem errada (CFO antes do técnico aprovar) emperra. Siga a sequência real.

## Interações
- **Agentes**: `avatar-voc-investigator` (dono — mapeia a DMU e o VOC por papel), `unit-economics-stack-analyst` (fornece ROI/payback para o comprador econômico), `proof-credibility-curator` (prova por papel: ROI, segurança, adoção), `positioning-lead-strategist` (posiciona por papel), `vsl-webinar-scriptwriter` e `email-sms-sequence-writer` (peças por papel no deal-book), `compliance-auditor` (claims de ROI e segurança com lastro).
- **Frameworks que pareiam**: [`voc-mining`](voc-mining.md) (VOC por papel), [`objection-belief-mapping`](objection-belief-mapping.md) (objeção por papel), [`positioning/jtbd`](../positioning/jtbd.md) (o "trabalho" de cada papel), [`proof-to-claim-chain`](../proof-to-claim-chain.md) (prova por claim de cada papel), [`../../reference/books/b2b-enterprise/meddic-meddpicc.md`](../../reference/books/b2b-enterprise/meddic-meddpicc.md).

## Fontes
> **Fonte:** Mobilizador/campeão e consenso do comitê de Matthew Dixon & Brent Adamson, *The Challenger Sale* (2011); descoberta de dor por papel de Neil Rackham, *SPIN Selling* (1988); papéis de decisão (comprador econômico, campeão) da qualificação MEDDIC/MEDDPICC — via [`../../reference/books/b2b-enterprise/dixon-adamson-challenger-sale.md`](../../reference/books/b2b-enterprise/dixon-adamson-challenger-sale.md), [`../../reference/books/b2b-enterprise/rackham-spin-selling.md`](../../reference/books/b2b-enterprise/rackham-spin-selling.md) e [`../../reference/books/b2b-enterprise/meddic-meddpicc.md`](../../reference/books/b2b-enterprise/meddic-meddpicc.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
