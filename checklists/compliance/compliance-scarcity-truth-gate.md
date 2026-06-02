---
id: checklist.compliance.compliance-scarcity-truth-gate
title: "Gate — Escassez Verdadeira (★ VETO: urgência 100% real)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [scarcity-urgency-engine, proof-to-claim-chain]
registries: [decision-registry, claim-registry]
tags: [gate, compliance, escassez, urgencia, veto, truthful-scarcity, d7]
---

# Gate — Escassez Verdadeira (★ VETO)

## Propósito
Este gate prova que **cada escassez e cada urgência da campanha é 100% verdadeira** — deadline que de fato fecha, vaga que de fato esgota, lote que de fato sobe. É um dos cinco gates de **veto** do `compliance-auditor` e a aplicação direta do princípio não-negociável `truthful_scarcity`. Ele existe porque escassez falsa é a mentira que mais destrói confiança e mais expõe a risco legal: um contador que reinicia, um "últimas 50 vagas" sem 50 no inventário, um falso lote. Cada gatilho é cruzado com o `asset-inventory-tracker` e o `run-of-show` via [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md): o limite bate com um número real? O deadline fecha de verdade? Urgência inventada **veta** a peça. E este é o veto mais duro do squad: escassez falsa **não tem override** — nem o `offerbook-chief` pode liberá-la.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (cruza cada gatilho de escassez com a realidade e **veta** a falsa; `config.yaml: agents` veto=true). O `launch-producer` e o `events-logistics-coordinator` corrigem a escassez na origem; o `offerbook-chief` arbitra apenas o que tem override (e escassez falsa não tem).
- **Artefato inspecionado:** **cada** deadline, "últimas vagas", lote ou contagem regressiva no `vsl-script`, `email-sms-sequences`, `mailers-inserts`, `ad-matrix` e `run-of-show`, cruzado com o `asset-inventory-tracker` (o número real) e o calendário do lançamento.

## Condição de Passagem
Cada gatilho de escassez ou urgência bate com um limite real e verificável de quantidade ou prazo, sem nenhum contador que reinicia nem vaga perpétua.

## Itens
1. **Deadline que fecha.** Verificar: cada prazo de fato encerra a oferta no run-of-show; nenhum contador reinicia sozinho.
2. **Vagas reais.** Verificar: cada "últimas N vagas" bate com N no `asset-inventory-tracker`, não é número inventado.
3. **Lote verdadeiro.** Verificar: cada subida de lote/preço de fato ocorre na data anunciada.
4. **Bônus de escassez real.** Verificar: bônus por tempo limitado de fato saem quando o prazo passa.
5. **Limite ancorado em capacidade.** Verificar: limites de vaga em ofertas high-ticket batem com a capacidade real de atendimento.
6. **Sem urgência inventada.** Verificar: nenhuma peça cria urgência sem um fato que a sustente (`scarcity-urgency-engine`).
7. **Extensão só por causa real.** Verificar: qualquer extensão de prazo só ocorre por motivo verdadeiro (ex.: instabilidade técnica real), nunca como tática.

## Evidência Exigida
Para marcar ✅: linkar o cruzamento de cada gatilho com o `asset-inventory-tracker` e o `run-of-show` (itens 1–3), a saída real dos bônus por prazo (item 4), a âncora de capacidade das vagas high-ticket (item 5) e a justificativa de qualquer extensão (item 7). O veredito aponta para o `decision-registry`.

## Protocolo de Falha
Escassez falsa → **VETO** da peça; o `compliance-auditor` registra `{peça, gatilho, número_real}` no `decision-registry` e devolve ao [`launch-producer`](../../agents/launch-producer.md) ou ao [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) para ancorar o gatilho em um limite real ou removê-lo. A peça **não vai ao blackbook** até a escassez ser verdadeira. **Sem override:** diferente dos demais gates, escassez falsa **não pode ser liberada** nem pelo [`offerbook-chief`](../../agents/offerbook-chief.md) — a política não admite exceção. Re-entrada: ancorar ou remover o gatilho, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`claim-registry`](../../data/registries/claim-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Política: [`compliance-policy`](../../docs/compliance-policy.md)
- Agentes: [`compliance-auditor`](../../agents/compliance-auditor.md) · [`launch-producer`](../../agents/launch-producer.md) · [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`compliance-claim-backing-gate`](compliance-claim-backing-gate.md) · [`compliance-disclaimers-gate`](compliance-disclaimers-gate.md) · [`compliance-data-privacy-gate`](compliance-data-privacy-gate.md) · [`compliance-sector-rules-gate`](compliance-sector-rules-gate.md)
