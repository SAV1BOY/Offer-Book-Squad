---
id: task.intelligence.run-market-intel
title: "Run Market Intel — Diagnosticar Sofisticação e Consciência, Dimensionar a Demanda e Provar a Multidão Faminta"
type: task
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
consumes:
  - decision.scope-one-sentence
  - artifact.case-pipeline
  - template.strategy.market-brief
produces:
  - artifact.market-brief
  - decision.sophistication-stage
  - decision.awareness-level
frameworks: [awareness-x-sophistication, starving-crowd]
checklists:
  - market/market-sophistication-gate
  - market/market-awareness-gate
  - market/market-starving-crowd-gate
registries: [offer-registry]
metrics: [value_equation_score, big_idea_strength]
tags: [intelligence, mercado, sofisticacao, consciencia, starving-crowd, tam-sam-som, d1]
---

# Run Market Intel — diagnosticar sofisticação e consciência, dimensionar a demanda e provar a multidão faminta

## Objetivo
Devolver um market-brief com dois números defensáveis — sofisticação (1-5) e consciência (1-5), cada um com ≥2 evidências independentes — mais o dimensionamento TAM/SAM/SOM e o veredito da multidão faminta, no estado em que avatar, mecanismo e Big Idea podem ser calibrados sem palpite.

## Agente dono
[`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md). O primeiro diagnosticador do squad. Não desenha oferta, não escreve copy, não inventa avatar; lê o terreno e devolve o brief. Sem poder de veto — sinaliza riscos.

## Gatilho / Quando
Roda em D1, no instante em que o [`offer-squad-architect`](../../agents/offer-squad-architect.md) libera a trilha de mercado no pipeline do caso. É a primeira task de inteligência e antecede `build-avatar-voc` e `curate-proof`. **Pré-condição:** existe uma frase de escopo travada (sei qual transformação e qual público) e a posição no DAG (sei se sou "construção completa" ou "revalidação leve"). Sem público definido não há mercado a diagnosticar. Se o escopo aponta para dois mercados distintos, **devolvo** ao architect/chief pedindo priorização — não diagnostico dois como um só.

## Inputs (Consome)
- **`decision.scope-one-sentence`** — o público-alvo e a transformação prometida: o recorte do mercado.
- **`artifact.case-pipeline`** (do architect) — meu peso esperado, os gates a passar e o contrato de saída (o que avatar/proof esperam de mim).
- **Handoff de pesquisa (`deepresearch_squad`)**, quando houver — market sizing (para TAM/SAM/SOM), VOC bruto e inteligência competitiva (anúncios, posicionamentos, claims dos concorrentes). É a matéria-prima da evidência.
- **[`template.strategy.market-brief`](../../templates/strategy/market-brief-template.md)** — o formato do entregável.
- **Registry lido/escrito:** [`offer-registry`](../../data/registries/offer-registry.md) — para registrar a oferta-semente com `sophistication_stage`.

## Procedimento
1. **Delimite o mercado.** Recorte exato do escopo (quem, qual transformação). Mercado vago = diagnóstico vago.
2. **Rode o teste starving-crowd (portão de entrada).** Aplique [`starving-crowd`](../../frameworks/starving-crowd.md): pontue Dor, Poder de compra e Alcance (0-10) **com evidência por nota**. Some; aplique o piso de corte. Sem fome → recomende "não escrever ainda, mudar mercado/oferta" e sinalize. **Confunda interesse com fome é o erro a evitar** — exija histórico de gasto, não promessa.
3. **Diagnostique a sofisticação (1-5).** Liste os **claims dominantes** dos concorrentes e compare anúncios antigos vs recentes. Anúncios que já explicam um "como" (mecanismo) → estágio 3+; mecanismos competindo entre si → estágio 4. Cite ≥2 evidências (Schwartz: inferir da evidência, não do palpite).
4. **Diagnostique a consciência (1-5).** Leia a VOC: como o prospect descreve a situação. Compara categorias de solução → nível 3; conhece marcas e hesita → nível 4. Cite ≥2 evidências.
5. **Resolva a ambiguidade (Tree-of-Thoughts).** Quando a sofisticação fica entre dois estágios, gere ≥3 leituras candidatas e pontue por *aderência à evidência* (×3), *consequência de errar para baixo* (×2), *consequência de errar para cima* (×1). Na dúvida, **arredonde para o mais sofisticado** — mercado estágio-4 com copy estágio-2 fica invisível.
6. **Dimensione TAM/SAM/SOM.** Total → servível → obtenível no prazo/orçamento, de baixo para cima, com base de cálculo explícita. Confirme SOM ≤ SAM ≤ TAM e SOM compatível com a meta de receita.
7. **Derive as implicações.** Qual mecanismo o estágio exige (claim simples / amplificado / mecanismo nomeado / elevado / identidade), qual lead recomendado, abertura da copy (direta/indireta).
8. **Self-verify (Bloom + red-team).** Cada número tem ≥2 evidências independentes? Há contra-evidência? O que o `mechanism-architect` rejeitaria (estágio sem evidência)? Corrija antes de emitir.
9. **Registre e passe os gates.** Escreva a oferta-semente no `offer-registry` (`sophistication_stage` justificado, `owner_agent`, `decided_in`). Passe os três gates de mercado com evidência linkada.

## Frameworks
- [`starving-crowd`](../../frameworks/starving-crowd.md) — ranking Dor/Poder/Alcance + veredito vai/não-vai (portão de entrada).
- [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) — célula da matriz 5×5 + implicação de lead/copy. (Taxonomias-mãe: [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md), [`awareness-levels`](../../lib/taxonomies/awareness-levels.md).)

## Outputs (Produz)
- **`artifact.market-brief`** — sofisticação + consciência (com evidência), célula da matriz, veredito starving-crowd, TAM/SAM/SOM, implicações de mecanismo/lead/abertura, nível de confiança.
- **`decision.sophistication-stage`** e **`decision.awareness-level`** — os dois números travados.
- **Registry escrito:** [`offer-registry`](../../data/registries/offer-registry.md) com a oferta-semente (`sophistication_stage`, `status: draft/proposed`, `owner_agent`, `decided_in`, `updated`).

## Definition of Done
Os dois números estão declarados com os termos das taxonomias e ≥2 evidências independentes cada; o veredito starving-crowd tem nota tripla justificada; TAM/SAM/SOM são coerentes e o SOM bate com a meta; as implicações (mecanismo/lead/abertura) estão derivadas; os três gates de mercado estão verdes com evidência linkada; a oferta-semente está no registry. Máximo de 3 ciclos; persistindo ambiguidade por falta de dados, entregue com confiança rebaixada e pedido de pesquisa registrado.

## Gates
- [`market/market-sophistication-gate`](../../checklists/market/market-sophistication-gate.md)
- [`market/market-awareness-gate`](../../checklists/market/market-awareness-gate.md)
- [`market/market-starving-crowd-gate`](../../checklists/market/market-starving-crowd-gate.md)

## Métricas
Move KPIs da família **offer_quality** ([`config.yaml`](../../config.yaml) `kpis:`), por ser a fundação que calibra a oferta sem palpite:
- **`value_equation_score`** — a sofisticação diagnosticada define quanta amplificação de valor o mercado exige; um diagnóstico errado infla ou esvazia a Value Equation a jusante.
- **`big_idea_strength`** — a consciência dominante e os claims saturados decidem o fit (nova/crível) da Big Idea; o brief é o lastro do critério de awareness.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (família offer_quality), com a oferta-semente registrada em [`offer-registry`](../../data/registries/offer-registry.md).

## Handoff
**Próxima task:** [`build-avatar-voc`](build-avatar-voc.md) — dono [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md). **Contrato de saída:** todo downstream recebe o market-brief com (i) dois números defensáveis com ≥2 evidências cada, (ii) o mercado-alvo recortado e o veredito starving-crowd, (iii) TAM/SAM/SOM, (iv) as implicações. O avatar parte do mercado-alvo para minerar a voz certa; o [`mechanism-architect`](../../agents/mechanism-architect.md) parte do estágio (3-4 exige mecanismo nomeado/elevado); o [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) parte da célula da matriz para escolher o lead. Garantia: esses números **nunca chegam sem evidência**.
