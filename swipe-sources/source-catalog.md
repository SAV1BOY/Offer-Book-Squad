---
id: swipe-source.source-catalog
title: "Catálogo de Fontes de Swipe (externas + internas)"
type: swipe-source
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Swiped.co — biblioteca pública de anúncios e cartas anotados — https://swiped.co"
  - "Swipefile.com — coleção de exemplos de copy e marketing — https://swipefile.com"
  - "Swipewell.app — ferramenta de captura/organização de swipe — https://swipewell.app"
  - "Really Good Emails — galeria de e-mails de marketing — https://reallygoodemails.com"
tags: [swipe-source, catalog, provenance, sources, legal]
---

# Catálogo de Fontes de Swipe

Este é o **manifesto de proveniência** do swipe do squad: a lista única de fontes de onde extraímos **estrutura, anatomia e princípios** — nunca copy protegida. Toda entrada em [`swipe/`](../swipe/) aponta, no bloco `## Fonte`, para uma fonte registrada aqui. Pareia com [`provenance-rules`](provenance-rules.md), [`usage-license`](usage-license.md) e [`attribution-log`](attribution-log.md). A regra-mãe está em [`../swipe.config`](../swipe.config) e em [`../docs/style-guide.md`](../docs/style-guide.md): guardamos `structure, anatomy, principles, original-patterns, links`; proibimos `pasted-copyrighted-copy, full-ad-reproduction`.

## O que catalogamos
Catalogamos a **fonte**, não o ativo. Para cada fonte registramos: o tipo de material, o que dela é lícito extrair, o que jamais copiamos, e o nível de confiança da atribuição. Um teardown nomeado (campanha específica) vive em [`../reference/swipe-breakdowns/`](../reference/swipe-breakdowns/); um padrão **original e reutilizável** vive em [`../swipe/`](../swipe/). Este catálogo é a ponte entre os dois e a auditoria de onde cada ideia nasceu.

## Fontes externas

| Fonte | Tipo de material | O que extraímos | O que NUNCA copiamos | Confiança |
|---|---|---|---|---|
| **Swiped.co** | Anúncios e cartas históricas anotados | Estrutura de carta, sequência de beats, função de cada bloco | Texto literal da carta/anúncio | Alta (anotado, datado) |
| **Swipefile.com** | Exemplos diversos de copy/marketing | Padrões de manchete, ângulos, arquétipos de oferta | Copy completa de campanha | Média (curadoria variável) |
| **Swipewell.app** | Capturas organizadas pelo usuário | Taxonomia de categorias, modos de organizar swipe | Ativos de terceiros capturados | Média (depende da captura) |
| **Really Good Emails** | Galeria de e-mails de marketing | Estrutura de e-mail, hierarquia visual, padrões de subject | HTML/copy/arte do e-mail original | Alta (fonte primária visível) |

Cada fonte externa entra no swipe **só** como destilação estrutural. Quando uma campanha nomeada merece teardown, ela recebe uma entrada em `reference/swipe-breakdowns/` e um registro no [`attribution-log`](attribution-log.md).

## Fontes internas

| Fonte | Caminho | O que vira swipe | Dono |
|---|---|---|---|
| **Controles vencedores próprios** | [`../data/winners`](../data/winners) | Estrutura de peças que bateram metas internas (sem PII) | `knowledge-librarian` |
| **Registro de controles** | [`../data/controls`](../data/controls) | Padrões dos campeões que sobreviveram a teste | `knowledge-librarian` |
| **Testes & decisões** | [`../data/decisions`](../data/decisions) | Aprendizados que sustentam o "por que funciona" | `knowledge-librarian` |

Fontes internas têm prioridade: um padrão provado pelos **nossos próprios dados** é mais confiável que um exemplo externo. Ainda assim, abstraímos a estrutura e removemos qualquer dado sensível antes de publicar em `swipe/`.

## Como o squad usa
- `knowledge-librarian`: dono do catálogo; registra fonte nova antes de qualquer padrão citá-la; mantém o [`attribution-log`](attribution-log.md) sincronizado.
- `compliance-auditor`: audita que todo padrão em `swipe/` cita uma fonte daqui e respeita o teto literal de 25 palavras; **veta** entrada sem proveniência.
- Agentes de copy (D4): consultam o swipe ligado a este catálogo como ponto de partida estrutural, jamais como texto a colar.

**Armadilha:** registrar um "exemplo" colando a copy original. Catalogue a **fonte** e destile a **estrutura** — o ativo de terceiros nunca entra no repositório.

## Fonte
> **Fonte:** Swiped.co, Swipefile.com, Swipewell.app, Really Good Emails (fontes externas de swipe, acessadas 2026-06-02); fontes internas em [`../data/winners`](../data/winners) e [`../data/controls`](../data/controls).
> **Anti-verbatim:** catalogamos a origem e extraímos estrutura/princípios em redação original. Nenhuma copy de terceiros reproduzida; citação literal ≤ 25 palavras, atribuída.
