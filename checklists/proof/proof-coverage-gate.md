---
id: checklist.proof.proof-coverage-gate
title: "Gate — Cobertura de Prova Completa por Claim e por Estágio"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
frameworks: [proof-to-claim-chain]
registries: [proof-registry, claim-registry]
tags: [gate, proof, coverage, proof-to-claim, d1, matriz, estagio]
---

# Gate — Cobertura de Prova Completa por Claim e por Estágio

## Propósito
Este gate prova que a **matriz prova × claim** está **completa** — que cada claim que a oferta fará foi enumerado e mapeado à melhor prova disponível, sem buracos silenciosos. Ele existe porque um claim que ninguém listou é um claim que ninguém provou: a copy o usará e o compliance o pegará tarde. Diferente do `proof-claim-backing-gate` (que prova que não há claim órfão nem prova órfã), este foca na **completude da enumeração e na profundidade da cobertura**: todos os claims do mecanismo e do resultado estão na matriz, cada um tem prova principal **e** reforço quando a severidade pede, e a taxa de cobertura (claims com prova / claims totais) é conhecida e reportada como KPI (`proof_coverage_rate`). Ele também garante que a cobertura respeita o estágio de sofisticação: nos estágios 3–4, claims de mecanismo não podem ficar cobertos só por prova de resultado. É o gate que transforma "temos provas" em "cada claim tem a prova certa, e sabemos quanto falta".

## Dono & Escopo
- **owner_agent:** `proof-credibility-curator` (inventaria e casa prova a claim; sem veto, sinaliza ao chief/compliance).
- **Artefato inspecionado:** a **matriz prova × claim** completa e a **taxa de cobertura**, com os claims no [`claim-registry`](../../data/registries/claim-registry.md) e as provas no [`proof-registry`](../../data/registries/proof-registry.md).

## Condição de Passagem
Todos os claims da oferta estão enumerados na matriz, cada um com prova de força adequada ao estágio, e a taxa de cobertura é conhecida com os gaps reportados.

## Itens
1. **Claims enumerados por inteiro.** Verificar: todo claim do mecanismo e do resultado que a oferta fará está listado na matriz — nenhum claim implícito fora dela.
2. **Prova principal por claim.** Verificar: cada claim enumerado tem uma prova principal designada (a munição mais forte e segura disponível).
3. **Reforço onde a severidade pede.** Verificar: claims de alta severidade ou alta exposição têm ≥1 prova de reforço além da principal.
4. **Cobertura por estágio.** Verificar: aplicado [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md), claims de mecanismo (estágio 3–4) estão cobertos por prova de mecanismo, não só de resultado.
5. **Taxa de cobertura conhecida.** Verificar: `proof_coverage_rate` (claims com prova adequada / claims totais) está calculada e registrada.
6. **Gaps de cobertura priorizados.** Verificar: claims sem prova adequada estão listados no proof-gap-report, ordenados por severidade.
7. **Sem cobertura provisória silenciosa.** Verificar: onde a cobertura é "provisória" (mapa de objeções incompleto), isso está explicitamente marcado, não escondido.

## Evidência Exigida
Para marcar cada item ✅, linkar a matriz prova × claim completa (lista de todos os claims com prova principal + reforços), o [`claim-registry`](../../data/registries/claim-registry.md) com cada claim e sua(s) prova(s), e o valor calculado de `proof_coverage_rate`. O proof-gap-report ordenado por severidade e a marcação explícita de qualquer cobertura provisória são a evidência-resumo de que nada ficou coberto por omissão.

## Protocolo de Falha
Item vermelho → não declara verde. Claim não enumerado → adiciona à matriz e busca prova. Claim sem prova principal → busca a munição mais forte disponível ou abre gap. Cobertura só de resultado num estágio que exige mecanismo → busca prova de mecanismo/comparativa ou abre gap para o [`mechanism-architect`](../../agents/mechanism-architect.md). Taxa de cobertura desconhecida → calcula antes de fechar. Cobertura provisória escondida → marca como provisória e sinaliza ao [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) que o mapa de objeções precisa ser completado. O curador **não tem veto**: gaps de alta severidade são sinalizados ao [`offerbook-chief`](../../agents/offerbook-chief.md) e ao [`compliance-auditor`](../../agents/compliance-auditor.md). Re-entrada: completada a cobertura, o gate é re-submetido.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`proof-registry`](../../data/registries/proof-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md)
- Agentes: [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`mechanism-architect`](../../agents/mechanism-architect.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md)
- Gate-âncora: [`proof-claim-backing-gate`](proof-claim-backing-gate.md)
- Gates irmãos: [`proof-objection-coverage-gate`](proof-objection-coverage-gate.md) · [`proof-source-credibility-gate`](proof-source-credibility-gate.md) · [`proof-permission-gate`](proof-permission-gate.md)
- Template: [`proof-bank-template`](../../templates/strategy/proof-bank-template.md)
