---
id: template.growth.affiliate-prizes
title: "Affiliate Prizes — Schema da Planilha de Prêmios por Faixa"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: affiliate-program-architect
consumes: [template.growth.affiliate-program, template.offer.products-and-offers]
produces: [data.registry.decision]
frameworks: [launch/affiliate-army, money-model-sequence, launch/cart-open-close]
checklists: [affiliate-program-checklist, compliance-checklist]
registries: [decision-registry]
tags: [template, csv-schema, affiliate-prizes, premios, leaderboard, tier, growth]
---

# Affiliate Prizes — Schema da Planilha de Prêmios

Este `.md` documenta o schema de [`affiliate-prizes-template.csv`](affiliate-prizes-template.csv), a **planilha de prêmios** do programa de afiliados: cada faixa (tier) com a meta de vendas que a destrava, o prêmio, a turma (cohort) e o estado. Uma linha por faixa. O CSV é a fonte de verdade do leaderboard de prêmios; este documento explica cada coluna. O `affiliate-program-architect` é dono dos dois arquivos, e o resumo das faixas aparece no bloco 6 do [`affiliate-program-template`](affiliate-program-template.md).

## Como usar
- **Agente dono:** [`affiliate-program-architect`](../../agents/affiliate-program-architect.md). Co-lido pelo [`launch-producer`](../../agents/launch-producer.md) (que integra a corrida de prêmios à janela do lançamento) e pelo [`compliance-auditor`](../../agents/compliance-auditor.md) (que confere que cada prêmio é real e entregável).
- **Task:** preenchido em `build-affiliate-program`, junto do [`affiliate-program-template`](affiliate-program-template.md). Lido pelos afiliados (que sabem o que ganham por meta) e pelo financeiro (que provisiona os prêmios).
- **Quando:** o arquiteto define os prêmios assim que a economia do afiliado fecha com o [`money-model-sequence`](../../frameworks/money-model-sequence.md). Aplica o [`affiliate-army`](../../frameworks/launch/affiliate-army.md) para desenhar as faixas que motivam o pico de vendas na janela do [`cart-open-close`](../../frameworks/launch/cart-open-close.md).
- **Como editar o CSV:** abra em editor de texto ou planilha. A primeira linha é o header `snake_case` — **não traduza nem reordene as colunas**. Adicione uma linha por faixa, da menor meta para a maior. Campos com vírgula vão entre aspas (`"..."`). Não ponha comentário no CSV — a documentação vive aqui.
- O gate [`affiliate-program-checklist`](../../checklists/affiliate-program-checklist.md) confere que cada faixa tem meta e prêmio reais. O [`compliance-checklist`](../../checklists/compliance-checklist.md) confere que todo prêmio é entregável (`truthful_scarcity` aplica também aos prêmios).

## Schema
Uma linha por coluna do CSV: nome, tipo, valores aceitos, agente-fonte e exemplo.

| Coluna | Tipo | Valores aceitos | Agente-fonte | Exemplo |
|---|---|---|---|---|
| `tier` | enum (slug) | a faixa de prêmio (bronze, prata, ouro, platina); ordena do menor ao maior | affiliate-program-architect | `prata` |
| `meta_vendas` | número (inteiro) | o número de vendas que destrava a faixa; cresce a cada tier | affiliate-program-architect | `30` |
| `premio` | string | o prêmio da faixa, concreto e entregável | affiliate-program-architect | `"Bônus em dinheiro R$2000 + co-marketing no nosso canal"` |
| `cohort` | string (slug) | a turma/lançamento a que a corrida pertence | affiliate-program-architect | `lancamento-motor-72h` |
| `status` | enum | `planejado` `ativo` `encerrado` `pago` | affiliate-program-architect | `ativo` |

## Exemplo
Planilha de amostra (lançamento do Motor 72h), três faixas preenchidas:

```csv
tier,meta_vendas,premio,cohort,status
bronze,10,"Acesso vitalício ao produto núcleo + selo Bronze",lancamento-motor-72h,planejado
prata,30,"Bônus em dinheiro R$2000 + co-marketing no nosso canal",lancamento-motor-72h,ativo
ouro,75,"Viagem com tudo pago para o evento anual + mentoria 1:1",lancamento-motor-72h,ativo
```

Leitura: as faixas sobem em meta de vendas (10 → 30 → 75), cada uma com um prêmio concreto e entregável. Todas pertencem à mesma turma (`lancamento-motor-72h`), o que permite um leaderboard único. O prêmio cresce com a meta, o que puxa o afiliado a vender mais dentro da janela do lançamento.

## DoD
A planilha está pronta quando: (1) o header do CSV é **idêntico** ao schema, em `snake_case`, sem coluna renomeada ou reordenada; (2) há ≥2 faixas, em ordem crescente de `meta_vendas`, sem meta repetida; (3) cada faixa tem um `premio` concreto e **entregável** pela operação, conferido no [`compliance-checklist`](../../checklists/compliance-checklist.md) — prêmio que não se honra é veto (`truthful_scarcity` vale para prêmios); (4) toda linha pertence a um `cohort` declarado, ligado ao lançamento; (5) a economia das faixas fecha com o [`money-model-sequence`](../../frameworks/money-model-sequence.md) (o prêmio cabe na margem que a venda do afiliado gera); (6) as faixas remetem ao resumo no bloco 6 do [`affiliate-program-template`](affiliate-program-template.md) e passam no [`affiliate-program-checklist`](../../checklists/affiliate-program-checklist.md); (7) o CSV está limpo (sem comentário, sem frontmatter). A estrutura final de prêmios vira decisão no [`decision-registry`](../../data/registries/decision-registry.md).
