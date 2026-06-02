---
id: authority.testimonial-vault
title: "Cofre de Depoimentos"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
tags: [authority, testimonial, social-proof, consent, voc, evidence]
---

# Cofre de Depoimentos

## Propósito

Este é o **cofre dos depoimentos** — as falas de clientes na própria voz deles, guardadas com a permissão de uso anexada. Um depoimento bom não elogia; ele conta uma transformação específica e desarma uma objeção que o avatar tem. A voz crua do cliente vence porque o avatar se reconhece nela.

O dono é o [`proof-credibility-curator`](../agents/proof-credibility-curator.md), com alimentação do [`avatar-voc-investigator`](../agents/avatar-voc-investigator.md), que colhe verbatims na mineração de voz do cliente. A regra inegociável deste cofre: **nenhum depoimento sai sem permissão de uso registrada**. Sem o consentimento, o depoimento fica trancado.

O cofre serve os escritores de copy do D4, que escolhem o depoimento por objeção. Ele também alimenta o [`media-kit.md`](media-kit.md) e o trabalho de PR. Cada fala vira munição rastreável, ligada a um claim no [`claim-registry`](../data/registries/claim-registry.md).

## Estrutura / Schema

Cada depoimento é um registro. Campos obrigatórios:

| Campo | O que registrar |
|---|---|
| `testimonial_id` | slug único, ex.: `depo-carla-dormiu-melhor` |
| `quote` | a fala literal do cliente (sem reescrever) |
| `author` | nome/perfil de quem falou |
| `avatar_match` | qual segmento de avatar representa |
| `objection_addressed` | a objeção que esta fala desarma |
| `format` | `texto` \| `áudio` \| `vídeo` \| `print-rede` |
| `result_linked` | resultado citado (ref a [`results-database.md`](results-database.md), se houver) |
| `consent_status` | `pending` \| `granted` \| `revoked` |
| `consent_scope` | onde pode usar (site, anúncio, mailer, PR) |
| `consent_doc` | link do termo de permissão assinado |
| `proof_id` | linha-espelho no [`proof-registry`](../data/registries/proof-registry.md) |

### Tracker (semeado vazio)

| testimonial_id | author | objection_addressed | format | consent_status | consent_scope | proof_id |
|---|---|---|---|---|---|---|
| `depo-exemplo-0001` _(EXEMPLO — apagar)_ | Carla M. (amostra) | "não tenho tempo" | vídeo | granted | site, anúncio | `proof-exemplo-0001` |

## Como coletar & verificar

1. Capture o depoimento na voz do cliente — não edite a fala para "melhorar".
2. Identifique qual objeção a fala desarma e marque `objection_addressed`.
3. Colha o **termo de permissão de uso** assinado: nome, imagem, escopo, prazo. Anexe em `consent_doc`.
4. Defina `consent_scope` — um depoimento liberado para site pode não estar liberado para anúncio pago.
5. Espelhe no [`proof-registry`](../data/registries/proof-registry.md) com `proof_type: testimonial`.

## Regras de uso & compliance

- **Permissão de uso é obrigatória.** Sem `consent_status: granted` + `consent_doc`, o depoimento não sai do cofre.
- Respeite o `consent_scope`: usar fora do escopo autorizado viola o consentimento.
- Não edite a fala a ponto de mudar o sentido; corte é permitido, distorção não.
- Depoimento que cita resultado atípico exige disclaimer, conforme [`../docs/compliance-policy.md`](../docs/compliance-policy.md).
- FTC/CDC: depoimento deve refletir experiência real e típica, ou trazer ressalva.
- Consentimento revogado (`revoked`) retira a fala de toda peça imediatamente.

## Liga com

- [`case-study-library.md`](case-study-library.md) — a fala vive dentro do caso completo.
- [`social-proof-inventory.md`](social-proof-inventory.md) e [`proof-asset-index.md`](proof-asset-index.md).
- [`media-kit.md`](media-kit.md) — depoimentos selecionados para imprensa.
- Agentes: [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (dono), [`avatar-voc-investigator`](../agents/avatar-voc-investigator.md) (alimenta), [`compliance-auditor`](../agents/compliance-auditor.md) (consentimento).
- Registries: [`proof-registry`](../data/registries/proof-registry.md), [`claim-registry`](../data/registries/claim-registry.md), [`objection-registry`](../data/registries/objection-registry.md).
