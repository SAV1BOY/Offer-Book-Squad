---
id: doc.agent-prompt-spec
title: "Especificação Canônica do Prompt de Agente (HRM)"
type: doc
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
frameworks: [reference-intellectual/hrm-hierarchical-reasoning]
sources:
  - "Sapient Inc., Hierarchical Reasoning Model, arXiv 2506.21734 (2025)"
tags: [hrm, prompt-engineering, cot, tot, react, few-shot, bloom]
---

# Especificação Canônica do Prompt de Agente (HRM)

Cada um dos **25 agentes** do squad é um **prompt operacional completo** — não um blurb de papel. Este documento define o esqueleto que **todos** seguem, onde cada técnica de prompt engineering vive, e o piso de qualidade (`qa-runner`: agente ≥ 1200 palavras).

> **HRM** (*Hierarchical Reasoning Model*, Sapient Inc., arXiv 2506.21734, 2025): um modelo recorrente com **dois módulos acoplados** — um **H-Module** (alto nível, lento, planejador abstrato) que dirige um **L-Module** (baixo nível, rápido, executor concreto). Operacionalizamos isso como o protocolo de raciocínio de cada agente: o H planeja e decompõe; o L executa e verifica; o H reavalia até convergir nos gates.

---

## Frontmatter obrigatório do agente
```yaml
---
id: agent.<slug>                 # derivado do path (agents/<slug>.md)
title: "<Nome do Agente>"
type: agent
layer: D0..D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: <self>
activates_on: [<condições de gatilho>]
consumes: [<ids upstream>]
produces: [<ids downstream>]
upstream: [<agent ids que me alimentam>]
downstream: [<agent ids que alimento>]
frameworks: [<framework ids que aplico>]
checklists: [<gate ids que devo passar>]
registries: [<registry ids que escrevo/leio>]
can_veto: [<o que posso bloquear>]    # OMITIR se o agente não tem veto
sources: [<citações quando aplicável>]
tags: [<...>]
---
```
Todo id deve estar **reservado em `config.yaml`** e resolver (bijeção verificada pelo `qa-runner`).

> **Termos de handoff:** `upstream` = *handoff_from* (quem me alimenta) e `downstream` = *handoff_to* (quem eu alimento). A matriz canônica de todos os handoffs (intra-squad agente→agente + cross-squad dos 12) está em [`handoff-matrix.md`](handoff-matrix.md).

---

## O esqueleto (12 seções, nesta ordem)

### `# <Agente> — <mandato em 1 frase>`

### `## 0. Identidade & Mandato`  *(técnica: ROLE / PERSONA)*
Um parágrafo que define **quem** é o agente, sua **linhagem** (quais autores/frameworks ele encarna) e seu **mandato inegociável**. Ex.: *"Você é o Mechanism Architect. Você isola e nomeia o mecanismo único que faz a oferta funcionar quando todo o resto falhou…"*

### `## 1. Contrato de Ativação`  *(quando eu acordo?)*
- Condições de gatilho (espelha `activates_on`).
- **Pré-condições** que precisam estar verdes a montante antes de eu rodar.
- **Condições de recusa:** quando devolvo/escalono em vez de agir.

### `## 2. Inputs que Consumo`  *(ReAct: OBSERVE)*
- Lista exata dos artefatos upstream (espelha `consumes`) e **quais campos** leio de cada.
- O que faço se um input obrigatório falta ou tem baixa confiança (degradar com elegância, pedir).

### `## 3. Protocolo de Raciocínio HRM`  ← **O NÚCLEO**
#### `### 3.1 H-Module (plano lento e abstrato)`  *(DECOMPOSIÇÃO + CoT estratégico)*
- Reescreve o objetivo em **uma** frase.
- Decompõe em 3–7 sub-objetivos.
- Escolhe a estratégia e **quais frameworks** aplicar a cada sub-objetivo (citando ids).
#### `### 3.2 L-Module (execução rápida e concreta)`  *(CoT + ReAct)*
- Para cada sub-objetivo, o passo-a-passo: *"Pense passo a passo: primeiro… então… portanto…"*.
- Loop ReAct explícito: **Pensamento → Ação** (aplica framework X) **→ Observação** (o que o artefato/registry retorna) **→ próximo Pensamento**.
#### `### 3.3 Pontos de Ramificação (Tree-of-Thoughts)`  *(ToT)*
- Pontos onde o agente **gera ≥3 candidatos**, pontua cada um contra a Value Equation / sofisticação / prova, e **poda**. Inclui a **rubrica de pontuação**.
#### `### 3.4 Convergência H↔L / Critério de Parada`
- O loop externo: depois que L executa, H reavalia o plano; itera até o critério de parada (um DoD mensurável) ou o máximo de ciclos.

### `## 4. Frameworks que Aplico`
Tabela: `framework id → quando no protocolo → output esperado`. (Espelha `frameworks`; cada um resolve.)

### `## 5. Exemplares Few-Shot`  *(técnica: FEW-SHOT)*
**≥2 mini-casos** totalmente resolvidos ("oferta bruta entra → output do agente sai"), cobrindo **estágios de sofisticação diferentes**. Cada um mostra o traço H/L abreviado. Redação **original**.

### `## 6. Self-Verification & Quality Gates`  *(SELF-VERIFICATION + BLOOM)*
- Os gates que devo passar antes de emitir (espelha `checklists`).
- Passe de autocrítica: *"Antes de emitir, eu verifico: (1)… (2)… (3)…"*, subindo a **escada de Bloom** (Lembrar→Entender→Aplicar→Analisar→**Avaliar→Criar**): o agente precisa **avaliar** e, quando aplicável, **recriar** seu próprio output.
- Prompt red-team: *"O que o Compliance Auditor / Voice Guardian rejeitaria aqui?"*

### `## 7. Poderes de Veto & Escalonamento`
- Exatamente o que posso **bloquear** (espelha `can_veto`) e o caminho de override.
- A quem escalono (geralmente `offerbook-chief`). *(Agentes sem veto declaram "Sem poder de veto" e listam o que sinalizam.)*

### `## 8. Registros & Decisões`  *(ReAct: write-back)*
O que devo logar e **em qual registry** (espelha `registries`), com o **formato exato** do registro (decisões, mecanismos, prova, pricing tests, winners…).

### `## 9. Contratos de Handoff`
- **Upstream** (quem me alimenta, o que eu exijo) — espelha `upstream`/`consumes`.
- **Downstream** (quem eu alimento, a **garantia** que dou) — espelha `downstream`/`produces`.
- *Contrato* = os campos/qualidade mínimos que o próximo agente pode confiar que existem.

### `## 10. Schema de Saída`
O formato exato que emito (geralmente um bloco fenced ou um ponteiro para um arquivo `templates/`). Spec campo-a-campo + um exemplo preenchido.

### `## 11. Modos de Falha & Recuperação`
Formas conhecidas de o agente errar (ex.: mecanismo que é clichê da categoria, prova infalsificável) e o procedimento de recuperação.

> **`offerbook-chief`** carrega uma 13ª seção exclusiva — `## 12. Mapa de Orquestração` — com a ordem dos agentes para Offer-Book vs Blackbook.

---

## Mapa técnica → seção (para o executor)
| Técnica | Onde vive |
|---|---|
| HRM (H/L/convergência) | §3.1, §3.2, §3.4 |
| Chain-of-Thought | §3.2 |
| Tree-of-Thoughts | §3.3 |
| Few-shot | §5 |
| Role/Persona | §0 |
| Decomposição | §3.1 |
| Self-verification | §6 |
| ReAct (act/observe/write-back) | §3.2 + §8 |
| Progressão de Bloom | §6 |

---

## Mini-exemplo de §3 (referência de profundidade — Mechanism Architect)

> **H-Module:** Objetivo → *"Nomear o mecanismo único que explica por que esta solução funciona onde dietas falham."* Sub-objetivos: (1) achar a causa-raiz via 5 Whys; (2) contrastar velho×novo; (3) batizar; (4) provar; (5) comprimir em 1 frase.
> **L-Module:** *Pensamento:* o avatar culpa "força de vontade". *Ação:* aplico `frameworks/unique-mechanism`. *Observação:* registry de objeções mostra "já tentei tudo" (consciência nível 3–4). *Pensamento:* então o mecanismo precisa reposicionar a culpa para algo fisiológico e novo…
> **ToT:** gero 3 nomes de mecanismo → pontuo por (novidade, credibilidade, simplicidade) → podo 2.
> **Convergência:** H confere `mechanism/mechanism-one-sentence-gate` e `mechanism-proof-gate`; se falham, volta ao L.

Este nível de concretude é o **piso**, não o teto, para as seções §3 e §5 de todo agente.
