---
id: checklist.vsl.vsl-risk-reversal-gate
title: "Gate — Reversão de Risco (garantia que o cliente entende e a economia suporta)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [risk-reversal-ladder, guarantee-design, copy/vsl-structure]
registries: [control-registry, offer-registry]
tags: [gate, vsl, garantia, reversao-de-risco, risk-reversal, d4]
---

# Gate — Reversão de Risco

## Propósito
Este gate prova que o roteiro **reverte o risco** da compra com uma garantia clara, crível e que a economia da oferta suporta. O medo de perder dinheiro é a última barreira antes do "sim"; uma reversão de risco bem-posta transfere esse risco do cliente para o vendedor e desbloqueia a conversão. Mas a garantia precisa ser real: uma promessa que a unit economics não sustenta vira prejuízo, e uma garantia impossível ("100% de resultado ou seu dinheiro de volta em dobro" sem lastro) é vetada pelo [`compliance-auditor`](../../agents/compliance-auditor.md). O gate força a garantia no Bloco 3, **depois** do valor e do preço, como o golpe final que remove a objeção de risco — e checa que o tipo de garantia (incondicional, condicional, condicional com prova de esforço) está coerente com o que o [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) aprovou. Ele costura com a escada de reversão de risco do offer book.

## Dono & Escopo
- **owner_agent:** `vsl-webinar-scriptwriter` (sem poder de veto; saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md)).
- **Artefato inspecionado:** o campo `risk_reversal` do roteiro no [`control-registry`](../../data/registries/control-registry.md), confrontado com a garantia desenhada no [`offer-registry`](../../data/registries/offer-registry.md) (via [`guarantee-design`](../../frameworks/guarantee-design.md) e [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md)) e com a margem aprovada pelo unit-econ.

## Condição de Passagem
O roteiro apresenta uma garantia clara no fechamento, do tipo que a unit economics suporta, que o cliente entende em uma frase e que remove a objeção de risco.

## Itens
1. **Garantia presente no fechamento.** Verificar: o Bloco 3 contém uma reversão de risco explícita, depois do valor e do preço.
2. **Clara em uma frase.** Verificar: o cliente entende a garantia sem letra miúda — prazo, condição e o que recebe de volta estão diretos.
3. **Tipo coerente com a economia.** Verificar: o tipo (incondicional/condicional/condicional-com-esforço) bate com o que o `offer-registry`/unit-econ aprovou.
4. **Sustentável pela margem.** Verificar: a garantia não cria prejuízo — a unit economics suporta a taxa de reembolso esperada.
5. **Não é impossível nem fraudulenta.** Verificar: nenhuma promessa de resultado garantido sem lastro; garantia impossível é flag ao [`compliance-auditor`](../../agents/compliance-auditor.md).
6. **Remove a objeção de risco.** Verificar: a garantia responde à objeção de risco dominante do roteiro (cruza com as objeções destruídas).
7. **Registrada.** Verificar: o `risk_reversal` aplicado está gravado no `control-registry` e aponta para a garantia do `offer-registry`.

## Evidência Exigida
Para marcar ✅: linkar o campo `risk_reversal` do roteiro no `control-registry` e a garantia no `offer-registry` lado a lado (itens 1–3, 7), a confirmação do unit-econ de que a margem suporta o tipo (item 4), a checagem de que a garantia não é impossível (item 5) e o vínculo com a objeção de risco que ela remove (item 6).

## Protocolo de Falha
Item vermelho → o `vsl-webinar-scriptwriter` ajusta a garantia ao tipo que a economia suporta, ou a reescreve para clareza. Garantia que a margem não suporta → sinaliza ao [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md). Garantia impossível/fraudulenta → sinaliza ao [`compliance-auditor`](../../agents/compliance-auditor.md) e reescreve. Re-entrada: corrige `risk_reversal` no `control-registry` e re-submete ao voice-guardian. Mudança de garantia no offer book reabre este gate.

## Links
- Gates irmãos: [`vsl-formula-fit-gate`](vsl-formula-fit-gate.md) · [`vsl-value-before-price-gate`](vsl-value-before-price-gate.md) · [`vsl-urgency-gate`](vsl-urgency-gate.md) · [`vsl-cta-strength-gate`](vsl-cta-strength-gate.md)
- Frameworks: [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md) · [`guarantee-design`](../../frameworks/guarantee-design.md) · [`vsl-structure`](../../frameworks/copy/vsl-structure.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) · [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
