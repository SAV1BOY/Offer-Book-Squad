---
id: framework.launch.abandoned-cart-recovery
title: "Abandoned Cart Recovery — Recuperação de Carrinho Abandonado"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [cart-open-close, surge-ops, product-launch-formula, money-model-sequence]
sources:
  - "Alex Hormozi, *$100M Offers* (2021), reversão de risco e objeções."
  - "Jeff Walker, *Launch* (2014; ed. atualizada, 2023), sequência de fechamento."
tags: [abandoned-cart, recovery, checkout, objection, downsell, email, sms, walker, hormozi]
---

# Abandoned Cart Recovery — Recuperação de Carrinho Abandonado

## TL;DR
Quem chega ao checkout e não paga é o lead **mais quente** que existe — quis comprar e travou. Recuperar carrinho abandonado é a sequência que remove o último atrito: lembra, responde a objeção, reverte o risco e, se preciso, oferece o downsell. É a maior fonte de receita "barata" de um lançamento, porque o desejo já existe. O `launch-producer` define a janela; o `email-sms-sequence-writer` escreve a sequência de recuperação por e-mail e SMS.

## Quando usar / Quando não
**Use** sempre que houver checkout: todo carrinho abandonado é receita recuperável que já demonstrou intenção.
**Use mais** em pico de fechamento, onde o volume de abandono é maior e a janela é curta — pareie com [`surge-ops.md`](surge-ops.md).
**Não use** com pressão falsa ou deadline inventado para "forçar" a volta — isso quebra a confiança (`truthful_scarcity`).
**Não use** como spam infinito: a sequência tem fim e respeita o descadastro.

## Inputs
- Captura do evento de abandono (e-mail/telefone no checkout, com consentimento).
- O mapa de objeções do avatar (do `objection-registry`) para escolher o argumento certo.
- A garantia e a reversão de risco da oferta ([`../../lib/taxonomies/guarantee-types.md`](../../lib/taxonomies/guarantee-types.md)).
- O downsell da escada, se houver ([`../money-model-designer/upsell-downsell-logic.md`](../money-model-designer/upsell-downsell-logic.md)).
- A janela e o deadline reais do carrinho ([`cart-open-close.md`](cart-open-close.md)).

## Procedimento
1. **Capture o abandono** no checkout com consentimento (LGPD): e-mail e, se autorizado, telefone.
2. **Dispare o lembrete rápido** (15-60 min): "ficou algo no seu carrinho", link direto de volta, sem pressão.
3. **Identifique a objeção provável**: preço, dúvida no resultado, falta de tempo, medo de risco. Escolha o argumento do `objection-registry`.
4. **Mande o contato de objeção** (algumas horas depois): rebata a objeção dominante com prova e reforce a garantia.
5. **Reverta o risco** explicitamente: traga a garantia certa para a frente — ela é a alavanca mais barata para destravar.
6. **Ofereça o downsell**, se aplicável: versão menor, parcelamento ou início adiado para quem travou no preço.
7. **Reforce o deadline real**: relembre o que some e quando, sem inventar urgência.
8. **Encerre a sequência**: limite o número de contatos e honre o descadastro. Quem não voltou, sai.
9. **Registre** taxa de recuperação e qual argumento converteu no `control-registry`.

## Outputs
- **Sequência de recuperação** (briefs): lembrete, objeção+prova, reversão de risco, downsell, deadline.
- Regra de captura de abandono conforme consentimento.
- Mapa objeção → argumento → prova usada.
- Métrica de recuperação (taxa, argumento vencedor) para a memória.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Captura**: e-mail no checkout, telefone opcional com opt-in.
- **Lembrete (30 min)**: "Sua vaga na turma ficou reservada por pouco tempo — termine aqui".
- **Objeção (3h)**: dominante = "não tenho tempo". E-mail com caso de aluno que estudou 20 min/dia + prova.
- **Reversão de risco**: reforça "aprovado na entrevista ou seguimos juntos de graça".
- **Downsell (dia seguinte)**: parcelamento em 12x para quem travou no preço à vista.
- **Deadline**: lembra que o bônus "50 frases" some no fechamento real de sábado.
- **Resultado**: parte relevante dos carrinhos volta; a objeção "tempo" some com prova, e o downsell salva quem travou no preço.

## Armadilhas
- **Demorar para o primeiro lembrete.** O desejo esfria rápido; o primeiro contato deve ser em minutos.
- **Argumento genérico.** Mandar a mesma copy para todos ignora a objeção real. Use o mapa de objeções.
- **Pressão falsa.** Inventar "última vaga" para quem abandonou destrói confiança e é veto.
- **Sequência sem fim.** Insistir demais vira spam, derruba entregabilidade e gera descadastro.
- **Ignorar consentimento.** Capturar contato sem opt-in viola LGPD — veto de compliance.

## Interações
- **Agentes**: `email-sms-sequence-writer` (escreve a sequência de recuperação); `launch-producer` (define a janela e integra ao fechamento); `money-model-designer` (fornece o downsell da escada); `value-equation-engineer` (a reversão de risco move a Probabilidade); `compliance-auditor` (consentimento e urgência real).
- **Frameworks que pareiam**: [`cart-open-close.md`](cart-open-close.md) (a janela e o deadline), [`surge-ops.md`](surge-ops.md) (captura no pico), [`../money-model-designer/upsell-downsell-logic.md`](../money-model-designer/upsell-downsell-logic.md) (o downsell), [`../../frameworks/money-model-sequence.md`](../../frameworks/money-model-sequence.md).

## Fontes
> **Fonte:** Alex Hormozi, *$100M Offers* (2021) — reversão de risco e objeções — via [`../../reference/books/offers-and-monetization/hormozi-100m-offers.md`](../../reference/books/offers-and-monetization/hormozi-100m-offers.md), acesso 2026-06-02.
> **Fonte:** Jeff Walker, *Launch* (2014; ed. atualizada, 2023) — sequência de fechamento — via [`../../reference/books/launches-and-funnels/walker-launch.md`](../../reference/books/launches-and-funnels/walker-launch.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
