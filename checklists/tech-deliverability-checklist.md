---
id: checklist.tech-deliverability-checklist
title: "Checklist — Tech & Deliverability (load test, fallback, aquecimento, anti-loop)"
type: checklist
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: tech-links-deliverability-engineer
frameworks: [launch/surge-ops, offer-to-funnel-mapping]
registries: [decision-registry, control-registry]
tags: [checklist, tech, deliverability, load-test, fallback, warmup, anti-loop, d5]
---

# Checklist — Tech & Deliverability

## Propósito
Este checklist prova que a infraestrutura técnica aguenta o pico e que os e-mails chegam. Existe porque lançamento morre na hora errada: a página cai no minuto da abertura do carrinho, o e-mail de venda vai para spam, o domínio não foi aquecido, ou uma automação entra em loop e dispara dez mensagens no mesmo lead. Surge de tráfego é previsível — então precisa de load test e fallback. Entrega de e-mail é frágil — então precisa de aquecimento e autenticação. Automação é cega — então precisa de trava anti-loop. Sem este checklist verde, a melhor copy do mundo não é vista. Ele garante `traceability_before_eloquence` no nível técnico: cada link rastreia, cada disparo tem teto e cada falha tem plano B.

## Dono & Escopo
- **owner_agent:** `tech-links-deliverability-engineer` (responde pela infra de links, páginas e entrega); o [`funnel-architect`](../agents/funnel-architect.md) entrega o mapa de URLs e o [`launch-producer`](../agents/launch-producer.md) alinha a janela de pico.
- **Artefato inspecionado:** o **plano de tech & deliverability** (`templates/funnel-tech/tech-deliverability-plan-template` preenchido) e o `templates/funnel-tech/links-urls-template`, registrados no [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
A infra passou em load test no pico esperado, há fallback para cada ponto crítico, o domínio/IP de envio está aquecido e autenticado, e toda automação tem trava anti-loop.

## Itens
1. **Load test no pico.** Como verificar: teste de carga simulando o tráfego esperado da abertura; a página e o checkout respondem dentro do limite, conforme [`launch/surge-ops`](../frameworks/launch/surge-ops.md).
2. **Fallback por ponto crítico.** Como verificar: cada ponto que pode cair (página, checkout, gateway) tem plano B documentado (espelho, fila, página estática).
3. **Aquecimento de envio.** Como verificar: domínio/IP de e-mail aquecido em rampa antes do volume de lançamento; histórico de reputação verificado.
4. **Autenticação de e-mail.** Como verificar: SPF, DKIM e DMARC configurados e validados para o domínio remetente.
5. **Trava anti-loop.** Como verificar: cada automação tem condição de saída e teto de frequência; um lead não recebe a mesma mensagem duas vezes por erro de gatilho.
6. **Links rastreáveis e vivos.** Como verificar: cada URL/UTM resolve para a página certa e está registrada; nenhum link morto, conforme [`offer-to-funnel-mapping`](../frameworks/offer-to-funnel-mapping.md).
7. **Monitoramento e alerta.** Como verificar: há painel/alerta de uptime, taxa de entrega e erros durante a janela de venda.
8. **Plano de rollback.** Como verificar: existe procedimento para reverter uma mudança que quebre o funil durante o lançamento.

## Evidência Exigida
Para marcar ✅: linkar o relatório de load test no pico (item 1), a tabela ponto-crítico→fallback (item 2), o registro de aquecimento e os checks SPF/DKIM/DMARC (itens 3–4), a configuração de teto/saída de cada automação (item 5) e a lista de URLs vivas com rastreio (item 6). O painel de monitoramento (item 7) fica linkado no `decision-registry`.

## Protocolo de Falha
Item vermelho → o plano volta ao `tech-links-deliverability-engineer` e o **carrinho não abre** sem infra verde. Página que não passa no load test reabre conversa com o `launch-producer` sobre janela e capacidade. Falha de autenticação ou domínio frio adia o envio até o aquecimento concluir. Re-entrada: corrigir o ponto técnico, re-testar, atualizar o `decision-registry`, re-submeter. Mudança no mapa de funil reabre a verificação de links.

## Links
- Gate relacionado: [`launch/launch-fallback-gate`](launch/launch-fallback-gate.md)
- Frameworks: [`launch/surge-ops`](../frameworks/launch/surge-ops.md) · [`offer-to-funnel-mapping`](../frameworks/offer-to-funnel-mapping.md)
- Registries: [`decision-registry`](../data/registries/decision-registry.md) · [`control-registry`](../data/registries/control-registry.md)
- Agentes: [`tech-links-deliverability-engineer`](../agents/tech-links-deliverability-engineer.md) · [`funnel-architect`](../agents/funnel-architect.md) · [`launch-producer`](../agents/launch-producer.md)
- Checklists vizinhos: [`funnel-map-checklist`](funnel-map-checklist.md) · [`run-of-show-checklist`](run-of-show-checklist.md)
