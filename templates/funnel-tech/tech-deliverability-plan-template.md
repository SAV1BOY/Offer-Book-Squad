---
id: template.funnel-tech.tech-deliverability-plan
title: "Plano Técnico & de Entregabilidade — Caixa de Entrada, Domínio e Pico"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: tech-links-deliverability-engineer
consumes: [template.funnel-tech.links-urls, template.funnel-tech.funnel-map, template.ops.run-of-show]
produces: [template.ops.launch-memo]
frameworks: [launch/surge-ops, launch/cart-open-close]
checklists: [tech/tech-deliverability-gate, launch/launch-fallback-gate]
registries: [decision-registry]
tags: [template, deliverability, email, dns, spf, dkim, dmarc, surge, fallback, funnel-tech]
---

# Plano Técnico & de Entregabilidade — Caixa de Entrada, Domínio e Pico

A malha de [`links-urls`](links-urls-template.md) só vale se os e-mails **chegam à caixa de entrada** e as páginas **aguentam o pico** do carrinho. Este template é o plano técnico que prova as duas coisas: autenticação de domínio (SPF, DKIM, DMARC), reputação e aquecimento de envio, capacidade de infraestrutura nos horários de pico e um plano de fallback para quando algo cai. É o segundo e último artefato do D5. Sem ele verde, o lançamento envia para spam ou derruba o checkout no momento da maior venda.

## Como usar
- **Agente dono:** `tech-links-deliverability-engineer`. Roda na task `plan-tech-deliverability`, em paralelo com a montagem do run-of-show.
- **Inputs:** o [`links-urls`](links-urls-template.md) (domínios e links que precisam entregar), o [`funnel-map`](funnel-map-template.md) (os picos de tráfego por página) e o [`run-of-show`](../ops/run-of-show-template.csv) (os horários de disparo de e-mail e abertura de carrinho). O plano de pico vem do [`surge-ops`](../../frameworks/launch/surge-ops.md).
- **Quando:** abre quando os links estão definidos e fecha quando autenticação, aquecimento e fallback estão verdes — **antes** da janela de carrinho abrir. Aquecimento de domínio leva dias, então este plano começa cedo.
- **Saída:** preencha os cinco blocos (domínio & autenticação, reputação & aquecimento, capacidade & pico, monitoramento, fallback). Vira insumo do [`launch-memo`](../ops/launch-memo-template.md), que comunica prontidão técnica ao time. Bloco vazio = risco técnico não coberto = [`tech-deliverability-gate`](../../checklists/tech/tech-deliverability-gate.md) ou [`launch-fallback-gate`](../../checklists/launch/launch-fallback-gate.md) vermelhos.

## Campos & Instruções
- **{{DOMINIO_ENVIO}}** — o domínio (ou subdomínio) que dispara os e-mails do lançamento (ex.: `news.minhamarca.com`). Idealmente separado do domínio transacional.
- **{{SPF_STATUS}}** — se o registro SPF autoriza o servidor de envio (publicado e válido). Sim/não + o que falta.
- **{{DKIM_STATUS}}** — se o DKIM assina os e-mails (chave publicada no DNS e ativa no provedor). Sim/não.
- **{{DMARC_POLITICA}}** — a política DMARC publicada (`none`, `quarantine`, `reject`) e o e-mail de relatório (`rua`). Define como o destinatário trata falha de autenticação.
- **{{REPUTACAO_ATUAL}}** — a reputação do domínio/IP de envio hoje (ferramenta + nota). Mostra de onde o aquecimento parte.
- **{{PLANO_AQUECIMENTO}}** — a rampa de volume de envio nos dias anteriores (quantos e-mails por dia, para que segmentos), para não cair em spam ao disparar tudo de uma vez.
- **{{SEGMENTACAO_ENVIO}}** — quais listas/segmentos recebem o quê e em que ordem (engajados primeiro protege a reputação).
- **{{CAPACIDADE_PAGINA}}** — a capacidade da página de checkout e da VSL sob carga (CDN, cache, limite de requisições). Vem do [`funnel-map`](funnel-map-template.md) (onde está o pico).
- **{{JANELA_DE_PICO}}** — os horários de maior carga (abertura de carrinho, último e-mail, webinar ao vivo). Vem do [`run-of-show`](../ops/run-of-show-template.csv).
- **{{PLANO_SURGE}}** — as ações de escala no pico (escalar servidor, fila de checkout, CDN), via [`surge-ops`](../../frameworks/launch/surge-ops.md).
- **{{MONITORAMENTO}}** — o que é monitorado ao vivo (taxa de entrega, bounce, uptime das páginas, erro de checkout) e quem recebe o alerta.
- **{{PLANO_FALLBACK}}** — o que fazer se algo cai: link reserva, página espelho, troca de provedor de e-mail, mensagem de status. Cada falha provável tem uma resposta.
- **{{RESPONSAVEL_TECNICO}}** — quem está de plantão na janela e como é acionado.

## O Template
```
# PLANO TÉCNICO & DE ENTREGABILIDADE — {{NOME_DO_LANCAMENTO}}
Owner: tech-links-deliverability-engineer · Data: {{DATA}}
Janela de carrinho: {{CART_OPEN}} → {{CART_CLOSE}}

## 1. DOMÍNIO & AUTENTICAÇÃO
Domínio de envio: {{DOMINIO_ENVIO}}
SPF: {{SPF_STATUS}}
DKIM: {{DKIM_STATUS}}
DMARC: política {{DMARC_POLITICA}} · relatório {{DMARC_RUA}}

## 2. REPUTAÇÃO & AQUECIMENTO
Reputação atual: {{REPUTACAO_ATUAL}}
Plano de aquecimento (rampa): {{PLANO_AQUECIMENTO}}
Segmentação de envio: {{SEGMENTACAO_ENVIO}}

## 3. CAPACIDADE & PICO  (framework: surge-ops)
Páginas críticas sob carga: {{CAPACIDADE_PAGINA}}
Janela(s) de pico: {{JANELA_DE_PICO}}
Plano de surge: {{PLANO_SURGE}}

## 4. MONITORAMENTO AO VIVO
Métricas vigiadas: {{MONITORAMENTO}}
Alertas para: {{RESPONSAVEL_TECNICO}}

## 5. PLANO DE FALLBACK
| Falha provável | Resposta | Quem aciona |
|----------------|----------|-------------|
| {{FALHA_1}} | {{RESPOSTA_1}} | {{QUEM_1}} |
| {{FALHA_2}} | {{RESPOSTA_2}} | {{QUEM_2}} |
| {{FALHA_3}} | {{RESPOSTA_3}} | {{QUEM_3}} |

## 6. STATUS DOS GATES
tech-deliverability-gate: {{STATUS}} — em {{DATA_GATE}}
launch-fallback-gate: {{STATUS}} — em {{DATA_GATE}}
```

## Exemplo preenchido
> **# PLANO TÉCNICO & DE ENTREGABILIDADE — Lançamento Motor 72h**
> Owner: tech-links-deliverability-engineer · Data: 2026-06-02
> Janela de carrinho: **e-mail #1 (seg 09h)** → **sex 23h59**.
>
> **1. DOMÍNIO & AUTENTICAÇÃO** — Domínio de envio: **news.minhaloja.com** (separado do transacional). SPF: **publicado e válido**. DKIM: **chave 2048 ativa no provedor**. DMARC: política **quarantine** · relatório **dmarc@minhaloja.com**.
> **2. REPUTAÇÃO & AQUECIMENTO** — Reputação atual: **Google Postmaster "Alta"**. Aquecimento: rampa de 7 dias (2k → 5k → 10k/dia) só para engajados dos últimos 90 dias. Segmentação: abre para engajados 30d, depois 90d, frios ficam fora até o meio da semana.
> **3. CAPACIDADE & PICO** — Páginas críticas: VSL e checkout atrás de CDN com cache de estáticos; checkout com fila nativa do gateway. Picos: seg 09h (abertura), sex 20h–23h59 (fechamento). Surge: autoescala do servidor de páginas para 3x, CDN com burst, fila de checkout ligada às 20h de sexta.
> **4. MONITORAMENTO** — Vigiados: taxa de entrega, bounce, uptime VSL/checkout, erro de pagamento. Alertas via Slack para o plantão técnico.
> **5. FALLBACK** — 1. Checkout cai → link reserva para checkout espelho no gateway B · plantão técnico. 2. E-mail marcado como spam em massa → pausar envio, trocar para IP de backup, reenviar só engajados · engenheiro de entregabilidade. 3. VSL fora do ar → página espelho estática com mesmo CTA · plantão técnico.
> **6. STATUS** — tech-deliverability-gate: **VERDE** — 2026-06-02. launch-fallback-gate: **VERDE** — 2026-06-02.

## DoD do entregável
O Plano Técnico & de Entregabilidade está pronto quando: (1) o domínio de envio tem **SPF, DKIM e DMARC** publicados e válidos, sem `{{PLACEHOLDER}}` solto, e a política DMARC está declarada com e-mail de relatório; (2) existe um plano de aquecimento em rampa e uma segmentação que envia primeiro aos engajados, protegendo a reputação antes do disparo grande; (3) as páginas críticas (VSL, checkout) têm capacidade conhecida sob carga e um plano de surge alinhado ao [`surge-ops`](../../frameworks/launch/surge-ops.md) para as janelas de pico vindas do [`run-of-show`](../ops/run-of-show-template.csv); (4) o monitoramento ao vivo cobre entrega, bounce, uptime e erro de checkout, com alerta indo para um responsável nomeado; (5) o plano de fallback lista cada falha provável com uma resposta e um responsável — sem isso o [`launch-fallback-gate`](../../checklists/launch/launch-fallback-gate.md) reprova; (6) os dois gates ficam verdes **antes** de o carrinho abrir, satisfazendo o [`tech-deliverability-gate`](../../checklists/tech/tech-deliverability-gate.md). Só então o plano vira insumo do [`launch-memo`](../ops/launch-memo-template.md), que declara prontidão técnica ao time de ops.
