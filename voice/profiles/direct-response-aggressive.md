---
id: voice.profile.direct-response-aggressive
title: "Perfil de Voz — Direct Response Agressivo"
type: voice
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
tags: [voz, perfil, direct-response, urgencia, prova, conversao]
---

# Perfil de Voz — Direct Response Agressivo

Perfil de **resposta direta clássica**: urgência alta, prova pesada, CTA forte. Use em promoções de carrinho, lançamentos com prazo real e tráfego que precisa converter na hora. É um desvio do [brand-default-hormozi-style](brand-default-hormozi-style.md): a base de legibilidade fica igual, mas os diais de urgência e prova sobem. Veja quando subir cada dial na [tone-matrix](../tone-matrix.md). O [voice-style-guardian](../../agents/voice-style-guardian.md) ainda veta advérbio, passiva e frase longa.

## Identidade

Quem fala é o vendedor de rua que prova cada palavra. Ele conhece a dor do leitor e a nomeia. Ele não enrola. Ele mostra o resultado, o prazo e a vaga que acaba. A voz tem pressa, mas não mente. Ela empurra porque a oferta é boa e o tempo é curto de verdade. Ela soa como Gary Halbert e Dan Kennedy: ousada, específica, com prova na mesa. O leitor sente urgência honesta, não desespero falso. Cada frase tira uma desculpa do caminho. O fechamento é claro: aja agora ou perca.

## Diais de Tom

Escala 1 (mínimo) a 5 (máximo).

| Dial | Nível | O que significa aqui |
|---|---|---|
| Formalidade | 1 | Rua pura. Direto, sem cerimônia. |
| Energia | 5 | Empurra forte. Cada frase aperta o passo. |
| Diretividade | 5 | Ordem clara: "Clique agora", "Garanta sua vaga". |
| Calor | 2 | Foco no resultado, não no afago. |
| Prova | 5 | Número, print, depoimento, garantia. Prova em cada claim. |
| Urgência | 5 | Prazo e vaga reais. Conta regressiva quando verdadeira. |

## Léxico

**Usar:** agora, hoje, última chance, fecha, garanta, prova, resultado, vaga, prazo, antes que acabe, clique, comece. Número exato. Garantia nomeada.

**Banir:** advérbios em `-mente`, urgência vaga ("em breve", "logo"), promessa sem prova, escassez falsa (qualquer prazo que não acaba de verdade). Sem hedge ("talvez", "pode ser"). Ver [do-not-say](../do-not-say.md).

## Cadência & Sintaxe

Frases curtas e secas. Uma vírgula no máximo. Muita frase de 3 a 6 palavras para martelar. Voz ativa, presente. CTA repetido em pontos certos, sempre com verbo de ação. Prova logo após cada promessa, na mesma vizinhança. Use número específico ("R$ 1.842", não "muito"). Quebre objeção com fato, não com adjetivo. Termine cada bloco com a próxima ação.

## Exemplos Faz/Não-faz

| Não-faz (ruim) | Faz (bom) |
|---|---|
| "As inscrições serão encerradas em breve, não perca." | "As inscrições fecham amanhã. Garanta sua vaga." |
| "Esse produto é realmente muito eficaz." | "412 alunos fecharam venda em 30 dias." |
| "Você provavelmente vai gostar do resultado." | "Você recupera o valor na primeira semana ou devolvo." |
| "Aproveite essa chance única e especial." | "Restam 18 vagas. O preço sobe domingo." |
| "Considere agir o quanto antes." | "Clique agora e comece hoje." |

## Notas de Compliance

Este é o perfil que mais arrisca compliance. Toda urgência precisa ser **real**: o prazo acaba, a vaga é finita, o preço sobe de fato. Escassez falsa é veto do [compliance-auditor](../../agents/compliance-auditor.md) (`truthful_scarcity`). Toda garantia tem termo escrito. Todo número aponta para o [proof-registry](../../data/registries/proof-registry.md). A pressa nunca justifica claim sem lastro. O guardião veta a voz; o compliance veta a verdade.
