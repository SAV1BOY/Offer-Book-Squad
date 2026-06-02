---
id: checklist.compliance.compliance-disclaimers-gate
title: "Gate — Disclaimers & Garantias (★ VETO: avisos obrigatórios presentes)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [proof-to-claim-chain, scarcity-urgency-engine]
registries: [decision-registry, claim-registry]
tags: [gate, compliance, disclaimers, garantia, t-and-c, veto, d7]
---

# Gate — Disclaimers & Garantias (★ VETO)

## Propósito
Este gate prova que **cada disclaimer obrigatório está presente e que a garantia é visível e exequível**. É um dos cinco gates de **veto** do `compliance-auditor`. Ele existe porque a ausência de um aviso de renda, saúde ou financeiro — ou uma garantia que a operação não honra — transforma uma oferta forte em risco legal e quebra de confiança. A política de compliance exige disclaimers de renda/resultado (quando há promessa de ganho), de saúde ("não substitui orientação profissional", sem promessa de cura) e financeiro ("não é recomendação de investimento; rentabilidade passada não garante futura"). A garantia precisa estar visível antes do preço e ser cumprível pela operação. Vale o princípio `truthful_scarcity` estendido à honestidade integral da oferta. Disclaimer ausente ou garantia inexequível **vetam** a peça; o veto só cai por override registrado do `offerbook-chief`.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (verifica disclaimers e exequibilidade da garantia; **veta** a falha; `config.yaml: agents` veto=true). Co-roda com o `offerbook-chief`, que arbitra overrides legítimos (ex.: disclaimer que o `voice-style-guardian` não pôde acomodar).
- **Artefato inspecionado:** os disclaimers e a garantia no `offer-book`, `vsl-script`, `email-sms-sequences`, `mailers-inserts`, `ad-matrix` e em cada página do `funnel-map`, cruzados com a [`guarantee-types`](../../lib/taxonomies/guarantee-types.md) e o [`claim-registry`](../../data/registries/claim-registry.md).

## Condição de Passagem
Cada peça com promessa de renda, saúde ou finanças carrega o disclaimer obrigatório, e a garantia está visível antes do preço e é exequível pela operação.

## Itens
1. **Disclaimer de renda/resultado.** Verificar: peças com promessa de ganho/transformação trazem "resultados variam; sem garantia de ganho".
2. **Disclaimer de saúde.** Verificar: peças de saúde não prometem cura e trazem "não substitui orientação profissional".
3. **Disclaimer financeiro.** Verificar: peças financeiras trazem "não é recomendação; rentabilidade passada não garante futura".
4. **Garantia visível antes do preço.** Verificar: cada página de oferta mostra a garantia antes do preço, não escondida no rodapé.
5. **Garantia exequível.** Verificar: a operação consegue honrar a garantia (prazo, condição) conforme a `guarantee-types`.
6. **FAQ coerente.** Verificar: o FAQ e os T&C batem com a oferta e os disclaimers, sem contradição.
7. **Disclaimer legível.** Verificar: o aviso é legível e próximo do claim, não em letra ilegível ou em link perdido.

## Evidência Exigida
Para marcar ✅: linkar a presença de cada disclaimer por tipo de claim (itens 1–3), a posição da garantia antes do preço em cada página de oferta (item 4), a confirmação de exequibilidade da garantia (item 5) e a coerência do FAQ/T&C (item 6). O veredito aponta para o `decision-registry`.

## Protocolo de Falha
Disclaimer ausente ou garantia inexequível → **VETO** da peça; o `compliance-auditor` registra a violação no `decision-registry` e devolve ao autor (copy via `voice-pass`) ou ao dono da garantia. Garantia que a operação não honra é veto conforme a política. A peça **não vai ao blackbook** até o aviso entrar ou a garantia ser ajustada. **Override:** só o [`offerbook-chief`](../../agents/offerbook-chief.md) pode arbitrar um conflito legítimo (ex.: redação de disclaimer vs. voz), com decisão explícita gravada no `decision-registry` — override sem registro não existe. A presença da prova por trás do claim é tratada no gate irmão de claim.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md)
- Taxonomia: [`guarantee-types`](../../lib/taxonomies/guarantee-types.md)
- Registries: [`claim-registry`](../../data/registries/claim-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Política: [`compliance-policy`](../../docs/compliance-policy.md)
- Agentes: [`compliance-auditor`](../../agents/compliance-auditor.md) · [`offerbook-chief`](../../agents/offerbook-chief.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Gates irmãos: [`compliance-claim-backing-gate`](compliance-claim-backing-gate.md) · [`compliance-scarcity-truth-gate`](compliance-scarcity-truth-gate.md) · [`compliance-data-privacy-gate`](compliance-data-privacy-gate.md) · [`compliance-sector-rules-gate`](compliance-sector-rules-gate.md)
