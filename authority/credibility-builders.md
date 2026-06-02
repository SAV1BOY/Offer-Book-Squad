---
id: authority.credibility-builders
title: "Construtores de Credibilidade"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
tags: [authority, credibility, signals, media, partners, numbers, trust]
---

# Construtores de Credibilidade

## Propósito

Este arquivo cataloga os **sinais de autoridade** que fazem o avatar confiar antes mesmo da prova de resultado — menções de mídia, números de escala, logos de parceiros, anos de experiência, volume atendido. São os atalhos de confiança que o cérebro do comprador usa: "se a Forbes citou e milhares já compraram, deve ser sério".

O dono é o [`proof-credibility-curator`](../agents/proof-credibility-curator.md), em parceria com o [`pr-brand-strategist`](../agents/pr-brand-strategist.md), que gera novas menções e parcerias. A regra: cada sinal aqui é **real e verificável**. Logo de imprensa sem matéria que o sustente, ou "número de clientes" inflado, viram veto do [`compliance-auditor`](../agents/compliance-auditor.md).

Estes sinais entram cedo na copy — no topo da VSL, no rodapé da página, no media kit — para baixar a guarda antes do pitch. Eles não substituem prova de resultado; eles abrem a porta para ela.

## Estrutura / Schema

Catalogue cada sinal por categoria. Campos:

| Campo | O que registrar |
|---|---|
| `signal_id` | slug único, ex.: `cred-citado-forbes` |
| `category` | `mídia` \| `número-escala` \| `parceiro` \| `experiência` \| `volume` \| `certificação` |
| `claim_text` | como o sinal aparece na copy (frase exata) |
| `value` | o número ou nome (ex.: "+10.000 alunos", "Forbes") |
| `source_link` | onde a prova do sinal vive (matéria, painel, contrato) |
| `verifiable` | há como conferir? |
| `usage_context` | onde usar (topo de VSL, rodapé, media kit, bio) |
| `proof_id` | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |
| `updated` | `YYYY-MM-DD` |

### Categorias de sinal

- **Mídia:** onde a marca/fundador apareceu (ver [`pr-placements.md`](pr-placements.md)).
- **Números de escala:** clientes atendidos, unidades vendidas, anos de mercado.
- **Parceiros:** marcas, plataformas, instituições associadas (ver [`partnerships-endorsements.md`](partnerships-endorsements.md)).
- **Certificações:** selos e credenciais (ver [`awards-certifications.md`](awards-certifications.md)).

## Como coletar & verificar

1. Liste todos os sinais existentes e a fonte que prova cada um.
2. Para mídia, guarde o link da matéria; para números, o print do painel; para parceria, o contrato ou página oficial.
3. Marque `verifiable: false` em sinal sem fonte — ele não vai para a copy até ganhar lastro.
4. Defina `usage_context` para cada um — número de escala brilha no topo; certificação no rodapé.
5. Espelhe no [`proof-registry`](../data/registries/proof-registry.md) com o `proof_type` adequado.

## Regras de uso & compliance

- Todo sinal usado em copy tem `verifiable: true` e fonte anexada.
- "Visto na Forbes" exige matéria real; logo de imprensa sem cobertura = enganoso = **veto**.
- Número de escala não pode ser arredondado para cima nem inflado; use o número defensável.
- Certificação precisa estar vigente; selo expirado sai da copy.
- Conformidade com [`../docs/compliance-policy.md`](../docs/compliance-policy.md): publicidade não enganosa (CDC) e endorsements honestos (FTC).

## Liga com

- [`pr-placements.md`](pr-placements.md), [`partnerships-endorsements.md`](partnerships-endorsements.md), [`awards-certifications.md`](awards-certifications.md), [`data-points-bank.md`](data-points-bank.md).
- [`media-kit.md`](media-kit.md) e [`proof-asset-index.md`](proof-asset-index.md).
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md), [`pr-brand-strategist`](../agents/pr-brand-strategist.md), [`compliance-auditor`](../agents/compliance-auditor.md).
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md).
