---
id: task.growth.build-affiliate-program
title: "Task — Construir o Programa de Afiliados"
type: task
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
consumes:
  - artifact.offer-book
  - artifact.money-model
  - artifact.unit-economics
  - artifact.run-of-show
  - artifact.events-calendar
produces:
  - artifact.affiliate-program
  - artifact.affiliate-prizes
  - artifact.affiliate-blackbook
frameworks: [launch/affiliate-army]
checklists:
  - affiliate-program-checklist
registries: [decision-registry]
tags: [growth, afiliados, jv, dream-100, leaderboard, prizes, blackbook, disclosure, d6]
---

# Task — Construir o programa de afiliados: cohorts, prêmios, funil e blackbook, com a economia fechando

## Objetivo
Desenhar um programa de afiliados onde a economia fecha, os parceiros certos são recrutados, e cada um recebe um funil pronto para promover sem fricção. O estado-pronto: cohorts + estrutura de prêmios dentro do teto da unit economics + funil de afiliado + leaderboard + affiliate blackbook, com disclosure de afiliação em toda peça e escassez de fechamento verdadeira — aprovado no affiliate-program-checklist.

## Agente dono
[`affiliate-program-architect`](../../agents/affiliate-program-architect.md). O general do exército de afiliados; arquiteta cohorts, prêmios, funil, leaderboard e blackbook — não escreve a copy do afiliado nem fecha o contrato comercial. Sem poder de veto, mas recusa publicar o que quebra a economia.

## Gatilho / Quando
Roda em D6: ativa quando o Offer Book está aprovado, a unit economics é conhecida e o run-of-show define a janela. Demais gatilhos: pedido do programa completo (cohorts/prêmios + funil + leaderboard + blackbook), ou recrutamento/ativação de parceiros (Dream 100) para uma janela datada. **Sem unit economics não define comissão** — sem saber quanto vale um cliente, qualquer percentual é chute que pode quebrar a margem. Comissão que inverte o LTV:CAC → **não publicar**; devolver ao [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) e ao [`money-model-designer`](../../agents/money-model-designer.md).

## Inputs (Consome)
- `artifact.unit-economics` — LTV, CAC, payback, margem por venda. **Define o teto de comissão** — quanto se pode pagar por venda sem inverter a economia.
- `artifact.money-model` — a escada e os papéis. Decide **sobre o quê** a comissão incide (front-end, upsell, continuidade).
- `artifact.offer-book` — a Big Idea, a oferta, a prova e os ângulos disponíveis — a matéria do swipe que se entrega ao afiliado.
- `artifact.run-of-show` + `artifact.events-calendar` — as fases e janelas em que os afiliados entram (aquecimento, abertura, fechamento) e os eventos (webinar de JV, live de leaderboard) que ancoram a competição.

## Procedimento
1. **Confirmar o teto econômico.** Ler LTV/CAC/payback. Se a unit economics não está fechada, parar — é a fundação da comissão.
2. **Definir as cohorts.** Dream 100 de topo (bônus extra + co-marketing), lista média (comissão padrão + prêmios), micro/embaixadores (comissão + reconhecimento no leaderboard).
3. **Estruturar comissão e prêmios (ToT).** Gerar ≥3 modelos — linear, tiered por volume, flat + leaderboard de prêmios — e pontuar por fit econômico, poder de motivação, simplicidade e justiça percebida. Aplicar [`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md). Podar os que estouram o teto; a comissão sai do que a unit economics permite, nunca da margem que não existe.
4. **Focar o recrutamento (ToT).** Gerar ≥3 estratégias — poucos gigantes, médios em volume, enxame de micro — e pontuar por alcance total, risco de concentração, qualidade de lead e esforço de gestão. Podar a de risco de concentração alto ou qualidade de lead baixa.
5. **Construir o funil de afiliado.** Página de recrutamento (com a economia e os prêmios) → onboarding com as datas das fases → área com links rastreáveis + swipe (puxado dos ângulos do Offer Book, em **redação original**) + e-mails por fase → reporte. O swipe cobre exatamente as janelas em que os afiliados entram (abertura e fechamento).
6. **Desenhar o leaderboard.** Competição ao vivo atualizada por métrica, com prêmios por ranking — que motiva volume **sem** incentivar promessa enganosa (adicionar critério de qualidade/reembolso ao ranking).
7. **Garantir a disclosure.** A relação de afiliação **deve ser divulgada** (FTC/CDC) em **cada** peça de swipe. A escassez de fechamento que o afiliado explora segue [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md) (transitiva) e **tem de ser verdadeira**.
8. **Empacotar o affiliate blackbook.** Datas, links, swipe original, regras, disclosure e FAQ do afiliado — tudo plug-and-play.
9. **Self-verify (Bloom + red-team).** Após pagar afiliados, o LTV:CAC continua saudável? O funil tem links, swipe, datas e disclosure? O leaderboard incentiva volume sem engano? Antecipar o veto do [`compliance-auditor`](../../agents/compliance-auditor.md) (afiliado que promete resultado sem prova, ou sem disclosure) e corrigir antes.
10. **Registrar e entregar.** Logar a estrutura de comissão/prêmios e o foco de recrutamento no `decision-registry`. Resultados por afiliado seguem ao [`knowledge-librarian`](../../agents/knowledge-librarian.md). Máximo de 2 ciclos antes de escalar.

## Frameworks
[`launch/affiliate-army`](../../frameworks/launch/affiliate-army.md) · (herdados) [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md) e [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md) via o run-of-show.

## Outputs (Produz)
- `artifact.affiliate-program` (template em [`growth/affiliate-program-template`](../../templates/growth/affiliate-program-template.md)) — comissão por degrau, cohorts, funil de afiliado.
- `artifact.affiliate-prizes` (template em [`growth/affiliate-prizes-template`](../../templates/growth/affiliate-prizes-template.md)) — estrutura de prêmios e regras do leaderboard.
- `artifact.affiliate-blackbook` (template em [`growth/affiliate-blackbook-template`](../../templates/growth/affiliate-blackbook-template.md)) — datas, links, swipe original, regras, disclosure, FAQ.
- [`decision-registry`](../../data/registries/decision-registry.md) atualizado com a estrutura de comissão/prêmios e o foco de recrutamento (Dream 100). O blackbook referencia o swipe do [`swipe-registry`](../../data/registries/swipe-registry.md).

## Definition of Done
- Unit economics conhecida e usada como teto da comissão antes de definir percentuais.
- Comissão + prêmios cabem no teto (LTV:CAC saudável após pagar afiliados).
- Cohorts definidas; funil de afiliado pronto para promover (links, swipe, datas, disclosure).
- Disclosure de afiliação presente em **toda** peça; swipe de fechamento usa escassez **verdadeira**.
- Leaderboard motiva volume sem incentivar engano; o affiliate-program-checklist verde; estrutura registrada.

## Gates
[`affiliate-program-checklist`](../../checklists/affiliate/affiliate-program-checklist.md).

## Handoff
**Próxima task:** [`build-pr-plan`](build-pr-plan.md) — dono [`pr-brand-strategist`](../../agents/pr-brand-strategist.md), que recebe os parceiros de topo que também geram PR/co-marketing. Também entrega ao [`compliance-auditor`](../qa-memory/compliance-audit.md) o swipe e as regras para auditoria de claims e disclosure, e ao [`knowledge-librarian`](../../agents/knowledge-librarian.md) o que vira memória. **Garantia:** um programa onde a comissão cabe na economia, os parceiros são curados, o funil está pronto para promover sem fricção, e cada peça de swipe já carrega a disclosure de afiliação obrigatória.
