---
id: framework.avatar-voc-investigator.voc-mining
title: "VOC Mining — Mineração da Voz do Cliente"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
frameworks: [avatar-voc-investigator.objection-belief-mapping, positioning.jtbd, copy.one-sentence-persuasion, awareness-x-sophistication]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
  - "Robert Collier, *The Robert Collier Letter Book* (1937)."
  - "Robert B. Cialdini, *Pre-Suasion* (2016)."
tags: [voc, voice-of-customer, verbatim, research, avatar, mining]
---

# VOC Mining — Mineração da Voz do Cliente

## TL;DR
VOC Mining é a coleta sistemática da **linguagem literal** que o avatar usa para descrever a dor, o desejo, as tentativas frustradas e as objeções. Você não inventa a copy — você **minera** as palavras exatas do cliente em reviews, fóruns, comentários, entrevistas e suporte, e devolve essas palavras na peça. A régua de Collier: entre na conversa que já acontece na mente dele. Vence como **primeiro passo** de toda inteligência de copy: sem VOC, a copy é suposição. Produz o banco de verbatims que alimenta gancho, dor, promessa e o mapa de objeções.

## Quando usar / Quando não
**Use** no início da D1, antes de mecanismo, Big Idea ou qualquer copy. É a base factual de tudo.
**Use** sempre que entrar em mercado novo, público novo ou quando a copy atual "não conecta" — quase sempre é VOC fraco.
**Use** para validar (não inventar) a emoção dominante e o nível de consciência com evidência real.
**Não use** verbatim de fonte enviesada como única base (só clientes muito satisfeitos, ou só haters) — minere os dois extremos e o meio.
**Não use** paráfrase no lugar do literal nos campos-chave: a força do VOC é a palavra **exata** do cliente, não a sua versão dela.

## Inputs
- As **fontes de voz**: reviews (Amazon, Google, App Store), fóruns/Reddit/grupos, comentários de concorrentes, transcrições de entrevistas, tickets de suporte, pesquisas, DMs.
- O **produto/categoria** e a lista de **concorrentes** (para minerar a voz do público deles).
- As **dimensões a preencher**: dor, desejo/resultado dos sonhos, tentativas frustradas, objeções, gatilhos de compra, linguagem/jargão próprio, emoção.
- O handoff do `deepresearch_squad` quando houver (VOC + competitor intel — ver [`../../config.yaml`](../../config.yaml) cross_squad).

## Procedimento
1. **Defina as fontes e a cota** — escolha 5+ fontes e mire ≥30 trechos brutos (o gate exige ≥10 verbatims no banco final). Inclua fontes positivas **e** negativas.
2. **Colete trechos literais** — copie a frase exata do cliente (com a marca da fonte), sem editar. Preserve gírias, erros e ênfase: é assim que ele fala.
3. **Classifique por dimensão** — etiquete cada trecho: Dor / Desejo / Tentativa frustrada / Objeção / Gatilho de compra / Linguagem própria / Emoção.
4. **Agrupe por tema** — junte trechos que dizem a mesma coisa. A frequência de um tema indica a **dor/desejo dominante**.
5. **Extraia a emoção dominante** — identifique a emoção que mais aparece nos trechos de dor (frustração, medo, vergonha, raiva, esperança). Valide com contagem, não com palpite (gate `avatar/avatar-dominant-emotion-gate`).
6. **Monte frases-âncora** — destaque os 10-20 verbatims mais fortes e específicos para reúso direto na copy (gancho, dor, promessa).
7. **Cruze com consciência** — use a linguagem para inferir o nível de consciência dominante (fala da vida = inconsciente; fala da dor = consciente do problema; compara soluções = consciente da solução) — ver [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md).
8. **Encaminhe ao mapa de objeções** — passe os trechos de Objeção ao [`objection-belief-mapping`](objection-belief-mapping.md).
9. **Registre** o banco no template de VOC e no `objection-registry` (objeções).

## Outputs
- Um **banco de VOC** com ≥10 verbatims literais (alvo 30+), classificados por dimensão e marcados pela fonte (gate `avatar/avatar-voc-verbatim-gate`).
- A **emoção dominante** validada por frequência.
- As **frases-âncora** (10-20) prontas para a copy.
- O **nível de consciência** inferido com evidência.
- Entrada para o [`objection-belief-mapping`](objection-belief-mapping.md) e para o `avatar-icp-template`.

## Exemplo
Oferta de amostra: app de finanças para autônomos. Verbatims minerados (fonte entre colchetes):
- **Dor** [review concorrente]: "Eu ganho bem mas todo mês fico no zero e não sei explicar pra onde foi."
- **Vergonha/emoção** [fórum]: "Tenho vergonha de dizer que fatura 12 mil e vive no cheque especial."
- **Tentativa frustrada** [Reddit]: "Já baixei mil planilhas, abandono na segunda semana toda vez."
- **Objeção** [comentário]: "Mais um app de finanças? Já tentei e não muda nada."
- **Linguagem própria**: "misturar o dinheiro", "tirar pró-labore", "mês de vacas magras".
- **Síntese**: emoção dominante = **vergonha + frustração**; consciência = **2 (problema)**; frase-âncora para gancho = "Você ganha bem e ainda fica no zero — e não sabe explicar por quê."

## Armadilhas
- **Inventar a voz.** Escrever o que você **acha** que o cliente diz. A copy de suposição falha. Minere o literal.
- **Parafrasear o literal.** "Otimizar finanças" no lugar de "misturar o dinheiro" perde a força do reconhecimento. Use a palavra dele.
- **Fonte enviesada.** Só reviews 5 estrelas (ou só os raivosos) distorce. Minere positivos, negativos e neutros.
- **Emoção por palpite.** Declarar "a emoção é medo" sem contagem fura o gate. Valide por frequência.
- **Cota baixa.** Menos de 10 verbatims não sustenta o avatar. Mire 30+ para ter densidade.
- **Não classificar.** Pilha de trechos sem dimensão não vira inteligência. Etiquete e agrupe.

## Interações
- **Agentes**: `avatar-voc-investigator` (dono — minera e classifica), `market-sophistication-analyst` (usa a voz para diagnosticar consciência/sofisticação), `big-idea-architect` (extrai sonho e inimigo dos verbatims), `vsl-webinar-scriptwriter` e `ad-creative-factory` (usam as frases-âncora), `proof-credibility-curator` (cruza objeção com prova necessária).
- **Frameworks que pareiam**: [`objection-belief-mapping`](objection-belief-mapping.md) (recebe as objeções), [`dmu-mapping-b2b`](dmu-mapping-b2b.md) (em B2B, VOC por papel do comitê), [`positioning/jtbd`](../positioning/jtbd.md) (o "trabalho" por trás do desejo), [`../copy/one-sentence-persuasion.md`](../copy/one-sentence-persuasion.md) (sonho/medo/suspeita/inimigo saem do VOC), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md).

## Fontes
> **Fonte:** Princípio de "entrar na conversa da mente do cliente" de Robert Collier, *The Robert Collier Letter Book* (1937); estados de consciência de Eugene M. Schwartz, *Breakthrough Advertising* (1966); priming de linguagem em Robert B. Cialdini, *Pre-Suasion* (2016) — via [`../../reference/books/copywriting/collier-letter-book.md`](../../reference/books/copywriting/collier-letter-book.md), [`../../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../../reference/books/copywriting/schwartz-breakthrough-advertising.md) e [`../../reference/books/persuasion-psychology/cialdini-presuasion.md`](../../reference/books/persuasion-psychology/cialdini-presuasion.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
