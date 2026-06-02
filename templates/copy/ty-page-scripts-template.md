---
id: template.copy.ty-page-scripts
title: "Thank-You Page Scripts — Roteiros de Pós-Conversão (Upsell, Onboarding, Indicação)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
consumes: [template.core.offer-book-master, template.offer.money-model, template.strategy.proof-bank, template.copy.vsl-webinar-script]
produces: [data.registry.control]
frameworks: [copy.close-frameworks, copy.fascination-bullets, copy.aida, offer-to-funnel-mapping, money-model-sequence]
checklists: [vsl/vsl-value-before-price-gate, vsl/vsl-cta-strength-gate, vsl/vsl-urgency-gate]
registries: [control-registry, offer-registry, proof-registry]
tags: [template, copy, thank-you-page, upsell, onboarding, post-conversion]
---

# Thank-You Page Scripts — Roteiros de Pós-Conversão

A página de obrigado (thank-you page) é o momento de **pico de intenção**: a pessoa acabou de comprar e confia em você como nunca mais vai confiar. Este template reúne os roteiros que essa página precisa: o **upsell no pico** (a oferta do degrau seguinte do Money Model), a **confirmação/onboarding** (o que fazer agora para o primeiro resultado rápido) e a **indicação** (convite para trazer outro cliente). Cada roteiro tem **um** trabalho e **um** CTA. É onde o Money Model ([`money-model-sequence`](../../frameworks/money-model-sequence.md)) ganha o upsell que sobe o AOV. Toda a redação passa pela voz padrão ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)). É o entregável de pós-conversão do `vsl-webinar-scriptwriter`.

## Como usar
- **Agente dono:** `vsl-webinar-scriptwriter` (camada D4). O degrau de upsell e a sequência vêm do `money-model-designer`; o próximo passo do funil, do `funnel-architect`; a voz, do `voice-style-guardian`; escassez do upsell validada pelo `compliance-auditor`.
- **Task:** `write-ty-page-scripts`. Consome o [`money-model`](../offer/money-model-template.md) (qual é o upsell), o [`offer-book-master`](../core/offer-book-master.md), o [`proof-bank`](../strategy/proof-bank-template.md) e a [`vsl-webinar-script`](vsl-webinar-script-template.md) (tom e oferta núcleo já travados).
- **Quando:** na D4, depois da página/VSL de venda. É o primeiro ponto pós-compra do funil.
- Regra: o upsell entra **no pico da compra**, não antes. **Valor antes do preço** também aqui. **Um** CTA por bloco; o "não, obrigado" do upsell é claro e leva ao onboarding (nunca prende o cliente). Onboarding aponta para o **primeiro resultado rápido** (sobe a probabilidade de sucesso da Value Equation). Use [`cta-block`](../../lib/components/cta-block.md), [`scarcity-block`](../../lib/components/scarcity-block.md).

## Campos & Instruções
- **{{CONFIRMACAO}}** — a confirmação calorosa da compra: o que ele acabou de garantir, em uma frase, e a tranquilidade ("deu certo, está tudo aqui").
- **{{OFERTA_UPSELL}}** — o degrau seguinte do Money Model (upgrade, feito-para-você, mais velocidade). O que é e o resultado a mais.
- **{{ENCAIXE_UPSELL}}** — por que faz sentido **agora**, em cima do que ele já comprou (lógica de continuidade, não venda fria).
- **{{ANCORA_UPSELL}}** / **{{PRECO_UPSELL}}** — o valor do upsell e o preço (de pico), valor **antes** do preço.
- **{{ESCASSEZ_UPSELL}}** — o limite real do upsell ("esta condição só nesta página", se for verdade) — falsa = veto.
- **{{CTA_SIM}}** / **{{CTA_NAO}}** — a aceitação (um clique, sem recompra de dados) e a recusa clara que leva ao onboarding.
- **{{ONBOARDING}}** — o primeiro passo concreto para o resultado rápido (acessar, instalar, agendar) e o que esperar.
- **{{INDICACAO}}** — (opcional) o convite para trazer outro cliente, com o incentivo honesto.

## O Template
```
# THANK-YOU PAGE SCRIPTS — {{NOME_DA_OFERTA}}
Owner: vsl-webinar-scriptwriter · Voz: brand-default-hormozi-style · Data: {{DATA}}
Momento: pico de intenção pós-compra · Degrau seguinte (Money Model): {{DEGRAU}}

## 1. CONFIRMAÇÃO  {{CONFIRMACAO}}

## 2. UPSELL NO PICO  (um CTA)
O que é: {{OFERTA_UPSELL}}
Por que agora (encaixe): {{ENCAIXE_UPSELL}}
Âncora R$ {{ANCORA_UPSELL}} → PREÇO de pico R$ {{PRECO_UPSELL}}   [valor ANTES do preço]
Escassez verdadeira: {{ESCASSEZ_UPSELL}} (motivo real: {{MOTIVO_REAL}})
[SIM] {{CTA_SIM}}   ·   [NÃO, OBRIGADO] {{CTA_NAO}} → leva ao onboarding

## 3. ONBOARDING (primeiro resultado rápido)
{{ONBOARDING}}

## 4. INDICAÇÃO (opcional)
{{INDICACAO}}
```

## Exemplo preenchido
> **# THANK-YOU PAGE SCRIPTS — Aprovado em Inglês** · Voz: brand-default-hormozi-style · Degrau seguinte: Mentoria Pro 1:1
>
> **1. CONFIRMAÇÃO** — "Pronto. Sua vaga no Aprovado em Inglês está garantida. O acesso já está no seu e-mail. Bem-vindo."
> **2. UPSELL NO PICO** — O que é: **Mentoria Pro 1:1** — 4 sessões com um recrutador sênior que simula a entrevista da empresa-alvo. Por que agora: "Você já tem o método; a Pro acelera quem tem entrevista marcada nas próximas semanas." Âncora R$1.600 → **R$497 só nesta página**. Escassez: "10 vagas de mentoria por mês (cada recrutador atende poucos)." [SIM] "Adicionar a Mentoria Pro com 1 clique" · [NÃO, OBRIGADO] "Seguir só com o curso" → vai ao onboarding.
> **3. ONBOARDING** — "Comece agora: assista à aula 1 (12 min) e grave seu primeiro shadowing hoje. Em 20 minutos você já sente a diferença na fala."
> **4. INDICAÇÃO** — "Conhece outro dev travando no inglês? Indique e vocês dois ganham uma sessão de roleplay extra."

## DoD do entregável
Os roteiros de thank-you page estão prontos quando: (1) há uma **confirmação** calorosa que tranquiliza o comprador; (2) o **upsell** é o degrau seguinte do [`money-model`](../offer/money-model-template.md), apresentado **no pico da compra**, com o encaixe lógico ("em cima do que você já comprou"); (3) o **valor vem antes do preço** do upsell, com preço de pico (`vsl-value-before-price-gate`); (4) a escassez do upsell, se houver, é **verdadeira** com motivo honesto (`vsl-urgency-gate`, validada pelo `compliance-auditor`); (5) há **um** CTA de aceite e um "não, obrigado" **claro** que leva ao onboarding (nunca prende o cliente) (`vsl-cta-strength-gate`); (6) o **onboarding** aponta para o primeiro resultado rápido (sobe a probabilidade de sucesso da Value Equation); (7) a indicação, se incluída, traz incentivo honesto; (8) cada bloco tem **um** trabalho único; (9) a peça passou pela **voz** ([`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md)), aprovada pelo `voice-style-guardian`; (10) as variações de upsell alimentam o [`control-registry`](../../data/registries/control-registry.md) e a oferta de upsell consta no [`offer-registry`](../../data/registries/offer-registry.md).
