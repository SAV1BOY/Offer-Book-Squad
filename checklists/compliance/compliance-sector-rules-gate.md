---
id: checklist.compliance.compliance-sector-rules-gate
title: "Gate — Regras Setoriais (★ VETO: saúde, finanças, profissões, EUA/Brasil)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [proof-to-claim-chain, scarcity-urgency-engine]
registries: [decision-registry, claim-registry]
tags: [gate, compliance, setor, anvisa, cvm, ftc, cdc, veto, d7]
---

# Gate — Regras Setoriais (★ VETO)

## Propósito
Este gate prova que **a oferta respeita as regras do setor em que vende** — saúde, finanças, serviços profissionais — e os marcos legais do Brasil e dos EUA. É um dos cinco gates de **veto** do `compliance-auditor`. Ele existe porque cada setor tem linhas que não se cruzam: suplemento não alega cura (Anvisa), educação financeira não é recomendação de investimento (CVM), serviço profissional não garante resultado (OAB/CFM/CFC). Some-se a FTC nos EUA (endossos, "results not typical"), CAN-SPAM, TCPA, e o CDC no Brasil (a oferta vincula; a publicidade não pode enganar). Vale o princípio `evidence_before_opinion` aplicado ao enquadramento regulatório de cada claim. Uma violação setorial **veta** a peça até reenquadrar. O veto só cai por override registrado do `offerbook-chief` — e a lei setorial nunca é dispensada por um override.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (enquadra cada peça nas regras do setor e **veta** a violação; `config.yaml: agents` veto=true). O autor da peça reenquadra o claim; o `offerbook-chief` arbitra override sem dispensar a regra.
- **Artefato inspecionado:** os claims setoriais do `offer-book`, `vsl-script`, `email-sms-sequences`, `mailers-inserts`, `ad-matrix`, `affiliate-program` e `pr-plan`, sob a política [`compliance-policy`](../../docs/compliance-policy.md) (seção 7) e a cadeia [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md).

## Condição de Passagem
Cada peça respeita as regras do seu setor (saúde, finanças, profissões) e os marcos de Brasil (CDC, Anvisa, CVM) e EUA (FTC, CAN-SPAM, TCPA), sem alegação proibida.

## Itens
1. **Saúde sem cura.** Verificar: peças de saúde/suplemento não alegam doença/cura (Anvisa) e trazem o disclaimer de saúde.
2. **Finanças sem recomendação.** Verificar: peças financeiras separam educação de recomendação de investimento (CVM).
3. **Profissões sem garantia.** Verificar: serviços jurídicos/médicos/contábeis não garantem resultado (OAB/CFM/CFC).
4. **FTC nos endossos.** Verificar: endossos e depoimentos seguem a FTC ("results not typical"), sem promessa atípica como regra.
5. **CDC: oferta vincula.** Verificar: o que a publicidade promete a oferta entrega; nada de propaganda enganosa (CDC).
6. **CAN-SPAM/TCPA.** Verificar: e-mail e SMS para o público dos EUA seguem CAN-SPAM e TCPA (consentimento, horário).
7. **Setor identificado.** Verificar: o setor da oferta está declarado e o conjunto de regras aplicável foi checado, não presumido.

## Evidência Exigida
Para marcar ✅: linkar o enquadramento de cada claim setorial à regra aplicável (itens 1–3), a conformidade dos endossos com a FTC (item 4), a aderência ao CDC (item 5) e a checagem de CAN-SPAM/TCPA quando há público nos EUA (item 6). O setor declarado e o veredito apontam para o `decision-registry`.

## Protocolo de Falha
Violação setorial → **VETO** da peça; o `compliance-auditor` registra a regra violada no `decision-registry` e devolve ao autor para **reenquadrar** o claim (ex.: "cura a ansiedade" → "apoia o bem-estar", com disclaimer). A peça **não vai ao blackbook** até ficar conforme. **Override:** só o [`offerbook-chief`](../../agents/offerbook-chief.md) arbitra um caso de fronteira, com decisão explícita gravada no `decision-registry` — a regra setorial nunca é dispensada por override. O lastro de prova por trás do claim é tratado no [`compliance-claim-backing-gate`](compliance-claim-backing-gate.md); os disclaimers no [`compliance-disclaimers-gate`](compliance-disclaimers-gate.md). Re-entrada: reenquadrar o claim, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) · [`scarcity-urgency-engine`](../../frameworks/scarcity-urgency-engine.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`claim-registry`](../../data/registries/claim-registry.md)
- Política: [`compliance-policy`](../../docs/compliance-policy.md)
- Agentes: [`compliance-auditor`](../../agents/compliance-auditor.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gates irmãos: [`compliance-claim-backing-gate`](compliance-claim-backing-gate.md) · [`compliance-disclaimers-gate`](compliance-disclaimers-gate.md) · [`compliance-scarcity-truth-gate`](compliance-scarcity-truth-gate.md) · [`compliance-data-privacy-gate`](compliance-data-privacy-gate.md)
