---
id: task.copy.voice-pass
title: "Task — Passe de Voz (Voice & Style Guardian)"
type: task
layer: D4
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
consumes:
  - artifact.vsl-script
  - artifact.email-sms-sequences
  - artifact.mailers-inserts
  - artifact.ad-matrix
  - lib/voice/brand-voice-guide
produces:
  - decision.voice-verdict
  - artifact.voice-redline
frameworks: [copy/hook-frameworks, copy/fascination-bullets]
checklists:
  - voice/voice-checklist
  - voice/voice-reading-level-gate
  - voice/voice-active-present-gate
  - voice/voice-no-adverb-gate
  - voice/voice-positive-language-gate
registries: [control-registry]
tags: [copy, voz, estilo, veto, passe, legibilidade, voz-ativa, guardiao, d4]
---

# Task — Passe de voz: o Voice & Style Guardian audita toda peça de copy e veta o que foge do padrão

## Objetivo
Auditar cada frase de cada peça de copy contra o guia de voz e emitir UM veredito — APROVADO, ou REPROVADO com a linha exata e a correção sugerida — para que nenhuma copy fora do padrão (3ª série, voz ativa, presente, sem advérbios, enquadramento positivo) chegue ao leitor ou ao downstream.

## Agente dono
[`voice-style-guardian`](../../agents/voice-style-guardian.md). É a última lente entre a copy e o leitor real. Diferente dos outros agentes de D4 (que criam), seu produto é um **veredito**. **Tem poder de veto de voz.**

## Gatilho / Quando
Roda como **passe obrigatório em TODAS as peças de copy de D4**, depois que o autor as emite e **dentro do mesmo HARD STOP** — a copy só existe porque o [`offer-book-stack/offer-book-dod-gate`](../../checklists/offer-book-stack/offer-book-dod-gate.md) já passou. É a etapa final de cada task de copy: [`write-vsl-webinar`](write-vsl-webinar.md), [`write-email-sms-sequences`](write-email-sms-sequences.md), [`write-mailers-inserts`](write-mailers-inserts.md) e [`generate-ad-matrix`](generate-ad-matrix.md). Demais gatilhos: pedido de auditoria de um lote, ou atualização do guia de voz que exige re-checagem do material existente. A peça precisa estar **completa o suficiente** para julgar e o `brand-voice-guide` carregado.

## Inputs (Consome)
- `artifact.vsl-script` / `artifact.email-sms-sequences` / `artifact.mailers-inserts` / `artifact.ad-matrix` — **cada frase** do corpo, ganchos, CTAs e legendas. Não amostrar — auditar por inteiro é o trabalho.
- `lib/voice/brand-voice-guide` — o perfil `brand-default-hormozi-style`: nível de leitura 3ª série, tempo presente, voz ativa, frases curtas, linguagem positiva, sem advérbios, sem redundância. É a régua.
- Autor/origem declarado da peça (rastreabilidade). Peça sem autor → pedir a fonte antes de auditar.

## Procedimento
1. **Confirmar a fonte.** Peça sem autor/origem → pedir a fonte antes de auditar. Peça truncada → auditar o que existe, marcar o ausente como `não_avaliável` e pedir a peça completa. **Nunca aprovar o que não leu.**
2. **Carregar a régua.** Ler o `brand-voice-guide` (perfil padrão, nível, tempo, voz, regras).
3. **Auditar frase a frase (L-Module).** Para cada frase, aplicar o checklist de voz: (a) frases curtas no teto de legibilidade; (b) ≤1 vírgula por frase; (c) sem advérbios (caçar `-mente`, "muito", "realmente", "rapidamente", "provavelmente"); (d) voz ativa (sujeito age); (e) tempo presente; (f) enquadramento positivo (diz o ganho, não só o medo); (g) sem redundância; (h) 3ª série (palavra curta e comum vence a sofisticada).
4. **Marcar cada violação.** Uma violação dura (advérbio, voz passiva evitável, frase acima do teto, enquadramento negativo dispensável, nível acima da 3ª série) marca a frase. Registrar `{linha, violação, trecho original}`.
5. **Reescrever preservando a persuasão (ToT).** Quando a frase falha mas a intenção precisa ser salva, gerar ≥3 reescritas e pontuar 0–5 por: conformidade de voz (×3), legibilidade 3ª série (×3), força preservada (×2), enquadramento positivo (×2). Ancorar em [`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md) ao consertar um gancho e em [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md) ao recompor bullets, para não matar o benefício.
6. **Consolidar o veredito (H-Module).** A peça passa nos quatro gates de voz? Se **qualquer** um falha → **REPROVADO** + redline. Não existe "aprovado com ressalvas": ou está na voz, ou volta.
7. **Tratar o conflito guia × compliance.** Disclaimer legal obrigatório que não cabe em 3ª série → **não remover o disclaimer**; escalar ao [`offerbook-chief`](../../agents/offerbook-chief.md) para arbitrar (a lei vence o estilo) e registrar o override.
8. **Registrar e devolver/liberar.** Logar o veredito de cada peça no `control-registry`. REPROVADO → devolver a redline ao autor (rodada N) e re-auditar no reenvio. APROVADO → liberar ao downstream. Máximo de 3 rodadas antes de escalar o impasse ao chief.

## Frameworks
[`copy/hook-frameworks`](../../frameworks/copy/hook-frameworks.md) · [`copy/fascination-bullets`](../../frameworks/copy/fascination-bullets.md).

## Outputs (Produz)
- `decision.voice-verdict` — APROVADO | REPROVADO, com nível de leitura medido e resumo de marcas por tipo.
- `artifact.voice-redline` (quando reprovado) — tabela `{linha, violação, trecho original, correção sugerida}`.
- [`control-registry`](../../data/registries/control-registry.md) atualizado (`asset_id`, tipo, veredito, marcas, rodada, autor_origem, `override_decision_id?`). Padrões de erro recorrentes sinalizados ao [`knowledge-librarian`](../../agents/knowledge-librarian.md).

## Definition of Done
- Cada frase de cada peça auditada (não amostra); nível de leitura medido contra a 3ª série.
- Veredito emitido: APROVADO (todas as frases passam nos quatro gates) ou REPROVADO com redline linha a linha.
- Conflito guia × compliance escalado ao chief e registrado como override quando aplicável (override sem registro não existe).
- Veredito registrado no `control-registry`; só copy APROVADA (ou liberada por `override_decision_id`) segue ao downstream.

## Gates
[`voice/voice-checklist`](../../voice/voice-checklist.md) · [`voice/voice-reading-level-gate`](../../checklists/voice/voice-reading-level-gate.md) · [`voice/voice-active-present-gate`](../../checklists/voice/voice-active-present-gate.md) · [`voice/voice-no-adverb-gate`](../../checklists/voice/voice-no-adverb-gate.md) · [`voice/voice-positive-language-gate`](../../checklists/voice/voice-positive-language-gate.md).

## Handoff
**Veto e devolução:** copy REPROVADA volta ao autor — [`vsl-webinar-scriptwriter`](write-vsl-webinar.md), [`email-sms-sequence-writer`](write-email-sms-sequences.md), [`direct-mail-insert-writer`](write-mailers-inserts.md) ou [`ad-creative-factory`](generate-ad-matrix.md) — que corrige e reenvia. **Próximas tasks (só com veredito APROVADO):** [`map-funnel`](../funnel-tech/map-funnel.md) (a copy que vira páginas), [`plan-tech-deliverability`](../funnel-tech/plan-tech-deliverability.md) (e-mail pronto para envio) e [`compliance-audit`](../qa-memory/compliance-audit.md) (copy já conforme à voz, para a auditoria de claims/escassez). **Contrato:** todo downstream pode confiar que a copy recebida está na voz da marca — ativa, presente, sem advérbio, positiva, 3ª série — ou carrega um `override_decision_id` explícito. O guardião **só** julga voz e estilo, nunca o ângulo, a oferta ou o claim.
