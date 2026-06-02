---
id: checklist.compliance-checklist
title: "Checklist — Compliance (claims, T&Cs, disclaimers, LGPD/FTC/CDC, escassez real)"
type: checklist
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [proof-to-claim-chain, scarcity-urgency-engine]
registries: [claim-registry, proof-registry, decision-registry]
tags: [checklist, compliance, claims, tcs, disclaimers, lgpd, ftc, cdc, escassez, d7]
---

# Checklist — Compliance

## Propósito
Este checklist é a **última barreira** antes da entrega. Ele prova que cada claim tem lastro, que T&Cs e disclaimers existem, que LGPD/FTC/CDC estão respeitados e que toda escassez é real. Existe porque uma promessa sem prova, uma escassez falsa ou um dado coletado sem base legal não são só risco de conversão — são risco jurídico e de marca. O `compliance-auditor` pode **vetar** qualquer peça. Escassez falsa é veto automático (`truthful_scarcity`). Claim sem prova é veto automático (`evidence_before_opinion`). Sem este checklist verde, nada vai ao ar. Ele protege o cliente, a marca e a operação, e garante que persuasão nunca vira engano.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (autoridade de veto; última barreira do squad); o [`offerbook-chief`](../agents/offerbook-chief.md) co-assina a liberação e cada agente de copy corrige o que for reprovado.
- **Artefato inspecionado:** **todas as peças voltadas ao público** (copy, funil, ads, mailers, material de afiliado e PR) contra a [`docs/compliance-policy.md`](../docs/compliance-policy.md), o [`claim-registry`](../data/registries/claim-registry.md) e o [`proof-registry`](../data/registries/proof-registry.md); o veredito é gravado no [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
Nenhum claim está órfão, T&Cs e disclaimers exigidos estão presentes, LGPD/FTC/CDC estão atendidos e toda escassez/urgência aponta para um limite real.

## Itens
1. **Nenhum claim órfão.** Como verificar: todo `claim_id` usado em peça pública tem `proof_id` no `proof-registry`, conforme [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md); claim sem prova = veto.
2. **Escassez 100% verdadeira.** Como verificar: cada prazo, vaga ou estoque citado aponta para restrição real e rastreável, conforme [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md); escassez falsa = veto.
3. **T&Cs presentes.** Como verificar: termos da oferta (preço, cobrança, renovação, cancelamento) estão escritos e linkados onde a venda acontece.
4. **Disclaimers exigidos.** Como verificar: resultados típicos, isenção de garantia de ganho e avisos do setor estão presentes onde há promessa de resultado.
5. **LGPD/FTC atendidos.** Como verificar: coleta de dados tem base legal e consentimento; divulgação paga (afiliado/influência) é declarada, conforme a `compliance-policy`.
6. **CDC respeitado.** Como verificar: direito de arrependimento, informação clara e ausência de prática abusiva conforme o Código de Defesa do Consumidor.
7. **Garantia exequível.** Como verificar: a garantia prometida é cumprível e seus termos não contradizem os T&Cs.
8. **Privacidade e dados sensíveis.** Como verificar: depoimentos e dados de clientes têm autorização de uso; nada exposto sem consentimento.
9. **Linguagem sem engano.** Como verificar: nenhuma frase induz a erro sobre preço, resultado ou disponibilidade.

## Evidência Exigida
Para marcar ✅: linkar a tabela claim→proof sem órfãos (item 1), a prova de que cada elemento de escassez aponta para limite real (item 2), os blocos de T&Cs e disclaimers nas páginas de venda (itens 3–4) e a base legal de coleta com as divulgações pagas (item 5). As autorizações de uso de depoimento (item 8) ficam arquivadas. O veredito final é gravado no `decision-registry`.

## Protocolo de Falha
Item vermelho → **veto**: a peça não vai ao ar e volta ao agente dono com o defeito nomeado. Claim órfão e escassez falsa são vetos absolutos — só humano sênior reverte, com decisão e justificativa gravadas no `decision-registry`. Falta de T&Cs/disclaimer ou base legal volta para correção imediata. Re-entrada: corrigir a peça, atualizar `claim-registry`/`proof-registry`, re-submeter ao `compliance-auditor`. Nenhum prazo de lançamento justifica liberar peça reprovada.

## Links
- Política: [`docs/compliance-policy.md`](../docs/compliance-policy.md)
- Gates-espelho: [`compliance/compliance-claim-backing-gate`](compliance/compliance-claim-backing-gate.md) · [`compliance/compliance-scarcity-truth-gate`](compliance/compliance-scarcity-truth-gate.md) · [`compliance/compliance-data-privacy-gate`](compliance/compliance-data-privacy-gate.md)
- Frameworks: [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md) · [`scarcity-urgency-engine`](../frameworks/scarcity-urgency-engine.md)
- Registries: [`claim-registry`](../data/registries/claim-registry.md) · [`proof-registry`](../data/registries/proof-registry.md) · [`decision-registry`](../data/registries/decision-registry.md)
- Agentes: [`compliance-auditor`](../agents/compliance-auditor.md) · [`offerbook-chief`](../agents/offerbook-chief.md)
- Checklists vizinhos: [`guarantee-checklist`](guarantee-checklist.md) · [`offer-stack-checklist`](offer-stack-checklist.md) · [`final-delivery-checklist`](final-delivery-checklist.md)
