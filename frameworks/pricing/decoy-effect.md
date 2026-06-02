---
id: framework.pricing.decoy-effect
title: "Decoy Effect — A Isca de Preço (Dominância Assimétrica)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: pricing-wtp-strategist
frameworks: [packaging-good-better-best, value-based-pricing, conjoint-cbc, price-anchoring]
sources:
  - "Dan Ariely, *Predictably Irrational* (HarperCollins, 2008), cap. 1 'The Truth About Relativity'."
  - "Joel Huber, John Payne & Christopher Puto, *Adding Asymmetrically Dominated Alternatives*, Journal of Consumer Research (1982)."
tags: [pricing, decoy, asymmetric-dominance, relativity, choice-architecture, anchoring, behavioral]
---

# Decoy Effect — A Isca de Preço (Dominância Assimétrica)

## TL;DR
As pessoas não julgam preço no absoluto. Julgam no **relativo**. O efeito decoy explora isso: você adiciona uma terceira opção **propositalmente pior** (a isca) para fazer a opção que você quer vender parecer óbvia. A isca não é feita para vender — é feita para **deslocar a escolha**. O caso clássico: web a US$59, impresso a US$125, web+impresso a US$125. O impresso sozinho é a isca; ele faz o combo parecer um roubo. Bem usado, o decoy aumenta a margem sem prometer nada falso. É uma alavanca de arquitetura de escolha do `pricing-wtp-strategist`.

## Quando usar / Quando não
**Use** quando tem uma linha de opções e quer **empurrar a escolha** para o degrau de maior margem (em geral o Best ou o Better) sem baixar preço.
**Use mais** junto do empacotamento Good-Better-Best ([`packaging-good-better-best.md`](packaging-good-better-best.md)): o decoy é a peça que torna o alvo óbvio.
**Não use** como manipulação que esconde valor real: a isca tem que ser uma opção **legítima**, só pior em relação ao alvo. Opção falsa ou enganosa = veto de compliance.
**Não use** com público sofisticado que percebe a armação e se ofende — teste antes. Ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md).
**Não use** sozinho para definir preço: ele ajusta a **escolha entre opções**, não o nível de preço (que vem do valor).

## Inputs
- Uma linha com pelo menos duas opções reais (ex.: o Good e o Best do empacotamento).
- Clareza de **qual opção você quer vender mais** (o alvo).
- Os atributos que o cliente compara (preço, features, volume) — de [`conjoint-cbc.md`](conjoint-cbc.md).
- Margem de cada opção, para confirmar que empurrar a escolha aumenta lucro.

## Procedimento
1. **Escolha o alvo.** Decida qual opção quer maximizar (normalmente a de maior margem ou ticket: o Best ou o Better).
2. **Mapeie os atributos de comparação.** Liste as 2-3 dimensões que o cliente usa para decidir (ex.: preço × horas de suporte). O decoy age sobre essas dimensões.
3. **Crie a isca dominada assimetricamente.** Desenhe uma terceira opção que é **claramente pior que o alvo** em pelo menos uma dimensão e **não melhor** em nenhuma, mas que parece comparável a uma terceira opção. Tipos:
   - **Decoy de preço**: mesma coisa que o alvo, custando quase o mesmo que ele — mas entregando menos (faz o alvo parecer "de graça o extra").
   - **Decoy de tamanho**: opção intermediária mal posicionada que faz o tamanho maior parecer o melhor valor por unidade.
4. **Posicione a isca perto do alvo**, não da opção barata. A isca tem que tornar **o alvo** óbvio, comparando-se a ele.
5. **Apresente as três juntas.** O efeito só funciona na comparação simultânea. A isca fica visível ao lado do alvo.
6. **Confirme a dominância.** Cheque: ninguém racional escolheria a isca em vez do alvo. Se alguém escolheria, não é decoy — é uma opção real competindo.
7. **Teste o mix.** Rode A/B (com decoy × sem decoy) e meça se a participação do alvo subiu e se a margem total melhorou. O decoy se prova no **deslocamento de escolha**, não nas vendas dele.
8. **Garanta a verdade.** A isca é uma oferta real que alguém **poderia** comprar e receberia o que promete. Nada falso, nada que some no carrinho. Passa por `compliance/compliance-claim-backing-gate`.
9. **Registre** o desenho do decoy, o alvo e o resultado do teste no `price-test-registry`.

## Outputs
- A **isca** desenhada (opção dominada) e o **alvo** que ela valoriza.
- Resultado A/B: **deslocamento de escolha** para o alvo e variação de margem total.
- Recomendação de manter, ajustar ou remover o decoy.
- Layout da página de preços com as três opções ordenadas.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI. Alvo = pacote "Elite" (R$3.990).
- Linha original: "Pro" R$1.990 (5h 1:1) e "Elite" R$3.990 (20h 1:1 + simulação com recrutador). Muitos param no Pro.
- **Decoy adicionado — "Pro Plus" R$3.490 (10h 1:1, sem simulação com recrutador).**
- Comparação: o Pro Plus custa quase o mesmo que o Elite (R$500 a menos) mas entrega bem menos (metade das horas, sem o "uau" da simulação). O Elite vira o óbvio: "por só R$500 a mais eu dobro as horas e ganho a simulação".
- Resultado A/B: a escolha do "Elite" subiu de 22% para 41%; o ticket médio da linha subiu. O Pro Plus quase não vende — e tudo bem, é a isca.
- Verdade preservada: quem comprar o Pro Plus recebe exatamente as 10h prometidas.

## Armadilhas
- **Isca que vende muito.** Se a isca atrai compradores, ela não está dominada — é uma opção real mal precificada. Redesenhe.
- **Isca longe do alvo.** Posicionada perto do barato, ela valoriza o barato, não o alvo. Aproxime do alvo.
- **Opções demais.** Decoy só funciona com poucas opções. Numa lista enorme, ele vira ruído.
- **Manipulação percebida.** Público sofisticado fareja a armação. Teste; se gera revolta, remova.
- **Decoy desonesto.** Isca falsa, indisponível ou que esconde o que entrega = veto de compliance. A isca é real.
- **Confiar no decoy para o nível de preço.** Ele move a **escolha**; o **preço-base** vem do valor ([`value-based-pricing.md`](value-based-pricing.md)).

## Interações
- **Agentes**: `pricing-wtp-strategist` (dono — desenha a isca e mede o deslocamento); `unit-economics-stack-analyst` (confirma que o deslocamento para o alvo melhora a margem da linha); `compliance-auditor` (veta isca falsa ou enganosa — a opção precisa ser real e entregável); `value-equation-engineer` (o "uau" do alvo vs. a isca é uma alavanca de valor relativa); `positioning-lead-strategist` (o alvo que a isca valoriza deve ser o pacote que melhor expressa a posição premium).
- **Frameworks que pareiam**: [`packaging-good-better-best.md`](packaging-good-better-best.md) (o decoy torna o degrau-alvo óbvio), [`price-anchoring.md`](../price-anchoring.md) (a isca também ancora preço), [`conjoint-cbc.md`](conjoint-cbc.md) (o simulador prevê o efeito da isca no share), [`value-based-pricing.md`](value-based-pricing.md), [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md) (o decoy como tipo de oferta de atração).

## Fontes
> **Fonte:** Dan Ariely, *Predictably Irrational* (2008), cap. 1; e Joel Huber, John Payne & Christopher Puto, "Adding Asymmetrically Dominated Alternatives", *Journal of Consumer Research* (1982) — via [`../../reference/books/persuasion-psychology/ariely-predictably-irrational.md`](../../reference/books/persuasion-psychology/ariely-predictably-irrational.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
