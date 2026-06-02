---
id: template.copy.sequence-matrix
title: "Sequence Matrix — Schema da Matriz de Sequência de E-mail/SMS"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: email-sms-sequence-writer
consumes: [template.core.offer-book-master, template.copy.email-sms-sequences]
produces: [data.registry.control]
frameworks: [copy.email-sequence-architecture, copy.aida, copy.close-frameworks, launch.cart-open-close]
checklists: [email-sms/email-step-coverage-gate, email-sms/email-segmentation-gate, email-sms/email-timing-gate]
registries: [control-registry, objection-registry]
tags: [template, csv-schema, sequence, email, sms, matrix]
---

# Sequence Matrix — Schema da Matriz de Sequência

Este `.md` documenta o schema de [`sequence-matrix-template.csv`](sequence-matrix-template.csv), a **matriz que planeja a sequência** de e-mail/SMS antes de escrever uma palavra de corpo: uma linha por mensagem, com timing, assunto, canal, lista (segmento) e gatilho. É a saída de planejamento do [`email-sequence-architecture`](../../frameworks/copy/email-sequence-architecture.md) — a sequência é uma narrativa em parcelas, não uma pilha de mensagens.

## Como usar
- **Agente dono:** `email-sms-sequence-writer`. Lido pelo `funnel-architect` (onde a sequência entra no funil) e pelo `compliance-auditor` (escassez do fechamento é real?).
- **Task:** `write-email-sms-sequences`. Preencha a matriz **primeiro** (o plano), depois redija cada mensagem no [`email-sms-sequences`](email-sms-sequences-template.md). A matriz garante cobertura e cadência antes do texto.
- **Como editar o CSV:** primeira linha = header `snake_case`, **não traduza nem reordene**. Uma linha por mensagem, na ordem de envio. Campos com vírgula entre aspas. Sem comentário no CSV (a doc vive aqui).
- Cada mensagem tem **um** trabalho e **um** CTA. Ordene do mais indireto (história) ao mais direto (fechamento). Acelere a frequência no último dia. Segmente por comportamento: quem comprou sai da lista de oferta.

## Campos & Instruções
| Coluna | Tipo | Valores aceitos | Agente-fonte | Exemplo |
|---|---|---|---|---|
| `titulo` | string | rótulo do trabalho do e-mail (indoutrinação, conteúdo-prova, mecanismo, transição, oferta, fechamento) | email-sms-sequence-writer | `E3 Mecanismo + Prova` |
| `timing` | string | dia relativo + hora (`D-3 09h`, `D0 20h`; D0 = dia de fechamento) | email-sms-sequence-writer | `D-1 09h` |
| `subject` | string | a linha de assunto (o gancho; ver [`hook-frameworks`](../../frameworks/copy/hook-frameworks.md)) | email-sms-sequence-writer | `"Vagas abertas: método + roleplay 1:1"` |
| `canal` | enum | `email` `sms` `whatsapp` | email-sms-sequence-writer | `email` |
| `lista` | string (slug) | o segmento que recebe (`lista-quente`, `clicou-e5-nao-comprou`, `nao-abriu`) — segmentação por comportamento | email-sms-sequence-writer | `clicou-e5-nao-comprou` |
| `gatilho` | string (slug) | o evento que dispara o envio (`inscricao-confirmada`, `carrinho-aberto`, `abriu-e2`, `nenhum`) | funnel-architect | `carrinho-aberto` |

## O Template
O artefato é o CSV. Mantenha o header idêntico ao de [`sequence-matrix-template.csv`](sequence-matrix-template.csv).

```csv
titulo,timing,subject,canal,lista,gatilho
{{TITULO}},{{TIMING}},"{{SUBJECT}}",{{CANAL}},{{LISTA}},{{GATILHO}}
```

## Exemplo preenchido
Matriz de amostra (curso de inglês para devs, carrinho aberto-fechado):

```csv
titulo,timing,subject,canal,lista,gatilho
E1 Indoutrinacao Historia,D-5 09h,"Por que devs fluentes em leitura travam na entrevista falada",email,lista-quente,inscricao-confirmada
E2 Conteudo-Prova,D-4 09h,"O metodo Shadowing Tecnico em 1 pagina",email,lista-quente,abriu-e1
E3 Mecanismo + Prova,D-3 09h,"Como o Rafael saiu de R$8k para US$7k/mes",email,lista-quente,abriu-e2
E5 Oferta Abre Carrinho,D-1 09h,"Vagas abertas: metodo + 120 falas + roleplay 1:1",email,lista-quente,carrinho-aberto
E6 Fechamento Manha,D0 09h,"Fecha hoje as 23h59 — e por que sao so 40 vagas",email,clicou-e5-nao-comprou,clicou-e5
E7 Fechamento Ultimas Horas,D0 20h,"Ultimas 4 horas (depois fecha de verdade)",sms,clicou-e5-nao-comprou,nao-comprou-ate-20h
```

Leitura: do indireto (E1 história) ao direto (E7 SMS de fechamento). A frequência sobe no D0 (manhã + noite). A segmentação muda no fechamento: só quem clicou e não comprou recebe E6/E7 — quem comprou já saiu da lista.

## DoD do entregável
A matriz está pronta quando: (1) o header do CSV é idêntico ao schema, em `snake_case`, sem coluna renomeada; (2) há uma linha por mensagem, ordenadas por `timing`, e cada `titulo` declara **um** trabalho único; (3) a cobertura do arco está completa — existe pelo menos indoutrinação/história, conteúdo-prova, mecanismo, oferta e fechamento (`email-step-coverage-gate` verde); (4) cada objeção dominante do [`objection-registry`](../../data/registries/objection-registry.md) é morta por algum e-mail; (5) a `lista` segmenta por comportamento — quem comprou não recebe oferta/fechamento (`email-segmentation-gate` verde); (6) o `timing` acelera no fechamento (≥2 envios no D0) e respeita o calendário de [`cart-open-close`](../../frameworks/launch/cart-open-close.md) (`email-timing-gate` verde); (7) todo `subject` de fechamento que diz "fecha hoje" fecha de verdade (escassez real, aprovada pelo `compliance-auditor`); (8) o CSV está limpo (sem comentário, sem frontmatter) e as variações de assunto alimentam o [`control-registry`](../../data/registries/control-registry.md).
