---
id: checklist.proof.proof-permission-gate
title: "Gate — Toda Prova Tem Consentimento e Direito de Uso (Proveniência Resolvida)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
frameworks: [proof-to-claim-chain]
registries: [proof-registry]
tags: [gate, proof, consentimento, proveniencia, lgpd, d1, direito-de-uso]
---

# Gate — Toda Prova Tem Consentimento e Direito de Uso

## Propósito
Este gate prova que **toda prova usável tem proveniência resolvida** — consentimento de quem a deu, fonte rastreável e direito de uso — antes de chegar à copy. Ele existe porque uma prova tecnicamente forte mas sem autorização é **não usável**: um depoimento sem consentimento, um caso de cliente citado sem liberação ou um dado privado sem base legal viram veto do `compliance-auditor` (privacidade) ou risco jurídico. O curador marca essas provas como `consent_status: pending` e as mantém fora de uso até a proveniência ser liberada. Diferente do `proof-source-credibility-gate` (que olha se a prova é epistemicamente forte), este olha se a prova é **legítima de usar**: temos o direito? A pessoa autorizou? O dado respeita a LGPD? Ele se alinha diretamente com o [`compliance-data-privacy-gate`](../compliance/compliance-data-privacy-gate.md). É o gate que impede o squad de construir copy sobre uma prova que precisará ser retirada — depois de impressa, publicada ou enviada.

## Dono & Escopo
- **owner_agent:** `proof-credibility-curator` (verifica consentimento e direito de uso; sem veto, sinaliza ao compliance).
- **Artefato inspecionado:** o `consent_status` e a proveniência de cada prova no [`proof-registry`](../../data/registries/proof-registry.md), cruzados com os ativos de autorização.

## Condição de Passagem
Cada prova em uso tem consentimento granted, fonte rastreável e direito de uso confirmado, e nenhuma prova pending/revoked está na matriz como usável.

## Itens
1. **Consentimento explícito.** Verificar: cada prova tem `consent_status` (granted, não pending/revoked); só prova `granted` entra como usável na matriz.
2. **Autorização rastreável.** Verificar: depoimentos e estudos de caso têm o ativo de autorização (termo assinado, e-mail de liberação) linkado.
3. **Fonte do dado documentada.** Verificar: dados e estatísticas têm origem rastreável (de onde vieram, quem coletou) — sem dado anônimo sem fonte.
4. **Base legal de privacidade.** Verificar: dados pessoais respeitam a LGPD (base legal para uso, anonimização quando exigida), alinhado ao [`compliance-data-privacy-gate`](../compliance/compliance-data-privacy-gate.md).
5. **Direito de uso da mídia.** Verificar: prints, logos, menções de mídia e endossos têm direito de uso (licença, fair use atribuído, autorização da marca citada).
6. **Pending fora de uso.** Verificar: toda prova `pending` ou `revoked` está **fora** da matriz de munição e marcada como bloqueada até liberar.
7. **Sinais de consentimento ao compliance.** Verificar: as provas pendentes que valem a pena liberar estão sinalizadas ao [`compliance-auditor`](../../agents/compliance-auditor.md) com a ação necessária.

## Evidência Exigida
Para marcar cada item ✅, linkar o [`proof-registry`](../../data/registries/proof-registry.md) com `consent_status` por prova e o `asset_link` da autorização, a origem documentada de cada dado, e a confirmação de base legal LGPD para dados pessoais. A lista de provas `pending/revoked` mantidas fora de uso (com a ação de liberação) é a evidência-resumo de que nada sem direito entrou na copy.

## Protocolo de Falha
Item vermelho → não declara verde. Prova sem consentimento → `consent_status: pending`, fora de uso até liberar; sinaliza a ação ao [`compliance-auditor`](../../agents/compliance-auditor.md). Caso de cliente citado sem liberação → marca não usável e busca autorização. Dado pessoal sem base legal → bloqueia até anonimizar ou obter base (LGPD). Mídia sem direito de uso → remove ou obtém licença. Prova `pending` que vazou para a matriz → retira da munição e marca bloqueada. O curador **não tem veto**: a barreira de privacidade é do compliance; ele sinaliza o gap e a recomendação. Re-entrada: resolvida a proveniência (consentimento granted, base legal, licença), a prova volta à matriz e o gate é re-submetido.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)
- Registries: [`proof-registry`](../../data/registries/proof-registry.md)
- Agentes: [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Alinhamento com compliance: [`compliance-data-privacy-gate`](../compliance/compliance-data-privacy-gate.md) · [`compliance-claim-backing-gate`](../compliance/compliance-claim-backing-gate.md)
- Gates irmãos: [`proof-claim-backing-gate`](proof-claim-backing-gate.md) · [`proof-coverage-gate`](proof-coverage-gate.md) · [`proof-objection-coverage-gate`](proof-objection-coverage-gate.md) · [`proof-source-credibility-gate`](proof-source-credibility-gate.md)
