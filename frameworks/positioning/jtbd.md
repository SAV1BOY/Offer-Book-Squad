---
id: framework.positioning.jtbd
title: "Jobs To Be Done — O Trabalho que o Cliente Contrata"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: positioning-lead-strategist
frameworks: [dunford-positioning, category-design, blue-ocean-strategy, moore-positioning-formula, perceived-value-stack]
sources:
  - "Clayton M. Christensen, Taddy Hall, Karen Dillon & David S. Duncan, *Competing Against Luck: The Story of Innovation and Customer Choice* (HarperBusiness, 2016), ISBN 978-0-06-243561-3."
  - "Anthony W. Ulwick, *Jobs to Be Done: Theory to Practice* (IDEA BITE PRESS, 2016)."
tags: [jtbd, jobs-to-be-done, customer-job, progress, outcome, switch, positioning, avatar]
---

# Jobs To Be Done — O Trabalho que o Cliente Contrata

## TL;DR
As pessoas não compram produtos. Elas **contratam** produtos para fazer um **trabalho** (job): um progresso que querem alcançar numa circunstância. O famoso exemplo: ninguém quer uma furadeira de 6mm — querem um furo de 6mm; na verdade, querem a prateleira no lugar. O JTBD muda a pergunta de "o que o cliente quer no produto?" para "**que progresso ele tenta fazer?**" e "o que ele demitiria para te contratar?". Isso revela a concorrência real (inclusive o "não fazer nada") e o valor que importa. O `positioning-lead-strategist` e o `avatar-voc-investigator` usam para ancorar posição e oferta no job, não na feature.

## Quando usar / Quando não
**Use** no começo, para entender **por que** o cliente compra — antes de definir mecanismo, posição e oferta.
**Use mais** para achar a **concorrência real** (tudo que faz o mesmo job, incluindo soluções de outra categoria e o status quo) e para alimentar a alternativa competitiva de [`dunford-positioning.md`](dunford-positioning.md).
**Use mais** para descobrir jobs **mal atendidos** que originam uma categoria nova ([`category-design.md`](category-design.md)) ou um fator "Criar" do ERRC ([`blue-ocean-strategy.md`](blue-ocean-strategy.md)).
**Não use** como substituto do avatar demográfico inteiro — JTBD complementa o perfil, focando no progresso e na circunstância.
**Não use** ficando só no job funcional: as dimensões emocional e social muitas vezes decidem a compra.

## Inputs
- Entrevistas e VOC de clientes que **recém compraram** ou recém trocaram (o momento da decisão é o mais rico).
- O **mapa da circunstância**: o que estava acontecendo quando o cliente buscou uma solução.
- A lista de soluções que ele **considerou e abandonou** (a concorrência do job).
- As forças do "switch": o que **empurra** (dor do status quo) e o que **puxa** (atração da nova solução), mais o que **prende** (hábito, medo).

## Procedimento
1. **Entreviste o momento da compra.** Pergunte a clientes recentes: "o que estava acontecendo quando você decidiu procurar isto?" Reconstrua a **circunstância**, não a demografia. O gatilho revela o job.
2. **Escreva o job na forma canônica**: "**Quando** [situação], **eu quero** [motivação], **para que** [resultado esperado]." Ex.: "Quando recebo uma vaga remota internacional, quero passar na entrevista técnica em inglês, para conseguir o emprego e o salário em dólar."
3. **Separe as três dimensões do job:**
   - **Funcional**: a tarefa prática (passar na entrevista).
   - **Emocional**: como ele quer se sentir (confiante, sem vergonha da pronúncia).
   - **Social**: como quer ser visto (um dev "global", competitivo).
   Os três pesam; a emocional/social costuma decidir.
4. **Mapeie a concorrência do job.** Liste **tudo** que o cliente poderia "contratar" para o mesmo progresso — inclusive outras categorias, gambiarras e "não fazer nada". Essa é a alternativa competitiva real.
5. **Mapeie as forças do switch.** O que **empurra** o cliente para fora do status quo (a dor)? O que **puxa** para a nova solução (a promessa)? O que **prende** (hábito, medo de mudar, ansiedade)? Você vende reforçando empurrar+puxar e dissolvendo o que prende.
6. **Liste os resultados desejados (outcomes).** Para cada etapa do job, que métrica o cliente quer melhorar (mais rápido, mais barato, menos erro)? Outcomes mal atendidos = oportunidade de oferta (abordagem Ulwick).
7. **Priorize os jobs/outcomes** por importância × insatisfação (use [`../pricing/maxdiff.md`](../pricing/maxdiff.md) para ranquear). O job importante e mal atendido é o alvo.
8. **Traduza para posição e oferta.** O job vira a "necessidade" na fórmula de Moore ([`moore-positioning-formula.md`](moore-positioning-formula.md)); os outcomes viram as alavancas de valor e a prova.
9. **Registre** os jobs, dimensões e forças no banco de VOC e no `decision-registry`.

## Outputs
- **Job statements** (forma canônica) com as três dimensões.
- **Mapa da concorrência do job** (a alternativa competitiva real, inclusive status quo).
- **Mapa das forças do switch** (empurrar / puxar / prender).
- Lista de **outcomes** priorizados → alvos de oferta e posição.

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI.
- **Job**: "Quando recebo a chance de uma vaga remota internacional, quero passar na entrevista técnica em inglês, para conseguir o emprego e o salário em dólar."
- **Dimensões**: funcional = passar na call técnica; emocional = não travar nem sentir vergonha; social = ser visto como dev competitivo no mercado global.
- **Concorrência do job**: apps de idioma, professor particular, "praticar com ChatGPT", desistir e ficar na vaga local (status quo).
- **Forças**: *empurra* = perdeu uma vaga por travar no inglês; *puxa* = salário em dólar; *prende* = medo de gastar e não conseguir, hábito de adiar.
- **Outcomes priorizados**: "reduzir o tempo até falar com fluidez técnica" e "aumentar a chance de aprovação" (alta importância, alta insatisfação).
- Tradução: a posição ataca o job ("aprovado na entrevista"), a oferta dissolve o que prende (garantia aprovado-ou-grátis) e reforça o que puxa (salário em dólar na copy).

## Armadilhas
- **Confundir job com produto.** "O cliente quer um curso" é solução, não job. O job é o **progresso** (passar na entrevista). Suba um nível.
- **Só o funcional.** Ignorar o emocional e o social perde o que de fato decide a compra.
- **Concorrência estreita.** Esquecer o "não fazer nada" e as soluções de outras categorias subestima a alternativa real.
- **Demografia no lugar da circunstância.** "Homem, 30 anos" não explica a compra; o **gatilho** explica.
- **Pesquisar quem não comprou recentemente.** A memória do momento da decisão some rápido. Foque em quem acabou de trocar.
- **Outcomes vagos.** "Quer ficar melhor" não orienta oferta. Métrica + direção (mais rápido, menos erro).

## Interações
- **Agentes**: `positioning-lead-strategist` (dono no posicionamento — o job vira a necessidade da posição); `avatar-voc-investigator` (conduz as entrevistas de job e mapeia as forças — JTBD é base do avatar); `mechanism-architect` (desenha o mecanismo para o outcome mal atendido); `value-equation-engineer` (os outcomes viram alavancas de valor); `pricing-wtp-strategist` (a importância do job sinaliza a WTP — job crítico mal atendido aceita preço maior); `unit-economics-stack-analyst` (cruza o valor do outcome com o custo de entregá-lo); `big-idea-architect` (o job emocional alimenta a tese); `vsl-webinar-scriptwriter` (a copy reforça empurrar/puxar e dissolve o que prende).
- **Frameworks que pareiam**: [`dunford-positioning.md`](dunford-positioning.md) (job → alternativa competitiva e valor), [`moore-positioning-formula.md`](moore-positioning-formula.md) (job → "necessidade"), [`category-design.md`](category-design.md) (job mal atendido → categoria nova), [`blue-ocean-strategy.md`](blue-ocean-strategy.md) (jobs guiam o "Criar"), [`../pricing/maxdiff.md`](../pricing/maxdiff.md) (prioriza jobs/outcomes), [`perceived-value-stack.md`](perceived-value-stack.md), [`../unique-mechanism.md`](../unique-mechanism.md).

## Fontes
> **Fonte:** Clayton M. Christensen et al., *Competing Against Luck* (2016), HarperBusiness; e Anthony W. Ulwick, *Jobs to Be Done: Theory to Practice* (2016) — acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
