---
id: checklist.voice.voice-active-present-gate
title: "Gate — Voz Ativa & Tempo Presente (o sujeito age, agora)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
frameworks: [copy/hook-frameworks, copy/fascination-bullets]
registries: [control-registry]
tags: [gate, voz, voz-ativa, tempo-presente, forca, d4]
---

# Gate — Voz Ativa & Tempo Presente

## Propósito
Este gate prova que **cada frase usa voz ativa e tempo presente** — o sujeito age, e age agora. Ele existe porque a voz passiva e o futuro enfraquecem a venda. "Os resultados serão alcançados" é frio e distante. "Você vê o resultado em dias" é forte e imediato. Hormozi vende no presente: o leitor sente o ganho enquanto lê, não numa promessa vaga de amanhã. O `voice-style-guardian` caça toda passiva evitável ("é feito", "serão enviados") e todo futuro dispensável ("você verá", "vai conseguir"). A correção é direta: ache o sujeito que age e ponha o verbo no presente. Vale o princípio `clarity_before_volume` somado à força da copy direta. Uma passiva natural e correta (sem agente claro) é a exceção rara, aceita e registrada. Mas a passiva preguiçosa, o gerúndio arrastado e o futuro à toa recebem marca. Um acúmulo de marcas reprova a peça. Este gate julga **só a voz e o tempo verbal** — o mérito do claim segue como veto separado do `compliance-auditor`.

## Dono & Escopo
- **owner_agent:** `voice-style-guardian` (marca cada passiva evitável e cada futuro dispensável, frase a frase).
- **Artefato inspecionado:** cada peça de copy de D4 — VSL, e-mail, SMS, mailer, ad, página. O veredito vai ao [`control-registry`](../../data/registries/control-registry.md) ligado ao `asset_id`. A régua é o perfil [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md).

## Condição de Passagem
Toda frase usa voz ativa e tempo presente, sem passiva evitável nem futuro dispensável, salvo exceção de passiva natural registrada.

## Itens
1. **Sujeito que age.** Verificar: cada frase tem um sujeito que pratica a ação ("Você emagrece"), não sofre a ação ("é emagrecido").
2. **Sem passiva evitável.** Verificar: nenhuma passiva preguiçosa ("serão enviados", "é feito") onde a ativa cabe; marque cada uma.
3. **Tempo presente.** Verificar: o verbo está no presente ("você vê"), não no futuro à toa ("você verá", "vai ver").
4. **Sem gerúndio arrastado.** Verificar: nenhum "está sabotando", "vai estar ganhando"; troque pelo presente direto.
5. **CTA no presente ativo.** Verificar: cada chamada à ação manda agir agora ("garanta hoje"), não numa promessa futura.
6. **Exceção de passiva registrada.** Verificar: toda passiva mantida é a forma natural correta, sem agente, com o motivo anotado.

## Evidência Exigida
Para marcar ✅: linkar o veredito no [`control-registry`](../../data/registries/control-registry.md) com a contagem de passivas e futuros marcados por frase, mais a redline `{linha, violação, correção sugerida}`. Cada exceção de passiva natural aceita carrega o motivo anotado. O perfil-régua fica citado como base.

## Protocolo de Falha
Item vermelho → veredito **REPROVADO**. O [`voice-style-guardian`](../../agents/voice-style-guardian.md) devolve a redline com a frase passiva/futura e a versão ativa no presente. Quando a intenção persuasiva corre risco, o guardião gera ≥3 reescritas e escolhe a que preserva a força sem amaciar o benefício, ancorada em [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md). O autor corrige e reenvia; o guardião re-audita. Máximo de 3 rodadas antes de escalar ao [`offerbook-chief`](../../agents/offerbook-chief.md). Re-entrada: reescrever as frases marcadas em voz ativa e presente, depois re-submeter a peça inteira.

## Links
- Frameworks: [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Voz: [`voice-checklist`](../../voice/voice-checklist.md) · [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)
- Agentes: [`voice-style-guardian`](../../agents/voice-style-guardian.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`voice-reading-level-gate`](voice-reading-level-gate.md) · [`voice-no-adverb-gate`](voice-no-adverb-gate.md) · [`voice-positive-language-gate`](voice-positive-language-gate.md) · [`voice-approval-gate`](voice-approval-gate.md)
