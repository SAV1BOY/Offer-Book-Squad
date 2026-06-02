---
id: framework.proof-to-claim-chain
title: "Proof-to-Claim Chain — Cada Claim Aponta para Sua Prova"
type: framework
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: proof-credibility-curator
frameworks: [value-equation, unique-mechanism, guarantee-design, scarcity-urgency-engine, grand-slam-offer]
sources:
  - "Claude Hopkins, *Scientific Advertising* (1923) — provar, não afirmar."
  - "Alex Hormozi, *$100M Offers* (2021) — prova e credibilidade."
tags: [proof, claim, traceability, credibility, compliance, evidence]
---

# Proof-to-Claim Chain — A Cadeia Prova→Claim

## TL;DR
Toda afirmação que você faz é uma dívida; a **prova** paga essa dívida. A regra do squad é `evidence_before_opinion`: nenhum claim entra na copy sem uma prova ligada a ele. Você cria uma **cadeia rastreável** — cada claim ↔ sua evidência (depoimento, dado, demonstração, estudo) — e tudo o que não tem lastro é **cortado** ou rebaixado. O `proof-credibility-curator` constrói a cadeia; o `compliance-auditor` **veta** qualquer claim órfão. Mostre, não diga.

## Quando usar / Quando não
**Use** em toda peça com afirmações: oferta, VSL, ad, e-mail, garantia, mecanismo.
**Use** como auditoria final antes do HARD STOP (Offer Book DoD) e antes do compliance.
**Não use** prova fraca para sustentar claim forte: um depoimento vago não paga uma promessa numérica.
**Não use** para "decorar" com prova irrelevante — cada prova precisa sustentar **aquele** claim específico.

## Inputs
- A **lista de claims** de todas as peças (promessas, números, superioridade, do mecanismo, da garantia).
- O **banco de prova**: depoimentos, estudos de caso, dados, demonstrações, credenciais, screenshots.
- A taxonomia de força de prova (qual tipo sustenta qual nível de claim).
- Os registries `claim-registry` e `proof-registry`.
- As regras de compliance aplicáveis (FTC/LGPD/CDC sobre claims de resultado).

## Procedimento
1. **Extraia todos os claims** de cada peça. Liste um por linha — promessa, número, "melhor que", afirmação do mecanismo, condição da garantia.
2. **Classifique a força exigida** por claim: claim numérico/extraordinário exige prova forte (dado, caso documentado); claim brando aceita prova mais leve.
3. **Inventarie a prova disponível** e classifique cada uma por força: demonstração ao vivo e dado auditável > estudo de caso > depoimento específico > depoimento vago > opinião do vendedor.
4. **Ligue cada claim à sua prova** (a cadeia). Use IDs cruzados entre `claim-registry` e `proof-registry`.
5. **Marque os órfãos**: todo claim sem prova suficiente. Para cada órfão, decida: **conseguir a prova**, **rebaixar o claim** até o que a prova sustenta, ou **cortar**.
6. **Cheque a relevância**: a prova fala **exatamente** do claim? Resultado de outro avatar/contexto não sustenta este claim.
7. **Confirme a verdade e a permissão**: a prova é real, verificável e autorizada (uso de depoimento, dados). Prova fabricada é veto e crime.
8. **Posicione a prova na peça**: ao lado do claim que ela sustenta, no ponto de maior ceticismo (preço, mecanismo, garantia).
9. **Registre** a cadeia completa; rode `proof/proof-claim-backing-gate` e o gate de compliance (`compliance/compliance-claim-backing-gate`). Nenhum claim órfão passa.

## Outputs
- **Matriz claim ↔ prova**: cada claim com sua evidência, força e localização na peça.
- Lista de **claims órfãos** com a decisão (provar / rebaixar / cortar).
- Veredito de relevância e verdade por prova.
- Status dos gates de lastro (sem órfãos = verde).

## Exemplo
Oferta de amostra: curso de inglês para profissionais de TI. Claims extraídos:
- *"Aprovado na entrevista em 60 dias"* → exige prova forte. **Prova**: 12 estudos de caso com data de início e oferta de emprego (screenshots autorizados). **Liga.**
- *"O Shadowing Técnico destrava a fala sob pressão"* (claim do mecanismo) → **Prova**: gravação antes/depois de 3 alunos numa simulação. **Liga.**
- *"O método mais eficaz do Brasil"* → claim de superioridade **sem** prova comparativa. **Órfão.** Decisão: **rebaixar** para "o método focado em entrevista que já aprovou 120 devs" (sustentável por dado).
- *"Você vai ganhar em dólar"* → resultado fora do controle do produto. **Órfão.** Decisão: **cortar** da promessa (vira benefício possível, não claim).
- **Resultado**: cada claim que fica tem prova relevante ao lado; os órfãos foram rebaixados ou cortados antes do compliance. A copy fica forte **e** defensável.

## Armadilhas
- **Claim órfão.** Afirmação sem prova é veto — e mina a confiança quando o prospect cobra.
- **Prova fraca para claim forte.** Depoimento vago não paga uma promessa numérica; cada nível exige força proporcional.
- **Prova irrelevante.** Resultado de outro contexto/avatar não sustenta este claim — relevância é obrigatória.
- **Prova fabricada ou sem permissão.** Crime e veto certo; só prova real e autorizada entra.
- **Prova longe do claim.** Evidência no rodapé não vence o ceticismo no ponto do preço — posicione junto.

## Interações
- **Agentes**: `proof-credibility-curator` (dono — constrói a cadeia); `compliance-auditor` (**veta** claim órfão — `compliance/compliance-claim-backing-gate`); `mechanism-architect` (prova do mecanismo); `value-equation-engineer` (a Probabilidade percebida vive de prova); `vsl-webinar-scriptwriter`, `ad-creative-factory`, `email-sms-sequence-writer` (posicionam prova ao lado do claim); `knowledge-librarian` (mantém o `proof-registry`).
- **Frameworks que pareiam**: [`value-equation.md`](value-equation.md), [`unique-mechanism.md`](unique-mechanism.md), [`guarantee-design.md`](guarantee-design.md), [`scarcity-urgency-engine.md`](scarcity-urgency-engine.md), [`offer/grand-slam-offer.md`](offer/grand-slam-offer.md).

## Fontes
> **Fonte:** Claude Hopkins, *Scientific Advertising* (1923), "provar, não afirmar"; Alex Hormozi, *$100M Offers* (2021), prova e credibilidade — via [`../reference/books/copywriting/hopkins-scientific-advertising.md`](../reference/books/copywriting/hopkins-scientific-advertising.md), acesso 2026-06-02.
> **Anti-verbatim:** estrutura e princípios em redação original. Citação literal ≤ 25 palavras, atribuída.
