---
id: checklist.positioning.positioning-lead-choice-gate
title: "Gate — Seleção de Lead Rigorosa e Justificada"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [lead-types, awareness-x-sophistication, positioning/moore-positioning-formula]
registries: [decision-registry]
tags: [gate, positioning, lead, escolha, tree-of-thoughts, d3]
---

# Gate — Seleção de Lead Rigorosa e Justificada

## Propósito
Este gate prova que o **lead travado venceu uma seleção real**, não que foi o primeiro palpite. Ele audita o segundo ponto de ramificação (Tree-of-Thoughts) do `positioning-lead-strategist`: gerar ≥3 leads plausíveis para a consciência dada, pontuá-los por fit de consciência, congruência com a Big Idea e nível de ceticismo do mercado, e podar os perdedores com motivo. Existe porque um lead "escolhido" sem alternativas consideradas costuma ser o lead favorito do redator, não o que converte aquele mercado. Enquanto o gate de awareness-fit prova que o vencedor **casa** com a consciência, este prova que o **processo** de escolha foi rigoroso: as alternativas existiram, foram pontuadas e os ramos podados têm justificativa. Materializa a disciplina de ToT do agente — sem comparação não há escolha defensável, só preferência. É o gate que impede que a abertura da copy nasça de viés em vez de análise, e garante que o estrategista possa explicar por que o Segredo venceu a Promessa naquele caso específico.

## Dono & Escopo
- **owner_agent:** `positioning-lead-strategist` (decisor vinculante; sua decisão de lead prevalece sobre os agentes de copy, mas ele registra a divergência).
- **Artefato inspecionado:** o **`artifact.positioning`** (`lead_type`, `lead_justificativa`, `ramos_podados`) e a decisão `lead-type-locked` no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
Pelo menos três leads candidatos foram gerados e pontuados por fit de consciência, congruência com a Big Idea e ceticismo do mercado, e os ramos podados estão registrados com motivo.

## Itens
1. **≥3 candidatos gerados.** Verificar: o registro mostra ao menos três leads plausíveis considerados para a consciência dada (não um único palpite).
2. **Critérios de pontuação aplicados.** Verificar: cada candidato foi pontuado por fit de consciência, congruência com a Big Idea e nível de ceticismo do mercado.
3. **Vencedor justificado.** Verificar: o `lead_justificativa` diz por que o lead vencedor superou os concorrentes diretos, não só por que é "bom".
4. **Ramos podados com motivo.** Verificar: `ramos_podados` lista os leads descartados, cada um com o motivo da poda (ex.: "Oferta direta podada — público frio").
5. **Congruência com a Big Idea.** Verificar: o lead vencedor carrega o gancho/vilão da Big Idea travada e não o contradiz.
6. **Ceticismo endereçado.** Verificar: a escolha considera o nível de ceticismo — mercado saturado/cético tende a Segredo/Prova, não a claims diretos sem lastro.
7. **Decisão registrada.** Verificar: `lead_type`, justificativa e ramos podados estão na decisão `lead-type-locked` do [`decision-registry`](../../data/registries/decision-registry.md).

## Evidência Exigida
Para marcar cada item ✅, linkar o `artifact.positioning` com a lista dos ≥3 candidatos, a pontuação por critério, e o campo `ramos_podados` com motivos. A decisão `lead-type-locked` no [`decision-registry`](../../data/registries/decision-registry.md) é a evidência-resumo; a tabela de pontuação (candidato × fit × congruência × ceticismo) demonstra que a escolha foi comparativa, não intuitiva.

## Protocolo de Falha
Item vermelho → a escolha não está rigorosa. Menos de três candidatos → o estrategista volta ao L-Module e gera o leque completo antes de travar. Vencedor sem justificativa comparativa → reescreve a justificativa contrastando com os concorrentes diretos. Ramos podados sem motivo → completa o registro de poda. Lead que contradiz a Big Idea → descarta e re-pontua dentro da congruência com a tese. O estrategista **não tem veto** sobre o pipeline; conflito com um agente de copy sobre o lead → a decisão do estrategista prevalece (é o mandato dele), mas a divergência é registrada no [`decision-registry`](../../data/registries/decision-registry.md). Re-entrada: refeita a seleção com candidatos e poda, o gate é re-submetido. O fit final do vencedor com a consciência é provado no [`positioning-awareness-fit`](positioning-awareness-fit.md).

## Links
- Frameworks: [`lead-types`](../../frameworks/lead-types.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) · [`moore-positioning-formula`](../../frameworks/positioning/moore-positioning-formula.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`big-idea-architect`](../../agents/big-idea-architect.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Template: [`positioning-template`](../../templates/strategy/positioning-template.md)
- Gates irmãos: [`positioning-awareness-fit`](positioning-awareness-fit.md) · [`positioning-category-gate`](positioning-category-gate.md) · [`positioning-differentiation-gate`](positioning-differentiation-gate.md) · [`positioning-descends-to-copy-gate`](positioning-descends-to-copy-gate.md)
