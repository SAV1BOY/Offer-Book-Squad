---
id: framework.big-idea-architect.big-idea-scoring
title: "Big Idea Scoring — Os 5 Critérios para Travar UMA Ideia"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: big-idea-architect
frameworks: [big-idea-architect.big-idea-ideation-tot, big-idea-architect.promise-hook-villain, power-of-one, big-idea-generator, awareness-x-sophistication]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
  - "David Ogilvy, *Ogilvy on Advertising* (1983)."
  - "Gary Bencivenga, *Bencivenga 7 Secrets*."
tags: [big-idea, scoring, criteria, selection, convergence]
---

# Big Idea Scoring — Os 5 Critérios

## TL;DR
Depois de divergir com [`big-idea-ideation-tot`](big-idea-ideation-tot.md), você converge pontuando cada candidata em **5 critérios**: **Nova** (fresca, não-óbvia), **Grande** (importa de verdade ao avatar), **Crível** (sustentada por mecanismo + prova), **Casa com a consciência** (fit com a célula de Schwartz) e **Única/Possuível** (ninguém mais pode dizer isto). A ideia com a maior soma, sem nota eliminatória, vence — e vira a UMA Big Idea do lançamento. Vence sempre que você precisa **escolher** entre candidatas com critério rastreável em vez de gosto. Alimenta o gate `big-idea/big-idea-new-big-credible-gate`.

## Quando usar / Quando não
**Use** logo após gerar 3-5 candidatas com ToT, para convergir em UMA.
**Use** quando há mais de uma ideia "boa" e a escolha precisa ser defensável (rastreável) ante o `offerbook-chief` e o `compliance-auditor`.
**Use** os critérios também como **checklist de qualidade** de uma única ideia antes de travá-la.
**Não use** para justificar travar duas ideias — o output é sempre UMA (Power of One). Empate resolve-se por fit de consciência.
**Não use** o scoring sem o lastro: "Crível" depende de prova real; sem ela, a nota é fantasia.

## Inputs
- As **3-5 candidatas** do [`big-idea-ideation-tot`](big-idea-ideation-tot.md), em formato promessa-gancho-vilão.
- O **mecanismo único** e o **arsenal de prova** (sustentam "Crível").
- A **célula** de consciência × sofisticação ([`../awareness-x-sophistication.md`](../awareness-x-sophistication.md)) (sustenta "Casa").
- O **estágio de sofisticação** ([`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md)) (sustenta "Nova" e "Única").
- O **`big-idea-registry`** (ideias passadas — o que já foi usado não é "Novo").

## Procedimento
1. **Monte a matriz** — linhas = candidatas; colunas = os 5 critérios; cada célula recebe nota **0-5**.
2. **Pontue "Nova" (0-5)** — quão fresca e contra-intuitiva é? Já saturada no mercado (sofisticação alta) = nota baixa. Ângulo inédito = nota alta.
3. **Pontue "Grande" (0-5)** — quão profundamente importa ao avatar? Toca a emoção e o resultado dominantes (do VOC)? Ideia "interessante mas pequena" = nota baixa.
4. **Pontue "Crível" (0-5)** — há mecanismo nomeado **e** prova que a sustentam? Promessa grande sem lastro = nota baixa (e risco de veto).
5. **Pontue "Casa com a consciência" (0-5)** — encaixa na célula do público-alvo? Ideia direta para público frio, ou ideia-mecanismo para mercado estágio-1, = nota baixa.
6. **Pontue "Única/Possuível" (0-5)** — só **você** pode dizer isto (por causa do mecanismo, da história, da prova)? Se o concorrente pode copiar a frase amanhã = nota baixa.
7. **Aplique as eliminatórias** — qualquer candidata com **Crível ≤ 2** ou **Casa ≤ 2** é descartada, por maior que seja a soma. Ideia não-crível ou que erra a célula queima o lançamento.
8. **Some e ranqueie** — a maior soma entre as sobreviventes vence. Empate: decide o maior "Casa com a consciência".
9. **Trave UMA** — formate a vencedora final em [`promise-hook-villain`](promise-hook-villain.md) e registre a matriz e a justificativa no `big-idea-registry`. Rode os gates de Big Idea.

## Outputs
- A **matriz de scoring** preenchida (candidatas × 5 critérios, com notas e justificativa).
- **UMA Big Idea travada**, em formato promessa-gancho-vilão.
- A **justificativa rastreável** da escolha (para os gates `big-idea/big-idea-single-gate`, `big-idea/big-idea-new-big-credible-gate`, `big-idea/big-idea-awareness-fit-gate`).
- Registro no `big-idea-registry` (a ideia + as descartadas, para memória).

## Exemplo
Oferta de amostra: curso de inglês para devs. Scoring das candidatas do ToT (notas 0-5):

| Candidata | Nova | Grande | Crível | Casa | Única | Soma |
|---|---|---|---|---|---|---|
| Mecanismo ("Shadowing Técnico") | 4 | 4 | 5 | 4 | 5 | **22** |
| Inimigo ("a gramática matou seu inglês") | 5 | 5 | 4 | 5 | 4 | **23** |
| Promessa ("fluente em 60 dias") | 2 | 5 | 3 | 4 | 2 | 16 |
| Identidade ("o dev global") | 3 | 4 | 3 | 2 | 3 | eliminada (Casa=2) |
| Descoberta ("ler não te faz falar") | 4 | 4 | 4 | 5 | 4 | 21 |

- **Vencedora: Inimigo (23).** Mais nova e maior, casa perfeitamente com a célula 2×4 (público sente a dor, culpa o próprio inglês), e é possuível porque ancora no mecanismo Shadowing Técnico como a alternativa.
- "Identidade" foi eliminada por Casa=2 (público frio ainda não se identifica como "dev global").

## Armadilhas
- **Travar duas ideias.** O scoring existe para escolher UMA. Duas ideias = reprovação automática.
- **Ignorar as eliminatórias.** Uma ideia com soma alta mas "Crível" baixo é uma bomba: grande promessa, nenhum lastro. Elimine.
- **Pontuar "Crível" sem prova.** "Crível" mede mecanismo + prova reais, não o quão convincente a frase soa.
- **Esquecer o registro.** Marcar "Nova" sem checar o `big-idea-registry` repete ângulos gastos.
- **Gosto disfarçado de nota.** Sem justificativa por célula, o scoring vira opinião. Documente o porquê de cada nota.
- **Empate mal resolvido.** Empate decide-se por fit de consciência, não por preferência estética.

## Interações
- **Agentes**: `big-idea-architect` (dono — converge e trava UMA), `offerbook-chief` (aprova a escolha rastreável), `compliance-auditor` (checa "Crível" contra a prova — pode vetar), `positioning-lead-strategist` (valida "Casa" com a célula), `proof-credibility-curator` (fornece o lastro de "Crível").
- **Frameworks que pareiam**: [`big-idea-ideation-tot`](big-idea-ideation-tot.md) (gera as candidatas), [`promise-hook-villain`](promise-hook-villain.md) (formata a vencedora), [`power-of-one`](../power-of-one.md) (a regra de UMA), [`big-idea-generator`](../big-idea-generator.md), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md), [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md).

## Fontes
> **Fonte:** Critérios de Big Idea (nova, grande, crível) de Eugene M. Schwartz, *Breakthrough Advertising* (1966) e David Ogilvy, *Ogilvy on Advertising* (1983); credibilidade e prova de Gary Bencivenga, *7 Secrets* — via [`../../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../../reference/books/copywriting/schwartz-breakthrough-advertising.md), [`../../reference/books/copywriting/ogilvy-on-advertising.md`](../../reference/books/copywriting/ogilvy-on-advertising.md) e [`../../reference/books/copywriting/bencivenga-7-secrets.md`](../../reference/books/copywriting/bencivenga-7-secrets.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
