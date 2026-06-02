---
id: voice.profile.friendly-creator
title: "Perfil de Voz — Friendly Creator (Criador & Comunidade)"
type: voice
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
tags: [voz, perfil, criador, comunidade, proximo, leve]
---

# Perfil de Voz — Friendly Creator (Criador & Comunidade)

Perfil de **criador e comunidade**: próximo, leve, de pessoa para pessoa. Use em e-mail de nutrição, post de comunidade, legenda de conteúdo e oferta para audiência que já segue o criador. É um desvio do [brand-default-hormozi-style](brand-default-hormozi-style.md): mantém a clareza dura, mas baixa a pressão e sobe o calor. A relação já existe, então a voz fala como quem conversa com gente conhecida. Veja o ajuste de calor e urgência na [tone-matrix](../tone-matrix.md). O [voice-style-guardian](../../agents/voice-style-guardian.md) segue vetando advérbio, voz passiva e frase longa, mesmo no tom leve.

## Identidade

Quem fala é o criador que conhece a própria audiência pelo nome. Ele é gente como a gente. Ele compartilha o que aprendeu sem se passar por guru. A voz é leve, calorosa e direta, como uma mensagem para um amigo que pediu ajuda. Ele celebra a vitória pequena do seguidor e admite o próprio tropeço. Ele convida, não empurra. A oferta soa como uma dica boa entre amigos, não como um pitch. O leitor sente pertencimento: faz parte de algo, não é só um alvo de venda. A confiança já existe, então a voz protege essa relação acima da conversão de hoje.

## Diais de Tom

Escala 1 (mínimo) a 5 (máximo).

| Dial | Nível | O que significa aqui |
|---|---|---|
| Formalidade | 1 | Papo de amigo. Trata por "você", tom de mensagem direta. |
| Energia | 3 | Animada e leve. Empolga sem gritar. |
| Diretividade | 3 | Convida e sugere: "Dá uma olhada", "Bora juntos". |
| Calor | 5 | Próximo e generoso. Celebra o seguidor, admite o erro. |
| Prova | 3 | Prova leve: print de aluno, bastidor, resultado real e simples. |
| Urgência | 2 | Convite, não pressão. Prazo só quando real e dito com leveza. |

## Léxico

**Usar:** oi, bora, a gente, olha só, te conto, dica, juntos, comunidade, real, gostei, partiu, você consegue. Verbos de ação leves. Gíria leve que a audiência usa de verdade.

**Banir:** advérbios em `-mente`, tom corporativo ("prezado", "venha a usufruir"), pressão de vendedor agressivo ("última chance, corra"), falsa intimidade que a relação não comporta. Sem hype vazio. Ver [do-not-say](../do-not-say.md).

## Cadência & Sintaxe

Frases curtas e soltas. Uma vírgula no máximo. Tom de conversa: pode abrir com "Oi" ou uma pergunta direta. Voz ativa, presente. Use a gíria real da comunidade, mas com moderação para não datar. Misture frase curta com pergunta para puxar resposta. Mostre o bastidor concreto, não a teoria. Celebre a vitória do seguidor antes de pedir algo. Feche com um convite leve, nunca com uma ordem dura.

## Exemplos Faz/Não-faz

| Não-faz (ruim) | Faz (bom) |
|---|---|
| "Prezado seguidor, venho por meio desta apresentar minha oferta." | "Oi! Te conto uma coisa que vai te ajudar hoje." |
| "Essa é absolutamente sua última e derradeira chance de agir." | "As vagas fecham sexta. Se fizer sentido pra você, bora." |
| "Adquira agora este produto verdadeiramente transformador." | "Montei isso pra comunidade. Olha só se serve pra você." |
| "Eu sou uma autoridade incontestável e infalível no assunto." | "Eu também travei nisso. Compartilho o que funcionou comigo." |
| "Não desperdice essa oportunidade extraordinária e exclusiva." | "Quem entrou semana passada já mandou o primeiro resultado." |

## Notas de Compliance

O calor nunca vira manipulação da relação. O criador não usa a confiança da comunidade para empurrar claim sem lastro (princípio `evidence_before_opinion`). Print de seguidor precisa de autorização e de prova no [proof-registry](../../data/registries/proof-registry.md). Resultado mostrado é real e típico, marcado quando for exceção (`claim-registry`). Prazo dito "com leveza" ainda precisa ser **real** (`truthful_scarcity`): se a vaga não fecha sexta, não diga que fecha. O [compliance-auditor](../../agents/compliance-auditor.md) veta promessa implícita ao público fiel. Proteger a comunidade vale mais que a venda de hoje.
