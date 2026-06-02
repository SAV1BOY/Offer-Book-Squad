---
id: template.growth.pr-plan
title: "PR Plan — O Plano de Imprensa & Marca (Ângulo, Alvos, Provas, Calendário)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
consumes: [template.core.offer-book-master, template.strategy.big-idea, template.strategy.proof-bank]
produces: [data.registry.decision]
frameworks: [launch/pr-brand-maximization, big-idea-generator, power-of-one, proof-to-claim-chain]
checklists: [pr/pr-plan-checklist]
registries: [decision-registry, proof-registry]
tags: [template, pr, imprensa, marca, earned-media, autoridade, growth]
---

# PR Plan — O Plano de Imprensa & Marca

A imprensa não vende sua oferta — ela **empresta autoridade** para ela. Uma matéria, um podcast, uma citação de terceiro fazem o que sua própria copy não pode: a prova vem de fora. Este template desenha o plano de PR de ponta a ponta: o ângulo noticiável, os veículos-alvo, a prova que sustenta cada história, o porta-voz e o calendário casado com o lançamento. PR amplifica uma oferta que já converte — não conserta oferta fraca (`offer_before_persuasion`). O ângulo nasce da **Big Idea única**: a mesma tese que move a copy move a pauta (Power of One). E aqui a regra é dura: nada de claim sem lastro numa nota de imprensa. O que você diz a um jornalista é o que o `compliance-auditor` mais vigia, porque vira palavra pública (`evidence_before_opinion`, `truthful_scarcity`).

## Como usar
- **Agente dono:** `pr-brand-strategist`. Pareia com o `proof-credibility-curator` (que fornece a prova de cada história), o `big-idea-architect` (dono do ângulo) e o `launch-producer` (que encaixa a janela de imprensa na pista do lançamento).
- **Task:** `build-pr-plan`. Roda em D6, depois do Offer Book aprovado e da Big Idea travada. Aplica o framework [`pr-brand-maximization`](../../frameworks/launch/pr-brand-maximization.md).
- **Quando:** o estrategista preenche este plano assim que existe um ângulo noticiável com prova. PR sem prova é assessoria de boato.
- Regra de ouro: **o que é notícia para o veículo, não o que é promoção para você**. O ângulo precisa interessar à audiência do jornalista, não só à sua. Campo vazio = pauta fraca = gate vermelho.

## Campos & Instruções
- **{{NOME_DA_CAMPANHA}}** — o nome de trabalho da campanha de PR, ligado ao lançamento.
- **{{BIG_IDEA}}** — a Grande Ideia única (vem do [`big-idea-template`](../strategy/big-idea-template.md)). É a raiz do ângulo.
- **{{ANGULO_NOTICIAVEL}}** — por que isso é **notícia agora**: o dado novo, a tendência, o contraste, o número surpreendente. O gancho do jornalista, não o seu CTA.
- **{{HISTORIAS}}** — as 2-3 histórias derivadas do ângulo (ex.: dado de mercado, caso de cliente, opinião contrária do fundador). Cada uma com sua prova.
- **{{PROVA_POR_HISTORIA}}** — a evidência que sustenta cada história (estudo, número, caso verificável), com id no [`proof-registry`](../../data/registries/proof-registry.md). Sem prova, a história não vai.
- **{{VEICULOS_ALVO}}** — a lista priorizada de veículos e jornalistas por fit + alcance + relevância (o "Dream 100" da imprensa). Quem fala com seu avatar entra primeiro.
- **{{PORTA_VOZ}}** — quem dá a entrevista (fundador, cliente, especialista) e a credencial que o torna citável.
- **{{ATIVOS_DE_PR}}** — o que entra no press kit: release, bio, fotos, fact sheet, FAQ de imprensa. Pronto para o jornalista usar.
- **{{CALENDARIO_PR}}** — a grade de outreach e embargo casada com o lançamento (pré-aquecimento, abertura, pico). Datas reais.
- **{{METRICA_DE_SUCESSO}}** — como você mede (menções, alcance, backlinks, sentimento, tráfego de referência). Resultado, não vaidade.
- **{{REGRAS_E_RISCOS}}** — o que **não** dizer, claims proibidos, temas sensíveis. Reforço de compliance para a fala pública.
- **{{STATUS}}** — o estado do plano: rascunho, em outreach, no ar, encerrado.

## O Template
```
# PR PLAN — {{NOME_DA_CAMPANHA}}
Owner: pr-brand-strategist · Data: {{DATA}} · Status: {{STATUS}}

## 1. ÂNGULO (a raiz)
Big Idea: {{BIG_IDEA}}
Ângulo noticiável (por que é notícia agora): {{ANGULO_NOTICIAVEL}}

## 2. HISTÓRIAS & PROVA
| # | História | Gancho | Prova (id no registry) |
|---|----------|--------|------------------------|
| 1 | {{HISTORIA_1}} | {{GANCHO_1}} | {{PROVA_1}} |
| 2 | {{HISTORIA_2}} | {{GANCHO_2}} | {{PROVA_2}} |
| 3 | {{HISTORIA_3}} | {{GANCHO_3}} | {{PROVA_3}} |

## 3. VEÍCULOS-ALVO (priorizados)
| # | Veículo / Jornalista | Audiência | Alcance | Fit | Status |
|---|----------------------|-----------|---------|-----|--------|
| 1 | {{VEICULO_1}} | {{AUDIENCIA_1}} | {{ALCANCE_1}} | {{FIT_1}} | {{STATUS_1}} |
| 2 | {{VEICULO_2}} | {{AUDIENCIA_2}} | {{ALCANCE_2}} | {{FIT_2}} | {{STATUS_2}} |

## 4. PORTA-VOZ
Quem fala: {{PORTA_VOZ}} · Credencial: {{CREDENCIAL}}

## 5. PRESS KIT (ativos)
Inclui: {{ATIVOS_DE_PR}}

## 6. CALENDÁRIO (casado com o lançamento)
Pré-aquecimento: {{DATA_PRE}}  Embargo até: {{DATA_EMBARGO}}
Abertura: {{DATA_ABERTURA}}  Pico/follow-up: {{DATA_PICO}}

## 7. MÉTRICA DE SUCESSO
Como medimos: {{METRICA_DE_SUCESSO}}

## 8. REGRAS & RISCOS (compliance)
Não dizer: {{O_QUE_NAO_DIZER}}
Temas sensíveis: {{TEMAS_SENSIVEIS}}
```

## Exemplo preenchido
> **# PR PLAN — Imprensa do Motor 72h**
> Owner: pr-brand-strategist · Data: 2026-06-02 · Status: em outreach
>
> **1. ÂNGULO** — Big Idea: *"A janela de 72 horas que devolve o lucro que seu checkout esconde."* Ângulo noticiável: **74% dos carrinhos no varejo PME brasileiro são abandonados** — um estudo novo mostra quanto isso custa por mês.
> **2. HISTÓRIAS & PROVA** — 1. *O dado*: o custo invisível do abandono (gancho: número inédito; prova: proof-registry#PR-014). 2. *O caso*: loja que recuperou +21% em 30 dias (gancho: caso verificável; prova: proof-registry#PR-031). 3. *A opinião contrária*: "desconto não recupera carrinho, tempo recupera" (gancho: contraste; prova: proof-registry#PR-040).
> **3. VEÍCULOS-ALVO** — 1. *Portal de E-commerce* (donos de loja, 300k/mês, fit alto, contatado). 2. *Podcast de Varejo* (gestores, 40k/ep, fit alto, agendado).
> **4. PORTA-VOZ** — Fundador, ex-head de growth de marketplace, autor do estudo.
> **5. PRESS KIT** — release, bio, fact sheet com o dado dos 74%, 3 fotos, FAQ de imprensa.
> **6. CALENDÁRIO** — pré-aquecimento 28/05; embargo até 02/06 9h; abertura 03/06; follow-up 06/06.
> **7. MÉTRICA** — menções em veículos-alvo, alcance somado, backlinks, tráfego de referência ao funil.
> **8. REGRAS & RISCOS** — Não dizer "garante recuperar X%" (é mediana, não garantia). Tema sensível: não citar nome de cliente sem autorização.

## DoD do entregável
O PR Plan está pronto quando: (1) os 8 blocos estão preenchidos, sem `{{PLACEHOLDER}}` solto; (2) o ângulo é **noticiável de verdade** (interessa à audiência do veículo, não é só promoção) e deriva da **Big Idea única** (Power of One); (3) cada história tem **prova rastreável** com id real no [`proof-registry`](../../data/registries/proof-registry.md) — história sem lastro não entra (`evidence_before_opinion`, satisfazendo a [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md)); (4) os veículos-alvo estão priorizados por fit + alcance + relevância e o porta-voz tem credencial citável; (5) o press kit existe e está pronto para o jornalista usar; (6) o calendário casa com a pista do lançamento (pré, abertura, pico) com datas reais e embargo honesto; (7) a métrica de sucesso é de resultado (alcance, backlinks, referência), não de vaidade; (8) as regras de fala pública estão escritas e nenhum claim sem lastro vai a um jornalista (alinhado ao `compliance-auditor`, `truthful_scarcity`). Só então o plano entra na pista do `launch-producer` e passa no [`pr-plan-checklist`](../../checklists/pr/pr-plan-checklist.md).
