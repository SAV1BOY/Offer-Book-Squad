---
id: template.qa.voice-guide
title: "Voice Guide — O Guia de Voz do Lançamento (3ª Série, Ativa, Presente)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
consumes: [voice.voice-checklist, template.core.offer-book-master]
produces: [data.registry.control]
frameworks: [power-of-one]
checklists: [compliance-checklist]
registries: [control-registry]
tags: [template, voice-guide, voz, 3a-serie, voz-ativa, tempo-presente, qa]
---

# Voice Guide — O Guia de Voz do Lançamento

Este template produz o **guia de voz** de um lançamento: a régua que toda copy segue antes de ir ao ar. A voz padrão é simples e dura: nível de 3ª série, voz ativa, tempo presente, enquadramento positivo, zero advérbio floreado. O guia parte do perfil-régua [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md) e do [`voice-checklist`](../../voice/voice-checklist.md), e os ajusta ao contexto do lançamento. O guia julga **voz**, nunca o mérito do claim — a verdade do número é veto do [`compliance-auditor`](../../agents/compliance-auditor.md).

## Como usar
- **Agente dono:** [`voice-style-guardian`](../../agents/voice-style-guardian.md). Pareia com todos os autores de D4 (que escrevem dentro da régua) e com o [`compliance-auditor`](../../agents/compliance-auditor.md) (cuja barreira de claim é independente da voz).
- **Task:** preenchido no início do D4, antes da primeira peça de copy. Lido por todo autor de VSL, e-mail, SMS, mailer e anúncio.
- **Quando:** o guardião escreve o guia assim que o Offer Book está aprovado e a Big Idea única existe ([`power-of-one`](../../frameworks/power-of-one.md)). Ele escolhe o perfil de tom do contexto e fixa o léxico (usar/banir) deste lançamento.
- Use exemplos faz/não-faz reais. Use a régua dura de oito itens por frase. Guia vago não corrige copy — cada item é binário e testável.

## Campos & Instruções
- **{{NOME_DO_LANCAMENTO}}** — o lançamento a que este guia pertence.
- **{{PERFIL_DE_TOM}}** — o perfil de voz do contexto (um dos perfis em [`voice/profiles`](../../voice/profiles/brand-default-hormozi-style.md)).
- **{{BIG_IDEA}}** — a tese única que a voz serve, sempre na mesma linguagem.
- **{{LEXICO_USAR}}** — as palavras e expressões que esta marca usa.
- **{{LEXICO_BANIR}}** — as palavras proibidas, do [`do-not-say`](../../voice/do-not-say.md) mais as deste lançamento.
- **{{REGRA_DURA}}** — os oito itens por frase (frase curta, ≤1 vírgula, sem advérbio, voz ativa, presente, positivo, sem redundância, 3ª série).
- **{{EXEMPLOS}}** — pares faz/não-faz, cada não-faz com a marca e a correção que passa.
- **{{VEREDITO}}** — como o guardião decide: APROVADO ou REPROVADO, sem meio-termo.

## O Template
```
# GUIA DE VOZ — {{NOME_DO_LANCAMENTO}}
Owner: voice-style-guardian · Data: {{DATA}}
Perfil de tom: {{PERFIL_DE_TOM}} · Big Idea: {{BIG_IDEA}}

## 1. A REGRA DURA (oito itens por frase)
1. Frase curta — ≤ 18 palavras (alvo ≤ 12).
2. No máximo 1 vírgula.
3. Sem advérbio floreado (procure -mente).
4. Voz ativa — o sujeito age.
5. Tempo presente — sem futuro à toa.
6. Enquadramento positivo — diz o ganho e a ação.
7. Sem redundância — uma ideia por frase.
8. Nível 3ª série — palavra curta e comum.

## 2. LEXICO
Usar: {{LEXICO_USAR}}
Banir: {{LEXICO_BANIR}}

## 3. EXEMPLOS FAZ / NAO-FAZ
| Não-faz (reprovado) | Marca | Faz (aprovado) |
|---------------------|-------|----------------|
| {{NAO_FAZ_1}} | {{MARCA_1}} | {{FAZ_1}} |
| {{NAO_FAZ_2}} | {{MARCA_2}} | {{FAZ_2}} |

## 4. VEREDITO
APROVADO se toda frase passa nos oito itens. REPROVADO ao primeiro acúmulo de marcas.
Redline ao autor: {linha, violação, correção}. Máximo 3 rodadas, depois sobe ao offerbook-chief.
```

## Exemplo preenchido
> **# GUIA DE VOZ — Lançamento do Motor 72h**
> Owner: voice-style-guardian · Data: 2026-06-02
> Perfil de tom: direct-response-aggressive · Big Idea: *"A janela de 72 horas que devolve o lucro que seu checkout esconde."*
>
> **1. A REGRA DURA** — frase curta, ≤1 vírgula, sem advérbio, voz ativa, presente, positiva, sem enchimento, 3ª série.
> **2. LEXICO** — Usar: "lucro", "recupera", "em dias", "no pico", "deadline real". Banir: "otimizar", "sinergia", "basicamente", "na verdade", "rapidamente", "única chance".
> **3. EXEMPLOS FAZ / NAO-FAZ** —
> | Não-faz | Marca | Faz |
> |---|---|---|
> | "Os resultados serão alcançados rapidamente." | passiva + futuro + advérbio | "Você vê o resultado em dias." |
> | "Não perca essa chance realmente única." | negativo + advérbio + superlativo | "Garanta sua vaga hoje." |
>
> **4. VEREDITO** — APROVADO quando toda frase passa. Uma peça com passiva, advérbio e futuro volta com a redline `{linha, violação, correção}`.

## DoD do entregável
O guia está pronto quando: (1) os 4 blocos estão preenchidos, sem `{{PLACEHOLDER}}` solto; (2) a régua dura traz os oito itens, cada um binário e testável, espelhando o [`voice-checklist`](../../voice/voice-checklist.md); (3) o perfil de tom é um perfil real de [`voice/profiles`](../../voice/profiles/brand-default-hormozi-style.md) e a Big Idea é única (`power-of-one`); (4) o léxico tem listas de usar e banir, e a lista de banir inclui o [`do-not-say`](../../voice/do-not-say.md); (5) há ≥2 pares faz/não-faz, cada não-faz com a marca e a correção que passa; (6) o veredito é binário (APROVADO/REPROVADO), com o fluxo de redline e o teto de 3 rodadas antes de escalar ao [`offerbook-chief`](../../agents/offerbook-chief.md); (7) o guia deixa claro que julga **voz**, não claim — a verdade do número e da escassez é veto independente do [`compliance-auditor`](../../agents/compliance-auditor.md) ([política de compliance](../../docs/compliance-policy.md)). O veredito de cada peça fica registrado no [`control-registry`](../../data/registries/control-registry.md), ligado ao `asset_id`.
