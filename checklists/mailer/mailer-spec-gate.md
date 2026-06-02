---
id: checklist.mailer.mailer-spec-gate
title: "Gate — Specs de Produção (cada peça tem formato, dimensões, dobras, sangria e QR completos)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: direct-mail-insert-writer
frameworks: [offer-stack-builder, scarcity-urgency-engine]
registries: [control-registry]
tags: [gate, mailer, insert, specs, producao, sangria, qr, d4]
---

# Gate — Specs de Produção

## Propósito
Este gate prova que **cada peça física tem as specs de produção completas antes de ir à gráfica**: formato, dimensões, dobras, sangria, área e tamanho do QR (com quiet zone) e número de cores. Ele existe porque papel postado não se corrige — uma sangria errada corta o texto, um QR na dobra fica ilegível, uma dimensão fora do envelope inviabiliza a postagem. O `direct-mail-insert-writer` materializa a estratégia em papel que cabe num envelope, e cada peça nasce com copy **e** specs preenchidas, nunca só a copy. Vale o princípio `spec_before_press`: nada vai à produção sem a ficha técnica fechada. O QR fica fora de dobra, com quiet zone e contraste, no tamanho mínimo legível. Este gate julga **só a viabilidade de produção** da peça — se o QR de fato rastreia é do `mailer-cta-trackable-gate`, e se o insert vai no degrau certo é do `mailer-insert-fit-gate`. Specs incompletas reprovam aqui: o mailer-checklist não deixa passar uma peça sem sangria ou sem dimensões. Uma dobra tripla que esconderia o QR mal posicionado é corrigida antes do envio, não depois.

## Dono & Escopo
- **owner_agent:** `direct-mail-insert-writer` (define formato, dimensões, dobras, sangria, área de QR e cores de cada peça).
- **Artefato inspecionado:** o bloco `specs` de cada peça em `artifact.mailers-inserts`, registrado no [`control-registry`](../../data/registries/control-registry.md). Specs incompletas voltam ao writer antes da gráfica; o QR/CTA é coordenado com o [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md).

## Condição de Passagem
Cada peça física tem formato, dimensões, dobras, sangria, área/tamanho do QR com quiet zone e número de cores definidos e prontos para a gráfica.

## Itens
1. **Formato definido.** Verificar: cada peça tem formato declarado (ex.: A6 postal, carta dobrada, dimensional).
2. **Dimensões em mm.** Verificar: largura × altura em milímetros está especificada para cada peça.
3. **Dobras.** Verificar: número e tipo de dobra estão definidos (ex.: dobra simples, tripla) ou marcado "sem dobra".
4. **Sangria.** Verificar: a sangria está especificada (ex.: 3 mm) para não cortar texto/arte na guilhotina.
5. **Área e tamanho do QR.** Verificar: o QR tem tamanho mínimo legível, quiet zone e posição **fora da dobra**.
6. **Cores.** Verificar: o número de cores de impressão está definido (ex.: 2 cores, 4/4).

## Evidência Exigida
Para marcar ✅: linkar, por peça, o bloco `specs` completo — `{formato, dimensoes_mm, dobras, sangria_mm, qr_mm, quiet_zone, cores}` — registrado no [`control-registry`](../../data/registries/control-registry.md). A confirmação de que o QR está fora da dobra e com quiet zone, e a coordenação da posição com o tech-engineer, ficam citadas.

## Protocolo de Falha
Item vermelho → o `direct-mail-insert-writer` **completa as specs antes de mandar à produção** — papel postado não se corrige. QR ilegível (na dobra, pequeno demais, sem contraste) ele reposiciona fora da dobra, aumenta o tamanho e garante a quiet zone. Specs faltantes (sem sangria/dimensões) reprovam no [`mailer-checklist`](../mailer-checklist.md). O writer **não tem veto**; ele sinaliza ao [`offerbook-chief`](../../agents/offerbook-chief.md) e coordena a posição do QR com o [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md). Se o QR de fato rastreia é do [`mailer-cta-trackable-gate`](mailer-cta-trackable-gate.md). Re-entrada: completar o bloco `specs`, reposicionar o QR e re-submeter ao control-registry.

## Links
- Frameworks: [`offer-stack-builder`](../../frameworks/offer-stack-builder.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`direct-mail-insert-writer`](../../agents/direct-mail-insert-writer.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`mailer-cta-trackable-gate`](mailer-cta-trackable-gate.md) · [`mailer-insert-fit-gate`](mailer-insert-fit-gate.md) · [`mailer-offer-coherence-gate`](mailer-offer-coherence-gate.md) · [`mailer-compliance-gate`](mailer-compliance-gate.md)
