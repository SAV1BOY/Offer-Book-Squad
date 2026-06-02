---
id: voice.voice-checklist
title: "Checklist de Aprovação de Voz"
type: voice
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
tags: [voz, checklist, aprovacao, veto, voz-ativa, sem-adverbios, legibilidade]
---

# Checklist de Aprovação de Voz

Este é o checklist que o [voice-style-guardian](../agents/voice-style-guardian.md) roda em **toda** peça de copy de D4 antes de liberar para o downstream. Ele espelha a régua dura do agente (§6) e os cinco gates que ele fiscaliza. O veredito é binário: **APROVADO** ou **REPROVADO**. Não existe "aprovado com ressalvas". Ou a peça está na voz, ou volta para o autor com a linha e a correção. Use junto com o [reading-level-guide](reading-level-guide.md), o [do-not-say](do-not-say.md) e a [tone-matrix](tone-matrix.md). O perfil-régua é o [brand-default-hormozi-style](profiles/brand-default-hormozi-style.md), ajustado pelo perfil do contexto.

## Condição de passagem

A peça passa quando **toda** frase obedece às oito regras de voz e a peça inteira passa nos cinco gates. Uma única violação dura marca a frase. Um acúmulo de marcas reprova a peça. O guardião lê a peça inteira, nunca uma amostra.

## A régua dura — oito itens por frase

Cada item é binário e testável. Marque cada frase.

| # | Item | Como verificar | Passa se |
|---|---|---|---|
| 1 | Frase curta | Conte as palavras | ≤ 18 palavras (alvo ≤ 12) |
| 2 | No máximo 1 vírgula | Conte as vírgulas | ≤ 1 vírgula na frase |
| 3 | Sem advérbio | Procure `-mente` e intensificador | Zero advérbio floreado |
| 4 | Voz ativa | Ache o sujeito que age | Sujeito age, sem passiva evitável |
| 5 | Tempo presente | Cheque o verbo | Presente, sem futuro desnecessário |
| 6 | Enquadramento positivo | Diz o ganho ou só o medo? | Diz o ganho e a ação |
| 7 | Sem redundância | Tem palavra repetida ou muleta? | Uma ideia por frase, zero enchimento |
| 8 | Nível 3ª série | "Uma criança entende?" | Palavra curta e comum |

## Os cinco gates da peça

Espelham os gates que o guardião fiscaliza. A peça precisa passar nos cinco.

| Gate | Pergunta | Falha se |
|---|---|---|
| `voice/voice-checklist` | Todas as frases passam na régua dura? | Acúmulo de marcas na peça |
| `voice/voice-reading-level-gate` | A peça inteira fica em 3ª série? | Trecho acima do nível-alvo |
| `voice/voice-active-present-gate` | Voz ativa e presente em toda parte? | Passiva evitável ou futuro à toa |
| `voice/voice-no-adverbs-gate` | Zero advérbio floreado? | Qualquer `-mente` ou intensificador vazio |
| `voice/voice-positive-framing-gate` | Diz o ganho, não só o medo? | Enquadramento negativo dispensável |

## O fluxo de aprovação

1. Receba a peça completa, com autor e origem declarados. Peça vinda truncada volta.
2. Carregue o perfil de voz do contexto e a [tone-matrix](tone-matrix.md).
3. Rode a régua dura frase a frase. Marque cada violação.
4. Rode os cinco gates sobre a peça inteira.
5. Se algum gate falha, o veredito é **REPROVADO**. Monte a redline: `{linha, violação, correção sugerida}`.
6. Se a intenção persuasiva corre risco, gere ≥3 reescritas e escolha a que preserva a força.
7. Devolva a redline ao autor. Re-audite o reenvio. Máximo de 3 rodadas antes de escalar ao [offerbook-chief](../agents/offerbook-chief.md).
8. Se todas as frases passam, o veredito é **APROVADO**. Libere para o downstream.
9. Registre o veredito no [control-registry](../data/registries/control-registry.md) ligado ao `asset_id`.

## Schema do veredito

```
PEÇA: <asset_id + tipo: vsl|email|sms|mailer|ad>
VEREDITO: APROVADO | REPROVADO
NÍVEL DE LEITURA: <medido> (alvo: 3ª série)
MARCAS (se reprovado):
  | Linha | Violação | Trecho original | Correção sugerida |
RESUMO: <nº de marcas por tipo>
OVERRIDE: <decision_id ou —>
PRÓXIMO PASSO: liberar p/ downstream | devolver ao autor (rodada N)
```

## Exemplos Faz/Não-faz

Cada par mostra a frase reprovada, a marca e a correção que passa.

| Não-faz (reprovado) | Marca | Faz (aprovado) |
|---|---|---|
| "Os resultados serão alcançados rapidamente." | passiva + futuro + advérbio | "Você vê o resultado em dias." |
| "Não perca essa chance realmente única." | negativo + advérbio + superlativo | "Garanta sua vaga hoje." |
| "Você provavelmente vai gostar disso." | hedge + futuro | "Você ganha 3 horas por dia." |
| "Na verdade, isso basicamente otimiza tudo, sem esforço." | enchimento + advérbio + 2 vírgulas | "Isto corta seu trabalho pela metade." |
| "As inscrições serão encerradas em breve." | passiva + urgência vaga | "As inscrições fecham amanhã." |

## Override e escalonamento

Só o [offerbook-chief](../agents/offerbook-chief.md) libera uma peça reprovada, com decisão **explícita e registrada** no [decision-registry](../data/registries/decision-registry.md). Override sem registro não existe. O caso típico é um termo técnico-legal que o [compliance-auditor](../agents/compliance-auditor.md) exige e que viola a 3ª série: a lei vence o estilo, mas a decisão fica gravada. Conflito guia × compliance sobe ao Chief. Impasse com um autor após 3 rodadas também sobe ao Chief, com o histórico de marcas.

## Notas de Compliance

O checklist julga **voz**, não mérito de claim. A verdade do número e da escassez é veto do [compliance-auditor](../agents/compliance-auditor.md). Todo número aprovado aponta ao [proof-registry](../data/registries/proof-registry.md); toda afirmação, ao [claim-registry](../data/registries/claim-registry.md). Voz limpa não autoriza claim sem lastro. As duas barreiras são independentes e ambas precisam passar.
