---
id: template.core.launch-blackbook-skeleton
title: "Launch Blackbook Skeleton — O Esqueleto do Blackbook Completo"
type: template
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: offerbook-chief
consumes: [template.core.offer-book-master]
frameworks: [offer-to-funnel-mapping, money-model-sequence, proof-to-claim-chain]
checklists: [blackbook-stack/blackbook-dod-gate, chief/chief-blackbook-readiness-gate]
registries: [offer-registry, control-registry, decision-registry, lessons-learned-registry]
tags: [template, blackbook, skeleton, launch, ops, compliance, core]
---

# Launch Blackbook Skeleton — O Esqueleto do Blackbook Completo

Este é o segundo núcleo do squad. O **Offer Book** prova que a oferta merece existir; o **Blackbook** é o livro de operações que transforma a oferta aprovada em um lançamento que roda. Ele espelha, em uma estrutura única, **toda** a saída de D4 a D7: copy, funil, ops, eventos, afiliados, PR, compliance e memória. Cada seção aponta para o artefato-fonte (não duplica) e diz se está pronto. É contra este esqueleto cheio que o `blackbook-dod-gate` decide se o lançamento pode ir ao ar. Nada de carrinho aberto antes deste mapa estar verde.

## Como usar
- **Agente dono:** `offerbook-chief`. Co-monta com o `offer-squad-architect`; o `compliance-auditor` audita e o `knowledge-librarian` fecha a memória.
- **Tasks:** abre em `assemble-blackbook` (depois do HARD STOP do Offer Book) e fecha quando os 8 capítulos estão preenchidos e o gate verde libera o go-live.
- **Quando:** o Chief cria este arquivo assim que o [`offer-book-master`](offer-book-master.md) passa no `offer-book-dod-gate`. Cada agente D4-D7 entrega seu template de domínio (copy, funil, ops...) e o Chief **transcreve o resumo + o link** para o capítulo correspondente. O esqueleto é um índice operacional, não um depósito de cópia. No fim, roda o [`blackbook-dod-gate`](../../checklists/blackbook-stack/blackbook-dod-gate.md).
- Use número e status binário (pronto/pendente) em cada linha. Use a voz do avatar só onde houver copy resumida. Capítulo sem dono ou sem link = bloco incompleto = gate vermelho.

## Campos & Instruções
- **{{NOME_DA_OFERTA}}** / **{{PROJECT_TYPE}}** — herdados do [`offer-book-master`](offer-book-master.md). O tipo define quais capítulos são obrigatórios (single-promo dispensa afiliados/PR; full-launch exige tudo).
- **{{OFFER_BOOK_LINK}}** — o link para o Offer Book aprovado e a data em que cruzou o HARD STOP. É a chave de entrada deste arquivo.
- **{{COPY_INVENTORY}}** — o inventário de copy (VSL/webinar, sequências de e-mail/SMS, mailers, ads), cada peça com status e link para o template-fonte em `templates/copy/`. Vem de `vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `direct-mail-insert-writer`, `ad-creative-factory`. Cada claim aqui já passou pelo [`proof-block`](../../lib/components/proof-block.md).
- **{{VOICE_STATUS}}** — confirmação de que o `voice-style-guardian` aprovou toda a copy na voz [`brand-default-hormozi-style`](../../voice/profiles/brand-default-hormozi-style.md).
- **{{FUNNEL_MAP}}** — o mapa de funil sem becos sem saída, com URLs e plano de deliverability. Vem de `funnel-architect` e `tech-links-deliverability-engineer`. Usa [`offer-to-funnel-mapping`](../../frameworks/offer-to-funnel-mapping.md).
- **{{OPS_RUN_OF_SHOW}}** — o run-of-show por fase (runway → carrinho aberto → fechamento), com responsáveis e horários. Vem de `launch-producer`.
- **{{EVENTS_LOGISTICS}}** — o calendário de eventos (lives, webinars, aulas) e o inventário de assets. Vem de `events-logistics-coordinator`.
- **{{AFFILIATE_PROGRAM}}** — o programa de afiliados (comissão, prêmios, swipe para parceiros). Vem de `affiliate-program-architect`. Opcional em single-promo.
- **{{PR_PLAN}}** — o plano de PR e marca (ângulos, alvos de imprensa, calendário). Vem de `pr-brand-strategist`. Opcional em single-promo.
- **{{COMPLIANCE_SIGNOFF}}** — o sign-off do `compliance-auditor`: claims com lastro, escassez verdadeira (ver [`scarcity-block`](../../lib/components/scarcity-block.md)), T&Cs, disclaimers, LGPD/FTC. É um capítulo com poder de **veto**.
- **{{MEMORY_UPDATE}}** — o fechamento de memória do `knowledge-librarian`: registries atualizados, controle vencedor arquivado, lições aprendidas. Vem do `lessons-learned-registry`.
- **{{GO_LIVE_STATUS}}** — verde/vermelho do `blackbook-dod-gate`, com data e pendências.

## O Template
```
# LAUNCH BLACKBOOK — {{NOME_DA_OFERTA}}
Project type: {{PROJECT_TYPE}} · Owner: offerbook-chief · Data: {{DATA}}
Offer Book aprovado: {{OFFER_BOOK_LINK}} (HARD STOP cruzado em {{DATA_HARD_STOP}})

## CAP. 1 — COPY & CRIATIVO  (D4 · fonte: templates/copy/)
VSL / Webinar: {{STATUS}} — {{LINK_VSL}}
Sequências e-mail/SMS: {{STATUS}} — {{LINK_SEQ}} ({{N_PASSOS}} passos)
Mailers / inserts: {{STATUS}} — {{LINK_MAILER}}
Matriz de ads: {{STATUS}} — {{LINK_ADS}} ({{N_ANGULOS}} ângulos)
Voz aprovada (voice-style-guardian): {{SIM/NAO}}

## CAP. 2 — FUNIL & TECH  (D5 · fonte: templates/funnel-tech/)
Mapa de funil (sem beco sem saída): {{STATUS}} — {{LINK_FUNIL}}
URLs & links: {{STATUS}} — {{LINK_URLS}}
Deliverability (e-mail/domínio): {{STATUS}} — {{LINK_DELIV}}

## CAP. 3 — OPS & RUN-OF-SHOW  (D6 · fonte: templates/ops/)
Fases do lançamento (runway→cart→close): {{STATUS}} — {{LINK_FASES}}
Run-of-show (quem faz o quê, quando): {{STATUS}} — {{LINK_ROS}}
Plano de surto/fallback: {{STATUS}} — {{LINK_SURGE}}

## CAP. 4 — EVENTOS & LOGÍSTICA  (D6 · fonte: templates/ops/)
Calendário de eventos: {{STATUS}} — {{LINK_CALENDARIO}}
Inventário de assets: {{STATUS}} — {{LINK_ASSETS}}

## CAP. 5 — AFILIADOS  (D6 · fonte: templates/growth/) [{{OBRIGATORIO/OPCIONAL}}]
Programa & comissão: {{STATUS}} — {{LINK_AFILIADOS}}
Swipe para parceiros: {{STATUS}} — {{LINK_SWIPE_AFIL}}
Prêmios / leaderboard: {{STATUS}} — {{LINK_PREMIOS}}

## CAP. 6 — PR & MARCA  (D6 · fonte: templates/growth/) [{{OBRIGATORIO/OPCIONAL}}]
Ângulos de pauta & alvos: {{STATUS}} — {{LINK_PR}}
Calendário de PR: {{STATUS}} — {{LINK_PR_CAL}}

## CAP. 7 — COMPLIANCE  (D7 · veto · fonte: templates/qa/)
Claims com lastro (sem órfão): {{SIM/NAO}}
Escassez/urgência verdadeira: {{SIM/NAO}}
T&Cs · disclaimers · LGPD/FTC: {{SIM/NAO}}
Sign-off do compliance-auditor: {{ASSINADO/PENDENTE}} em {{DATA}}

## CAP. 8 — MEMÓRIA  (D7 · fonte: data/registries/)
Registries atualizados: {{LISTA}}
Controle vencedor arquivado: {{LINK_CONTROL}}
Lições aprendidas: {{N}} registradas — {{LINK_LESSONS}}

## STATUS DO GO-LIVE
blackbook-dod-gate: {{GO_LIVE_STATUS}} — em {{DATA_GATE}}
Pendências: {{O_QUE_FALTA_OU_NENHUMA}}
```

## Exemplo preenchido
> **# LAUNCH BLACKBOOK — Motor de Recuperação 72h**
> Project type: single-promo · Owner: offerbook-chief · Data: 2026-06-02
> Offer Book aprovado: ../core/offer-book-master.md (HARD STOP cruzado em 2026-06-02)
>
> **CAP. 1 — COPY** — VSL: pronto — copy/vsl #v3. Sequências: pronto — 7 passos (carrinho aberto→fechamento). Mailers: n/a (single-promo digital). Ads: pronto — 6 ângulos. Voz aprovada: **sim**.
> **CAP. 2 — FUNIL & TECH** — Mapa: pronto, sem beco sem saída (opt-in→VSL→checkout→upsell→TY). URLs: pronto. Deliverability: pronto (SPF/DKIM/DMARC verdes).
> **CAP. 3 — OPS** — Fases: pronto (runway 7d → cart 5d → close 24h). Run-of-show: pronto. Fallback: pronto (página de espera + e-mail de quebra).
> **CAP. 4 — EVENTOS** — Calendário: pronto (1 aula ao vivo de abertura). Assets: pronto (slides, thumb, lower-thirds).
> **CAP. 5 — AFILIADOS** — **opcional / pulado** nesta promo.
> **CAP. 6 — PR** — **opcional / pulado** nesta promo.
> **CAP. 7 — COMPLIANCE** — Claims com lastro: **sim** (6/6). Escassez verdadeira: **sim** (40 vagas por capacidade de setup). T&Cs/LGPD: **sim**. Sign-off: **assinado** em 2026-06-02.
> **CAP. 8 — MEMÓRIA** — Registries: offer, control, decision atualizados. Controle: control-registry #CTRL-009. Lições: 3 registradas.
> **STATUS** — blackbook-dod-gate: **VERDE** — em 2026-06-02. Pendências: **nenhuma** → liberado para go-live.

## DoD do entregável
O Launch Blackbook está pronto quando: (1) os 8 capítulos estão preenchidos, sem `{{PLACEHOLDER}}` solto, e cada linha tem status binário **e** link ao artefato-fonte; (2) o Offer Book referenciado já cruzou o HARD STOP (este arquivo nunca abre antes); (3) toda a copy de D4 está aprovada na voz pelo `voice-style-guardian`; (4) o funil não tem beco sem saída e a deliverability está verde; (5) o run-of-show nomeia responsável e horário para cada passo, com plano de fallback; (6) os capítulos opcionais (afiliados, PR) estão marcados como obrigatórios **ou** explicitamente pulados conforme o `{{PROJECT_TYPE}}`; (7) o `compliance-auditor` assinou o capítulo 7 — sem órfão de prova e com escassez verdadeira (poder de veto); (8) o `knowledge-librarian` atualizou os registries e registrou as lições. Só então o [`blackbook-dod-gate`](../../checklists/blackbook-stack/blackbook-dod-gate.md) fica verde e o lançamento vai ao ar. O Offer Book entra por [`offer-book-master`](offer-book-master.md); a memória final sai para o [`lessons-learned-registry`](../../data/registries/lessons-learned-registry.md).
