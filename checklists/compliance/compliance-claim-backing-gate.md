---
id: checklist.compliance.compliance-claim-backing-gate
title: "Gate — Lastro de Claim (★ VETO: nenhum claim sem prova)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [proof-to-claim-chain, scarcity-urgency-engine]
registries: [decision-registry, claim-registry]
tags: [gate, compliance, claim, lastro, prova, veto, d7]
---

# Gate — Lastro de Claim (★ VETO)

## Propósito
Este gate prova que **nenhum claim de qualquer peça vai ao ar sem uma prova catalogada**. É um dos cinco gates de **veto** do `compliance-auditor`, a última barreira do pipeline. Ele existe porque claim sem lastro destrói LTV, queima a marca e expõe a risco legal (CDC no Brasil, FTC nos EUA). Vale o princípio `evidence_before_opinion`: toda promessa de resultado, número, prazo ou comparação aponta para um `proof_id` real, via a cadeia [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md). Espelha, na barreira final, o que o `ads-claim-backing-gate` faz em D4. Aqui a sanção é absoluta: claim órfão, prova fraca ou promessa infalsificável **vetam** a peça. Não existe "aprovado com ressalvas" em claim. O veto só é levantado por override humano explícito do `offerbook-chief`, registrado no `decision-registry` — e nem isso vale para claim comprovadamente falso.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (audita o lastro de cada claim e **veta** o órfão; `config.yaml: agents` veto=true). Co-roda com o `offerbook-chief`, que arbitra overrides; o `proof-credibility-curator` fornece a prova faltante.
- **Artefato inspecionado:** **cada** claim do `offer-book`, `vsl-script`, `email-sms-sequences`, `mailers-inserts`, `ad-matrix`, `funnel-map`, `affiliate-program` e `pr-plan`, cruzado com o [`claim-registry`](../../data/registries/claim-registry.md) e o [`proof-registry`](../../data/registries/proof-registry.md). A cadeia claim→prova é a régua.

## Condição de Passagem
Cada claim de cada peça está ligado a uma prova catalogada e suficiente, sem nenhum claim órfão nem promessa de resultado infalsificável.

## Itens
1. **Claims extraídos.** Verificar: cada peça lista seus claims (promessa, número, prazo, comparação) no `claim-registry`.
2. **Cadeia claim→prova.** Verificar: cada `claim_id` tem um `proof_id` catalogado e suficiente (`proof-to-claim-chain`), sem órfão.
3. **Prova não-fraca.** Verificar: a prova sustenta o claim (caso real, dado, fonte), não um depoimento vago ou número sem origem.
4. **Promessa falsificável.** Verificar: nenhum claim promete resultado/prazo infalsificável ("ganhe X garantido") sem evidência.
5. **Resultado atípico com disclaimer.** Verificar: claims de resultado excepcional carregam disclaimer ("resultados variam; sem garantia de ganho").
6. **Comparação sustentada.** Verificar: todo "melhor/mais rápido que" tem base verificável.
7. **Veto do órfão.** Verificar: todo claim sem lastro está **vetado** e a peça não publica até a prova chegar.

## Evidência Exigida
Para marcar ✅: linkar a tabela claim→proof sem órfãos do `claim-registry`/`proof-registry` (itens 1–3), as reescritas de promessas infalsificáveis (item 4), os disclaimers de resultado atípico (item 5) e a lista de claims vetados com o flag ao curador (item 7). O veredito aponta para o `decision-registry`.

## Protocolo de Falha
Claim sem prova → **VETO** do claim e da peça que o contém; o `compliance-auditor` registra `{peça, linha, claim, prova_ausente}` no `decision-registry` e devolve ao autor via o `voice-pass`, acionando o [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) para o lastro. A peça **não vai ao blackbook** até o claim ter prova ou ser reescrito como afirmação verificável. **Override:** só o [`offerbook-chief`](../../agents/offerbook-chief.md) pode levantar o veto, com decisão explícita gravada no `decision-registry` — override sem registro não existe, e claim comprovadamente falso **não tem override**. Espelhado em D4 por [`ads/ads-claim-backing-gate`](../ads/ads-claim-backing-gate.md).

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md)
- Registries: [`claim-registry`](../../data/registries/claim-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Política: [`compliance-policy`](../../docs/compliance-policy.md)
- Agentes: [`compliance-auditor`](../../agents/compliance-auditor.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Espelho em D4: [`ads/ads-claim-backing-gate`](../ads/ads-claim-backing-gate.md)
- Gates irmãos: [`compliance-disclaimers-gate`](compliance-disclaimers-gate.md) · [`compliance-scarcity-truth-gate`](compliance-scarcity-truth-gate.md) · [`compliance-data-privacy-gate`](compliance-data-privacy-gate.md) · [`compliance-sector-rules-gate`](compliance-sector-rules-gate.md)
