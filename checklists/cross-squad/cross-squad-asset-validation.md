---
id: checklist.cross-squad.cross-squad-asset-validation
title: "Gate — Validação de Ativo Cross-Squad"
type: gate
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [proof-to-claim-chain, scarcity-urgency-engine, offer-to-funnel-mapping]
registries: [proof-registry, claim-registry, decision-registry, swipe-registry]
tags: [gate, cross-squad, asset, validation, ingestion, compliance]
---

# Gate — Validação de Ativo Cross-Squad

## Propósito
Este gate prova que **todo ativo recebido de outro squad é validado antes de entrar nos registries e ser usado**. Existe porque ativo de fora pode trazer claim sem lastro, dado sem método ou copy fora da voz — e contaminar o lançamento. Um ativo importado (sizing do data-squad, VOC do deepresearch, criativo do design/traffic, crítica do advisory) só vira insumo confiável depois de passar pelos mesmos padrões internos. Protege `evidence_before_opinion` na ingestão, conforme `config.yaml: cross_squad.*.shared_assets`.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (valida lastro e conformidade do que entra; pode **vetar**); o `knowledge-librarian` registra o ativo aceito como memória reutilizável.
- **Artefato inspecionado:** o ativo recebido de um squad vizinho — market-theses, audience-insights, pricing-science, ad-creative, strategic-review, risk-assessment, landing-pages — antes de gravar em [`proof-registry`](../../data/registries/proof-registry.md), [`claim-registry`](../../data/registries/claim-registry.md) ou [`swipe-registry`](../../data/registries/swipe-registry.md).

## Condição de Passagem
O ativo recebido tem proveniência declarada, cada claim com lastro citável, método explícito para todo número, e passa nos padrões internos de voz e escassez verdadeira — logo pode entrar nos registries.

## Itens
1. **Proveniência declarada.** Verificar: o ativo nomeia squad de origem, autor e data de produção.
2. **Lastro de claims.** Verificar: cada afirmação factual no ativo tem fonte citável; claims órfãos são sinalizados.
3. **Método dos números.** Verificar: todo dado/estatística traz o método de obtenção (amostra, instrumento, janela).
4. **Escassez verdadeira.** Verificar: se o ativo sugere escassez/urgência, ela aponta para limite real — escassez falsa = veto.
5. **Coerência com a oferta.** Verificar: o ativo não contradiz a Big Idea travada nem o mecanismo único.
6. **Padrão de voz (se for copy/criativo).** Verificar: criativo importado passa pela revisão de voz antes de uso, ou é marcado para reescrita.
7. **Licença/uso (se for swipe).** Verificar: o ativo tem direito de uso e vira padrão original, não copy literal (>25 palavras).
8. **Registro de ingestão.** Verificar: `decision_id` ou linha de registry com origem, status (aceito/rejeitado) e destino.

## Evidência Exigida
Para marcar ✅: linkar o ativo com proveniência (item 1), a tabela claim→fonte e a nota de método (itens 2–3), a checagem de escassez (item 4), a comparação com Big Idea/mecanismo (item 5), o registro de revisão de voz (item 6), a nota de licença (item 7) e a linha de ingestão no registry (item 8).

## Protocolo de Falha
Item vermelho → o `compliance-auditor` **rejeita o ativo** e o devolve ao squad de origem (via `offerbook-chief`) com o defeito nomeado; o ativo **não entra** nos registries. Claim sem lastro, número sem método ou escassez falsa é veto automático. Re-entrada: o squad de origem corrige e re-envia, ou o ativo é descartado e a lacuna vira novo pedido de pesquisa via [`cross-squad-research-request-quality`](cross-squad-research-request-quality.md). Ativo aceito é gravado pelo `knowledge-librarian`.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md)
- Registries: [`proof-registry`](../../data/registries/proof-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md) · [`swipe-registry`](../../data/registries/swipe-registry.md)
- Config: `cross_squad.*.shared_assets` (ativos compartilhados)
- Gates relacionados: [`cross-squad-handoff-quality`](cross-squad-handoff-quality.md) · [`cross-squad-research-request-quality`](cross-squad-research-request-quality.md)
- Agentes: [`compliance-auditor`](../../agents/compliance-auditor.md) · [`knowledge-librarian`](../../agents/knowledge-librarian.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
