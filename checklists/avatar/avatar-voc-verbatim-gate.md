---
id: checklist.avatar.avatar-voc-verbatim-gate
title: "Gate — Banco de VOC com ≥10 Verbatims Literais por Segmento (com fonte rastreável)"
type: gate
layer: D1
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: avatar-voc-investigator
frameworks: [avatar-voc-investigator/voc-mining]
registries: [objection-registry]
tags: [gate, avatar, voc, verbatim, d1, fonte, voz-do-cliente]
---

# Gate — Banco de VOC com Verbatims Literais

## Propósito
Este gate prova que o `avatar-voc-investigator` construiu o avatar pela **voz literal do cliente**, não por suposição. Existe porque o avatar de slide ("homem, 35 anos, classe B") não escreve copy que converte — o que converte é a frase exata que o cliente disse, na cabeça dele. O piso é **≥10 verbatims literais por segmento**, cada um com fonte rastreável, porque verbatim fabricado é a falha mais grave deste agente: uma frase "bonita" que ninguém disse envenena toda a copy a jusante. Os escritores de VSL e e-mail herdam este banco para falar na voz do cliente; o `mechanism-architect` herda a culpa que o avatar atribui. Sem verbatims reais, o squad inventa o cliente.

## Dono & Escopo
- **owner_agent:** `avatar-voc-investigator` (etnógrafo do squad, dono do banco de verbatims).
- **Artefato inspecionado:** o **banco de VOC** (`voc-verbatim-bank-template` preenchido) e o avatar/ICP, por segmento, com verbatims e fontes.

## Condição de Passagem
Cada segmento tem pelo menos dez verbatims literais com fonte rastreável, e nenhuma afirmação sobre o cliente aparece sem um verbatim que a sustente.

## Itens
1. **≥10 verbatims por segmento.** Verificar: cada segmento do avatar tem no mínimo dez frases literais coletadas — contagem explícita.
2. **Frases literais, não paráfrase.** Verificar: cada verbatim está entre aspas, na linguagem do cliente ("eu congelo quando o gringo fala rápido"), não reescrito pelo agente.
3. **Fonte por verbatim.** Verificar: cada frase tem origem rastreável (review, entrevista, transcrição de suporte, fórum, DM).
4. **Proxy marcado.** Verificar: verbatims tirados de concorrentes (proxy) estão marcados como "proxy" vs "diretos"; o agente não os mistura sem rótulo.
5. **Sem afirmação órfã.** Verificar: toda afirmação sobre o cliente no avatar aponta para ≥1 verbatim que a sustenta.
6. **Verbatims categorizados.** Verificar: cada frase está marcada por função (dor, desejo, objeção, crença) para o uso a jusante.
7. **Segmentação coerente.** Verificar: se o mercado-alvo abriga duas vozes distintas, há dois segmentos, cada um com seu piso de dez — não uma voz média.

## Evidência Exigida
Para marcar cada item ✅, linkar o banco de VOC com os verbatims numerados, a fonte de cada um e a categoria. A contagem por segmento precisa ser visível (≥10). Verbatims proxy precisam estar rotulados. As objeções extraídas dos verbatims são registradas no [`objection-registry`](../../data/registries/objection-registry.md). O permalink do banco conta como evidência; frases sem fonte são descartadas, não marcadas ✅.

## Protocolo de Falha
Item vermelho → o `avatar-voc-investigator` volta à coleta; abaixo de dez verbatims por segmento, o gate não passa. Verbatim sem fonte → descartado (frase fabricada é falha grave). Fonte de VOC fraca → degrada com elegância: usa reviews de concorrentes como proxy rotulado e **rebaixa a confiança** até atingir o piso, sinalizando ao `offerbook-chief`. Segmento médio que não soa como ninguém → divide em segmentos e minera cada um. Re-entrada: atingido o piso com fontes, o gate é re-submetido. O agente não tem veto; sinaliza VOC insuficiente ao chief.

## Links
- Frameworks: [`voc-mining`](../../frameworks/avatar-voc-investigator/voc-mining.md)
- Registries: [`objection-registry`](../../data/registries/objection-registry.md) · [`proof-registry`](../../data/registries/proof-registry.md)
- Agentes: [`avatar-voc-investigator`](../../agents/avatar-voc-investigator.md) · [`vsl-webinar-scriptwriter`](../../agents/vsl-webinar-scriptwriter.md) · [`email-sms-sequence-writer`](../../agents/email-sms-sequence-writer.md)
- Gate par (emoção): [`avatar-dominant-emotion-gate`](avatar-dominant-emotion-gate.md)
- Recorte de mercado a montante: [`market-awareness-gate`](../market/market-awareness-gate.md)
