---
id: framework.reference-intellectual.kennedy-no-bs
title: "Kennedy — Message-Market-Match, Oferta, Urgência e Posição (No B.S.)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [awareness-x-sophistication, offer-stack-builder, scarcity-urgency-engine, offer-to-funnel-mapping]
sources:
  - "Dan S. Kennedy, *The Ultimate Sales Letter* (4ª ed., Adams Media, 2011), ISBN 978-1-4405-1141-3."
tags: [kennedy, message-market-match, offer, urgency, positioning, direct-response, no-bs]
---

# Kennedy — Message-Market-Match, Oferta, Urgência e Posição (No B.S.)

## TL;DR
Kennedy é o sistematizador "sem firula" da resposta direta moderna. A tese central é o triângulo **Mensagem–Mercado–Mídia (Message-Market-Match)**: a mensagem certa, para o mercado certo, pela mídia certa. Erre um lado e nada salva. Disso saem duas leis do squad: toda peça tem um **propósito de resposta mensurável** (nada de "branding" vago); e a **oferta** com o **CTA** carregam a venda — copy bonita sem oferta forte é dinheiro queimado. Some a isso a exigência de uma **razão verdadeira para agir agora**. Vence quando a campanha precisa de disciplina: alvo único, oferta clara, resposta medida.

## Quando usar / Quando não
**Use** para alinhar a tríade antes de escrever: a quem falo, com que mensagem, por qual canal.
**Use** para auditar qualquer peça que pareça "bonita mas sem propósito" — exija a resposta mensurável.
**Use** para escrever a carta/VSL em torno de **uma** oferta e **um** CTA, e para checar a urgência com motivo real.
**Não use** para montar o stack ou derivar o preço — Kennedy carrega a oferta na copy, mas o desenho da oferta é Hormozi.
**Não use** para escolher o nível de consciência — isso é Schwartz; Kennedy assume o avatar já definido.
**Fit:** universal; é a régua de **foco e resposta** que atravessa toda peça de D4.

## Inputs
- O avatar único e sua dor específica (do banco de VOC) — Kennedy escreve para **uma** pessoa.
- A oferta forte já desenhada (mecanismo, stack, garantia) — ver [`hormozi-offers-leads-models.md`](hormozi-offers-leads-models.md).
- O canal/mídia candidato e seu fit com o mercado.
- A razão **verdadeira** para agir agora (prazo, limite, consequência de adiar).
- A métrica de resposta esperada (a peça serve a qual decisão mensurável?).

## Procedimento
1. **Case a tríade Message-Market-Match.** Antes de redigir, alinhe **mensagem ↔ mercado ↔ mídia**. Identifique o elo mais fraco — ele define o resultado — e corrija-o primeiro.
2. **Escreva para uma pessoa.** Defina o avatar único com nome, dor e contexto. Copy "para todos" não converte ninguém; fale a uma só.
3. **Defina o propósito de resposta.** Declare a ação mensurável que a peça deve gerar (clique, opt-in, compra). Sem propósito medível, é decoração — corte.
4. **Construa a carta em torno da oferta.** A peça inteira existe para entregar **uma oferta irresistível** com clareza: o que é, o que custa, o que se ganha, por que agora.
5. **Use um único CTA forte.** Um pedido, explícito e repetido. Múltiplos CTAs dividem a decisão e derrubam a resposta.
6. **Dê um motivo real para agir agora.** Amarre a urgência a um fato — prazo, vaga, consequência. "Compre já" vazio não move e queima confiança.
7. **Escreva quente, edite frio.** Redija no calor da convicção; depois corte com frieza o que não serve à resposta.
8. **Meça e registre.** Logue a resposta da peça e o que ela provou; alimente o `control-registry` e o ciclo de teste.

## Outputs
- O **diagnóstico da tríade**: mensagem, mercado e mídia alinhados, com o elo fraco corrigido.
- O **avatar único** declarado (a quem a peça fala).
- O **propósito de resposta mensurável** da peça.
- A **carta/VSL** organizada em torno de uma oferta e um CTA.
- A **urgência com motivo real** documentada (o fato que a sustenta).

## Exemplo
Oferta de amostra: software de agendamento para clínicas odontológicas.
- **Tríade**: mercado = donos de clínica com cadeira ociosa; mensagem = "pare de perder horário vago"; mídia = e-mail direto para uma lista comprada de associações. Elo fraco identificado: a mídia (lista fria) → mensagem precisa parecer pessoal (Pilha A).
- **Avatar único**: "Dra. Helena, dona de duas cadeiras, perde 12 horários por semana com faltas."
- **Propósito de resposta**: agendar uma demonstração (métrica clara), não "conhecer a marca".
- **Oferta + CTA**: "Recupere 10 horários por semana em 30 dias — agende sua demo" (um único CTA, repetido).
- **Urgência real**: "abrimos 15 onboardings este mês; depois, fila de espera de 6 semanas" — limite verdadeiro de capacidade.
- **Resultado**: a peça tem alvo único, oferta clara e resposta medível; o `compliance-auditor` confirma que a urgência tem lastro.

## Armadilhas
- **Mensagem certa, mercado/mídia errados.** O elo fraco invalida a melhor copy; sempre cheque a tríade inteira.
- **Escrever para "todos".** Sem avatar único, a peça não fala a ninguém.
- **Peça sem propósito de resposta.** "Branding" vago não se mede e não se otimiza.
- **CTA múltiplo ou tímido.** Dividir o pedido derruba a conversão; peça uma ação, com clareza.
- **Urgência sem motivo.** "Últimas vagas" sem vaga real é veto de compliance e queima confiança.
- **Oferta fraca carregada por copy bonita.** Sem oferta forte, nenhuma frase salva a venda.

## Interações
- **Agentes** (de `config.yaml`): `positioning-lead-strategist` (aplica Message-Market-Match para casar lead, público e canal); `vsl-webinar-scriptwriter` (estrutura a carta/VSL em torno da oferta e de um único CTA); `email-sms-sequence-writer` (razão-para-agir-agora verdadeira no fechamento); `direct-mail-insert-writer` (disciplina "escreva para uma pessoa"); `funnel-architect` (escolha de mídia/canal); `compliance-auditor` (confere urgência com motivo real, `truthful_scarcity`).
- **Frameworks que pareiam**: [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md) (casamento mensagem-mercado), [`../offer-stack-builder.md`](../offer-stack-builder.md) (a oferta que a carta carrega), [`../scarcity-urgency-engine.md`](../scarcity-urgency-engine.md) (urgência com lastro), [`../offer-to-funnel-mapping.md`](../offer-to-funnel-mapping.md) (a mídia certa); e a referência [`caples-tested-advertising.md`](caples-tested-advertising.md) (testar a mensagem que casa com o mercado).

## Fontes
> **Fonte:** Dan S. Kennedy, *The Ultimate Sales Letter* (4ª ed., Adams Media, 2011), ISBN 978-1-4405-1141-3 — via [`../../reference/books/copywriting/kennedy-ultimate-sales-letter.md`](../../reference/books/copywriting/kennedy-ultimate-sales-letter.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
