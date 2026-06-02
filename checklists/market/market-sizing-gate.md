---
id: checklist.market.market-sizing-gate
title: "Gate — Mercado Dimensionado com TAM/SAM/SOM Coerentes e SOM Compatível com a Meta"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
frameworks: [starving-crowd, awareness-x-sophistication]
registries: [offer-registry]
tags: [gate, market, sizing, tam-sam-som, d1, receita, viabilidade]
---

# Gate — Mercado Dimensionado (TAM/SAM/SOM)

## Propósito
Este gate prova que o `market-sophistication-analyst` dimensionou o mercado em TAM/SAM/SOM com base de cálculo explícita, e que o SOM comporta a meta de receita do caso. Existe porque um diagnóstico perfeito de um mercado pequeno demais para a meta é um lançamento que nasce condenado: o `offerbook-chief` precisa do tamanho antes de liberar o pipeline. Sizing fantasia — um TAM gigante sem base — engana o squad inteiro e infla expectativas. O gate força o número de baixo para cima (SOM realista no prazo/orçamento → SAM → TAM), com a base de cada camada visível, para que a decisão de seguir seja sobre demanda real, não sobre um slide otimista.

## Dono & Escopo
- **owner_agent:** `market-sophistication-analyst` (consolida o sizing a partir do handoff de pesquisa ou de coleta própria).
- **Artefato inspecionado:** o **bloco de dimensionamento** do market-brief (TAM/SAM/SOM com base de cálculo), referenciado pela oferta-semente no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O mercado tem TAM, SAM e SOM dimensionados com base de cálculo explícita, na ordem coerente SOM ≤ SAM ≤ TAM, e o SOM comporta a meta de receita do caso.

## Itens
1. **Três camadas presentes.** Verificar: o brief traz TAM (total com o problema), SAM (servível pelo produto no recorte) e SOM (obtenível no prazo/orçamento) — nenhuma camada faltando.
2. **Base de cálculo explícita.** Verificar: cada camada mostra **como** foi calculada (fonte de população, % de recorte, premissa de captura), não só um número solto.
3. **Ordem coerente.** Verificar: SOM ≤ SAM ≤ TAM; nenhuma camada maior que a anterior.
4. **Construção de baixo para cima.** Verificar: o SOM foi derivado de premissas realistas de alcance no prazo/orçamento, não fatiado de cima por chute.
5. **SOM compatível com a meta.** Verificar: o SOM, ao ticket médio previsto, comporta a meta de receita do escopo; se não comportar, o brief sinaliza o risco.
6. **Fonte do sizing citada.** Verificar: o handoff de pesquisa (ou a coleta própria) está citado; estimativas próprias são marcadas como "ordem de grandeza".
7. **Validade temporal marcada.** Verificar: o brief registra que o sizing vale para o ciclo atual e deve ser reavaliado (a demanda migra).

## Evidência Exigida
Para marcar cada item ✅, linkar o bloco de dimensionamento do market-brief com os três números e a base de cada um, e a linha do [`offer-registry`](../../data/registries/offer-registry.md) que referencia o sizing. A base de cálculo precisa ser reproduzível (fonte + fórmula), não declarada. A checagem SOM-vs-meta linka a meta de receita do escopo travado no [`chief-scope-approval-gate`](../chief/chief-scope-approval-gate.md).

## Protocolo de Falha
Item vermelho → o `market-sophistication-analyst` refaz o sizing de baixo para cima com a base explícita; número sem base não passa. SOM incompatível com a meta → o analista **sinaliza ao `offerbook-chief`** (detentor do veto) o risco de mercado pequeno demais, recomendando ajustar a meta, o recorte ou a oferta — a decisão de barrar é do chief. Sizing fantasia (TAM gigante sem fonte) → reconstrói com fonte rastreável. Sem dados de pesquisa → entrega como "ordem de grandeza" com confiança rebaixada. Re-entrada: refeito o sizing com base, o gate é re-submetido.

## Links
- Frameworks: [`starving-crowd`](../../frameworks/starving-crowd.md) · [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Escopo/meta de receita: [`chief-scope-approval-gate`](../chief/chief-scope-approval-gate.md)
- Gate par (fome do mercado): [`market-starving-crowd-gate`](market-starving-crowd-gate.md)
