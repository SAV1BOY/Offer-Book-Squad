---
id: checklist.market.market-starving-crowd-gate
title: "Gate — Multidão Faminta Provada (Dor × Poder de Compra × Alcance, com veredito vai/não-vai)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
frameworks: [starving-crowd]
registries: [offer-registry]
tags: [gate, market, starving-crowd, halbert, d1, dor, poder-de-compra]
---

# Gate — Multidão Faminta Provada

## Propósito
Este gate prova que o mercado escolhido tem **fome real** antes de qualquer palavra de copy, conforme a parábola da *starving crowd* de Halbert: a melhor oferta para uma multidão sem fome ainda falha. Existe porque é o portão de entrada do squad — se o mercado não tem dor aguda, poder de compra e alcance, nenhum mecanismo ou Big Idea salva o lançamento. O `market-sophistication-analyst` pontua as três dimensões (0-10 cada) com evidência por nota, e o veredito vai/não-vai precede o diagnóstico fino. O erro clássico é confundir **interesse** (curiosidade) com **fome** (dor que faz gastar). Este gate força a prova de que a multidão paga, não só de que ela existe.

## Dono & Escopo
- **owner_agent:** `market-sophistication-analyst` (aplica o framework [`starving-crowd`](../../frameworks/starving-crowd.md) como portão de entrada).
- **Artefato inspecionado:** o **bloco starving-crowd** do market-brief (Dor / Poder de compra / Alcance + soma + veredito), referenciado pela oferta-semente no [`offer-registry`](../../data/registries/offer-registry.md).

## Condição de Passagem
O mercado-alvo tem nota tripla (Dor, Poder de compra, Alcance) com evidência por nota e um veredito vai/não-vai acima do piso de corte declarado.

## Itens
1. **Três dimensões pontuadas (0-10).** Verificar: Dor, Poder de compra e Alcance têm cada uma uma nota de 0 a 10 — nenhuma em branco.
2. **Evidência por nota.** Verificar: cada uma das três notas cita a evidência que a justifica (reviews de dor aguda, histórico de gasto na categoria, tamanho/coesão dos grupos onde a multidão se reúne).
3. **Poder de compra provado por gasto.** Verificar: a nota de Poder de compra se apoia em **histórico de gasto** na categoria, não em promessa ou intenção declarada.
4. **Soma e piso declarados.** Verificar: o brief soma as três notas e compara com uma regra de corte explícita (o piso de "vai").
5. **Veredito binário.** Verificar: o brief declara `vai` ou `não-vai` — sem meio-termo.
6. **Dor distinta de interesse.** Verificar: o brief mostra que a Dor é aguda o bastante para mover dinheiro, não mera curiosidade.
7. **Mercado-alvo recortado.** Verificar: quando há candidatos, a starving-crowd escolhe qual atacar primeiro, e o recorte está nomeado.

## Evidência Exigida
Para marcar cada item ✅, linkar o bloco starving-crowd do market-brief com as três notas, a evidência de cada uma, a soma, o piso e o veredito. A nota de Poder de compra precisa linkar prova de gasto real (preços praticados, volume da categoria, histórico de compra), não intenção. O permalink do brief e da linha do [`offer-registry`](../../data/registries/offer-registry.md) contam como evidência.

## Protocolo de Falha
Item vermelho → o `market-sophistication-analyst` reavalia a dimensão fraca com mais evidência; nota sem lastro não passa. Veredito `não-vai` (nenhum candidato passa o piso) → o analista **sinaliza ao `offerbook-chief`** recomendando "não escrever ainda — mudar o mercado ou a oferta"; a decisão de parar é do chief. Interesse confundido com fome → reavalia o Poder de compra exigindo histórico de gasto. Mercado quente que esfriou → marca a validade do diagnóstico e recomenda reavaliar. Re-entrada: refeita a nota com evidência, o gate é re-submetido. Lembrete: a starving-crowd **antecede**, não substitui, os gates de sofisticação e consciência.

## Links
- Frameworks: [`starving-crowd`](../../frameworks/starving-crowd.md)
- Registries: [`offer-registry`](../../data/registries/offer-registry.md)
- Agentes: [`market-sophistication-analyst`](../../agents/market-sophistication-analyst.md) · [`offerbook-chief`](../../agents/offerbook-chief.md)
- Gate par (tamanho): [`market-sizing-gate`](market-sizing-gate.md)
- Diagnóstico fino que ele antecede: [`market-sophistication-gate`](market-sophistication-gate.md)
