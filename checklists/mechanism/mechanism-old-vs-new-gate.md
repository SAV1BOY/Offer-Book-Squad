---
id: checklist.mechanism.mechanism-old-vs-new-gate
title: "Gate — Contraste Velho × Novo Construído (por que tudo o que ele tentou falhou, e o seu não)"
type: gate
layer: D2
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: mechanism-architect
frameworks: [unique-mechanism]
registries: [offer-registry]
tags: [gate, mechanism, velho-vs-novo, d2, reposiciona-culpa, posicionamento]
---

# Gate — Contraste Velho × Novo Construído

## Propósito
Este gate prova que o `mechanism-architect` construiu a tabela **velho × novo** — o contraste que explica por que tudo o que o avatar já tentou falhou, e por que o mecanismo novo não vai falhar. Existe porque é esse contraste que reposiciona a culpa para longe do avatar e justifica a existência do mecanismo: "o jeito velho tratava como questão de disciplina; o jeito novo trata como reajuste de um ponto metabólico". Sem o contraste, o mecanismo flutua sem inimigo — e um mecanismo sem "velho a derrubar" não convence um mercado cético. O `positioning-lead-strategist` herda esta tabela para construir o lead; o `big-idea-architect` a usa para enquadrar a tese. É a ponte entre a causa-raiz e a frase única do mecanismo.

## Dono & Escopo
- **owner_agent:** `mechanism-architect` (constrói o contraste em [`unique-mechanism`](../../frameworks/unique-mechanism.md)).
- **Artefato inspecionado:** a **tabela velho × novo** do `mechanism-sheet`, com as dimensões contrastadas, referenciada no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
A tabela velho × novo contrasta, dimensão a dimensão, por que a abordagem antiga falha e a nova funciona, sem caricaturar o velho nem repetir um mecanismo de concorrente.

## Itens
1. **Tabela com dimensões.** Verificar: há uma tabela que contrasta jeito velho × jeito novo em dimensões concretas (causa atacada, esforço, tempo, premissa).
2. **Velho = o que o avatar tentou.** Verificar: a coluna "velho" descreve o que o avatar de fato já tentou (o que falhou), não um espantalho inventado.
3. **Novo = o mecanismo.** Verificar: a coluna "novo" é o mecanismo nomeado, não uma promessa vaga.
4. **Reposiciona a culpa.** Verificar: o contraste tira o peso do avatar ("você não falhou — o método falhou") e o coloca no fator novo.
5. **Não caricatura o velho.** Verificar: a abordagem antiga é descrita com justiça (crível), não como obviamente idiota — senão o avatar que a usou se sente burro.
6. **Diferente dos concorrentes.** Verificar: o "novo" não é o mecanismo que um concorrente já vende (cruzar com o [`market-competitor-evidence-gate`](../market/market-competitor-evidence-gate.md)).
7. **Coerente com o estágio.** Verificar: o contraste casa com a sofisticação (estágio 4 = "melhor que os mecanismos existentes", não "novo no mundo").

## Evidência Exigida
Para marcar cada item ✅, linkar a tabela velho × novo do `mechanism-sheet` e a referência no [`offer-registry`](../../data/registries/offer-registry.md). A coluna "velho" precisa derivar do que o avatar tentou, rastreável nos verbatims do banco de VOC. A diferenciação frente aos concorrentes linka o inventário competitivo. O reposicionamento de culpa linka a objeção dominante do [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md). O permalink da tabela conta como evidência.

## Protocolo de Falha
Item vermelho → o `mechanism-architect` reconstrói o contraste. Velho caricaturado → reescreve a coluna antiga com justiça, para o avatar não se sentir idiota. "Novo" igual ao de um concorrente → volta ao naming/causa e diferencia. Contraste que não reposiciona a culpa → realinha à objeção dominante. Sofisticação mal lida (introduz onde devia elevar) → troca o enquadramento de "novo no mundo" para "melhor que os existentes". Re-entrada: construída e diferenciada a tabela, o gate é re-submetido. O agente não tem veto; sinaliza ao `positioning-lead-strategist` o contraste pronto para o lead.

## Links
- Frameworks: [`unique-mechanism`](../../frameworks/unique-mechanism.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`mechanism-architect`](../../agents/mechanism-architect.md) · [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`big-idea-architect`](../../agents/big-idea-architect.md)
- Diferenciação verificada contra: [`market-competitor-evidence-gate`](../market/market-competitor-evidence-gate.md)
- Reposiciona a culpa de: [`avatar-objection-map-gate`](../avatar/avatar-objection-map-gate.md)
- Gate seguinte (frase): [`mechanism-one-sentence-gate`](mechanism-one-sentence-gate.md)
