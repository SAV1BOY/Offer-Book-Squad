---
id: lib.utility.readability-checker
title: "Verificador de Legibilidade (nível ~3ª série)"
type: utility
layer: cross
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: voice-style-guardian
frameworks: []
tags: [utility, readability, voice, plain-language, qa, reuse]
---

# Verificador de Legibilidade (nível ~3ª série)

## Propósito
Esta utility mede se um texto está no **nível de leitura ~3ª série** — o piso de clareza da voz do squad (perfil `brand-default-hormozi-style`). Frase curta vende; parágrafo longo perde o leitor. Ela calcula o nível de leitura, aponta as frases que estão acima do alvo, e sinaliza jargão, advérbios e voz passiva — os inimigos da clareza descritos no [`style-guide`](../../docs/style-guide.md) §1.

É a ferramenta de QA da voz: o `voice-style-guardian` a roda em toda copy (D4) antes de aprovar. Em vez de "está confuso", ela dá um número e uma lista de correções concretas. Reutilizável em qualquer artefato de texto — VSL, e-mail, ad, página, e até nos próprios arquivos da lib.

## Spec
**Inputs:**
- `texto` — o conteúdo a checar (string ou path de arquivo `.md`).
- `nivel_alvo` (default = 3) — série de leitura desejada.
- `idioma` (default = pt) — ajusta a fórmula ao português.

**Outputs:**
- `nivel_leitura` — série estimada (ex.: "4,2").
- `media_palavras_frase` — alvo ≤ ~12.
- `frases_longas` — lista de frases acima do alvo (com sugestão de quebra).
- `jargao_flag` — termos do [`do-not-say`](../../voice/do-not-say.md) encontrados.
- `passiva_flag` — trechos em voz passiva (alvo: voz ativa).
- `adverbios_flag` — advérbios floreados ("-mente" desnecessário).
- `veredito` — `PASSA / AJUSTAR`.

**Lógica:**
1. Tokeniza em frases e palavras; conta sílabas (heurística PT).
2. Aplica uma fórmula de legibilidade adaptada ao português (índice tipo Flesch ajustado).
3. Marca frases com >12 palavras ou >1 vírgula (regra de "uma vírgula no máximo").
4. Cruza o léxico com o banco [`do-not-say`](../../voice/do-not-say.md).
5. Detecta passiva ("foi feito", "é realizado") e advérbios floreados.
6. Veredito `AJUSTAR` se `nivel_leitura > nivel_alvo + 1` ou se houver flags críticas.

## Como um script implementa
`scripts/readability-checker.py` (owner: voice-style-guardian). Roda com `python scripts/readability-checker.py <path>` e `--check` para dry-run read-only; pode rodar em lote sobre uma pasta. É chamado pelo [`qa-runner.py`](../../scripts/qa-runner.py) como sub-checagem da voz e pelo gate `voice/voice-checklist`. Stdlib + pyyaml (única dep externa), conforme [`style-guide`](../../docs/style-guide.md) §4k. `EXIT 0` passa, `1` se o texto fica acima do alvo (falha de voz), `2` erro de uso. Saída: relatório markdown com nível, frases longas e flags.

## Exemplo
> **Input:** *"A nossa metodologia foi cuidadosamente desenvolvida para que, de maneira eficaz, os resultados sejam alcançados pelos clientes."*
> **Output:**
> - nivel_leitura: **9,1** (muito acima do alvo 3)
> - media_palavras_frase: **18**
> - passiva_flag: **SIM** ("foi desenvolvida", "sejam alcançados")
> - adverbios_flag: **SIM** ("cuidadosamente", "eficazmente")
> - veredito: **AJUSTAR**
> - sugestão: *"Nosso método entrega o resultado. Rápido."* (nível 2,0; voz ativa).

A frase original reprova; a reescrita passa. O número torna a voz auditável, não opinativa.

## Liga com
- **Frameworks:** nenhum (utility de QA transversal).
- **Docs/Voz:** [`style-guide`](../../docs/style-guide.md) §1 (a voz padrão), [`do-not-say`](../../voice/do-not-say.md) (léxico banido).
- **Scripts:** [`qa-runner.py`](../../scripts/qa-runner.py) (chama esta checagem na validação de voz).
- **Agentes:** `voice-style-guardian` (dono — roda em toda copy e pode **vetar** texto fora da voz), e **todos** os agentes de copy (`vsl-webinar-scriptwriter`, `email-sms-sequence-writer`, `direct-mail-insert-writer`, `ad-creative-factory`) como checagem antes do handoff.
