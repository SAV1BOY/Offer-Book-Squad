---
id: swipe-source.usage-license
title: "Licença de Uso do Swipe (o que pode e o que não pode)"
type: swipe-source
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Offer Book Squad — swipe.config (rules: store/forbid), via ../swipe.config"
  - "Offer Book Squad — docs/compliance-policy.md (política anti-plágio), via ../docs/compliance-policy.md"
tags: [swipe-source, license, usage, fair-use, compliance, legal]
---

# Licença de Uso do Swipe

Este documento define **como o squad pode usar** o material catalogado em [`source-catalog`](source-catalog.md) e tudo o que vira padrão em [`../swipe/`](../swipe/). Ele não é aviso jurídico; é a **política interna de uso** que torna o swipe seguro e reutilizável. A regra-mãe vem de [`../swipe.config`](../swipe.config) e de [`../docs/style-guide.md`](../docs/style-guide.md): o squad licencia para si **estrutura, anatomia, princípios e padrões originais** — nunca a copy protegida de terceiros. Pareia com [`provenance-rules`](provenance-rules.md) e [`attribution-log`](attribution-log.md).

## O princípio: licenciamos ideias, não palavras
Estrutura e método não são protegidos por direito autoral — a **expressão** (as palavras exatas) é. Por isso o squad pode estudar e remontar a *anatomia* de qualquer peça do mundo, desde que escreva o resultado em redação própria. O que cruza a linha é colar a frase, o parágrafo ou o anúncio de outro. Esta licença existe para manter cada arquivo do lado seguro dessa linha.

## Usos permitidos
- **Destilar a estrutura** de uma peça pública (a ordem dos blocos, a função de cada beat) e descrevê-la com nossas palavras.
- **Nomear o princípio** que faz a peça funcionar, atribuído ao autor/fonte (Schwartz, Cialdini, Hormozi…).
- **Criar um padrão original** com `{{placeholders}}` que qualquer agente preenche com a voz da marca.
- **Citar literalmente até 25 palavras**, entre aspas e com fonte ao lado, só quando necessário para nomear um conceito.
- **Usar dados internos** de [`../data/winners`](../data/winners) e [`../data/controls`](../data/controls) depois de remover PII e números sensíveis.

## Usos proibidos
- **Colar copy de terceiros** — qualquer frase, manchete ou parágrafo transcrito acima do teto literal.
- **Reproduzir um anúncio/carta/e-mail inteiro**, mesmo "como referência" ou "para estudo".
- **Encadear citações curtas** para reconstruir um trecho longo (cópia fatiada).
- **Republicar ativos de marca** — arte, HTML, fontes, áudio, logotipos de terceiros.
- **Revender ou redistribuir** o material-fonte de plataformas como [Swiped.co](source-catalog.md) ou [Really Good Emails](source-catalog.md) — consultamos, não redistribuímos.
- **Expor dados sob NDA** ou qualquer informação de cliente identificável.

## Atribuição obrigatória
Todo padrão em `swipe/` carrega um bloco `## Fonte` apontando para a fonte registrada no catálogo, e toda campanha nomeada gera uma linha no [`attribution-log`](attribution-log.md). Sem atribuição rastreável, o padrão não passa no `compliance-auditor`. A atribuição é a prova de que estudamos a estrutura de uma origem real, não inventamos um número ou copiamos no escuro.

## Validade e revisão
Esta licença vale para todo o `swipe/` e é revisada quando uma fonte muda seus termos ou quando a [`../docs/compliance-policy.md`](../docs/compliance-policy.md) é atualizada. Em conflito entre esta licença e os termos de uma plataforma-fonte, **prevalece o mais restritivo**. Na dúvida, o `compliance-auditor` decide e pode vetar.

## Como o squad usa
- `knowledge-librarian`: aplica a licença ao curar swipe; recusa material que só existe como copy colada.
- `compliance-auditor`: última barreira — confere atribuição, teto literal e ausência de ativo de terceiros; **veta** o que violar.
- Agentes de copy (D4): tratam todo swipe como **andaime estrutural** licenciado, preenchendo `{{...}}` com voz própria.

**Armadilha:** assumir que "está num site de swipe, então posso copiar". O site cataloga exemplos; o direito autoral da copy continua do autor. Licencie a **estrutura**, escreva o **texto**.

## Fonte
> **Fonte:** Offer Book Squad — [`../swipe.config`](../swipe.config) (regras store/forbid) e [`../docs/style-guide.md`](../docs/style-guide.md) / [`../docs/compliance-policy.md`](../docs/compliance-policy.md) (política anti-plágio). Acesso 2026-06-02.
> **Anti-verbatim:** política descrita em redação original. Nenhuma copy de terceiros reproduzida; citação literal ≤ 25 palavras, atribuída.
