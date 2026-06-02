---
id: checklist.voice.voice-no-adverb-gate
title: "Gate — Sem Advérbios (zero advérbio floreado, zero redundância)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
frameworks: [copy/hook-frameworks, copy/fascination-bullets]
registries: [control-registry]
tags: [gate, voz, sem-adverbios, redundancia, economia, d4]
---

# Gate — Sem Advérbios

## Propósito
Este gate prova que **a peça não usa advérbio floreado nem palavra redundante**. Ele existe porque o advérbio quase sempre tapa um verbo fraco. "Corre rapidamente" é "dispara". "Realmente único" é "único" — ou é mentira. Strunk & White ensinam a cortar toda palavra que não trabalha. Hormozi mostra o número e a prova, não o exagero vazio. O `voice-style-guardian` caça as terminações `-mente` e os intensificadores de muleta ("muito", "realmente", "rapidamente", "provavelmente", "basicamente") e os corta ou troca por um verbo ou substantivo concreto. Caça também a redundância: sinônimos empilhados, ornamento e enchimento ("grátis de graça", "muito único"). Vale o princípio `clarity_before_volume`: cada palavra ganha o seu lugar ou sai. Um advérbio floreado, uma muleta, uma redundância — e a frase recebe marca. Um acúmulo de marcas reprova a peça. Este gate julga **só o ornamento e a redundância** — o mérito do claim segue como veto separado do `compliance-auditor`. Concreto vence abstrato: número, exemplo, prova.

## Dono & Escopo
- **owner_agent:** `voice-style-guardian` (caça advérbios e redundâncias, frase a frase, e emite o veredito).
- **Artefato inspecionado:** cada peça de copy de D4 — VSL, e-mail, SMS, mailer, ad, página. O veredito vai ao [`control-registry`](../../data/registries/control-registry.md) ligado ao `asset_id`. A régua é o perfil [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md) e o [`do-not-say`](../../voice/do-not-say.md).

## Condição de Passagem
A peça não contém advérbio floreado, intensificador de muleta nem palavra redundante; cada palavra mantida trabalha pela frase.

## Itens
1. **Sem terminação `-mente`.** Verificar: nenhum advérbio em `-mente` floreado; troque por verbo/substantivo concreto ou corte.
2. **Sem intensificador de muleta.** Verificar: zero "muito", "realmente", "rapidamente", "provavelmente", "basicamente" e afins.
3. **Sem redundância.** Verificar: nenhum sinônimo empilhado nem enchimento ("grátis de graça", "muito único", "totalmente completo").
4. **Concreto no lugar do exagero.** Verificar: onde havia adjetivo vazio, há número, exemplo ou prova ("corta 3 horas", não "incrível").
5. **Uma ideia por frase.** Verificar: nenhuma muleta ligando duas ideias na mesma frase; corte ou quebre.
6. **Sem hedge enfraquecedor.** Verificar: nenhum "talvez", "possivelmente", "meio que" amaciando o benefício.

## Evidência Exigida
Para marcar ✅: linkar o veredito no [`control-registry`](../../data/registries/control-registry.md) com a lista de advérbios, muletas e redundâncias marcados por frase, mais a redline `{linha, violação, correção sugerida}`. Cada corte mostra a versão concreta que entrou no lugar. O perfil-régua e o `do-not-say` ficam citados como base.

## Protocolo de Falha
Item vermelho → veredito **REPROVADO**. O [`voice-style-guardian`](../../agents/voice-style-guardian.md) devolve a redline com o advérbio/redundância e o corte ou a troca concreta. Quando o corte arrisca a força do gancho, o guardião gera ≥3 reescritas e escolhe a que preserva o benefício, ancorada em [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md). O autor corrige e reenvia; o guardião re-audita. Máximo de 3 rodadas antes de escalar ao [`offerbook-chief`](../../agents/offerbook-chief.md). Re-entrada: cortar/trocar cada marca e re-submeter a peça inteira.

## Links
- Frameworks: [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Voz: [`voice-checklist`](../../voice/voice-checklist.md) · [`do-not-say`](../../voice/do-not-say.md) · [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)
- Agentes: [`voice-style-guardian`](../../agents/voice-style-guardian.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`voice-reading-level-gate`](voice-reading-level-gate.md) · [`voice-active-present-gate`](voice-active-present-gate.md) · [`voice-positive-language-gate`](voice-positive-language-gate.md) · [`voice-approval-gate`](voice-approval-gate.md)
