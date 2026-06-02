---
id: task.assembly.assemble-offer-book
title: "Assemble Offer Book — Fechar o Mapa-Mestre, Rodar o ★ HARD STOP (offer-book-dod-gate) e Liberar (ou Barrar) o D4"
type: task
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes:
  - artifact.offer-book-master-skeleton
  - artifact.market-brief
  - artifact.avatar-icp
  - artifact.voc-verbatim-bank
  - artifact.mechanism-sheet
  - artifact.proof-bank
  - artifact.value-equation-scorecard
  - artifact.money-model
  - artifact.pricing-wtp-sheet
  - artifact.unit-economics-sheet
  - artifact.offer-stack
  - artifact.guarantee
  - artifact.big-idea
  - artifact.positioning
  - decision.lead-type-locked
produces:
  - artifact.offer-book
  - decision.hard-stop-status
frameworks: [proof-to-claim-chain, offer-to-funnel-mapping]
checklists:
  - offer-book-stack/offer-book-dod-gate
  - chief/chief-offer-book-readiness-gate
registries: [offer-registry, decision-registry]
tags: [assembly, offer-book, hard-stop, dod-gate, compliance, readiness, d3]
---

# Assemble Offer Book — fechar o mapa-mestre, rodar o ★ HARD STOP e liberar (ou barrar) o D4

## Objetivo
Transcrever os destilados de D1-D3 nos 10 blocos do Offer Book Master, auditar a verdade da oferta e rodar o **★ HARD STOP** (`offer-book-stack/offer-book-dod-gate`) — verde libera a primeira palavra de copy (D4); vermelho **barra o D4** e devolve ao agente dono do bloco que falhou.

## Agente dono
[`offerbook-chief`](../../agents/offerbook-chief.md), com o [`compliance-auditor`](../../agents/compliance-auditor.md) como auditor de verdade do pacote. O chief não escreve copy nem desenha oferta — ele transcreve o destilado de cada agente, roda os gates e decide seguir ou repetir. Ambos detêm **poder de veto**: o chief sobre cruzar o HARD STOP; o compliance sobre claim sem lastro ou escassez falsa.

## Gatilho / Quando
Roda no fim de D3, quando a camada está fechada: Big Idea travada e posição + lead travados, sobre uma D2 completa (mecanismo provado, value equation aprovada, money model com ≥2 partes, preço por valor, unit economics conhecidos). É o **portão entre estratégia e copy**. **Pré-condição:** todos os blocos D1-D3 têm seu artefato-fonte entregue. Conforme `config.yaml: defaults.hard_stop_before_copy: true` e o `ARCHITECTURE.md`, **nenhuma palavra de copy (D4+) nasce antes deste gate passar**. Se algum bloco está vazio ou um gate a montante está vermelho, esta task **não fecha**.

## Inputs (Consome)
- **`artifact.offer-book-master-skeleton`** + **[`template.core.offer-book-master`](../../templates/core/offer-book-master.md)** — o esqueleto aberto no [`intake-and-scope`](../planning/intake-and-scope.md), com os 10 blocos a preencher.
- **D1:** `artifact.market-brief` (sofisticação + consciência + starving-crowd), `artifact.avatar-icp` + `artifact.voc-verbatim-bank` (dor/desejo/emoção em verbatim, top objeções), `artifact.proof-bank` (cobertura de prova; nenhum claim grande órfão).
- **D2:** `artifact.mechanism-sheet` (nome + 1 frase), `artifact.value-equation-scorecard` (4 alavancas, sem componente órfão), `artifact.money-model` (espinha; partes preenchidas; atração liquida CAC), `artifact.pricing-wtp-sheet` (preço + método de WTP), `artifact.unit-economics-sheet` (LTV/CAC/payback), `artifact.offer-stack` + `artifact.guarantee`.
- **D3:** `artifact.big-idea` (a ÚNICA: promessa/gancho/vilão), `artifact.positioning` + `decision.lead-type-locked` (posição + lead casado com a matriz).
- **Registries lidos/escritos:** [`offer-registry`](../../data/registries/offer-registry.md), [`decision-registry`](../../data/registries/decision-registry.md).

## Procedimento
1. **Confirme a completude dos insumos.** Cada um dos 10 blocos tem seu artefato-fonte? Falta algum → devolva ao agente dono **antes** de transcrever. Não inventar conteúdo de bloco.
2. **Transcreva os destilados nos 10 blocos.** Preencha o Offer Book Master: (1) Mercado, (2) Avatar, (3) Mecanismo, (4) Prova, (5) Valor, (6) Money Model, (7) Pricing & Unit Economics, (8) Big Idea & Posição, (9) Reversão de Risco & Escassez, (10) Status. O arquivo **resume e linka** os templates-fonte — não os duplica. Use a voz do avatar nos campos de dor/desejo/objeção; número e prova nos campos de valor/economia. **Nenhum `{{PLACEHOLDER}}` solto.**
3. **Verifique a cadeia prova→claim.** Aplique [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md): nenhum claim grande está órfão de prova; cada objeção top tem resposta com prova linkada.
4. **Auditoria de verdade (compliance).** O [`compliance-auditor`](../../agents/compliance-auditor.md) inspeciona: claim sem lastro, escassez/urgência sem motivo real, garantia inexequível, âncora fictícia. Achado → marca o bloco como pendente e o gate **não** fica verde.
5. **Confira o mapeamento oferta→funil.** Aplique [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md): cada degrau da espinha tem um próximo passo claro, antecipando o funil de D5 (coerência estrutural antes de liberar copy).
6. **★ RODE O HARD STOP — `offer-book-stack/offer-book-dod-gate`.** Verifique os 10 critérios do DoD do Offer Book Master, item a item, com evidência linkada (não opinião): mercado com sofisticação **e** consciência com evidência; avatar com dor/desejo/emoção em verbatim e 3 objeções com prova; mecanismo nomeado em 1 frase; nenhum claim grande órfão; toda alavanca com ação concreta e nenhum componente órfão; money model com ≥2 partes (alvo 4) e atração que liquida o CAC; preço por método de WTP nomeado e LTV:CAC + payback conhecidos; **UMA** Big Idea com promessa/gancho/vilão e lead que casa com a matriz; garantia e escassez confirmadas reais e exequíveis.
7. **Decida — verde ou vermelho (BLOQUEIO).**
   - **VERDE:** marque o bloco 10 (`STATUS_GATE: VERDE`, data, pendências: nenhuma). Passe também o [`chief/chief-offer-book-readiness-gate`](../../checklists/chief/chief-offer-book-readiness-gate.md). **Só então** o lançamento cruza o HARD STOP para o [`launch-blackbook-skeleton`](../../templates/core/launch-blackbook-skeleton.md) e a copy de D4.
   - **VERMELHO:** **barre o D4.** Nomeie o bloco que falhou, devolva ao agente dono (ex.: claim órfão → [`proof-credibility-curator`](../../agents/proof-credibility-curator.md); escassez falsa → [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md); duas teses → [`big-idea-architect`](../../agents/big-idea-architect.md)), registre a pendência e **recuse liberar a copy**. Nenhuma exceção sem override registrado.
8. **Self-verify (Bloom + red-team).** O escopo ainda é UMA frase (sem scope creep)? Cada critério do gate tem evidência linkada? *"O que o compliance rejeitaria aqui?"* — se houver risco, paro antes de marcar verde.
9. **Registre.** Logue `decision.hard-stop-status` (verde/vermelho + data + pendências) no `decision-registry` e atualize o estado da oferta no `offer-registry`. Override do HARD STOP só com decisão **explícita e registrada** do chief.

## Frameworks
- [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) — cada claim com lastro; nenhum órfão.
- [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) — cada degrau → próximo passo (coerência antes da copy).

## Outputs (Produz)
- **`artifact.offer-book`** ([`template.core.offer-book-master`](../../templates/core/offer-book-master.md)) — o mapa-mestre com os 10 blocos preenchidos e validados; a fonte de verdade de todo o D4+.
- **`decision.hard-stop-status`** — verde (D4 liberado) ou vermelho (D4 barrado) + bloco que falhou + pendências.
- **Registries escritos:** [`decision-registry`](../../data/registries/decision-registry.md) (status do HARD STOP, overrides) e [`offer-registry`](../../data/registries/offer-registry.md) (estado da oferta).

## Definition of Done
Os 10 blocos do Offer Book Master estão preenchidos sem `{{PLACEHOLDER}}` solto; cada critério do `offer-book-dod-gate` está atendido com evidência linkada; o compliance não tem achado aberto; o `chief/chief-offer-book-readiness-gate` está verde; o status do HARD STOP está registrado. Estado terminal: **VERDE** (lançamento cruza para D4) ou **VERMELHO** (D4 barrado, bloco devolvido ao dono). Não existe estado "parcial liberado".

## Gates
- [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) — **★ HARD STOP** (bloqueia D4+).
- [`chief/chief-offer-book-readiness-gate`](../../checklists/chief/chief-offer-book-readiness-gate.md)

## Handoff
**Próxima task (só com HARD STOP VERDE):** a camada de copy D4 — [`write-vsl-webinar`](../copy/write-vsl-webinar.md) (dono [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md)) e as demais tasks de copy, cada uma submetida ao [`voice-style-guardian`](../../agents/voice-style-guardian.md). **Contrato de saída:** os agentes de D4 recebem o Offer Book aprovado como fonte de verdade — Big Idea única, posição + lead travados, mecanismo, value stack, garantia e escassez verdadeira, com cada claim linkado a prova. **Garantia:** nenhuma copy nasce antes deste gate verde; com o gate vermelho, o handoff é **de volta** ao agente dono do bloco que falhou, nunca adiante. Em paralelo, o caso segue para o `launch-blackbook-skeleton` na construção do Blackbook.
