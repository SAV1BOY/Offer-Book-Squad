---
id: checklist.funnel.funnel-no-dead-end-gate
title: "Gate — Sem Becos Sem Saída (toda página tem próximo passo)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: funnel-architect
frameworks: [offer-to-funnel-mapping, launch/cart-open-close]
registries: [decision-registry]
tags: [gate, funil, sem-becos, proximo-passo, recuperacao, d5]
---

# Gate — Sem Becos Sem Saída

## Propósito
Este gate prova que **nenhuma página ou estado do funil termina sem próximo passo**. Toda página tem uma seta de saída, e todo "não" — recusa de upsell, abandono de checkout, fim de uma sequência — tem rota, não silêncio. Ele existe porque um beco sem saída é margem perdida: o comprador que chega à página de obrigado sem convite à continuidade, ou recusa o upsell e cai no vazio, nunca volta. Na lógica de Brunson, cada página tem um único próximo passo; o gate eleva isso a regra inegociável. Vale o princípio `decision_before_ornament`: cada página serve a uma decisão e leva à próxima. O gate força o teste "siga cada seta — alguma termina no vazio?". É a barreira central do `funnel-architect`, listada como gate obrigatório no `config.yaml`, e a que mais protege a receita do backend.

## Dono & Escopo
- **owner_agent:** `funnel-architect` (garante o próximo passo em cada página e estado). O `compliance-auditor` co-checa garantia/T&C visíveis por página.
- **Artefato inspecionado:** o `funnel-map` completo e as `page-specs`, com as bifurcações e rotas de recuperação registradas no [`decision-registry`](../../data/registries/decision-registry.md). Gate obrigatório conforme `config.yaml: routing.map-funnel`.

## Condição de Passagem
Toda página e todo estado do funil — incluindo a página de obrigado, o "não" do upsell e o abandono — tem um próximo passo definido.

## Itens
1. **Próximo passo por página.** Verificar: cada página tem ao menos uma seta de saída (CTA ou redirecionamento), sem tela final morta.
2. **Página de obrigado viva.** Verificar: a página de obrigado convida à continuidade ou à próxima oferta, não encerra o fluxo.
3. **"Não" do upsell roteado.** Verificar: a recusa do upsell cai no downsell ou na oferta de continuidade tardia, nunca no vazio.
4. **Abandono com recuperação.** Verificar: o abandono de checkout dispara a sequência de recuperação (via `launch/cart-open-close`).
5. **Fim de sequência com saída.** Verificar: a última mensagem de cada sequência aponta para um próximo passo (oferta backend, conteúdo).
6. **Teste da seta.** Verificar: seguindo cada seta do mapa, nenhuma termina no vazio (TY, "não", abandono cobertos).
7. **Garantia/T&C por página.** Verificar: cada página de oferta tem garantia/T&C visível (pré-checagem do `compliance-auditor`).

## Evidência Exigida
Para marcar ✅: linkar o `funnel-map` com a seta de saída de cada página (itens 1–2), as rotas de "não" e abandono no `decision-registry` (itens 3–4), o fim de cada sequência com próximo passo (item 5) e o resultado do teste da seta (item 6).

## Protocolo de Falha
Item vermelho → o `funnel-architect` **adiciona o próximo passo** (convite à continuidade, downsell, recuperação) à página ou estado morto; nenhuma página termina sem seta. Beco na página de obrigado, "não" sem rota ou abandono sem recuperação reabrem o gate. A cobertura das trilhas do money model é garantida no [`funnel-path-coverage-gate`](funnel-path-coverage-gate.md); o backend ligado no [`funnel-backend-gate`](funnel-backend-gate.md); rotas e loops no [`funnel-redirect-gate`](funnel-redirect-gate.md). Re-entrada: fechar o beco, atualizar o `decision-registry` e re-submeter. Mudança na copy ou no money model a montante reabre este gate.

## Links
- Frameworks: [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md) · [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`funnel-architect`](../../agents/funnel-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`funnel-path-coverage-gate`](funnel-path-coverage-gate.md) · [`funnel-order-bump-gate`](funnel-order-bump-gate.md) · [`funnel-redirect-gate`](funnel-redirect-gate.md) · [`funnel-backend-gate`](funnel-backend-gate.md)
