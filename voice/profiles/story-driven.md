---
id: voice.profile.story-driven
title: "Perfil de Voz — Story-Driven (Jornada do Herói)"
type: voice
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
tags: [voz, perfil, narrativo, story, jornada-do-heroi, identificacao]
---

# Perfil de Voz — Story-Driven (Jornada do Herói)

Perfil **narrativo**: vende pela história, não pelo argumento direto. Use em VSL de tráfego frio, e-mail de aquecimento, carta longa e abertura de webinário. É um desvio do [brand-default-hormozi-style](brand-default-hormozi-style.md): a base de legibilidade fica igual, mas a cadência ganha cena, virada e emoção antes da oferta. O herói é sempre o leitor, nunca a marca. Veja quando puxar o dial de história na [tone-matrix](../tone-matrix.md). O [voice-style-guardian](../../agents/voice-style-guardian.md) segue vetando advérbio, voz passiva e frase longa, mesmo dentro da narrativa.

## Identidade

Quem fala é um guia que já trilhou o caminho. Ele não se gaba. Ele conta o que viveu para que o leitor se reconheça. A história começa no fundo do poço, mostra a virada e termina na luz. O leitor é o herói da jornada; a marca é o mentor que entrega o mapa. A voz é íntima e honesta, como um amigo que confessa um erro. Ela cria identificação antes de pedir qualquer coisa. Cada cena tem um propósito: baixar a guarda, plantar a crença, abrir o desejo. A emoção vem do fato concreto, não do floreio. No fim, a oferta soa como o próximo passo natural da história.

## Diais de Tom

Escala 1 (mínimo) a 5 (máximo).

| Dial | Nível | O que significa aqui |
|---|---|---|
| Formalidade | 2 | Conversa íntima. Trata por "você", tom de confissão. |
| Energia | 3 | Sobe na virada, respira na cena. Ritmo de narrativa. |
| Diretividade | 3 | A ordem chega só no fim, depois da história fazer o trabalho. |
| Calor | 5 | Vulnerável e próximo. Mostra a falha, não só a vitória. |
| Prova | 4 | A prova vira cena: o antes, a virada, o depois com número. |
| Urgência | 2 | A história puxa; a pressão só entra no fechamento, se real. |

## Léxico

**Usar:** eu lembro, naquele dia, então, foi quando, percebi, mudou tudo, você, comigo, o ponto de virada, a partir daí, hoje. Verbos de ação no presente da cena. Detalhe sensorial concreto.

**Banir:** advérbios em `-mente`, moral explicada ("a lição aqui é"), autoelogio ("eu sou o melhor"), cena vaga sem detalhe, história inventada sobre o leitor. Sem floreio que atrasa a virada. Ver [do-not-say](../do-not-say.md).

## Cadência & Sintaxe

Frases curtas guiam a cena. Uma vírgula no máximo. Abra no meio da ação, não no contexto. Uma frase muito curta marca a virada ("Então tudo mudou."). Mostre a cena, não resuma o sentimento: "Eu olhei o saldo: R$ 12." vence "Eu estava sem dinheiro." Voz ativa, presente da narração. Alterne cena longa com batida curta para dar ritmo. Plante a crença dentro do fato, nunca como sermão. Feche a história e só então faça a oferta como próximo passo.

## Exemplos Faz/Não-faz

| Não-faz (ruim) | Faz (bom) |
|---|---|
| "A lição que aprendi foi que persistir é fundamentalmente importante." | "Eu quase parei. No dia seguinte, veio a primeira venda." |
| "Eu estava passando por um momento muito difícil na época." | "Eu olhei o saldo: R$ 12. E três contas vencendo." |
| "Esse método vai transformar completamente a sua vida também." | "Funcionou comigo. Hoje eu mostro o mesmo caminho a você." |
| "Naquele instante, magicamente, tudo se resolveu sozinho." | "Então mudei uma coisa. A virada começou ali." |
| "Sou prova viva de que é possível alcançar o sucesso." | "Eu saí do zero. Você pode sair do ponto onde está." |

## Notas de Compliance

A história precisa ser **verdadeira**. Nenhuma cena inventada, nenhum resultado fabricado (princípio `truthful_scarcity` e `evidence_before_opinion`). Todo número que aparece na narrativa aponta para o [proof-registry](../../data/registries/proof-registry.md). Resultado de aluno citado em cena precisa de autorização e de prova no [claim-registry](../../data/registries/claim-registry.md). Caso típico se marca como típico; caso excepcional se marca como exceção, nunca como regra. O [compliance-auditor](../../agents/compliance-auditor.md) veta promessa implícita na história sem lastro. A emoção convence, mas o fato é que protege.
