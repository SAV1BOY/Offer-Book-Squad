---
id: voice.tone-matrix
title: "Matriz de Tom — Quando Subir e Baixar Cada Dial"
type: voice
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
tags: [voz, tom, matriz, urgencia, formalidade, prova, consciencia, sofisticacao]
---

# Matriz de Tom — Quando Subir e Baixar Cada Dial

A voz da marca é uma só, mas o **tom** muda com o contexto. Este arquivo diz **quando** mexer em cada dial e **quanto**. A base de legibilidade nunca muda: frase curta, voz ativa, presente, sem advérbio. O que se ajusta é a urgência, a formalidade, a prova, o calor e a diretividade. O [voice-style-guardian](../agents/voice-style-guardian.md) usa esta matriz para julgar se o tom casa com o contexto. Os perfis em [profiles/](profiles/) já vêm com os dials pré-setados; esta matriz mostra os limites e os gatilhos para sair do default [brand-default-hormozi-style](profiles/brand-default-hormozi-style.md).

A escala é sempre **1 (mínimo) a 5 (máximo)**. A régua de leitura está no [reading-level-guide](reading-level-guide.md). As proibições estão no [do-not-say](do-not-say.md). O passe final está no [voice-checklist](voice-checklist.md).

## Como ler esta matriz

Cada dial responde a um gatilho de contexto. Você sobe um dial quando o contexto pede e a verdade permite. Você baixa quando o contexto não suporta. Regra dura: **a urgência só sobe se a escassez é real** (princípio `truthful_scarcity`). Nenhum ajuste de tom autoriza claim sem lastro. O tom muda a temperatura, nunca o fato.

## Os seis dials e seus gatilhos

| Dial | Sobe quando | Baixa quando | Teto de segurança |
|---|---|---|---|
| **Urgência** | Prazo real, vaga finita, preço que sobe de fato | Relação de nutrição, topo de funil, público frio sem oferta | Nunca acima de 3 sem escassez verdadeira e datada |
| **Formalidade** | Comprador B2B, decisor técnico, deal de alto valor | Audiência de criador, tráfego frio de massa, comunidade | Nunca vira jargão de gabinete (ver [do-not-say](do-not-say.md)) |
| **Prova** | Claim grande, preço alto, público cético ou sofisticado | Promessa pequena e óbvia, público que já confia | Prova sobe sem limite, mas cada número aponta ao [proof-registry](../data/registries/proof-registry.md) |
| **Calor** | Comunidade fiel, história pessoal, relação longa | Decisor que quer dado, não afago | Calor nunca vira falsa intimidade |
| **Diretividade** | Momento de CTA, leitor já convencido | Abertura, leitor frio, fase de ensino | Ordem só depois do valor entregue |
| **Energia** | Lançamento, carrinho aberto, evento ao vivo | Conteúdo de fundo, B2B sóbrio | Empurrar nunca vira gritar |

## Matriz por estágio de consciência

Casa com a taxonomia de [awareness-levels](../lib/taxonomies/awareness-levels.md). Quanto menos consciente o público, mais a história e a prova carregam; quanto mais consciente, mais a oferta e a urgência fecham.

| Consciência | Urgência | Prova | Diretividade | Move primeiro |
|---|---|---|---|---|
| Inconsciente | 1 | 4 | 2 | A dor nomeada e a história |
| Consciente do problema | 2 | 4 | 2 | O problema e o mecanismo |
| Consciente da solução | 3 | 4 | 3 | Por que esta solução, não outra |
| Consciente do produto | 4 | 5 | 4 | O diferencial e a prova dura |
| Mais consciente | 5 | 3 | 5 | A oferta, o preço e o prazo |

## Matriz por estágio de sofisticação

Casa com [sophistication-levels](../lib/taxonomies/sophistication-levels.md). Mercado mais batido exige mecanismo único e prova mais pesada; mercado novo aceita a promessa direta.

| Sofisticação | Prova | Mecanismo no texto | Cuidado de voz |
|---|---|---|---|
| Estágio 1 (mercado novo) | 3 | Promessa direta basta | Não complique o que é simples |
| Estágio 2 | 3 | Promessa maior e específica | Número exato vence adjetivo |
| Estágio 3 | 4 | Mecanismo nomeado entra | Sem hype, o mecanismo carrega |
| Estágio 4 | 5 | Mecanismo + prova pesada | Cético: mostre, não diga |
| Estágio 5 (exausto) | 5 | Nova identidade / nicho | Honestidade radical vence o ruído |

## Matriz por contexto de peça

| Contexto | Perfil-base sugerido | Urgência | Formalidade | Calor |
|---|---|---|---|---|
| Ad de tráfego frio | [story-driven](profiles/story-driven.md) ou default | 2 | 2 | 3 |
| VSL / webinário | [story-driven](profiles/story-driven.md) → fecha no default | 3 | 2 | 4 |
| E-mail de nutrição | [friendly-creator](profiles/friendly-creator.md) | 1 | 1 | 5 |
| E-mail de carrinho | [direct-response-aggressive](profiles/direct-response-aggressive.md) | 5 | 1 | 2 |
| Página de vendas | default → [direct-response-aggressive](profiles/direct-response-aggressive.md) no CTA | 4 | 2 | 3 |
| Deal book B2B | [premium-enterprise](profiles/premium-enterprise.md) | 2 | 4 | 3 |
| Post de comunidade | [friendly-creator](profiles/friendly-creator.md) | 1 | 1 | 5 |

## Exemplos Faz/Não-faz

Mostram o mesmo claim com o dial certo e errado para o contexto.

| Contexto | Não-faz (tom errado) | Faz (tom certo) |
|---|---|---|
| Nutrição (urgência alta demais) | "Última chance! Corra agora ou perca tudo!" | "Te conto uma ideia que ajuda você hoje." |
| Carrinho (urgência baixa demais) | "Talvez você queira dar uma olhada quando puder." | "As vagas fecham amanhã. Garanta a sua." |
| B2B (hype no lugar de dado) | "Nossa solução revolucionária muda tudo!" | "Você corta 22% do custo por lead no trimestre." |
| Tráfego frio (CTA cedo demais) | "Compre agora este produto incrível." | "Existe um motivo pelo qual você ainda trava aqui." |

## Notas de Compliance

Subir a urgência sem escassez real é veto do [compliance-auditor](../agents/compliance-auditor.md) (`truthful_scarcity`). Subir a prova exige cada número rastreado no [proof-registry](../data/registries/proof-registry.md) e cada afirmação no [claim-registry](../data/registries/claim-registry.md). Mudar o tom nunca muda o fato. A matriz ajusta temperatura, não verdade. Quando o tom contextual conflita com um disclaimer legal, a lei vence e o caso sobe ao [offerbook-chief](../agents/offerbook-chief.md).
