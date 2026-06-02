---
id: checklist.email-sms.email-subject-gate
title: "Gate — Subject Lines (abrem sem clickbait, batem com o corpo)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
frameworks: [copy/email-sequence-architecture, copy/slippery-slide]
registries: [control-registry]
tags: [gate, email, sms, subject, pre-header, anti-clickbait, d4]
---

# Gate — Subject Lines

## Propósito
Este gate prova que cada e-mail-chave tem um **subject que abre — sem clickbait — e que bate com o corpo**. O subject é o gancho do e-mail: se não para o dedo na caixa de entrada, o melhor corpo nunca é lido. Mas um subject que promete o que o corpo não entrega ("Você ganhou R$1.000") destrói a confiança, treina o leitor a ignorar a marca e machuca a entregabilidade. O gate força o Tree-of-Thoughts do agente — gerar três ou mais subjects por e-mail-chave (curiosidade, benefício, urgência), mais o pré-header, e podar os fracos — e exige **congruência**: a promessa do subject é cumprida no corpo. Ele também checa o fit com a consciência do segmento (subject de descoberta para frio, subject direto para quente) e a abertura como primeiro degrau da slippery slide. É a barreira entre a abertura honesta e o grito vazio.

## Dono & Escopo
- **owner_agent:** `email-sms-sequence-writer` (sem poder de veto; saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md), que **veta** voz fora do padrão).
- **Artefato inspecionado:** os campos `subject`, `subject_variantes` (podadas) e `pre_header` de cada mensagem-chave na `sequence-matrix` do [`control-registry`](../../data/registries/control-registry.md), gerados via o Tree-of-Thoughts de subjects do agente.

## Condição de Passagem
Cada e-mail-chave tem um subject vencedor escolhido entre ao menos três candidatos, com pré-header, que para o leitor sem clickbait e cuja promessa o corpo cumpre.

## Itens
1. **Candidatos gerados.** Verificar: cada e-mail-chave tem ≥3 subjects candidatos, com os podados nomeados em `subject_variantes`.
2. **Pré-header presente.** Verificar: o subject vem com um pré-header que complementa (não repete) a linha de assunto.
3. **Para o leitor.** Verificar: o subject vencedor interrompe o padrão da caixa (curiosidade, benefício ou urgência concretos), não é genérico.
4. **Sem clickbait.** Verificar: a promessa do subject é cumprida no corpo; nenhum subject promete o que o corpo não entrega.
5. **Fit com a consciência do segmento.** Verificar: a abordagem do subject casa com o nível do segmento (descoberta para frio, direto para quente).
6. **Primeiro degrau da slippery slide.** Verificar: o subject puxa para a primeira linha do corpo, que puxa para a seguinte.
7. **Registrado.** Verificar: subject vencedor, variantes podadas e pré-header estão no `control-registry`.

## Evidência Exigida
Para marcar ✅: linkar a `sequence-matrix` no `control-registry` com os candidatos e o vencedor por e-mail-chave (itens 1, 7), o pré-header (item 2), a verificação subject↔corpo que descarta clickbait (itens 3–4) e o fit com a consciência do segmento mais a transição para o corpo (itens 5–6).

## Protocolo de Falha
Item vermelho → o `email-sms-sequence-writer` volta ao Tree-of-Thoughts e regera os subjects do e-mail com defeito; clickbait é reprovação e reescreve-se o subject para a promessa que o corpo cumpre. Subject fora de voz volta ao [`voice-style-guardian`](../../agents/voice-style-guardian.md). Subject incoerente com a consciência → realinha ao segmento. Re-entrada: atualiza `subject`/`pre_header` no `control-registry` e re-submete. Mudança de corpo reabre este gate.

## Links
- Gates irmãos: [`email-step-coverage-gate`](email-step-coverage-gate.md) · [`email-segmentation-gate`](email-segmentation-gate.md) · [`email-timing-gate`](email-timing-gate.md) · [`email-urgency-coherence-gate`](email-urgency-coherence-gate.md)
- Frameworks: [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md) · [`slippery-slide`](../../frameworks/copy/slippery-slide.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
