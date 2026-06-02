---
id: task.copy.write-vsl-webinar
title: "Task — Escrever VSL & Webinar"
type: task
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes:
  - artifact.offer-book
  - artifact.big-idea
  - artifact.positioning
  - decision.lead-type-locked
  - artifact.mechanism-sheet
  - artifact.value-equation
  - artifact.offer-stack
  - artifact.guarantee
  - data.registry.proof
  - data.registry.objection
produces:
  - artifact.vsl-script
  - artifact.webinar-script
  - artifact.recap-vsl
  - artifact.sales-letter
  - artifact.ty-page-scripts
frameworks: [copy/vsl-structure, copy/pastor, copy/pas, copy/slippery-slide, launch/perfect-webinar]
checklists:
  - offer-book-stack/offer-book-dod-gate
  - vsl/vsl-value-before-price-gate
  - vsl/vsl-risk-reversal-gate
  - vsl/vsl-cta-strength-gate
registries: [control-registry]
metrics: [vsl_conversion_rate, cart_close_lift, copy_throughput]
tags: [copy, vsl, webinar, sales-letter, ty-page, value-before-price, hard-stop]
---

# Task — Escrever VSL & Webinar

## Objetivo
Transformar o Offer Book aprovado em roteiros de longo formato — VSL, webinar, recap VSL, sales letter/offer page e TY page scripts — que entregam **valor antes do preço**, deslizam do gancho ao CTA único e estão prontos para o passe de voz. O estado-pronto: roteiros com os 3 blocos completos, cada claim com prova linkada, escassez verdadeira, aprovados nos gates de VSL e encaminhados ao [`voice-style-guardian`](voice-pass.md).

## Agente dono
[`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md). Sem poder de veto; submete tudo ao voice-guardian.

## Gatilho / Quando
**HARD STOP: esta task de copy (D4) só ativa APÓS o [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) estar APROVADO.** Conforme `config.yaml: defaults.hard_stop_before_copy: true` e o `ARCHITECTURE.md`, nenhuma palavra de copy nasce antes de o Offer Book passar no Definition of Done. Se o gate está vermelho, o agente **recusa** e devolve ao [`offerbook-chief`](../../agents/offerbook-chief.md). Demais gatilhos: pedido de VSL/webinar/recap/sales letter/TY page, com a camada D3 fechada (Big Idea + posição + **lead travados**).

## Inputs (Consome)
- `artifact.offer-book` — o pacote estratégico aprovado (fonte de verdade).
- `artifact.big-idea` — promessa, gancho, vilão, consciência-alvo (o fio condutor).
- `artifact.positioning` + `decision.lead-type-locked` — a categoria e o **lead travado** (define a abertura).
- `artifact.mechanism-sheet` — o mecanismo único em uma frase.
- `artifact.value-equation` + `artifact.offer-stack` + `artifact.guarantee` — sonho, alavancas, componentes a empilhar, reversão de risco.
- [`data.registry.proof`](../../data/registries/proof-registry.md) — prova por claim. **Nenhum claim sem prova linkada.**
- [`data.registry.objection`](../../data/registries/objection-registry.md) — objeções por nível de consciência.

## Procedimento
1. **Verificar o HARD STOP.** Confirmar o `offer-book-dod-gate` verde. Vermelho → recusar e devolver ao chief.
2. **Carregar inputs e travar a abertura.** Ler offer-book, big-idea, lead travado. O lead define o Bloco 1; não invente a abertura — se o lead não está travado, devolver ao [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md).
3. **Decompor em 3 blocos (H-Module).** Bloco 1 — Gancho & Promessa (lead); Bloco 2 — Conteúdo & Mecanismo (quebra/reconstrói crenças, deposita prova); Bloco 3 — Oferta & Fechamento (value stack → preço ancorado → garantia → escassez real → CTA único).
4. **Gerar a abertura (ToT).** Produzir ≥3 ganchos para o Bloco 1; pontuar por scroll-stop, congruência com a Big Idea e velocidade até a recompensa. Podar o que demora ou trai a tese.
5. **Sequenciar a quebra de crença (Bloco 2).** Ordenar as objeções do `objection-registry` pela crença-raiz que destrava as demais. Para cada claim, ancorar a prova do `proof-registry` **junto** (proof-to-claim). Claim sem prova → marcar `[PROVA PENDENTE]` e escalar ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md).
6. **Empilhar o fechamento (Bloco 3).** Listar o value stack item a item, somar o valor total, **só então** revelar o preço (ancoragem), depois a garantia (reversão) e a escassez **verdadeira**. Nenhum preço pode aparecer antes do Bloco 3.
7. **Aplicar a slippery slide.** Ao fim de cada beat, perguntar "isto faz querer o próximo?". Cortar/reescrever todo trecho que faz parar; usar open loops e transições.
8. **Gerar variantes de formato.** VSL/sales letter via [`copy/vsl-structure`](../../frameworks/copy/vsl-structure.md); webinar via [`launch/perfect-webinar`](../../frameworks/launch/perfect-webinar.md); recap VSL abrindo direto pela oferta para quem não ficou até o fim.
9. **Self-verify (Bloom + red-team).** Antecipar o veto do compliance (claim sem lastro, escassez falsa, garantia impossível) e do voice-guardian (frase longa, advérbio, voz passiva). Corrigir antes de emitir.
10. **Registrar e encaminhar.** Logar no `control-registry` como `draft` e entregar ao voice-pass. Máximo de 2 passes de reescrita antes de escalar ao chief.

## Frameworks
[`copy/vsl-structure`](../../frameworks/copy/vsl-structure.md) · [`launch/perfect-webinar`](../../frameworks/launch/perfect-webinar.md) · [`copy/pas`](../../frameworks/copy/pas.md) · [`copy/pastor`](../../frameworks/copy/pastor.md) · [`copy/slippery-slide`](../../frameworks/copy/slippery-slide.md).

## Outputs (Produz)
- `artifact.vsl-script`, `artifact.webinar-script`, `artifact.recap-vsl`, `artifact.sales-letter`, `artifact.ty-page-scripts` (templates em [`copy/vsl-webinar-script-template`](../../templates/copy/vsl-webinar-script-template.md), [`copy/sales-letter-offer-page-template`](../../templates/copy/sales-letter-offer-page-template.md), [`copy/recap-vsl-template`](../../templates/copy/recap-vsl-template.md), [`copy/ty-page-scripts-template`](../../templates/copy/ty-page-scripts-template.md)).
- [`control-registry`](../../data/registries/control-registry.md) atualizado com cada roteiro (`asset_id`, blocos, claims usados, objeções destruídas, `value_before_price: true`, `risk_reversal`, `cta_unico`, `status: draft`).

## Definition of Done
- HARD STOP verde (offer-book-dod-gate aprovado) **antes** de qualquer linha.
- Os 3 blocos presentes; mecanismo no Bloco 2; value stack no Bloco 3.
- Nenhum preço aparece antes do valor (Bloco 3); cada claim tem prova linkada (zero `[PROVA PENDENTE]` no estado final).
- Escassez verdadeira; risco revertido; CTA **único**.
- Slippery slide sem freio; os três gates de VSL verdes.
- Roteiro registrado no `control-registry` e encaminhado ao voice-pass.

## Gates
[`vsl/vsl-value-before-price-gate`](../../checklists/vsl/vsl-value-before-price-gate.md) · [`vsl/vsl-risk-reversal-gate`](../../checklists/vsl/vsl-risk-reversal-gate.md) · [`vsl/vsl-cta-strength-gate`](../../checklists/vsl/vsl-cta-strength-gate.md). Gate de entrada (HARD STOP): [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).

## Métricas
Move KPIs da família **conversion** ([`config.yaml`](../../config.yaml) `kpis:`), por ser a peça de venda de longo formato:
- **`vsl_conversion_rate`** — esta task **é** a fonte direta do KPI (vendas / espectadores VSL): o roteiro com valor antes do preço, slippery slide e CTA único é o que converte o espectador.
- **`cart_close_lift`** — o recap VSL e a sales letter no fechamento puxam o lift na janela de fechamento.
- **`copy_throughput`** — cada roteiro aprovado e registrado conta na vazão de copy da semana.
Acompanhamento no [`kpi-dashboard-template`](../../data/metrics/kpi-dashboard-template.md) (família conversion), com cada roteiro versionado em [`control-registry`](../../data/registries/control-registry.md).

## Handoff
**Próxima task:** [`voice-pass`](voice-pass.md) (passe obrigatório do voice-style-guardian). **Contrato de saída:** cada roteiro entregue tem os 3 blocos, valor antes do preço, risco revertido, CTA único e cada claim linkado a prova — pronto para o guardião e, após o veredito APROVADO, para o [`funnel-architect`](../funnel-tech/map-funnel.md) (scripts → páginas) e o [`launch-producer`](../ops/build-run-of-show.md) (webinar → run-of-show).
