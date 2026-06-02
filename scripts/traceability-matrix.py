#!/usr/bin/env python3
"""
traceability-matrix.py — gera docs/traceability-matrix.md a partir do config.yaml

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: config.yaml (routing) + tasks/**/*.md (frontmatter metrics)
PRODUCES: docs/traceability-matrix.md (tabela task -> agents -> frameworks ->
          checklists -> templates -> registry -> metrics)
USAGE: python scripts/traceability-matrix.py [--check]
DEPENDS: stdlib (+ pyyaml)
EXIT: 0 ok · 1 erro · 2 uso
"""
from __future__ import annotations
import argparse, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def task_metrics(name: str) -> str:
    """Lê o frontmatter `metrics:` do arquivo de task correspondente, se houver."""
    for dp, _, fns in os.walk(os.path.join(ROOT, "tasks")):
        if f"{name}.md" in fns:
            txt = open(os.path.join(dp, f"{name}.md"), encoding="utf-8").read()
            m = FM_RE.match(txt)
            if m:
                fm = yaml.safe_load(m.group(1)) or {}
                mt = fm.get("metrics") or []
                return ", ".join(mt) if isinstance(mt, list) else str(mt)
    return "—"


def cell(v) -> str:
    if not v:
        return "—"
    return "<br>".join(v) if isinstance(v, list) else str(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="dry-run (não escreve)")
    a = ap.parse_args()

    cfg = yaml.safe_load(open(os.path.join(ROOT, "config.yaml"), encoding="utf-8"))
    routing = cfg.get("routing", {})

    rows = []
    for name, r in routing.items():
        if not isinstance(r, dict) or "runs" in r:   # pula composites (project types)
            continue
        rows.append((
            name, cell(r.get("agents")), cell(r.get("frameworks")),
            cell(r.get("checklists")), cell(r.get("templates")),
            cell(r.get("registry")), task_metrics(name),
        ))

    out = ["---",
           "id: doc.traceability-matrix",
           "title: \"Matriz de Rastreabilidade (Task -> Agents -> Frameworks -> Checklists -> Templates -> Registries -> Metrics)\"",
           "type: doc", "layer: cross", "status: stable", "version: 1.0.0",
           "updated: 2026-06-02", "owner_agent: knowledge-librarian",
           "tags: [traceability, routing, matrix, generated]", "---", "",
           "# Matriz de Rastreabilidade",
           "",
           "> **Gerado** por `scripts/traceability-matrix.py` a partir de [`config.yaml`](../config.yaml) `routing` "
           "+ o campo `metrics:` de cada `tasks/**`. Não editar à mão — rode o script para regenerar. "
           "É a fonte legível única que liga cada task à sua cadeia operacional.", "",
           "| Task | Agents | Frameworks | Checklists | Templates | Registry | Metrics |",
           "|---|---|---|---|---|---|---|"]
    for row in rows:
        out.append("| `" + row[0] + "` | " + " | ".join(row[1:]) + " |")
    out += ["",
            f"_Tasks roteadas: {len(rows)} · composites (project types) omitidos · "
            "cada célula resolve a ids reservados no config._"]

    text = "\n".join(out) + "\n"
    dest = os.path.join(ROOT, "docs", "traceability-matrix.md")
    if a.check:
        print(f"[--check] geraria {dest} com {len(rows)} tasks (não escrito).")
        sys.exit(0)
    open(dest, "w", encoding="utf-8").write(text)
    print(f"OK · escrito {dest} · {len(rows)} tasks roteadas.")
    sys.exit(0)


if __name__ == "__main__":
    main()
