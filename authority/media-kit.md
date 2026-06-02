---
id: authority.media-kit
title: "Media Kit"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
tags: [authority, media-kit, pr, brand, press, assets]
---

# Media Kit

## Propósito

Este arquivo especifica o **media kit** do squad — o pacote pronto que entregamos a jornalistas, podcasters, parceiros e afiliados para que falem da marca com precisão. Um media kit bom remove atrito: o veículo recebe bio, fatos, números, fotos e contato em um só lugar, e a chance de uma colocação de imprensa sobe. Ele transforma a marca em fonte fácil de citar.

O dono é o [`pr-brand-strategist`](../agents/pr-brand-strategist.md), com curadoria de prova do [`proof-credibility-curator`](../agents/proof-credibility-curator.md). A regra: tudo no kit é **verdadeiro e verificável** — cada número aponta para o banco que o sustenta. Um fact sheet com dado sem lastro vira veto do [`compliance-auditor`](../agents/compliance-auditor.md), porque o kit circula fora do nosso controle e o erro se propaga.

O kit puxa material dos outros bancos de autoridade: bio da [`founder-story-framework.md`](founder-story-framework.md), números do [`data-points-bank.md`](data-points-bank.md), colocações do [`pr-placements.md`](pr-placements.md), prêmios de [`awards-certifications.md`](awards-certifications.md). Ele é a vitrine consolidada da autoridade.

## Estrutura / Schema

O media kit é um pacote com seções fixas. Componentes a montar:

| Componente | O que conter |
|---|---|
| `boilerplate` | parágrafo-padrão da marca (1 curto, 1 longo) |
| `founder_bio` | bio do fundador (ver [`founder-story-framework.md`](founder-story-framework.md)) |
| `fact_sheet` | fatos e números-chave, cada um com fonte |
| `key_stats` | estatísticas destacadas (ref a [`data-points-bank.md`](data-points-bank.md)) |
| `press_clips` | colocações anteriores (ref a [`pr-placements.md`](pr-placements.md)) |
| `headshots` | fotos em alta resolução (links + crédito) |
| `logo_pack` | logos em formatos e versões, com guia de uso |
| `spokespeople` | porta-vozes disponíveis e temas |
| `contact` | contato de imprensa + prazo de resposta |
| `usage_terms` | regras de uso de imagem e marca |

### Esqueleto do kit

```
# Media Kit — {{marca}}
## Sobre (boilerplate curto / longo)
## Fundador ({{founder_bio}})
## Fatos & Números ({{fact_sheet}} — cada item com fonte)
## Na Imprensa ({{press_clips}})
## Imagens ({{headshots}} · {{logo_pack}} + guia de uso)
## Porta-vozes & Temas ({{spokespeople}})
## Contato de Imprensa ({{contact}})
```

## Como coletar & verificar

1. Monte cada seção puxando do banco de autoridade correspondente; não recrie números, referencie a fonte.
2. Para cada item do `fact_sheet` e `key_stats`, anexe a fonte verificável — o kit não carrega dado órfão.
3. Prepare imagens em alta resolução com crédito de foto e direito de uso confirmado.
4. Defina `usage_terms` claros: como usar logo, o que pode e o que não pode ser editado.
5. Versione o kit; quando um número muda, atualize aqui e marque a versão para não circular dado velho.

## Regras de uso & compliance

- Todo número do kit aponta para fonte verificável; fact sheet com dado sem lastro = **veto** do [`compliance-auditor`](../agents/compliance-auditor.md).
- O kit circula fora do nosso controle — por isso o rigor de fonte é maior, não menor.
- Imagens e logos de terceiros (parceiros, veículos) só entram com direito de uso confirmado.
- Boilerplate e bio seguem a voz da marca e os disclaimers de [`../docs/compliance-policy.md`](../docs/compliance-policy.md).
- Dado desatualizado é retirado da versão vigente; circular número velho é risco de marca.

## Liga com

- [`founder-story-framework.md`](founder-story-framework.md) — origem da bio.
- [`pr-placements.md`](pr-placements.md), [`data-points-bank.md`](data-points-bank.md), [`awards-certifications.md`](awards-certifications.md), [`credibility-builders.md`](credibility-builders.md).
- [`proof-asset-index.md`](proof-asset-index.md) — índice das provas usadas no kit.
- Agentes: [`pr-brand-strategist`](../agents/pr-brand-strategist.md) (dono), [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (curadoria de prova), [`compliance-auditor`](../agents/compliance-auditor.md) (veto).
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md).
