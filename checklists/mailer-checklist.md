---
id: checklist.mailer-checklist
title: "Checklist — Mala Direta & Inserts (casamento com produto, CTA/QR rastreável)"
type: checklist
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: direct-mail-insert-writer
frameworks: [offer-stack-builder, scarcity-urgency-engine, proof-to-claim-chain]
registries: [control-registry, claim-registry, proof-registry]
tags: [checklist, copy, direct-mail, mailer, insert, qr-code, cta, rastreavel, d4]
---

# Checklist — Mala Direta & Inserts

## Propósito
Este checklist prova que cada peça física — save-the-date, mailer e insert por degrau de compra — **casa com o produto certo**, fala na voz do avatar e leva a uma ação rastreável. Existe porque mala direta é cara e lenta: um insert que promete o que o produto não entrega, ou um QR que não rastreia, queima verba e confunde o cliente. A peça vive longe do funil digital, então o vínculo oferta→produto→ação precisa ser explícito no papel. Sem este checklist verde, o mailer vira folheto bonito sem rastro de conversão. Ele garante o princípio `traceability_before_eloquence`: cada peça impressa serve a uma decisão de compra e deixa um rastro mensurável.

## Dono & Escopo
- **owner_agent:** `direct-mail-insert-writer` (escreve a peça e responde pela coerência); o [`voice-style-guardian`](../agents/voice-style-guardian.md) co-assina a voz e o [`tech-links-deliverability-engineer`](../agents/tech-links-deliverability-engineer.md) confirma que o QR/URL rastreia.
- **Artefato inspecionado:** o entregável `artifact.mailers-inserts` (peças de mala direta e inserts), registrado no [`control-registry`](../data/registries/control-registry.md).

## Condição de Passagem
Cada peça aponta para o produto/degrau correto do money model, traz UMA ação clara com CTA e QR/URL rastreáveis, e nenhum claim impresso está sem prova.

## Itens
1. **Casamento peça↔produto.** Como verificar: cada mailer/insert nomeia o produto ou degrau do money model que entrega, e o nome bate com o [`offer-registry`](../data/registries/offer-registry.md).
2. **CTA único e claro.** Como verificar: a peça tem UMA ação principal (não três); leia em voz alta — o próximo passo é óbvio em uma frase.
3. **QR/URL rastreável.** Como verificar: cada QR e cada URL carrega parâmetro de rastreio (UTM/código) e resolve para a página certa; o `tech-links-deliverability-engineer` confirma o link vivo.
4. **Claim com lastro.** Como verificar: todo número ou promessa impressa tem `proof_id` no [`proof-registry`](../data/registries/proof-registry.md); claim sem prova sai da peça.
5. **Escassez verdadeira.** Como verificar: se a peça cita prazo ou vagas, o limite é real e rastreado — escassez falsa = veto do `compliance-auditor`.
6. **Voz aprovada.** Como verificar: o `voice-style-guardian` deu `voice-verdict` APROVADO (3ª série, ativa, presente, sem jargão).
7. **Insert por degrau.** Como verificar: cada insert pós-compra corresponde ao degrau que o cliente acabou de comprar e oferece o próximo passo da sequência.
8. **Endereçamento e timing.** Como verificar: a peça declara segmento de destino e janela de envio coerente com a fase do lançamento.

## Evidência Exigida
Para marcar ✅: linkar a peça no `control-registry`, a linha do `offer-registry` que prova o casamento produto↔peça (item 1), a tabela claim→proof sem órfãos (item 4), o teste do QR/URL com parâmetro de rastreio resolvendo na página certa (item 3) e o `voice-verdict` APROVADO (item 6). Escassez citada exige o limite real linkado (item 5).

## Protocolo de Falha
Item vermelho → a peça volta ao `direct-mail-insert-writer` com o defeito nomeado e **não vai para impressão**. Claim sem lastro ou escassez falsa aciona veto do `compliance-auditor`. QR/URL quebrado volta ao `tech-links-deliverability-engineer`. Re-entrada: corrigir a peça, atualizar o `control-registry`, re-submeter. Mudança no produto ou no degrau do money model reabre este checklist para todas as peças afetadas.

## Links
- Frameworks: [`offer-stack-builder`](../frameworks/offer-stack-builder.md) · [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md) · [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md)
- Registries: [`control-registry`](../data/registries/control-registry.md) · [`claim-registry`](../data/registries/claim-registry.md) · [`proof-registry`](../data/registries/proof-registry.md) · [`offer-registry`](../data/registries/offer-registry.md)
- Agentes: [`direct-mail-insert-writer`](../agents/direct-mail-insert-writer.md) · [`voice-style-guardian`](../agents/voice-style-guardian.md) · [`tech-links-deliverability-engineer`](../agents/tech-links-deliverability-engineer.md)
- Checklists vizinhos: [`compliance-checklist`](compliance-checklist.md) · [`offer-stack-checklist`](offer-stack-checklist.md)
