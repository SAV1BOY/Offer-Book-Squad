#!/usr/bin/env python3
"""
blackbook-assembler.py — consolida os artefatos do Blackbook num índice/sumário

PART OF: Offer Book Squad / scripts
OWNER_AGENT: knowledge-librarian
CONSUMES: templates/core/launch-blackbook-skeleton.md, checklists/blackbook-stack/*, e os artefatos por domínio do build (--src; default: repo)
PRODUCES: sumário markdown no stdout + --out opcional (índice consolidado do Blackbook)
USAGE:
  python scripts/blackbook-assembler.py                 # sumário no stdout
  python scripts/blackbook-assembler.py --out data/blackbook-index.md
  python scripts/blackbook-assembler.py --check         # dry-run read-only (não escreve)
DEPENDS: stdlib (+ pyyaml p/ ler frontmatter)
EXIT: 0 ok · 1 falha (skeleton/gates ausentes, ou --out existe sem --force) · 2 erro de uso
"""
from __future__ import annotations
import argparse, os, re, sys

try:
    import yaml
except Exception:
    print("ERRO: pyyaml necessário (pip install pyyaml)"); sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env"}
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

SKELETON = "templates/core/launch-blackbook-skeleton.md"
GATES_DIR = "checklists/blackbook-stack"

# Seções do Blackbook -> dirs que alimentam cada uma (por domínio do pipeline D0–D7).
SECTIONS = [
    ("Estratégia & Offer Book", ["templates/strategy", "templates/offer", "templates/core"]),
    ("Copy & Criativo", ["templates/copy"]),
    ("Funil & Tech", ["templates/funnel-tech"]),
    ("Ops & Eventos", ["templates/ops"]),
    ("Growth, Afiliados & PR", ["templates/growth"]),
    ("QA & Compliance", ["templates/qa"]),
    ("Memória (Registries)", ["data/registries"]),
]


def read_fm(path: str) -> dict:
    text = open(path, encoding="utf-8").read()
    m = FM_RE.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def list_md(rel_dir: str):
    absd = os.path.join(ROOT, rel_dir)
    if not os.path.isdir(absd):
        return []
    out = []
    for fn in sorted(os.listdir(absd)):
        if fn.endswith(".md"):
            rel = os.path.join(rel_dir, fn).replace(os.sep, "/")
            out.append(rel)
    return out


def main():
    ap = argparse.ArgumentParser(description="Consolida os artefatos do Blackbook num índice/sumário.")
    ap.add_argument("--out", default="", help="path do índice markdown (default: stdout)")
    ap.add_argument("--check", action="store_true", help="dry-run read-only (não escreve)")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--force", action="store_true", help="sobrescreve --out se existir")
    a = ap.parse_args()

    skeleton_abs = os.path.join(ROOT, SKELETON)
    gates = list_md(GATES_DIR)
    missing = []
    if not os.path.exists(skeleton_abs):
        missing.append(SKELETON)
    if not gates:
        missing.append(GATES_DIR + "/* (nenhum gate)")

    section_files, total = [], 0
    for name, dirs in SECTIONS:
        files = []
        for d in dirs:
            files.extend(list_md(d))
        total += len(files)
        section_files.append((name, files))

    # monta o sumário markdown
    sk_fm = read_fm(skeleton_abs) if os.path.exists(skeleton_abs) else {}
    lines = [
        "# Launch Blackbook — Índice Consolidado",
        "",
        "> Gerado por `scripts/blackbook-assembler.py`. Consolida o esqueleto, "
        "os gates de DoD e os artefatos por domínio do build.",
        "",
        f"- **Esqueleto:** [`{SKELETON}`](../{SKELETON})"
        + (f" — *{sk_fm.get('title')}*" if sk_fm.get("title") else ""),
        f"- **Gates de fechamento (blackbook-stack):** {len(gates)}",
        f"- **Artefatos consolidados:** {total}",
        "",
        "## Gates de Definition of Done",
    ]
    for g in gates:
        fm = read_fm(os.path.join(ROOT, g))
        lines.append(f"- [`{os.path.basename(g)}`](../{g})" + (f" — {fm.get('title')}" if fm.get("title") else ""))
    lines.append("")
    lines.append("## Seções do Blackbook")
    for name, files in section_files:
        lines.append(f"\n### {name} ({len(files)})")
        if not files:
            lines.append("- _(pendente — nenhum artefato neste domínio ainda)_")
        for f in files:
            fm = read_fm(os.path.join(ROOT, f))
            title = fm.get("title", os.path.basename(f))
            lines.append(f"- [`{os.path.basename(f)}`](../{f}) — {title}")
    summary = "\n".join(lines).rstrip() + "\n"

    print("\n=== BLACKBOOK-ASSEMBLER ===")
    print(f"esqueleto: {'ok' if os.path.exists(skeleton_abs) else 'AUSENTE'} · "
          f"gates: {len(gates)} · artefatos: {total}")
    if not a.quiet:
        for name, files in section_files:
            print(f"  • {name}: {len(files)}")
        for mp in missing:
            print(f"  ✗ ausente: {mp}")

    if missing:
        print("\nRESULTADO: FALHA ❌ (fontes do Blackbook ausentes)\n")
        sys.exit(1)

    if a.check or not a.out:
        if a.check:
            print("\n[--check] sumário gerado em memória (nada escrito):")
        print("\n--- ÍNDICE ---")
        sys.stdout.write(summary)
        print("\nRESULTADO: " + ("DRY-RUN OK ✅" if a.check else "OK ✅") + "\n")
        sys.exit(0)

    out_path = a.out if os.path.isabs(a.out) else os.path.join(ROOT, a.out)
    if os.path.exists(out_path) and not a.force:
        print(f"  ✗ já existe: {a.out} (use --force)")
        print("\nRESULTADO: NÃO ESCRITO ❌\n")
        sys.exit(1)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"  ✓ índice escrito: {a.out}")
    print("\nRESULTADO: CONSOLIDADO ✅\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
