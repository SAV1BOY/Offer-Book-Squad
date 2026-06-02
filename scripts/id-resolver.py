#!/usr/bin/env python3
"""
id-resolver.py — constrói e valida o mapa id<->path (bijeção) de todos os .md

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: todos os .md do repo (frontmatter `id`) + a regra path->id de ARCHITECTURE.md §5.2
PRODUCES: relatório no stdout + .id-resolver.json (na raiz)
USAGE:
  python scripts/id-resolver.py            # valida o repo inteiro
  python scripts/id-resolver.py --dir agents
  python scripts/id-resolver.py --check    # dry-run read-only (não escreve o json)
DEPENDS: stdlib (+ pyyaml)
EXIT: 0 bijeção ok · 1 colisão/id<->path inconsistente · 2 erro de uso
"""
from __future__ import annotations
import argparse, json, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário (pip install pyyaml)"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env", "fixtures"}
# .md sem frontmatter aceitos (infra de repo) — não entram no mapa de ids:
NO_FRONTMATTER_OK = {"README.md", "ARCHITECTURE.md", "BUILD-PROGRESS.md"}

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Mapa do PRIMEIRO segmento do path -> namespace do id (plural -> singular).
PREFIX_MAP = {
    "agents": "agent", "frameworks": "framework", "tasks": "task",
    "workflows": "workflow", "checklists": "checklist", "templates": "template",
    "reference": "reference", "swipe": "swipe", "swipe-sources": "swipe-source",
    "voice": "voice", "phrases": "phrases", "authority": "authority",
    "projects": "project", "archive": "archive", "data": "data", "docs": "doc",
    "lib": "lib",
}
# Subdiretórios cujo 2º segmento colapsa para um tipo singular.
SUBDIR_SINGULAR = {
    ("lib", "components"): "component",
    ("lib", "patterns"): "pattern",
    ("lib", "utilities"): "utility",
    ("data", "registries"): "registry",
    ("voice", "profiles"): "profile",
    ("reference", "swipe-breakdowns"): "swipe-breakdown",
    ("reference", "case-studies"): "case",
    ("reference", "industries"): "industry",
}


def derive_id(relpath: str) -> str:
    """Deriva o id determinístico a partir do path relativo (ARCHITECTURE §5.2)."""
    rel = relpath.replace(os.sep, "/")
    parts = rel.split("/")
    parts[-1] = os.path.splitext(parts[-1])[0]  # tira .md do filename
    if parts[-1].lower() == "readme":
        parts[-1] = "readme"
    top = parts[0]
    # templates: o sufixo "-template" é redundante no id (o type já é 'template').
    if top == "templates" and parts[-1].endswith("-template"):
        parts[-1] = parts[-1][: -len("-template")]
    # Caso especial: lib/taxonomies/X -> taxonomy.X (descarta o prefixo lib).
    if len(parts) >= 2 and (top, parts[1]) == ("lib", "taxonomies"):
        return ".".join(["taxonomy"] + parts[2:])
    # Caso especial: reference/books/<tema>/X -> reference.book.X (colapsa o tema).
    if top == "reference" and len(parts) >= 2 and parts[1] == "books":
        return ".".join(["reference", "book", parts[-1]])
    out = [PREFIX_MAP.get(top, top)]
    if len(parts) >= 2 and (top, parts[1]) in SUBDIR_SINGULAR:
        out.append(SUBDIR_SINGULAR[(top, parts[1])])
        out.extend(parts[2:])
    else:
        out.extend(parts[1:])
    return ".".join(out)


def iter_md(target_dir: str):
    for dp, dns, fns in os.walk(target_dir):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if fn.endswith(".md"):
                yield os.path.join(dp, fn)


def read_frontmatter(path: str) -> dict | None:
    text = open(path, encoding="utf-8").read()
    m = FM_RE.match(text)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def main():
    ap = argparse.ArgumentParser(description="Valida a bijeção id<->path dos .md.")
    ap.add_argument("--dir", default=".", help="subdiretório a validar (default: repo)")
    ap.add_argument("--check", action="store_true", help="dry-run read-only (não escreve json)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    target = os.path.normpath(os.path.join(ROOT, a.dir))
    if not os.path.isdir(target):
        print(f"ERRO: diretório inexistente: {a.dir}"); sys.exit(2)

    id_to_path: dict[str, str] = {}     # id declarado -> path (checa unicidade)
    collisions, missing_id, mismatch, no_fm = [], [], [], []
    mapped = 0

    for p in sorted(iter_md(target)):
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        fname = os.path.basename(p)
        fm = read_frontmatter(p)
        if fm is None:
            if fname in NO_FRONTMATTER_OK:
                continue
            no_fm.append(rel)
            continue
        declared = str(fm.get("id", "")).strip()
        expected = derive_id(rel)
        if not declared:
            missing_id.append(rel)
            continue
        mapped += 1
        # 1) unicidade (id->path é injetivo)
        if declared in id_to_path and id_to_path[declared] != rel:
            collisions.append((declared, id_to_path[declared], rel))
        else:
            id_to_path.setdefault(declared, rel)
        # 2) consistência (id declarado == id derivado do path)
        if declared != expected:
            mismatch.append((rel, declared, expected))

    n_err = len(collisions) + len(missing_id) + len(mismatch) + len(no_fm)
    print("\n=== ID-RESOLVER — bijeção id<->path ===")
    print(f"diretório: {a.dir} · arquivos mapeados: {mapped} · ids únicos: {len(id_to_path)}")
    print(f"colisões: {len(collisions)} · sem id: {len(missing_id)} · "
          f"inconsistentes: {len(mismatch)} · sem frontmatter: {len(no_fm)}")

    if not a.quiet:
        for fid, a_, b_ in collisions:
            print(f"  ✗ COLISÃO id {fid!r}: {a_}  <->  {b_}")
        for rel in missing_id:
            print(f"  ✗ SEM ID: {rel}")
        for rel, declared, expected in mismatch:
            print(f"  ✗ INCONSISTENTE: {rel} declara {declared!r} (esperado {expected!r})")
        for rel in no_fm:
            print(f"  ✗ SEM FRONTMATTER: {rel}")

    if not a.check:
        json.dump(
            {"dir": a.dir, "mapped": mapped, "unique_ids": len(id_to_path),
             "collisions": collisions, "missing_id": missing_id,
             "mismatch": mismatch, "no_frontmatter": no_fm,
             "map": id_to_path},
            open(os.path.join(ROOT, ".id-resolver.json"), "w"),
            ensure_ascii=False, indent=1)

    ok = n_err == 0
    print(f"\nRESULTADO: {'BIJEÇÃO OK ✅' if ok else 'FALHA ❌'} "
          f"({mapped} ids, {n_err} problema(s))\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
