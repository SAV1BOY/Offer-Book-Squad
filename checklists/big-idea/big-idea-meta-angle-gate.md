---
id: checklist.big-idea.big-idea-meta-angle-gate
title: "Gate — Meta-Ângulo & Congruência (o lançamento demonstra a própria tese)"
type: gate
layer: D3
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [meta-launch-principle, power-of-one, big-idea-architect/big-idea-ideation-tot]
registries: [big-idea-registry, decision-registry]
tags: [gate, big-idea, meta-launch, congruencia, angulos-podados, d3]
---

# Gate — Meta-Ângulo & Congruência

## Propósito
Este gate prova duas coisas que protegem a Big Idea depois de travada. Primeiro, a **congruência meta-lançamento**: o próprio lançamento deve **demonstrar a tese que vende** — se a ideia promete um método, o lançamento usa esse método; um lançamento que contradiz a própria promessa mina a credibilidade antes da venda. Segundo, a **disciplina dos ângulos podados**: as candidatas que perderam na poda não somem nem voltam como teses concorrentes — viram `pruned` no registry e abastecem os ângulos de anúncio que o [`ad-creative-factory`](../../agents/ad-creative-factory.md) testa **sobre a UMA Big Idea**. Assim o Power of One sobrevive ao contato com a copy: uma tese central, muitos ângulos de entrada. O gate garante que a memória da poda existe (para não re-litigar a decisão) e que cada ângulo derivado é fiel à tese travada, não um desvio para outra ideia.

## Dono & Escopo
- **owner_agent:** `big-idea-architect` (guarda a congruência e a proveniência dos ângulos; serve a tese e os ramos podados aos agentes de copy).
- **Artefato inspecionado:** o campo `meta_congruencia` da Big Idea `locked`, os registros `pruned` com `motivo_poda` e `ramo` no [`big-idea-registry`](../../data/registries/big-idea-registry.md), e a decisão de derivação de ângulos no [`decision-registry`](../../data/registries/decision-registry.md).

## Condição de Passagem
O lançamento demonstra a própria tese (congruência meta-lançamento confirmada) e todos os ângulos derivados rastreiam aos ramos podados, fiéis à UMA Big Idea travada.

## Itens
1. **Congruência meta-lançamento.** Verificar: o mecanismo/método da Big Idea é demonstrado pelo próprio formato do lançamento (via [`meta-launch-principle`](../../frameworks/meta-launch-principle.md)).
2. **Sem autocontradição.** Verificar: o lançamento não viola a promessa que vende (ex.: prometer "sem esforço" e exigir um processo penoso para comprar).
3. **Ramos podados preservados.** Verificar: as candidatas perdedoras estão `pruned` no `big-idea-registry`, cada uma com `ramo` e `motivo_poda`.
4. **Ângulos derivam dos ramos.** Verificar: os ângulos de anúncio nascem dos ramos podados, não de novas teses inventadas a jusante.
5. **Fidelidade à tese travada.** Verificar: cada ângulo derivado serve a mesma promessa/gancho/vilão da `locked` — nenhum vira tese concorrente.
6. **Memória da poda registrada.** Verificar: a decisão de poda e a derivação de ângulos estão no `decision-registry`, evitando re-litígio.
7. **Handoff de ângulos pronto.** Verificar: a tese e os ramos podados estão disponíveis ao `ad-creative-factory` (e demais agentes de copy) com proveniência clara.

## Evidência Exigida
Para marcar ✅: linkar o campo `meta_congruencia` que mostra o lançamento demonstrando a tese (itens 1–2), os registros `pruned` com ramo e motivo no `big-idea-registry` (item 3), o mapa ângulo→ramo de origem (itens 4–5) e a decisão de derivação no `decision-registry` com o handoff de ângulos (itens 6–7).

## Protocolo de Falha
Item vermelho → o `big-idea-architect` corrige a incongruência (alinha o formato do lançamento à tese) ou recupera os ramos podados do `big-idea-registry`. Ângulo que virou tese concorrente é rebaixado a variação da UMA Big Idea — ou eliminado. Pressão por duas teses "para testar" → o agente explica que ângulos de teste são variações sobre a tese travada, geradas pelo [`ad-creative-factory`](../../agents/ad-creative-factory.md). Re-entrada: atualiza `meta_congruencia` e a proveniência dos ângulos e re-submete. Mudança da tese travada reabre este gate e o [`big-idea-single-gate`](big-idea-single-gate.md).

## Links
- Gates irmãos: [`big-idea-single-gate`](big-idea-single-gate.md) · [`big-idea-new-big-credible-gate`](big-idea-new-big-credible-gate.md) · [`big-idea-relevant-proprietary-gate`](big-idea-relevant-proprietary-gate.md) · [`big-idea-awareness-fit-gate`](big-idea-awareness-fit-gate.md)
- Frameworks: [`meta-launch-principle`](../../frameworks/meta-launch-principle.md) · [`power-of-one`](../../frameworks/power-of-one.md) · [`big-idea-ideation-tot`](../../frameworks/big-idea-architect/big-idea-ideation-tot.md)
- Registries: [`big-idea-registry`](../../data/registries/big-idea-registry.md) · [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`big-idea-architect`](../../agents/big-idea-architect.md) · [`ad-creative-factory`](../../agents/ad-creative-factory.md) · [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
