---
id: framework.reference-intellectual.schwartz-breakthrough-advertising
title: "Schwartz — Consciência e Sofisticação na Prática"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [awareness-x-sophistication, unique-mechanism, big-idea-generator, power-of-one]
sources:
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966), Boardroom/Bottom Line Books (reimpressão)."
tags: [schwartz, awareness, sophistication, mass-desire, mechanism, market-diagnosis]
---

# Schwartz — Consciência e Sofisticação na Prática

## TL;DR
Schwartz dá ao squad a régua que decide **onde a copy começa** e **o que ela precisa dizer**. A copy não cria desejo; ela canaliza um desejo de massa que já existe. Dois eixos governam tudo: o **estado de consciência** do prospect (quanto ele sabe) e o **estágio de sofisticação** do mercado (quão cansado ele está dos claims). Este framework operacionaliza o diagnóstico desses dois eixos e a decisão que sai dele: prometer mais, introduzir mecanismo ou migrar para identidade. Vence quando o mercado já ouviu de tudo e gritar mais alto parou de funcionar.

## Quando usar / Quando não
**Use** no início de todo caso, antes de uma palavra de copy: é o diagnóstico que impede escrever lead de estágio-2 para um mercado de estágio-4.
**Use** para escolher o lead, o gancho e o comprimento da abertura — cada nível de consciência exige um ponto de partida diferente.
**Use** para decidir quando o **mecanismo** entra: a sofisticação 3 é o gatilho.
**Não use** como ferramenta de oferta ou preço — Schwartz mede o estado do mercado, não monta o stack (isso é Hormozi).
**Não use** para inventar consciência: o nível se **declara com evidência** de VOC, não por palpite.
**Fit:** quanto mais maduro o mercado, mais central este framework fica; em mercado virgem (estágio 1), basta nomear o claim.

## Inputs
- Banco de VOC com a linguagem literal do mercado (fóruns, reviews, suporte, entrevistas).
- O claim dominante dos concorrentes e quantos já o fizeram.
- A dor e o desejo de massa principais do avatar.
- O mecanismo candidato, se já existir — ver [`../unique-mechanism.md`](../unique-mechanism.md).
- As taxonomias de [níveis de consciência](../../lib/taxonomies/awareness-levels.md) e [estágios de sofisticação](../../lib/taxonomies/sophistication-levels.md).

## Procedimento
1. **Declare a consciência (1-5).** Do **inconsciente** ao **mais consciente**: o prospect sabe que tem o problema? Conhece a solução? Conhece você? Marque o nível com **citação de VOC** que o comprove.
2. **Declare a sofisticação (1-5).** Quantos já fizeram este claim no mercado? Estágio 1: ninguém. Estágio 5: todos, e o mercado está exausto. Justifique com exemplos de concorrentes.
3. **Mensure o desejo de massa.** Some a esperança ou o medo já presente. Pontue por **intensidade, urgência e escopo** — não invente, identifique.
4. **Cruze os dois eixos** na matriz consciência × sofisticação para achar o ponto de partida do lead.
5. **Escolha a jogada de sofisticação:**
   - Estágio 1 → **diga o claim** direto.
   - Estágio 2 → **amplie** o claim (maior, mais rápido, mais).
   - Estágio 3 → **introduza o mecanismo** (o *como*, o porquê de funcionar quando o resto falhou).
   - Estágio 4 → **eleve o mecanismo** (mais fácil, mais rápido, sem o sacrifício).
   - Estágio 5 → **migre para identidade** e pertencimento; o mercado já não compra promessa nem mecanismo.
6. **Ajuste o lead pela consciência:** inconsciente exige história e identidade; mais consciente quer preço, bônus e CTA.
7. **Registre o diagnóstico** no `market-brief` com as duas notas (1-5) e a evidência, e entregue ao `big-idea-architect` e ao `positioning-lead-strategist`.

## Outputs
- As **duas notas** consciência (1-5) e sofisticação (1-5), cada uma com evidência.
- O **ponto de partida do lead** derivado da matriz.
- A **jogada de sofisticação** escolhida (claim / amplificação / mecanismo / mecanismo elevado / identidade).
- A **mensuração do desejo de massa** (intensidade, urgência, escopo).

## Exemplo
Oferta de amostra: suplemento para dormir.
- **Consciência (3/5)**: o avatar sabe que dorme mal e já tentou chá e melatonina (VOC: "já tomei de tudo e acordo às 3h"). Conhece soluções, não conhece a marca.
- **Sofisticação (4/5)**: dezenas de marcas já prometem "durma melhor" e "fórmula natural". O claim simples morreu.
- **Jogada**: estágio 4 → **elevar o mecanismo**. Não basta dizer "tem melatonina"; é preciso um mecanismo novo e crível ("Protocolo de Onda Lenta que age na fase 3 do sono, onde a melatonina sozinha não chega").
- **Lead**: como a consciência é 3, abre pela frustração das tentativas falhas, não por educação básica sobre sono.
- **Desejo de massa**: intensidade alta (exaustão diária), urgência alta, escopo amplo → ângulo forte.
- **Resultado**: o `mechanism-architect` recebe a ordem de isolar e nomear o mecanismo; a Big Idea ancora no desejo dominante, não num benefício inventado.

## Armadilhas
- **Escrever abaixo do estágio.** Prometer mais (estágio 2) num mercado exausto (estágio 4) soa como ruído. Suba para o mecanismo.
- **Pular para identidade cedo demais.** Estágio 5 só funciona quando promessa e mecanismo já se gastaram; antes disso, é vazio.
- **Confundir os dois eixos.** Consciência é sobre o **prospect**; sofisticação é sobre o **mercado/claims**. Diagnostique cada um separado.
- **Declarar nível sem evidência.** Sem VOC que comprove, a nota é chute e a copy erra o alvo.
- **Inventar desejo.** Schwartz é claro: o desejo já existe. Mostre-o, não o fabrique.

## Interações
- **Agentes** (de `config.yaml`): `market-sophistication-analyst` (dono — declara as duas notas com evidência no `market-brief`); `mechanism-architect` (isola o mecanismo que a sofisticação 3-4 exige); `positioning-lead-strategist` (escolhe o lead pela matriz; trata estágio 5 com identidade); `big-idea-architect` (ancora a Big Idea no desejo de massa); `vsl-webinar-scriptwriter` e `ad-creative-factory` (ajustam abertura e comprimento ao nível de consciência).
- **Frameworks que pareiam**: [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md) (a matriz operacional), [`../unique-mechanism.md`](../unique-mechanism.md) (o que a sofisticação dispara), [`../big-idea-generator.md`](../big-idea-generator.md), [`../power-of-one.md`](../power-of-one.md); e [`hormozi-offers-leads-models.md`](hormozi-offers-leads-models.md) (quando o mecanismo vira o núcleo da oferta).

## Fontes
> **Fonte:** Eugene M. Schwartz, *Breakthrough Advertising* (1966), reimpressão Boardroom/Bottom Line Books — via [`../../reference/books/copywriting/schwartz-breakthrough-advertising.md`](../../reference/books/copywriting/schwartz-breakthrough-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
