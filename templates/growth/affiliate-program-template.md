---
id: template.growth.affiliate-program
title: "Affiliate Program — O Programa de Afiliados (Recrutar, Armar, Premiar)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
consumes: [template.core.offer-book-master, template.growth.affiliate-prizes]
produces: [template.growth.affiliate-blackbook]
frameworks: [launch/affiliate-army, money-model-sequence, launch/cart-open-close, launch/runway-and-phases]
checklists: [affiliate/affiliate-program-checklist]
registries: [decision-registry]
tags: [template, affiliate, jv, dream-100, comissao, leaderboard, growth]
---

# Affiliate Program — O Programa de Afiliados

Este template desenha o **programa de afiliados** de ponta a ponta: quem recruta, quanto paga, em que janela, com que regras e com que prêmios. Um afiliado leva sua oferta para uma lista que você não tem. Coordenado, ele vira um **exército** que dispara no mesmo dia e multiplica o pico. O programa só funciona sobre uma oferta que já converte na lista própria — afiliado amplifica o que existe, não conserta oferta fraca (`offer_before_persuasion`). A escassez e os bônus aqui são **100% reais** (`truthful_scarcity`): o deadline some de verdade no mesmo horário para todos.

## Como usar
- **Agente dono:** `affiliate-program-architect`. Pareia com o `launch-producer` (integra os afiliados à pista) e com o `money-model-designer` (garante que a economia do afiliado fecha com a escada).
- **Task:** `build-affiliate-program`. Roda em D6, depois do Offer Book aprovado e da oferta validada na lista própria.
- **Quando:** o arquiteto preenche este template assim que o calendário do lançamento existe. Ele define a economia, recruta o [Dream 100](../../frameworks/launch/affiliate-army.md), e entrega o material no [`affiliate-blackbook-template`](affiliate-blackbook-template.md). Os prêmios vêm da planilha [`affiliate-prizes-template`](affiliate-prizes-template.csv).
- Use número e prova nos campos de comissão e economia. Use a Big Idea única em toda comunicação. Campo vazio = programa incompleto = gate vermelho.

## Campos & Instruções
- **{{NOME_DO_PROGRAMA}}** — o nome de trabalho do programa de afiliados, ligado ao nome da oferta núcleo.
- **{{OFERTA_VINCULADA}}** — a oferta que os afiliados promovem (vem do [`offer-book-master`](../core/offer-book-master.md)).
- **{{PROVA_CONVERSAO_PROPRIA}}** — a taxa de conversão da sua própria lista, usada como prova no recrutamento. Sem ela, não recrute.
- **{{COMISSAO_PCT}}** / **{{COMISSAO_BASE}}** — o percentual e sobre o quê incide (núcleo, núcleo+upsell). Cruze com o `money-model-sequence` para confirmar que a venda do afiliado liquida o custo.
- **{{COOKIE_ATRIBUICAO}}** — a janela de atribuição do link rastreado (ex.: 30 dias, último clique).
- **{{JANELA_PROMOCAO}}** — as datas de início e fim em que todos os parceiros enviam, alinhadas ao [`cart-open-close`](../../frameworks/launch/cart-open-close.md). Todos fecham no mesmo deadline real.
- **{{DREAM_100}}** — a lista priorizada de parceiros por fit + tamanho + confiança. Quem tem a audiência mais aderente entra primeiro.
- **{{REGRAS_E_LIMITES}}** — o que o afiliado pode e não pode dizer. Claim sem lastro feito por afiliado também é veto do `compliance-auditor`. Define proibições (spam, bid em marca, claim falso).
- **{{ESTRUTURA_PREMIOS}}** — o resumo das faixas de prêmio (detalhe na planilha [`affiliate-prizes-template`](affiliate-prizes-template.csv)).
- **{{PAGAMENTO}}** — quando e como a comissão é paga (prazo, método, janela de estorno/refund).
- **{{STATUS}}** — o estado do programa: rascunho, recrutando, ativo, encerrado.

## O Template
```
# PROGRAMA DE AFILIADOS — {{NOME_DO_PROGRAMA}}
Owner: affiliate-program-architect · Data: {{DATA}} · Status: {{STATUS}}

## 1. OFERTA & PROVA
Oferta vinculada: {{OFERTA_VINCULADA}}
Conversão da lista própria (prova de recrutamento): {{PROVA_CONVERSAO_PROPRIA}}
Big Idea única (mensagem comum): {{BIG_IDEA}}

## 2. ECONOMIA DO AFILIADO
Comissão: {{COMISSAO_PCT}} sobre {{COMISSAO_BASE}}
Janela de atribuição (cookie): {{COOKIE_ATRIBUICAO}}
A venda do afiliado liquida o custo? {{SIM/NAO}} — como: {{COMO_FECHA_A_ECONOMIA}}

## 3. JANELA & CALENDÁRIO
Abertura: {{DATA_ABERTURA}} · Fechamento: {{DATA_FECHAMENTO}}
Deadline real e único para todos: {{DEADLINE}}
Motivo honesto do limite: {{MOTIVO_ESCASSEZ}}

## 4. DREAM 100 (parceiros priorizados)
| # | Parceiro | Audiência | Tamanho | Fit | Confiança | Status |
|---|----------|-----------|---------|-----|-----------|--------|
| 1 | {{PARCEIRO_1}} | {{AUDIENCIA_1}} | {{TAMANHO_1}} | {{FIT_1}} | {{CONFIANCA_1}} | {{STATUS_1}} |
| 2 | {{PARCEIRO_2}} | {{AUDIENCIA_2}} | {{TAMANHO_2}} | {{FIT_2}} | {{CONFIANCA_2}} | {{STATUS_2}} |

## 5. REGRAS & LIMITES (compliance)
Pode dizer: {{O_QUE_PODE}}
Não pode dizer: {{O_QUE_NAO_PODE}}
Proibições: {{SPAM_BID_MARCA_CLAIM_FALSO}}

## 6. PRÊMIOS (resumo; detalhe na planilha)
{{ESTRUTURA_PREMIOS}}
Planilha: growth/affiliate-prizes-template.csv

## 7. PAGAMENTO
Prazo: {{PRAZO_PAGAMENTO}} · Método: {{METODO}} · Janela de estorno: {{REFUND_HOLD}}
```

## Exemplo preenchido
> **# PROGRAMA DE AFILIADOS — Exército do Motor 72h**
> Owner: affiliate-program-architect · Data: 2026-06-02 · Status: recrutando
>
> **1. OFERTA & PROVA** — Oferta: Motor de Recuperação 72h (R$497). Conversão da lista própria: **6,2%**. Big Idea: *"A janela de 72 horas que devolve o lucro que seu checkout esconde."*
> **2. ECONOMIA** — Comissão: **40%** sobre núcleo+upsell. Cookie: **30 dias, último clique**. Liquida o custo? **Sim** — o upsell de gestão mensal paga a comissão e ainda sobra margem.
> **3. JANELA** — Abertura: terça 03/06 · Fechamento: sábado 07/06. Deadline único: **sábado 23h59**. Motivo honesto: a turma tem **40 vagas** por capacidade real de setup feito-para-você.
> **4. DREAM 100** — 1. *Loja em Foco* (donos de e-commerce, 28k, fit alto, confiança alta, confirmado); 2. *Métricas que Vendem* (gestores de tráfego, 15k, fit alto, confiança média, convidado).
> **5. REGRAS** — Pode dizer: mediana +21% em 142 lojas (com link à prova). Não pode dizer: "ganho garantido" sem o "ou seu dinheiro de volta". Proibições: spam, bid no nome da marca, claim sem lastro.
> **6. PRÊMIOS** — Faixas Bronze/Prata/Ouro por meta de vendas; top 3 ganham viagem. Detalhe na planilha.
> **7. PAGAMENTO** — Prazo: **D+45** (após janela de refund). Método: PIX/transferência. Janela de estorno: **30 dias**.

## DoD do entregável
O programa está pronto quando: (1) os 7 blocos estão preenchidos, sem `{{PLACEHOLDER}}` solto; (2) a oferta já converte na lista própria e a prova de conversão está declarada; (3) a comissão tem percentual e base, e a economia do afiliado **fecha** com o [`money-model-sequence`](../../frameworks/money-model-sequence.md) (a venda liquida o custo); (4) a janela tem abertura, fechamento e um **deadline único e real** para todos, com motivo honesto (`truthful_scarcity`); (5) o Dream 100 está priorizado por fit + tamanho + confiança; (6) as regras de claim estão escritas e nenhum afiliado pode fazer claim sem lastro (alinhado ao `compliance-auditor`); (7) os prêmios remetem à planilha [`affiliate-prizes-template`](affiliate-prizes-template.csv) e o pagamento tem prazo, método e janela de estorno. Só então o programa segue para o [`affiliate-blackbook-template`](affiliate-blackbook-template.md) (o material que arma o parceiro) e passa no [`affiliate-program-checklist`](../../checklists/affiliate-program-checklist.md).
