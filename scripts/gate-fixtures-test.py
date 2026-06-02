#!/usr/bin/env python3
"""
gate-fixtures-test.py — testes NEGATIVOS: prova que os gates BLOQUEIAM artefatos ruins

PART OF: Offer Book Squad / scripts
OWNER_AGENT: offerbook-chief
CONSUMES: data/fixtures/* (artefatos propositalmente ruins) + os validadores
PRODUCES: veredito no stdout
USAGE: python scripts/gate-fixtures-test.py
DEPENDS: stdlib
EXIT: 0 todos os gates se comportaram (negativos falharam, positivo passou)
      1 regressão (algum gate deixou passar / bloqueou indevidamente) · 2 uso

Um gate só vale se BLOQUEIA. Aqui rodamos os validadores contra fixtures ruins e
exigimos falha (rc!=0); e contra um artefato bom e exigimos sucesso (rc==0).
"""
from __future__ import annotations
import os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable

# (nome, args, expect_fail) — expect_fail=True → esperamos rc!=0 (gate bloqueou)
CASES = [
    ("handoff-validate REJEITA contrato incompleto",
     ["scripts/handoff-validate.py", "data/fixtures/bad-handoff-incomplete.md"], True),
    ("compliance-scanner --strict PEGA escassez falsa em copy viva",
     ["scripts/compliance-scanner.py", "--strict", "--dir", "data/fixtures", "--quiet"], True),
    ("[controle +] handoff-validate ACEITA o contrato bom",
     ["scripts/handoff-validate.py", "data/handoffs/example-deepresearch-to-offerbook.md"], False),
]


def run(args) -> int:
    return subprocess.run([PY] + args, cwd=ROOT, capture_output=True, text=True).returncode


def main():
    if len(sys.argv) > 1 and sys.argv[1] not in ("--check",):
        print("uso: python scripts/gate-fixtures-test.py [--check]"); sys.exit(2)
    print("\n=== GATE FIXTURES — testes negativos (e 1 controle positivo) ===")
    good = 0
    for name, args, expect_fail in CASES:
        rc = run(args)
        behaved = (rc != 0) if expect_fail else (rc == 0)
        verb = ("bloqueou" if expect_fail else "aceitou") if behaved else "COMPORTAMENTO ERRADO"
        print(f"  {'✓' if behaved else '✗'} {name} — rc={rc} ({verb})")
        good += behaved
    allok = good == len(CASES)
    print(f"\nRESULTADO: {'OK ✅ — gates se comportaram (' + str(good) + '/' + str(len(CASES)) + ')' if allok else 'REGRESSÃO ❌ — um gate falhou em bloquear/aceitar'}\n")
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
