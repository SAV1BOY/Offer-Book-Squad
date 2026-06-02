---
id: checklist.proof.proof-source-credibility-gate
title: "Gate — Força da Prova Classificada por Especificidade e Verificabilidade"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
frameworks: [proof-to-claim-chain]
registries: [proof-registry]
tags: [gate, proof, credibilidade, fonte, verificabilidade, d1, autoridade]
---

# Gate — Força da Prova Classificada por Especificidade e Verificabilidade

## Propósito
Este gate prova que **a força de cada prova foi classificada honestamente** — por especificidade (número, nome, data, contexto) somada à verificabilidade (há fonte checável, print, autoridade legítima?) — e não inflada para parecer mais forte do que é. Ele existe porque a regra de ouro do `proof-credibility-curator` é que **prova específica e verificável vence prova emocional e vaga**, e porque um "depoimento" sem fonte ou um dado infalsificável é exatamente o que o `compliance-auditor` derruba. Encarnando Cialdini (prova social e autoridade como gatilhos **legítimos**), ele garante que a nota `strong` só é dada a prova que resiste ao escrutínio, que a autoridade citada é real, e que prova fraca entra como reforço, nunca como munição principal. Diferente do `proof-permission-gate` (que olha consentimento e direito de uso), este olha a **qualidade epistêmica** da prova: ela prova mesmo o que diz provar? É o gate que separa credibilidade de teatro.

## Dono & Escopo
- **owner_agent:** `proof-credibility-curator` (classifica força por especificidade + verificabilidade; sem veto, sinaliza).
- **Artefato inspecionado:** a **classificação de força** de cada prova (`weak/moderate/strong`) e seus atributos de verificabilidade no [`proof-registry`](../../data/registries/proof-registry.md).

## Condição de Passagem
Cada prova tem força classificada por especificidade + verificabilidade, nenhuma prova vaga ou infalsificável está marcada strong, e toda autoridade citada é legítima e checável.

## Itens
1. **Força por critério explícito.** Verificar: cada prova tem `strength` derivada de especificidade (número/nome/data/contexto) + verificabilidade (fonte checável) — não por impressão.
2. **Nenhuma prova vaga marcada strong.** Verificar: depoimento genérico ("adorei o curso") está `weak`; só prova específica e checável recebe `strong`.
3. **Nada infalsificável como forte.** Verificar: número sem base, claim impossível de checar ou resultado infalsificável não recebe nota alta — busca-se o contra antes de declarar `strong`.
4. **Verificabilidade marcada.** Verificar: `verifiable: true/false` está preenchido; provas `strong` têm `verifiable: true` com o link do ativo (print, estudo, fonte).
5. **Autoridade legítima.** Verificar: credenciais e endossos citados são reais e relevantes ao claim (autoridade no domínio certo), não autoridade emprestada de outro campo.
6. **Prova fraca como reforço, não munição.** Verificar: provas `weak/moderate` aparecem como reforço; a munição principal de cada objeção/claim é a mais forte e segura disponível.
7. **Especificidade documentada.** Verificar: cada prova `strong` registra os elementos de especificidade (qual número, qual data, qual fonte) no [`proof-registry`](../../data/registries/proof-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar o [`proof-registry`](../../data/registries/proof-registry.md) com a coluna `strength` e os atributos `verifiable`, `source_name`, `asset_link` por prova, e a justificativa de força (quais elementos de especificidade + verificabilidade sustentam a nota). A rubrica de classificação aplicada (especificidade ×2, verificabilidade ×3, risco de compliance invertido ×2) é a evidência-resumo de que a nota não foi inflada.

## Protocolo de Falha
Item vermelho → não declara verde. Prova inflada (vaga marcada `strong`) → **rebaixa a força** exigindo especificidade + verificabilidade; não maquia o fraco como forte. Número sem base → marca não usável até a metodologia ser documentada. Autoridade emprestada (especialista de outro campo) → rebaixa ou descarta como prova de autoridade. Prova `strong` sem `asset_link`/`verifiable` → exige o ativo checável antes de manter a nota. Munição principal fraca → busca prova mais forte ou abre gap. O curador **não tem veto**: provas que o compliance derrubaria são sinalizadas ao [`compliance-auditor`](../../agents/compliance-auditor.md) e ao [`offerbook-chief`](../../agents/offerbook-chief.md). Re-entrada: reclassificada honestamente a prova, o gate é re-submetido.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`proof-registry`](../../data/registries/proof-registry.md)
- Agentes: [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Alinhamento com compliance: [`compliance-claim-backing-gate`](../compliance/compliance-claim-backing-gate.md)
- Gates irmãos: [`proof-claim-backing-gate`](proof-claim-backing-gate.md) · [`proof-coverage-gate`](proof-coverage-gate.md) · [`proof-objection-coverage-gate`](proof-objection-coverage-gate.md) · [`proof-permission-gate`](proof-permission-gate.md)
