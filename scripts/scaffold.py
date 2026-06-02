#!/usr/bin/env python3
"""
scaffold.py — gera frontmatter + esqueleto de seções conforme o type

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: as regras de docs/style-guide.md §4 (seções por tipo) + ARCHITECTURE.md §5.1 (frontmatter) + a regra path->id de id-resolver.py
PRODUCES: um .md novo conformante no path indicado (frontmatter + headings ##)
USAGE:
  python scripts/scaffold.py --type framework --path frameworks/copy/aida.md --title "AIDA"
  python scripts/scaffold.py --type checklist --path checklists/market/market-sophistication-gate.md
  python scripts/scaffold.py --type framework --path frameworks/copy/aida.md --check   # dry-run: imprime, não escreve
DEPENDS: stdlib (+ pyyaml)
EXIT: 0 ok (arquivo gerado / dry-run limpo) · 1 falha de validação (path/type/colisão) · 2 erro de uso
"""
from __future__ import annotations
import argparse, datetime, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário (pip install pyyaml)"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()

ALLOWED_TYPES = {
    "agent", "checklist", "gate", "framework", "reference", "template", "task",
    "workflow", "swipe", "swipe-source", "voice", "phrases", "registry",
    "component", "pattern", "utility", "taxonomy", "script", "project-phase",
    "doc", "config",
}

# Seções `##` obrigatórias por tipo (docs/style-guide.md §4). Conteúdo em PT.
SECTIONS = {
    "checklist": ["Propósito", "Dono & Escopo", "Condição de Passagem", "Itens",
                  "Evidência Exigida", "Protocolo de Falha", "Links"],
    "gate": ["Propósito", "Dono & Escopo", "Condição de Passagem", "Itens",
             "Evidência Exigida", "Protocolo de Falha", "Links"],
    "framework": ["TL;DR", "Quando usar / Quando não", "Inputs", "Procedimento",
                  "Outputs", "Exemplo", "Armadilhas", "Interações", "Fontes"],
    "reference": ["Citação", "Tese central", "Frameworks/Modelos", "Princípios",
                  "Como o squad usa", "Cross-refs"],
    "template": ["Como usar", "Campos & Instruções", "O Template",
                 "Exemplo preenchido", "DoD do entregável"],
    "task": ["Objetivo", "Agente dono", "Gatilho / Quando", "Inputs (Consome)",
             "Procedimento", "Frameworks", "Outputs (Produz)",
             "Definition of Done", "Gates", "Handoff"],
    "workflow": ["Objetivo", "Gatilho", "Agentes", "Mapa de Estágios", "Diagrama",
                 "Pontos de Decisão", "Critério de Saída", "Falha/Rollback"],
    "swipe": ["O que é", "Anatomia", "Por que funciona", "Padrão reutilizável",
              "Adaptação", "Fonte"],
    "swipe-source": ["Propósito", "Catálogo de Fontes", "Regras de Uso & Licença"],
    "voice": ["Identidade", "Diais de Tom (1-5)", "Léxico (usar/banir)",
              "Cadência & Sintaxe", "Exemplos Faz/Não-faz", "Notas de Compliance"],
    "phrases": ["Propósito", "Bancos de Frases", "Notas de Uso"],
    "registry": ["Propósito", "Schema", "Quem escreve / Quem lê", "Registros"],
    "component": ["Propósito", "Esqueleto", "Como preencher", "Exemplo"],
    "pattern": ["Propósito", "Estrutura", "Quando aplicar", "Exemplo"],
    "utility": ["Propósito", "Contrato (I/O)", "Comportamento", "Como o script implementa"],
    "taxonomy": ["Propósito", "Termos", "Notas de Uso"],
    "project-phase": ["Objetivo da Fase", "Critério de Entrada", "Agentes & Tasks",
                      "Passos (runbook)", "Artefatos Produzidos", "Gates",
                      "Critério de Saída"],
    "doc": ["Propósito", "Conteúdo", "Cross-refs"],
    "agent": ["Identidade & Missão", "Gatilhos de Ativação", "Inputs (Consome)",
              "Protocolo de Raciocínio (HRM)", "Procedimento", "Frameworks & Checklists",
              "Outputs (Produz)", "Vetos & Limites", "Handoff", "Exemplo"],
    "config": ["Propósito", "Schema", "Notas"],
    "doc-readme": ["Propósito", "Conteúdo", "Cross-refs"],
}

# Prefixo do path (1º segmento) -> namespace do id. Espelha id-resolver.PREFIX_MAP.
PREFIX_MAP = {
    "agents": "agent", "frameworks": "framework", "tasks": "task",
    "workflows": "workflow", "checklists": "checklist", "templates": "template",
    "reference": "reference", "swipe": "swipe", "swipe-sources": "swipe-source",
    "voice": "voice", "phrases": "phrases", "authority": "authority",
    "projects": "project", "archive": "archive", "data": "data", "docs": "doc",
    "lib": "lib",
}
SUBDIR_SINGULAR = {
    ("lib", "components"): "component",
    ("lib", "patterns"): "pattern",
    ("lib", "utilities"): "utility",
    ("data", "registries"): "registry",
    ("voice", "profiles"): "profile",
    ("reference", "swipe-breakdowns"): "swipe-breakdown",
}


def derive_id(relpath: str) -> str:
    """Deriva o id determinístico a partir do path relativo (ARCHITECTURE §5.2)."""
    rel = relpath.replace(os.sep, "/")
    parts = rel.split("/")
    parts[-1] = os.path.splitext(parts[-1])[0]
    if parts[-1].lower() == "readme":
        parts[-1] = "readme"
    top = parts[0]
    if len(parts) >= 2 and (top, parts[1]) == ("lib", "taxonomies"):
        return ".".join(["taxonomy"] + parts[2:])
    out = [PREFIX_MAP.get(top, top)]
    if len(parts) >= 2 and (top, parts[1]) in SUBDIR_SINGULAR:
        out.append(SUBDIR_SINGULAR[(top, parts[1])])
        out.extend(parts[2:])
    else:
        out.extend(parts[1:])
    return ".".join(out)


def humanize(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").strip().title()


def layer_for(rel: str) -> str:
    """Camada default: a maioria dos artefatos é cross; project-phase fica cross também."""
    return "cross"


def build_frontmatter(file_type: str, rel: str, title: str) -> str:
    slug = os.path.splitext(os.path.basename(rel))[0]
    fm = {
        "id": derive_id(rel),
        "title": title or humanize(slug),
        "type": file_type,
        "layer": layer_for(rel),
        "status": "draft",
        "version": "0.1.0",
        "updated": TODAY,
        "owner_agent": "knowledge-librarian",
    }
    # sources é obrigatório em reference/framework-reference/swipe (ARCHITECTURE §5.5)
    needs_sources = (
        rel.startswith("reference/")
        or rel.startswith("frameworks/reference-intellectual/")
        or rel.startswith("swipe")
    )
    if needs_sources:
        fm["sources"] = ["TODO: Autor, *Título* (Ano) — via <URL>, acesso " + TODAY]
    fm["tags"] = [file_type]
    body = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return "---\n" + body + "---\n"


def build_body(file_type: str, title: str, rel: str) -> str:
    slug = os.path.splitext(os.path.basename(rel))[0]
    heading = title or humanize(slug)
    sections = SECTIONS.get(file_type, ["Propósito", "Conteúdo"])
    lines = [f"# {heading}", ""]
    for sec in sections:
        lines.append(f"## {sec}")
        lines.append(f"<!-- TODO ({file_type}): preencher \"{sec}\" conforme docs/style-guide.md §4. -->")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description="Gera um .md conformante (frontmatter + seções por tipo).")
    ap.add_argument("--type", required=True, help="tipo do arquivo (ver docs/style-guide.md §4)")
    ap.add_argument("--path", required=True, help="path relativo à raiz, ex.: frameworks/copy/aida.md")
    ap.add_argument("--title", default="", help="título humano (default: derivado do filename)")
    ap.add_argument("--check", action="store_true", help="dry-run read-only: imprime o conteúdo, não escreve")
    ap.add_argument("--force", action="store_true", help="sobrescreve se o arquivo já existir")
    a = ap.parse_args()

    if a.type not in ALLOWED_TYPES:
        print(f"ERRO: type inválido {a.type!r}. Aceitos: {sorted(ALLOWED_TYPES)}"); sys.exit(2)

    rel = a.path.replace(os.sep, "/").lstrip("/")
    if not rel.endswith(".md"):
        print(f"ERRO: --path deve terminar em .md (recebi {rel!r})"); sys.exit(2)

    abs_path = os.path.normpath(os.path.join(ROOT, rel))
    if not abs_path.startswith(ROOT):
        print("ERRO: --path escapa da raiz do repo"); sys.exit(2)

    content = build_frontmatter(a.type, rel, a.title) + "\n" + build_body(a.type, a.title, rel)

    print("\n=== SCAFFOLD ===")
    print(f"type: {a.type} · path: {rel} · id: {derive_id(rel)}")
    print(f"seções: {len(SECTIONS.get(a.type, [])) or 'genérico'}")

    if os.path.exists(abs_path) and not a.force:
        print(f"  ✗ já existe: {rel} (use --force para sobrescrever)")
        print("\nRESULTADO: NÃO ESCRITO ❌\n")
        sys.exit(1)

    if a.check:
        print("\n--- DRY-RUN (conteúdo gerado, nada escrito) ---")
        print(content)
        print("RESULTADO: DRY-RUN OK ✅\n")
        sys.exit(0)

    os.makedirs(os.path.dirname(abs_path) or ".", exist_ok=True)
    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ escrito: {rel}")
    print("\nRESULTADO: GERADO ✅\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
