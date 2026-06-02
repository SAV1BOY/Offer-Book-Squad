---
id: checklist.vsl-script-checklist
title: "Checklist — Roteiro de VSL (estrutura PAS/PASTOR, valor antes do preço)"
type: checklist
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [copy/vsl-structure, copy/pastor, copy/pas, copy/slippery-slide]
registries: [control-registry, proof-registry, objection-registry]
tags: [checklist, copy, vsl, pas, pastor, valor-antes-preco, d4]
---

# Checklist — Roteiro de VSL

## Propósito
Este checklist prova que o roteiro de VSL segue uma **estrutura de persuasão completa** (PAS ou PASTOR), entrega **valor antes do preço** e fecha com reversão de risco e CTA forte. Existe porque um VSL que pede a venda antes de construir desejo e prova converte mal — o cliente não compra o que não desejou nem acreditou. A estrutura garante que dor, solução, prova, transformação e oferta apareçam na ordem que move o "sim". Sem este checklist verde, o roteiro vira lista de features sem narrativa. Ele só pode existir depois do HARD STOP liberado: nenhuma palavra de VSL nasce antes do Offer Book passar no DoD. É a primeira peça de copy a executar a Big Idea travada.

## Dono & Escopo
- **owner_agent:** `vsl-webinar-scriptwriter` (escreve o roteiro); o [`voice-style-guardian`](../agents/voice-style-guardian.md) co-assina a voz.
- **Artefato inspecionado:** o `artifact.vsl-script` (e a `artifact.sales-letter`/offer page derivada), registrado no [`control-registry`](../data/registries/control-registry.md), sustentado pelo [`proof-registry`](../data/registries/proof-registry.md) e pelo [`objection-registry`](../data/registries/objection-registry.md).

## Condição de Passagem
O roteiro segue PAS/PASTOR completo, entrega valor e prova antes de revelar o preço, desarma as objeções dominantes, fecha com reversão de risco e CTA único — e a voz está aprovada.

## Itens
1. **HARD STOP liberado.** Como verificar: o [`offer-book-checklist`](offer-book-checklist.md) está ✅ — sem ele, o roteiro não nasce.
2. **Estrutura PAS/PASTOR presente.** Como verificar: o roteiro tem todos os beats da estrutura escolhida (problema, agitação, solução; ou problema-amplificação-história-transformação-oferta-resposta-resultado), conforme `pastor` e `pas`.
3. **Abertura na consciência certa.** Como verificar: o lead de abertura bate com o tipo de lead travado no posicionamento, conforme `vsl-structure`.
4. **Valor antes do preço.** Como verificar: ler o roteiro em ordem — desejo, prova e transformação aparecem antes do número; o preço só surge depois do valor construído.
5. **Mecanismo apresentado.** Como verificar: o roteiro nomeia e explica o mecanismo único como o "porquê" da promessa.
6. **Prova ancorada.** Como verificar: cada claim forte no roteiro aponta para um `proof_id` no `proof-registry`; sem prova, o claim sai.
7. **Objeções desarmadas.** Como verificar: as objeções dominantes do `objection-registry` aparecem respondidas no roteiro antes do CTA.
8. **Reversão de risco.** Como verificar: a garantia/risco reverso está apresentada de forma clara antes do fechamento.
9. **CTA único e forte.** Como verificar: o roteiro fecha com UMA chamada explícita, com o próximo passo óbvio — não três opções.
10. **Escassez verdadeira.** Como verificar: qualquer prazo/limite citado é real e rastreável; escassez falsa = veto do `compliance-auditor`.
11. **Voz aprovada.** Como verificar: o `voice-style-guardian` deu `voice-verdict` APROVADO (3ª série, ativa, presente, sem jargão).

## Evidência Exigida
Para marcar ✅: linkar o roteiro no `control-registry`, o mapa de beats da estrutura PAS/PASTOR (item 2), a posição do preço depois do valor no roteiro (item 4), a tabela claim→proof sem órfãos (item 6), a tabela objeção→resposta (item 7) e o `voice-verdict` APROVADO (item 11). Escassez citada exige o limite real linkado (item 10).

## Protocolo de Falha
Item vermelho → o roteiro volta ao `vsl-webinar-scriptwriter` com o defeito nomeado e **não vai para gravação/publicação**. Preço antes do valor, claim órfão ou escassez falsa aciona veto (voz pelo `voice-style-guardian`, claim/escassez pelo `compliance-auditor`). Re-entrada: reescrever o beat, atualizar o `control-registry`, re-submeter. Mudança na Big Idea ou na oferta reabre este checklist.

## Links
- Frameworks: [`vsl-structure`](../frameworks/copy/vsl-structure.md) · [`pastor`](../frameworks/copy/pastor.md) · [`pas`](../frameworks/copy/pas.md) · [`slippery-slide`](../frameworks/copy/slippery-slide.md)
- Registries: [`control-registry`](../data/registries/control-registry.md) · [`proof-registry`](../data/registries/proof-registry.md) · [`objection-registry`](../data/registries/objection-registry.md)
- Agentes: [`vsl-webinar-scriptwriter`](../agents/vsl-webinar-scriptwriter.md) · [`voice-style-guardian`](../agents/voice-style-guardian.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Gates por agente: [`vsl/vsl-value-before-price-gate`](vsl/vsl-value-before-price-gate.md) · [`vsl/vsl-risk-reversal-gate`](vsl/vsl-risk-reversal-gate.md) · [`vsl/vsl-cta-strength-gate`](vsl/vsl-cta-strength-gate.md)
- Checklists vizinhos: [`webinar-checklist`](webinar-checklist.md) · Agrega para: [`launch-blackbook-checklist`](launch-blackbook-checklist.md)
