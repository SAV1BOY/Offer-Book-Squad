#!/usr/bin/env python3
"""
sequence-matrix-generator.py — gera a matriz de e-mail/SMS (CSV) a partir de um money model

PART OF: Offer Book Squad / scripts
OWNER_AGENT: email-sms-sequence-writer
CONSUMES: um money model simples (YAML/JSON; --in) OU defaults embutidos (carrinho aberto-fechado)
PRODUCES: CSV no schema de templates/copy/sequence-matrix-template.csv (header: titulo,timing,subject,canal,lista,gatilho)
USAGE:
  python scripts/sequence-matrix-generator.py --in money-model.yaml --out matrix.csv
  python scripts/sequence-matrix-generator.py --offer "Aprovado em Ingles" --cart-days 5
  python scripts/sequence-matrix-generator.py --check         # dry-run: imprime no stdout, não escreve
DEPENDS: stdlib (csv) + pyyaml (só se --in for .yaml)
EXIT: 0 ok · 1 falha (input inválido / saída já existe sem --force) · 2 erro de uso
"""
from __future__ import annotations
import argparse, csv, io, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADER = ["titulo", "timing", "subject", "canal", "lista", "gatilho"]

# Arco de sequência canônico (style-guide §4d exemplo): indireto -> direto, acelera no D0.
# Cada beat: (rótulo, offset_dia, hora, canal, lista, gatilho, template_subject)
ARC = [
    ("E1 Indoutrinacao Historia", -1, "09h", "email", "lista-quente", "inscricao-confirmada",
     "Por que {avatar} trava em {dor}"),
    ("E2 Conteudo-Prova", 0, "09h", "email", "lista-quente", "abriu-e1",
     "O metodo {mecanismo} em 1 pagina"),
    ("E3 Mecanismo + Prova", 0, "09h", "email", "lista-quente", "abriu-e2",
     "Como {prova} com {mecanismo}"),
    ("E4 Convite Transicao", 0, "09h", "email", "lista-quente", "nenhum",
     "Amanha abro {vagas} vagas do {offer}"),
    ("E5 Oferta Abre Carrinho", 0, "09h", "email", "lista-quente", "carrinho-aberto",
     "Vagas abertas: {offer}"),
    ("E6 Fechamento Manha", 0, "09h", "email", "clicou-e5-nao-comprou", "clicou-e5",
     "Fecha hoje as 23h59 — e por que sao so {vagas} vagas"),
    ("E7 Fechamento Ultimas Horas", 0, "20h", "sms", "clicou-e5-nao-comprou", "nao-comprou-ate-20h",
     "Ultimas horas (depois fecha de verdade)"),
]


def load_model(path: str) -> dict:
    raw = open(path, encoding="utf-8").read()
    if path.endswith((".yaml", ".yml")):
        try:
            import yaml
        except Exception:
            print("ERRO: pyyaml necessário para --in .yaml"); sys.exit(2)
        return yaml.safe_load(raw) or {}
    if path.endswith(".json"):
        return json.loads(raw)
    print(f"ERRO: --in deve ser .yaml/.yml/.json (recebi {path!r})"); sys.exit(2)


def schedule(n_beats: int, cart_days: int) -> list[str]:
    """Distribui os dias relativos: aquece de D-cart_days até D-1, fecha em D0 (manhã+noite)."""
    days = []
    # 7 beats canônicos -> [D-5, D-4, D-3, D-2, D-1, D0, D0] quando cart_days=5
    open_idx = 4  # E5 abre carrinho em D-1
    for i in range(n_beats):
        if i < open_idx:
            d = -(cart_days) + i
            d = min(d, -1)
            days.append(f"D{d}")
        elif i == open_idx:
            days.append("D-1")
        else:
            days.append("D0")
    return days


def fill(template: str, ctx: dict) -> str:
    out = template
    for k, v in ctx.items():
        out = out.replace("{" + k + "}", str(v))
    # remove placeholders não resolvidos
    while "{" in out and "}" in out:
        a = out.index("{"); b = out.index("}", a)
        out = out[:a] + out[b + 1:]
    return out.strip()


def build_rows(model: dict) -> list[dict]:
    ctx = {
        "offer": model.get("offer", "Sua Oferta"),
        "avatar": model.get("avatar", "seu cliente"),
        "dor": model.get("pain", "no momento decisivo"),
        "mecanismo": model.get("mechanism", "Mecanismo Unico"),
        "prova": model.get("proof", "um aluno teve resultado"),
        "vagas": model.get("seats", model.get("vagas", 40)),
    }
    cart_days = int(model.get("cart_days", 5))
    days = schedule(len(ARC), cart_days)
    rows = []
    for (label, _off, hour, canal, lista, gatilho, subj_t), day in zip(ARC, days):
        rows.append({
            "titulo": label,
            "timing": f"{day} {hour}",
            "subject": fill(subj_t, ctx),
            "canal": canal,
            "lista": lista,
            "gatilho": gatilho,
        })
    # passos extras de continuidade/upsell, se o money model os declarar
    for extra in (model.get("upsells") or []):
        rows.append({
            "titulo": f"U+ {extra}", "timing": "D+1 10h",
            "subject": fill("Proximo passo: {x}", {"x": extra}),
            "canal": "email", "lista": "compradores", "gatilho": "comprou-core",
        })
    return rows


def write_csv(rows: list[dict], stream) -> None:
    w = csv.DictWriter(stream, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    for r in rows:
        w.writerow(r)


def main():
    ap = argparse.ArgumentParser(description="Gera a matriz de sequência (CSV) de um money model.")
    ap.add_argument("--in", dest="infile", default="", help="money model (.yaml/.json) — opcional")
    ap.add_argument("--out", default="", help="path do CSV de saída (default: stdout)")
    ap.add_argument("--offer", default="", help="nome da oferta (override rápido sem --in)")
    ap.add_argument("--cart-days", type=int, default=None, help="dias de runway até o fechamento")
    ap.add_argument("--check", action="store_true", help="dry-run read-only: imprime no stdout, não escreve")
    ap.add_argument("--force", action="store_true", help="sobrescreve --out se existir")
    a = ap.parse_args()

    model: dict = {}
    if a.infile:
        path = a.infile if os.path.isabs(a.infile) else os.path.join(ROOT, a.infile)
        if not os.path.exists(path):
            print(f"ERRO: --in inexistente: {a.infile}"); sys.exit(1)
        model = load_model(path)
        if not isinstance(model, dict):
            print("ERRO: money model deve ser um mapa (chaves: offer, mechanism, seats, cart_days, …)")
            sys.exit(1)
    if a.offer:
        model["offer"] = a.offer
    if a.cart_days is not None:
        model["cart_days"] = a.cart_days

    rows = build_rows(model)

    print("\n=== SEQUENCE-MATRIX-GENERATOR ===")
    print(f"oferta: {model.get('offer', 'Sua Oferta')} · runway: D-{int(model.get('cart_days', 5))} → D0 · linhas: {len(rows)}")

    buf = io.StringIO()
    write_csv(rows, buf)
    csv_text = buf.getvalue()

    if a.check or not a.out:
        print("\n--- CSV " + ("(--check, nada escrito)" if a.check else "(stdout)") + " ---")
        sys.stdout.write(csv_text)
        print("\nRESULTADO: DRY-RUN OK ✅\n" if a.check else "\nRESULTADO: OK ✅\n")
        sys.exit(0)

    out_path = a.out if os.path.isabs(a.out) else os.path.join(ROOT, a.out)
    if os.path.exists(out_path) and not a.force:
        print(f"  ✗ já existe: {a.out} (use --force)")
        print("\nRESULTADO: NÃO ESCRITO ❌\n")
        sys.exit(1)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(csv_text)
    print(f"  ✓ escrito: {a.out}")
    print("\nRESULTADO: GERADO ✅\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
