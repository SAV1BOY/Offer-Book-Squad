---
id: checklist.run-of-show-checklist
title: "Checklist — Run of Show (blocos, timings, palestrantes, surge sales)"
type: checklist
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [launch/perfect-webinar, launch/surge-ops, launch/product-launch-formula]
registries: [decision-registry, control-registry]
tags: [checklist, run-of-show, blocos, timings, palestrantes, surge-sales, d6]
---

# Checklist — Run of Show

## Propósito
Este checklist prova que o run of show é um roteiro minuto a minuto que qualquer operador consegue rodar ao vivo. Existe porque evento ao vivo não perdoa: um bloco sem timing estoura o relógio, um palestrante sem deixa fica perdido, e o momento da venda (surge sales) passa sem que o CTA seja dado. Cada bloco precisa de início, fim e dono. Cada transição precisa de uma deixa. O pico de vendas precisa de um roteiro próprio — quando abre o carrinho, quem anuncia, qual oferta na tela. Sem este checklist verde, o evento improvisa na hora mais cara. Ele garante `decision_before_ornament`: cada bloco serve a um momento de decisão do espectador, e o relógio fecha.

## Dono & Escopo
- **owner_agent:** `launch-producer` (monta e dirige o run of show); o [`vsl-webinar-scriptwriter`](../agents/vsl-webinar-scriptwriter.md) entrega o script do pitch e o [`events-logistics-coordinator`](../agents/events-logistics-coordinator.md) garante a operação técnica.
- **Artefato inspecionado:** o **run of show** (`templates/ops/run-of-show-template` preenchido) e o `templates/ops/sales-flow-template`, registrados no [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
Cada bloco tem início, fim e dono, cada palestrante tem suas deixas, o relógio fecha sem estouro, e o momento de surge sales tem roteiro próprio com CTA na hora certa.

## Itens
1. **Blocos com timing.** Como verificar: cada bloco tem horário de início e fim; a soma fecha dentro da duração total sem estouro.
2. **Dono por bloco.** Como verificar: cada bloco nomeia quem conduz (palestrante, operador, host).
3. **Deixas de transição.** Como verificar: cada troca de bloco/palestrante tem uma deixa explícita (frase-gatilho, sinal); ninguém fica sem saber a vez.
4. **Roteiro do pitch.** Como verificar: o bloco de oferta segue a estrutura de valor-antes-de-preço, conforme [`launch/perfect-webinar`](../frameworks/launch/perfect-webinar.md), com o script do `vsl-webinar-scriptwriter`.
5. **Surge sales com CTA.** Como verificar: o momento de abertura de carrinho tem roteiro próprio — quem anuncia, qual oferta na tela, qual link, conforme [`launch/surge-ops`](../frameworks/launch/surge-ops.md).
6. **Escassez verdadeira no palco.** Como verificar: prazos/vagas anunciados ao vivo são reais e rastreados; escassez falsa = veto do `compliance-auditor`.
7. **Plano de contingência.** Como verificar: há bloco-buffer e plano para atraso, falha de áudio/vídeo ou palestrante ausente.
8. **Q&A e fechamento.** Como verificar: há janela de perguntas e um fechamento que repete o CTA antes de encerrar.

## Evidência Exigida
Para marcar ✅: linkar o run of show no `decision-registry`, a grade de blocos com timing somando à duração total (item 1), a coluna dono por bloco (item 2), a lista de deixas de transição (item 3) e o roteiro de surge sales com CTA e link (item 5). O script do pitch (item 4) fica linkado ao `control-registry`.

## Protocolo de Falha
Item vermelho → o run of show volta ao `launch-producer` com o defeito nomeado e **o evento não vai ao ar**. Relógio que estoura é recortado antes do ensaio. Bloco sem dono ou transição sem deixa é resolvido na grade. Surge sales sem CTA claro reabre conversa com o `vsl-webinar-scriptwriter`. Escassez falsa aciona veto do `compliance-auditor`. Re-entrada: corrigir a grade, ensaiar, atualizar o `decision-registry`, re-submeter.

## Links
- Gate relacionado: [`launch/launch-surge-gate`](launch/launch-surge-gate.md)
- Frameworks: [`launch/perfect-webinar`](../frameworks/launch/perfect-webinar.md) · [`launch/surge-ops`](../frameworks/launch/surge-ops.md) · [`launch/product-launch-formula`](../frameworks/launch/product-launch-formula.md)
- Registries: [`decision-registry`](../data/registries/decision-registry.md) · [`control-registry`](../data/registries/control-registry.md)
- Agentes: [`launch-producer`](../agents/launch-producer.md) · [`vsl-webinar-scriptwriter`](../agents/vsl-webinar-scriptwriter.md) · [`events-logistics-coordinator`](../agents/events-logistics-coordinator.md)
- Checklists vizinhos: [`launch-memo-checklist`](launch-memo-checklist.md) · [`events-logistics-checklist`](events-logistics-checklist.md) · [`cart-close-checklist`](cart-close-checklist.md)
