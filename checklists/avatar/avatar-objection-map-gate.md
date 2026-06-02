---
id: checklist.avatar.avatar-objection-map-gate
title: "Gate — Mapa de Objeções com a Falsa Crença por Trás de Cada Não (priorizado por severidade)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
frameworks: [avatar-voc-investigator/objection-belief-mapping]
registries: [objection-registry]
tags: [gate, avatar, objecao, falsa-crenca, d1, severidade, prova]
---

# Gate — Mapa de Objeções com a Falsa Crença

## Propósito
Este gate prova que o `avatar-voc-investigator` mapeou cada objeção até a **falsa crença** por trás dela, e priorizou por severidade. Existe porque copy que rebate a objeção de superfície ("é caro") sem atacar a crença-raiz ("vou desperdiçar dinheiro de novo") não move ninguém. O mapa é a aresta-chave do pipeline D1: o `proof-credibility-curator` casa prova a cada objeção, e o `mechanism-architect` usa as falsas crenças que o mecanismo precisa reverter (ex.: "a culpa é minha por falta de talento" → o mecanismo reatribui a culpa ao método). Sem o mapa completo, alguma peça a jusante deixa uma objeção de alta severidade sem resposta — e ela mata a conversão silenciosamente.

## Dono & Escopo
- **owner_agent:** `avatar-voc-investigator` (dono da fonte do [`objection-registry`](../../data/registries/objection-registry.md)).
- **Artefato inspecionado:** o **mapa de objeções/falsas crenças** do avatar e as linhas correspondentes no [`objection-registry`](../../data/registries/objection-registry.md).

## Condição de Passagem
Cada objeção minerada tem a falsa crença identificada, uma categoria e uma severidade, e as objeções de alta severidade estão cobertas e registradas.

## Itens
1. **Objeção em verbatim.** Verificar: cada objeção parte de um verbatim literal do cliente, não de suposição do agente.
2. **Falsa crença identificada.** Verificar: para cada "não" de superfície, o mapa nomeia a crença-raiz por trás (ex.: "já tentei tudo" → "nada funciona pra mim").
3. **Categoria atribuída.** Verificar: cada objeção tem categoria (`price · time · trust · belief-self · belief-mechanism · fit · risk · priority`).
4. **Severidade marcada.** Verificar: cada objeção tem severidade (`low · medium · high`), e as `high` estão sinalizadas.
5. **Cobertura das alta severidade.** Verificar: toda objeção de severidade alta tem um caminho de resposta nomeado (prova a buscar ou crença a reverter pelo mecanismo).
6. **Registro completo.** Verificar: cada objeção está no [`objection-registry`](../../data/registries/objection-registry.md) com `objection_text`, `category`, `underlying_emotion`, `severity`, `awareness_level`.
7. **Sem mapa pela metade.** Verificar: as objeções recorrentes nos verbatims estão todas no mapa — nenhuma de alta frequência foi deixada de fora.

## Evidência Exigida
Para marcar cada item ✅, linkar o mapa de objeções e as linhas do [`objection-registry`](../../data/registries/objection-registry.md) com o schema preenchido por objeção. Cada falsa crença precisa derivar de um verbatim rastreável. A cobertura das objeções de alta severidade linka o handoff ao [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) e ao [`mechanism-architect`](../../agents/mechanism-architect.md). O permalink de cada linha do registry conta como evidência.

## Protocolo de Falha
Item vermelho → o `avatar-voc-investigator` aprofunda da objeção de superfície até a falsa crença, que é o que o mecanismo precisa reverter. Objeção sem crença-raiz → não passa. Objeção de alta severidade sem caminho de resposta → fica aberta e é sinalizada. Objeção fatal recorrente (aparece em quase todos os verbatims, pode inviabilizar a oferta) → o agente **sinaliza ao `offerbook-chief`** e ao `value-equation-engineer`. Re-entrada: completado o mapa e o registry, o gate é re-submetido. O agente não tem veto; a decisão sobre objeção inviabilizante é do comando.

## Links
- Frameworks: [`objection-belief-mapping`](../../frameworks/avatar-voc-investigator/objection-belief-mapping.md)
- Registries: [`objection-registry`](../../data/registries/objection-registry.md)
- Agentes: [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`proof-credibility-curator`](../../agents/proof-credibility-curator.md) · [`mechanism-architect`](../../agents/mechanism-architect.md)
- Gate par (B2B): [`avatar-dmu-gate`](avatar-dmu-gate.md)
- Reversão de crença a jusante: [`mechanism-root-cause-gate`](../mechanism/mechanism-root-cause-gate.md)
