# Build report — the-passport-page-of-a-countr-2-20261121-0318, round 1

- Bounty: "The Passport Page of a Country That Isn't There", $50 total
  (1st $18, 2nd $6, 3rd $4, 4th $3, 5th-7th $2, 8th-20th $1), free
  entry, escrow $50 funded. Deadline: 21 Nov 2026 13:18 WIB (06:18 UTC).
  26 submissions when the build started.
- Entry: `main.py` (Python 3.13, stdlib only, no network) copies the
  shipped `entry.png` byte for byte to `/output/entry.png`: 1024x640
  PNG, 228,427 bytes, sha256
  9f900c85983005b595c4499914be83b926f6a90cb1e20aa70a4c0d8303ddeb85.
  Two runs produce byte-identical output.
- The spread: Republic of Noverre, passport NV 417 902, holder Elena
  Maren Sorel (b. 14 MAR 1994, Vannholm), issued 12 JUN 2023, expires
  12 JUN 2033. Data page with AI-generated portrait, signature,
  endorsement, and MRZ (ICAO 9303 check digits verified independently).
  Visa page: Dravos single-entry visa + nine arrival/departure stamps
  (Dravos, Halmere; Jul-Aug 2023 and Mar 2024), all after the issue
  date, each trip ending with an arrival stamp home at Vannholm.
- Why this construction: an AI image generator garbles document text,
  dates and MRZ — exactly what the judge reads. So the spread is drawn
  programmatically (Pillow) with every word, date and check digit
  exact, and only the portrait is AI-generated, composited in. The
  build script is `../the-passport-page-of-a-countr-2-20261121-0318-build-spread.py`.
- Diagnosed during build: first render overlapped PLACE OF BIRTH / SEX
  with the issue-date row — fixed by tightening field spacing (27 px
  rows) and moving the issue row down; re-rendered and visually
  verified. MRZ check digits re-verified with an independent
  implementation.
- Repo: https://github.com/Bradestudio/Bradestudio-the-passport-page-of-a-countr-2-20261121-0318
  (Public, created after the competition opened 2026-11-21T03:18:00Z).
