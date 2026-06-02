---
id: checklist.avatar.avatar-dominant-emotion-gate
title: "Gate — Emoção Dominante Nomeada e Ancorada em Verbatims (o motor da copy)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
frameworks: [avatar-voc-investigator/voc-mining, positioning/jtbd]
registries: [objection-registry]
tags: [gate, avatar, emocao-dominante, d1, motor-emocional, big-idea]
---

# Gate — Emoção Dominante Nomeada e Ancorada

## Propósito
Este gate prova que o `avatar-voc-investigator` nomeou a **emoção dominante** de cada segmento e a ancorou na frequência real dos verbatims, não na intuição. Existe porque a emoção dominante é o motor da copy: errar entre "frustração com o tempo perdido" e "medo da humilhação pública" faz a Big Idea falar com a cabeça errada do cliente. Esta é a escolha mais alavancada do agente, e por isso ela é decidida por **contagem nos verbatims** (em quantos a emoção aparece literalmente), não por palpite. O `big-idea-architect` ancora a tese nesta emoção; os escritores escolhem o tom por ela. Uma emoção dominante sem lastro nos verbatims contamina toda a persuasão a jusante.

## Dono & Escopo
- **owner_agent:** `avatar-voc-investigator` (extrai a emoção do conjunto de verbatims).
- **Artefato inspecionado:** o **bloco de emoção dominante** do avatar/ICP, por segmento, com a âncora de frequência (n/total de verbatims) e a contra-evidência considerada.

## Condição de Passagem
Cada segmento tem uma emoção dominante nomeada, ancorada em pelo menos três verbatims, escolhida pela frequência real e não pela intuição do agente.

## Itens
1. **Emoção nomeada por segmento.** Verificar: cada segmento tem exatamente uma emoção dominante nomeada (ex.: "medo de falhar como mãe"), não uma lista vaga.
2. **Âncora de frequência.** Verificar: a emoção está ancorada em ≥3 verbatims, com a contagem visível (ex.: 8 de 12).
3. **Candidatas pontuadas.** Verificar: o agente gerou ≥3 emoções candidatas e pontuou por frequência, intensidade e alavancagem (Tree-of-Thoughts), registrando as podadas.
4. **Linguagem visceral citada.** Verificar: a intensidade da emoção é sustentada por linguagem visceral nos verbatims, não por adjetivo do agente.
5. **Contra-evidência buscada.** Verificar: o agente checou se há verbatims que contradizem a emoção escolhida e explicou por que ela ainda vence (`contradiction_before_conclusion`).
6. **Casa com o JTBD.** Verificar: a emoção dominante é coerente com o Job To Be Done emocional/social do segmento (do [`avatar-jtbd-gate`](avatar-jtbd-gate.md)).
7. **Coerente com a consciência.** Verificar: o registro emocional bate com o nível de consciência herdado do market-brief (nível 2 = dor crua; nível 4 = comparação/hesitação).

## Evidência Exigida
Para marcar cada item ✅, linkar o bloco de emoção dominante do avatar com a âncora de frequência (n/total), os ≥3 verbatims que a sustentam e a tabela de candidatas pontuadas com as podadas. A contagem precisa ser reproduzível a partir do banco de VOC. A coerência com o nível de consciência linka o [`market-awareness-gate`](../market/market-awareness-gate.md). O permalink do avatar conta como evidência.

## Protocolo de Falha
Item vermelho → o `avatar-voc-investigator` **refaz a escolha** a partir da frequência real, não da intuição. Emoção dominante sem ≥3 verbatims → não passa. Emoção escolhida por palpite → re-pontua as candidatas por frequência (ToT) e corrige. Contra-evidência forte ignorada → reabre a escolha. Emoção incoerente com a consciência → revisa contra o market-brief. Re-entrada: ancorada a emoção na contagem, o gate é re-submetido. O agente não tem veto; sinaliza ao `offerbook-chief` se a emoção dominante revelar uma objeção fatal recorrente.

## Links
- Frameworks: [`voc-mining`](../../frameworks/avatar-voc-investigator/voc-mining.md) · [`jtbd`](../../frameworks/positioning/jtbd.md)
- Registries: [`objection-registry`](../../data/registries/objection-registry.md)
- Agentes: [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`big-idea-architect`](../../agents/big-idea-architect.md)
- Gate de origem (verbatims): [`avatar-voc-verbatim-gate`](avatar-voc-verbatim-gate.md)
- Nível de consciência a montante: [`market-awareness-gate`](../market/market-awareness-gate.md)
