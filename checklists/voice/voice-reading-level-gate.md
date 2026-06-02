---
id: checklist.voice.voice-reading-level-gate
title: "Gate — Nível de Leitura (a peça inteira fica em 3ª série)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
frameworks: [copy/hook-frameworks, copy/fascination-bullets]
registries: [control-registry]
tags: [gate, voz, legibilidade, 3a-serie, frase-curta, d4]
---

# Gate — Nível de Leitura

## Propósito
Este gate prova que **toda a peça de copy lê no nível de uma criança de 3ª série** — palavra curta, frase curta, uma ideia por vez. Ele existe porque copy que exige releitura perde a venda: o leitor real escaneia no celular, distraído, com pressa. Hormozi escreve assim de propósito — fala como gente fala, sem ornamento. Flesch provou que o texto entendido na primeira leitura converte mais. O `voice-style-guardian` mede cada frase contra a régua dura (§6): comprimento, número de vírgulas, palavra comum versus sofisticada. Vale o princípio `clarity_before_volume`: clareza vence quantidade. Uma frase acima do teto, uma palavra que uma criança não entende, e a frase recebe marca. Um acúmulo de marcas reprova a peça inteira. O guardião lê a peça toda, nunca uma amostra — aprovar o que não leu é a pior falha. Este gate não julga o mérito do claim nem o ângulo; julga **só a legibilidade**. A verdade do número segue como veto separado do `compliance-auditor`.

## Dono & Escopo
- **owner_agent:** `voice-style-guardian` (mede o nível de leitura frase a frase e emite o veredito).
- **Artefato inspecionado:** cada peça de copy de D4 — VSL, e-mail, SMS, mailer, ad, página — recebida dos autores. O veredito é registrado no [`control-registry`](../../data/registries/control-registry.md) ligado ao `asset_id`. A régua é o perfil [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md) e o [`reading-level-guide`](../../voice/reading-level-guide.md).

## Condição de Passagem
A peça inteira lê em nível de 3ª série — frases curtas, palavras comuns, uma ideia por frase — sem nenhum trecho acima do nível-alvo.

## Itens
1. **Frase curta.** Verificar: cada frase fica em ≤18 palavras (alvo ≤12); conte as palavras de cada uma.
2. **No máximo 1 vírgula.** Verificar: nenhuma frase tem 2+ vírgulas; duas vírgulas viram candidata a quebra em duas frases.
3. **Palavra comum.** Verificar: a palavra curta e comum vence a sofisticada; marque todo termo que uma criança não entende.
4. **Uma ideia por frase.** Verificar: cada frase carrega um pensamento só; frase com duas ideias é quebrada.
5. **Sem jargão desnecessário.** Verificar: nenhum termo técnico dispensável sem explicação simples no lugar.
6. **Peça inteira lida.** Verificar: o guardião auditou cada frase, não uma amostra; trechos truncados voltam.

## Evidência Exigida
Para marcar ✅: linkar o veredito no [`control-registry`](../../data/registries/control-registry.md) com o nível de leitura medido (alvo: 3ª série) e a contagem de marcas por frase. Frases reprovadas aparecem na redline `{linha, violação, correção sugerida}`. O perfil-régua e o `reading-level-guide` ficam citados como base da medição.

## Protocolo de Falha
Item vermelho → veredito **REPROVADO**. O [`voice-style-guardian`](../../agents/voice-style-guardian.md) devolve a redline ao autor com a linha, a violação e a correção que passa. O autor reescreve e reenvia; o guardião re-audita. Não existe "aprovado com ressalvas". Máximo de 3 rodadas antes de escalar ao [`offerbook-chief`](../../agents/offerbook-chief.md). Se um termo técnico-legal exigido pelo [`compliance-auditor`](../../agents/compliance-auditor.md) viola a 3ª série, a lei vence o estilo, mas o override é **registrado** no `decision-registry` pelo Chief. Re-entrada: corrigir as frases marcadas e re-submeter a peça inteira.

## Links
- Frameworks: [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Voz: [`voice-checklist`](../../voice/voice-checklist.md) · [`reading-level-guide`](../../voice/reading-level-guide.md) · [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)
- Agentes: [`voice-style-guardian`](../../agents/voice-style-guardian.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`voice-active-present-gate`](voice-active-present-gate.md) · [`voice-no-adverb-gate`](voice-no-adverb-gate.md) · [`voice-positive-language-gate`](voice-positive-language-gate.md) · [`voice-approval-gate`](voice-approval-gate.md)
