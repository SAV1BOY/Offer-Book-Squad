---
id: checklist.voice.voice-approval-gate
title: "Gate — Aprovação de Voz (a peça passa nos cinco gates de voz ou volta)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
frameworks: [copy/hook-frameworks, copy/fascination-bullets]
registries: [control-registry]
tags: [gate, voz, aprovacao, veredito, veto, d4]
---

# Gate — Aprovação de Voz

## Propósito
Este gate prova que **a peça inteira passa na régua dura de voz e nos cinco gates antes de seguir ao downstream**. Ele é o veredito final do `voice-style-guardian`: **APROVADO** ou **REPROVADO**, sem meio-termo. Ele existe porque cada peça precisa de um passe único que consolida os quatro testes — nível de leitura, voz ativa e presente, sem advérbio, enquadramento positivo — num só carimbo. Nenhuma copy chega ao [`funnel-architect`](../../agents/funnel-architect.md) ou ao [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) sem esse passe. Vale o princípio `clarity_before_volume`: a marca soa igual em toda peça, ou a peça volta. O guardião lê a peça toda, frase a frase, nunca uma amostra — aprovar o que não leu é a pior falha. Uma única violação dura marca a frase; um acúmulo de marcas reprova a peça. Não existe "aprovado com ressalvas". Este gate julga **só a voz** — o mérito do claim e a verdade do número seguem como veto separado e independente do `compliance-auditor`. As duas barreiras passam, ou a peça não vai ao ar.

## Dono & Escopo
- **owner_agent:** `voice-style-guardian` (consolida os cinco gates num único veredito por peça).
- **Artefato inspecionado:** cada peça de copy de D4 — VSL, e-mail, SMS, mailer, ad, página — recebida dos autores com origem declarada. O veredito vai ao [`control-registry`](../../data/registries/control-registry.md) ligado ao `asset_id`. A régua é o [`voice-checklist`](../../voice/voice-checklist.md) e o perfil [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md).

## Condição de Passagem
A peça inteira passa nos cinco gates de voz e recebe veredito APROVADO, ou volta ao autor com a redline.

## Itens
1. **Nível de leitura.** Verificar: a peça passa no [`voice-reading-level-gate`](voice-reading-level-gate.md) — 3ª série, frase curta, palavra comum.
2. **Voz ativa e presente.** Verificar: a peça passa no [`voice-active-present-gate`](voice-active-present-gate.md) — sujeito age, no presente.
3. **Sem advérbio.** Verificar: a peça passa no [`voice-no-adverb-gate`](voice-no-adverb-gate.md) — zero advérbio floreado, zero redundância.
4. **Linguagem positiva.** Verificar: a peça passa no [`voice-positive-language-gate`](voice-positive-language-gate.md) — diz o ganho e a ação.
5. **Peça inteira lida.** Verificar: o guardião auditou cada frase, com origem e autor declarados; peça truncada volta.
6. **Veredito binário.** Verificar: o resultado é APROVADO ou REPROVADO, sem "aprovado com ressalvas".
7. **Registro do veredito.** Verificar: o veredito e as marcas estão no `control-registry` ligados ao `asset_id`.

## Evidência Exigida
Para marcar ✅: linkar o veredito consolidado no [`control-registry`](../../data/registries/control-registry.md) com o resultado de cada um dos quatro gates, o nível de leitura medido (alvo: 3ª série) e a redline `{linha, violação, correção sugerida}` quando reprovado. Um override só conta com o `decision_id` explícito do Chief no [`decision-registry`](../../data/registries/decision-registry.md). O `voice-checklist` e o perfil-régua ficam citados como base.

## Protocolo de Falha
Qualquer gate vermelho → veredito **REPROVADO** para a peça inteira. O [`voice-style-guardian`](../../agents/voice-style-guardian.md) devolve a redline ao autor com a linha, a violação e a correção que passa. O autor reescreve e reenvia; o guardião re-audita. Máximo de 3 rodadas antes de escalar o impasse ao [`offerbook-chief`](../../agents/offerbook-chief.md). Só o Chief libera uma peça reprovada, com decisão **registrada** no `decision-registry` — o caso típico é um termo técnico-legal que o [`compliance-auditor`](../../agents/compliance-auditor.md) exige e que viola a 3ª série: a lei vence o estilo, mas o override fica gravado. Override sem registro não existe. Re-entrada: corrigir as frases marcadas e re-submeter a peça inteira para novo veredito.

## Links
- Frameworks: [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Voz: [`voice-checklist`](../../voice/voice-checklist.md) · [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md) · [`tone-matrix`](../../voice/tone-matrix.md)
- Agentes: [`voice-style-guardian`](../../agents/voice-style-guardian.md) · [`compliance-auditor`](../../agents/compliance-auditor.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`voice-reading-level-gate`](voice-reading-level-gate.md) · [`voice-active-present-gate`](voice-active-present-gate.md) · [`voice-no-adverb-gate`](voice-no-adverb-gate.md) · [`voice-positive-language-gate`](voice-positive-language-gate.md)
