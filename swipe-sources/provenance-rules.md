---
id: swipe-source.provenance-rules
title: "Regras de Proveniência do Swipe (anti-plágio)"
type: swipe-source
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
sources:
  - "Offer Book Squad — swipe.config (rules: anti-plágio), via ../swipe.config"
  - "Offer Book Squad — docs/style-guide.md (bloco de citação; 4g swipe), via ../docs/style-guide.md"
tags: [swipe-source, provenance, anti-plagiarism, rules, compliance]
---

# Regras de Proveniência do Swipe

Este é o **contrato anti-plágio** que todo arquivo em [`swipe/`](../swipe/) obedece. Ele transforma a regra de [`../swipe.config`](../swipe.config) em procedimento verificável e é aplicado por `scripts/citation-checker.py` e pelo `compliance-auditor`. A lei única: **guardamos estrutura, anatomia, princípios, padrões originais e links — nunca copy protegida colada.** Pareia com o [`source-catalog`](source-catalog.md), a [`usage-license`](usage-license.md) e o [`attribution-log`](attribution-log.md).

## O que pode entrar (store)
- **Estrutura** — a ordem dos blocos de uma peça (lead → corpo → oferta → close).
- **Anatomia** — os beats e a função de cada um (o "trabalho" de cada parte).
- **Princípios** — por que funciona, mapeado a frameworks/reference nomeados.
- **Padrões originais** — esqueletos reutilizáveis escritos **por nós**, com `{{placeholders}}`.
- **Links** — para a fonte, os frameworks e os agentes que usam o padrão.

## O que NUNCA entra (forbid)
- **Copy protegida colada** — frases, parágrafos ou headlines de terceiros transcritos.
- **Reprodução integral de anúncio/carta/e-mail** — ainda que "como exemplo".
- **Ativos de marca** — arte, HTML, imagens ou áudio de terceiros.
- **Dados sensíveis internos** — PII, números de cliente, qualquer coisa sob NDA.

## Regra do literal (≤ 25 palavras)
Citação literal só é permitida quando **curta, atribuída e necessária** para nomear um conceito — **no máximo 25 palavras**, entre aspas, com a fonte ao lado. Acima disso, **parafraseie**. Nunca encadeie várias citações de 25 palavras para reconstruir um trecho longo (isso é cópia fatiada e está proibido).

## Requisitos por entrada (every_entry_requires)
Todo padrão em `swipe/` precisa, sem exceção, de:
1. **`source`** — proveniência registrada no [`source-catalog`](source-catalog.md).
2. **`structural-breakdown`** — a seção `## Anatomia` (beats/estrutura).
3. **`why-it-works`** — a seção `## Por que funciona`, citando framework/reference.
4. **`reusable-pattern`** — a seção `## Padrão reutilizável`, redação original com `{{...}}`.

Faltando qualquer um, o `compliance-auditor` **veta** a publicação.

## Procedimento de destilação (como transformar fonte em swipe)
1. **Leia a peça-fonte**; identifique a função de cada bloco (não o texto).
2. **Escreva a anatomia** em palavras nossas — beats, ordem, propósito.
3. **Mapeie o "por que"** a princípios nomeados (Cialdini, Schwartz, Value Equation…).
4. **Abstraia o esqueleto** em um padrão `{{placeholder}}` que sirva a qualquer nicho.
5. **Registre a fonte** no catálogo e a atribuição no log.
6. **Rode o checker**: estrutura presente, zero copy colada, literal ≤ 25 palavras.

## Como o squad usa
- `knowledge-librarian`: aplica este procedimento ao criar/curar qualquer swipe.
- `compliance-auditor`: última barreira — reprova entrada sem as 4 exigências ou com literal acima do teto.
- Agentes de copy: tratam o swipe como **andaime estrutural**, preenchendo os `{{...}}` com a voz da marca, nunca colando a fonte.

**Armadilha:** "inspirar-se" tão de perto que a paráfrase vira a frase original com sinônimos. Reescreva a partir da **função**, não da redação.

## Fonte
> **Fonte:** Offer Book Squad — [`../swipe.config`](../swipe.config) (regras anti-plágio) e [`../docs/style-guide.md`](../docs/style-guide.md) (bloco de citação, template 4g swipe). Acesso 2026-06-02.
> **Anti-verbatim:** regras descritas em redação original. Nenhuma copy de terceiros reproduzida; citação literal ≤ 25 palavras, atribuída.
