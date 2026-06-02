---
id: checklist.mechanism.mechanism-proof-gate
title: "Gate — Cada Elo da Cadeia Causal com Lastro de Prova (sem alegação infalsificável)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
frameworks: [unique-mechanism, value-equation]
registries: [offer-registry]
tags: [gate, mechanism, prova, lastro, d2, credibilidade, proof-registry]
---

# Gate — Cada Elo da Cadeia Causal com Lastro

## Propósito
Este gate prova que cada elo da cadeia causal do mecanismo tem **lastro de prova**, em vez de uma alegação que ninguém pode verificar. Existe porque novidade sem prova é clickbait: um mecanismo que pontua alto em originalidade mas zero em credibilidade destrói confiança e arma o veto do `compliance-auditor` (alegação fisiológica sem fonte, promessa implícita de cura). O `value-equation-engineer` só ancora o valor num mecanismo **provado**, não provisório. Este gate fecha a tríade do mecanismo (causa, nome, prova): ele garante que a cadeia que reposiciona a culpa do avatar se sustenta em estudo, dado ou casos rastreáveis. Só depois do lastro verde o mecanismo muda de `provisório` para `provado` no registry.

## Dono & Escopo
- **owner_agent:** `mechanism-architect` (cruza a cadeia causal com o [`proof-registry`](../../data/registries/proof-registry.md)).
- **Artefato inspecionado:** os **elos provados** do `mechanism-sheet` e o campo `status: provisorio|provado` no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
Cada elo da cadeia causal aponta para prova rastreável no proof-registry, sem alegação infalsificável, e o mecanismo está marcado como provado.

## Itens
1. **Cada elo com prova.** Verificar: cada passo da cadeia causal (do `mechanism-root-cause-gate`) tem ≥1 `proof_id` correspondente no [`proof-registry`](../../data/registries/proof-registry.md).
2. **Prova rastreável.** Verificar: cada prova tem fonte verificável (estudo, dado próprio, casos), não afirmação genérica.
3. **Sem alegação infalsificável.** Verificar: nenhum elo se apoia numa alegação que nada poderia refutar.
4. **Alegação fisiológica com fonte.** Verificar: qualquer afirmação fisiológica/científica cita fonte primária — sem ela, o `compliance-auditor` veta.
5. **Sem promessa de cura implícita.** Verificar: a cadeia não embute promessa de cura ou resultado garantido que viole compliance.
6. **Força da prova declarada.** Verificar: cada prova tem o `strength` indicado (o `proof-credibility-curator` classifica), e elos críticos não dependem só de prova fraca.
7. **Status atualizado.** Verificar: o mecanismo só é `provado` no registry depois que todos os elos têm lastro; senão permanece `provisório` com a lacuna nomeada.

## Evidência Exigida
Para marcar cada item ✅, linkar cada elo da cadeia ao seu `proof_id` no [`proof-registry`](../../data/registries/proof-registry.md) e a linha do [`offer-registry`](../../data/registries/offer-registry.md) com `status: provado` e `prova_refs[]`. Alegações fisiológicas precisam linkar fonte primária. A classificação de força vem do [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). O permalink de cada prova conta como evidência; elos sem `proof_id` mantêm o mecanismo `provisório`.

## Protocolo de Falha
Item vermelho → o `mechanism-architect` **não marca o mecanismo como provado**; rebaixa a `provisório` e aciona o `proof-credibility-curator` pelo elo faltante. Alegação infalsificável → reescreve o elo para algo verificável. Alegação fisiológica sem fonte → busca a fonte ou remove o elo. Prova fraca em elo crítico → flag ao `proof-credibility-curator` e ao chief. Re-entrada: lastreados todos os elos, o gate é re-submetido e o `value-equation-engineer` pode ancorar o valor com segurança. O agente não tem veto; suas flags informam o veto do `compliance-auditor`.

## Links
- Frameworks: [`unique-mechanism`](../../frameworks/unique-mechanism.md) · [`value-equation`](../../frameworks/value-equation.md) · [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`proof-registry`](../../data/registries/proof-registry.md) · [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`mechanism-architect`](../../agents/mechanism-architect.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gate anterior (nome): [`mechanism-naming-gate`](mechanism-naming-gate.md) · Gate seguinte (frase): [`mechanism-one-sentence-gate`](mechanism-one-sentence-gate.md)
- Habilita o valor a jusante: [`value-likelihood-gate`](../value/value-likelihood-gate.md)
