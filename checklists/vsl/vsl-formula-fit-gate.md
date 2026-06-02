---
id: checklist.vsl.vsl-formula-fit-gate
title: "Gate — Fit de Fórmula (a estrutura certa para o formato e o lead)"
type: gate
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [copy/vsl-structure, launch/perfect-webinar, copy/pas, copy/pastor, copy/slippery-slide]
registries: [control-registry]
tags: [gate, vsl, webinar, estrutura, formula, slippery-slide, d4]
---

# Gate — Fit de Fórmula

## Propósito
Este gate prova que o roteiro usa **a estrutura certa para o formato e para o lead travado** — e que ela tem os três blocos no lugar. VSL, webinar, recap VSL e sales letter não compartilham a mesma fórmula: um webinar segue o Perfect Webinar (one-thing + quebra das três crenças + stack); uma VSL segue o esqueleto de três blocos com a slippery slide por cima. O gate força o esqueleto-mestre — Gancho & Promessa (captura a atenção), Conteúdo & Mecanismo (conquista a crença), Oferta & Fechamento (converte a ação) — e exige que a abertura herde o **lead travado** pelo [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md): o roteirista não inventa a abertura. Acima de tudo, ele checa a **slippery slide**: cada beat existe para fazer consumir o próximo (Sugarman). Um trecho que faz parar é um vazamento; o gate o reprova. Sem fit de fórmula, os outros gates de VSL fiscalizam um roteiro mal-estruturado.

## Dono & Escopo
- **owner_agent:** `vsl-webinar-scriptwriter` (sem poder de veto; toda saída passa pelo [`voice-style-guardian`](../../agents/voice-style-guardian.md), que **tem veto de voz**).
- **Artefato inspecionado:** o roteiro (VSL/webinar/recap/sales letter) e seus blocos `b1_gancho/b2_mecanismo/b3_oferta` registrados no [`control-registry`](../../data/registries/control-registry.md), montados a partir de [`vsl-structure`](../../frameworks/copy/vsl-structure.md) ou [`perfect-webinar`](../../frameworks/launch/perfect-webinar.md), com o lead travado herdado do posicionamento.

## Condição de Passagem
O roteiro segue a fórmula correta do seu formato, tem os três blocos no lugar, abre pelo lead travado e desliza sem freio do gancho ao CTA.

## Itens
1. **Fórmula certa para o formato.** Verificar: webinar usa Perfect Webinar; VSL/sales letter usa o esqueleto de três blocos — a estrutura registrada bate com o tipo de asset.
2. **Bloco 1 — Gancho & Promessa.** Verificar: abre pelo **lead travado**, faz a grande promessa da Big Idea e nomeia o vilão — não abre pela oferta.
3. **Bloco 2 — Conteúdo & Mecanismo.** Verificar: entrega o mecanismo único como nova oportunidade e quebra/reconstrói as crenças (veículo, interno, externo).
4. **Bloco 3 — Oferta & Fechamento.** Verificar: empilha valor, ancora preço depois, reverte risco e fecha com CTA — na ordem certa.
5. **Lead herdado, não inventado.** Verificar: a abertura corresponde ao `lead_type` travado pelo posicionamento (Segredo, Oferta, Promessa, etc.).
6. **Slippery slide sem freio.** Verificar: ao fim de cada beat, ele puxa o próximo (open loop/transição); nenhum trecho faz o leitor/ouvinte parar.
7. **Ordem de crença defensável.** Verificar: a sequência de quebra de crença começa pela crença-raiz que destrava as demais (Tree-of-Thoughts do agente).

## Evidência Exigida
Para marcar ✅: linkar o roteiro no `control-registry` com os três blocos identificados e a fórmula do formato (itens 1–4, 7), o `lead_type` herdado do posicionamento (item 5) e a verificação da slippery slide — os pontos de transição que evitam parada (item 6).

## Protocolo de Falha
Item vermelho → o `vsl-webinar-scriptwriter` reescreve o bloco com defeito (não remenda): repõe o mecanismo no Bloco 2, move o stack para o Bloco 3, troca a fórmula se o formato pede. Abertura sem lead → devolve ao [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) (não inventa). Trecho que freia a slippery slide → corta ou reescreve com open loop. Re-entrada: atualiza o roteiro no `control-registry` e re-submete ao [`voice-style-guardian`](../../agents/voice-style-guardian.md). Máximo de 2 passes de reescrita antes de escalar ao chief.

## Links
- Gates irmãos: [`vsl-value-before-price-gate`](vsl-value-before-price-gate.md) · [`vsl-risk-reversal-gate`](vsl-risk-reversal-gate.md) · [`vsl-urgency-gate`](vsl-urgency-gate.md) · [`vsl-cta-strength-gate`](vsl-cta-strength-gate.md)
- Frameworks: [`vsl-structure`](../../frameworks/copy/vsl-structure.md) · [`perfect-webinar`](../../frameworks/launch/perfect-webinar.md) · [`pas`](../../frameworks/copy/pas.md) · [`pastor`](../../frameworks/copy/pastor.md) · [`slippery-slide`](../../frameworks/copy/slippery-slide.md)
- Registries: [`control-registry`](../../data/registries/control-registry.md)
- Agentes: [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) · [`positioning-lead-strategist`](../../agents/positioning-lead-strategist.md) · [`voice-style-guardian`](../../agents/voice-style-guardian.md)
- Depende de: [`offer-book-dod-gate`](../offer-book-stack/offer-book-dod-gate.md) (HARD STOP)
