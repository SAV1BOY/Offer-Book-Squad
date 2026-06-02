---
id: reference.industry.saas-b2b
title: "Playbook de Setor — SaaS B2B"
type: reference
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: market-sophistication-analyst
tags: [industry, saas, b2b, subscription, plg, free-trial, retention, playbook]
---

# Playbook de Setor — SaaS B2B

Guia de campo para ofertas de **software como serviço para empresas (SaaS B2B)** — assinatura, trial, freemium, vendas self-serve e sales-led. Serve o squad como ponto de partida de diagnóstico. Não substitui a pesquisa do caso — calibra a expectativa e aponta as armadilhas do nicho.

## Panorama do mercado
SaaS B2B vende **software que resolve uma dor operacional e cobra de forma recorrente**. A economia é diferente do infoproduto: o custo de aquisição é alto e se paga ao longo de meses, então **retenção e expansão de receita** (não a venda única) decidem o negócio. O mercado é maduro e competitivo — quase toda categoria já tem players estabelecidos, integrações e comparativos. O comprador empresarial é racional, avalia ROI, envolve um comitê e teme o custo de troca. O dinheiro entra onde o software **economiza tempo/dinheiro mensurável, reduz risco ou gera receita** para a empresa — e onde a adoção é fácil. Dois movimentos dominam: **PLG (product-led growth)**, em que o produto se vende via trial/freemium e o usuário ativa sozinho; e **sales-led**, com vendedor para tickets maiores e ciclos longos. Quem casa o motor de aquisição ao ticket vence; quem usa vendedor caro para produto barato (ou trial para enterprise complexo) queima caixa.

## Avatar & dores típicas
Há dois avatares e eles não coincidem: o **usuário** (quem opera o software no dia a dia) e o **comprador/economic buyer** (quem assina o cheque). O usuário tem dor de processo: "perco horas nisso", "uso planilha e quebra", "as ferramentas não conversam", "não tenho visibilidade". O comprador tem dor de negócio: custo, risco, escala, conformidade. As objeções recorrentes: "qual o ROI?", "quanto custa migrar?", "vai integrar com o que já temos?", "e se a equipe não adotar?", "é seguro?". A objeção mestra B2B é **risco e custo de troca**, não preço. Por isso prova de ROI, casos de empresas parecidas, segurança e onboarding sem dor valem mais que features soltas. Venda para o comprador o resultado de negócio; ao usuário, a vida mais fácil.

## Sofisticação & consciência típicas
Categorias estabelecidas vivem em **estágio 4 a 5** de sofisticação (ver [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md)): muitos players, claims e mecanismos competindo — o diferencial vem de **mecanismo superior** (mais fácil, mais rápido, menos atrito) e de **categoria/posicionamento** ("não somos mais um X, somos o primeiro Y"). Produtos que criam categoria nova podem operar em 2-3. Consciência (ver [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md)) tende a ser alta no fundo do funil — quem busca a categoria está **consciente da solução** (nível 3) ou **do produto** (nível 4), comparando você com concorrentes. O topo ainda pega **consciente do problema** (nível 2), que sente a dor mas não sabe que existe software para isso. Segmente: educar o problema no topo, diferenciar e provar ROI no fundo.

## Ofertas & money models que funcionam
Ver papéis em [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md). A espinha clássica do setor:
- **Atração:** **trial gratuito** ou **freemium** que entrega valor antes de cobrar (o equivalente PLG do tripwire), ou demo/diagnóstico no sales-led. A meta é o **"aha moment"** rápido que liquida o custo de aquisição ao virar conta paga.
- **Núcleo:** o plano de assinatura com **mecanismo nomeado** e empacotamento por valor (tiers). A **garantia** (ver [`../../lib/taxonomies/guarantee-types.md`](../../lib/taxonomies/guarantee-types.md)) aqui é trial sem cartão, SLA, ou garantia de migração — reduz o risco de troca.
- **Upsell:** upgrade de tier, assentos adicionais, módulos premium, done-for-you de implementação, suporte prioritário (expansão é onde o LTV cresce).
- **Downsell:** plano menor, anual com desconto, ou pausa em vez de cancelamento para recuperar quem ia sair.
- **Continuidade:** **é a espinha** — a assinatura mensal/anual é o produto. O foco é reduzir churn e crescer NRR (net revenue retention); a expansão dentro da base costuma valer mais que a venda nova.

## Big Ideas & ângulos comuns
A Big Idea (UMA, ver `one_big_idea`) raramente é "mais features". Costuma ser **uma mudança de categoria ou de jeito de trabalhar** ("pare de [processo antigo] — faça [novo paradigma]"), ancorada em ROI específico e mecanismo de produto defensável. Ângulos que funcionam: o custo invisível do status quo ("quanto você perde por mês fazendo do jeito antigo"), a inversão ("você não precisa de mais ferramentas, precisa de menos"), a categoria nova ([positioning à la Dunford/Moore]). Para o comprador, ancore em número de negócio; para o usuário, na dor diária. Evite a promessa genérica de "produtividade" — vaga e indistinguível dos concorrentes.

## Canais & benchmarks
Faixas **aproximadas e que variam muito** por categoria, ticket e motor (PLG vs sales-led); trate como ponto de partida, não meta.
- **Trial → pago (PLG):** conversão frequentemente citada na faixa de ~15–25% para trial sem cartão e mais alta com cartão exigido; freemium → pago costuma ser bem menor, ~1–5% (aproximado, varia muito).¹
- **Churn:** churn mensal de logos saudável para SMB costuma ser citado em ~3–5% ao mês; menor para mid-market/enterprise (aproximado).²
- **NRR (net revenue retention):** referência "boa" frequentemente citada acima de ~100%, com top performers >120% (aproximado).²
- **CAC payback:** alvo comum citado em ~12 meses ou menos (ilustrativo — depende de margem e ticket).
Sempre meça **ativação, churn e NRR reais** do seu produto; benchmarks externos só servem para detectar anomalia.

## Compliance do setor
O `compliance-auditor` é a última barreira (ver [`../../agents/compliance-auditor.md`](../../agents/compliance-auditor.md)) e pode **vetar**. Pontos críticos do setor:
- **Claims de ROI/desempenho:** "economize X horas", "aumente Y%", "reduza custo em Z" exigem lastro (estudo, caso real, dado próprio) e disclaimer de que resultados variam (ver gate [`../../checklists/compliance/compliance-claim-backing-gate.md`](../../checklists/compliance/compliance-claim-backing-gate.md)). Logo de cliente exige autorização de uso.
- **Dados/privacidade & segurança:** SaaS processa dado de terceiros — LGPD/GDPR, DPA, e claims de segurança (SOC 2, ISO, criptografia) só se forem verdadeiros e comprováveis (gate [`../../checklists/compliance/compliance-data-privacy-gate.md`](../../checklists/compliance/compliance-data-privacy-gate.md)). "Conforme a LGPD" sem lastro é veto.
- **Termos de assinatura:** renovação automática, cancelamento e reembolso precisam ser claros e honestos; cobrança recorrente exige consentimento inequívoco.
- **Escassez verdadeira:** "preço sobe", "vagas no beta", "desconto de lançamento" só se forem **reais** (`truthful_scarcity`; gate [`../../checklists/compliance/compliance-scarcity-truth-gate.md`](../../checklists/compliance/compliance-scarcity-truth-gate.md)).

## Cross-refs
- [`../books/offers-and-monetization/hormozi-100m-money-models.md`](../books/offers-and-monetization/hormozi-100m-money-models.md) · [`../books/offers-and-monetization/ramanujam-monetizing-innovation.md`](../books/offers-and-monetization/ramanujam-monetizing-innovation.md) · [`../books/offers-and-monetization/nagle-strategy-tactics-pricing.md`](../books/offers-and-monetization/nagle-strategy-tactics-pricing.md)
- [`../../lib/taxonomies/sophistication-levels.md`](../../lib/taxonomies/sophistication-levels.md) · [`../../lib/taxonomies/awareness-levels.md`](../../lib/taxonomies/awareness-levels.md) · [`../../lib/taxonomies/offer-types.md`](../../lib/taxonomies/offer-types.md) · [`../../lib/taxonomies/guarantee-types.md`](../../lib/taxonomies/guarantee-types.md)
- [`agencies.md`](agencies.md) — quando SaaS é vendido com serviço. · [`professional-services.md`](professional-services.md) — venda consultiva B2B.
- Próximo do setor: [`../../frameworks/unique-mechanism.md`](../../frameworks/unique-mechanism.md) · [`../../frameworks/value-equation.md`](../../frameworks/value-equation.md) · [`../../frameworks/positioning`](../../frameworks/positioning) (forward-refs).

---
¹ Conversão de trial/freemium: [OpenView / benchmarks de PLG amplamente citados](https://openviewpartners.com/product-led-growth/); valores variam por categoria. ² Churn e NRR: referências citadas frequentemente em [SaaS Capital](https://www.saas-capital.com/) e relatórios de mercado. Demais números marcados como ilustrativos.
