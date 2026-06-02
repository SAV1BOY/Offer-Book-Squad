---
id: task.ops.build-launch-memo
title: "Task — Construir o Launch Memo & as Fases"
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
produces:
  - artifact.launch-memo
  - artifact.launch-phases
frameworks: [launch/product-launch-formula, launch/runway-and-phases]
checklists:
  - launch/launch-phase-readiness-gate
registries: [decision-registry]
metrics: [cart_close_lift, time_to_blackbook, compliance_pass_rate]
tags: [ops, launch, memo, phases, plf, runway, datas-ancora, d6]
---

# Task — Construir o launch memo & as fases: a tese do lançamento, as datas-âncora e a pista I–VIII

## Objetivo
Converter a estratégia aprovada (Offer Book + copy + funil) na fundação do lançamento: o **launch memo** (tese, datas-âncora, metas, papéis) e as **Fases I–VIII** (do aquecimento ao pós-venda), na ordem que constrói desejo antes de pedir o dinheiro. O estado-pronto: memo + pista de fases com cada fase nomeada, datada e com dono e ativo, respeitando a espinha do money model — aprovado no gate de prontidão de fases, pronto para virar run-of-show.

## Agente dono
[`launch-producer`](../../agents/launch-producer.md). O diretor de palco do lançamento; sequencia e fasea, não escreve copy nem desenha oferta. Sem poder de veto, mas recusa construir sobre fundação podre.

## Gatilho / Quando
Roda em D6, **nunca antes**: ativa quando o Offer Book passou no `offer-book-stack/offer-book-dod-gate` **e** a camada D4 (copy) e D5 (funil/tech) entregaram seus artefatos. Demais gatilhos: pedido de launch memo + plano de fases para uma promoção com data. Copy ou funil não prontos → **não montar** as fases; devolver ao [`offerbook-chief`](../../agents/offerbook-chief.md) com o que falta. **Sem money model não sequencia** — sem a espinha, a pista seria uma agenda de eventos avulsos.

## Inputs (Consome)
- `artifact.offer-book` — a Big Idea travada, a oferta núcleo, a promessa, a janela pretendida e os ativos de prova a distribuir ao longo das fases.
- `artifact.money-model` — a sequência da escada e **a ordem** em que cada degrau aparece ao público (a espinha das fases).
- `artifact.funnel-map` — as páginas por degrau e onde mora cada CTA (a pista coreografa o tráfego por esse mapa).
- `artifact.tech-deliverability-plan` — capacidade, janelas de envio, limites de deliverability e URLs canônicas (os limites físicos do plano).
- `artifact.vsl-webinar-script` + `artifact.email-sms-sequences` — as peças prontas a **encaixar** nas fases (o produtor agenda, não cria).

## Procedimento
1. **Confirmar as pré-condições.** Offer Book DoD verde; copy e funil entregues; money model presente. Se falta, recusar/devolver conforme o gatilho.
2. **Escrever o launch memo.** A tese do lançamento em uma frase, as datas-âncora (pré-lançamento, carrinho abre, carrinho fecha), a meta (receita/vendas/aplicações) e os papéis (quem faz o quê).
3. **Escolher a arquitetura (ToT).** Gerar ≥3 formatos — PLF clássico, perfect-webinar, challenge — e pontuar por fit com a oferta (preço/complexidade), aderência do avatar, carga operacional, construção de desejo e risco de execução. Podar os de Fit ou Carga baixos; empate desempata por menor risco.
4. **Desenhar a pista de fases.** Aplicar [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md) e [`launch/product-launch-formula`](../../frameworks/launch/product-launch-formula.md): Fase I–II aquecimento (valor + objeção→resposta), III evento de venda, IV abertura de carrinho, V–VII prova/objeção/escassez/fechamento, VIII pós-venda + downsell. Encaixar cada e-mail/VSL pronto na fase certa.
5. **Respeitar a espinha do money model.** A venda do core vem **depois** da prova; a atração precede o core; o upsell ascende logo após a compra. A ordem das fases segue a ordem da escada.
6. **Atribuir dono e ativo por fase.** Cada fase tem responsável e os ativos (e-mail, live, página) que a sustentam. Fase sem ativo pronto → marcar `bloqueado por <input>`.
7. **Validar a escassez planejada.** A escassez de cada fase (deadline, vagas) **tem de ser real**. Escassez falsa → **não agendar** e sinalizar ao [`compliance-auditor`](../../agents/compliance-auditor.md).
8. **Self-verify (Bloom + red-team).** As fases estão na ordem que constrói desejo? Cada fase tem dono + ativo? A espinha é respeitada? Antecipar o veto de escassez do compliance.
9. **Registrar e entregar.** Logar a decisão de formato (alternativas podadas, motivo, trade-off) no `decision-registry`. Entregar o memo + fases à task de run-of-show. Máximo de 2 ciclos antes de escalar ao chief.

## Frameworks
[`launch/product-launch-formula`](../../frameworks/launch/product-launch-formula.md) · [`launch/runway-and-phases`](../../frameworks/launch/runway-and-phases.md).

## Outputs (Produz)
- `artifact.launch-memo` (template em [`ops/launch-memo-template`](../../templates/ops/launch-memo-template.md)) — tese, datas-âncora, meta, papéis.
- `artifact.launch-phases` (template em [`ops/launch-phases-template`](../../templates/ops/launch-phases-template.md)) — Fases I–VIII com ativos, datas e donos.
- [`decision-registry`](../../data/registries/decision-registry.md) atualizado com a escolha de formato e as datas-âncora das fases.

## Definition of Done
- Offer Book DoD verde; copy e funil entregues; money model presente — confirmados antes de sequenciar.
- Launch memo com tese, datas-âncora, meta e papéis.
- Fases I–VIII na ordem que constrói desejo, respeitando a espinha do money model; cada fase com dono e ativo.
- Toda escassez planejada é real (zero deadline/vaga falsos); o gate de prontidão de fases verde.
- Formato e datas registrados no `decision-registry`; memo + fases prontos para o run-of-show.

## Gates
[`launch/launch-phase-readiness-gate`](../../checklists/launch/launch-phase-readiness-gate.md).

## Métricas
Move KPIs de **conversion**, **efficiency** e **operational** ([`config.yaml`](../../config.yaml) `kpis:`), por sequenciar o desejo antes de pedir o dinheiro:
- **`cart_close_lift`** — as datas-âncora (abre/fecha) e as Fases V–VII (prova/objeção/escassez/fechamento) na ordem que constrói desejo são o que arma o lift da janela de fechamento.
- **`time_to_blackbook`** — o launch memo + as fases são um marco do caminho até o Blackbook completo; sequenciar sobre fundação pronta evita retrabalho.
- **`compliance_pass_rate`** — agendar só escassez real (zero deadline/vaga falsos) protege as fases do veto de compliance.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md), com o formato e as datas-âncora em [`decision-registry`](../../data/registries/decision-registry.md).

## Handoff
**Próxima task:** [`build-run-of-show`](build-run-of-show.md) — mesmo dono [`launch-producer`](../../agents/launch-producer.md). **Contrato:** o run-of-show recebe o launch memo (datas-âncora, meta) e as Fases I–VIII (ordem, donos, ativos) para detalhar a janela crítica minuto a minuto, o sales-flow e o plano de surge. **Garantia:** a pista respeita a espinha do money model, cada fase tem dono e ativo, e nenhuma fase carrega escassez falsa — a base sobre a qual o run-of-show coreografa o dia.
