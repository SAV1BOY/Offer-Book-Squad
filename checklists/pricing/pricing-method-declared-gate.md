---
id: checklist.pricing.pricing-method-declared-gate
title: "Gate — Método de WTP Declarado (nada de palpite)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [pricing/van-westendorp, pricing/gabor-granger, pricing/conjoint-cbc, pricing/kano-model]
registries: [price-test-registry]
tags: [gate, pricing, metodo, wtp, convergencia, d2]
---

# Gate — Método de WTP Declarado

## Propósito
Este gate prova que cada ponto de preço veio de um **método de WTP nomeado e registrado** — não de intuição. Ele protege a tese de que nenhum método isolado decide o preço: a **convergência** decide. Um número defendido por "achismo" é frágil; um número onde van Westendorp, Gabor-Granger e conjoint apontam para a mesma faixa é robusto. O gate força o coração do agente — testar três ou mais métodos e cruzar resultados — e exige que a confiança do dado seja honesta: ponto `testado` (com dado de mercado real) versus `inferido` (proxies + valor mapeado, com plano de validação). Sem método declarado, o preço não é auditável, o relançamento não sabe o que reprecificar e o [`compliance-auditor`](../../agents/compliance-auditor.md) não pode checar uma âncora.

## Dono & Escopo
- **owner_agent:** `pricing-wtp-strategist` (roda os métodos, declara qual decidiu e registra). Sem poder de veto — alimenta os vetos de quem os tem.
- **Artefato inspecionado:** o campo `metodo` e `convergencia` de cada ponto no [`price-test-registry`](../../data/registries/price-test-registry.md), com a faixa, o ponto de indiferença e o ponto ótimo derivados de cada método rodado.

## Condição de Passagem
Cada ponto de preço nomeia ao menos um método de WTP usado, com pelo menos dois métodos convergindo na faixa, e declara se é testado ou inferido.

## Itens
1. **Método nomeado por ponto.** Verificar: cada ponto registra o(s) método(s) (`van-westendorp`, `gabor-granger`, `conjoint`, `kano`, `proxy`) — nenhum ponto sem método.
2. **≥3 métodos quando viável / ≥2 convergindo.** Verificar: o agente rodou três ou mais métodos onde possível; ao menos dois convergem na faixa fixada.
3. **Faixa e pontos derivados.** Verificar: o método produziu piso/teto, ponto de indiferença e/ou ponto ótimo — não só uma opinião de preço.
4. **Convergência avaliada.** Verificar: o campo `convergencia` está marcado alta/média/baixa; se baixa, há um desempate registrado (ex.: A/B de checkout).
5. **Status testado vs inferido.** Verificar: o ponto é `testado` (dado de mercado real) ou `inferido` (proxies + valor); inferido vem com plano de validação.
6. **Sem método único como decisor.** Verificar: nenhum ponto foi fixado por um só método caro/lento (ex.: conjoint sozinho) sem corroboração.
7. **Registrado e datado.** Verificar: método, faixa, convergência e status estão gravados e datados no `price-test-registry`.

## Evidência Exigida
Para marcar ✅: linkar a entrada do `price-test-registry` por ponto com os métodos rodados, a faixa derivada e o ponto fixado (itens 1–3, 7), o grau de convergência e, se baixa, o desempate (item 4), e o `status` testado/inferido com plano de validação quando inferido (itens 5–6).

## Protocolo de Falha
Item vermelho → o `pricing-wtp-strategist` adiciona ≥2 métodos e exige convergência antes de fixar; método único é reprovação. Se dois métodos divergem muito, não fixa ponto único — roda um teste-desempate e re-submete. Ponto sem dado de mercado fica `inferido` com plano de validação, e o agente sinaliza ao [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) que a margem depende de confirmar. Re-entrada: atualiza o `price-test-registry` e re-submete. Novo dado de WTP reabre este gate.

## Links
- Gates irmãos: [`pricing-value-derived-gate`](pricing-value-derived-gate.md) · [`pricing-anchor-gate`](pricing-anchor-gate.md) · [`pricing-packaging-gate`](pricing-packaging-gate.md) · [`pricing-kano-gate`](pricing-kano-gate.md)
- Frameworks: [`van-westendorp`](../../frameworks/pricing/van-westendorp.md) · [`gabor-granger`](../../frameworks/pricing/gabor-granger.md) · [`conjoint-cbc`](../../frameworks/pricing/conjoint-cbc.md) · [`kano-model`](../../frameworks/pricing/kano-model.md)
- Registries: [`price-test-registry`](../../data/registries/price-test-registry.md)
- Agentes: [`pricing-wtp-strategist`](../../agents/pricing-wtp-strategist.md) · [`unit-economics-stack-analyst`](../../agents/unit-economics-stack-analyst.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Agrega para: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md)
