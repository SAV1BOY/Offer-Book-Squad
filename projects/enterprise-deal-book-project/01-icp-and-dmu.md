---
id: project.enterprise-deal-book-project.01-icp-and-dmu
title: "Fase 01 — ICP & Unidade de Decisão (DMU)"
type: project-phase
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
consumes:
  - artifact.account-icp-sketch
  - decision.scope-one-sentence
  - template.strategy.avatar-icp
  - template.strategy.voc-verbatim-bank
produces:
  - artifact.account-icp
  - artifact.dmu-map
  - artifact.objection-belief-map-by-role
  - artifact.proof-bank
tags: [project-phase, enterprise, b2b, icp, dmu, comite, meddic, spin, prova, d1]
---

# Fase 01 — ICP & Unidade de Decisão (DMU)

## Objetivo da Fase
Reconstruir a conta-alvo e mapear o comitê que decide, papel por papel. Em B2B, uma mensagem genérica perde o comprador econômico ou o influenciador técnico. Esta fase entrega o ICP da conta e o mapa da DMU — usuário, comprador econômico, influenciador técnico, campeão, bloqueador e mentor — cada um com sua dor, seu ganho, a métrica que importa e a objeção própria. Também monta o banco de prova por papel, porque o que convence o usuário (facilidade) não convence o CFO (ROI). O estado-pronto é a DMU completa, o VOC por papel com verbatims rastreáveis, o mapa de objeções por papel e a prova casada a cada papel. A régua MEDDIC já manda: sem comprador econômico mapeado, não há previsão confiável; e o campeão é testado, não presumido.

## Critério de Entrada
A [`00-brief`](00-brief.md) entrega o `artifact.account-icp-sketch` e a frase de escopo. Pré-condição: existe um recorte de conta ou vertical e acesso a alguma voz dos stakeholders (entrevistas, calls, e-mails, pesquisa de mercado). Sem fonte de VOC dos papéis, o banco é marcado abaixo do piso e sinalizado — verbatim fabricado é falha grave. Se a conta abriga dois comitês com processos distintos, a fase segmenta. O [`objection-registry`](../../data/registries/objection-registry.md) é a fonte que esta fase escreve; o [`proof-registry`](../../data/registries/proof-registry.md) recebe a prova por papel.

## Agentes & Tasks
- **Task [`build-avatar-voc`](../../tasks/intelligence/build-avatar-voc.md)** — dono [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md). Mapeia o ICP e a DMU.
- **Task [`curate-proof`](../../tasks/intelligence/curate-proof.md)** — dono [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). Casa prova a cada papel.
- **Task [`run-market-intel`](../../tasks/intelligence/run-market-intel.md)** — dono [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md), para a sofisticação do comprador.

## Passos
1. Detalhe o ICP da conta: porte, vertical, gatilho de compra, contexto de negócio.
2. Liste os papéis da DMU com [`avatar-voc-investigator/dmu-mapping-b2b`](../../frameworks/avatar-voc-investigator/dmu-mapping-b2b.md): usuário, comprador econômico, influenciador técnico, campeão, bloqueador, mentor.
3. Capture o VOC de cada papel com [`voc-mining`](../../frameworks/avatar-voc-investigator/voc-mining.md): dor, ganho, métrica que importa, linguagem própria.
4. Identifique a Dor de negócio (o "I" de MEDDIC) com perguntas no estilo SPIN — problema, implicação, valor — ref [`reference/books/b2b-enterprise/rackham-spin-selling`](../../reference/books/b2b-enterprise/rackham-spin-selling.md).
5. Mapeie a objeção por papel com [`objection-belief-mapping`](../../frameworks/avatar-voc-investigator/objection-belief-mapping.md): a do usuário difere da do CFO e da do técnico.
6. Identifique o comprador econômico (o "E") e teste o campeão (o "C") — peça uma ação que prove o poder dele, ref [`reference/books/b2b-enterprise/meddic-meddpicc`](../../reference/books/b2b-enterprise/meddic-meddpicc.md).
7. Case a prova por papel com [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md): ROI para o CFO, segurança para o técnico, adoção para o usuário.
8. Cheque a cobertura: todo papel-chave tem dor, métrica, objeção e prova. Escreva no `objection-registry` e no `proof-registry`.

## Artefatos Produzidos
- `artifact.account-icp` — o ICP detalhado da conta-alvo.
- `artifact.dmu-map` — papel → dor/ganho → métrica → objeção → mensagem → prova.
- `artifact.objection-belief-map-by-role` — objeção e falsa crença por papel.
- `artifact.proof-bank` — a prova casada a cada papel.
- Registries escritos: [`objection-registry`](../../data/registries/objection-registry.md), [`proof-registry`](../../data/registries/proof-registry.md), [`claim-registry`](../../data/registries/claim-registry.md).

## Gates
- [`avatar/avatar-voc-verbatim-gate`](../../checklists/avatar/avatar-voc-verbatim-gate.md) — VOC com verbatims rastreáveis por papel.
- [`proof-checklist`](../../checklists/proof-checklist.md) — cada claim com prova por papel.
- [`avatar-voc-checklist`](../../checklists/avatar-voc-checklist.md) — a cobertura da DMU está completa.

## Critério de Saída
O ICP da conta está detalhado; a DMU cobre todos os papéis; cada papel tem dor, métrica, objeção e prova; o comprador econômico está mapeado e o campeão foi testado; o VOC por papel tem verbatims rastreáveis. Os gates de avatar e prova estão verdes; as objeções e a prova estão nos registries. A próxima fase é a [`02-value-and-pricing-packaging`](02-value-and-pricing-packaging.md), que recebe a DMU e a prova para quantificar o valor que o comprador econômico precisa aprovar e empacotar a oferta enterprise.
