---
id: framework.launch.surge-ops
title: "Surge Ops — Operação de Pico"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [cart-open-close, runway-and-phases, product-launch-formula, abandoned-cart-recovery]
sources:
  - "Jeff Walker, *Launch* (2014; ed. atualizada, 2023), launch-day operations."
  - "Alex Hormozi, *$100M Offers* (2021), execução de oferta sob volume."
tags: [surge, ops, launch-day, deliverability, war-room, fallback, capacity, walker]
---

# Surge Ops — Operação de Pico

## TL;DR
Abertura e fechamento concentram tráfego, pagamentos e suporte numa janela de horas. **Surge Ops** é o plano de guerra para essas horas: capacidade testada, sala de comando (war room), monitoramento ao vivo e planos de contingência para checkout, e-mail e páginas. A maioria das vendas chega no pico — se a infra cai ou o suporte trava, você perde a receita exatamente quando ela acontece. O `launch-producer` comanda o pico; o `tech-links-deliverability-engineer` garante que links, páginas e entregabilidade aguentam.

## Quando usar / Quando não
**Use** em toda abertura e todo fechamento de carrinho — os dois picos de um lançamento.
**Use mais** em lançamento grande, com afiliados ou lista numerosa: o volume simultâneo estressa checkout, e-mail e suporte ao mesmo tempo.
**Não use** como desculpa para over-engineering num lançamento pequeno: dimensione o plano ao tamanho real do pico.
**Não use** isolado da escassez verdadeira: o pico existe porque o deadline é real ([`cart-open-close.md`](cart-open-close.md)).

## Inputs
- Calendário com os horários exatos dos picos (abertura e fechamento).
- Estimativa de volume: tráfego, pagamentos por minuto, tickets de suporte esperados.
- Stack técnico mapeado: checkout, gateway, e-mail/SMS, páginas, rastreamento.
- Planos de contingência por ponto de falha (página alternativa, segundo gateway, fila de suporte).
- Equipe de plantão definida com papéis e canal de comunicação.

## Procedimento
1. **Mapeie os pontos de falha**: checkout, gateway de pagamento, provedor de e-mail, páginas, links rastreados, entregabilidade.
2. **Teste a capacidade antes**: simule o pico (carga, envio em massa, checkout real) e meça onde quebra (gate `launch/launch-surge-gate`).
3. **Prepare os fallbacks**: página de checkout reserva, segundo gateway, e-mail de backup, link alternativo. Documente o gatilho de cada um (gate `launch/launch-fallback-gate`).
4. **Monte a war room**: equipe de plantão com papéis claros — tech, suporte, copy, comando — num canal único em tempo real.
5. **Arme o monitoramento ao vivo**: dashboard de vendas, taxa de erro de checkout, deliverability, fila de suporte.
6. **Aqueça a entrega**: alinhe o disparo em ondas para não estourar o provedor e não cair em spam (com `tech-links-deliverability-engineer`).
7. **Opere o pico**: na abertura e no fechamento, a war room observa, responde e aciona fallback em minutos se algo falha.
8. **Capture o carrinho abandonado** em tempo quase real e encaminhe para [`abandoned-cart-recovery.md`](abandoned-cart-recovery.md).
9. **Faça o pós-mortem**: registre o que quebrou, o que segurou e o que melhorar no `lessons-learned-registry`.

## Outputs
- **Plano de pico**: pontos de falha, fallbacks e gatilhos documentados.
- **Run-of-show da war room**: papéis, canal, escala de plantão por horário.
- **Dashboard de monitoramento** com os sinais críticos (vendas, erros, deliverability, suporte).
- Pós-mortem para a memória do squad.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Pontos de falha**: gateway único, e-mail num só provedor, página de checkout num plano básico.
- **Teste**: simulação de 500 checkouts/hora revela timeout no gateway → contrata plano maior + segundo gateway.
- **Fallbacks**: link de checkout reserva e provedor de e-mail de backup, com gatilho "erro >2%".
- **War room (sábado, fechamento)**: tech monitora erros, suporte responde em 5 min, comando decide fallback.
- **Ondas de e-mail**: disparo em 3 lotes às 09h, 18h e 23h para não estourar a entrega.
- **Resultado**: pico de vendas das 22h-24h absorvido sem queda; carrinho abandonado recuperado na hora.

## Armadilhas
- **Não testar a capacidade.** Descobrir o limite durante o pico é descobrir tarde demais.
- **Sem fallback.** Um único gateway ou provedor é um único ponto de falha para toda a receita.
- **War room sem papéis.** Todo mundo apaga o mesmo incêndio e ninguém decide. Defina quem faz o quê.
- **Disparo único gigante.** Mandar tudo de uma vez derruba a entrega e joga e-mail no spam.
- **Ignorar o pós-mortem.** Sem registrar o que quebrou, o próximo pico repete o erro.

## Interações
- **Agentes**: `launch-producer` (comanda a war room e o pico); `tech-links-deliverability-engineer` (capacidade, links, páginas, entregabilidade); `events-logistics-coordinator` (logística do evento ao vivo no pico); `email-sms-sequence-writer` (ondas de disparo); `compliance-auditor` (garante que a urgência do pico é real).
- **Frameworks que pareiam**: [`cart-open-close.md`](cart-open-close.md) (os dois picos), [`runway-and-phases.md`](runway-and-phases.md) (quando o pico cai na pista), [`product-launch-formula.md`](product-launch-formula.md), [`abandoned-cart-recovery.md`](abandoned-cart-recovery.md).

## Fontes
> **Fonte:** Jeff Walker, *Launch* (2014; ed. atualizada, 2023) — operação do dia de lançamento — via [`../../reference/books/launches-and-funnels/walker-launch.md`](../../reference/books/launches-and-funnels/walker-launch.md), acesso 2026-06-02.
> **Fonte:** Alex Hormozi, *$100M Offers* (2021) — execução de oferta sob volume — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
