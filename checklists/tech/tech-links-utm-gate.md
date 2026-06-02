---
id: checklist.tech.tech-links-utm-gate
title: "Gate — Links & UTM (cada destino rastreado por uma convenção consistente)"
type: gate
layer: D5
status: stable
version: 1.0.0
updated: 2026-06-02
owner_agent: tech-links-deliverability-engineer
frameworks: [launch/surge-ops]
registries: [decision-registry]
tags: [gate, tech, links, utm, rastreamento, atribuicao, d5]
---

# Gate — Links & UTM
 
## Propósito
Este gate prova que **cada link do lançamento carrega uma UTM consistente e cada destino é rastreável**. Ele existe porque sem atribuição o time não sabe de onde veio a conversão — qual ad, qual ângulo, qual e-mail vendeu — e otimiza no escuro. O `tech-links-deliverability-engineer` gera um link rastreado por origem, campanha e conteúdo (o ângulo) para cada destino da `ad-matrix` e das sequências, padroniza a convenção e encurta o que precisa. O tráfego pago exige um link por ângulo (eixo dor/mecanismo/identidade) para o funil atribuir a conversão à criativa certa. Vale o princípio `traceability_before_eloquence`: rastreabilidade vence beleza. Uma UTM inconsistente — `origem=fb` numa peça, `origem=facebook` noutra — fragmenta o relatório e mente sobre o que funciona. Este gate julga **só a instrumentação dos links** — que nenhum link crie redirecionamento circular é do `tech-anti-loop-gate`. O rastreamento sem consentimento (cookies/LGPD) é flag ao `compliance-auditor`. O link sem UTM ou com convenção quebrada recebe marca até a padronização entrar.

## Dono & Escopo
- **owner_agent:** `tech-links-deliverability-engineer` (gera, padroniza e encurta os links rastreados).
- **Artefato inspecionado:** o `links-urls` cruzado com os destinos e ângulos da `ad-matrix` e das `email-sms-sequences`. O resultado vai ao [`decision-registry`](../../data/registries/decision-registry.md). Gate consumido em `config.yaml: routing.plan-tech-deliverability`. Modelo: [`links-urls-template`](../../templates/funnel-tech/links-urls-template.md).

## Condição de Passagem
Cada destino do funil tem um link rastreado por uma convenção UTM consistente (origem/campanha/conteúdo), pronto para atribuição.

## Itens
1. **UTM por destino.** Verificar: cada link relevante carrega UTM; nenhum destino de campanha sem rastreamento.
2. **Convenção consistente.** Verificar: origem, campanha e conteúdo seguem o mesmo padrão em toda peça (sem `fb` vs `facebook`).
3. **Conteúdo = ângulo.** Verificar: o parâmetro de conteúdo identifica o ângulo (dor/mecanismo/identidade) para atribuir a criativa.
4. **Link por ângulo no tráfego pago.** Verificar: cada criativa da `ad-matrix` tem seu próprio link rastreado.
5. **Encurtamento sem perda.** Verificar: links encurtados preservam a UTM no destino final.
6. **Atribuição testada.** Verificar: a conversão chega ao relatório com origem/campanha/conteúdo corretos.

## Evidência Exigida
Para marcar ✅: linkar a tabela de links no [`decision-registry`](../../data/registries/decision-registry.md) no formato `{destino, utm: {origem, campanha, conteudo}, encurtado?}`, mais o teste de atribuição mostrando a conversão chegando com os parâmetros certos. Os destinos e ângulos da `ad-matrix` que embasaram os links ficam citados.

## Protocolo de Falha
Item vermelho → o `tech-links-deliverability-engineer` **padroniza a convenção** (origem/campanha/conteúdo) para que a atribuição funcione antes de liberar a tabela. O engenheiro **não tem veto** sobre o pipeline. Rastreamento/captura sem aviso de privacidade ou consentimento vira flag ao [`compliance-auditor`](../../agents/compliance-auditor.md), dono do veto (LGPD/cookies). Link que cria redirecionamento circular é tratado no [`tech-anti-loop-gate`](tech-anti-loop-gate.md). Re-entrada: padronizar a UTM, re-testar a atribuição e atualizar o `decision-registry`.

## Links
- Frameworks: [`launch/surge-ops`](../../frameworks/launch/surge-ops.md)
- Registries: [`decision-registry`](../../data/registries/decision-registry.md)
- Agentes: [`tech-links-deliverability-engineer`](../../agents/tech-links-deliverability-engineer.md) · [`funnel-architect`](../../agents/funnel-architect.md) · [`compliance-auditor`](../../agents/compliance-auditor.md)
- Gates irmãos: [`tech-load-test-gate`](tech-load-test-gate.md) · [`tech-deliverability-gate`](tech-deliverability-gate.md) · [`tech-anti-loop-gate`](tech-anti-loop-gate.md) · [`tech-fallback-gate`](tech-fallback-gate.md)
