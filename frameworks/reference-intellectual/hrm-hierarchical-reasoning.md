---
id: framework.reference-intellectual.hrm-hierarchical-reasoning
title: "HRM — Hierarchical Reasoning Model (a Base Metodológica dos Agentes)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: []
sources:
  - "Guan Wang et al. (Sapient Intelligence), *Hierarchical Reasoning Model*, arXiv 2506.21734 (2025)."
tags: [hrm, hierarchical-reasoning, h-module, l-module, prompt-engineering, agent-protocol, sapient]
---

# HRM — Hierarchical Reasoning Model (a Base Metodológica dos Agentes)

## TL;DR
O **HRM** (*Hierarchical Reasoning Model*, Sapient Inc., arXiv 2506.21734, 2025) é uma arquitetura recorrente inspirada no cérebro com **dois módulos acoplados**: um **H-Module** (alto nível, lento, planejador abstrato) que dirige um **L-Module** (baixo nível, rápido, executor concreto). Para cada passo do H, o L roda várias iterações rápidas e converge a um equilíbrio local; então o H reavalia o plano. O squad **não treina** esse modelo — ele o usa como **protocolo de raciocínio** de cada um dos 25 agentes: o H planeja e decompõe, o L executa e verifica, o H reavalia até convergir nos gates. Este framework é a base metodológica da seção §3 de todo agente, especificada em [`../../docs/agent-prompt-spec.md`](../../docs/agent-prompt-spec.md).

## Quando usar / Quando não
**Use** ao escrever ou auditar o prompt de qualquer agente: a §3 (Protocolo de Raciocínio HRM) é obrigatória e segue este desenho.
**Use** para decidir o que pertence ao **plano** (H: objetivo, decomposição, escolha de framework) e o que pertence à **execução** (L: passo-a-passo, ReAct, aplicação concreta).
**Use** para definir o **critério de parada** de um agente — o loop H↔L itera até um DoD mensurável ou o máximo de ciclos.
**Não use** como técnica de copy ou de oferta — HRM é **meta**: governa como os agentes pensam, não o que vendem.
**Não use** o paper como promessa de produto: o squad empresta a **metáfora arquitetural** (separação planejar/executar), não os pesos nem o treinamento do modelo.
**Fit:** transversal a todos os agentes e camadas (D0-D7); é o esqueleto cognitivo comum.

## Inputs
- O **objetivo** do agente (o mandato da §0 do prompt).
- Os **inputs upstream** que o agente consome (§2) e seu nível de confiança.
- O catálogo de **frameworks** que o agente pode aplicar (a tabela da §4).
- A **rubrica de pontuação** (Value Equation, sofisticação, prova) para os pontos de ramificação.
- Os **gates/DoD** que definem a convergência (§6).

## Procedimento
Mapeamento do HRM para a §3 do prompt de agente (de `agent-prompt-spec.md`):
1. **H-Module — plano lento e abstrato (§3.1).** Reescreva o objetivo em **uma** frase. Decomponha em 3-7 sub-objetivos. Escolha a estratégia e **quais frameworks** aplicar a cada sub-objetivo, citando ids. É o planejador: pensa devagar, no abstrato.
2. **L-Module — execução rápida e concreta (§3.2).** Para cada sub-objetivo, rode o passo-a-passo (Chain-of-Thought) e o loop **ReAct**: *Pensamento → Ação* (aplica o framework) *→ Observação* (o que o artefato/registry retorna) *→ próximo Pensamento*. É o executor: itera rápido, no concreto, até estabilizar aquele sub-objetivo.
3. **Pontos de ramificação — Tree-of-Thoughts (§3.3).** Onde houver escolha, **gere ≥3 candidatos**, pontue cada um pela rubrica (novidade, credibilidade, simplicidade; ou as alavancas de valor) e **pode** os fracos.
4. **Convergência H↔L — critério de parada (§3.4).** Depois que o L executa, o **H reavalia** o plano à luz do que o L observou; itera o loop externo até o critério de parada — um DoD mensurável (gate verde) ou o máximo de ciclos. É o equivalente operacional do "L converge a um equilíbrio local dentro de cada ciclo do H".
5. **Verificação (§6).** Antes de emitir, suba a escada de Bloom (Lembrar → Entender → Aplicar → Analisar → **Avaliar → Criar**): o agente **avalia** e, quando preciso, **recria** o próprio output. Inclua o red-team ("o que o Compliance/Voice rejeitaria?").
6. **Registro (§8).** Escreva de volta a decisão no registry certo — o write-back que fecha o ciclo ReAct.

## Outputs
- A **seção §3** do prompt de agente, estruturada em H (3.1), L (3.2), ToT (3.3) e convergência (3.4).
- O **critério de parada** explícito do agente (qual DoD/gate encerra o loop).
- O **traço H/L** abreviado nos exemplares few-shot (§5), mostrando plano → execução → reavaliação.
- O mapeamento técnica → seção alinhado ao `agent-prompt-spec.md`.

## Exemplo
Aplicação ao `mechanism-architect` (referência de profundidade do `agent-prompt-spec.md`):
- **H-Module (plano):** objetivo → "Nomear o mecanismo único que explica por que esta solução funciona onde dietas falham." Sub-objetivos: (1) achar a causa-raiz via 5 Whys; (2) contrastar velho × novo; (3) batizar; (4) provar; (5) comprimir em 1 frase. Para cada um, escolhe o framework.
- **L-Module (execução):** *Pensamento:* o avatar culpa "força de vontade". *Ação:* aplica [`../unique-mechanism.md`](../unique-mechanism.md). *Observação:* o `objection-registry` mostra "já tentei tudo" (consciência 3-4). *Pensamento:* então o mecanismo precisa reposicionar a culpa para algo fisiológico e novo.
- **ToT:** gera 3 nomes de mecanismo → pontua por novidade, credibilidade e simplicidade → poda 2.
- **Convergência H↔L:** o H confere os gates `mechanism-one-sentence-gate` e `mechanism-proof-gate`; se falham, devolve ao L para nova iteração; se passam, **para** e emite.
- **Resultado:** um mecanismo nomeado, provado e comprimido em uma frase — produzido pelo mesmo loop plano/execução/reavaliação que o HRM descreve.

## Armadilhas
- **Misturar plano e execução.** Detalhar a tática no H (ou planejar no L) embola o raciocínio. Mantenha o H abstrato e o L concreto.
- **Loop sem critério de parada.** Sem um DoD mensurável, o agente itera para sempre ou para cedo demais. Defina o gate que encerra.
- **Pular a reavaliação do H.** Executar uma vez e emitir ignora a convergência; o H **precisa** reavaliar à luz da observação do L.
- **ToT sem rubrica.** Gerar candidatos e escolher "no gosto" anula o ganho; pontue contra uma régua explícita.
- **Tratar o paper como produto.** O squad usa a **metáfora arquitetural** (planejar/executar/reavaliar), não os pesos do modelo de 27M de parâmetros nem seu treinamento.
- **Externalizar o que o HRM faz interno.** O modelo "pensa em silêncio"; no prompt, ao contrário, **explicitamos** o traço H/L para auditabilidade — não confunda as duas camadas.

## Interações
- **Agentes** (de `config.yaml`): **todos os 25** — cada prompt carrega a §3 HRM. O `offer-squad-architect` (dono do `agent-prompt-spec.md`) garante que cada agente segue o esqueleto; o `offerbook-chief` carrega a 13ª seção de orquestração; os demais (de `market-sophistication-analyst` a `knowledge-librarian`) instanciam H/L/ToT/convergência no seu domínio.
- **Documento mestre**: [`../../docs/agent-prompt-spec.md`](../../docs/agent-prompt-spec.md) — a especificação canônica que este framework operacionaliza, com o mapa técnica → seção (HRM em §3.1, §3.2, §3.4).
- **Frameworks que pareiam**: qualquer framework de domínio é **aplicado dentro do L-Module** (citado na §4 do agente) e **pontuado nos pontos de ramificação** — HRM é o trilho onde todos correm.

## Fontes
> **Fonte:** Guan Wang, Jin Li, Yuhao Sun et al. (Sapient Inc. / Sapient Intelligence), *Hierarchical Reasoning Model*, arXiv 2506.21734 (2025), submetido 26 jun. 2025 — via <https://arxiv.org/abs/2506.21734>, acesso 2026-06-02.
> **Anti-verbatim:** estrutura e conceitos (módulos H/L, convergência, ToT) em redação original. Citação literal ≤ 25 palavras, atribuída.
