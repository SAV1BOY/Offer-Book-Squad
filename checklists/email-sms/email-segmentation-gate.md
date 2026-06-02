---
id: checklist.email-sms.email-segmentation-gate
title: "Gate — Segmentação (a pessoa certa recebe a mensagem certa; quem comprou é suprimido)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
frameworks: [copy/email-sequence-architecture, launch/cart-open-close]
registries: [control-registry]
tags: [gate, email, sms, segmentacao, supressao, relevancia, d4]
---

# Gate — Segmentação

## Propósito
Este gate prova que **a pessoa certa recebe a mensagem certa** — e que **quem já comprou para de receber venda**. Relevância é metade da conversão de e-mail: a mesma mensagem que aquece um lead frio irrita um comprador, e mandar oferta para quem já pagou queima a lista e a confiança. O gate exige uma regra de segmento por mensagem (por engajamento, por estágio no funil, por consciência ou por ação — clicou/não clicou/comprou) e, crucialmente, uma **regra de supressão**: quem comprou sai de todos os fluxos que vendem. Ele equilibra os dois erros opostos — fragmentar demais (segmentos pequenos demais para importar) e não segmentar (todo mundo recebe tudo). É o gate que protege a entregabilidade e a relevância ao mesmo tempo, e o [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) depende dele para a saúde da lista.

## Dono & Escopo
- **owner_agent:** `email-sms-sequence-writer` (sem poder de veto; saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md)).
- **Artefato inspecionado:** os campos `lista_segmento` e `supressao` de cada mensagem na `sequence-matrix` do [`control-registry`](../../data/registries/control-registry.md), e o corte de listas escolhido via [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md).

## Condição de Passagem
Cada mensagem declara seu segmento-alvo e sua regra de supressão, com quem comprou removido dos fluxos de venda e nenhum segmento incoerente com o conteúdo.

## Itens
1. **Segmento por mensagem.** Verificar: cada linha da matriz tem `lista_segmento` preenchido — nenhuma mensagem dispara para "todos" sem critério.
2. **Critério de corte declarado.** Verificar: o corte usa um eixo claro (engajamento, estágio, consciência ou ação), não um agrupamento arbitrário.
3. **Supressão de compradores.** Verificar: quem comprou tem `supressao` que o remove de todos os fluxos que vendem o mesmo produto.
4. **Coerência segmento×conteúdo.** Verificar: nenhum segmento recebe uma mensagem incoerente (frio recebendo "última chance" de algo que nunca viu).
5. **Lead herdado por segmento.** Verificar: a abertura dos e-mails-chave herda o lead travado conforme a consciência do segmento.
6. **Sem fragmentação inútil.** Verificar: nenhum segmento é pequeno/irrelevante demais para justificar uma mensagem própria.
7. **Regras registradas.** Verificar: segmento e supressão de cada mensagem estão gravados no `control-registry`.

## Evidência Exigida
Para marcar ✅: linkar a `sequence-matrix` no `control-registry` com `lista_segmento` e `supressao` por mensagem (itens 1–3, 7), a checagem de coerência segmento×conteúdo (item 4), o lead herdado por consciência (item 5) e a justificativa de que nenhum segmento fragmenta sem ganho (item 6).

## Protocolo de Falha
Item vermelho → o `email-sms-sequence-writer` adiciona a regra de segmento/supressão faltante; quem comprou recebendo venda é reprovação e corrige-se com supressão por ação. Segmento incoerente → realinha a mensagem ao estágio. Fragmentação inútil → funde segmentos. Re-entrada: atualiza segmento/supressão no `control-registry` e re-submete ao [`voice-style-guardian`](../../agents/voice-style-guardian.md). Mudança de fluxo reabre este gate.

## Links
- Gates irmãos: [`email-step-coverage-gate`](email-step-coverage-gate.md) · [`email-timing-gate`](email-timing-gate.md) · [`email-subject-gate`](email-subject-gate.md) · [`email-urgency-coherence-gate`](email-urgency-coherence-gate.md)
- Frameworks: [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md) · [`cart-open-close`](../../frameworks/launch/cart-open-close.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md) · [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
