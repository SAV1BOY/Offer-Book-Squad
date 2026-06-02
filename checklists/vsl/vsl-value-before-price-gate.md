---
id: checklist.vsl.vsl-value-before-price-gate
title: "Gate — Valor Antes do Preço (o número só aparece depois do stack)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [copy/vsl-structure, value-equation, price-anchoring, offer-stack-builder]
registries: [control-registry, proof-registry]
tags: [gate, vsl, valor-antes-preco, ancoragem, value-stack, d4]
---

# Gate — Valor Antes do Preço

## Propósito
Este gate prova a regra de ouro do fechamento: **o valor aparece antes do preço**. Hormozi é a base — empilhar valor até o preço parecer ridículo de barato. Se o número surge antes de o leitor entender o que recebe, ele julga pelo custo, não pelo valor; se surge depois de um stack bem-somado e de uma âncora alta, o preço parece trivial. O gate força a sequência do Bloco 3: empilhar o value stack item a item, somar o "valor total", **só então** revelar o preço ancorado. Ele também trava um claim sem prova — cada afirmação de valor aponta para o [`proof-registry`](../../data/registries/proof-registry.md) — e veta que qualquer preço apareça nos Blocos 1 ou 2. É o gate que mais distingue um roteiro que vende de um que assusta: a ordem em que valor e preço aparecem decide a conversão.

## Dono & Escopo
- **owner_agent:** `vsl-webinar-scriptwriter` (sem poder de veto; saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md)).
- **Artefato inspecionado:** o Bloco 3 do roteiro — o `value stack`, o `valor total`, o ponto de revelação do preço e o `value_before_price` registrados no [`control-registry`](../../data/registries/control-registry.md) —, com a prova por claim no [`proof-registry`](../../data/registries/proof-registry.md).

## Condição de Passagem
Nenhum preço aparece antes do value stack somado, o número é revelado ancorado dentro do Bloco 3, e cada claim de valor tem prova linkada.

## Itens
1. **Nenhum preço nos Blocos 1–2.** Verificar: percorrer o roteiro — o primeiro número de preço só aparece no Bloco 3, depois do stack.
2. **Value stack item a item.** Verificar: o stack lista cada componente com seu valor individual (via [`offer-stack-builder`](../../frameworks/offer-stack-builder.md)).
3. **Valor total somado.** Verificar: há uma soma explícita do valor antes do preço — o "valor total" precede o número.
4. **Preço ancorado depois.** Verificar: o preço surge após a âncora (consistente com [`price-anchoring`](../../frameworks/price-anchoring.md) e o [`pricing-anchor-gate`](../pricing/pricing-anchor-gate.md)), não nu.
5. **Cada claim com prova.** Verificar: toda afirmação de valor aponta para o `proof-registry`; claim sem lastro vira `[PROVA PENDENTE]` e bloqueia a publicação.
6. **Alavancas de valor presentes.** Verificar: o stack move as alavancas da value equation (Sonho/Probabilidade/Tempo/Esforço), não só lista features.
7. **`value_before_price` marcado.** Verificar: o campo `value_before_price: true` está registrado no `control-registry` com a posição do número.

## Evidência Exigida
Para marcar ✅: linkar o Bloco 3 no `control-registry` mostrando o stack item a item, o valor total somado e o ponto em que o preço aparece (itens 1–4, 7), a prova por claim no `proof-registry` (item 5) e o mapeamento stack→alavancas de valor (item 6).

## Protocolo de Falha
Item vermelho → o `vsl-webinar-scriptwriter` move **todo** número para o Bloco 3, depois do stack; preço antes do valor é reprovação. Claim sem prova → marca `[PROVA PENDENTE]` e escalona ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md), ou reescreve para o que se prova. Âncora fictícia → sinaliza ao [`compliance-auditor`](../../agents/compliance-auditor.md). Re-entrada: corrige a ordem no roteiro, atualiza o `control-registry` e re-submete ao voice-guardian.

## Links
- Gates irmãos: [`vsl-formula-fit-gate`](vsl-formula-fit-gate.md) · [`vsl-risk-reversal-gate`](vsl-risk-reversal-gate.md) · [`vsl-urgency-gate`](vsl-urgency-gate.md) · [`vsl-cta-strength-gate`](vsl-cta-strength-gate.md)
- Frameworks: [`vsl-structure`](../../frameworks/copy/vsl-structure.md) · [`value-equation`](../../frameworks/value-equation.md) · [`price-anchoring`](../../frameworks/price-anchoring.md) · [`offer-stack-builder`](../../frameworks/offer-stack-builder.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md)
- Agentes: [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Relacionado: [`pricing-anchor-gate`](../pricing/pricing-anchor-gate.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
