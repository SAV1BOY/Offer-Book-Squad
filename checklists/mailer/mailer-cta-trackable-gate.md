---
id: checklist.mailer.mailer-cta-trackable-gate
title: "Gate — CTA Rastreável (cada QR/link físico→digital leva ao destino certo e é medido)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: direct-mail-insert-writer
frameworks: [offer-stack-builder, scarcity-urgency-engine]
registries: [control-registry]
tags: [gate, mailer, qr, cta, utm, rastreio, scan, d4]
---

# Gate — CTA Rastreável

## Propósito
Este gate prova que **o caminho físico→digital de cada peça funciona e é medido**: o QR aponta para a URL certa, a URL carrega a UTM correta, há um fallback impresso e a taxa de scan→ação pode ser apurada. Ele existe porque o sucesso do `direct-mail-insert-writer` é medido em scan→ação, não em peças enviadas — um QR que leva ao destino errado, ou um link sem UTM, queima a verba de postagem sem deixar rastro. Cada CTA físico→digital é único, de baixa fricção e coordenado com o [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) e com o [`funnel-architect`](../../agents/funnel-architect.md), para que o QR caia na página certa do funil. Vale o princípio `traceability_before_eloquence`: um toque que não se mede não conta. Há uma URL curta vanity como fallback do QR, para quem não escaneia. Este gate julga **só o rastreio e o destino** do CTA — se o QR cabe na peça (tamanho, quiet zone, fora de dobra) é do `mailer-spec-gate`, e se a oferta resumida bate com a Big Idea é do `mailer-offer-coherence-gate`. URL/QR não coordenados reprovam: o writer sinaliza ao tech-engineer e não imprime destino solto.

## Dono & Escopo
- **owner_agent:** `direct-mail-insert-writer` (define o CTA físico→digital e o destino de cada peça).
- **Artefato inspecionado:** o bloco `cta_fisico_digital` de cada peça em `artifact.mailers-inserts` — `{tipo, destino/UTM, fallback}` — registrado no [`control-registry`](../../data/registries/control-registry.md). A URL/UTM é coordenada com o [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md); o destino casa com a página do [`funnel-architect`](../../agents/funnel-architect.md).

## Condição de Passagem
Cada peça tem um CTA físico→digital único, com destino e UTM coordenados com o tech, fallback impresso e taxa de scan→ação mensurável.

## Itens
1. **Destino correto.** Verificar: o QR/link aponta para a página certa do funil, não para um destino genérico ou quebrado.
2. **UTM coordenada.** Verificar: a URL carrega a UTM acordada com o tech-engineer, para atribuir a origem da peça.
3. **CTA único.** Verificar: cada peça tem **um** CTA físico→digital primário, de baixa fricção, sem competir com outros.
4. **Fallback impresso.** Verificar: há uma URL curta vanity (ou código) como fallback para quem não escaneia o QR.
5. **Scan→ação mensurável.** Verificar: existe como apurar a taxa de scan→ação da peça (a métrica de sucesso).
6. **Coordenação confirmada.** Verificar: o `tech-links-deliverability-engineer` confirmou que destino e UTM existem e respondem.

## Evidência Exigida
Para marcar ✅: linkar, por peça, o bloco `cta_fisico_digital` com `{tipo, destino, UTM, fallback}` no [`control-registry`](../../data/registries/control-registry.md), mais a confirmação do [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) de que o destino responde e a UTM atribui. A página de destino casada com o [`funnel-architect`](../../agents/funnel-architect.md) fica citada.

## Protocolo de Falha
Item vermelho → o `direct-mail-insert-writer` **não imprime destino solto**: URL/QR não coordenados ele sinaliza ao [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) e segura a peça até o destino e a UTM existirem. Destino genérico ou quebrado ele corrige antes da gráfica — papel postado não se redireciona. CTA sem fallback ele completa com uma URL curta vanity. O writer **não tem veto**; escalona ao [`offerbook-chief`](../../agents/offerbook-chief.md). Se o QR não cabe na peça (tamanho, quiet zone, dobra) é do [`mailer-spec-gate`](mailer-spec-gate.md). Re-entrada: coordenar destino e UTM com o tech, adicionar o fallback e re-submeter ao control-registry.

## Links
- Frameworks: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`funnel-architect`](../../agents/funnel-architect.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`mailer-spec-gate`](mailer-spec-gate.md) · [`mailer-insert-fit-gate`](mailer-insert-fit-gate.md) · [`mailer-offer-coherence-gate`](mailer-offer-coherence-gate.md) · [`mailer-compliance-gate`](mailer-compliance-gate.md)
