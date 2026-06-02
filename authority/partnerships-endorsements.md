---
id: authority.partnerships-endorsements
title: "Parcerias e Endossos"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
tags: [authority, partnerships, endorsements, partners, influencers, trust]
---

# Parcerias e Endossos

## Propósito

Este arquivo cataloga as **parcerias e endossos** da marca — marcas associadas, plataformas integradas, instituições parceiras, especialistas que recomendam, influenciadores que endossam. A autoridade aqui é emprestada e transferida: quando uma marca ou nome respeitado se associa a nós, parte da confiança dele vem junto. O avatar pensa "se eles confiam, posso confiar".

O dono é o [`pr-brand-strategist`](../agents/pr-brand-strategist.md), com curadoria de prova do [`proof-credibility-curator`](../agents/proof-credibility-curator.md). A regra: cada parceria e endosso é **real e autorizado**. Citar parceria que não existe, usar logo de marca sem direito, ou inventar endosso são enganosos e viram veto do [`compliance-auditor`](../agents/compliance-auditor.md). Endosso de pessoa exige autorização de uso da imagem e do nome, como um depoimento.

Estes ativos alimentam os [`credibility-builders.md`](credibility-builders.md), a faixa de parceiros na página e o [`media-kit.md`](media-kit.md). Endosso pago ou com contrapartida exige divulgação clara (FTC) — relação comercial não revelada é enganosa.

## Estrutura / Schema

Registre cada parceria ou endosso como uma linha. Colunas obrigatórias:

| Coluna | Tipo | O que registrar |
|---|---|---|
| `partner_id` | slug | id único, ex.: `parc-plataforma-x` |
| `kind` | enum | `parceria` \| `integração` \| `endosso-especialista` \| `endosso-influencer` \| `instituição` |
| `partner_name` | string | nome da marca/pessoa/instituição |
| `nature` | string | o que a relação é (contrato, integração, recomendação) |
| `is_paid` | bool | há pagamento ou contrapartida? (exige divulgação) |
| `authorization` | enum | `autorizado` \| `pendente` \| `negado` (uso de nome/logo) |
| `auth_doc` | URL/path | contrato ou termo que comprova |
| `usage_scope` | string | onde pode usar nome/logo (site, anúncio, kit) |
| `verifiable` | bool | a relação é checável? |
| `proof_id` | ref | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |

### Tracker (semeado vazio)

| partner_id | kind | partner_name | is_paid | authorization | usage_scope | verifiable | proof_id |
|---|---|---|---|---|---|---|---|
| `parc-exemplo-0001` _(EXEMPLO — apagar)_ | parceria | Plataforma X (amostra) | false | autorizado | site, kit | true | `proof-exemplo-0001` |

## Como coletar & verificar

1. Para cada parceria, guarde o `auth_doc` — contrato, termo de uso de marca ou autorização escrita.
2. Defina `usage_scope`: uma marca pode autorizar o logo no site mas não em anúncio pago.
3. Marque `is_paid: true` em endosso com pagamento ou contrapartida — isso aciona a divulgação obrigatória.
4. Para endosso de pessoa, colha autorização de nome e imagem, como no [`testimonial-vault.md`](testimonial-vault.md).
5. Espelhe no [`proof-registry`](../data/registries/proof-registry.md) com `proof_type: endorsement`.

## Regras de uso & compliance

- Só parceria/endosso com `authorization: autorizado` e dentro do `usage_scope` entra na copy.
- Logo de marca sem direito, parceria inexistente ou endosso inventado = **veto** do [`compliance-auditor`](../agents/compliance-auditor.md).
- Endosso pago (`is_paid: true`) exige divulgação clara da relação comercial (FTC), conforme [`../docs/compliance-policy.md`](../docs/compliance-policy.md).
- Autorização revogada retira o nome/logo de toda peça imediatamente.
- Endosso de especialista não vira promessa de resultado nem alegação regulada (saúde, finanças).

## Liga com

- [`credibility-builders.md`](credibility-builders.md) — parceiro vira sinal de autoridade.
- [`awards-certifications.md`](awards-certifications.md), [`pr-placements.md`](pr-placements.md), [`media-kit.md`](media-kit.md).
- [`proof-asset-index.md`](proof-asset-index.md) — índice-mestre.
- Agentes: [`pr-brand-strategist`](../agents/pr-brand-strategist.md) (dono), [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (curadoria), [`compliance-auditor`](../agents/compliance-auditor.md) (veto + divulgação). Relação com [`affiliate-program-architect`](../agents/affiliate-program-architect.md) em endossos de afiliados.
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md).
