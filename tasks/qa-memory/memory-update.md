---
id: task.qa-memory.memory-update
title: "Task — Atualizar a Memória do Squad"
type: task
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
frameworks: [proof-to-claim-chain]
checklists:
  - final-delivery-checklist
registries: [control-registry, lessons-learned-registry, swipe-registry]
tags: [qa, memoria, registries, swipe, licoes-aprendidas, controles, reuso, d7]
---

# Task — Atualizar a memória do squad: transformar o lançamento entregue em conhecimento reutilizável

## Objetivo
Extrair do blackbook fechado tudo que vira memória reutilizável — controles vencedores, padrões de swipe, lições aprendidas — e gravá-lo nos registries, para que o próximo lançamento reuse antes de recriar (`memory_before_repetition`). O estado-pronto: o `control-registry`, o `lessons-learned-registry` e o `swipe-registry` atualizados com os ativos do lançamento, cada entrada rastreável à sua fonte, e o final-delivery-checklist verde — o ciclo do squad fechado.

## Agente dono
[`knowledge-librarian`](../../agents/knowledge-librarian.md). Registra tudo que vira memória reutilizável (conforme o [`ARCHITECTURE.md`](../../ARCHITECTURE.md): "Knowledge Librarian registra tudo que vira memória reutilizável"). Sem poder de veto.

## Gatilho / Quando
Roda em D7, por último: ativa quando a [`assemble-blackbook`](assemble-blackbook.md) entrega o blackbook aprovado e o `compliance-verdict` é APROVADO. É a etapa final de toda composição que vende (`run-full-launch`, `run-single-promo`). Conforme `config.yaml: defaults.mandatory_registry_update: true` e `registry_on_completion: true`. Blackbook não fechado → **não registrar memória parcial**; aguardar a montagem.

## Inputs (Consome)
- `artifact.launch-blackbook` — o pacote final do lançamento, fonte de todos os ativos a memorizar.
- `decision.compliance-verdict` — **APROVADO**: só material conforme entra na memória (nada com claim sem lastro vira swipe).
- `decision.voice-verdict` — os vereditos de voz por peça, para marcar quais controles passaram limpos.
- `artifact.ad-matrix` / `artifact.vsl-script` / `artifact.email-sms-sequences` — as peças cujos ganchos/estruturas vencedoras viram swipe (em redação original).

## Procedimento
1. **Confirmar a entrada.** Blackbook fechado e `compliance-verdict` APROVADO. Caso contrário, aguardar.
2. **Catalogar os controles.** Atualizar o `control-registry` com cada peça final (VSL, e-mails, ads, mailers) e seu status (`live`/`winner` quando houver dado de desempenho), ligando ao veredito de voz e de compliance.
3. **Extrair o swipe.** Identificar os ganchos, sequências e estruturas que funcionaram e gravá-los no `swipe-registry` como padrões **originais** (estrutura/princípios, nunca copy literal — cada entrada com categoria e ângulo). Aplicar a disciplina de [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md): um swipe só carrega o claim cujo lastro o Offer Book provou.
4. **Registrar as lições aprendidas.** Consolidar no `lessons-learned-registry` o que funcionou e o que quebrou — execução do lançamento, deliverability, fulfillment, leaderboard de afiliados, ângulos de PR, decisões que se provaram certas ou erradas — cada lição com o contexto e a recomendação para o próximo ciclo.
5. **Rastrear cada entrada à fonte.** Toda entrada de memória aponta para o artefato/decisão de origem no blackbook (rastreabilidade > eloquência).
6. **Verificar a não-duplicação.** Antes de criar uma entrada, checar se já existe um padrão equivalente; consolidar em vez de duplicar.
7. **Self-verify (red-team).** "Algum claim sem lastro escapou para o swipe?" "Alguma lição ficou sem recomendação acionável?" "O próximo lançamento acharia isto pela busca?" Corrigir antes de fechar.
8. **Rodar o final-delivery-checklist e fechar.** Confirmar que os três registries estão atualizados, rastreáveis e sem duplicata; marcar o ciclo do squad como concluído.

## Frameworks
[`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md).

## Outputs (Produz)
- [`control-registry`](../../data/registries/control-registry.md) atualizado — cada peça final com status e vereditos ligados.
- [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md) atualizado — lições do lançamento com contexto e recomendação.
- [`swipe-registry`](../../data/registries/swipe-registry.md) atualizado — padrões originais (ganchos/sequências/estruturas vencedoras) com categoria e ângulo.

## Definition of Done
- Blackbook fechado e `compliance-verdict` APROVADO confirmados antes de registrar.
- Os três registries (control, lessons-learned, swipe) atualizados com os ativos do lançamento.
- Cada swipe é redação **original** e só carrega claim com lastro (zero claim sem prova na memória).
- Cada entrada rastreável à sua fonte; sem duplicata (padrões equivalentes consolidados).
- O final-delivery-checklist verde; o ciclo do squad fechado.

## Gates
[`final-delivery-checklist`](../../checklists/final-delivery-checklist.md).

## Handoff
**Fim do ciclo.** A memória atualizada alimenta o **próximo** lançamento: o [`offerbook-chief`](../../agents/offerbook-chief.md) e o [`offer-squad-architect`](../../agents/offer-squad-architect.md) consultam o `lessons-learned-registry` na [`intake-and-scope`](../planning/intake-and-scope.md) (memória antes de repetição), os autores de copy reusam o `swipe-registry`, e os controles vencedores do `control-registry` viram baseline. **Contrato:** nenhuma memória parcial ou não-conforme entra nos registries — só ativos de um lançamento fechado, aprovado no compliance e rastreáveis à fonte.
