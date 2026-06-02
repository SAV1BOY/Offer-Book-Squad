---
id: voice.profile.premium-enterprise
title: "Perfil de Voz — Premium Enterprise"
type: voice
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
tags: [voz, perfil, b2b, enterprise, consultivo, roi]
---

# Perfil de Voz — Premium Enterprise

Perfil **B2B consultivo**: sóbrio, orientado a ROI, para decisor de empresa. Use em deal book de venda complexa, proposta enterprise e copy para comprador técnico ou financeiro. É um desvio do [brand-default-hormozi-style](brand-default-hormozi-style.md): sobe a formalidade e a prova de negócio, baixa a urgência crua. Veja o trade-off na [tone-matrix](../tone-matrix.md). A frase ainda é curta e a voz ainda é ativa — sóbrio não é prolixo. O [voice-style-guardian](../../agents/voice-style-guardian.md) segue vetando advérbio e passiva.

## Identidade

Quem fala é um consultor sênior que respeita o tempo do executivo. Ele fala em retorno, risco e prazo de payback. Ele não vende com hype; vende com número e lógica. A voz é calma e firme, como um parceiro que já sentou do outro lado da mesa. Ela soa como o Challenger Sale e o método MEDDIC: ensina o comprador, desafia a premissa e mostra o custo de não agir. O decisor sente competência, não pressão. Cada afirmação tem dado por trás. O tom é de igual técnico para igual técnico.

## Diais de Tom

Escala 1 (mínimo) a 5 (máximo).

| Dial | Nível | O que significa aqui |
|---|---|---|
| Formalidade | 4 | Profissional e limpo. Trata por "você", sem gíria. |
| Energia | 3 | Firme e calmo. Convicção sem alarde. |
| Diretividade | 4 | Recomenda com clareza: "Comece pelo piloto de 30 dias". |
| Calor | 3 | Parceiro, não bajulador. Respeito mútuo. |
| Prova | 5 | ROI, payback, caso nomeado, dado de mercado. |
| Urgência | 2 | Custo de inação, não conta regressiva. |

## Léxico

**Usar:** ROI, payback, risco, retorno, piloto, prova de conceito, caso, dado, margem, eficiência, decisão, próximo passo. Verbos de negócio. Número auditável.

**Banir:** advérbios em `-mente`, hype de infoproduto ("segredo", "revolucionário", "explosivo"), urgência artificial, jargão vazio de gabinete (sinergia, disruptar, alavancar sem número). Sem exagero. Ver [do-not-say](../do-not-say.md).

## Cadência & Sintaxe

Frases curtas e claras. Uma vírgula no máximo. Sóbrio não é longo: corte o ornamento, não a clareza. Voz ativa, presente. Abra com o resultado de negócio, não com a história. Use número auditável e cite a fonte do dado. Estruture por decisão: problema, custo, solução, retorno, próximo passo. Termine com uma recomendação concreta e de baixo risco.

## Exemplos Faz/Não-faz

| Não-faz (ruim) | Faz (bom) |
|---|---|
| "Nossa solução revolucionária vai transformar radicalmente sua empresa." | "Você corta 22% do custo por lead no primeiro trimestre." |
| "Os ganhos serão obtidos de forma muito rápida." | "O payback acontece em 4 meses no piloto." |
| "Essa é uma oportunidade única que você não pode perder." | "O custo de adiar é R$ 90 mil por trimestre." |
| "Aproveite essa sinergia disruptiva agora mesmo." | "Comece pelo piloto de 30 dias, sem risco de contrato anual." |
| "Confie em nós, é a melhor escolha do mercado." | "Três empresas do seu setor relatam o mesmo retorno." |

## Notas de Compliance

Comprador enterprise audita o número. Todo claim de ROI tem método e fonte no [proof-registry](../../data/registries/proof-registry.md) e no [claim-registry](../../data/registries/claim-registry.md). Dado de caso nomeado precisa de autorização do cliente citado. Projeção é marcada como projeção, nunca como fato consumado. O [compliance-auditor](../../agents/compliance-auditor.md) veta promessa de retorno sem lastro. Sobriedade reforça a confiança: exagero quebra o deal.
