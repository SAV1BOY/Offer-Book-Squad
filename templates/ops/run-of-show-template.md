---
id: template.ops.run-of-show
title: "Run of Show — Schema do Roteiro Minuto a Minuto do Lançamento"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
consumes: [template.core.offer-book-master, template.ops.launch-phases]
produces: [data.registry.decision]
frameworks: [launch/surge-ops, launch/cart-open-close, launch/perfect-webinar, launch/runway-and-phases]
checklists: [run-of-show-checklist, launch/launch-roles-gate, launch/launch-surge-gate]
registries: [decision-registry, control-registry]
tags: [template, csv-schema, run-of-show, roteiro, ops, surge, lancamento]
---

# Run of Show — Schema do Roteiro Minuto a Minuto

Este `.md` documenta o schema de [`run-of-show-template.csv`](run-of-show-template.csv), o **roteiro minuto a minuto** do dia do lançamento (webinar, live, abertura de carrinho). Uma linha por bloco de tempo, do início ao fim. O CSV é a fonte de verdade da pista; este documento explica cada coluna. O `launch-producer` é dono dos dois arquivos.

## Como usar
- **Agente dono:** `launch-producer`. Co-lido pelo `events-logistics-coordinator` (que prepara a sala e o hosting de cada bloco) e pelo `vsl-webinar-scriptwriter` (dono do bloco de pitch).
- **Task:** preenchido durante a produção do lançamento e lido ao vivo no dia do evento. Cada bloco tem um responsável nomeado e uma ação de contingência (`surge_action`).
- **Quando:** depois que as fases do lançamento existem em [`launch-phases-template`](launch-phases-template.md) e o Offer Book está aprovado. Aplica o [`surge-ops`](../../frameworks/launch/surge-ops.md) para a coluna de contingência e o [`perfect-webinar`](../../frameworks/launch/perfect-webinar.md) para a ordem dos blocos.
- **Como editar o CSV:** abra em editor de texto ou planilha. A primeira linha é o header `snake_case` — **não traduza nem reordene as colunas**. Adicione uma linha por bloco, em ordem de horário. Campos com vírgula vão entre aspas (`"..."`). Horários no formato `HH:MM`. Não ponha comentário no CSV — a documentação vive aqui.
- O gate [`run-of-show-checklist`](../../checklists/run-of-show-checklist.md) confere que todo bloco tem responsável e que cada momento de venda tem `surge_action`. O [`launch-roles-gate`](../../checklists/launch/launch-roles-gate.md) confere que nenhum bloco fica sem dono.

## Schema
Uma linha por coluna do CSV: nome, tipo, valores aceitos, agente-fonte e exemplo.

| Coluna | Tipo | Valores aceitos | Agente-fonte | Exemplo |
|---|---|---|---|---|
| `bloco` | string (slug) | nome do segmento da pista (abertura, conteudo, pitch-da-oferta, perguntas, fechamento) | launch-producer | `pitch-da-oferta` |
| `inicio` | hora (`HH:MM`) | horário de início do bloco, 24h | launch-producer | `19:35` |
| `fim` | hora (`HH:MM`) | horário de fim do bloco, 24h; posterior a `inicio` | launch-producer | `19:50` |
| `responsavel` | ref (agent-id) | o agente ou pessoa que conduz o bloco | launch-producer | `vsl-webinar-scriptwriter` |
| `conteudo` | string | o que acontece no bloco, em uma frase clara | launch-producer | `"revela a oferta e abre o carrinho"` |
| `surge_action` | string (slug) | a ação de contingência se a métrica do bloco desviar ([`surge-ops`](../../frameworks/launch/surge-ops.md)) | launch-producer | `disparar-email-carrinho-aberto` |

## Exemplo
Roteiro de amostra (webinar do Motor 72h), três blocos preenchidos:

```csv
bloco,inicio,fim,responsavel,conteudo,surge_action
abertura,19:00,19:08,launch-producer,"boas-vindas e promessa do dia",monitorar-presenca-ao-vivo
pitch-da-oferta,19:35,19:50,vsl-webinar-scriptwriter,"revela a oferta e abre o carrinho",disparar-email-carrinho-aberto
fechamento,20:10,20:20,launch-producer,"recapitula a oferta e o deadline real",reforcar-escassez-verdadeira-no-chat
```

Leitura: cada bloco tem horário de início e fim, um responsável nomeado, o conteúdo em uma frase e uma `surge_action` pronta. O bloco de pitch tem dono próprio (o scriptwriter) e dispara o e-mail de carrinho aberto se a conversão ao vivo cair.

## DoD
O roteiro está pronto quando: (1) o header do CSV é **idêntico** ao schema, em `snake_case`, sem coluna renomeada ou reordenada; (2) os blocos cobrem a pista inteira em ordem, sem buraco de horário, e `fim > inicio` em cada linha; (3) todo bloco tem `responsavel` nomeado, satisfazendo o [`launch-roles-gate`](../../checklists/launch/launch-roles-gate.md); (4) todo momento de venda ou risco tem `surge_action` real e executável, derivada do [`surge-ops`](../../frameworks/launch/surge-ops.md) e satisfazendo o [`launch-surge-gate`](../../checklists/launch/launch-surge-gate.md); (5) o `conteudo` está em voz ativa e presente, sem `{{placeholder}}` solto; (6) qualquer escassez citada no roteiro é **100% verdadeira** (`truthful_scarcity`), alinhada à [política de compliance](../../docs/compliance-policy.md); (7) o CSV está limpo (sem comentário, sem frontmatter) e passa no [`run-of-show-checklist`](../../checklists/run-of-show-checklist.md). A versão final do roteiro vira uma decisão registrada no [`decision-registry`](../../data/registries/decision-registry.md).
