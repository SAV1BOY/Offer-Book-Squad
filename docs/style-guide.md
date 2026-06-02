---
id: doc.style-guide
title: "Guia de Estilo & Templates por Tipo de Arquivo"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
tags: [conventions, templates, voice, dod, citation]
---

# Guia de Estilo & Templates por Tipo de Arquivo

Define **como escrever** (voz) e **a estrutura obrigatória** de cada tipo de arquivo. O `scripts/scaffold.py` gera o esqueleto conformante; o `scripts/qa-runner.py` valida seções e pisos de palavras. Ver também [`ARCHITECTURE.md`](../ARCHITECTURE.md) (frontmatter, ids, DoD) e [`agent-prompt-spec.md`](agent-prompt-spec.md) (agentes).

---

## 1. Voz padrão (perfil `brand-default-hormozi-style`)
- **Nível de leitura ~3ª série:** frases curtas, uma vírgula no máximo.
- **Voz ativa, tempo presente.** Linguagem **positiva**.
- **Sem advérbios floreados, sem redundância, sem jargão** desnecessário.
- **Concreto > abstrato:** número, exemplo, prova. "Mostre", não "diga".
- O `voice-style-guardian` fiscaliza tudo em D4. Detalhes em [`voice/`](../voice/) e [`do-not-say`](../voice/do-not-say.md).

## 2. Pisos de palavras (qa-runner)
| Tipo | Piso | | Tipo | Piso |
|---|---|---|---|---|
| agent | 1200 | | template | 250 |
| framework | 500 | | workflow | 300 |
| reference | 400 | | swipe | 200 |
| task | 350 | | voice/phrases | 200 |
| checklist/gate | 150 | | registry/lib/doc | conforme tipo |

## 3. Bloco de citação (reference/, frameworks/reference-intellectual/, swipe-*)
```md
> **Fonte:** Autor, *Título* (Ano), cap./pp. — via <URL>, acesso 2026-06-02.
> **Anti-verbatim:** estrutura/princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
```

---

## 4. Templates por tipo (seções `##` obrigatórias)

### 4a. Checklist / Gate (`type: checklist | gate`)
```
## Propósito          — o que este gate prova; por que existe.
## Dono & Escopo      — owner_agent; qual artefato inspeciona.
## Condição de Passagem — uma frase (o gate é nomeado por ela).
## Itens              — numerados; cada um binário e testável + "como verificar".
## Evidência Exigida  — o que linkar para marcar cada item ✅.
## Protocolo de Falha — o que acontece no fail (quem corrige, ponto de re-entrada).
## Links              — frameworks/registries consultados.
```
Gates por agente: exatamente **5** por subpasta, nomeados `*-gate.md`.

### 4b. Framework (`type: framework`)
```
## TL;DR              — 2–3 frases: o que é, quando vence.
## Quando usar / Quando não — critério de decisão, fit por sofisticação.
## Inputs             — o que você precisa antes de aplicar.
## Procedimento       — passos numerados, concretos, executáveis.
## Outputs            — o que produz; formato.
## Exemplo            — uma passada completa numa oferta de amostra.
## Armadilhas         — modos de falha + correção.
## Interações         — quais agentes usam; quais frameworks pareiam.
## Fontes             — bloco de citação (obrigatório em reference-intellectual/).
```

### 4c. Reference / Livro (`type: reference`)
```
## Citação            — bloco estruturado (autor, título, ano, ed., locator).
## Tese central       — o argumento do livro em palavras nossas.
## Frameworks/Modelos — cada modelo nomeado + como NÓS operacionalizamos (link p/ framework).
## Princípios         — bullets parafraseados (citação literal ≤ 25 palavras).
## Como o squad usa   — quais agentes/frameworks citam e por quê.
## Cross-refs         — outros reference, swipe-breakdowns.
```

### 4d. Template (`type: template`) — `.md` e `.csv`
`.md`:
```
## Como usar          — qual agente, qual task, quando.
## Campos & Instruções — cada placeholder {{ASSIM}} explicado.
## O Template         — bloco fenced com {{PLACEHOLDERS}} pronto p/ copiar.
## Exemplo preenchido — o mesmo template completo numa oferta de amostra.
## DoD do entregável  — quando o template preenchido está "pronto".
```
`.csv`: primeira linha = header `snake_case`; um `.md` irmão de mesmo nome documenta o schema (uma linha por coluna: nome, tipo, valores, agente-fonte, exemplo). O CSV fica **limpo** (sem comentário).

### 4e. Task (`type: task`)
```
## Objetivo           — uma frase; o estado-pronto.
## Agente dono        — quem executa.
## Gatilho / Quando   — ativação no workflow.
## Inputs (Consome)   — artefatos + registries lidos.
## Procedimento       — passos executáveis numerados (o runbook).
## Frameworks         — ids.
## Outputs (Produz)   — artefatos escritos, registries atualizados.
## Definition of Done — critério testável.
## Gates              — ids de checklist/gate.
## Handoff            — próxima task/agente + o contrato.
```

### 4f. Workflow (`type: workflow`)
```
## Objetivo           — o resultado ponta-a-ponta.
## Gatilho            — o que inicia.
## Agentes            — lista ordenada.
## Mapa de Estágios   — tabela: estágio → agente → task ids → gates → outputs.
## Diagrama           — ASCII/mermaid dos handoffs.
## Pontos de Decisão  — condições de ramificação.
## Critério de Saída  — quando completa (todos os gates verdes).
## Falha/Rollback     — pontos de re-entrada.
```

### 4g. Swipe (`type: swipe`) & Swipe-source (`type: swipe-source`)
Swipe:
```
## O que é            — tipo de artefato, arquétipo-fonte (sem copy literal).
## Anatomia           — o esqueleto/beats/sequência que faz funcionar (ESTRUTURA).
## Por que funciona   — mapeado a princípios nomeados (cita framework/reference).
## Padrão reutilizável — template abstraído, redação ORIGINAL.
## Adaptação          — como ajustar por estágio de sofisticação.
## Fonte              — bloco de citação (proveniência).
```
Swipe-source: índice/manifesto de proveniência e regras de uso/licença.

### 4h. Voice profile (`type: voice`) & Phrases (`type: phrases`)
Voice profile: `## Identidade · ## Diais de Tom (1–5) · ## Léxico (usar/banir) · ## Cadência & Sintaxe · ## Exemplos Faz/Não-faz · ## Notas de Compliance`.
Phrases: bancos de frases **originais** agrupados por função; cada grupo marca o princípio que dispara.

### 4i. Registry (`type: registry`, `.md` com tabela ou bloco de schema)
```
## Propósito · ## Schema (campos, tipos, valores) · ## Quem escreve / lê
## Registros — tabela (semeada vazia ou com exemplo). 
```
Os 10: offer, claim, proof, objection, price-test, big-idea, swipe, control, decision, lessons-learned.

### 4j. Lib (`component | pattern | utility | taxonomy`)
- **taxonomy** (`.md`): vocabulário controlado — termos com `definição, aliases, parent`.
- **component**: bloco de entregável reutilizável (skeleton fill-in).
- **pattern**: padrão de raciocínio/estrutura (mini-framework).
- **utility**: spec de helper transversal que um script implementa.

### 4k. Script (`.py`, `type: script`) — **runnable, não ilustrativo**
Header obrigatório:
```python
#!/usr/bin/env python3
"""
<name>.py — <propósito em 1 linha>
PART OF: Offer Book Squad / scripts
OWNER_AGENT: <agente>
CONSUMES: <paths/registries>   PRODUCES: <paths/outputs>
USAGE: python scripts/<name>.py [args]   (--check = dry-run read-only)
DEPENDS: stdlib (pyyaml é a única dep externa permitida)
EXIT: 0 ok · 1 falha de validação · 2 erro de uso
"""
```

### 4l. Project phase (`type: project-phase`, `NN-slug.md`)
```
## Objetivo da Fase · ## Critério de Entrada (fase NN-1) · ## Agentes & Tasks
## Passos (runbook) · ## Artefatos Produzidos · ## Gates · ## Critério de Saída → próxima fase
```

---

## 5. Checklist de "pronto" antes do commit
- [ ] Frontmatter válido; `id` ↔ path.
- [ ] Todas as referências resolvem (`qa-runner`).
- [ ] Seções obrigatórias do tipo presentes e substanciais (piso de palavras).
- [ ] Exemplo concreto onde exigido.
- [ ] Citação onde há claim factual (≤25 palavras literais).
- [ ] Voz aprovada (ativa, presente, 3ª série).
