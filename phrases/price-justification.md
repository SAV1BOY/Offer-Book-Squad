---
id: phrases.price-justification
title: "Banco de Justificativa de Preço e Ancoragem"
type: phrases
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: vsl-webinar-scriptwriter
frameworks: [price-anchoring, value-equation, offer-stack-builder, awareness-levels]
tags: [price, anchoring, justification, value-stack, cost-of-inaction, decoy]
---

# Banco de Justificativa de Preço e Ancoragem

Frases-modelo **originais** para apresentar o preço de forma que ele pareça pequeno diante do valor. O preço nunca é julgado sozinho: o cérebro o compara a uma âncora. Você escolhe a âncora — o valor empilhado, a alternativa cara, o custo de não resolver, o preço por dia — para que o seu número vire a escolha óbvia. Cada grupo marca o gatilho que dispara. Os colchetes `[ ]` são variáveis: preencha com os valores reais — toda âncora é honesta, nunca inventada.

## Quando usar

Use este banco no momento da revelação do preço: depois do valor empilhado e da garantia, antes ou junto da CTA ([`ctas.md`](ctas.md), [`close-lines.md`](close-lines.md)). A justificativa transforma "quanto custa" em "quanto vale". Empilhe o valor de cada parte antes de mostrar o preço (ver [`../frameworks/offer-stack-builder.md`](../frameworks/offer-stack-builder.md)) e ancore com um número maior e verdadeiro primeiro (ver [`../frameworks/price-anchoring.md`](../frameworks/price-anchoring.md)). Regra dura: a ancoragem **molda** a percepção do número, mas a ciência de WTP **define** o número. Âncora honesta converte; âncora inventada (preço "de" que nunca existiu, soma de valor inflada) é veto do `compliance-auditor`. Nunca prometa retorno financeiro garantido — diga "valor", "economia possível", não "lucro certo".

## Banco de frases

### Ancoragem por valor empilhado — a soma antes do preço
> Gatilho: [ancoragem] — a primeira cifra grande puxa a percepção do preço final. Base em [`../reference/psychology/anchoring.md`](../reference/psychology/anchoring.md). A soma reflete o valor real de cada parte.

- "Só [componente A] já vale [valor]. Some [B] e [C] e passa de [soma]. Você não paga isso." [ancoragem]
- "Se você contratasse cada parte separada, gastaria [soma]. Tudo junto, hoje, sai por [preço]." [ancoragem]
- "Coloquei o valor de cada item na tela. A conta dá [soma]. O investimento é uma fração disso." [ancoragem] [prova]

### Ancoragem por alternativa — comparar com o caro
> Gatilho: [relatividade] — o preço encolhe ao lado de uma alternativa mais cara e real. Base em [`../reference/psychology/anchoring.md`](../reference/psychology/anchoring.md). A comparação precisa ser legítima.

- "Um [profissional/serviço equivalente] cobra [valor] por [unidade]. Aqui você resolve por [preço], uma vez." [relatividade]
- "Contratar [solução tradicional] custaria [valor] por ano. Este é o mesmo resultado por [preço]." [relatividade]
- "Compare com [alternativa que ele já considera]: mesmo problema, preço maior, e sem [diferencial seu]." [relatividade] [enquadramento]

### Decomposição — o preço por dia, por uso
> Gatilho: [enquadramento] — quebrar o preço em parcelas pequenas reduz a dor de pagar. Base em [`../reference/psychology/framing-effect.md`](../reference/psychology/framing-effect.md).

- "São [preço] no total. Diluído em [período], dá menos que [comparação cotidiana barata] por dia." [enquadramento]
- "Pense por uso: [preço] dividido por [N usos/meses] é [valor pequeno] por vez." [enquadramento]
- "Menos que [gasto trivial recorrente] por dia para [resultado grande]." [enquadramento] [relatividade]

### Custo de não resolver — o preço de continuar parado
> Gatilho: [aversão à perda] — o custo da inação faz o preço parecer barato. Base em [`../reference/psychology/loss-aversion.md`](../reference/psychology/loss-aversion.md).

- "Continuar com [situação atual] custa [perda concreta] por [período]. O programa custa menos que [esse intervalo]." [aversão à perda]
- "A pergunta não é se você pode pagar [preço]. É quanto [o problema] já te custou sem você notar." [aversão à perda] [enquadramento]
- "Cada [unidade de tempo] adiando sai mais caro que o investimento inteiro." [aversão à perda]

### Justificativa de valor — por que vale o preço
> Gatilho: [equação de valor] — o resultado, a rapidez e a certeza justificam o número. Base em [`../frameworks/value-equation.md`](../frameworks/value-equation.md).

- "Você não está pagando por [entregável físico]. Está pagando para [resultado] em [tempo] com [certeza]." [equação de valor]
- "O preço reflete o atalho: o que levaria [tempo longo] sozinho, aqui leva [tempo curto]." [equação de valor] [especificidade]
- "Barato é o que você compra e não usa. Isto você usa até [resultado] — aí o preço some na conta." [enquadramento]

## Como adaptar por consciência

Siga [`../lib/taxonomies/awareness-levels.md`](../lib/taxonomies/awareness-levels.md): em público frio, o preço entra tarde e bem ancorado; em público quente, vai direto.

- **Nível 1 Inconsciente:** não fale preço; construa desejo e valor primeiro.
- **Nível 2 Consciente do problema:** ancore pelo custo de não resolver, não pela tabela.
- **Nível 3 Consciente da solução:** compare com a alternativa cara que ele já pesquisa.
- **Nível 4 Consciente do produto:** empilhe o valor e mostre o preço como fração da soma.
- **Nível 5 Mais consciente:** preço direto, com uma âncora curta e a parcela; ele só quer o número.

## Liga com

- Como moldar a percepção do número: [`../frameworks/price-anchoring.md`](../frameworks/price-anchoring.md).
- Como empilhar o valor antes do preço: [`../frameworks/offer-stack-builder.md`](../frameworks/offer-stack-builder.md), [`../frameworks/value-equation.md`](../frameworks/value-equation.md).
- O efeito isca no pacote: [`../frameworks/pricing/decoy-effect.md`](../frameworks/pricing/decoy-effect.md).
- Agentes: `pricing-wtp-strategist` define o número por WTP; `vsl-webinar-scriptwriter` e `email-sms-sequence-writer` escrevem a justificativa; `compliance-auditor` **veta** âncora inventada e promessa de lucro garantido.
- Sequência interna: a justificativa de preço apoia o fecho em [`close-lines.md`](close-lines.md) e responde objeção de custo em [`objection-handling.md`](objection-handling.md).
