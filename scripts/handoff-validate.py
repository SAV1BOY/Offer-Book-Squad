#!/usr/bin/env python3
"""
handoff-validate.py — valida um handoff cross-squad contra o contrato

PART OF: Offer Book Squad / scripts
OWNER_AGENT: offer-squad-architect
CONSUMES: um arquivo de handoff (data/handoffs/*.md) com a seção "## Campos do contrato"
PRODUCES: veredito no stdout (campos completos? aceite possível?)
USAGE:
  python scripts/handoff-validate.py data/handoffs/example-deepresearch-to-offerbook.md
  python scripts/handoff-validate.py <file> --check    # não falha exit (dry-run)
DEPENDS: stdlib
EXIT: 0 contrato completo · 1 campo(s) ausente(s)/vazio(s) · 2 uso
"""
from __future__ import annotations
import argparse, os, re, sys

REQUIRED = [
    "de_squad", "para_squad", "artefato", "campos_esperados",
    "qualidade_minima_por_campo", "dono", "criterio_de_aceite",
    "return_on_reject", "registry_entry",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", help="arquivo de handoff (.md)")
    ap.add_argument("--check", action="store_true", help="dry-run (não falha exit)")
    a = ap.parse_args()

    if not os.path.exists(a.file):
        print(f"ERRO: arquivo inexistente: {a.file}"); sys.exit(2)
    text = open(a.file, encoding="utf-8").read()

    print(f"\n=== HANDOFF-VALIDATE — {os.path.basename(a.file)} ===")
    missing, empty = [], []
    for field in REQUIRED:
        # procura "- **field:** valor" (ou "**field:**")
        m = re.search(rf"\*\*{re.escape(field)}\s*:\*\*\s*(.*)", text)
        if not m:
            missing.append(field)
            print(f"  ✗ {field}: AUSENTE")
        elif not m.group(1).strip() or m.group(1).strip() in ("_(preencher)_", "TBD", "—"):
            empty.append(field)
            print(f"  ⚠ {field}: VAZIO")
        else:
            print(f"  ✓ {field}")

    problems = missing + empty
    ok = not problems
    print(f"\nVEREDITO: {'CONTRATO COMPLETO ✅ (pronto p/ aceite)' if ok else 'INCOMPLETO ❌ — ' + ', '.join(problems)}")
    print("(o aceite editorial ainda passa por checklists/cross-squad/cross-squad-asset-validation.)\n")
    sys.exit(0 if (ok or a.check) else 1)


if __name__ == "__main__":
    main()
