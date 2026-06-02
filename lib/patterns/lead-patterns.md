---
id: lib.pattern.lead-patterns
title: "Padrões de Lead (abertura por nível de consciência)"
type: pattern
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [awareness-x-sophistication, big-idea-generator]
tags: [pattern, lead, copy-opening, awareness, reuse]
---

# Padrões de Lead (abertura por nível de consciência)

## O que é
O **lead** são as primeiras frases de uma peça — onde o leitor decide ficar ou sair. Este padrão é um mini-framework de decisão: ele casa o **tipo de lead** com o **nível de consciência** do prospect. A regra mestra de Schwartz: *encontre o leitor onde ele está*. Quem já quer o produto recebe um lead direto; quem nem sabe que tem o problema recebe um lead indireto. Errar o casamento queima tráfego.

Os 6 tipos de lead estão na taxonomia [`lead-types`](../taxonomies/lead-types.md): Oferta, Promessa, Problema-Solução, Segredo, Proclamação, História. Os 5 níveis de consciência estão em [`awareness-levels`](../taxonomies/awareness-levels.md). Este padrão é o **mapa** entre os dois, reutilizável em qualquer VSL, ad, e-mail ou carta.

## Estrutura do padrão
Aplique em três passos:

1. **Diagnostique a consciência dominante** (1 a 5) com evidência de VOC. Frio pede indireto; quente pede direto.
2. **Escolha o lead pelo mapa:**

| Consciência | Lead recomendado | Diretividade |
|---|---|---|
| 1 Inconsciente | História / Proclamação | Indireto |
| 2 Consciente do problema | Problema-Solução | Semi-direto |
| 3 Consciente da solução | Promessa / Segredo | Semi-direto |
| 4 Consciente do produto | Oferta | Direto |
| 5 Mais consciente | Oferta direta | Direto |

3. **Monte a abertura na sequência canônica:** Gancho → Identificação (a fala do avatar) → Tensão/Promessa → Ponte para o corpo. Quanto mais frio o público, mais longa a fase de identificação antes de qualquer venda.

## Quando aplicar
- No início de **toda** peça de copy, antes de escrever o corpo.
- Quando um lançamento atinge vários níveis ao mesmo tempo — segmente e use um lead por nível.
- Quando uma peça não retém (alta saída nos primeiros segundos): o lead provavelmente não casa com a consciência.

Não aplique um lead de Oferta a público frio. Direto demais cedo demais = rejeição.

## Exemplo
> **Caso: público frio (consciência 1), avatar dono de e-commerce que "acha que o problema é tráfego".**
> Lead escolhido: **História + Proclamação** (indireto).
> Abertura: *"Outro dia, um lojista me mandou o print do faturamento dele. Subiu o tráfego em 40%. O lucro? Caiu. O problema nunca foi tráfego."* — Gancho (história) → Identificação (o print, a dor real) → Tensão (o lucro caiu) → Proclamação (o problema não é tráfego) → ponte para o mecanismo.

A abertura não vende nada ainda. Ela baixa a guarda e cria o desejo antes da oferta.

## Variações
- **Lead de Segredo** (consciência 3-4): abre com informação nova e curiosa sobre o [mecanismo único](../../frameworks/unique-mechanism.md). Cuidado: o segredo precisa ser real.
- **Lead de Promessa** (consciência 3-4): abre com o maior benefício, grande **e** crível. Em mercado cético, ancore com prova logo atrás.
- **Lead de Oferta** (consciência 4-5): abre direto com a [oferta irresistível](../components/offer-block.md) — só funciona com público quente.
- **Híbrido por segmento:** o mesmo lançamento usa História para tráfego frio e Oferta para a lista quente.

## Liga com
- **Frameworks:** [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) (a matriz que trava o lead), [`big-idea-generator`](../../frameworks/big-idea-generator.md) (a Big Idea molda o gancho), [`copy/slippery-slide`](../../frameworks/copy/slippery-slide.md).
- **Taxonomias:** [`lead-types`](../taxonomies/lead-types.md) (os 6 tipos), [`awareness-levels`](../taxonomies/awareness-levels.md) (os 5 níveis).
- **Componentes:** [`offer-block`](../components/offer-block.md), [`proof-block`](../components/proof-block.md).
- **Agentes:** `positioning-lead-strategist` (dono — trava o lead), `vsl-webinar-scriptwriter`, `ad-creative-factory`, `email-sms-sequence-writer` (aplicam na abertura).
