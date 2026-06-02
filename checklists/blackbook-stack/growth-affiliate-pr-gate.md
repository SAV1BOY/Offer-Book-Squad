---
id: checklist.blackbook-stack.growth-affiliate-pr-gate
title: "Gate — Growth, Afiliados & PR (afiliados + PR prontos)"
type: gate
layer: D7
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
frameworks: [affiliate-army, pr-brand-maximization, money-model-sequence]
registries: [decision-registry, control-registry]
tags: [gate, growth, affiliate, pr, brand, d6, d7, dod-input]
---

# Gate — Growth, Afiliados & PR

## Propósito
Este gate prova que **o programa de afiliados e o plano de PR estão prontos para amplificar o lançamento**. Existe porque a aquisição não pode depender só de tráfego pago: afiliados e imprensa multiplicam alcance, mas só funcionam se tiverem materiais, regras de comissão, swipe e um cronograma de mídia prontos antes da abertura. É o quarto insumo do [`blackbook-dod-gate`](blackbook-dod-gate.md): growth garante que a oferta forte chegue a mais gente sem improviso de última hora.

## Dono & Escopo
- **owner_agent:** `compliance-auditor` (audita prontidão e conformidade dos termos); produzido em D6 por `affiliate-program-architect` e `pr-brand-strategist`.
- **Artefato inspecionado:** o programa de afiliados (regras, prêmios, blackbook do afiliado) e o plano de PR, gravados no [`decision-registry`](../../data/registries/decision-registry.md) e ligados aos ativos do [`control-registry`](../../data/registries/control-registry.md).

## Condição de Passagem
O programa de afiliados tem regras de comissão, materiais e cronograma prontos, e o plano de PR tem ângulos, alvos e calendário definidos — ambos alinhados à Big Idea e à escada do money model.

## Itens
1. **Estrutura de comissão definida.** Verificar: percentuais/valores por degrau e janela de atribuição (cookie) gravados, com termos claros.
2. **Blackbook do afiliado pronto.** Verificar: swipe de emails/anúncios, datas e links existem para o afiliado usar sem reescrever.
3. **Prêmios/leaderboard (se aplicável).** Verificar: estrutura de prêmios e regras de premiação definidas ou marcadas `não-aplicável`.
4. **Recrutamento de afiliados.** Verificar: lista-alvo de afiliados e sequência de convite prontas.
5. **Ângulos de PR.** Verificar: a narrativa de imprensa nasce da Big Idea travada, sem claim sem lastro.
6. **Alvos de mídia.** Verificar: lista de veículos/jornalistas/podcasts com contato e ângulo por alvo.
7. **Calendário de PR.** Verificar: datas de pitch e publicação alinhadas às fases do run-of-show.
8. **Conformidade dos materiais.** Verificar: copy de afiliado e PR passam pelas mesmas regras de claim e escassez verdadeira.

## Evidência Exigida
Para marcar ✅: linkar a estrutura de comissão e termos (itens 1, 3–4), o blackbook do afiliado no `control-registry` (item 2), o plano de PR com ângulos/alvos/datas (itens 5–7) e o registro de revisão de conformidade dos materiais (item 8).

## Protocolo de Falha
Item vermelho → o `compliance-auditor` devolve a `affiliate-program-architect` (afiliados) ou `pr-brand-strategist` (PR) com a lacuna nomeada e **não libera o blackbook-dod-gate**. Claim de afiliado/PR sem lastro ou ângulo que contradiz a Big Idea reprova. Re-entrada: corrigir os termos/materiais, realinhar à Big Idea, atualizar o `decision-registry` e re-submeter.

## Links
- Frameworks: [`affiliate-army`](../../frameworks/launch/affiliate-army.md) · [`pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md) · [`money-model-sequence`](../../frameworks/money-model-sequence.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md) · [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`affiliate-program-architect`](../../agents/affiliate-program-architect.md) · [`pr-brand-strategist`](../../agents/pr-brand-strategist.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Agrega para: [`blackbook-dod-gate`](blackbook-dod-gate.md)
