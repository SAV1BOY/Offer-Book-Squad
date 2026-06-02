---
id: checklist.affiliate-program-checklist
title: "Checklist — Programa de Afiliados (prêmios alinhados, leaderboard, tracking)"
type: checklist
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
frameworks: [launch/affiliate-army, money-model-sequence]
registries: [decision-registry, offer-registry]
tags: [checklist, afiliados, premios, leaderboard, tracking, comissao, d6]
---

# Checklist — Programa de Afiliados

## Propósito
Este checklist prova que o programa de afiliados **paga o comportamento certo, mostra a disputa e rastreia cada venda**. Existe porque afiliado mal incentivado vende errado: um prêmio que premia volume bruto atrai lixo; um leaderboard invisível mata a competição; um tracking furado gera disputa de comissão e queima parceiro. Os prêmios precisam estar alinhados ao resultado que importa — venda líquida, não clique. A disputa precisa ser visível para puxar esforço. Cada venda precisa de atribuição rastreável. Sem este checklist verde, o programa atrai os afiliados errados e paga pelas razões erradas. Ele garante `decision_before_ornament`: cada regra do programa serve a uma venda real e rastreada, não a vaidade.

## Dono & Escopo
- **owner_agent:** `affiliate-program-architect` (desenha o programa e responde pelos incentivos); o [`launch-producer`](../agents/launch-producer.md) encaixa o programa nas fases e o [`compliance-auditor`](../agents/compliance-auditor.md) veta prêmio ou claim que afiliado não pode usar.
- **Artefato inspecionado:** o **programa de afiliados** (`templates/growth/affiliate-program-template`, `templates/growth/affiliate-prizes-template` e `templates/growth/affiliate-blackbook-template` preenchidos), registrado no [`decision-registry`](../data/registries/decision-registry.md).

## Condição de Passagem
Os prêmios premiam o resultado certo, o leaderboard é visível e justo, cada venda tem atribuição rastreável, e o material do afiliado respeita compliance.

## Itens
1. **Prêmios alinhados ao resultado.** Como verificar: a estrutura de prêmios premia venda líquida/qualidade, não clique nem volume bruto; o gatilho de cada prêmio está claro.
2. **Comissão coerente com unit economics.** Como verificar: a comissão cabe na margem do `offer-registry` e não quebra o LTV:CAC, conforme [`money-model-sequence`](../frameworks/money-model-sequence.md).
3. **Leaderboard visível.** Como verificar: existe um placar atualizado e regras de empate claras; a disputa é pública para os afiliados, conforme [`launch/affiliate-army`](../frameworks/launch/affiliate-army.md).
4. **Tracking por afiliado.** Como verificar: cada afiliado tem link/código único com atribuição rastreável até a venda; nenhuma venda fica sem origem.
5. **Janela de atribuição definida.** Como verificar: a regra de cookie/atribuição (primeiro ou último clique, prazo) está escrita e é a mesma para todos.
6. **Material pronto e em compliance.** Como verificar: swipes, e-mails e ads para afiliados existem e nenhum traz claim sem lastro; o `compliance-auditor` aprova o que o afiliado pode dizer.
7. **Regras de pagamento.** Como verificar: prazo de pagamento, estorno e clawback por reembolso estão definidos por escrito.
8. **Onboarding do afiliado.** Como verificar: há instruções de como entrar, pegar o link e usar o material — sem fricção para começar.

## Evidência Exigida
Para marcar ✅: linkar o programa no `decision-registry`, a tabela prêmio→gatilho→resultado (item 1), a comissão rastreada à margem do `offer-registry` (item 2), o leaderboard com regras (item 3) e o esquema de link/código único por afiliado (item 4). O kit de material com aprovação de compliance (item 6) e as regras de pagamento/clawback (item 7) ficam linkados.

## Protocolo de Falha
Item vermelho → o programa volta ao `affiliate-program-architect` com o defeito nomeado e **não é aberto a afiliados**. Prêmio que premia o comportamento errado é redesenhado. Comissão que estoura a margem reabre conversa com o `unit-economics-stack-analyst`. Material com claim sem lastro aciona veto do `compliance-auditor`. Re-entrada: corrigir as regras, atualizar o `decision-registry`, re-submeter. Mudança na oferta ou na margem reabre a estrutura de comissão.

## Links
- Frameworks: [`launch/affiliate-army`](../frameworks/launch/affiliate-army.md) · [`money-model-sequence`](../frameworks/money-model-sequence.md)
- Registries: [`decision-registry`](../data/registries/decision-registry.md) · [`offer-registry`](../data/registries/offer-registry.md)
- Agentes: [`affiliate-program-architect`](../agents/affiliate-program-architect.md) · [`launch-producer`](../agents/launch-producer.md) · [`compliance-auditor`](../agents/compliance-auditor.md)
- Checklists vizinhos: [`pr-plan-checklist`](pr-plan-checklist.md) · [`events-logistics-checklist`](events-logistics-checklist.md) · [`compliance-checklist`](compliance-checklist.md)
