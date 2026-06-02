---
id: checklist.voice.voice-positive-language-gate
title: "Gate — Linguagem Positiva (diz o ganho e a ação, não só o medo)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
frameworks: [copy/hook-frameworks, copy/fascination-bullets]
registries: [control-registry]
tags: [gate, voz, enquadramento-positivo, ganho, acao, d4]
---

# Gate — Linguagem Positiva

## Propósito
Este gate prova que **cada frase diz o ganho e a ação, não só o medo**. Ele existe porque o enquadramento negativo afasta o leitor em vez de movê-lo. "Não fique para trás" lembra a dor sem mostrar a saída. "Saia na frente hoje" mostra o ganho e o que fazer. Hormozi vende o resultado que o leitor quer, não o castigo que ele teme. O `voice-style-guardian` checa cada frase: ela aponta o benefício e a próxima ação, ou só assusta? O medo dispensável vira marca; o ganho concreto passa. Vale o princípio `clarity_before_volume` somado à força da copy direta. Uma frase que só nega ("pare de errar", "evite o fracasso") recebe marca quando a versão positiva cabe e vende melhor. Um acúmulo de marcas reprova a peça. O guardião lê a peça toda, nunca uma amostra. Este gate julga **só o enquadramento** — diz o ganho, não só o medo. O mérito do claim e a verdade do número seguem como veto separado do `compliance-auditor`. Concreto vence vago: mostre o resultado, não a ameaça.

## Dono & Escopo
- **owner_agent:** `voice-style-guardian` (checa o enquadramento de cada frase e emite o veredito).
- **Artefato inspecionado:** cada peça de copy de D4 — VSL, e-mail, SMS, mailer, ad, página. O veredito vai ao [`control-registry`](../../data/registries/control-registry.md) ligado ao `asset_id`. A régua é o perfil [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md) e o [`do-not-say`](../../voice/do-not-say.md).

## Condição de Passagem
Toda frase diz o ganho e a ação, sem enquadramento negativo dispensável, salvo a urgência verdadeira que o claim sustenta.

## Itens
1. **Diz o ganho.** Verificar: cada frase aponta o benefício que o leitor quer ("ganha 3 horas"), não só a perda que ele teme.
2. **Manda agir.** Verificar: a chamada diz a ação positiva ("garanta hoje"), não só o que evitar ("não perca").
3. **Sem medo dispensável.** Verificar: nenhuma frase usa ameaça vazia onde a versão de ganho cabe e vende mais.
4. **Sem culpa ou vergonha.** Verificar: a copy não envergonha o leitor ("você falhou de novo"); ela mostra o caminho à frente.
5. **Urgência verdadeira.** Verificar: toda urgência ("fecha amanhã") é um fato real do `decision-registry`, não medo inventado.
6. **Concreto no ganho.** Verificar: o benefício é número, exemplo ou prova ("a balança cai"), não adjetivo vago.

## Evidência Exigida
Para marcar ✅: linkar o veredito no [`control-registry`](../../data/registries/control-registry.md) com a contagem de frases de enquadramento negativo marcadas, mais a redline `{linha, violação, correção sugerida}`. Cada marca mostra a versão positiva que entrou no lugar. Toda urgência mantida aponta ao fato real que a sustenta. O perfil-régua e o `do-not-say` ficam citados como base.

## Protocolo de Falha
Item vermelho → veredito **REPROVADO**. O [`voice-style-guardian`](../../agents/voice-style-guardian.md) devolve a redline com a frase negativa e a versão positiva que diz o ganho. Quando a intenção persuasiva corre risco, o guardião gera ≥3 reescritas e escolhe a que preserva a força sem amaciar o benefício, ancorada em [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md). O autor corrige e reenvia; o guardião re-audita. Não existe "aprovado com ressalvas". Máximo de 3 rodadas antes de escalar ao [`offerbook-chief`](../../agents/offerbook-chief.md). Urgência apresentada como medo sem lastro vira flag ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto de escassez falsa. Re-entrada: reescrever cada frase marcada em enquadramento positivo e re-submeter a peça inteira.

## Links
- Frameworks: [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Voz: [`voice-checklist`](../../voice/voice-checklist.md) · [`do-not-say`](../../voice/do-not-say.md) · [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)
- Agentes: [`voice-style-guardian`](../../agents/voice-style-guardian.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`voice-reading-level-gate`](voice-reading-level-gate.md) · [`voice-active-present-gate`](voice-active-present-gate.md) · [`voice-no-adverb-gate`](voice-no-adverb-gate.md) · [`voice-approval-gate`](voice-approval-gate.md)
