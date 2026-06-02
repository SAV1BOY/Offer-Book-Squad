#!/usr/bin/env bash
# install-hooks.sh — ativa os git hooks versionados do Offer Book Squad.
# Uso: bash scripts/install-hooks.sh
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT" || exit 1
chmod +x scripts/hooks/* 2>/dev/null || true
git config core.hooksPath scripts/hooks
echo "✅ hooks instalados — core.hooksPath = scripts/hooks"
echo "   pre-commit: regenera traceability/backlog + qa-runner --strict + crosslink + id + citation"
echo "   (para desativar: git config --unset core.hooksPath)"
