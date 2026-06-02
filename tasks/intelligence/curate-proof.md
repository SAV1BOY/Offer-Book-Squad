---
id: task.intelligence.curate-proof
title: "Curate Proof — Inventariar e Classificar a Prova, Casar Cada Prova a um Claim/Objeção e Reportar os Gaps"
type: task
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
consumes:
  - artifact.objection-belief-map
  - artifact.market-brief
  - template.strategy.proof-bank
produces:
  - artifact.proof-bank
  - artifact.proof-claim-matrix
  - artifact.proof-gap-report
frameworks: [proof-to-claim-chain]
checklists:
  - proof/proof-claim-backing-gate
registries: [proof-registry, claim-registry]
tags: [intelligence, prova, credibilidade, depoimento, caso, claim, proof-to-claim, gap, d1]
---

# Curate Proof — inventariar e classificar a prova, casar cada prova a um claim/objeção e reportar os gaps

## Objetivo
Devolver o arsenal de prova mapeado claim a claim e objeção a objeção — cada prova classificada por força e proveniência, cada objeção de alta severidade desarmada pela melhor prova, e cada buraco reportado como proof-gap — no estado em que a copy nunca afirma o que não pode provar.

## Agente dono
[`proof-credibility-curator`](../../agents/proof-credibility-curator.md). O guardião da credibilidade e a primeira linha de defesa do `compliance-auditor`. Não inventa avatar (herda o mapa de objeções), não desenha mecanismo, não escreve copy. Sem poder de veto — sinaliza gaps.

## Gatilho / Quando
Roda em D1, quando o [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) entrega o **mapa de objeções** e o gate [`avatar/avatar-objection-map-gate`](../../checklists/avatar/avatar-objection-map-gate.md) está verde — é a dependência real, porque curo prova **contra as objeções e claims**, não no vácuo. **Pré-condição:** existe um mapa de objeções (sei contra o que provar) e o market-brief (sei o estágio — 3-5 exige prova de **mecanismo**, não só de resultado). Se um claim central não tem nenhuma prova e não é factível obtê-la a tempo, **não fabrico** — reporto o proof-gap (o compliance vetaria de qualquer forma). Prova sem consentimento/proveniência fica **não usável** até resolver.

## Inputs (Consome)
- **`artifact.objection-belief-map`** (do avatar) — cada objeção, sua falsa crença e severidade. A lista do que a prova precisa desarmar. `belief-self` pede prova de pessoas como o avatar; `price` pede prova de ROI/valor.
- **`artifact.market-brief`** (do market-analyst) — o estágio de sofisticação (3-5 → prova de mecanismo) e a emoção dominante (a prova precisa ressoar; em B2B, roteada por papel da DMU).
- **Inventário de prova bruto** — depoimentos, casos, dados internos, prints, estudos, menções de mídia, credenciais/autoridade.
- **[`template.strategy.proof-bank`](../../templates/strategy/proof-bank-template.md)** — o formato do banco.
- **Registries escritos:** [`proof-registry`](../../data/registries/proof-registry.md) (sou o dono) e [`claim-registry`](../../data/registries/claim-registry.md).

## Procedimento
1. **Enumere claims e objeções.** Liste os claims que a oferta fará (do mecanismo/resultado) e as objeções que precisam de prova, as de **alta severidade** primeiro.
2. **Inventarie toda a prova.** Catalogue cada peça com `proof_type` (testimonial / case-study / data / screenshot / demo / endorsement / media-mention), `summary` e `source_name`.
3. **Classifique a força.** Aplique [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md): especificidade + verificabilidade → `weak/moderate/strong`. Depoimento vago = weak; caso com número auditável, nome, data e print = strong. Classifique **honesto** — não infle weak para strong.
4. **Verifique a proveniência.** Consentimento, fonte checável, direito de uso. Sem autorização → `consent_status: pending`, não usável. Dado "87% melhoram" sem n/metodologia → não usável até a base ser documentada.
5. **Monte a matriz prova × claim/objeção.** Cada claim/objeção recebe a melhor prova disponível. Em B2B, agrupe por papel da DMU (ROI pro CFO, compliance pro risco, benchmark técnico pro TI).
6. **Escolha a munição principal (Tree-of-Thoughts).** Quando uma objeção de alta severidade tem várias provas candidatas, gere ≥3 e pontue por *especificidade* (×2), *verificabilidade* (×3), *ressonância com a emoção dominante* (×2), *risco de compliance* (×2, invertido). Prova específica e verificável vence prova emocional e vaga; o que o compliance derrubaria não entra como principal.
7. **Identifique os proof-gaps.** Cruze a matriz: sobrou claim sem prova? Ex.: "resultado em 90 dias" sem caso datado → gap de severidade alta → recomende obter caso datado ou suavizar/remover o claim.
8. **Self-verify (Bloom + red-team).** Cada prova casada a ≥1 claim (sem prova órfã)? Cada claim forte com prova (sem claim órfão)? A classificação é honesta? *"O que o `compliance-auditor` rejeitaria?"* — esta é a pergunta central. Abra o gap **aqui**, antes do veto lá na frente.
9. **Registre e passe o gate.** Escreva cada prova no `proof-registry` (com `strength` e `consent_status`) e cada claim no `claim-registry` (com a prova que o sustenta). Liste os proof-gaps com recomendação. Passe o `proof-claim-backing-gate`.

## Frameworks
- [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) — corrente prova → claim/objeção; nenhuma prova órfã, nenhum claim órfão; força classificada. (Estágio herdado: 3-4 → prova de mecanismo; 5 → prova de identidade/comunidade.)

## Outputs (Produz)
- **`artifact.proof-bank`** — inventário classificado por força e proveniência.
- **`artifact.proof-claim-matrix`** — cada claim/objeção com a melhor prova disponível (em B2B, por papel da DMU).
- **`artifact.proof-gap-report`** — o que **não** se pode afirmar: `{claim, objeção associada, prova faltante, severidade, recomendação}`.
- **Registries escritos:** [`proof-registry`](../../data/registries/proof-registry.md) e [`claim-registry`](../../data/registries/claim-registry.md).

## Definition of Done
Cada claim que a oferta fará tem ≥1 prova de força adequada ao estágio (mecanismo provado nos estágios 3-4); cada objeção de alta severidade tem prova que a desarma; toda prova tem `consent_status` resolvido; os proof-gaps estão listados e priorizados com recomendação; o `proof-claim-backing-gate` está verde. Se um claim central permanece sem prova, **não declaro verde** — entrego o gap como bloqueio sinalizado ao chief e ao compliance.

## Gates
- [`proof/proof-claim-backing-gate`](../../checklists/proof/proof-claim-backing-gate.md)

## Handoff
**Próxima task:** fecha a camada D1 e libera o D2 ([`define-mechanism`](../offer-architecture/define-mechanism.md), dono [`mechanism-architect`](../../agents/mechanism-architect.md), que recebe a prova do mecanismo disponível para nomear um mecanismo com lastro). Adiante, os escritores de copy recebem a matriz prova×objeção e o `compliance-auditor` recebe o registro de prova com proveniência. **Garantia:** nenhum claim chega ao escritor de copy sem prova catalogada, e tudo que não tem prova vem marcado como gap — para que ninguém escreva o que o compliance vetará.
