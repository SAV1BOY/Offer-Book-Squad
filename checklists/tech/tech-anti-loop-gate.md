---
id: checklist.tech.tech-anti-loop-gate
title: "Gate — Anti-Loop (sem redirecionamento circular, sem rota órfã, retry idempotente)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: tech-links-deliverability-engineer
frameworks: [launch/surge-ops]
registries: [decision-registry]
tags: [gate, tech, anti-loop, integracao, idempotencia, rota-orfa, d5]
---

# Gate — Anti-Loop

## Propósito
Este gate prova que **o fluxo do funil não entra em loop, não tem rota órfã e as integrações são idempotentes**. Ele existe porque um redirecionamento circular trava o cliente no meio da compra, e um retry não idempotente duplica o pedido. O caso clássico: o "não" do upsell encadeia para o downsell, cujo "não" aponta de volta ao upsell — o cliente roda em círculo e desiste. O `tech-links-deliverability-engineer` varre cada redirecionamento do `funnel-map`, quebra todo ciclo redirecionando o estado terminal para a página de obrigado ou a continuidade, e confirma que cada estado aponta para um destino real. Nas integrações (gateway→CRM→3PL), ele torna cada webhook idempotente com chave por pedido, para que o retry não gere duplicidade. Vale o princípio `traceability_before_eloquence`: cada estado tem destino conhecido. Este gate julga **só a integridade do fluxo e das integrações** — a capacidade sob carga é do `tech-load-test-gate`. Funil com rota ambígua não é consertado aqui: volta ao `funnel-architect`, porque engenheirar sobre ambiguidade gera o próprio loop que este gate previne.

## Dono & Escopo
- **owner_agent:** `tech-links-deliverability-engineer` (varre redirecionamentos, quebra ciclos e torna integrações idempotentes).
- **Artefato inspecionado:** o `funnel-map` + `decision.funnel-routes` (cada bifurcação→destino) e o plano de integração no `tech-deliverability-plan`. O resultado vai ao [`decision-registry`](../../data/registries/decision-registry.md). Gate consumido em `config.yaml: routing.plan-tech-deliverability`.

## Condição de Passagem
Nenhum redirecionamento circular, nenhuma rota órfã e cada integração crítica é idempotente sob retry.

## Itens
1. **Sem ciclo de redirecionamento.** Verificar: nenhum caminho do funil aponta de volta a um estado já visitado (ex.: 2º "não"→upsell).
2. **Sem rota órfã.** Verificar: cada estado/bifurcação do funil aponta para um destino real, sem beco sem saída.
3. **Estado terminal definido.** Verificar: todo caminho termina em página de obrigado, continuidade ou estado final claro.
4. **Webhooks idempotentes.** Verificar: gateway→CRM→3PL usam chave de idempotência por pedido; o retry não duplica.
5. **Sem loop de disparo de e-mail.** Verificar: nenhuma sequência (carrinho aberto/fechado) re-dispara em laço sobre o mesmo contato.
6. **Varredura registrada.** Verificar: a varredura de redirecionamentos foi feita e os ciclos encontrados/corrigidos estão anotados.

## Evidência Exigida
Para marcar ✅: linkar o registro anti-loop no [`decision-registry`](../../data/registries/decision-registry.md) no formato `{area: anti_loop, ciclos_encontrados, correcao}` e o registro de integrações `{sistema, status, idempotente?}`, mais o mapa de redirecionamentos varrido. As rotas do `funnel-map` que embasaram a varredura ficam citadas.

## Protocolo de Falha
Item vermelho → o `tech-links-deliverability-engineer` quebra o ciclo (redireciona o estado terminal para TY/continuidade) e torna o webhook idempotente antes de declarar o fluxo pronto. Funil com **rota ambígua ou estado sem destino** ele **recusa** implementar e devolve ao [`funnel-architect`](../../agents/funnel-architect.md) — engenheirar sobre ambiguidade gera loop ou rota órfã. O engenheiro **não tem veto** sobre o pipeline; ele registra a recusa. A capacidade sob carga é do [`tech-load-test-gate`](tech-load-test-gate.md). Re-entrada: corrigir o ciclo/rota órfã, adicionar idempotência, re-varrer e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/surge-ops`](../../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`funnel-architect`](../../agents/funnel-architect.md)
- Gates irmãos: [`tech-load-test-gate`](tech-load-test-gate.md) · [`tech-deliverability-gate`](tech-deliverability-gate.md) · [`tech-links-utm-gate`](tech-links-utm-gate.md) · [`tech-fallback-gate`](tech-fallback-gate.md)
