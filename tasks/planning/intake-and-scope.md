---
id: task.planning.intake-and-scope
title: "Intake & Scope — Receber o Briefing, Classificar o Project Type e Travar UMA Frase de Escopo"
type: task
layer: D0
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes:
  - briefing.raw-offer
  - template.core.offer-book-master
produces:
  - decision.project-type
  - decision.scope-one-sentence
  - artifact.offer-book-master-skeleton
frameworks: [power-of-one, awareness-x-sophistication]
checklists:
  - chief/chief-project-type-gate
  - chief/chief-scope-approval-gate
registries: [decision-registry]
tags: [planning, intake, escopo, project-type, hard-stop, command, d0]
---

# Intake & Scope — receber o briefing, classificar o tipo de projeto e travar o escopo em uma frase

## Objetivo
Transformar um briefing bruto em UM project type classificado, UMA frase de escopo travada e o esqueleto do Offer Book Master aberto — o estado em que o pipeline pode ser desenhado sem ambiguidade.

## Agente dono
[`offerbook-chief`](../../agents/offerbook-chief.md). É o ponto de entrada do squad. Não escreve copy nem desenha oferta; classifica, sequencia, aprova e veta.

## Gatilho / Quando
Roda em D0, no instante em que chega um briefing de oferta bruta (mercado-alvo, produto, preço atual, prova existente, restrição de tempo/orçamento, meta de receita). É a primeira task de toda composição (`run-offer-book`, `run-full-launch`, `run-single-promo`, `run-enterprise-deal-book`). Nada começa antes dela.

## Inputs (Consome)
- **`briefing.raw-offer`** — o pedido cru do solicitante: quem compra, qual a dor, qual a meta, qual o prazo, que prova já existe.
- **[`template.core.offer-book-master`](../../templates/core/offer-book-master.md)** — o mapa-mestre de pré-requisitos; o esqueleto que esta task abre e que `assemble-offer-book` fecha.
- **Registry lido:** [`decision-registry`](../../data/registries/decision-registry.md) — para checar se já existe decisão sobre este caso (memória antes de repetição).

## Procedimento
1. **Leia o briefing e extraia o mínimo.** Confirme três campos: quem compra, qual a dor, qual a meta. Se faltar qualquer um, **não prossiga** — devolva ao solicitante com 3 perguntas objetivas. Não invente escopo.
2. **Reescreva o pedido em UMA frase de escopo** no molde: "Transformar [oferta] para [avatar] em [entregável], até [prazo]." Aplique [`power-of-one`](../../frameworks/power-of-one.md): um avatar, uma promessa, um próximo passo. Se a frase admite dois avatares ou duas promessas, corte até sobrar uma.
3. **Leia o terreno em alto nível** com [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md): estime, sem fechar diagnóstico (isso é do D1), se o mercado parece quente/frio e maduro/novo. Isso calibra a escolha do project type.
4. **Gere ≥3 project types candidatos** (Tree-of-Thoughts) entre os 7: offer-book · single-promo · full-launch · offer-ladder · enterprise-deal-book · relaunch · continuity-launch. Pontue cada um por maturidade da oferta, risco, ROI esperado e prazo.
5. **Pode até UM project type.** Rubrica: oferta não validada + prazo curto → tier menor (single-promo/offer-book); mercado quente + oferta provada → full-launch; B2B com comitê → enterprise-deal-book. Registre as alternativas podadas e o motivo.
6. **Defina a prioridade e o Definition of Done do caso** — o critério testável que dirá "pronto" para este project type específico.
7. **Abra o esqueleto do Offer Book Master** a partir do template, preenchendo só `{{PROJECT_TYPE}}`, `{{NOME_DA_OFERTA}}` (de trabalho) e `{{DATA}}`. Deixe os blocos D1-D3 vazios — eles serão preenchidos pelas tasks a jusante.
8. **Passe os dois gates de comando:** [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md) (existe UM tipo classificado com motivo) e [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md) (a frase de escopo é única e não bifurca).
9. **Escreva as decisões no registry** (project type, escopo, alternativas podadas) e marque o HARD STOP: nenhuma copy antes do `offer-book-stack/offer-book-dod-gate`.

## Frameworks
- [`power-of-one`](../../frameworks/power-of-one.md)
- [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md)

## Outputs (Produz)
- **`decision.project-type`** — um dos 7 tipos, com motivo e alternativas podadas.
- **`decision.scope-one-sentence`** — a frase de escopo travada.
- **`artifact.offer-book-master-skeleton`** — o Offer Book Master aberto com os blocos D1-D3 reservados.
- **Registry escrito:** [`decision-registry`](../../data/registries/decision-registry.md) com `{decision_id, fase, opção_escolhida, alternativas_podadas, motivo, data}`.

## Definition of Done
Existe UM project type classificado, UMA frase de escopo que não admite duas leituras, o esqueleto do Offer Book Master aberto, os dois gates de comando verdes com evidência, e as decisões registradas. O HARD STOP está declarado e o caso está pronto para o desenho de pipeline.

## Gates
- [`chief/chief-project-type-gate`](../../checklists/chief/chief-project-type-gate.md)
- [`chief/chief-scope-approval-gate`](../../checklists/chief/chief-scope-approval-gate.md)

## Handoff
**Próxima task:** [`design-pipeline`](design-pipeline.md) — dono [`offer-squad-architect`](../../agents/offer-squad-architect.md). **Contrato:** o architect recebe (i) o project type classificado (gate verde), (ii) a frase de escopo travada (gate verde) e (iii) o esqueleto do Offer Book Master. Garantia: o architect nunca recebe um escopo elástico — se a frase ainda bifurca, esta task não fecha. Se o briefing for insuficiente, o handoff é de volta ao solicitante, não adiante.
