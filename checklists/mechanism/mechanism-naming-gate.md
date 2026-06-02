---
id: checklist.mechanism.mechanism-naming-gate
title: "Gate — Mecanismo com Nome Próprio, Novo e Memorável (não clichê de categoria)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
frameworks: [unique-mechanism]
registries: [offer-registry]
tags: [gate, mechanism, naming, nome-proprio, d2, novidade, sofisticacao]
---

# Gate — Mecanismo com Nome Próprio

## Propósito
Este gate prova que o `mechanism-architect` batizou o mecanismo com um **nome próprio, novo e memorável**, em vez de um clichê de categoria. Existe porque em mercados estágio 3-4 — onde quase todo lançamento vive — o nome do mecanismo é a diferença entre "mais um produto" e "a única coisa que faz sentido". Um nome genérico ("método exclusivo", "fórmula secreta") não fura o ceticismo nem se cola na memória; um nome próprio ("Termostato Metabólico") vira a alça por onde o avatar segura a ideia. O nome precisa casar com o estágio: introduzir um mecanismo novo (estágio 3) ou elevar um existente (estágio 4). Sem um nome que soe diferente dos concorrentes do market-brief, o mecanismo se dissolve no ruído da categoria.

## Dono & Escopo
- **owner_agent:** `mechanism-architect` (gera e poda candidatos via Tree-of-Thoughts em [`unique-mechanism`](../../frameworks/unique-mechanism.md)).
- **Artefato inspecionado:** o **nome do mecanismo** no `mechanism-sheet` e a decisão de naming (candidatos, vencedor, motivo da poda) no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O mecanismo tem um nome próprio, novo frente aos concorrentes e memorável, escolhido entre candidatos pontuados e coerente com o estágio de sofisticação.

## Itens
1. **Nome próprio, não descrição.** Verificar: o mecanismo tem um nome batizado (substantivo próprio), não uma frase genérica de categoria.
2. **Novo frente aos concorrentes.** Verificar: o nome não repete os mecanismos já em mercado listados no [`market-competitor-evidence-gate`](../market/market-competitor-evidence-gate.md).
3. **≥3 candidatos pontuados.** Verificar: o agente gerou ao menos três nomes e os pontuou contra a rubrica (novidade, credibilidade, simplicidade, reposiciona-culpa), registrando os podados.
4. **Memorável e simples.** Verificar: o nome cabe na memória do avatar e ele consegue repeti-lo — sem jargão.
5. **Coerente com a sofisticação.** Verificar: o naming casa com o estágio (3 = introduzir mecanismo novo; 4 = elevar um existente).
6. **Não promete cura/garantia implícita.** Verificar: o nome não embute claim proibido (cura, garantia médica) que o `compliance-auditor` rejeitaria.
7. **Ligado à causa-raiz.** Verificar: o nome aponta para a causa-raiz isolada no [`mechanism-root-cause-gate`](mechanism-root-cause-gate.md), não para um rótulo solto.

## Evidência Exigida
Para marcar cada item ✅, linkar o nome no `mechanism-sheet` e a decisão de naming no [`offer-registry`](../../data/registries/offer-registry.md) (candidatos gerados, vencedor, motivo da poda). A novidade é verificada contra o inventário competitivo do [`market-competitor-evidence-gate`](../market/market-competitor-evidence-gate.md). A ligação à causa-raiz linka o gate anterior. O permalink da decisão de naming conta como evidência.

## Protocolo de Falha
Item vermelho → o `mechanism-architect` volta a gerar candidatos. Nome que é clichê de categoria → volta aos 5 Whys e desce mais um nível de causa até achar algo realmente novo. Nome bonito vazio de causa → separa naming de mecanismo: primeiro a cadeia causal provada, só depois o nome. Nome que embute claim proibido → reescreve sem a promessa. Re-entrada: escolhido e justificado o nome, o gate é re-submetido. O agente não tem veto; sinaliza ao `compliance-auditor` qualquer nome de risco. Máximo de 3 ciclos antes de escalar ao chief.

## Links
- Frameworks: [`unique-mechanism`](../../frameworks/unique-mechanism.md) · [`magic-naming`](../../frameworks/magic-naming.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`mechanism-architect`](../../agents/mechanism-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Novidade verificada contra: [`market-competitor-evidence-gate`](../market/market-competitor-evidence-gate.md)
- Gate anterior (causa): [`mechanism-root-cause-gate`](mechanism-root-cause-gate.md) · Gate seguinte (prova): [`mechanism-proof-gate`](mechanism-proof-gate.md)
