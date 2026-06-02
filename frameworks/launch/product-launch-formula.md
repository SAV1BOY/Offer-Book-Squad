---
id: framework.launch.product-launch-formula
title: "Product Launch Formula — A Fórmula de Lançamento (Walker)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: launch-producer
frameworks: [runway-and-phases, cart-open-close, perfect-webinar, money-model-sequence, value-equation]
sources:
  - "Jeff Walker, *Launch* (2014; ed. atualizada, 2023), Product Launch Formula."
tags: [launch, plf, pre-pre-launch, pre-launch, open-cart, sideways-sales-letter, mental-triggers, walker]
---

# Product Launch Formula — A Fórmula de Lançamento

## TL;DR
Você não "abre o carrinho e torce". Você conduz o mercado por uma **sequência psicológica** que constrói desejo antes de pedir a venda. Walker chama de **Sideways Sales Letter**: a carta de vendas é fatiada em conteúdo de pré-lançamento (Prelaunch Content) entregue em dias, não numa página só. As fases são **Pre-Pre-Launch → Pre-Launch → Open Cart → Close Cart**. A meta é chegar na abertura com a audiência já convencida, ansiosa e com a objeção dissolvida. É o esqueleto-mãe que o `launch-producer` usa para orquestrar todo lançamento por evento.

## Quando usar / Quando não
**Use** quando há uma lista (própria ou de parceiros) e um produto com mecanismo claro, e você quer um pico de receita concentrado em janela curta.
**Use mais** em mercado de sofisticação 2-4: o conteúdo de pré-lançamento educa o mercado e instala o mecanismo antes do pitch.
**Não use** para venda evergreen pura de baixo ticket sem evento — ali um funil contínuo converte melhor. Para esse caso, pareie com [`../money-model-designer/offer-ladder-sequencing.md`](../money-model-designer/offer-ladder-sequencing.md).
**Não use** sem ter o Offer Book aprovado: a sequência amplifica a oferta, não a substitui. Sem oferta forte, lançamento é só barulho (`offer_before_persuasion`).

## Inputs
- Offer Book aprovado (núcleo, mecanismo nomeado, garantia, prova) — pós HARD STOP.
- A escada do Money Model com a oferta de atração e o núcleo definidos.
- Lista/audiência dimensionada e segmentada; capacidade de e-mail/SMS verificada.
- A Big Idea única do lançamento ([`../../frameworks/big-idea-generator.md`](../../frameworks/big-idea-generator.md)).
- Calendário-alvo (datas de cada PLC, abertura e fechamento do carrinho).

## Procedimento
1. **Fixe a data de fechamento** primeiro e trabalhe para trás. O deadline real é o motor da urgência (`truthful_scarcity`).
2. **Desenhe o Pre-Pre-Launch**: 1-2 contatos que "tateiam" o mercado, ativam curiosidade e coletam objeções por enquete. Pergunte "qual sua maior dificuldade com X?".
3. **Construa os 3 Prelaunch Content (PLC)**. PLC1 = **Oportunidade** (o que muda, a transformação, o gatilho da Autoridade). PLC2 = **Transformação** (o mecanismo, prova, casos; mata "será que funciona?"). PLC3 = **Experiência de Posse** (mostra o "depois", instruções, e antecipa a oferta; mata "será que funciona para MIM?").
4. **Plante os gatilhos mentais** em cada peça: Autoridade, Reciprocidade, Prova Social, Comunidade, Antecipação, Escassez. Um gatilho-líder por PLC.
5. **Abra o carrinho (Open Cart)** com um evento — webinar, vídeo de vendas ou página. Conecte ponta a ponta com [`cart-open-close.md`](cart-open-close.md).
6. **Sustente a abertura** com sequência de e-mail/SMS que rebate objeções, mostra prova e relembra o deadline (entregue ao `email-sms-sequence-writer`).
7. **Feche com força (Close Cart)**: dia final com 2-4 contatos, escassez verdadeira (vagas/bônus/preço que somem de fato) e CTA único.
8. **Pós-fechamento**: entregue, faça onboarding e prepare o downsell/continuidade da escada.

## Outputs
- **Calendário do lançamento**: datas de cada PLC, abertura, fechamento, com gatilho por peça.
- **Briefs dos 3 PLCs** (ângulo, objeção-alvo, gatilho, CTA suave).
- Mapa de transição para [`cart-open-close.md`](cart-open-close.md) e para a sequência de e-mail/SMS.
- Run-of-show inicial para o `launch-producer` operar.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Pre-Pre-Launch**: enquete "qual seu maior medo numa entrevista técnica em inglês?". Resposta dominante: "travar e perder a vaga".
- **PLC1 (Oportunidade)**: vídeo "A vaga remota internacional que você perde por causa do inglês — e por que não é culpa sua".
- **PLC2 (Transformação)**: apresenta o mecanismo "Shadowing Técnico" + 3 casos de aprovados. Mata "será que funciona?".
- **PLC3 (Posse)**: mostra o aluno fazendo o simulador 1:1 e anuncia "vagas abrem terça". Mata "funciona para mim?".
- **Open Cart (terça)**: webinar com o pitch e a Grand Slam Offer; carrinho aberto 5 dias.
- **Close Cart (sábado)**: 3 e-mails no último dia, bônus "50 frases de entrevista" some à meia-noite real.
- **Resultado**: a audiência chega na abertura já convencida; a objeção foi dissolvida nos PLCs, não na hora da venda.

## Armadilhas
- **Pular o pré-lançamento e só "abrir".** Sem PLCs, você pede a venda para um público frio — conversão despenca.
- **Escassez falsa no fechamento.** Deadline que "volta no dia seguinte" queima a lista e é veto de compliance (`truthful_scarcity`).
- **PLCs que viram pitch disfarçado.** O pré-lançamento entrega valor real; vender cedo demais quebra a reciprocidade.
- **Múltiplas ideias.** Cada PLC deve servir à mesma Big Idea — dispersar tese confunde (`one_big_idea`).
- **Lista esgotada.** Lançar para quem você já cansou sem reaquecer derruba aberturas e entregabilidade.

## Interações
- **Agentes**: `launch-producer` (dono — orquestra o calendário e o run-of-show); `email-sms-sequence-writer` (escreve a sequência de abertura/fechamento); `value-equation-engineer` (cada PLC move uma alavanca de valor); `money-model-designer` (a escada que o lançamento monetiza); `affiliate-program-architect` (parceiros entram com seus PLCs no mesmo calendário).
- **Frameworks que pareiam**: [`runway-and-phases.md`](runway-and-phases.md) (fases detalhadas), [`cart-open-close.md`](cart-open-close.md), [`perfect-webinar.md`](perfect-webinar.md) (formato do Open Cart), [`affiliate-army.md`](affiliate-army.md), [`pr-brand-maximization.md`](pr-brand-maximization.md).

## Fontes
> **Fonte:** Jeff Walker, *Launch* (2014; ed. atualizada, 2023), Product Launch Formula — via [`../../reference/books/launches-and-funnels/walker-launch.md`](../../reference/books/launches-and-funnels/walker-launch.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
