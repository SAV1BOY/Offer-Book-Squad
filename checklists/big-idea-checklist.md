---
id: checklist.big-idea-checklist
title: "Checklist — Big Idea (UMA Big Idea nos 5 critérios, casada à consciência)"
type: checklist
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [big-idea-generator, power-of-one, big-idea-architect/big-idea-ideation-tot, big-idea-architect/big-idea-scoring, big-idea-architect/promise-hook-villain, meta-launch-principle]
registries: [big-idea-registry]
tags: [checklist, big-idea, power-of-one, consciencia, d3]
---

# Checklist — Big Idea

## Propósito
Este checklist prova que existe **UMA Big Idea travada**, aprovada nos cinco critérios e casada ao nível de consciência dominante do mercado. Existe porque o Power of One é inegociável: múltiplas ideias diluem a mensagem e confundem o comprador. A Big Idea é a tese que organiza toda a copy — ela precisa ser nova, grande, crível, relevante e proprietária, e precisa encontrar o cliente onde a consciência dele está (do inconsciente ao mais consciente). Sem este checklist verde, a copy nasce sem espinha dorsal e cada peça puxa para um lado. Ele encarna `one_big_idea`: uma tese por lançamento, com mecanismo único por trás. É o que transforma estratégia em uma frase que vende.

## Dono & Escopo
- **owner_agent:** `big-idea-architect` (entrega UMA tese; pode **vetar** múltiplas ideias, falha em qualquer dos 5 critérios, desalinho de consciência ou ausência de mecanismo).
- **Artefato inspecionado:** o `artifact.big-idea` e a `decision.big-idea-locked`, registrados no [`big-idea-registry`](../data/registries/big-idea-registry.md).

## Condição de Passagem
Exatamente UMA Big Idea está `locked`, aprovada nos 5 critérios (nova/grande/crível/relevante/proprietária), com mecanismo único por trás e casada ao nível de consciência dominante.

## Itens
1. **Exatamente UMA Big Idea.** Como verificar: o `big-idea-registry` tem uma única tese com status `locked` para este lançamento — duas ou mais reprova, conforme `power-of-one`.
2. **Critério "nova".** Como verificar: a ideia traz um ângulo que o mercado ainda não ouviu até a exaustão, conforme `big-idea-scoring`.
3. **Critério "grande".** Como verificar: a ideia é grande o bastante para sustentar uma campanha inteira, não um único anúncio.
4. **Critério "crível".** Como verificar: a ideia tem lastro — apoia-se no mecanismo único e na prova, sem soar exagero vazio.
5. **Critério "relevante".** Como verificar: a ideia toca a dor/desejo dominante do avatar, na emoção dominante mapeada no VOC.
6. **Critério "proprietária".** Como verificar: a ideia é difícil de copiar porque amarra ao mecanismo único da oferta, não a um clichê de categoria.
7. **Casa com a consciência.** Como verificar: o tipo de abordagem da ideia bate com o nível de consciência dominante (mais consciente → oferta direta; inconsciente → história/problema), conforme `meta-launch-principle`.
8. **Mecanismo por trás.** Como verificar: a Big Idea aponta para o mecanismo único registrado — promessa sem "por quê" é vetada.
9. **Promessa-gancho-vilão definidos.** Como verificar: a tese tem promessa clara, gancho de abertura e o vilão/inimigo comum nomeados, conforme `promise-hook-villain`.

## Evidência Exigida
Para marcar ✅: linkar a única linha `locked` no `big-idea-registry` (item 1), a planilha de scoring com os 5 critérios pontuados (itens 2–6), a nota de fit de consciência (item 7) e o `mechanism_id` ligado (item 8). A tríade promessa-gancho-vilão aparece no artefato da Big Idea (item 9).

## Protocolo de Falha
Item vermelho → a Big Idea volta ao `big-idea-architect` para nova rodada de ideação e **bloqueia D3→Offer Book** (HARD STOP a montante). Mais de uma tese travada, falha em um critério, desalinho de consciência ou ausência de mecanismo aciona **veto**. Re-entrada: gerar/reprovar candidatas, pontuar, travar UMA, atualizar o `big-idea-registry`, re-submeter. Mudança no mecanismo ou no mercado reabre este checklist.

## Links
- Frameworks: [`big-idea-generator`](../frameworks/big-idea-generator.md) · [`power-of-one`](../frameworks/power-of-one.md) · [`big-idea-ideation-tot`](../frameworks/big-idea-architect/big-idea-ideation-tot.md) · [`big-idea-scoring`](../frameworks/big-idea-architect/big-idea-scoring.md) · [`promise-hook-villain`](../frameworks/big-idea-architect/promise-hook-villain.md) · [`meta-launch-principle`](../frameworks/meta-launch-principle.md)
- Registries: [`big-idea-registry`](../data/registries/big-idea-registry.md)
- Agentes: [`big-idea-architect`](../agents/big-idea-architect.md) · [`positioning-lead-strategist`](../agents/positioning-lead-strategist.md) · [`mechanism-architect`](../agents/mechanism-architect.md)
- Gates por agente: [`big-idea/big-idea-single-gate`](big-idea/big-idea-single-gate.md) · [`big-idea/big-idea-new-big-credible-gate`](big-idea/big-idea-new-big-credible-gate.md) · [`big-idea/big-idea-awareness-fit-gate`](big-idea/big-idea-awareness-fit-gate.md)
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate relacionado: [`offer-book-stack/big-idea-locked-gate`](offer-book-stack/big-idea-locked-gate.md)
