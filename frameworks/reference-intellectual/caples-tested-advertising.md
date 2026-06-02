---
id: framework.reference-intellectual.caples-tested-advertising
title: "Caples — Testar Headlines (o Título é o Anúncio)"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [hook-frameworks, awareness-x-sophistication]
sources:
  - "John Caples, *Tested Advertising Methods* (1ª ed. 1932; 5ª ed. rev. Fred E. Hahn, Prentice Hall, 1998), ISBN 978-0-13-095701-6."
tags: [caples, headlines, testing, split-test, control, direct-response]
---

# Caples — Testar Headlines (o Título é o Anúncio)

## TL;DR
Caples provou, por teste de cupom, que **o título é o anúncio**: dois anúncios idênticos, mudando só a headline, geram resultados que diferem em **múltiplos** — não em pontos percentuais. Daí sua disciplina: você não debate qual título é melhor, você **testa** e deixa os números decidirem (`evidence_before_opinion`). Os vencedores costumam carregar **interesse próprio, notícia, curiosidade** ou promessa de via rápida. Este framework é o ciclo de geração e teste de manchetes do squad, com manutenção do **control**. Vence sempre que há tráfego para medir e a tentação é confiar no palpite do redator.

## Quando usar / Quando não
**Use** ao gerar e priorizar headlines, linhas de assunto e ganchos de anúncio — a alavanca de maior impacto.
**Use** para instaurar cultura de teste: variações, medição, manter o vencedor, tentar batê-lo.
**Use** para humildade de processo: o que o redator acha que ganha frequentemente perde.
**Não use** como ferramenta de oferta ou preço — Caples otimiza a **porta de entrada** (o título), não o que está dentro.
**Não use** para "testar" sem volume: sem tráfego suficiente, o resultado é ruído, não evidência.
**Fit:** universal; o **tipo** de título vencedor muda com a consciência e a sofisticação — pareie com Schwartz.

## Inputs
- A oferta e o benefício central já definidos (o título promete algo verdadeiro).
- O nível de consciência dominante — ver [`schwartz-breakthrough-advertising.md`](schwartz-breakthrough-advertising.md).
- O `control-registry` (o vencedor atual a bater) e o `swipe-registry`.
- O canal e o volume de tráfego disponível para um teste estatisticamente honesto.

## Procedimento
1. **Trate o título como o anúncio.** Aceite a lei de Caples: a maior parte do dinheiro se ganha ou se perde no título. Invista o esforço onde o impacto é maior.
2. **Gere muitos títulos por ângulo.** Para cada oferta, produza dezenas — não dois. Quantidade alimenta o teste.
3. **Aplique as 4 qualidades vencedoras.** Marque cada título por **interesse próprio** (benefício direto), **notícia** (novo, agora), **curiosidade** e **forma rápida/fácil**. Os mais fortes carregam ao menos uma.
4. **Prometa um benefício específico e crível.** Título vago não para ninguém; o específico atravessa a indiferença.
5. **Monte o split-test.** Rode variações com o resto da peça **igual**, mudando só o título. Garanta volume para a diferença ser real, não ruído.
6. **Deixe os números decidirem.** Meça a resposta. O palpite do redator perde para o cupom com frequência humilhante — aceite o veredito.
7. **Mantenha o control.** Guarde o vencedor atual. Só o substitua quando uma variação **o bater** em teste.
8. **Ajuste pelo mercado.** Calibre o **tipo** de título ao nível de consciência: mais consciente aceita oferta/preço no título; menos consciente quer curiosidade e benefício.
9. **Registre vencedores** no `control-registry` e alimente o `swipe-registry`.

## Outputs
- O **lote de títulos** gerados, marcados pelas 4 qualidades.
- O **plano de split-test** (o que varia, o volume mínimo, a métrica).
- O **control** atual (vencedor) e o histórico de quem o bateu.
- A **nota de calibração** por nível de consciência.

## Exemplo
Oferta de amostra: curso online de fotografia para iniciantes.
- **Lei do título**: a equipe investe o esforço em gerar 30 manchetes, não em polir o corpo.
- **Geração + 4 qualidades**:
  - Interesse próprio: "Tire fotos de revista com a câmera que você já tem."
  - Notícia: "O novo método que ensina foco perfeito em um fim de semana."
  - Curiosidade: "O erro de foco que 9 em cada 10 iniciantes cometem."
  - Via rápida: "Domine o modo manual em 7 dias."
- **Split-test**: as quatro rodam como anúncio com a mesma imagem e oferta; só a headline muda; volume suficiente para significância.
- **Veredito**: o ângulo de **curiosidade** bate o de interesse próprio por margem de múltiplos — vira o novo control, contrariando o palpite inicial da equipe.
- **Calibração**: como a consciência é baixa (iniciantes), curiosidade vence; num público avançado, o teste mudaria.
- **Resultado**: o `knowledge-librarian` registra o vencedor no `control-registry`.

## Armadilhas
- **Confiar no palpite.** O redator "sabe" qual ganha — e erra com frequência. Teste.
- **Testar dois títulos só.** Pouca variação não revela o vencedor real; gere muitos.
- **Mudar várias coisas de uma vez.** Se imagem, oferta e título mudam juntos, o teste não isola o título.
- **Título vago.** "Transforme sua vida" não para ninguém; prometa o específico e crível.
- **Volume insuficiente.** Declarar vencedor sem amostra honesta é ruído travestido de evidência.
- **Trocar o control sem ele ser batido.** Aposentar o vencedor por gosto, não por dado, perde dinheiro.

## Interações
- **Agentes** (de `config.yaml`): `ad-creative-factory` (gera muitos títulos por ângulo e os marca para teste); `vsl-webinar-scriptwriter` (trata título/abertura como a alavanca de maior impacto); `email-sms-sequence-writer` (testa linhas de assunto como Caples testava manchetes); `knowledge-librarian` (registra vencedores no `control-registry` e alimenta o `swipe-registry`); `market-sophistication-analyst` (ajusta o tipo de título ao nível de consciência).
- **Frameworks que pareiam**: [`../copy/hook-frameworks.md`](../copy/hook-frameworks.md) (geração e teste de títulos), [`../awareness-x-sophistication.md`](../awareness-x-sophistication.md) (o ciclo de variação por estágio); e as referências [`ogilvy-on-advertising.md`](ogilvy-on-advertising.md) (o herdeiro do culto ao título) e [`sugarman-triggers.md`](sugarman-triggers.md) (o título que põe o leitor no topo da escorrega).

## Fontes
> **Fonte:** John Caples, *Tested Advertising Methods* (1ª ed. 1932; 5ª ed. rev. Fred E. Hahn, Prentice Hall, 1998), ISBN 978-0-13-095701-6 — via [`../../reference/books/copywriting/caples-tested-advertising.md`](../../reference/books/copywriting/caples-tested-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
