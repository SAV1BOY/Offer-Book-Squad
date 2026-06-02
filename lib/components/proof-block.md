---
id: lib.component.proof-block
title: "Bloco de Prova (cada claim com lastro)"
type: component
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
frameworks: [proof-to-claim-chain, value-equation]
tags: [component, proof, credibility, claim-backing, reuse]
---

# Bloco de Prova (cada claim com lastro)

## O que é
O bloco de prova conecta uma **afirmação** (claim) a uma **evidência** que a sustenta. A regra do squad é dura: nenhum claim sem lastro (princípio `evidence_before_opinion`). Um claim sozinho é opinião; um claim com prova é argumento. Este bloco é a unidade que transforma um em outro.

Cada prova tem um **tipo** (depoimento, número, demonstração, estudo, antes-e-depois, autoridade) e uma **força**. Prova forte e específica vence prova vaga. "+21% de receita em 142 lojas" vence "muita gente adorou". O bloco é reutilizável: o mesmo esqueleto cobre qualquer tipo de prova e amarra direto ao [proof-registry](../../data/registries/proof-registry.md) e ao [claim-registry](../../data/registries/claim-registry.md) via [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md).

## Quando usar
- Logo depois de **todo** claim grande na copy — resultado, velocidade, facilidade.
- Para reverter ceticismo em mercado [sofisticado](../taxonomies/sophistication-levels.md), onde promessa pura não basta.
- Como matéria-prima do depoimento por objeção (cada prova fecha uma dúvida).

Não use prova genérica para claim específico. Se o claim diz "30 dias", a prova precisa mostrar "30 dias".

## Bloco
```
CLAIM: "{{AFIRMAÇÃO_EXATA_DA_COPY}}"
TIPO DE PROVA: {{DEPOIMENTO | NÚMERO | DEMONSTRAÇÃO | ESTUDO | ANTES_DEPOIS | AUTORIDADE}}
A PROVA: {{EVIDÊNCIA_CONCRETA_E_ESPECÍFICA}}
FONTE/RASTRO: {{onde_verificar — proof-registry id, print, link, nome}}
FORÇA: {{FRACA | MÉDIA | FORTE}} — por quê: {{justificativa}}

(Claim tem lastro suficiente: {{SIM/NÃO}} — owner: proof-credibility-curator)
```

Preencha cada `{{...}}`. Sem rastro verificável e sem "sim", o claim não vai para a copy — vira passivo de compliance.

## Exemplo preenchido
> CLAIM: *"Você recupera +15% da receita perdida em carrinhos."*
> TIPO DE PROVA: **NÚMERO + ANTES_DEPOIS**.
> A PROVA: **142 lojas usaram a sequência; mediana de +21% de receita recuperada em 30 dias**.
> FONTE/RASTRO: **proof-registry #PR-031; painel exportado em anexo**.
> FORÇA: **FORTE** — amostra grande, número mediano (não cereja), prazo casado com o claim.
> (Claim tem lastro suficiente: **SIM** — dado primário, rastreável.)

A prova é específica, casa com o claim (15% prometido vs 21% provado), tem rastro e força justificada.

## Liga com
- **Frameworks:** [`proof-to-claim-chain`](../../frameworks/proof-to-claim-chain.md) (a corrente claim→prova), [`value-equation`](../../frameworks/value-equation.md) (prova reduz o risco percebido = sobe o valor).
- **Registries:** [`proof-registry`](../../data/registries/proof-registry.md), [`claim-registry`](../../data/registries/claim-registry.md).
- **Agentes:** `proof-credibility-curator` (dono — curadoria e força da prova), `compliance-auditor` (**veta** claim sem lastro), `vsl-webinar-scriptwriter` e `ad-creative-factory` (encaixam prova após cada claim).
