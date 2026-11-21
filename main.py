#!/usr/bin/env python3
"""Entrypoint for the make.fun the-passport-page-of-a-countr-2-20261121-0318 entry.

Writes one invented passport spread to /output/entry.png: the open
passport of Elena Maren Sorel, citizen of the Republic of Noverre --
a country that does not exist. Stdlib only, no network, no clock,
no randomness: the program copies the entry image shipped in this
repository byte for byte, so every run writes the exact same bytes.

The spread (1024x640 PNG, 228,427 bytes):
- Left page: data page with portrait, fields, signature, endorsement
  and a machine-readable strip (MRZ, ICAO 9303 check digits verified).
  Passport NV 417 902, issued 12 JUN 2023 in Vannholm, expires
  12 JUN 2033. Holder born 14 MAR 1994 in Vannholm.
- Right page: a Kingdom of Dravos single-entry visa (28 JUL-27 AUG
  2023, fee 25 KRN paid) and nine arrival/departure stamps from
  Dravos and Halmere, every one dated after the passport's issue.
- The telling detail: the endorsement "VALID FOR TRAVEL BY SEA AND
  MOUNTAIN PASS ONLY. NOT VALID FOR AIR TRAVEL. FERRY LEVY 40 KRN
  PAID." -- Noverre has no airport; you arrive by ferry or on foot
  over the pass, which is what kind of place it is.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

ASSET = Path(__file__).resolve().parent / "entry.png"


def main():
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not dest and len(sys.argv) > 1:
        dest = sys.argv[1]
    if not dest:
        dest = "/output" if Path("/output").is_dir() else "output"
    outdir = Path(dest)
    outdir.mkdir(parents=True, exist_ok=True)
    target = outdir / "entry.png"
    shutil.copyfile(ASSET, target)
    data = target.read_bytes()
    print(f"wrote {target} ({len(data)} bytes, "
          f"sha256 {hashlib.sha256(data).hexdigest()})")


if __name__ == "__main__":
    main()
