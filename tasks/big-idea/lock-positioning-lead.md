---
id: task.big-idea.lock-positioning-lead
title: "Lock Positioning & Lead — Travar a Posição Competitiva e o Tipo de Lead que Casa com a Consciência"
type: task
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
consumes:
  - decision.big-idea-locked
  - artifact.big-idea
  - artifact.market-brief
  - artifact.avatar-icp
  - artifact.mechanism-sheet
  - artifact.value-equation
produces:
  - decision.positioning-locked
  - decision.lead-type-locked
  - artifact.positioning
frameworks: [positioning/dunford-positioning, positioning/moore-positioning-formula, positioning/category-design, lead-types, awareness-x-sophistication]
checklists:
  - positioning/positioning-awareness-fit
registries: [decision-registry]
tags: [big-idea, positioning, lead-selection, dunford, moore, awareness, category-design, d3]
---

# Lock Positioning & Lead — travar a posição competitiva e o tipo de lead que casa com a consciência

## Objetivo
Dado a UMA Big Idea travada, fixar a posição competitiva (qual categoria a oferta ocupa e contra o que compete) e o tipo de lead que abre a copy, casado com o nível de consciência do mercado — a moldura dentro da qual toda copy de D4 nasce.

## Agente dono
[`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md), o cartógrafo competitivo. Decide a moldura (categoria de referência, concorrente-fantasma, abertura), não escreve a copy. **Sem poder de veto** — é um decisor vinculante: o `vsl-webinar-scriptwriter`, o `ad-creative-factory` e o `email-sms-sequence-writer` aplicam o lead travado.

## Gatilho / Quando
Roda em D3, quando: (a) o [`big-idea-architect`](../../agents/big-idea-architect.md) trava UMA Big Idea; (b) o chief pede a posição + lead antes do Offer Book DoD; (c) uma mudança de concorrência exige re-posicionar. **Pré-condição:** existe **uma** Big Idea travada (não duas — se chegarem duas, devolvo ao big-idea-architect, pois sem foco não há posição); o market-brief declara consciência + sofisticação e mapeia as alternativas competitivas (inclusive a "não-ação" e a solução caseira); o mechanism-sheet traz o diferenciador. Se a consciência não está declarada, devolvo ao [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md). Sem veto, quando discordo a montante eu **sinalizo** ao chief e registro a ressalva, não bloqueio.

## Inputs (Consome)
- **`artifact.big-idea`** (travada) — promessa, gancho, vilão, mecanismo, consciência-alvo. A posição e o lead **servem** a esta tese; não a contradizem.
- **`artifact.market-brief`** — consciência dominante, sofisticação, as alternativas competitivas reais, a linguagem da categoria.
- **`artifact.avatar-icp`** — o JTBD, o critério de compra, a objeção dominante.
- **`artifact.mechanism-sheet`** — o diferenciador que sustenta a categoria escolhida.
- **`artifact.value-equation`** — o benefício central que entra na fórmula de posicionamento.
- **Registry escrito:** [`decision-registry`](../../data/registries/decision-registry.md).

## Procedimento
1. **Inventarie as alternativas competitivas.** Aplique [`dunford-positioning`](../../frameworks/positioning/dunford-positioning.md): liste concorrente direto, solução caseira, não fazer nada. Descubra contra o que o avatar **realmente** compara (ex.: "fazer sozinho no YouTube").
2. **Crave o atributo de valor único.** O diferenciador que sustenta a posição (não "mais conteúdo", que perde para o grátis — "implementação guiada com o mecanismo X").
3. **Decida a categoria (Tree-of-Thoughts).** Aplique [`category-design`](../../frameworks/positioning/category-design.md): gere ≥3 enquadramentos (competir na existente; sub-nicho; criar nova) e pontue por facilidade de comparação favorável, demanda já existente, custo de educação, defensabilidade. Sofisticação baixa + demanda madura → competir (não pague para educar); sofisticação alta/saturada → criar/renomear categoria (fuja do leilão de claims).
4. **Monte a fórmula de Moore.** Aplique [`moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md): "para [alvo] que [necessidade], o [produto] é um [categoria] que [benefício], diferente de [alternativa]." Sem campo vazio.
5. **Selecione o lead (Tree-of-Thoughts).** Cruze a consciência-alvo da Big Idea com [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) e [`lead-types`](../../frameworks/lead-types.md). Gere ≥3 leads plausíveis e pontue por fit de consciência, congruência com a Big Idea, ceticismo do mercado. Tendência: nível 1 → História; 2 → Problema-Solução; 3 → Segredo (se mecanismo novo); 4 → Oferta; 5 → Oferta direta. Descarte o lead que contradiz a consciência (Oferta direta para frio queima tráfego) ou briga com o gancho.
6. **Valide o fit.** A categoria torna a comparação favorável e é fiel à Big Idea? O lead casa com a consciência e carrega o gancho da tese? A fórmula de Moore fecha sem buraco?
7. **Self-verify (Bloom + red-team).** A fórmula está completa? A categoria torna a comparação favorável ou só repete a do concorrente? Usei Oferta direta num público frio? *"O que o `compliance-auditor` veria como claim de categoria sem prova?"* Se a categoria existente força comparação desfavorável, re-enquadro (sub-nicho/categoria nova).
8. **Registre e passe o gate.** Logue no `decision-registry` (`categoria_referencia`, `categoria_decisao`, `atributo_unico`, `moore_formula`, `alternativas_competitivas`, `lead_type`, `consciencia_alvo`, `lead_justificativa`, `ramos_podados`). Passe o `positioning-awareness-fit`.

## Frameworks
- [`positioning/dunford-positioning`](../../frameworks/positioning/dunford-positioning.md) — alternativas + atributo único + categoria.
- [`positioning/moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md) — a frase de posicionamento.
- [`positioning/category-design`](../../frameworks/positioning/category-design.md) — criar vs competir.
- [`lead-types`](../../frameworks/lead-types.md) — 1 dos 6 leads travado.
- [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) — casar lead ↔ consciência.

## Outputs (Produz)
- **`decision.positioning-locked`** — categoria de referência + decisão de categoria + atributo único + fórmula de Moore + alternativas competitivas.
- **`decision.lead-type-locked`** — 1 dos 6 leads, com consciência-alvo e justificativa.
- **`artifact.positioning`** ([`template`](../../templates/strategy/positioning-template.md)) — a posição e o lead travados, com os ramos podados.
- **Registry escrito:** [`decision-registry`](../../data/registries/decision-registry.md).

## Definition of Done
A posição está travada (categoria + atributo único + fórmula de Moore completa, sem campo vazio); a categoria torna a comparação favorável e é fiel à Big Idea; o lead está travado com justificativa de consciência e carrega o gancho da tese; o gate `positioning-awareness-fit` está verde; a decisão está no registry. Em lançamento multi-consciência, o lead é travado **por segmento** com a matriz entregue.

## Gates
- [`positioning/positioning-awareness-fit`](../../checklists/positioning/positioning-awareness-fit.md) (reprova lead que não casa com a consciência)

## Handoff
**Próxima task:** [`assemble-offer-book`](../assembly/assemble-offer-book.md) — dono [`offerbook-chief`](../../agents/offerbook-chief.md), que recebe a posição + o lead para fechar o último bloco do Offer Book Master e rodar o HARD STOP. Adiante (só **após** o Offer Book DoD), os agentes de copy ([`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md), [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md), [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md), [`ad-creative-factory`](../../agents/ad-creative-factory.md)) aplicam o lead. **Garantia:** cada agente de copy recebe (1) a categoria de referência e o atributo único, (2) a fórmula de Moore pronta para virar headline/abertura e (3) o lead travado com a justificativa de consciência — para que nenhuma peça "escolha" a abertura por conta própria. Fecha a camada D3.
