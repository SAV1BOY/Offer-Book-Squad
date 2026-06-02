---
id: data.risk-assumptions.risk-log-template
title: "Log de Riscos (EXEMPLO ILUSTRATIVO / Template)"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
produces: [data.registry.decision]
frameworks: [scarcity-urgency-engine, money-model-sequence]
checklists: [offer-book-stack/offer-book-dod-gate]
registries: [decision-registry, offer-registry]
tags: [template, risk, mitigation, probability, impact, owner]
---

# Log de Riscos (EXEMPLO ILUSTRATIVO / Template)

> **AVISO:** Este arquivo é um **template ilustrativo (seed)**. Os riscos e os donos são **fictícios**, só para mostrar o formato. Não use como fato. Cada lançamento real copia este log, renomeia para `risk-log-<caso>.md`, apaga o aviso e registra uma linha por risco.

## Como usar
- **Agente dono:** [`offerbook-chief`](../../agents/offerbook-chief.md) (prioriza a mitigação); cada risco tem um **dono nomeado** que executa a mitigação. O [`knowledge-librarian`](../../agents/knowledge-librarian.md) consolida o log na memória.
- **Task:** atualizado ao longo de todo o lançamento, sempre que um risco aparece ou muda de estado; revisado no DoD pelo [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md).
- **Quando:** uma linha por risco, desde o intake. Risco aceito como trade-off liga à decisão no [`decision-registry`](../registries/decision-registry.md). Flags de risco de entrada vêm do Advisory Board (`config.yaml: cross_squad.advisory_board_squad`).
- Probabilidade e impacto em escala simples (baixa/média/alta). Risco sem `dono` ou sem `mitigação` = linha incompleta = não conta.

## Campos & Instruções
- **{{RISCO}}** — o que pode dar errado, em uma frase clara.
- **{{PROBABILIDADE}}** — `baixa` \| `média` \| `alta` (chance de acontecer).
- **{{IMPACTO}}** — `baixo` \| `médio` \| `alto` (dano se acontecer).
- **{{MITIGACAO}}** — a ação concreta que reduz a probabilidade ou o impacto.
- **{{DONO}}** — o agente responsável pela mitigação (id de [`config.yaml`](../../config.yaml)).
- **{{STATUS}}** — `aberto` \| `mitigado` \| `aceito` \| `materializado`.

## O Template
```
# LOG DE RISCOS — {{CASO}}
Owner: offerbook-chief · Atualizado: {{DATA}}

| risco | probabilidade | impacto | mitigação | dono | status |
|-------|---------------|---------|-----------|------|--------|
| {{RISCO}} | {{PROBABILIDADE}} | {{IMPACTO}} | {{MITIGACAO}} | {{DONO}} | {{STATUS}} |
```

## Exemplo preenchido
> **# LOG DE RISCOS — Método X**
> Owner: offerbook-chief · Atualizado: 2026-06-02
>
> | risco | probabilidade | impacto | mitigação | dono | status |
> |---|---|---|---|---|---|
> | Presença ao vivo abaixo de 40% _(ex.)_ | média | alto | SMS de "estamos ao vivo" + lembrete 1h antes | launch-producer | mitigado |
> | CAC acima de R$ 600 corrói a margem _(ex.)_ | média | alto | front-end liquida o CAC; cortar criativo fraco cedo | unit-economics-stack-analyst | aberto |
> | Claim de resultado sem prova suficiente _(ex.)_ | baixa | alto | toda claim ligada à prova antes da copy; veto se órfã | compliance-auditor | mitigado |
>
> Leitura: cada risco tem probabilidade, impacto, uma mitigação **executável** e um dono nomeado. O risco de CAC fica `aberto` porque depende de dado de mídia ainda em coleta; quando aceito como trade-off, liga à decisão no [`decision-registry`](../registries/decision-registry.md). O risco de claim órfã é porteira de compliance (`truthful_scarcity` e lastro).

## DoD do entregável
O log está pronto quando: (1) cada risco tem probabilidade, impacto, mitigação e **dono nomeado**, sem `{{PLACEHOLDER}}` solto; (2) toda mitigação é uma ação concreta e executável, não intenção vaga; (3) o `dono` resolve para um agente real de [`config.yaml`](../../config.yaml); (4) risco aceito como trade-off aponta para a decisão no [`decision-registry`](../registries/decision-registry.md); (5) riscos de claim ou escassez passam pela porteira do `compliance-auditor`, alinhados à [política de compliance](../../docs/compliance-policy.md); (6) o texto está em voz ativa e presente, 3ª série. O log é revisado no [`offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) e consolidado na memória pelo `knowledge-librarian`.
