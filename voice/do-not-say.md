---
id: voice.do-not-say
title: "Do-Not-Say — O Que a Voz Bane"
type: voice
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
tags: [voz, banir, jargao, voz-passiva, adverbios, redundancia, hedge]
---

# Do-Not-Say — O Que a Voz Bane

Lista dura do que **não** entra na copy do squad. Cada item enfraquece a voz: tira clareza, tira força ou tira confiança. O [voice-style-guardian](../agents/voice-style-guardian.md) caça estes padrões frase a frase e veta a peça que os contém. Esta lista é a régua do veto: se está aqui, marca. Use junto com o [reading-level-guide](reading-level-guide.md), a [tone-matrix](tone-matrix.md) e o [voice-checklist](voice-checklist.md). Cada perfil em [profiles/](profiles/) herda esta lista e pode acrescentar banimentos próprios.

## Regra-mãe

Se a palavra não trabalha, ela sai. Se a frase tem duas formas e uma é mais simples, fica a simples. Se o termo soa de gabinete, troque pelo termo da rua. Toda exceção precisa de motivo escrito.

## 1. Advérbios floreados (banir)

Terminações em `-mente` e intensificadores vazios. Eles dizem que algo é forte sem mostrar. Mostre com verbo e número.

- **Banir:** rapidamente, basicamente, realmente, simplesmente, literalmente, efetivamente, absolutamente, completamente, totalmente, extremamente.
- **Banir intensificadores:** muito, bastante, super, mega, demais (como muleta), tão.
- **Conserto:** troque por fato. "Cresce rapidamente" vira "dobra em 30 dias".

## 2. Hedge e incerteza (banir)

Palavra que pede desculpa enfraquece a promessa. A voz é firme, não tímida.

- **Banir:** talvez, pode ser, possivelmente, provavelmente, de repente, quem sabe, eventualmente, meio que, de certa forma, acho que.
- **Conserto:** afirme ou corte. "Você provavelmente vê resultado" vira "Você vê o resultado".

## 3. Voz passiva e futuro arrastado (banir)

A passiva esconde quem age. O futuro adia a entrega. A voz mostra o sujeito agindo agora.

- **Banir construções:** "será feito", "foi alcançado", "é oferecido", "serão obtidos", "vem sendo".
- **Banir futuro desnecessário:** "você vai conseguir", "os resultados virão", "será possível".
- **Conserto:** "Os resultados serão alcançados" vira "Você alcança o resultado".

## 4. Jargão de gabinete (banir)

Palavra corporativa que não diz nada. Cheira a apresentação de slide, não a conversa honesta.

- **Banir:** sinergia, alavancar (sem número), paradigma, disruptar, escalar (vago), holístico, robusto, solução end-to-end, mindset, ecossistema, alinhamento estratégico.
- **Conserto:** diga o que faz. "Alavancar resultados" vira "dobrar a venda".

## 5. Superlativo e hype vazio (banir)

Adjetivo grande sem prova queima a confiança. O leitor cético desliga.

- **Banir:** incrível, revolucionário, único de verdade, transformador, explosivo, definitivo, infalível, garantido (sem termo), o melhor do mercado, número um.
- **Conserto:** troque o adjetivo por evidência. "Resultado incrível" vira "412 vendas em 30 dias".

## 6. Redundância e enchimento (banir)

Palavra repetida ou frase de aquecimento. Vai direto ao ponto.

- **Banir enchimento:** "na verdade", "vale ressaltar que", "é importante notar", "como você sabe", "sem mais delongas", "antes de mais nada".
- **Banir redundância:** "grátis de graça", "elo de ligação", "planejar antecipadamente", "surpresa inesperada", "juntos em conjunto".
- **Conserto:** corte a muleta e a repetição. "Na verdade, isso basicamente ajuda" vira "Isto resolve seu problema".

## 7. Enquadramento negativo desnecessário (banir)

Dizer só o que evitar ativa o medo, não o desejo. Diga o ganho e a ação.

- **Banir como padrão:** "não fique para trás", "não perca", "pare de fracassar", "evite o erro de".
- **Conserto:** vire para o ganho. "Não fique para trás" vira "Saia na frente hoje".

## 8. Escassez e claim falsos (veto duro)

Pior que voz fraca: voz desonesta. Aqui o veto é do [compliance-auditor](../agents/compliance-auditor.md), não só do guardião.

- **Banir:** prazo que não acaba, "vagas limitadas" sem limite real, contador que reinicia, "últimas unidades" falso, depoimento sem prova, número sem fonte.
- **Conserto:** diga só o que é verdade. Se a vaga não fecha sexta, não diga que fecha.

## Exemplos Faz/Não-faz

| Não-faz (banido) | Faz (limpo) |
|---|---|
| "Na verdade, esse método é simplesmente revolucionário." | "Este método dobra sua venda em 60 dias." |
| "Os resultados provavelmente serão alcançados pelos alunos." | "Você alcança o resultado em semanas." |
| "Vamos alavancar sinergias para escalar seu negócio." | "Você triplica os pedidos com um passo simples." |
| "Não perca essa oportunidade absolutamente única." | "Garanta sua vaga hoje." |
| "Vale ressaltar que, de certa forma, isso pode ajudar." | "Isto resolve seu maior gargalo." |

## Notas de Compliance

O item 8 cruza com o veto de [compliance-auditor](../agents/compliance-auditor.md): escassez falsa e claim sem lastro são vetos de verdade, não só de estilo. Todo número vem do [proof-registry](../data/registries/proof-registry.md); toda afirmação, do [claim-registry](../data/registries/claim-registry.md). Quando um termo banido é exigido por lei (um disclaimer técnico, por exemplo), ele fica e o caso sobe ao [offerbook-chief](../agents/offerbook-chief.md). A lista bane o que enfraquece, nunca o que a lei obriga.
