---
id: template.qa.faq
title: "FAQ — O Bloco de Perguntas que Mata Objeções"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: compliance-auditor
consumes: [data.registry.objection, data.registry.proof, template.core.offer-book-master]
produces: [data.registry.objection]
frameworks: [proof-to-claim-chain, scarcity-urgency-engine, risk-reversal-ladder]
checklists: [compliance-checklist, compliance/compliance-claim-backing-gate, compliance/compliance-disclaimers-gate]
registries: [objection-registry, proof-registry, claim-registry]
tags: [template, faq, objecoes, prova, compliance, qa]
---

# FAQ — O Bloco que Mata Objeções

Este template produz o **FAQ** da oferta: não um amontoado de dúvidas, mas a lista das objeções reais que travam a compra, cada uma respondida com prova. Toda pergunta é uma objeção do [`objection-registry`](../../data/registries/objection-registry.md); toda resposta aponta para uma prova do [`proof-registry`](../../data/registries/proof-registry.md). O FAQ não inventa força — ele desarma o "não" com verdade (`evidence_before_opinion`). Nenhuma resposta promete o que a oferta não entrega, e nenhuma escassez citada é falsa (`truthful_scarcity`).

## Como usar
- **Agente dono:** [`compliance-auditor`](../../agents/compliance-auditor.md) (garante que cada resposta tem lastro). Pareia com o [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) (que traz as objeções na voz do cliente) e com o [`voice-style-guardian`](../../agents/voice-style-guardian.md) (que aprova a voz).
- **Task:** preenchido depois do Offer Book aprovado, quando as objeções e as provas estão mapeadas. Lido pela copy de D4 (VSL, e-mails, página) e colado na página de vendas.
- **Quando:** o auditor monta o FAQ assim que o [`objection-registry`](../../data/registries/objection-registry.md) tem as objeções dominantes. Aplica o [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) para amarrar resposta à prova e a [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md) para responder à objeção de risco com a garantia certa.
- Use a objeção na voz do avatar como pergunta. Use número e prova na resposta. Resposta sem prova = claim órfão = veto do auditor.

## Campos & Instruções
- **{{NOME_DA_OFERTA}}** — a oferta a que este FAQ pertence, da planilha [`products-and-offers`](../offer/products-and-offers-template.csv).
- **{{OBJECAO}}** — a objeção dominante, escrita como pergunta, na voz do cliente (slug no [`objection-registry`](../../data/registries/objection-registry.md)).
- **{{RESPOSTA}}** — a resposta curta que desarma a objeção, em voz ativa e presente.
- **{{PROVA_REF}}** — o id da prova que sustenta a resposta (`proof-registry#PR-NNN`). Sem ela, a resposta não entra.
- **{{ALAVANCA}}** — a alavanca que a resposta aciona (prova, garantia, escassez real, mecanismo único).
- **{{DISCLAIMER}}** — quando há promessa de resultado, o aviso obrigatório ("resultados variam; sem garantia de ganho"), conforme a [política de compliance](../../docs/compliance-policy.md).

## O Template
```
# FAQ — {{NOME_DA_OFERTA}}
Owner: compliance-auditor · Data: {{DATA}}

## P1: {{OBJECAO_1}}
R: {{RESPOSTA_1}}
Prova: {{PROVA_REF_1}} · Alavanca: {{ALAVANCA_1}}
Disclaimer (se houver promessa): {{DISCLAIMER_1}}

## P2: {{OBJECAO_2}}
R: {{RESPOSTA_2}}
Prova: {{PROVA_REF_2}} · Alavanca: {{ALAVANCA_2}}
Disclaimer (se houver promessa): {{DISCLAIMER_2}}

## P3: {{OBJECAO_3}}
R: {{RESPOSTA_3}}
Prova: {{PROVA_REF_3}} · Alavanca: {{ALAVANCA_3}}
Disclaimer (se houver promessa): {{DISCLAIMER_3}}

## P4: {{OBJECAO_4}}
R: {{RESPOSTA_4}}
Prova: {{PROVA_REF_4}} · Alavanca: {{ALAVANCA_4}}
Disclaimer (se houver promessa): {{DISCLAIMER_4}}
```

## Exemplo preenchido
> **# FAQ — Motor de Recuperação 72h**
> Owner: compliance-auditor · Data: 2026-06-02
>
> **P1: "É caro demais para mim agora."**
> R: O Motor custa R$497 e devolve, em média, mais que isso no primeiro mês. Você recupera receita que já era sua. Prova: proof-registry#PR-031 · Alavanca: prova de resultado.
> Disclaimer: resultados variam; não há garantia de ganho.
>
> **P2: "Já tentei de tudo e nada funcionou."**
> R: Você tentou táticas soltas. Aqui você instala uma sequência de 7 mensagens cronometradas, no pico de intenção. É o mecanismo, não mais esforço. Prova: proof-registry#PR-031 · Alavanca: mecanismo único.
>
> **P3: "E se não der certo comigo?"**
> R: Você tem a garantia do dobro do dinheiro de volta em 30 dias. O risco é nosso, não seu. Prova: proof-registry#PR-022 · Alavanca: reversão de risco.
>
> **P4: "Posso entrar depois?"**
> R: A turma tem 40 vagas, por capacidade real de setup. O carrinho fecha sábado às 23h59 e não reabre nesta condição. Prova: política de vagas declarada · Alavanca: escassez verdadeira.

## DoD do entregável
O FAQ está pronto quando: (1) cada pergunta é uma objeção real do [`objection-registry`](../../data/registries/objection-registry.md), na voz do avatar, sem `{{PLACEHOLDER}}` solto; (2) cada resposta aponta para uma prova que resolve no [`proof-registry`](../../data/registries/proof-registry.md), satisfazendo o [`compliance-claim-backing-gate`](../../checklists/compliance/compliance-claim-backing-gate.md) — nenhuma resposta fica como claim órfão (`evidence_before_opinion`); (3) toda promessa de resultado traz o disclaimer obrigatório, satisfazendo o [`compliance-disclaimers-gate`](../../checklists/compliance/compliance-disclaimers-gate.md); (4) qualquer escassez citada é **100% verdadeira** (`truthful_scarcity`), alinhada à [política de compliance](../../docs/compliance-policy.md); (5) as respostas estão em voz ativa, presente, 3ª série, aprovadas pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md); (6) o vínculo objeção↔resposta↔prova fica registrado no [`claim-registry`](../../data/registries/claim-registry.md) e atualiza o [`objection-registry`](../../data/registries/objection-registry.md). O FAQ passa no [`compliance-checklist`](../../checklists/compliance-checklist.md) antes de ir para a página de vendas.
