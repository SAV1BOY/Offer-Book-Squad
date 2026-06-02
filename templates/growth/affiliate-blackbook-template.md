---
id: template.growth.affiliate-blackbook
title: "Affiliate Blackbook — O Kit que Arma o Parceiro (Swipe, Datas, Links, Prêmios)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
consumes: [template.growth.affiliate-program, template.growth.affiliate-prizes, template.core.offer-book-master, template.core.launch-blackbook-skeleton]
produces: [data.registry.decision]
frameworks: [launch/affiliate-army, launch/cart-open-close, launch/runway-and-phases, money-model-sequence]
checklists: [affiliate/affiliate-program-checklist]
registries: [decision-registry, control-registry]
tags: [template, affiliate, blackbook, swipe, promo-pack, leaderboard, growth]
---

# Affiliate Blackbook — O Kit que Arma o Parceiro

O programa de afiliados diz **quem** promove e **quanto** paga. Este Blackbook entrega o **como**: o kit pronto que o parceiro copia, cola e envia. Um afiliado armado não escreve do zero — ele aperta um botão. Quanto menos esforço você pede, mais parceiros enviam, e maior o pico. O Blackbook reúne em um só lugar a Big Idea única, o swipe aprovado, o calendário de envios, os links rastreados e o placar de prêmios. Tudo aqui passou pelo `voice-style-guardian` e pelo `compliance-auditor` **antes** de chegar à mão do parceiro. Claim sem lastro que um afiliado dispara é veto seu, não dele — então o kit já vem com a prova ao lado de cada afirmação (`evidence_before_opinion`). A escassez do kit é a mesma da oferta: real, com deadline único para todos (`truthful_scarcity`).

## Como usar
- **Agente dono:** `affiliate-program-architect`. Pareia com o `email-sms-sequence-writer` (que escreve o swipe na voz da marca), o `tech-links-deliverability-engineer` (que gera os links rastreados) e o `launch-producer` (que encaixa os envios na pista do lançamento).
- **Task:** `build-affiliate-program`. Roda em D6, **depois** do [`affiliate-program-template`](affiliate-program-template.md) estar verde (economia e regras travadas) e da oferta já converter na lista própria.
- **Quando:** o arquiteto monta o Blackbook assim que o swipe é aprovado e os links existem. É o entregável que o parceiro recebe no kickoff. Ele consome o [Dream 100](../../frameworks/launch/affiliate-army.md) do programa e os prêmios da planilha [`affiliate-prizes-template`](affiliate-prizes-template.csv).
- Regra de ouro: **zero fricção**. Todo swipe vem pronto para copiar, todo link já rastreia, toda data já está no fuso do parceiro. Campo vazio = parceiro travado = veta o envio.

## Campos & Instruções
- **{{NOME_DO_LANCAMENTO}}** — o nome do lançamento ao qual este kit serve (vem do [`offer-book-master`](../core/offer-book-master.md)).
- **{{BIG_IDEA}}** — a Grande Ideia única que **todo** parceiro repete (Power of One). Uma só mensagem multiplica o sinal; várias o diluem.
- **{{PROMESSA_E_PROVA}}** — a promessa central com a prova ao lado (número + link). É o que o afiliado pode dizer com segurança.
- **{{SWIPE_EMAIL}}** — os e-mails prontos por fase (aquecimento, abertura, meio, fechamento), na voz da marca, aprovados pelo `voice-style-guardian`.
- **{{SWIPE_SOCIAL_DM}}** — posts, stories e DMs curtos para o parceiro disparar fora do e-mail.
- **{{CALENDARIO_ENVIOS}}** — a grade de quando enviar o quê, alinhada ao [`cart-open-close`](../../frameworks/launch/cart-open-close.md) e à [`runway-and-phases`](../../frameworks/launch/runway-and-phases.md). Todos fecham no mesmo deadline real.
- **{{LINKS_RASTREADOS}}** — o link único de cada parceiro (UTM + id de afiliado), gerado pelo `tech-links-deliverability-engineer`. Atribuição igual à do programa.
- **{{CRIATIVOS}}** — banners, thumbs e imagens prontas, nos tamanhos dos canais do parceiro.
- **{{REGRAS_DE_CLAIM}}** — o que pode e o que não pode dizer (copiado do programa). Reforço explícito de compliance no kit.
- **{{PLACAR_E_PREMIOS}}** — o resumo das faixas de prêmio e onde ver o placar ao vivo (detalhe na planilha [`affiliate-prizes-template`](affiliate-prizes-template.csv)).
- **{{SUPORTE_E_CONTATO}}** — o canal direto para o parceiro tirar dúvida (quem responde, em quanto tempo).
- **{{STATUS}}** — o estado do kit: rascunho, em revisão, liberado.

## O Template
```
# AFFILIATE BLACKBOOK — {{NOME_DO_LANCAMENTO}}
Owner: affiliate-program-architect · Data: {{DATA}} · Status: {{STATUS}}

## 0. A MENSAGEM ÚNICA (todos repetem)
Big Idea: {{BIG_IDEA}}
Promessa + prova: {{PROMESSA_E_PROVA}}  (link da prova: {{LINK_PROVA}})

## 1. SWIPE DE E-MAIL (copiar e colar)
Fase aquecimento: {{SWIPE_EMAIL_AQUECIMENTO}}
Fase abertura:    {{SWIPE_EMAIL_ABERTURA}}
Fase meio:        {{SWIPE_EMAIL_MEIO}}
Fase fechamento:  {{SWIPE_EMAIL_FECHAMENTO}}  (deadline real: {{DEADLINE}})

## 2. SWIPE SOCIAL & DM
Posts/stories: {{SWIPE_SOCIAL}}
DMs curtas:    {{SWIPE_DM}}

## 3. CALENDÁRIO DE ENVIOS (fuso do parceiro)
| Data/Hora | Canal | Peça | Link |
|-----------|-------|------|------|
| {{DATA_1}} | {{CANAL_1}} | {{PECA_1}} | {{LINK_1}} |
| {{DATA_2}} | {{CANAL_2}} | {{PECA_2}} | {{LINK_2}} |

## 4. LINKS RASTREADOS (um por parceiro)
Parceiro: {{PARCEIRO}} → {{LINK_RASTREADO}} (atribuição: {{COOKIE_ATRIBUICAO}})

## 5. CRIATIVOS
Banners/thumbs: {{LISTA_CRIATIVOS}}

## 6. REGRAS DE CLAIM (compliance)
Pode dizer: {{O_QUE_PODE}}
Não pode dizer: {{O_QUE_NAO_PODE}}

## 7. PLACAR & PRÊMIOS
Resumo das faixas: {{PLACAR_E_PREMIOS}}
Planilha de prêmios: growth/affiliate-prizes-template.csv
Placar ao vivo: {{LINK_PLACAR}}

## 8. SUPORTE
Canal direto: {{SUPORTE_E_CONTATO}} (resposta em {{SLA}})
```

## Exemplo preenchido
> **# AFFILIATE BLACKBOOK — Exército do Motor 72h**
> Owner: affiliate-program-architect · Data: 2026-06-02 · Status: liberado
>
> **0. MENSAGEM ÚNICA** — Big Idea: *"A janela de 72 horas que devolve o lucro que seu checkout esconde."* Promessa + prova: mediana **+21%** de receita recuperada em **142 lojas** (link: relatorio.exemplo/142-lojas).
> **1. SWIPE DE E-MAIL** — Aquecimento (seg): *"Quanto seu carrinho abandonado custou esse mês?"*. Abertura (ter): *"Abriu: o Motor que recupera em 72h."*. Meio (qui): *"As 3 fugas de lucro que ninguém te conta."*. Fechamento (sáb): *"Fecha hoje 23h59. Sem prorrogação."* (deadline real: **sáb 23h59**).
> **2. SWIPE SOCIAL & DM** — Post: print do painel de recuperação. DM: *"Te mando o link da turma que abre agora?"*.
> **3. CALENDÁRIO** — ter 9h e-mail abertura; qui 9h e-mail meio; sáb 9h + 20h e-mail fechamento; todos no fuso do parceiro.
> **4. LINKS RASTREADOS** — *Loja em Foco* → motor72h.exemplo/?ref=lojaemfoco (atribuição: 30 dias, último clique).
> **5. CRIATIVOS** — 3 banners (feed, story, e-mail) + thumb de vídeo.
> **6. REGRAS DE CLAIM** — Pode: "mediana +21% em 142 lojas (com link)". Não pode: "ganho garantido" sem a garantia de dobro do dinheiro.
> **7. PLACAR & PRÊMIOS** — Bronze/Prata/Ouro por meta; top 3 ganham viagem. Placar ao vivo: placar.exemplo/motor72h.
> **8. SUPORTE** — WhatsApp do parceiro com a equipe (resposta em até 2h em horário comercial).

## DoD do entregável
O Blackbook está pronto quando: (1) os 8 blocos estão preenchidos, sem `{{PLACEHOLDER}}` solto; (2) a **Big Idea é única** e repetida em todo swipe (Power of One) — múltiplas mensagens = reprovação; (3) cada promessa traz a **prova ao lado** com link, e o swipe passou pelo `voice-style-guardian` (voz ativa, presente, 3ª série) e pelo `compliance-auditor` (`claim_backing`); (4) o calendário de envios cobre aquecimento → abertura → meio → fechamento, alinhado ao [`cart-open-close`](../../frameworks/launch/cart-open-close.md), com um **deadline único e real** para todos (`truthful_scarcity`); (5) cada parceiro tem um **link rastreado** próprio com atribuição igual à do programa, gerado pelo `tech-links-deliverability-engineer`; (6) os criativos existem nos tamanhos dos canais; (7) as regras de claim estão escritas e o resumo de prêmios remete à planilha [`affiliate-prizes-template`](affiliate-prizes-template.csv); (8) há canal de suporte com SLA. Só então o kit vai à mão do parceiro, alimenta o [`launch-blackbook-skeleton`](../core/launch-blackbook-skeleton.md) e passa no [`affiliate-program-checklist`](../../checklists/affiliate-program-checklist.md).
