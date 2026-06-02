---
id: checklist.tech.tech-deliverability-gate
title: "Gate — Deliverability (o e-mail chega na caixa de entrada, não no spam)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: tech-links-deliverability-engineer
frameworks: [launch/surge-ops]
registries: [decision-registry]
tags: [gate, tech, deliverability, spf, dkim, dmarc, aquecimento, reputacao, d5]
---

# Gate — Deliverability

## Propósito
Este gate prova que **o e-mail do lançamento chega na caixa de entrada, com autenticação completa e domínio aquecido**. Ele existe porque a melhor copy não vende da pasta de spam. Um domínio novo que dispara para uma lista grande hoje queima a reputação e zera a conversão — e ainda contamina os envios futuros. O `tech-links-deliverability-engineer` segue as diretrizes dos provedores (Google/Yahoo): SPF, DKIM e DMARC configurados, mais uma rampa de aquecimento gradual que prioriza o segmento mais engajado antes do frio. Vale o princípio `evidence_before_opinion`: a reputação se prova com autenticação e histórico, não com pressa. No ToT do agente, o "envio total no dia 1 de domínio novo" é rejeitado (entregabilidade ~0); vence a rampa de 7–14 dias com o segmento quente primeiro. Este gate julga **só a entregabilidade e a reputação** — a capacidade da página que recebe o pico é do `tech-load-test-gate`, e o consentimento/privacidade da captura é flag ao `compliance-auditor`. Se o domínio é novo e o pedido é disparo total imediato, o engenheiro recusa o go-live de e-mail.

## Dono & Escopo
- **owner_agent:** `tech-links-deliverability-engineer` (configura a autenticação e desenha a rampa de aquecimento).
- **Artefato inspecionado:** a parte de deliverability do `tech-deliverability-plan`, cruzada com o volume e a cadência das `email-sms-sequences` e a idade do domínio/IP. O resultado vai ao [`decision-registry`](../../data/registries/decision-registry.md). Gate consumido em `config.yaml: routing.plan-tech-deliverability`.

## Condição de Passagem
O e-mail passa em SPF, DKIM e DMARC, e a rampa de aquecimento protege a reputação do domínio antes do volume cheio.

## Itens
1. **SPF configurado.** Verificar: o registro SPF do domínio de envio existe e está correto.
2. **DKIM configurado.** Verificar: o e-mail é assinado com DKIM válido.
3. **DMARC configurado.** Verificar: existe política DMARC publicada e alinhada com SPF/DKIM.
4. **Idade do domínio avaliada.** Verificar: a idade e o histórico do domínio/IP estão medidos para dimensionar a rampa.
5. **Rampa de aquecimento.** Verificar: há rampa gradual (ex.: 7–14 dias) proporcional ao tamanho da lista e à idade do domínio.
6. **Segmento quente primeiro.** Verificar: o disparo começa pelo segmento mais engajado antes do frio.
7. **Sem disparo total de domínio novo.** Verificar: nenhum envio cheio imediato de domínio novo e não aquecido.

## Evidência Exigida
Para marcar ✅: linkar o registro de deliverability no [`decision-registry`](../../data/registries/decision-registry.md) no formato `{spf, dkim, dmarc, rampa_aquecimento, segmento_inicial}`, mais a confirmação da autenticação e o cronograma da rampa. O tamanho da lista e a idade do domínio que dimensionaram a rampa ficam citados.

## Protocolo de Falha
Item vermelho → o `tech-links-deliverability-engineer` **recusa o go-live de e-mail** e escala ao [`offerbook-chief`](../../agents/offerbook-chief.md) a recomendação de adiar o disparo até a autenticação e a rampa estarem prontas — sem aquecimento, o lançamento queima a reputação. O engenheiro **não tem veto** sobre o pipeline; ele recusa executar o disparo de domínio frio e registra a recusa. Captura/rastreamento sem aviso de privacidade vira flag ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto (LGPD/consentimento). A capacidade da página que recebe o pico do disparo é do [`tech-load-test-gate`](tech-load-test-gate.md). Re-entrada: configurar SPF/DKIM/DMARC, desenhar a rampa, começar pelo segmento quente e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/surge-ops`](../../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`compliance-auditor`](../../agents/compliance-auditor.md) · [`launch-producer`](../../agents/launch-producer.md)
- Gates irmãos: [`tech-load-test-gate`](tech-load-test-gate.md) · [`tech-anti-loop-gate`](tech-anti-loop-gate.md) · [`tech-links-utm-gate`](tech-links-utm-gate.md) · [`tech-fallback-gate`](tech-fallback-gate.md)
