---
id: checklist.mechanism-checklist
title: "Checklist — Mecanismo Único (nomeado + provado em 1 frase)"
type: checklist
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
frameworks: [unique-mechanism, value-equation]
registries: [offer-registry, proof-registry]
tags: [checklist, mecanismo, unique-mechanism, naming, prova, d2]
---

# Checklist — Mecanismo Único

## Propósito
Este checklist prova que a oferta tem um **mecanismo único nomeado e provado** — a explicação de *por que* ela funciona quando tudo o que o cliente tentou antes falhou. Existe porque em mercados sofisticados a promessa sozinha não convence: o comprador já ouviu a promessa e não acreditou. O mecanismo é o "porquê" novo que reabre a crença. Sem nome próprio, ele não gruda; sem prova, ele não convence; sem caber em uma frase, ele não comunica. Sem este checklist verde, a Big Idea e a copy ficam sem lastro de "por quê". Ele encarna a lição de Schwartz sobre sofisticação: quando o mercado descrê da promessa, vence quem traz o mecanismo novo e crível.

## Dono & Escopo
- **owner_agent:** `mechanism-architect` (isola e nomeia o mecanismo único da oferta).
- **Artefato inspecionado:** o `artifact.mechanism-sheet` e a `decision.mechanism-name`, registrados no [`offer-registry`](../data/registries/offer-registry.md), com a prova vinda do [`proof-registry`](../data/registries/proof-registry.md).

## Condição de Passagem
O mecanismo tem nome próprio, descreve-se em UMA frase clara e tem ≥1 prova ligada ao porquê ele funciona — casado ao nível de sofisticação do mercado.

## Itens
1. **Nome próprio do mecanismo.** Como verificar: o mecanismo tem um nome único e memorável no `offer-registry`, não um termo genérico de categoria.
2. **Descrição em UMA frase.** Como verificar: ler a frase — explica o porquê a oferta funciona em uma linha, nível 3ª série, sem jargão.
3. **Mecanismo provado.** Como verificar: ≥1 `proof_id` no `proof-registry` sustenta a alegação de que o mecanismo causa o resultado.
4. **Casa com a sofisticação.** Como verificar: o grau de novidade do mecanismo bate com o nível de sofisticação declarado do mercado, conforme `unique-mechanism`.
5. **Conecta dor → resultado.** Como verificar: o mecanismo liga a dor dominante do avatar ao resultado prometido, sem salto lógico.
6. **Diferencia da concorrência.** Como verificar: a frase do mecanismo deixa claro o que ele faz de diferente do que o mercado já tentou.
7. **Move alavanca de valor.** Como verificar: o mecanismo eleva ≥1 alavanca da `value-equation` (sobe probabilidade percebida ou reduz tempo/esforço).
8. **Sem promessa órfã.** Como verificar: o mecanismo não infla o sonho sem sustentar a probabilidade — não há "milagre" sem o "como".

## Evidência Exigida
Para marcar ✅: linkar a linha do `offer-registry` com o nome e a frase única do mecanismo (itens 1–2), o `proof_id` que o sustenta no `proof-registry` (item 3) e a nota de fit de sofisticação (item 4). A ligação dor→resultado e a alavanca de valor movida aparecem no mechanism-sheet (itens 5–7).

## Protocolo de Falha
Item vermelho → o mecanismo volta ao `mechanism-architect` com o defeito nomeado e **bloqueia D2→D3** (Big Idea não nasce sem mecanismo). Mecanismo sem prova volta a pedir prova ao `proof-credibility-curator`; mecanismo que não move alavanca é reprovado pelo `value-equation-engineer`. Re-entrada: renomear/reprovar, anexar prova, atualizar o `offer-registry`, re-submeter. Mudança de mercado-alvo reabre este checklist.

## Links
- Frameworks: [`unique-mechanism`](../frameworks/unique-mechanism.md) · [`value-equation`](../frameworks/value-equation.md)
- Registries: [`offer-registry`](../data/registries/offer-registry.md) · [`proof-registry`](../data/registries/proof-registry.md)
- Agentes: [`mechanism-architect`](../agents/mechanism-architect.md) · [`proof-credibility-curator`](../agents/proof-credibility-curator.md) · [`value-equation-engineer`](../agents/value-equation-engineer.md)
- Gates por agente: [`mechanism/mechanism-naming-gate`](mechanism/mechanism-naming-gate.md) · [`mechanism/mechanism-proof-gate`](mechanism/mechanism-proof-gate.md) · [`mechanism/mechanism-one-sentence-gate`](mechanism/mechanism-one-sentence-gate.md)
- Agrega para: [`offer-book-checklist`](offer-book-checklist.md) · Gate relacionado: [`offer-book-stack/offer-architecture-gate`](offer-book-stack/offer-architecture-gate.md)
