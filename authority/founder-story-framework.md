---
id: authority.founder-story-framework
title: "Framework da História Fundadora"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pr-brand-strategist
tags: [authority, founder-story, narrative, credibility, origin, proof]
---

# Framework da História Fundadora

## Propósito

Este arquivo estrutura a **história fundadora como prova de autoridade**. A história de origem responde a pergunta silenciosa do avatar: "por que devo ouvir você?". Quando o fundador viveu o problema do avatar e achou a saída, a história deixa de ser autopromoção e vira evidência — prova de que o mecanismo nasceu da dor real, não de um slide. É a forma mais humana de credibilidade.

O dono é o [`pr-brand-strategist`](../agents/pr-brand-strategist.md), em parceria com o [`proof-credibility-curator`](../agents/proof-credibility-curator.md), que liga cada afirmação factual da história a uma prova. A regra: a história é verdadeira e cada número dentro dela tem lastro. "Faturei sete dígitos" exige fonte como qualquer outro claim — sem ela, o trecho vira veto do [`compliance-auditor`](../agents/compliance-auditor.md).

A história alimenta a abertura da VSL, a bio do [`media-kit.md`](media-kit.md), o pitch de PR e a página de origem. Ela cria conexão antes da prova fria de resultado entrar. Bem contada, ela transfere a autoridade da jornada para a oferta.

## Estrutura / Schema

A história fundadora segue beats. Registre cada beat e sua prova:

| Campo | O que registrar |
|---|---|
| `story_id` | slug único, ex.: `founder-story-v1` |
| `origin_pain` | a dor inicial — o mesmo problema do avatar |
| `failed_attempts` | o que o fundador tentou e falhou (gera identificação) |
| `turning_point` | a virada — descoberta do mecanismo |
| `mechanism_link` | ref ao mecanismo único da oferta |
| `transformation` | o resultado do fundador (com prova) |
| `result_ids` | refs a números em [`results-database.md`](results-database.md) |
| `mission` | por que ajuda outros agora (a ponte para o avatar) |
| `claim_ids` | claims factuais da história no [`claim-registry`](../data/registries/claim-registry.md) |
| `proof_ids` | provas que sustentam cada afirmação |

### Esqueleto da história (beats)

```
1. Eu estava onde você está — {{origin_pain}}
2. Tentei de tudo — {{failed_attempts}}
3. Então descobri — {{turning_point}} → {{mechanism_link}}
4. Mudou tudo — {{transformation}} (fonte: {{result_ids}})
5. Hoje minha missão é — {{mission}} (a ponte para você)
```

## Como coletar & verificar

1. Entreviste o fundador para extrair os beats reais — foque na dor de origem e no momento de virada.
2. Para cada afirmação factual (números, prazos, marcos), registre um `claim_id` e ligue a uma `proof_id`.
3. Ligue o resultado do fundador a uma linha verificável em [`results-database.md`](results-database.md).
4. Conecte o `turning_point` ao mecanismo único da oferta — a história prova a origem do mecanismo.
5. Marque trechos sem prova como "narrativo" e mantenha-os livres de números não verificáveis.

## Regras de uso & compliance

- Cada número na história tem lastro; afirmação factual sem prova = **veto** do [`compliance-auditor`](../agents/compliance-auditor.md).
- Resultado do fundador é atípico por natureza — exige disclaimer "resultados variam", conforme [`../docs/compliance-policy.md`](../docs/compliance-policy.md).
- Nada de inventar ou dramatizar fatos; emoção real é permitida, distorção de fato não.
- A história não promete que o avatar terá o mesmo resultado; ela explica a origem do mecanismo.
- Setores regulados: a jornada não vira promessa de cura ou de ganho.

## Liga com

- [`results-database.md`](results-database.md) — os números do fundador, verificáveis.
- [`credibility-builders.md`](credibility-builders.md) e [`media-kit.md`](media-kit.md) — a bio nasce daqui.
- [`proof-asset-index.md`](proof-asset-index.md) — provas da história entram no índice-mestre.
- Agentes: [`pr-brand-strategist`](../agents/pr-brand-strategist.md) (dono), [`proof-credibility-curator`](../agents/proof-credibility-curator.md) (lastro), [`compliance-auditor`](../agents/compliance-auditor.md) (veto). A abertura é usada pelo [`vsl-webinar-scriptwriter`](../agents/vsl-webinar-scriptwriter.md).
- Registries: [`claim-registry`](../data/registries/claim-registry.md), [`proof-registry`](../data/registries/proof-registry.md).
- Framework: [`proof-to-claim-chain`](../frameworks/proof-to-claim-chain.md).
