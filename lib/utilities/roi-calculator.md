---
id: lib.utility.roi-calculator
title: "Calculadora de ROI & Payback (para a copy)"
type: utility
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: unit-economics-stack-analyst
frameworks: [value-equation, money-model-sequence]
tags: [utility, roi, payback, unit-economics, copy-proof, reuse]
---

# Calculadora de ROI & Payback (para a copy)

## Propósito
Esta utility transforma o preço da oferta em um **argumento de ROI** que a copy pode usar com lastro. Em vez de "vale a pena", ela calcula **quanto o cliente ganha por real investido** e **em quanto tempo o investimento se paga** (payback). É a ponte entre os números reais de unit economics e a frase que aparece na página — sempre com o cálculo rastreável, nunca inventado.

Serve dois leitores. Para o cliente: prova de que o retorno supera o custo. Para o squad: validação interna de que a oferta liquida o CAC e gera LTV positivo. Reutilizável em qualquer oferta com resultado financeiro quantificável.

## Spec
**Inputs:**
- `preco_oferta` (R$) — quanto o cliente paga.
- `ganho_esperado` (R$) — resultado financeiro médio **provado** (vem do [proof-registry](../../data/registries/proof-registry.md), não de chute).
- `prazo_resultado` (meses) — tempo até o ganho se materializar.
- `custo_recorrente` (R$/mês, opcional) — para ofertas de [continuidade](../patterns/continuity-patterns.md).
- `margem_cliente` (%, opcional) — converte receita em lucro quando aplicável.

**Outputs:**
- `roi_pct` = ((ganho_esperado − preco_oferta) / preco_oferta) × 100.
- `roi_multiplo` = ganho_esperado / preco_oferta (ex.: "7x").
- `payback_meses` = preco_oferta / (ganho_esperado / prazo_resultado).
- `frase_copy` — string pronta, conservadora, com a fonte do ganho.
- `flag_lastro` — `SIM/NÃO`: o `ganho_esperado` tem prova rastreável?

**Lógica:**
1. Valida que `ganho_esperado` aponta para um id do proof-registry. Sem lastro → `flag_lastro=NÃO` e bloqueia a frase.
2. Usa a **mediana** provada, não o melhor caso (evita claim exagerado, veto de compliance).
3. Calcula ROI, múltiplo e payback.
4. Gera `frase_copy` conservadora ("clientes recuperam, em média, X por real investido — base: N casos").

## Como um script implementa
`scripts/roi-calculator.py` (owner: unit-economics-stack-analyst). Lê os inputs de [`offer/unit-economics-template`](../../templates/strategy/unit-economics-template.md) e os ganhos provados do proof-registry. Roda com `python scripts/roi-calculator.py --offer <id>` e `--check` para dry-run read-only. Stdlib + pyyaml (única dep externa permitida, conforme [`style-guide`](../../docs/style-guide.md) §4k). Saída em markdown para colar no offer book; `EXIT 0` ok, `1` se algum claim não tem lastro, `2` erro de uso. Escreve a frase no [claim-registry](../../data/registries/claim-registry.md) para o `compliance-auditor` auditar.

## Exemplo
> **Inputs:** preco_oferta = R$ 497; ganho_esperado = R$ 3.500 (mediana de 142 casos, proof #PR-031); prazo_resultado = 1 mês.
> **Outputs:**
> - roi_pct = **604%**
> - roi_multiplo = **~7x**
> - payback_meses = **0,14** (cerca de 4 dias)
> - frase_copy: *"Na mediana de 142 lojas, cada R$ 1 investido virou R$ 7 em 30 dias — o curso se paga na primeira semana."*
> - flag_lastro: **SIM** (proof #PR-031).

Número conservador, payback explícito, fonte citada. A copy ganha um argumento que aguenta auditoria.

## Liga com
- **Frameworks:** [`value-equation`](../../frameworks/value-equation.md) (ROI alto = valor percebido alto), [`money-model-sequence`](../../frameworks/money-model-sequence.md) (payback rápido liquida o CAC).
- **Registries:** [`proof-registry`](../../data/registries/proof-registry.md), [`claim-registry`](../../data/registries/claim-registry.md), [`price-test-registry`](../../data/registries/price-test-registry.md).
- **Componentes/Padrões:** [`proof-block`](../components/proof-block.md), [`value-stack-block`](../components/value-stack-block.md), [`continuity-patterns`](../patterns/continuity-patterns.md).
- **Agentes:** `unit-economics-stack-analyst` (dono), `pricing-wtp-strategist` (usa payback no pricing), `compliance-auditor` (audita o lastro), `vsl-webinar-scriptwriter` (usa a frase na copy).
