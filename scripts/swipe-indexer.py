#!/usr/bin/env python3
"""
swipe-indexer.py — indexa swipe/ e regenera a tabela do swipe-registry

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: swipe.config + frontmatter dos .md em swipe/ e reference/swipe-breakdowns/
PRODUCES: atualiza a tabela sob "## Registros" em data/registries/swipe-registry.md
USAGE:
  python scripts/swipe-indexer.py            # regenera a tabela do registry
  python scripts/swipe-indexer.py --check    # dry-run read-only: só reporta (não escreve)
DEPENDS: stdlib (+ pyyaml)
EXIT: 0 ok · 1 falha (config/registry ausente, ou entrada inválida no swipe) · 2 erro de uso
"""
from __future__ import annotations
import argparse, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário (pip install pyyaml)"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env"}
SWIPE_CONFIG = os.path.join(ROOT, "swipe.config")
DEFAULT_REGISTRY = "data/registries/swipe-registry.md"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
COLUMNS = ["swipe_id", "title", "swipe_type", "category", "pattern_name",
           "principle", "sophistication_fit", "source_ref", "path",
           "reuse_count", "status", "owner_agent", "updated"]
GEN_NOTE = ("<!-- Tabela GERADA por scripts/swipe-indexer.py — não editar à mão. "
            "Rode `python scripts/swipe-indexer.py` (--check = dry-run). -->")


def read_config() -> dict:
    if not os.path.exists(SWIPE_CONFIG):
        print(f"ERRO: swipe.config não encontrado em {SWIPE_CONFIG}"); sys.exit(1)
    return yaml.safe_load(open(SWIPE_CONFIG, encoding="utf-8").read()) or {}


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


def category_from_path(rel: str, cat_dirs: dict[str, str]) -> str:
    for cat_id, d in cat_dirs.items():
        d = d.rstrip("/") + "/"
        if rel.startswith(d):
            return cat_id
    if rel.startswith("reference/swipe-breakdowns/"):
        return "swipe-breakdown"
    return "-"


def md_cell(val) -> str:
    if val is None:
        return "-"
    if isinstance(val, (list, tuple)):
        val = "; ".join(str(x) for x in val)
    return str(val).replace("|", r"\|").replace("\n", " ").strip() or "-"


def build_rows(cfg: dict) -> tuple[list[list[str]], list[str]]:
    cats = cfg.get("categories", []) or []
    cat_dirs = {c.get("id"): c.get("dir", "") for c in cats if isinstance(c, dict)}

    scan_dirs = list(cat_dirs.values()) + ["reference/swipe-breakdowns"]
    rows, problems, seen = [], [], set()
    for d in scan_dirs:
        absd = os.path.join(ROOT, d)
        if not os.path.isdir(absd):
            continue
        for p in sorted(iter_md(absd)):
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            if rel in seen:
                continue
            seen.add(rel)
            if os.path.basename(rel) == "index.md":
                continue  # índices de categoria não entram como linhas
            fm = read_frontmatter(p)
            if fm is None:
                problems.append(f"{rel}: sem frontmatter")
                continue
            sid = str(fm.get("id", "")).strip()
            if not sid:
                problems.append(f"{rel}: sem id no frontmatter")
                continue
            srcs = fm.get("sources")
            row = {
                "swipe_id": f"`{sid}`",
                "title": fm.get("title", "-"),
                "swipe_type": fm.get("type", "swipe"),
                "category": category_from_path(rel, cat_dirs),
                "pattern_name": (fm.get("tags") or ["-"])[0] if fm.get("tags") else "-",
                "principle": (fm.get("frameworks") or ["-"])[0] if fm.get("frameworks") else "-",
                "sophistication_fit": fm.get("sophistication_fit", "-"),
                "source_ref": (srcs[0] if isinstance(srcs, list) and srcs else (srcs or "-")),
                "path": f"`{rel}`",
                "reuse_count": fm.get("reuse_count", 0),
                "status": "indexed",
                "owner_agent": fm.get("owner_agent", "knowledge-librarian"),
                "updated": fm.get("updated", "-"),
            }
            rows.append([md_cell(row[c]) for c in COLUMNS])
    return rows, problems


def render_table(rows: list[list[str]]) -> str:
    header = "| " + " | ".join(COLUMNS) + " |"
    sep = "|" + "|".join(["---"] * len(COLUMNS)) + "|"
    body = "\n".join("| " + " | ".join(r) + " |" for r in rows) if rows else \
        "| " + " | ".join(["-"] * len(COLUMNS)) + " |"
    return "\n".join([header, sep, body, "", GEN_NOTE]) + "\n"


def splice_registry(text: str, table_block: str) -> str:
    """Substitui tudo depois de '## Registros' pela tabela gerada, mantendo o resto."""
    m = re.search(r"(^##\s+Registros\s*\n)", text, re.MULTILINE)
    if not m:
        raise ValueError("registry sem seção '## Registros'")
    head = text[:m.end()]
    return head + "\n" + table_block


def main():
    ap = argparse.ArgumentParser(description="Indexa swipe/ e regenera a tabela do swipe-registry.")
    ap.add_argument("--check", action="store_true", help="dry-run read-only: só reporta, não escreve")
    ap.add_argument("--registry", default=DEFAULT_REGISTRY, help="path do registry (default do swipe.config)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    cfg = read_config()
    reg_rel = cfg.get("index_output", a.registry) or a.registry
    reg_abs = os.path.normpath(os.path.join(ROOT, reg_rel))

    rows, problems = build_rows(cfg)
    table_block = render_table(rows)

    print("\n=== SWIPE-INDEXER ===")
    print(f"registry: {reg_rel} · entradas indexadas: {len(rows)} · problemas: {len(problems)}")
    if not a.quiet:
        for prob in problems[:40]:
            print(f"  ✗ {prob}")
        for r in rows[:8]:
            print(f"  • {r[0]}  [{r[3]}]")
        if len(rows) > 8:
            print(f"  … (+{len(rows) - 8} entrada(s))")

    if not os.path.exists(reg_abs):
        print(f"  ✗ registry inexistente: {reg_rel}")
        print("\nRESULTADO: FALHA ❌\n")
        sys.exit(1)

    if a.check:
        print(f"\n[--check] {len(rows)} entrada(s) seriam escritas em {reg_rel} (nada gravado).")
        ok = not problems
        print(f"RESULTADO: {'DRY-RUN OK ✅' if ok else 'DRY-RUN COM PROBLEMAS ❌'}\n")
        sys.exit(0 if ok else 1)

    try:
        new_text = splice_registry(open(reg_abs, encoding="utf-8").read(), table_block)
    except ValueError as e:
        print(f"  ✗ {e}")
        print("\nRESULTADO: FALHA ❌\n")
        sys.exit(1)
    with open(reg_abs, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"  ✓ tabela regenerada com {len(rows)} entrada(s).")

    ok = not problems
    print(f"\nRESULTADO: {'ÍNDICE ATUALIZADO ✅' if ok else 'ATUALIZADO COM PROBLEMAS ❌'}\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
