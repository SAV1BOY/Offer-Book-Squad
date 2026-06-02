---
id: template.cross-squad.handoff-contract
title: "Contrato de Handoff Cross-Squad — O Acordo Reutilizável da Fronteira"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offer-squad-architect
consumes: [data.registry.decision]
produces: [data.handoffs.handoff-manifest-template, data.registry.decision]
frameworks: [offer-to-funnel-mapping, proof-to-claim-chain, power-of-one, awareness-x-sophistication]
checklists: [cross-squad/cross-squad-handoff-quality, cross-squad/cross-squad-asset-validation, cross-squad/cross-squad-research-request-quality, architect/handoff-contract-gate]
registries: [decision-registry, offer-registry]
tags: [template, contract, handoff, cross-squad, reusable, dod, return-on-reject]
---

# Contrato de Handoff Cross-Squad — O Acordo Reutilizável da Fronteira

Este template produz o **contrato de handoff**: o acordo escrito que rege toda passagem de artefato entre o Offer Book Squad e um squad vizinho. Ele existe porque integração entre squads quebra no contrato — o copy-squad recebe um offer book sem a Big Idea, o advisory recebe uma oferta sem prova, o data-squad entrega pricing sem método. Um handoff só é válido quando o destinatário pode agir **sem voltar a perguntar** (`traceability_before_eloquence`). O contrato nomeia o que será entregue, com que qualidade por campo, sob qual critério de aceite e o que acontece quando o pacote volta. É reutilizável: a mesma estrutura serve a qualquer aresta cross-squad (`config.yaml: cross_squad`).

## Como usar
- **Agente dono:** [`offer-squad-architect`](../../agents/offer-squad-architect.md) (define o contrato de cada handoff; não executa as fases). O [`offerbook-chief`](../../agents/offerbook-chief.md) libera ou segura a passagem; o [`compliance-auditor`](../../agents/compliance-auditor.md) co-assina quando o pacote leva claims.
- **Task:** preenchido sempre que um artefato vai cruzar a fronteira — de saída (ex.: offer book → copy) ou de entrada (ex.: crítica → advisory). Um contrato por aresta.
- **Quando:** antes do handoff acontecer. O contrato preenchido é referenciado em `contract_ref` no [`handoff-manifest-template`](../../data/handoffs/handoff-manifest-template.md) e a passagem só ocorre depois que o gate de fronteira fica verde. As três gates regem a aresta: [`cross-squad-handoff-quality`](../../checklists/cross-squad/cross-squad-handoff-quality.md) (saída), [`cross-squad-asset-validation`](../../checklists/cross-squad/cross-squad-asset-validation.md) (entrada) e [`cross-squad-research-request-quality`](../../checklists/cross-squad/cross-squad-research-request-quality.md) (pedido de pesquisa). O contrato em si é coberto pelo [`handoff-contract-gate`](../../checklists/architect/handoff-contract-gate.md).
- Campo vazio = handoff pela metade = gate vermelho. Cada campo esperado declara a sua **qualidade mínima**, para o downstream calibrar o esforço.

## Campos do contrato
- **{{de_squad}}** — o squad de origem do artefato (nome de `config.yaml: cross_squad`, ex.: `offerbook`).
- **{{para_squad}}** — o squad de destino (ex.: `copy_squad`, `advisory_board_squad`, `data_squad`).
- **{{artefato}}** — o que está sendo passado, nomeado sem ambiguidade (ex.: offer book + Big Idea + banco de prova).
- **{{campos_esperados}}** — a lista de campos que o artefato **já traz** ao chegar (o que o downstream pode contar como pronto).
- **{{qualidade_minima_por_campo}}** — o padrão mínimo de cada campo esperado (ex.: cada claim com `proof_id`; Big Idea única; sofisticação 1–5 declarada).
- **{{dono}}** — o agente responsável pelo artefato de cada lado (quem assina a entrega e quem recebe).
- **{{criterio_de_aceite}}** — a definição de "recebido": o que o destinatário deve **conseguir fazer** com o pacote sem perguntar.
- **{{return_on_reject}}** — o que acontece quando o pacote é rejeitado: para quem volta, com qual defeito nomeado e qual o ponto de re-entrada.
- **{{registry_entry}}** — o `decision_id` da decisão de handoff no [`decision-registry`](../../data/registries/decision-registry.md) e a linha no [`handoff-manifest-template`](../../data/handoffs/handoff-manifest-template.md).

## O Template
```
# CONTRATO DE HANDOFF — {{de_squad}} -> {{para_squad}}
Owner (origem): {{dono}} · Data: {{DATA}} · Direção: {{DIRECAO}} (entrada/saída)

## 1. ARTEFATO
{{artefato}}

## 2. CAMPOS ESPERADOS (o que o pacote já traz)
| Campo esperado | Qualidade mínima |
|----------------|------------------|
| {{campo_1}} | {{qualidade_1}} |
| {{campo_2}} | {{qualidade_2}} |
| {{campo_3}} | {{qualidade_3}} |

## 3. DONO (quem assina cada lado)
Entrega (origem): {{dono_origem}} · Recebe (destino): {{dono_destino}}

## 4. CRITERIO DE ACEITE (a definição de "recebido")
{{criterio_de_aceite}}

## 5. RETURN-ON-REJECT (o que acontece se voltar)
Volta para: {{agente_que_corrige}} · Defeito nomeado: {{defeito}}
Ponto de re-entrada: {{ponto_reentrada}}

## 6. REGISTRO
decided_in: {{registry_entry}} (decision-registry) · manifesto: {{linha_manifesto}}
```

## Exemplo preenchido
> **# CONTRATO DE HANDOFF — offerbook -> copy_squad**
> Owner (origem): offerbook-chief · Data: 2026-06-02 · Direção: saída
>
> **1. ARTEFATO** — Offer Book consolidado + Big Idea travada + banco de prova (`config.yaml: cross_squad.copy_squad.handoff_to_copy`).
>
> **2. CAMPOS ESPERADOS**
> | Campo esperado | Qualidade mínima |
> |---|---|
> | Big Idea | **única** (`power-of-one`), travada e casada à consciência do avatar |
> | Money model | 4 partes sequenciadas, com preço/gatilho/CTA por degrau |
> | Banco de prova | cada claim com `proof_id` ligado no [`proof-registry`](../../data/registries/proof-registry.md) |
> | Diagnóstico de mercado | `sofisticação 1–5` e `consciência 1–5` declaradas ([`awareness-x-sophistication`](../../frameworks/awareness-x-sophistication.md)) |
>
> **3. DONO** — Entrega: offerbook-chief (co-assina compliance-auditor nas claims) · Recebe: copy_squad.
>
> **4. CRITERIO DE ACEITE** — o copy-squad consegue escrever VSL e e-mails **sem voltar a perguntar**: a Big Idea é uma só, cada claim tem prova citável, e o nível de consciência calibra o lead. Se precisar perguntar, o pacote não passou.
>
> **5. RETURN-ON-REJECT** — pacote sem prova ligada volta ao `proof-credibility-curator`; pacote que contradiz a Big Idea volta ao `big-idea-architect`, com o defeito **nomeado**. Re-entrada: corrigir o artefato, atualizar o manifesto e re-submeter como **nova linha** (ex.: `ho-0001` rejeitado → `ho-0002` corrigido).
>
> **6. REGISTRO** — decided_in: `dec-exemplo-0001` no [`decision-registry`](../../data/registries/decision-registry.md) · manifesto: linha `ho-0002-offerbook-copy` no [`handoff-manifest-template`](../../data/handoffs/handoff-manifest-template.md).
>
> Leitura: o contrato diz exatamente o que o copy-squad recebe, com que qualidade por campo, e o que ele precisa conseguir fazer. A passagem só ocorre depois do [`cross-squad-handoff-quality`](../../checklists/cross-squad/cross-squad-handoff-quality.md) verde; a rejeição tem rota de volta e ponto de re-entrada, sem informação órfã.

## DoD
O contrato está pronto quando: (1) `de_squad` e `para_squad` estão nomeados pelos nomes de `config.yaml: cross_squad`, e a direção (entrada/saída) está declarada, sem `{{placeholder}}` solto; (2) o `artefato` é nomeado sem ambiguidade e cada **campo esperado** traz a sua **qualidade mínima** (o downstream sabe o que pode contar como pronto); (3) o `dono` de cada lado está identificado (quem entrega e quem recebe); (4) o `criterio_de_aceite` declara o que o destinatário deve **conseguir fazer sem perguntar** (`traceability_before_eloquence`); (5) o `return_on_reject` nomeia para quem o pacote volta, com qual defeito e qual o ponto de re-entrada; (6) o contrato resolve para um `registry_entry` no [`decision-registry`](../../data/registries/decision-registry.md) e para uma linha no [`handoff-manifest-template`](../../data/handoffs/handoff-manifest-template.md); (7) claims no pacote têm lastro citável e qualquer escassez é **100% verdadeira** (`truthful_scarcity`), alinhada à [política de compliance](../../docs/compliance-policy.md); (8) o texto está em voz ativa e presente, 3ª série. O contrato é coberto pelo [`handoff-contract-gate`](../../checklists/architect/handoff-contract-gate.md) e a passagem pelas três gates de fronteira em [`checklists/cross-squad/`](../../checklists/cross-squad/); o handoff é registrado em [`data/handoffs/`](../../data/handoffs/).
