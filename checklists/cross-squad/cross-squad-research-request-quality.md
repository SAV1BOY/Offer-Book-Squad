---
id: checklist.cross-squad.cross-squad-research-request-quality
title: "Gate — Qualidade do Pedido de Pesquisa Cross-Squad"
type: gate
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
frameworks: [awareness-x-sophistication, starving-crowd, proof-to-claim-chain]
registries: [decision-registry, offer-registry, proof-registry]
tags: [gate, cross-squad, research, request, deepresearch, intake]
---

# Gate — Qualidade do Pedido de Pesquisa Cross-Squad

## Propósito
Este gate prova que **todo pedido de pesquisa enviado a outro squad (tipicamente o deepresearch-squad) é específico, respondível e útil para uma decisão**. Existe porque pesquisa mal pedida volta genérica e cara: "estude o mercado" não move nada; "qual o nível de sofisticação do mercado X e os 3 concorrentes de referência" move o `market-sophistication-gate`. Cada pedido precisa nomear a decisão que vai destravar. Protege `decision_before_ornament` na fronteira de inteligência, conforme `config.yaml: cross_squad.deepresearch_squad`.

## Dono & Escopo
- **owner_agent:** `offerbook-chief` (aprova o que sai como pedido); o `market-sophistication-analyst` e o `avatar-voc-investigator` formulam a pergunta técnica.
- **Artefato inspecionado:** o pedido de pesquisa enviado ao deepresearch-squad (ou a outro squad de dados), registrado no [`decision-registry`](../../data/registries/decision-registry.md) com o retorno esperado em `data/research`.

## Condição de Passagem
O pedido nomeia a decisão que destrava, faz perguntas específicas e respondíveis, define o formato e a fonte aceitável de retorno, e tem prazo — logo o squad de pesquisa pode entregar algo acionável.

## Itens
1. **Decisão-alvo nomeada.** Verificar: o pedido declara qual decisão (sofisticação, avatar, pricing, concorrente) será destravada pela resposta.
2. **Perguntas específicas.** Verificar: cada pergunta é fechada ou mensurável, não "fale sobre"; ≥1 critério de resposta por pergunta.
3. **Escopo delimitado.** Verificar: mercado, geografia, segmento e janela de tempo da pesquisa estão definidos.
4. **Formato de retorno definido.** Verificar: o pedido diz como quer a resposta (verbatims com fonte, sizing com método, tabela competitiva).
5. **Fonte aceitável declarada.** Verificar: o pedido define o padrão de evidência (primária, citável) para o retorno entrar no `proof-registry`.
6. **Prazo e prioridade.** Verificar: data-limite e prioridade explícitas.
7. **Pedido registrado.** Verificar: `decision_id` com o pedido, o destinatário e o retorno esperado.

## Evidência Exigida
Para marcar ✅: linkar o documento do pedido com a decisão-alvo (item 1), a lista de perguntas com critério de resposta (item 2), o escopo delimitado (item 3), a especificação de formato e fonte (itens 4–5), o prazo (item 6) e o `decision_id` (item 7).

## Protocolo de Falha
Item vermelho → o `offerbook-chief` **não envia o pedido** e devolve ao analista de origem para reformular a pergunta com a decisão-alvo e o critério de resposta. Pedido genérico ou sem decisão associada é reprovado. Re-entrada: reescrever as perguntas como fechadas/mensuráveis, definir formato e fonte, registrar e re-submeter. Retorno que não atende ao formato/fonte aciona o [`cross-squad-asset-validation`](cross-squad-asset-validation.md) antes de entrar nos registries.

## Links
- Frameworks: [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`starving-crowd`](../../frameworks/starving-crowd.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md)
- Config: `cross_squad.deepresearch_squad` (handoff_from_research)
- Gates relacionados: [`cross-squad-handoff-quality`](cross-squad-handoff-quality.md) · [`cross-squad-asset-validation`](cross-squad-asset-validation.md)
- Agentes: [`offerbook-chief`](../../agents/offerbook-chief.md) · [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md)
