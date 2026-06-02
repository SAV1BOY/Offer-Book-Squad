---
id: checklist.vsl.vsl-cta-strength-gate
title: "Gate — Força do CTA (um único pedido, claro e forte)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [copy/vsl-structure, launch/perfect-webinar, copy/slippery-slide]
registries: [control-registry]
tags: [gate, vsl, cta, power-of-one, fechamento, d4]
---

# Gate — Força do CTA

## Propósito
Este gate prova que o roteiro fecha com **um único pedido, claro e forte**. O fim de uma VSL ou webinar é o momento da ação; um CTA ambíguo, fraco ou múltiplo desperdiça todo o valor empilhado antes dele. O gate aplica o Power of One ao fechamento: um pedido por roteiro. Dois pedidos concorrentes ("compre ou agende uma call ou baixe o material") dividem a decisão e derrubam a conversão. Ele exige que o CTA seja **específico** (o que fazer, onde clicar, o que acontece a seguir), **repetido** nos momentos certos sem virar ruído, e **conectado** à urgência verdadeira da [`vsl-urgency-gate`](vsl-urgency-gate.md) e à reversão de risco da [`vsl-risk-reversal-gate`](vsl-risk-reversal-gate.md). A slippery slide precisa desaguar nele sem freio. É o último beat antes de o roteiro virar página ou evento, e o [`funnel-architect`](../../agents/funnel-architect.md) depende de um destino único para mapear o próximo passo.

## Dono & Escopo
- **owner_agent:** `vsl-webinar-scriptwriter` (sem poder de veto; saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md)).
- **Artefato inspecionado:** o campo `cta_unico` do roteiro no [`control-registry`](../../data/registries/control-registry.md), no fechamento do Bloco 3, conectado à urgência e à garantia, e o destino que o [`funnel-architect`](../../agents/funnel-architect.md) recebe.

## Condição de Passagem
O roteiro fecha com exatamente um pedido, específico e acionável, conectado à urgência verdadeira e à garantia, com a slippery slide desaguando nele sem freio.

## Itens
1. **Um único pedido.** Verificar: o fechamento faz **um** CTA; dois ou mais pedidos concorrentes reprovam (Power of One).
2. **Específico e acionável.** Verificar: o CTA diz exatamente o que fazer e o que acontece (verbo de ação + destino), não "saiba mais".
3. **Conectado à urgência.** Verificar: o pedido amarra-se à escassez verdadeira (consistente com [`vsl-urgency-gate`](vsl-urgency-gate.md)) — agir agora tem um porquê real.
4. **Conectado à garantia.** Verificar: o CTA vem logo após a reversão de risco — o pedido é seguro de aceitar (cruza com [`vsl-risk-reversal-gate`](vsl-risk-reversal-gate.md)).
5. **Repetição sem ruído.** Verificar: o CTA é reforçado nos momentos certos (após o stack, após a garantia, no fim), sem repetição que canse.
6. **Slippery slide deságua nele.** Verificar: o último beat puxa direto para a ação — nenhum trecho freia antes do pedido.
7. **Destino único registrado.** Verificar: o `cta_unico` e seu destino estão no `control-registry`, prontos para o `funnel-architect` mapear.

## Evidência Exigida
Para marcar ✅: linkar o `cta_unico` no `control-registry` com o pedido específico e seu destino (itens 1–2, 7), a conexão com a urgência e a garantia (itens 3–4), o padrão de repetição do CTA (item 5) e a verificação de que a slippery slide deságua no pedido sem freio (item 6).

## Protocolo de Falha
Item vermelho → o `vsl-webinar-scriptwriter` reduz a UM pedido (Power of One no fechamento) e o torna específico. CTA fraco/vago → reescreve com verbo de ação e destino. CTA desconectado da urgência/garantia → reposiciona após a reversão de risco e ancora na escassez real. Re-entrada: corrige `cta_unico` no `control-registry` e re-submete ao [`voice-style-guardian`](../../agents/voice-style-guardian.md). Máximo de 2 passes de reescrita antes de escalar ao chief.

## Links
- Gates irmãos: [`vsl-formula-fit-gate`](vsl-formula-fit-gate.md) · [`vsl-value-before-price-gate`](vsl-value-before-price-gate.md) · [`vsl-risk-reversal-gate`](vsl-risk-reversal-gate.md) · [`vsl-urgency-gate`](vsl-urgency-gate.md)
- Frameworks: [`vsl-structure`](../../frameworks/copy/vsl-structure.md) · [`perfect-webinar`](../../frameworks/launch/perfect-webinar.md) · [`slippery-slide`](../../frameworks/copy/slippery-slide.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) · [`funnel-architect`](../../agents/funnel-architect.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
