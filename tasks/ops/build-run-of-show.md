---
id: task.ops.build-run-of-show
title: "Task — Construir o Run-of-Show & o Sales-Flow"
type: task
layer: D6
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
consumes:
  - artifact.offer-book
  - artifact.money-model
  - artifact.funnel-map
  - artifact.tech-deliverability-plan
  - artifact.vsl-webinar-script
  - artifact.email-sms-sequences
  - artifact.launch-memo
  - artifact.launch-phases
produces:
  - artifact.run-of-show
  - artifact.sales-flow
frameworks: [launch/product-launch-formula, launch/runway-and-phases, launch/surge-ops]
checklists:
  - launch/launch-phase-readiness-gate
  - launch/launch-surge-gate
registries: [decision-registry]
metrics: [cart_close_lift, compliance_pass_rate, time_to_blackbook]
tags: [ops, launch, run-of-show, sales-flow, surge, war-room, cart-open-close, d6]
---

# Task — Construir o run-of-show & o sales-flow: a janela crítica minuto a minuto, com dono, horário e fallback

## Objetivo
Transformar o launch memo e as fases num run-of-show executável — onde cada e-mail, cada abertura de live, cada virada de página e cada gatilho de escassez tem **dono, horário e fallback** — mais o sales-flow (a vazão de vendas) e o plano de surge (a operação de pico). O estado-pronto: run-of-show minuto a minuto da janela crítica (abertura → fechamento de carrinho) + sales-flow + surge plan com capacidade confirmada e plano B, e zero escassez não-lastreada — aprovado nos gates de prontidão de fases e de surge.

## Agente dono
[`launch-producer`](../../agents/launch-producer.md). Sequencia, agenda, coreografa e blinda contra o caos do dia. Sem poder de veto, mas recusa agendar disparos de peças inexistentes e escassez falsa.

## Gatilho / Quando
Roda em D6, **depois** de [`build-launch-memo`](build-launch-memo.md): ativa quando o memo + as Fases I–VIII existem e o Offer Book DoD está verde com copy (D4) e funil/tech (D5) entregues. Demais gatilhos: ajuste de calendário/janela de carrinho ou plano de pico para um lançamento já desenhado. Carrinho que abriria sem o e-mail de fechamento pronto → **recusar** e escalar (queima a janela de urgência). `tech-deliverability-plan` que não confirma capacidade para o pico → **escalar** ao chief e ao [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) antes de marcar a data.

## Inputs (Consome)
- `artifact.launch-memo` + `artifact.launch-phases` — a tese, as datas-âncora e a pista I–VIII a detalhar.
- `artifact.money-model` — a ordem da escada que o sales-flow executa (atração antes do core; upsell logo após a compra).
- `artifact.funnel-map` — as páginas e transições que o run-of-show coreografa.
- `artifact.tech-deliverability-plan` — capacidade de carga, janelas de envio, URLs canônicas e fallbacks técnicos (os limites do plano de pico).
- `artifact.vsl-webinar-script` + `artifact.email-sms-sequences` — as peças a **agendar** (quando a VSL/webinar vai ao ar, quando cada e-mail dispara).

## Procedimento
1. **Confirmar a fundação.** Memo + fases prontos; copy e funil entregues; capacidade técnica confirmada. Se falta, recusar/escalar conforme o gatilho.
2. **Detalhar o run-of-show da janela crítica.** Para cada disparo da abertura ao fechamento de carrinho, cravar `<HH:MM> — ação — dono — fallback`. Encaixar cada e-mail/SMS/live da sequência no minuto certo.
3. **Coreografar o sales-flow.** As ondas de venda e os gatilhos de escassez **verdadeiros** por fase, aplicando a mecânica de [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md) (transitiva via PLF) e a sequência da escada.
4. **Escolher a janela de carrinho (ToT).** Gerar ≥3 janelas (4 dias com cadência crescente, 7 dias, flash de 48h) e pontuar por urgência verdadeira sustentável, fadiga de lista, receita projetada e fôlego de suporte. Podar a que cria urgência que não se consegue honrar.
5. **Planejar o surge.** Aplicar [`launch/surge-ops`](../../frameworks/launch/surge-ops.md): checar a capacidade no `tech-deliverability-plan`, definir o war-room (quem monitora pagamento, deliverability, suporte) e os fallbacks (página espelho, link de pagamento reserva, e-mail de "deadline estendido por instabilidade" **só se a instabilidade for real**).
6. **Cravar o pico minuto a minuto.** A última noite do fechamento: e-mail de "horas restantes", SMS de "fecha à meia-noite", "últimos minutos", fechamento **real** no horário. Definir o teto de tráfego e o gatilho de fallback.
7. **Checar colisões e fadiga.** Nenhum buraco na linha do tempo; nenhum gatilho colidindo no mesmo minuto; cadência de fechamento que não estoura o limite de envio (redistribuir com o tech-engineer se preciso).
8. **Self-verify (Bloom + red-team).** Cada disparo tem dono + horário + fallback? A escassez agendada é 100% real? O pico tem capacidade confirmada e plano B? Antecipar o veto de escassez do [`compliance-auditor`](../../agents/compliance-auditor.md) (deadline que se renova, "últimas vagas" sem limite real) e corrigir antes de emitir.
9. **Registrar e entregar.** Logar a decisão de janela/cadência e o plano de fallback do pico no `decision-registry`. Cravar os handoffs para eventos, afiliados, PR e compliance. Máximo de 2 ciclos antes de escalar ao chief.

## Frameworks
[`launch/product-launch-formula`](../../frameworks/launch/product-launch-formula.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md) · [`launch/surge-ops`](../../frameworks/launch/surge-ops.md) · (transitivo) [`launch/cart-open-close`](../../frameworks/launch/cart-open-close.md).

## Outputs (Produz)
- `artifact.run-of-show` (template em [`ops/run-of-show-template`](../../templates/ops/run-of-show-template.md)) — janela crítica minuto a minuto, cada linha com ação, dono e fallback.
- `artifact.sales-flow` (template em [`ops/sales-flow-template`](../../templates/ops/sales-flow-template.md)) — ondas de venda + gatilhos de escassez verdadeiros + picos.
- [`decision-registry`](../../data/registries/decision-registry.md) atualizado com a janela/cadência de carrinho e o plano de fallback do pico. Lições de execução seguem ao [`knowledge-librarian`](../../agents/knowledge-librarian.md).

## Definition of Done
- Memo + fases + capacidade técnica confirmados antes de cravar horários.
- Run-of-show da janela crítica minuto a minuto: **cada** disparo com dono + horário + fallback.
- Sales-flow com ondas e gatilhos de escassez **100% verdadeiros**.
- Surge plan com capacidade confirmada (Nx tráfego médio), war-room e fallbacks (página espelho, link reserva).
- Sem buraco/colisão na linha do tempo; cadência dentro do limite de envio.
- Os gates de prontidão de fases e de surge verdes; decisões registradas; handoffs cravados.

## Gates
[`launch/launch-phase-readiness-gate`](../../checklists/launch/launch-phase-readiness-gate.md) · [`launch/launch-surge-gate`](../../checklists/launch/launch-surge-gate.md).

## Métricas
Move KPIs de **conversion**, **operational** e **efficiency** ([`config.yaml`](../../config.yaml) `kpis:`), por coreografar a janela crítica minuto a minuto:
- **`cart_close_lift`** — o sales-flow do fechamento (e-mail de "horas restantes", SMS de "fecha à meia-noite", fechamento real no horário) é o disparo direto do lift da janela de fechamento.
- **`compliance_pass_rate`** — gatilhos de escassez **100% verdadeiros** (deadline que não se renova, vagas com limite real) protegem o run-of-show do veto de escassez.
- **`time_to_blackbook`** — capacidade de surge confirmada e fallbacks testados evitam o caos do dia que vira retrabalho e atrasa o Blackbook.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md), com a janela/cadência e o plano de fallback em [`decision-registry`](../../data/registries/decision-registry.md).

## Handoff
**Próxima task:** [`build-events-logistics`](build-events-logistics.md) — dono [`events-logistics-coordinator`](../../agents/events-logistics-coordinator.md). **Contrato:** o coordenador recebe o run-of-show com datas e fallbacks para operacionalizar a logística (salas, links, ensaios, fulfillment). Também entrega ao [`affiliate-program-architect`](../growth/build-affiliate-program.md) as janelas em que afiliados entram na sequência, ao [`pr-brand-strategist`](../growth/build-pr-plan.md) os marcos de PR alinhados às fases, e ao [`compliance-auditor`](../qa-memory/compliance-audit.md) o run-of-show para auditoria de escassez/urgência. **Garantia:** um calendário datado, com fases nomeadas, donos atribuídos, gatilhos de escassez **verdadeiros** e fallbacks definidos — ninguém precisa adivinhar "quando" ou "quem".
