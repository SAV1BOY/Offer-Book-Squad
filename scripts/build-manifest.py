#!/usr/bin/env python3
"""
build-manifest.py — emite um manifesto do build (contagem por diretório + ids)

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: a árvore de arquivos do repo (.md/.csv/.py/.yaml) + frontmatter `id`/`type`
PRODUCES: relatório no stdout + .build-manifest.json (na raiz; em .gitignore)
USAGE:
  python scripts/build-manifest.py            # manifesto do repo
  python scripts/build-manifest.py --dir agents
  python scripts/build-manifest.py --check    # dry-run read-only (não escreve json)
DEPENDS: stdlib (+ pyyaml p/ ler frontmatter)
EXIT: 0 sempre (informativo) · 2 erro de uso
"""
from __future__ import annotations
import argparse, datetime, json, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário (pip install pyyaml)"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env"}
EXTS = (".md", ".csv", ".py", ".yaml")
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def read_fm(path: str) -> dict:
    try:
        text = open(path, encoding="utf-8").read()
    except Exception:
        return {}
    m = FM_RE.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def iter_files(target_dir: str):
    for dp, dns, fns in os.walk(target_dir):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if fn.endswith(EXTS):
                yield os.path.join(dp, fn)


def top_dir(rel: str) -> str:
    parts = rel.split("/")
    return parts[0] if len(parts) > 1 else "(root)"


def main():
    ap = argparse.ArgumentParser(description="Emite um manifesto do build (contagem por dir + ids).")
    ap.add_argument("--dir", default=".", help="subdiretório (default: repo)")
    ap.add_argument("--check", action="store_true", help="dry-run read-only (não escreve json)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    target = os.path.normpath(os.path.join(ROOT, a.dir))
    if not os.path.isdir(target):
        print(f"ERRO: diretório inexistente: {a.dir}"); sys.exit(2)

    by_dir: dict[str, dict] = {}
    by_type: dict[str, int] = {}
    ids: list[dict] = []
    total = 0

    for p in sorted(iter_files(target)):
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        ext = os.path.splitext(rel)[1]
        td = top_dir(rel)
        d = by_dir.setdefault(td, {"files": 0, "by_ext": {}})
        d["files"] += 1
        d["by_ext"][ext] = d["by_ext"].get(ext, 0) + 1
        total += 1
        if ext == ".md":
            fm = read_fm(p)
            fid = str(fm.get("id", "")).strip()
            ftype = fm.get("type")
            if fid:
                ids.append({"id": fid, "path": rel, "type": ftype})
            if ftype:
                by_type[str(ftype)] = by_type.get(str(ftype), 0) + 1

    seen, dups = set(), []
    for e in ids:
        if e["id"] in seen:
            dups.append(e["id"])
        seen.add(e["id"])

    manifest = {
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "dir": a.dir,
        "total_files": total,
        "unique_ids": len(seen),
        "duplicate_ids": sorted(set(dups)),
        "by_dir": {k: by_dir[k] for k in sorted(by_dir)},
        "by_type": dict(sorted(by_type.items())),
        "ids": sorted(ids, key=lambda e: e["id"]),
    }

    label = f" — {a.dir}" if a.dir != "." else ""
    print(f"\n=== BUILD-MANIFEST{label} ===")
    print(f"arquivos: {total} · ids únicos: {len(seen)} · ids duplicados: {len(set(dups))}")
    if not a.quiet:
        print(f"\n{'dir':<18}{'arquivos':>9}")
        for k in sorted(by_dir):
            print(f"{k:<18}{by_dir[k]['files']:>9}")
        if by_type:
            print("\npor type (md):")
            for t, c in sorted(by_type.items()):
                print(f"  {t:<16}{c:>5}")
        if dups:
            print("\n  ⚠ ids duplicados:")
            for d in sorted(set(dups)):
                print(f"    {d}")

    if not a.check:
        json.dump(manifest, open(os.path.join(ROOT, ".build-manifest.json"), "w"),
                  ensure_ascii=False, indent=1)
        print(f"\nescrito: .build-manifest.json")

    print("\nRESULTADO: MANIFESTO OK ✅\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
