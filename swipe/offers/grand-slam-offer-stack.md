---
id: swipe.offers.grand-slam-offer-stack
title: "Padrão: Oferta-Núcleo Empilhada (Grand Slam)"
type: swipe
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: knowledge-librarian
frameworks: [offer-stack-builder, value-equation, unique-mechanism, risk-reversal-ladder]
sources:
  - "Alex Hormozi, *$100M Offers* (2021)."
  - "Eugene M. Schwartz, *Breakthrough Advertising* (1966)."
tags: [swipe, offers, grand-slam, value-stack, mechanism, guarantee, core-offer]
---

# Padrão: Oferta-Núcleo Empilhada (Grand Slam)

## O que é
Arquétipo: **a oferta principal empilhada** — a proposta que entrega a transformação central e vence porque o valor percebido supera o preço em larga margem. É a oferta-núcleo do Money Model: não a isca de entrada nem o upsell, mas a peça que carrega o resultado prometido. Em vez de "um produto por um preço", ela monta um **bloco** de mecanismo, entregáveis, bônus e reversão de risco que, somados, fazem o preço parecer pequeno. Estudamos a **estrutura de empilhamento**, não a copy de nenhuma oferta nomeada.

## Anatomia
Os beats da oferta-núcleo, na nossa leitura:
1. **Promessa-resultado (o sonho).** O resultado específico e desejado que o comprador alcança — alto na alavanca "sonho" da [Value Equation](../../frameworks/value-equation.md).
2. **Mecanismo único nomeado.** O "como" diferente que torna a promessa crível num mercado cético — sobe a probabilidade percebida de sucesso. Ver [`unique-mechanism`](../../frameworks/unique-mechanism.md).
3. **Os entregáveis-núcleo.** O que o comprador recebe para atingir o resultado, organizados por etapa da jornada — cada item resolve um obstáculo real.
4. **Bônus que matam objeções.** Cada bônus existe para derrubar uma objeção específica ("e se eu travar em X?") e para baixar tempo/esforço percebidos.
5. **Ancoragem de valor.** O valor somado dos itens é exibido **antes** do preço, ancorando alto. Ver [`price-anchoring`](../../frameworks/price-anchoring.md).
6. **Revelação de preço.** O número aparece depois do valor empilhado, parecendo um desconto contra o total.
7. **Reversão de risco.** Garantia real e exequível que transfere o risco do comprador para o vendedor. Ver [`guarantee-types`](../../lib/taxonomies/guarantee-types.md).
8. **Escassez/urgência verdadeira.** Uma razão real para agir agora (vagas, janela, lote) — nunca inventada.
9. **CTA único e específico.** Um caminho de ação, dito com instrução concreta.

## Por que funciona
- **Value Equation.** Cada bloco move uma das 4 alavancas (sobe sonho/probabilidade, baixa tempo/esforço) — princípio `value_equation_test`. Ver [`value-equation`](../../frameworks/value-equation.md).
- **Mecanismo vence saturação.** Em mercado maduro, o "como" único reabre a crença — Schwartz, sofisticação 3-4. Ver [`sophistication-levels`](../../lib/taxonomies/sophistication-levels.md).
- **Ancoragem.** Mostrar o valor somado antes do preço fixa uma referência alta — ver [`anchoring`](../../reference/psychology/anchoring.md).
- **Reversão de risco.** Transferir o risco é a alavanca mais barata para subir conversão sem mexer no preço — ver [`risk-reversal-ladder`](../../frameworks/risk-reversal-ladder.md).
- **Escassez verdadeira.** A urgência real fecha sem mentir — princípio `truthful_scarcity`, sob veto do [compliance-auditor](../../agents/compliance-auditor.md).

## Padrão reutilizável
Esqueleto da oferta-núcleo, abstraído e original:
```
PROMESSA: Você alcança {{resultado-específico}} em {{prazo-crível}}.
MECANISMO: Isso funciona por causa de {{mecanismo-único-nomeado}} —
           o motivo de {{abordagem-comum}} ter falhado até agora.
VOCÊ RECEBE:
  - {{entregável-1}} → resolve {{obstáculo-1}}  (valor: {{R$_1}})
  - {{entregável-2}} → resolve {{obstáculo-2}}  (valor: {{R$_2}})
  - {{entregável-3}} → resolve {{obstáculo-3}}  (valor: {{R$_3}})
BÔNUS (matam objeção):
  - {{bônus-1}} → para quem teme {{objeção-1}}  (valor: {{R$_b1}})
  - {{bônus-2}} → para quem teme {{objeção-2}}  (valor: {{R$_b2}})
VALOR TOTAL: {{soma}}.  HOJE: {{preço}}.
GARANTIA: {{tipo-de-garantia-real}} — o risco é nosso.
POR QUE AGORA: {{razão-verdadeira-de-urgência}}.
AÇÃO: {{CTA-único-com-instrução}}.
```
Regra de ouro: se um item não move uma alavanca de valor nem mata uma objeção, **corte**.

## Adaptação por sofisticação
Ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md).
- **Estágio 1-2:** lidere pela **promessa** direta; o mecanismo fica leve, o benefício carrega a oferta.
- **Estágio 3:** o **mecanismo nomeado** vira o centro — gaste prova mostrando por que é novo e funciona.
- **Estágio 4:** posicione o mecanismo como **superior** (mais rápido, mais fácil, menos sacrifício) com prova comparativa.
- **Estágio 5:** migre o eixo para **identidade** — quem o comprador se torna; a tribo e a prova social pesada conduzem.

## Fonte
> **Fonte:** Alex Hormozi, *$100M Offers* (2021); fundamentos de sofisticação em Eugene M. Schwartz, *Breakthrough Advertising* (1966) — via [`source-catalog`](../../swipe-sources/source-catalog.md). Acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Nenhuma copy de oferta reproduzida; nenhuma citação literal acima.
