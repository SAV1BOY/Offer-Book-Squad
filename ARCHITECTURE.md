# ARCHITECTURE — Offer Book Squad

Este documento é o **mapa-mestre** do squad: princípios, camadas do pipeline, os 25 agentes, as convenções de arquivo (frontmatter, IDs, Definition of Done), o modelo de roteamento e o plano de build. Qualquer sessão futura deve conseguir retomar o trabalho só lendo este arquivo + [`BUILD-PROGRESS.md`](BUILD-PROGRESS.md) + [`config.yaml`](config.yaml).

---

## 1. O que separa "uma oferta" de uma "máquina de offer book"

Uma oferta comum descreve um produto e um preço. Um **offer book de verdade**:
- diagnostica o mercado (sofisticação + consciência) **antes** de escrever uma palavra;
- conhece o cliente pela voz dele (VOC), não por suposição;
- isola e nomeia o **mecanismo único**;
- mapeia prova a cada claim e a cada objeção;
- deriva preço de **valor/WTP**, nunca de custo;
- desenha um **Money Model** (a *sequência* atração→upsell→downsell→continuidade), não uma oferta avulsa;
- destila tudo em **UMA Grande Ideia** (Power of One);
- e só então vira copy, funil, evento, afiliados e logística — com escassez **100% verdadeira** e compliance.

### Princípio central (o pipeline)
```
Mercado → Avatar → Mecanismo → Valor → Money Model → Big Idea → Posição
        → [★ OFFER BOOK] → Copy → Funil → Ops/Eventos → Afiliados/PR
        → [★ BLACKBOOK] → Memória
```

### HARD STOP
Nenhuma copy (D4+) nasce antes do Offer Book passar no **Definition of Done** (`checklists/offer-book-stack/offer-book-dod-gate.md`). É o princípio Agora: ~50–60% do trabalho é pesquisa/estratégia antes da primeira palavra. Modelado em `config.yaml: defaults.hard_stop_before_copy: true`.

---

## 2. Os 11 princípios não-negociáveis

| Princípio | Significado |
|---|---|
| `evidence_before_opinion` | Toda afirmação aponta para evidência. |
| `contradiction_before_conclusion` | Buscar o contra antes de concluir. |
| `traceability_before_eloquence` | Rastreabilidade > beleza. |
| `decision_before_ornament` | Cada peça serve a uma decisão. |
| `memory_before_repetition` | Reusar memória antes de recriar. |
| `clarity_before_volume` | Clareza > quantidade. |
| **`offer_before_persuasion`** | Sem oferta forte, não escreva. |
| **`one_big_idea`** | UMA tese por lançamento. |
| **`truthful_scarcity`** | Escassez falsa = veto. |
| **`value_equation_test`** | Toda peça move ≥1 alavanca de valor. |
| **`money_model_spine`** | O centro é a sequência, não a oferta. |

---

## 3. Camadas do pipeline (`layer:` no frontmatter)

| Camada | Nome | Agentes-chave | Saída |
|---|---|---|---|
| **D0** | Comando & Arquitetura | offerbook-chief, offer-squad-architect | project type + pipeline do caso |
| **D1** | Inteligência | market-sophistication-analyst, avatar-voc-investigator, proof-credibility-curator | mercado + avatar + prova |
| **D2** | Arquitetura de Oferta | mechanism-architect, value-equation-engineer, money-model-designer, pricing-wtp-strategist, unit-economics-stack-analyst | mecanismo + valor + money model + preço + unit economics |
| **D3** | Big Idea & Posição | big-idea-architect, positioning-lead-strategist | UMA Big Idea + posicionamento → **★ OFFER BOOK (HARD STOP)** |
| **D4** | Copy & Criativo | vsl-webinar-scriptwriter, email-sms-sequence-writer, direct-mail-insert-writer, ad-creative-factory, voice-style-guardian | VSL, sequências, mailers, ads (na voz) |
| **D5** | Funil & Tech | funnel-architect, tech-links-deliverability-engineer | mapa de funil + URLs + deliverability |
| **D6** | Ops/Eventos & Growth | launch-producer, events-logistics-coordinator, affiliate-program-architect, pr-brand-strategist | run-of-show + logística + afiliados + PR |
| **D7** | QA/Compliance & Memória | compliance-auditor, knowledge-librarian | **★ BLACKBOOK** + registries atualizados |

---

## 4. Os 25 agentes

**Comando (2):** `offerbook-chief` · `offer-squad-architect`
**Inteligência (3):** `market-sophistication-analyst` · `avatar-voc-investigator` · `proof-credibility-curator`
**Arquitetura de oferta (5):** `mechanism-architect` · `value-equation-engineer` · `money-model-designer` · `pricing-wtp-strategist` · `unit-economics-stack-analyst`
**Big Idea & posição (2):** `big-idea-architect` · `positioning-lead-strategist`
**Copy & criativo (5):** `vsl-webinar-scriptwriter` · `email-sms-sequence-writer` · `direct-mail-insert-writer` · `ad-creative-factory` · `voice-style-guardian`
**Funil & tech (2):** `funnel-architect` · `tech-links-deliverability-engineer`
**Ops & eventos (2):** `launch-producer` · `events-logistics-coordinator`
**Growth (2):** `affiliate-program-architect` · `pr-brand-strategist`
**QA & memória (2):** `compliance-auditor` · `knowledge-librarian`

### Regras anti-caos (quem manda no quê)
- **OfferBook Chief** decide o project type, a prioridade e a definição de pronto.
- **Offer Squad Architect** decide o desenho do pipeline e os handoffs.
- **Money Model Designer** é dono da espinha: nada de copy/funil/logística antes da escada existir.
- **Value Equation Engineer** pode reprovar qualquer componente que não mova uma alavanca.
- **Big Idea Architect** entrega UMA tese — múltiplas ideias = reprovação.
- **Compliance Auditor** é a última barreira e pode **vetar** claim sem lastro ou escassez falsa.
- **Knowledge Librarian** registra tudo que vira memória reutilizável.

Cada agente é um **prompt operacional HRM completo** — ver o esqueleto canônico em [`docs/agent-prompt-spec.md`](docs/agent-prompt-spec.md).

---

## 5. Convenções de arquivo

### 5.1 Frontmatter YAML (todo `.md`)
```yaml
---
id: <namespace.slug>             # DERIVADO do path; único; ex.: agent.money-model-designer
title: "<Título Humano>"
type: agent|checklist|gate|framework|reference|template|task|workflow|swipe|swipe-source|voice|phrases|registry|component|pattern|utility|taxonomy|script|project-phase|doc|config
layer: D0..D7|cross               # camada do pipeline (seção 3)
status: draft|review|stable|deprecated
version: 0.1.0                    # semver; sobe em mudança material
updated: 2026-06-02               # ISO date
owner_agent: <agent-id|null>      # agente dono (null para libs transversais)
# relacionamentos (OMITIR a chave se vazia — nunca deixar em branco):
consumes: [<ids upstream>]        # contratos de entrada
produces: [<ids downstream>]      # contratos de saída
frameworks: [<framework ids>]     # frameworks aplicados/citados
checklists: [<gate ids>]          # gates que este artefato deve passar
registries: [<registry ids>]      # registries lidos/escritos
sources: [<citation ids|URL>]     # OBRIGATÓRIO em reference/framework-reference/swipe
# roteamento (agents/tasks/workflows):
activates_on: [<condições>]
upstream: [<agent ids>]
downstream: [<agent ids>]
can_veto: [<o que pode bloquear>]
tags: [<...>]
---
```

### 5.2 IDs determinísticos (path → id)
O `id` é derivado do path: `agents/money-model-designer.md` → `agent.money-model-designer`; `frameworks/copy/aida.md` → `framework.copy.aida`; `data/registries/proof-registry.md` → `data.registry.proof`. `scripts/id-resolver.py` constrói o mapa id↔path e `scripts/qa-runner.py` exige **bijeção** (zero colisão, zero referência pendente).

### 5.3 `config.yaml` = fonte única de verdade
O config **reserva** todos os ids (25 agentes, gates, registries, workflows) na Fase 0, antes de qualquer arquivo citá-los. Assim, referências de frontmatter sempre resolvem mesmo no build em camadas. Qualquer `upstream/downstream/can_veto` de agente que contradiga o config **falha** no `qa-runner`.

### 5.4 Naming & links
- `kebab-case`, minúsculas, sem espaço. Fases de projeto: `NN-slug.md` (zero-padded, `00-…`).
- Gates: `*-gate.md` com o nome afirmando a condição de passagem.
- Cross-links em prosa sempre **relativos** (`../frameworks/value-equation.md`).
- Idioma: **conteúdo em português**; chaves de frontmatter, paths e código em inglês.

### 5.5 Definition of Done por arquivo (sem stubs no estado final)
1. Frontmatter válido para o `type`; `id` ↔ path consistente.
2. Toda referência (`consumes/produces/frameworks/checklists/sources`) resolve.
3. Todas as seções obrigatórias do esqueleto do tipo presentes e substanciais (SOTA).
4. ≥1 exemplo concreto onde o esqueleto exige (agentes, frameworks, templates, tasks, swipe).
5. Bloco de citação válido em reference/framework-reference/swipe.
6. `qa-runner.py` passa (lint + links + seções + ids + pisos de palavras: agente ≥1200, framework ≥500, gate ≥150).
7. Redação original; metodologia de terceiros citada por **princípio/estrutura**, nunca copy literal (>25 palavras).

---

## 6. Modelo de roteamento

`config.yaml → routing.<task>` mapeia cada task para `{agents, frameworks, checklists, templates, registry}`. As composições (`run-offer-book`, `run-full-launch`, `run-single-promo`, `run-enterprise-deal-book`) encadeiam tasks. Os **quality_gates.mandatory** e **per_domain** definem o que precisa passar; o **HARD STOP** (`offer-book-dod-gate`) bloqueia D4+.

```
Task → Agents → Frameworks → Checklists → Templates → Registry → (gate) → Handoff
```

---

## 7. Plano de build (camada por camada) — ver BUILD-PROGRESS.md

Ordem por dependência (referências sempre resolvem graças à reserva de ids no config):

`Fase 0` Foundation → `1` taxonomias → `2` reference (citações) → `3` frameworks → `4` lib (resto) → `5` agents + registries → `6` checklists → `7` templates → `8` tasks → `9` workflows → `10` swipe → `11` voice/phrases → `12` data → `13` authority → `14` projects → `15` scripts → `16` docs → `17` archive → `18` QA de integração.

**Meta ≈ 768 arquivos.** `scripts/coverage-report.py` imprime a contagem viva por diretório vs meta.

### Reconciliações & decisões de estrutura (para não surpreender sessões futuras)
- **Gates por agente:** 14 subpastas × 5 = 70 (exatamente as 14 detalhadas no mapeamento, não 25). As demais subpastas de `checklists/` (architect, unit-econ, mailer, voice, tech, events, affiliate, pr) recebem gates conforme necessidade do agente dono.
- **Registries** vivem em `data/registries/` mas são construídos na **Fase 5** (junto dos agentes), pois agentes os citam.
- **Swipe vs swipe-breakdowns:** `swipe/<categoria>/` guarda índice + padrões **originais**; teardowns de campanhas nomeadas vivem em `reference/swipe-breakdowns/` (sem duplicar).
- **Citações:** apenas `reference/`, `frameworks/reference-intellectual/`, `swipe-*` e claims factuais citam fonte primária; o resto cita transitivamente via os frameworks/reference que referencia.

---

## 8. Referências intelectuais (citadas, nunca copiadas)

Hormozi (*$100M Offers* 2021, *Leads* 2023, *Money Models* 2025) · Schwartz (*Breakthrough Advertising*) · Cialdini · Halbert · Sugarman · Ogilvy · Caples · Hopkins · Collier · Bencivenga · Kennedy · Ramanujam · Nagle · Voss · Kahneman · Ariely · Ries/Trout · Dunford · Moore · Walker · Brunson · Challenger Sale · SPIN · MEDDIC. Metodologia de raciocínio: **HRM** (Sapient Inc., *Hierarchical Reasoning Model*, arXiv 2506.21734, 2025).

Regra anti-plágio em [`docs/compliance-policy.md`](docs/compliance-policy.md) e [`docs/style-guide.md`](docs/style-guide.md).
