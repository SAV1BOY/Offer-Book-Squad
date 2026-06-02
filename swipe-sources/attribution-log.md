---
id: swipe-source.attribution-log
title: "Log de Atribuição do Swipe (rastro de proveniência)"
type: swipe-source
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Offer Book Squad — source-catalog.md (fontes registradas), via source-catalog.md"
  - "Offer Book Squad — reference/swipe-breakdowns/ (teardowns nomeados), via ../reference/swipe-breakdowns/"
tags: [swipe-source, attribution, log, provenance, audit, registry]
---

# Log de Atribuição do Swipe

Este é o **rastro auditável** de onde cada ideia do swipe nasceu. Para cada campanha nomeada que estudamos, registramos a fonte, o que foi extraído (sempre **estrutura/princípio**, nunca copy) e onde o padrão derivado vive. É a ponte de auditoria entre o [`source-catalog`](source-catalog.md), as [`provenance-rules`](provenance-rules.md), a [`usage-license`](usage-license.md) e os arquivos de [`../swipe/`](../swipe/) e [`../reference/swipe-breakdowns/`](../reference/swipe-breakdowns/). O `compliance-auditor` consulta este log para confirmar que todo padrão tem origem declarada.

## Schema do log
Cada linha registra uma **fonte estudada** e o destino do que dela extraímos. Campos:

- **fonte** — campanha/autor/plataforma de origem (link para o catálogo ou o teardown).
- **tipo** — externa (plataforma/campanha pública) ou interna (nossos controles).
- **extraído** — o que foi destilado: estrutura, anatomia, princípio (nunca "copy").
- **destino** — o arquivo de swipe ou teardown que carrega a destilação.
- **confiança** — alta/média (qualidade e datação da fonte).
- **data** — quando foi registrado (ISO).

## Registros

| Fonte | Tipo | Extraído | Destino | Confiança | Data |
|---|---|---|---|---|---|
| Lançamento $100M Money Models (Hormozi, 2025) | Externa | Estrutura econômica e sequencial de lançamento (atração→upsell→continuidade) | [`../reference/swipe-breakdowns/hormozi-100m-money-models-launch.md`](../reference/swipe-breakdowns/hormozi-100m-money-models-launch.md) | Alta | 2026-06-02 |
| Perfect Webinar (Brunson) | Externa | Sequência de quebra de crença + fechamento empilhado (estrutura) | [`../reference/swipe-breakdowns/brunson-perfect-webinar-structure.md`](../reference/swipe-breakdowns/brunson-perfect-webinar-structure.md) | Alta | 2026-06-02 |
| Carta "Two Young Men" do WSJ (Conroy) | Externa | Anatomia de carta-controle de resposta direta | [`../reference/swipe-breakdowns/classic-direct-mail-controls.md`](../reference/swipe-breakdowns/classic-direct-mail-controls.md) | Alta | 2026-06-02 |
| "Coat of Arms Letter" (Halbert) | Externa | Lead de identidade + personalização (estrutura) | [`../reference/swipe-breakdowns/halbert-style-personal-letter.md`](../reference/swipe-breakdowns/halbert-style-personal-letter.md) | Alta | 2026-06-02 |
| Convenção de VSL de nutracêutico | Externa | Anatomia "causa-raiz oculta"→ingrediente→oferta | [`../reference/swipe-breakdowns/supplement-vsl-anatomy.md`](../reference/swipe-breakdowns/supplement-vsl-anatomy.md) | Média | 2026-06-02 |
| Sequência de lançamento de info-produto | Externa | Arco de e-mail (pré-lançamento→carrinho→objeções→fechamento) | [`../reference/swipe-breakdowns/info-product-launch-email-sequence.md`](../reference/swipe-breakdowns/info-product-launch-email-sequence.md) | Média | 2026-06-02 |
| Swiped.co (biblioteca anotada) | Externa | Estrutura de cartas/anúncios históricos | [`source-catalog.md`](source-catalog.md) | Alta | 2026-06-02 |
| Really Good Emails (galeria) | Externa | Estrutura e hierarquia visual de e-mail | [`source-catalog.md`](source-catalog.md) | Alta | 2026-06-02 |
| Controles vencedores próprios | Interna | Estrutura de peças que bateram metas (sem PII) | [`../data/winners`](../data/winners) | Alta | 2026-06-02 |

A tabela cresce a cada nova fonte estudada. **Nenhuma linha** referencia copy literal — só estrutura, anatomia ou princípio, com o arquivo de destino que a parafraseia em redação original.

## Procedimento de registro
1. **Antes** de criar um padrão ou teardown, registre a fonte aqui (ou confirme que já está).
2. Preencha **extraído** com a natureza estrutural do que será destilado — se você não consegue descrever sem colar texto, **pare**.
3. Aponte o **destino** para o arquivo que carregará a destilação.
4. Marque a **confiança** pela datação/curadoria da fonte.
5. O `compliance-auditor` confere a linha contra o arquivo de destino na auditoria de D7.

## Como o squad usa
- `knowledge-librarian`: dono do log; adiciona a linha antes de qualquer padrão citar a fonte; mantém sincronia com o [`source-catalog`](source-catalog.md).
- `compliance-auditor`: cruza cada `## Fonte` do swipe com este log; **veta** padrão cuja origem não esteja registrada.
- Sessões futuras: leem o log para entender de onde veio cada ideia sem reabrir a fonte.

**Armadilha:** registrar a fonte mas esquecer de checar que o destino parafraseou — atribuição sem paráfrase ainda é cópia. O log prova a origem; o arquivo prova a redação original.

## Fonte
> **Fonte:** Offer Book Squad — [`source-catalog.md`](source-catalog.md) (fontes registradas) e [`../reference/swipe-breakdowns/`](../reference/swipe-breakdowns/) (teardowns nomeados). Acesso 2026-06-02.
> **Anti-verbatim:** log e procedimento em redação original. Nenhuma copy de terceiros reproduzida; citação literal ≤ 25 palavras, atribuída.
