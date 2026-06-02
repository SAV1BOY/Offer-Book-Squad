---
id: checklist.mechanism.mechanism-root-cause-gate
title: "Gate — Causa-Raiz do Problema e da Solução Isoladas (5 Whys completos, sem salto)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
frameworks: [unique-mechanism, value-equation]
registries: [offer-registry]
tags: [gate, mechanism, causa-raiz, 5-whys, d2, reposiciona-culpa]
---

# Gate — Causa-Raiz do Problema e da Solução Isoladas

## Propósito
Este gate prova que o `mechanism-architect` desceu até a **causa-raiz** do problema do avatar e até o passo causal da solução, usando os 5 Whys, antes de batizar qualquer mecanismo. Existe porque um nome bonito sem cadeia causal é rótulo vazio — e clichê de categoria ("método natural") não fura o ceticismo de um mercado estágio 3-4. A causa-raiz é o que **reposiciona a culpa** para longe do avatar ("não é sua força de vontade — é seu termostato metabólico travado"). Sem isolar a causa real do problema e o passo que de fato muda o resultado, o mecanismo não tem do que se sustentar, e o `value-equation-engineer` a jusante não tem alavanca real para pontuar. É a fundação causal de todo o núcleo conceitual da oferta.

## Dono & Escopo
- **owner_agent:** `mechanism-architect` (aplica os 5 Whys de [`unique-mechanism`](../../frameworks/unique-mechanism.md)).
- **Artefato inspecionado:** a **cadeia causal** do `mechanism-sheet` (problema-raiz e solução-raiz), registrada no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
A cadeia causal do problema desce até uma raiz reposicionável, e o passo causal da solução está isolado, sem salto infalsificável entre os elos.

## Itens
1. **Cadeia do problema completa.** Verificar: os 5 Whys descem do sintoma ("não emagrece") até a causa-raiz ("dietas repetidas treinaram o corpo a economizar") — sem pular níveis.
2. **Causa-raiz reposicionável.** Verificar: a raiz tira a culpa do avatar (moral/força de vontade) e a coloca num fator novo (fisiológico/sistêmico).
3. **Passo causal da solução isolado.** Verificar: o que **causa** o resultado está separado da lista de features — é o passo, não o pacote.
4. **Sem salto infalsificável.** Verificar: nenhum elo da cadeia é uma alegação que nada poderia refutar; cada elo é verificável ou marcado para prova.
5. **Ancorado na objeção dominante.** Verificar: a causa-raiz neutraliza a objeção #1 do avatar ("já tentei tudo e nada funcionou"), reatribuindo a culpa.
6. **Move ≥1 alavanca.** Verificar: o passo causal da solução move pelo menos uma alavanca da [`value-equation`](../../frameworks/value-equation.md) (sonho, probabilidade, tempo ou esforço).
7. **Suposições marcadas.** Verificar: se algum elo depende de input de baixa confiança, está marcado `provisório`, com a lacuna nomeada.

## Evidência Exigida
Para marcar cada item ✅, linkar a cadeia causal do `mechanism-sheet` (sintoma → … → raiz) e a linha do [`offer-registry`](../../data/registries/offer-registry.md). A âncora na objeção dominante linka o [`objection-registry`](../../data/registries/objection-registry.md) e o verbatim da culpa do avatar. A alavanca movida é declarada para o handoff ao [`value-equation-engineer`](../../agents/value-equation-engineer.md). O permalink do registry conta como evidência; elos infalsificáveis não são marcados ✅.

## Protocolo de Falha
Item vermelho → o `mechanism-architect` volta aos 5 Whys e desce mais um nível de causa até achar algo verificável e reposicionável. Salto infalsificável → reescreve o elo para algo verificável ou rebaixa a `provisório` e aciona o `proof-credibility-curator`. Sem objeção dominante mapeada → o agente **não prossegue** e pede ao `avatar-voc-investigator` o verbatim da culpa. Produto sem diferença real de método (commodity) → escalona ao `offerbook-chief`, porque fabricar causa-raiz seria mentir. Re-entrada: completada e verificável a cadeia, o gate é re-submetido. O agente não tem veto; suas flags informam os vetos de quem os tem.

## Links
- Frameworks: [`unique-mechanism`](../../frameworks/unique-mechanism.md) · [`value-equation`](../../frameworks/value-equation.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md) · [`objection-registry`](../../data/registries/objection-registry.md)
- Agentes: [`mechanism-architect`](../../agents/mechanism-architect.md) · [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`value-equation-engineer`](../../agents/value-equation-engineer.md)
- Objeção dominante a montante: [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md)
- Gate seguinte (nome): [`mechanism-naming-gate`](mechanism-naming-gate.md)
