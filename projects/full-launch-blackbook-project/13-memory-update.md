---
id: project.full-launch-blackbook-project.13-memory-update
title: "Fase 13 — Atualização da Memória"
type: project-phase
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
consumes:
  - artifact.launch-blackbook
  - decision.compliance-verdict
  - decision.voice-verdict
  - artifact.ad-matrix
  - artifact.vsl-script
  - artifact.email-sms-sequences
produces:
  - registry.control-update
  - registry.lessons-learned-update
  - registry.swipe-update
tags: [project-phase, qa, memoria, registries, swipe, licoes-aprendidas, controles, reuso, d7]
---

# Fase 13 — Atualização da Memória

## Objetivo da Fase
Extrair do blackbook fechado tudo que vira memória reutilizável — controles vencedores, padrões de swipe, lições aprendidas — e gravá-lo nos registries, para que o próximo lançamento reuse antes de recriar. O estado-pronto é o control-registry, o lessons-learned-registry e o swipe-registry atualizados com os ativos do lançamento, cada entrada rastreável à sua fonte, e o final-delivery-checklist verde — o ciclo do squad fechado. Esta é a última fase do projeto: ela transforma o trabalho entregue em ativo que acelera o próximo ciclo (memória antes de repetição).

## Critério de Entrada
A Fase 12 entrega o `artifact.launch-blackbook` fechado e o `decision.compliance-verdict` APROVADO — só material conforme entra na memória (nada com claim sem lastro vira swipe). O `decision.voice-verdict` por peça permite marcar quais controles passaram limpos. As peças de copy (`artifact.ad-matrix`, `artifact.vsl-script`, `artifact.email-sms-sequences`) entram como fonte dos ganchos e estruturas vencedoras. Pré-condição: o blackbook está fechado e o compliance APROVADO — blackbook não fechado não gera memória parcial. Conforme `config.yaml: defaults.mandatory_registry_update: true` e `registry_on_completion: true`. Os registries [`control-registry`](../../data/registries/control-registry.md), [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) e [`swipe-registry`](../../data/registries/swipe-registry.md) são escritos.

## Agentes & Tasks
- **Task [`memory-update`](../../tasks/qa-memory/memory-update.md)** — dono [`knowledge-librarian`](../../agents/knowledge-librarian.md). Registra tudo que vira memória reutilizável. Sem poder de veto.

## Passos
1. Confirme a entrada: blackbook fechado e compliance-verdict APROVADO. Caso contrário, aguarde.
2. Catalogue os controles: atualize o `control-registry` com cada peça final (VSL, e-mails, ads, mailers) e seu status, ligando ao veredito de voz e de compliance.
3. Extraia o swipe: grave os ganchos, sequências e estruturas vencedoras no `swipe-registry` como padrões originais (estrutura/princípios, nunca copy literal), com categoria e ângulo. Aplique a disciplina de [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md): um swipe só carrega o claim cujo lastro o Offer Book provou.
4. Registre as lições aprendidas: consolide no `lessons-learned-registry` o que funcionou e o que quebrou (execução, deliverability, fulfillment, leaderboard de afiliados, ângulos de PR), cada lição com contexto e recomendação.
5. Rastreie cada entrada à fonte: toda entrada aponta para o artefato/decisão de origem no blackbook.
6. Verifique a não-duplicação: antes de criar, cheque se já existe um padrão equivalente e consolide.
7. Self-verify com red-team: algum claim sem lastro escapou para o swipe? Alguma lição ficou sem recomendação acionável? O próximo lançamento acharia isto pela busca?
8. Rode o final-delivery-checklist e feche: os três registries atualizados, rastreáveis e sem duplicata; ciclo do squad concluído.

## Artefatos Produzidos
- Registry escrito: [`control-registry`](../../data/registries/control-registry.md) — cada peça final com status e vereditos ligados.
- Registry escrito: [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) — lições do lançamento com contexto e recomendação.
- Registry escrito: [`swipe-registry`](../../data/registries/swipe-registry.md) — padrões originais (ganchos/sequências/estruturas vencedoras) com categoria e ângulo.

## Gates
- [`final-delivery-checklist`](../../checklists/final-delivery-checklist.md)

## Critério de Saída
O blackbook fechado e o compliance-verdict APROVADO foram confirmados; os três registries (control, lessons-learned, swipe) estão atualizados com os ativos do lançamento; cada swipe é redação original e só carrega claim com lastro (zero claim sem prova na memória); cada entrada é rastreável à sua fonte; não há duplicata; o final-delivery-checklist está verde. O ciclo do squad está fechado. A memória atualizada alimenta o próximo lançamento: o chief e o architect a consultam na [`00-brief`](00-brief.md) do próximo caso, os autores reusam o swipe e os controles vencedores viram baseline. Esta é a fase final do projeto full-launch-blackbook.
