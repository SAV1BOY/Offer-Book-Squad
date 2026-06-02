---
id: voice.profile.brand-default-hormozi-style
title: "Perfil de Voz — Brand Default (Estilo Hormozi)"
type: voice
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
tags: [voz, perfil, default, hormozi, legibilidade, voz-ativa]
---

# Perfil de Voz — Brand Default (Estilo Hormozi)

Este é o perfil **padrão** do squad (`config.yaml → voice.default_profile`). Toda peça nasce aqui. Os outros perfis ([direct-response-aggressive](direct-response-aggressive.md), [premium-enterprise](premium-enterprise.md), [story-driven](story-driven.md), [friendly-creator](friendly-creator.md)) são desvios controlados deste centro. O [voice-style-guardian](../../agents/voice-style-guardian.md) mede toda copy contra esta régua. Ver também a [tone-matrix](../tone-matrix.md) e o [reading-level-guide](../reading-level-guide.md).

## Identidade

Quem fala é um operador direto. Ele já fez a coisa. Ele mostra o número, não a teoria. Ele fala como gente fala na mesa do bar, não como um manual. A voz é a de Alex Hormozi: clara, dura, sem ornamento. Ela respeita o tempo do leitor. Cada palavra trabalha ou sai. O leitor sente que alguém honesto explica algo simples. Não há firula, não há pose. Há prova e ação. Esta voz vende porque ela entrega antes de pedir. Ela ensina de graça e o leitor confia. O tom é de igual para igual, nunca de cima para baixo.

## Diais de Tom

Escala 1 (mínimo) a 5 (máximo).

| Dial | Nível | O que significa aqui |
|---|---|---|
| Formalidade | 2 | Fala de rua, simples. Trata por "você". Sem termo de gabinete. |
| Energia | 4 | Empurra com firmeza. Direto ao ponto, sem gritar. |
| Diretividade | 5 | Manda fazer. "Faça isto", não "talvez considere". |
| Calor | 3 | Respeita o leitor. Honesto, não bajulador. |
| Prova | 4 | Mostra número e exemplo. Concreto vence abstrato. |
| Urgência | 3 | Presente e ativo. Pressão só quando a escassez é real. |

## Léxico

**Usar:** você, agora, mostra, faz, prova, número, resultado, simples, claro, hoje, veja, ganhe, comece. Verbos de ação. Palavras curtas e comuns.

**Banir:** advérbios em `-mente` (rapidamente, basicamente, realmente), jargão de gabinete (sinergia, alavancar, paradigma), enchimento (na verdade, de certa forma, vale ressaltar), superlativo vazio (incrível, revolucionário, único de verdade). Ver a lista completa em [do-not-say](../do-not-say.md).

## Cadência & Sintaxe

Frases curtas. Uma vírgula no máximo por frase. Se há duas vírgulas, quebre em duas frases. Uma ideia por frase. Voz ativa sempre: o sujeito age. Tempo presente: "você vê", não "você verá". Alterne frase muito curta com frase média para dar ritmo. Comece parágrafos com a parte mais forte. Use número exato, não arredondado vago. Mostre, não diga. Termine seções com uma ordem clara de ação.

## Exemplos Faz/Não-faz

| Não-faz (ruim) | Faz (bom) |
|---|---|
| "Os resultados serão alcançados rapidamente pelos alunos." | "Você vê o resultado em dias." |
| "Essa é uma oportunidade verdadeiramente incrível e única." | "Você ganha 3 horas por dia." |
| "Não fique para trás dos seus concorrentes." | "Saia na frente hoje." |
| "De certa forma, basicamente, isso pode ajudar você." | "Isto resolve seu problema." |
| "Nós oferecemos uma solução que visa otimizar processos." | "Você corta o trabalho pela metade." |

## Notas de Compliance

A voz nunca cria claim sem lastro. Todo número aponta para prova no [proof-registry](../../data/registries/proof-registry.md). Escassez e urgência são 100% reais (princípio `truthful_scarcity`). Se um disclaimer legal não cabe em 3ª série, o disclaimer fica e o conflito sobe ao [offerbook-chief](../../agents/offerbook-chief.md). A lei vence o estilo. O [compliance-auditor](../../agents/compliance-auditor.md) checa o claim; o guardião checa a voz.
