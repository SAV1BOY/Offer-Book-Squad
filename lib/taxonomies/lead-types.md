---
id: taxonomy.lead-types
title: "Os 6 Tipos de Lead (abertura de copy)"
type: taxonomy
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
sources:
  - "Michael Masterson & John Forde, *Great Leads* (2011)"
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)"
tags: [lead, copy-opening, awareness, hook]
---

# Os 6 Tipos de Lead

> **Fonte:** Michael Masterson & John Forde, *Great Leads* (2011); fundamentos em Schwartz, *Breakthrough Advertising* (1966). **Anti-verbatim:** princípios em redação original.

O **lead** são as primeiras frases (os primeiros 10-20% de uma VSL, carta ou ad) — onde o leitor decide ficar ou sair. O tipo de lead **deve casar com o nível de [consciência](awareness-levels.md)**: leads diretos para quem já está consciente; leads indiretos para quem ainda não.

| # | Lead | Diretividade | Casa com consciência | Quando vence |
|---|---|---|---|---|
| 1 | **Oferta** | Direto | 4-5 (Produto/Mais consciente) | Público quente; oferta forte fala por si |
| 2 | **Promessa** | Direto | 3-4 (Solução/Produto) | Benefício grande e crível |
| 3 | **Problema-Solução** | Semi-direto | 2-3 (Problema/Solução) | Dor latente e nomeável |
| 4 | **Segredo** | Indireto | 2-3 | Mecanismo/informação nova e curiosa |
| 5 | **Proclamação** | Indireto | 1-2 | Afirmação ousada que desperta |
| 6 | **História** | Indireto | 1-2 (Inconsciente) | Público frio; resistência alta |

## Detalhe por lead

### 1. Lead de Oferta
Abre direto com a **oferta irresistível** ("Leve X, Y e Z por R$..."). Exige público consciente do produto e uma oferta tão forte que a própria estrutura convence. Ver [`offer-types`](offer-types.md).

### 2. Lead de Promessa
Abre com o **maior benefício** ("Em 30 dias, você vai..."). A promessa precisa ser grande **e** crível — promessa grande demais em mercado cético derruba a leitura.

### 3. Lead de Problema-Solução
Espelha a **dor** na linguagem do avatar (verbatim), agita a consequência, então apresenta a solução. O cavalo de batalha do mercado consciente do problema.

### 4. Lead de Segredo
Abre com **informação nova e intrigante** ("Existe um motivo pelo qual..."). Casa com o mecanismo único (sofisticação 3-4). Cuidado: o "segredo" precisa ser real e provável, não clickbait.

### 5. Lead de Proclamação
Uma **afirmação ousada e específica** ("Demita seu nutricionista."). Desperta o inconsciente/consciente-do-problema pela audácia. Precisa de prova logo atrás.

### 6. Lead de História
Abre com **narrativa** (jornada, virada, identificação). Vence o público frio porque baixa a guarda antes de vender. Ver [`frameworks/copy/slippery-slide`](../../frameworks/copy/slippery-slide.md) e o arco de [storytelling](../../reference/psychology/identity-and-belonging.md).

## Como o squad usa
- `positioning-lead-strategist`: trava o lead via a matriz [`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md) — o gate `positioning/positioning-awareness-fit` reprova lead que não casa com a consciência.
- `vsl-webinar-scriptwriter`, `ad-creative-factory`, `email-sms-sequence-writer`: aplicam o lead travado na abertura de cada peça.

**Armadilha:** usar lead de Oferta (direto) num público frio (inconsciente) — queima o tráfego. Frio pede História/Proclamação.
