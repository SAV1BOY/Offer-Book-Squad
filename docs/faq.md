---
id: doc.faq
title: "FAQ — Perguntas Frequentes"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
tags: [faq, help]
---

# FAQ

**Por onde começo um caso novo?**
Pelo [`offerbook-chief`](../agents/offerbook-chief.md): ele trava a frase de escopo e escolhe o project type. Depois siga [`onboarding.md`](onboarding.md).

**Qual project type usar?**
- Oferta não validada → `single-promo` (Tier 1, enxuto).
- Só quero a fundação → `offer-book`.
- Oferta provada + mercado quente → `full-launch`.
- B2B com comitê → `enterprise-deal-book`. Ver o Mapa de Orquestração do chief.

**Por que o HARD STOP antes da copy?**
Porque o maior risco não é copy fraca — é **oferta fraca** e **mercado errado**. Nenhuma copy nasce antes do Offer Book passar no [`offer-book-dod-gate`](../checklists/offer-book-stack/offer-book-dod-gate.md). ~50-60% do trabalho é pesquisa/estratégia.

**O que torna a escassez "verdadeira"?**
Quantidade, prazo ou bônus com mecânica real e verificável. Falsa = veto do [`compliance-auditor`](../agents/compliance-auditor.md), sem override. Ver [`compliance-policy.md`](compliance-policy.md).

**Como adiciono um arquivo novo?**
Use `python scripts/scaffold.py` para gerar o esqueleto do tipo, siga o [`style-guide.md`](style-guide.md), garanta que o id está reservado no [`config.yaml`](../config.yaml) e rode `qa-runner.py`. Ver [`contributing.md`](contributing.md).

**Posso copiar copy de swipe famoso?**
Não. O `swipe/` guarda **estrutura/anatomia** em redação original; citação literal ≤25 palavras, atribuída. Proveniência em [`swipe-sources/attribution-log.md`](../swipe-sources/attribution-log.md).

**O que é o "money model" e por que é a espinha?**
É a **sequência** de ofertas (atração→upsell→downsell→continuidade), não uma oferta avulsa. O [`money-model-designer`](../agents/money-model-designer.md) é dono dela; nada de copy/funil antes de a escada existir.

**Quantas Big Ideas por lançamento?**
UMA (Power of One). O [`big-idea-architect`](../agents/big-idea-architect.md) gera 3-5 via ToT e trava uma; múltiplas = reprovação.

**Onde fica a memória entre lançamentos?**
Nos 10 registries em [`data/registries/`](../data/registries/) + `swipe/` + `archive/`. O [`knowledge-librarian`](../agents/knowledge-librarian.md) cuida disso (`memory_before_repetition`).

**Como rodo a auditoria de qualidade?**
`python scripts/qa-runner.py --dir <pasta>` (score 0-100, gate 95) e `--strict` para fechar forward-refs no final.
