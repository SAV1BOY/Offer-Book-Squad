---
id: checklist.big-idea.big-idea-new-big-credible-gate
title: "Gate — Nova, Grande e Crível (três dos cinco critérios)"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [big-idea-generator, big-idea-architect/big-idea-scoring, big-idea-architect/promise-hook-villain]
registries: [big-idea-registry, proof-registry]
tags: [gate, big-idea, nova, grande, crivel, criterios, d3]
---

# Gate — Nova, Grande e Crível

## Propósito
Este gate prova que a Big Idea travada é, ao mesmo tempo, **Nova, Grande e Crível** — três dos cinco critérios de uma grande ideia (os outros dois, Relevante e Proprietária, são da [`big-idea-relevant-proprietary-gate`](big-idea-relevant-proprietary-gate.md)). Ele encarna a linhagem de Schwartz e Ogilvy: a ideia precisa ser **fresca** (o mercado não a ouviu à exaustão), **importar de verdade** na vida do avatar e ser **acreditável** dada a prova. Um critério fraco afunda a ideia: uma ideia nova mas incrível não vende; uma grande mas genérica vira commodity; uma crível mas batida não para ninguém. O gate aplica a regra de poda do agente — qualquer critério com nota ≤ 2 reprova, mesmo que os outros sejam altos — e amarra a credibilidade à prova disponível: a promessa não pode exceder o que o [`proof-registry`](../../data/registries/proof-registry.md) sustenta.

## Dono & Escopo
- **owner_agent:** `big-idea-architect` (**tem poder de veto**: ideia que falha em qualquer um dos cinco critérios é reprovação).
- **Artefato inspecionado:** os `scores` (nova, grande, crível) da Big Idea `locked` no [`big-idea-registry`](../../data/registries/big-idea-registry.md), produzidos por [`big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md), e a prova que sustenta a credibilidade no [`proof-registry`](../../data/registries/proof-registry.md).

## Condição de Passagem
A Big Idea travada pontua acima de 2 em Nova, Grande e Crível, e a credibilidade está lastreada na prova disponível, sem promessa que exceda o que se prova.

## Itens
1. **Nova > 2.** Verificar: a ideia é fresca para o mercado (não um clichê da categoria); a nota de Nova na matriz é ≥ 3.
2. **Grande > 2.** Verificar: a ideia muda o jogo na vida do avatar (não um detalhe menor); a nota de Grande é ≥ 3.
3. **Crível > 2.** Verificar: o avatar acredita, dada a prova; a nota de Crível é ≥ 3.
4. **Nenhum critério ≤ 2.** Verificar: nenhum dos três está em 1 ou 2 — um critério fraco afunda a ideia e reprova o gate.
5. **Credibilidade lastreada.** Verificar: a promessa da ideia está sustentada por prova no `proof-registry`; promessa além da prova rebaixa Crível.
6. **Frescor real, não cosmético.** Verificar: a novidade vem do mecanismo/ângulo, não de uma reembalagem de um claim gasto.
7. **Pontuação rastreável.** Verificar: as três notas e suas justificativas estão na matriz de pontuação no `big-idea-registry`.

## Evidência Exigida
Para marcar ✅: linkar a matriz de pontuação no `big-idea-registry` com as notas de Nova, Grande e Crível e suas justificativas (itens 1–4, 7), a prova que sustenta a credibilidade no `proof-registry` (item 5) e a fonte do frescor — o mecanismo/ângulo que torna a ideia nova (item 6).

## Protocolo de Falha
Item vermelho → **veto**: o `big-idea-architect` reprova. Crível baixa → rebaixa a promessa ao que o `proof-registry` sustenta ou escalona ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). Nova baixa → re-ancora no mecanismo único ([`mechanism-architect`](../../agents/mechanism-architect.md)). Grande baixa → reconsidera o desejo dominante do VOC. Re-entrada: re-pontua ou re-ideia (mínimo de 3 ramos) e re-submete. Mudança de prova ou de promessa reabre este gate.

## Links
- Gates irmãos: [`big-idea-single-gate`](big-idea-single-gate.md) · [`big-idea-relevant-proprietary-gate`](big-idea-relevant-proprietary-gate.md) · [`big-idea-awareness-fit-gate`](big-idea-awareness-fit-gate.md) · [`big-idea-meta-angle-gate`](big-idea-meta-angle-gate.md)
- Frameworks: [`big-idea-generator`](../../frameworks/big-idea-generator.md) · [`big-idea-scoring`](../../frameworks/big-idea-architect/big-idea-scoring.md) · [`promise-hook-villain`](../../frameworks/big-idea-architect/promise-hook-villain.md)
- Registries: [`big-idea-registry`](../../data/registries/big-idea-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md)
- Agentes: [`big-idea-architect`](../../agents/big-idea-architect.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`mechanism-architect`](../../agents/mechanism-architect.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
