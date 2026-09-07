#!/usr/bin/env python3
"""
Fetches the current list of live visitors from the whos.amung.us Pro API
and writes a trimmed, public-safe JSON file that the static site can fetch
directly (no API key exposed to the browser).
"""
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

API_KEY = os.environ.get("WHOS_API_KEY")
SITEKEY = os.environ.get("WHOS_SITEKEY", "onj9u")
OUT_PATH = sys.argv[1] if len(sys.argv) > 1 else "data/readers.json"
MAX_ROWS = 40

if not API_KEY:
    print("ERROR: WHOS_API_KEY env var is not set", file=sys.stderr)
    sys.exit(1)

url = f"https://whos.amung.us/api/v1/{SITEKEY}/stats?list=recent"
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {API_KEY}"})

try:
    with urllib.request.urlopen(req, timeout=20) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print(f"ERROR: whos.amung.us API returned HTTP {e.code}: {e.read()[:500]}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"ERROR: request failed: {e}", file=sys.stderr)
    sys.exit(1)

data = payload.get("data", {})
pages = data.get(SITEKEY, {}).get("pages", []) if SITEKEY in data else data.get("pages", [])

rows = []
for p in pages[:MAX_ROWS]:
    rows.append({
        "country": p.get("country") or "",
        "country_code": (p.get("country_code") or "").upper(),
        "city": p.get("city") or "",
        "referrer": p.get("referrer") or "",
        "ref_class": p.get("ref_class") or "",
        "desktop": bool(p.get("desktop")),
        "os": p.get("os") or "",
        "browser": p.get("browser") or "",
    })

out = {
    "count": len(pages),
    "fetched_at": datetime.now(timezone.utc).isoformat(),
    "rows": rows,
}

os.makedirs(os.path.dirname(OUT_PATH) or ".", exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=0)

print(f"Wrote {len(rows)} rows to {OUT_PATH}")
