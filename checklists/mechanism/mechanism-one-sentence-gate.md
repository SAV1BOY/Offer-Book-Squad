---
id: checklist.mechanism.mechanism-one-sentence-gate
title: "Gate — Mecanismo Comprimido em Uma Frase que o Avatar Repete e Acredita"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
frameworks: [unique-mechanism]
registries: [offer-registry]
tags: [gate, mechanism, one-sentence, d2, big-idea, clareza]
---

# Gate — Mecanismo Comprimido em Uma Frase

## Propósito
Este gate prova que o `mechanism-architect` comprimiu o mecanismo em **uma frase** que o avatar entende e acredita na primeira leitura. Existe porque um mecanismo que precisa de um parágrafo para ser explicado não cabe na cabeça do cliente nem na abertura de uma VSL. A frase é a matéria-prima da Big Idea: o `big-idea-architect` a recebe como insumo direto. Ela precisa caber numa leitura de 3ª série, reposicionar a culpa e soar crível — tudo de uma vez. O teste é simples e duro: "o avatar entende e acredita na primeira leitura?". Se a frase precisa de nota de rodapé, o mecanismo não está pronto. É o último portão da tríade do mecanismo, e o que entrega o núcleo conceitual destilado para D3.

## Dono & Escopo
- **owner_agent:** `mechanism-architect` (comprime o mecanismo em [`unique-mechanism`](../../frameworks/unique-mechanism.md)).
- **Artefato inspecionado:** a **frase única** do `mechanism-sheet`, registrada em `frase_unica` no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O mecanismo cabe em uma frase de leitura simples, que reposiciona a culpa e soa crível, e o avatar a entende e acredita na primeira leitura.

## Itens
1. **Uma frase só.** Verificar: o mecanismo está em uma única frase, não em um parágrafo nem em duas orações encadeadas longas.
2. **Leitura de 3ª série.** Verificar: a frase usa linguagem simples, voz ativa e tempo presente, sem jargão (conforme o guia de voz).
3. **Reposiciona a culpa.** Verificar: a frase tira o peso do avatar ("você não falhou — seu termostato metabólico travou, e ele pode ser reajustado").
4. **Crível na primeira leitura.** Verificar: a frase não estoura a credibilidade; o avatar cético não a rejeita de imediato.
5. **Contém o nome do mecanismo.** Verificar: a frase carrega o nome próprio batizado no [`mechanism-naming-gate`](mechanism-naming-gate.md).
6. **O avatar repete sozinho.** Verificar: a frase é curta e clara o bastante para o avatar reproduzi-la com as próprias palavras.
7. **Sem promessa proibida.** Verificar: a frase não embute cura/garantia que o `compliance-auditor` rejeitaria.

## Evidência Exigida
Para marcar cada item ✅, linkar a `frase_unica` no `mechanism-sheet` e a linha do [`offer-registry`](../../data/registries/offer-registry.md). A frase precisa aparecer literalmente entre aspas. A presença do nome do mecanismo linka o [`mechanism-naming-gate`](mechanism-naming-gate.md); a ausência de promessa proibida linka a checagem de compliance. O permalink da linha do registry conta como evidência. O teste de 1ª leitura é registrado (passou/refez).

## Protocolo de Falha
Item vermelho → o `mechanism-architect` **reescreve o enquadramento** (não só troca palavras): se a frase não passa no teste de 1ª leitura, o problema costuma ser o enquadramento, não a redação. Frase longa demais → corta para uma oração. Jargão → substitui por linguagem de 3ª série. Promessa proibida → remove o claim e reancorar em prazo/resultado crível. Re-entrada: aprovada a frase no teste de 1ª leitura, o gate é re-submetido e a frase segue como insumo da Big Idea. O agente não tem veto; entrega a frase ao `big-idea-architect`. Máximo de 3 ciclos antes de escalar ao chief.

## Links
- Frameworks: [`unique-mechanism`](../../frameworks/unique-mechanism.md) · [`power-of-one`](../../frameworks/power-of-one.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`mechanism-architect`](../../agents/mechanism-architect.md) · [`big-idea-architect`](../../agents/big-idea-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gate anterior (nome): [`mechanism-naming-gate`](mechanism-naming-gate.md) · Contraste: [`mechanism-old-vs-new-gate`](mechanism-old-vs-new-gate.md)
- Matéria-prima da Big Idea a jusante: [`avatar-jtbd-gate`](../avatar/avatar-jtbd-gate.md)
