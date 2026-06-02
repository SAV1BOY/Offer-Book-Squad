#!/usr/bin/env python3
"""
link-utm-builder.py — gera vanity URLs + UTM por CTA a partir de um input

PART OF: Offer Book Squad / scripts
OWNER_AGENT: tech-links-deliverability-engineer
CONSUMES: lista de CTAs (YAML/JSON; --in) OU CTAs avulsos via --cta; base_url + campanha
PRODUCES: CSV (cta,vanity,full_url,utm_source,utm_medium,utm_campaign,utm_content) no stdout/--out
USAGE:
  python scripts/link-utm-builder.py --base https://x.co --campaign black-friday --in ctas.yaml
  python scripts/link-utm-builder.py --base https://x.co --campaign bf --cta "Comprar Agora:email:e5"
  python scripts/link-utm-builder.py --base https://x.co --campaign bf --cta "Comprar:email:e5" --check
DEPENDS: stdlib (csv, urllib) + pyyaml (só se --in for .yaml)
EXIT: 0 ok · 1 falha (input/base inválida, saída já existe) · 2 erro de uso
"""
from __future__ import annotations
import argparse, csv, io, json, os, re, sys
from urllib.parse import urlencode, urlsplit, urlunsplit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADER = ["cta", "vanity", "full_url", "utm_source", "utm_medium",
          "utm_campaign", "utm_content"]
SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = (s.replace("á", "a").replace("ã", "a").replace("â", "a").replace("à", "a")
          .replace("é", "e").replace("ê", "e").replace("í", "i")
          .replace("ó", "o").replace("ô", "o").replace("õ", "o")
          .replace("ú", "u").replace("ç", "c"))
    return SLUG_RE.sub("-", s).strip("-") or "cta"


def valid_base(url: str) -> bool:
    p = urlsplit(url)
    return p.scheme in ("http", "https") and bool(p.netloc)


def load_ctas(path: str) -> list[dict]:
    raw = open(path, encoding="utf-8").read()
    if path.endswith((".yaml", ".yml")):
        try:
            import yaml
        except Exception:
            print("ERRO: pyyaml necessário para --in .yaml"); sys.exit(2)
        data = yaml.safe_load(raw) or {}
    elif path.endswith(".json"):
        data = json.loads(raw)
    else:
        print(f"ERRO: --in deve ser .yaml/.yml/.json (recebi {path!r})"); sys.exit(2)
    items = data.get("ctas", data) if isinstance(data, dict) else data
    out = []
    for it in items or []:
        if isinstance(it, str):
            out.append(parse_cta_string(it))
        elif isinstance(it, dict):
            out.append({"label": it.get("label", it.get("cta", "CTA")),
                        "source": it.get("source", "site"),
                        "medium": it.get("medium", "cpc"),
                        "content": it.get("content", "")})
    return out


def parse_cta_string(s: str) -> dict:
    """Formato curto: 'Label:source:content' (medium opcional como 4º campo)."""
    parts = [p.strip() for p in s.split(":")]
    label = parts[0] if parts else "CTA"
    source = parts[1] if len(parts) > 1 and parts[1] else "site"
    content = parts[2] if len(parts) > 2 else ""
    medium = parts[3] if len(parts) > 3 else ("email" if source == "email" else "cpc")
    return {"label": label, "source": source, "medium": medium, "content": content}


def build_row(cta: dict, base: str, campaign: str) -> dict:
    label = cta.get("label", "CTA")
    source = cta.get("source", "site")
    medium = cta.get("medium", "cpc")
    content = cta.get("content") or slugify(label)
    vanity_slug = slugify(label)
    vanity = base.rstrip("/") + "/" + vanity_slug
    params = {"utm_source": source, "utm_medium": medium,
              "utm_campaign": campaign, "utm_content": content}
    p = urlsplit(vanity)
    full = urlunsplit((p.scheme, p.netloc, p.path, urlencode(params), ""))
    return {"cta": label, "vanity": vanity, "full_url": full,
            "utm_source": source, "utm_medium": medium,
            "utm_campaign": campaign, "utm_content": content}


def write_csv(rows: list[dict], stream) -> None:
    w = csv.DictWriter(stream, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    for r in rows:
        w.writerow(r)


def main():
    ap = argparse.ArgumentParser(description="Gera vanity URLs + UTM por CTA.")
    ap.add_argument("--base", required=True, help="base URL (https://dominio)")
    ap.add_argument("--campaign", required=True, help="utm_campaign (slug do lançamento)")
    ap.add_argument("--in", dest="infile", default="", help="lista de CTAs (.yaml/.json)")
    ap.add_argument("--cta", action="append", default=[], help="CTA avulso 'Label:source:content[:medium]' (repetível)")
    ap.add_argument("--out", default="", help="CSV de saída (default: stdout)")
    ap.add_argument("--check", action="store_true", help="dry-run read-only: imprime no stdout, não escreve")
    ap.add_argument("--force", action="store_true", help="sobrescreve --out se existir")
    a = ap.parse_args()

    if not valid_base(a.base):
        print(f"ERRO: --base inválida (esperado http(s)://dominio): {a.base!r}"); sys.exit(2)
    campaign = slugify(a.campaign)

    ctas: list[dict] = []
    if a.infile:
        path = a.infile if os.path.isabs(a.infile) else os.path.join(ROOT, a.infile)
        if not os.path.exists(path):
            print(f"ERRO: --in inexistente: {a.infile}"); sys.exit(1)
        ctas.extend(load_ctas(path))
    ctas.extend(parse_cta_string(s) for s in a.cta)

    if not ctas:
        # default mínimo demonstrativo (mantém --check rodando sem input)
        ctas = [parse_cta_string("Comprar Agora:email:cta-principal"),
                parse_cta_string("Quero Saber Mais:site:cta-secundario:organic")]

    rows = [build_row(c, a.base, campaign) for c in ctas]

    print("\n=== LINK-UTM-BUILDER ===")
    print(f"base: {a.base} · campanha: {campaign} · CTAs: {len(rows)}")
    if not rows:
        print("  (nenhum CTA)")

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
