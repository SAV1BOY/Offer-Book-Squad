---
id: lib.utility.price-ladder-builder
title: "Construtor de Escada de Preços (good-better-best + degraus)"
type: utility
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [pricing/packaging-good-better-best, pricing/decoy-effect, price-anchoring]
tags: [utility, pricing, packaging, ladder, anchoring, reuse]
---

# Construtor de Escada de Preços (good-better-best + degraus)

## Propósito
Esta utility monta a **escada de preços** de uma oferta — os pacotes (good-better-best), a âncora e, quando útil, a isca (decoy) — derivando cada degrau do **valor e da disposição a pagar (WTP)**, nunca do custo. Ela garante que os preços contam uma história coerente: o degrau-alvo parece a escolha óbvia, a âncora torna o alvo barato, e a isca empurra para o alvo.

O objetivo é remover o "achismo" do pricing. Em vez de "quanto cobrar?", a utility responde "quais 3 pacotes, em quais preços, com qual ancoragem, para maximizar receita por lead". Reutilizável em qualquer oferta com mais de um nível de empacotamento.

## Spec
**Inputs:**
- `wtp_distribuicao` — faixas de WTP do [price-test-registry](../../data/registries/price-test-registry.md) (Van Westendorp / Gabor-Granger).
- `componentes` — itens disponíveis para empacotar (do [offer stack](../../frameworks/offer-stack-builder.md)).
- `degrau_alvo` — o pacote que você quer que a maioria compre.
- `margem_minima` (%) — piso de margem por degrau.
- `usar_decoy` (bool) — incluir a isca?

**Outputs:**
- `escada` — tabela: pacote → itens → preço → papel (âncora / alvo / isca / entrada).
- `racional_ancoragem` — por que cada preço relativo ao alvo.
- `spread_pct` — distância de preço entre degraus (evita degraus colados).
- `flag_value_derived` — `SIM/NÃO`: cada preço deriva de WTP/valor com método declarado?

**Lógica:**
1. Lê a WTP e posiciona o `degrau_alvo` no ponto de maior receita esperada.
2. Cria a **âncora alta** acima do alvo (faz o alvo parecer pequeno; ver [`price-anchoring`](../../frameworks/price-anchoring.md)).
3. Cria a **entrada** abaixo (captura quem não paga o alvo).
4. Se `usar_decoy`, insere uma isca propositalmente pior que o alvo (ver [`pricing/decoy-effect`](../../frameworks/pricing/decoy-effect.md)).
5. Checa `margem_minima` e `spread_pct`; rejeita degraus que violam o piso ou ficam colados.

## Como um script implementa
`scripts/price-ladder-builder.py` (owner: pricing-wtp-strategist). Lê [`strategy/pricing-wtp-template`](../../templates/strategy/pricing-wtp-template.md) e o price-test-registry; escreve a escada em [`offer/products-and-offers-template`](../../templates/offer/products-and-offers-template.csv). Roda com `python scripts/price-ladder-builder.py --offer <id>`, `--check` para dry-run. Stdlib + pyyaml. `EXIT 0` ok, `1` se algum preço não deriva de valor (gate `pricing/pricing-value-derived-gate`), `2` erro de uso. O CSV de saída fica limpo; o `.md` irmão documenta o schema, conforme [`style-guide`](../../docs/style-guide.md) §4d.

## Exemplo
> **Inputs:** WTP mediano R$ 500; alvo = pacote "Pro"; usar_decoy = true.
> **Output (escada):**

| Pacote | Itens | Preço | Papel |
|---|---|---|---|
| Start | núcleo só | R$ 297 | entrada |
| **Pro** | núcleo + 3 bônus + suporte | **R$ 497** | **alvo** |
| Pro Solo | núcleo + 3 bônus, sem suporte | R$ 447 | isca (decoy) |
| Elite | Pro + mentoria 1:1 | R$ 1.497 | âncora |

> racional_ancoragem: *Elite (R$ 1.497) faz o Pro parecer barato; Pro Solo (R$ 447) por quase o mesmo preço sem suporte empurra para o Pro.*
> flag_value_derived: **SIM** (Van Westendorp, registry #PT-014).

A isca e a âncora trabalham para o alvo; cada preço tem método.

## Liga com
- **Frameworks:** [`pricing/packaging-good-better-best`](../../frameworks/pricing/packaging-good-better-best.md), [`pricing/decoy-effect`](../../frameworks/pricing/decoy-effect.md), [`price-anchoring`](../../frameworks/price-anchoring.md), [`pricing/value-based-pricing`](../../frameworks/pricing/value-based-pricing.md).
- **Taxonomias:** [`offer-types`](../taxonomies/offer-types.md) (papéis na escada).
- **Registries:** [`price-test-registry`](../../data/registries/price-test-registry.md), [`offer-registry`](../../data/registries/offer-registry.md).
- **Componentes/Utilities:** [`value-stack-block`](../components/value-stack-block.md), [`roi-calculator`](roi-calculator.md).
- **Agentes:** `pricing-wtp-strategist` (dono), `unit-economics-stack-analyst` (valida margem), `money-model-designer` (encaixa a escada na sequência), `value-equation-engineer` (confere que cada degrau move uma alavanca).
