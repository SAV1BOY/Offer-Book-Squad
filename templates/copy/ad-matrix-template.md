---
id: template.copy.ad-matrix
title: "Ad Matrix — Schema da Matriz de Ângulos de Anúncio"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: ad-creative-factory
consumes: [template.core.offer-book-master, template.copy.ad-matrix-creative]
produces: [data.registry.control]
frameworks: [copy.hook-frameworks, copy.aida, copy.fascination-bullets, awareness-x-sophistication]
checklists: [ad/ad-angle-coverage-gate, compliance/truthful-scarcity-and-claims-gate]
registries: [control-registry, big-idea-registry, objection-registry]
tags: [template, csv-schema, ad, matrix, angles, testing]
---

# Ad Matrix — Schema da Matriz de Ângulos de Anúncio

Este `.md` documenta o schema de [`ad-matrix-template.csv`](ad-matrix-template.csv), a **matriz de ângulos** que a fábrica de criativos usa para gerar e testar anúncios: uma linha por ângulo, com gancho, headline, corpo, CTA, tipo de lead e a hipótese que o teste prova. Cada ângulo é uma aposta diferente sobre o que move o avatar — a matriz organiza o teste sistemático em vez de criativos avulsos.

## Como usar
- **Agente dono:** `ad-creative-factory`. Lido pelo `vsl-webinar-scriptwriter` (o ângulo vencedor vira gancho de VSL) e pelo `compliance-auditor` (claim de ad tem lastro?).
- **Task:** `produce-ad-creatives`. Preencha a matriz **primeiro** (os ângulos), depois expanda cada linha em variações no [`ad-matrix-creative`](ad-matrix-template.md) — peça à fábrica. A matriz garante diversidade de ângulo e leitura de teste.
- **Como editar o CSV:** primeira linha = header `snake_case`, **não traduza nem reordene**. Uma linha por ângulo. Campos com vírgula entre aspas. Sem comentário no CSV (a doc vive aqui).
- Varie o **ângulo** (dor, mecanismo, prova, identidade) e o **lead_type** ([`lead-types`](../../lib/taxonomies/lead-types.md)) para cobrir níveis de [consciência](../../lib/taxonomies/awareness-levels.md). Cada linha carrega **uma** hipótese testável — é o que faz a matriz aprender.

## Campos & Instruções
| Coluna | Tipo | Valores aceitos | Agente-fonte | Exemplo |
|---|---|---|---|---|
| `angulo` | string | o ângulo do criativo (dor, mecanismo, prova, identidade, objeção, comparação) | ad-creative-factory | `Mecanismo janela 72h` |
| `hook` | string | a primeira frase que para o scroll ([`hook-frameworks`](../../frameworks/copy/hook-frameworks.md)) | ad-creative-factory | `"Existe uma janela de 72h que devolve a venda perdida"` |
| `headline` | string | o título do anúncio (curto, específico) | ad-creative-factory | `"A janela de 72 horas"` |
| `corpo` | string | o corpo do anúncio — dor/mecanismo/prova + ponte para a oferta | ad-creative-factory | `"O motivo do carrinho abandonado não é preço. É timing..."` |
| `cta` | string | a chamada para ação, na voz do avatar ([`cta-block`](../../lib/components/cta-block.md)) | ad-creative-factory | `"Quero meu diagnóstico por R$27"` |
| `lead_type` | enum | um dos 6 [tipos de lead](../../lib/taxonomies/lead-types.md): `oferta` `promessa` `problema-solucao` `segredo` `proclamacao` `historia` | positioning-lead-strategist | `segredo` |
| `hipotese_teste` | string (slug) | a hipótese que este criativo prova ("dor explícita bate mais que mecanismo") | ad-creative-factory | `curiosidade-de-mecanismo-vence-publico-morno` |

## O Template
O artefato é o CSV. Mantenha o header idêntico ao de [`ad-matrix-template.csv`](ad-matrix-template.csv).

```csv
angulo,hook,headline,corpo,cta,lead_type,hipotese_teste
{{ANGULO}},"{{HOOK}}","{{HEADLINE}}","{{CORPO}}","{{CTA}}",{{LEAD_TYPE}},{{HIPOTESE}}
```

## Exemplo preenchido
Matriz de amostra (Motor de Recuperação 72h), quatro ângulos:

```csv
angulo,hook,headline,corpo,cta,lead_type,hipotese_teste
Dor do carrinho,"Voce ve o dinheiro escapar no checkout e nao sabe recuperar","O lucro que seu checkout esconde","60% dos carrinhos sao abandonados. As primeiras 72h concentram 80% da receita recuperavel. O Motor 72h captura essa janela sem mais trafego.","Quero meu diagnostico por R$27",problema-solucao,dor-explicita-bate-mais-que-mecanismo
Mecanismo janela 72h,"Existe uma janela de 72 horas que devolve a venda perdida","A janela de 72 horas",O motivo do carrinho abandonado nao e preco. E timing. Uma sequencia cronometrada nas primeiras 72h recupera ate +18% da receita.,"Ver como funciona",segredo,curiosidade-de-mecanismo-vence-publico-morno
Prova 142 lojas,"142 lojas recuperaram +21% de receita sem aumentar trafego","+21% de receita em 142 lojas","Sem novo anuncio. Sem desconto. So uma sequencia de 7 mensagens no momento certo. Mediana de +21% em 30 dias.","Quero esse resultado",promessa,prova-numerica-derruba-ceticismo
Identidade lojista,"Lojista bom nao deixa venda morrer no carrinho","Pare de doar suas vendas",Todo dia que passa sem recuperar carrinho e dinheiro que vai pro concorrente. Vire o lojista que fecha a torneira.,"Garantir minha vaga",proclamacao,frame-de-identidade-engaja-publico-frio
```

Leitura: quatro ângulos distintos (dor, mecanismo, prova, identidade), cada um com um lead diferente que casa com um nível de consciência, e cada linha carrega uma hipótese clara para o teste decidir o vencedor.

## DoD do entregável
A matriz está pronta quando: (1) o header do CSV é idêntico ao schema, em `snake_case`, sem coluna renomeada; (2) há ≥3 ângulos **distintos** (não três variações do mesmo) — `ad-angle-coverage-gate` verde; (3) cada `lead_type` cita um dos 6 [tipos](../../lib/taxonomies/lead-types.md) e os ângulos cobrem mais de um nível de [consciência](../../lib/taxonomies/awareness-levels.md); (4) cada linha tem **uma** `hipotese_teste` clara e isolável (a matriz existe para aprender); (5) todo claim de número no `corpo`/`headline` tem lastro no [`proof-registry`](../../data/registries/proof-registry.md) e passa pelo `compliance-auditor` (`truthful-scarcity-and-claims-gate` verde); (6) cada `hook` para o scroll e cada `cta` aponta uma ação única; (7) os ângulos derivam da Big Idea travada ([`big-idea-registry`](../../data/registries/big-idea-registry.md)) e atacam objeções do [`objection-registry`](../../data/registries/objection-registry.md); (8) o CSV está limpo (sem comentário, sem frontmatter) e os resultados de teste alimentam o [`control-registry`](../../data/registries/control-registry.md).
