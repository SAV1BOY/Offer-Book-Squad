---
id: checklist.avatar.avatar-jtbd-gate
title: "Gate — Job To Be Done Mapeado nas Três Dimensões (funcional, emocional, social)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
frameworks: [positioning/jtbd, avatar-voc-investigator/voc-mining]
registries: [objection-registry]
tags: [gate, avatar, jtbd, d1, funcional, emocional, social]
---

# Gate — Job To Be Done Mapeado

## Propósito
Este gate prova que o `avatar-voc-investigator` mapeou o que o cliente **realmente contrata** a solução para fazer — nas três dimensões: funcional, emocional e social. Existe porque o cliente não compra um produto, ele "contrata" um progresso; e quase sempre o job **social** ou **emocional** pesa mais que o funcional. No exemplo do inglês, o job funcional é "passar na entrevista", mas o social — "ser respeitado pelos pares" — é o que move a compra. Mapear só o funcional faz a prova a jusante errar o alvo (notas de proficiência em vez de casos de pares respeitados). O `proof-credibility-curator` prioriza a prova pelo job dominante; o `big-idea-architect` ancora a tese nele. Sem o JTBD nas três dimensões, a oferta resolve o problema errado.

## Dono & Escopo
- **owner_agent:** `avatar-voc-investigator` (aplica [`positioning/jtbd`](../../frameworks/positioning/jtbd.md) sobre os verbatims).
- **Artefato inspecionado:** o **bloco JTBD** do avatar/ICP, por segmento, com as três dimensões nomeadas e o job dominante identificado.

## Condição de Passagem
Cada segmento tem o Job To Be Done mapeado nas três dimensões (funcional, emocional, social), ancorado em verbatims, com o job dominante identificado.

## Itens
1. **Três dimensões presentes.** Verificar: o brief nomeia o job funcional, o emocional e o social de cada segmento — nenhum em branco.
2. **Ancoragem em verbatim.** Verificar: cada dimensão do job deriva de um verbatim rastreável, não de suposição.
3. **Job dominante identificado.** Verificar: o brief diz qual das três dimensões pesa mais na decisão de compra (ex.: social > funcional).
4. **Progresso, não feature.** Verificar: o job está escrito como o progresso que o cliente busca ("parar de me sentir burro"), não como a feature do produto.
5. **Implicação de prova derivada.** Verificar: o job dominante gera uma instrução ao `proof-credibility-curator` sobre que tipo de prova priorizar (casos de pares vs métricas).
6. **Coerente com a emoção dominante.** Verificar: o JTBD emocional/social bate com a emoção dominante do [`avatar-dominant-emotion-gate`](avatar-dominant-emotion-gate.md).
7. **Alinhado ao mecanismo.** Verificar: o job que o cliente contrata é coerente com o que o mecanismo da oferta promete entregar a jusante.

## Evidência Exigida
Para marcar cada item ✅, linkar o bloco JTBD do avatar com as três dimensões, o verbatim que ancora cada uma e o job dominante marcado. A implicação de prova linka o handoff ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md). A coerência com a emoção dominante linka o [`avatar-dominant-emotion-gate`](avatar-dominant-emotion-gate.md). O permalink do avatar conta como evidência; jobs sem verbatim de origem não são marcados ✅.

## Protocolo de Falha
Item vermelho → o `avatar-voc-investigator` volta aos verbatims e completa a dimensão faltante. Job escrito como feature → reescreve como progresso do cliente. Job dominante não identificado → re-pondera as três dimensões pela frequência/intensidade nos verbatims. JTBD incoerente com a emoção dominante → revisa os dois juntos. Re-entrada: mapeadas as três dimensões com âncora, o gate é re-submetido. O agente não tem veto; sinaliza ao `offerbook-chief` se o job dominante revelar que a oferta resolve o problema errado.

## Links
- Frameworks: [`jtbd`](../../frameworks/positioning/jtbd.md) · [`voc-mining`](../../frameworks/avatar-voc-investigator/voc-mining.md)
- Registries: [`objection-registry`](../../data/registries/objection-registry.md)
- Agentes: [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`big-idea-architect`](../../agents/big-idea-architect.md)
- Gate de emoção (par): [`avatar-dominant-emotion-gate`](avatar-dominant-emotion-gate.md)
- Promessa do mecanismo a jusante: [`mechanism-one-sentence-gate`](../mechanism/mechanism-one-sentence-gate.md)
