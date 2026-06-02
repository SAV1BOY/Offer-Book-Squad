---
id: authority.awards-certifications
title: "Prêmios e Certificações"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
tags: [authority, awards, certifications, credentials, badges, trust]
---

# Prêmios e Certificações

## Propósito

Este arquivo cataloga os **prêmios, certificações e credenciais** da marca, do fundador e da equipe — selos de qualidade, premiações setoriais, certificações técnicas, registros profissionais, acreditações. São sinais de autoridade institucional: uma certificação reconhecida diz ao avatar que um terceiro confiável já validou competência ou qualidade. Eles reduzem o risco percebido antes do pitch.

O dono é o [`proof-credibility-curator`](../agents/proof-credibility-curator.md). A regra inegociável: cada selo é **real, vigente e verificável**. Certificação vencida, prêmio inventado ou credencial exagerada são enganosos e viram veto do [`compliance-auditor`](../agents/compliance-auditor.md). Selo de "certificado por X" exige o documento ou a página oficial que comprove, e exige que esteja dentro do prazo de validade.

Estes ativos alimentam os [`credibility-builders.md`](credibility-builders.md), o rodapé da página, a bio do [`media-kit.md`](media-kit.md) e o pitch de PR. Em setores regulados (saúde, finanças, jurídico), a credencial certa é pré-requisito para até poder anunciar.

## Estrutura / Schema

Registre cada prêmio ou certificação como uma linha. Colunas obrigatórias:

| Coluna | Tipo | O que registrar |
|---|---|---|
| `cert_id` | slug | id único, ex.: `cert-iso-9001-2025` |
| `kind` | enum | `prêmio` \| `certificação` \| `credencial` \| `acreditação` \| `selo` |
| `name` | string | nome oficial do prêmio/certificação |
| `issuer` | string | entidade emissora (reconhecida?) |
| `holder` | string | quem detém (marca, fundador, equipe) |
| `issue_date` | data | quando foi concedido |
| `expiry_date` | data | validade (ou `permanente`) |
| `status` | enum | `vigente` \| `expirado` \| `em-renovação` |
| `proof_link` | URL/path | certificado, registro ou página oficial |
| `verifiable` | bool | terceiro consegue conferir? |
| `proof_id` | ref | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |

### Tracker (semeado vazio)

| cert_id | kind | name | issuer | holder | status | expiry_date | verifiable | proof_id |
|---|---|---|---|---|---|---|---|---|
| `cert-exemplo-0001` _(EXEMPLO — apagar)_ | certificação | ISO 9001 (amostra) | Org. X | marca | vigente | 2027-06-02 | true | `proof-exemplo-0001` |

## Como coletar & verificar

1. Para cada selo, guarde o `proof_link` — o certificado, o número de registro ou a página oficial do emissor.
2. Registre `issue_date` e `expiry_date`; monte um alerta de renovação antes do vencimento.
3. Confirme que o emissor é reconhecido — certificação de entidade obscura tem força fraca e pode confundir.
4. Marque `status: expirado` assim que vencer; selo expirado sai da copy no mesmo dia.
5. Espelhe no [`proof-registry`](../data/registries/proof-registry.md) com `proof_type: endorsement` ou `media-mention`, conforme o caso.

## Regras de uso & compliance

- Só selo `vigente` e `verifiable: true` entra na copy; certificação expirada ou em renovação não.
- Prêmio ou credencial inventado, ou exagerado, é enganoso = **veto** do [`compliance-auditor`](../agents/compliance-auditor.md).
- Respeite as regras de uso do emissor — alguns selos têm guia de marca próprio.
- Em setores regulados, a credencial é pré-requisito legal para anunciar (Anvisa, CVM, OAB/CFM/CFC), conforme [`../docs/compliance-policy.md`](../docs/compliance-policy.md).
- Credencial individual não vira garantia de resultado para o cliente.

## Liga com

- [`credibility-builders.md`](credibility-builders.md) — o selo vira sinal de autoridade.
- [`partnerships-endorsements.md`](partnerships-endorsements.md) — endossos e selos de parceiros.
- [`media-kit.md`](media-kit.md) e [`proof-asset-index.md`](proof-asset-index.md).
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (dono), [`pr-brand-strategist`](../agents/pr-brand-strategist.md), [`compliance-auditor`](../agents/compliance-auditor.md) (veto + regra setorial).
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md).
