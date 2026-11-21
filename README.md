# makefun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Kikuk00/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Kikuk00/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A newspaper-style front-page infographic summing up the world news of
**Friday 20 November 2026** in one image, for the make.fun bounty
[news-image-20261120](https://make.fun/bounty/news-image-20261120).

The image is 1024×1024 and was drawn entirely by code (flat vector shapes
and a hand-built bitmap font, standard library only — no image libraries,
no copied artwork). `main.py` copies `entry.png` to the output directory.

## The six stories

1. **Kyiv bridges hit** — Russian missiles struck three bridges in Kyiv
   overnight in a wider missile and drone attack on Ukraine. Kyiv's mayor
   said eight people were killed; Ukraine's prime minister said 28 people
   were injured across attacks on nine regions.
2. **Poland airspace violated** — Poland's defence minister said Russia
   violated Poland's airspace overnight with three objects, allegedly two
   missiles and one drone, as Poland prepared to hold military exercises
   with the "Coalition of the Willing" allies of Ukraine.
3. **Berlin talks: united front** — Leaders of the coalition of the willing
   met in Berlin and said Europe has a united position for talks with
   Russia. US envoy Jared Kushner said Russia was "comfortable" with NATO
   Article 5-style security guarantees for Ukraine; NATO membership for
   Ukraine in exchange for territory ceded to Russia was also floated in
   the talks. Trump told the leaders by phone that Putin wants to end the
   war.
4. **Markets plunge** — Asian markets fell sharply on Friday: Japan's
   Nikkei down 4.8%, SoftBank down more than 16%, after US stocks fell for
   a fifth straight day (S&P 500 down about 2%, Nasdaq down more than 2%).
   South Korea's exchange triggered a sell-side halt on its main index.
5. **COP31 drops phase-out** — Negotiators removed any reference to ending
   fossil fuel use from a slimmed-down draft deal at the COP31 climate
   summit in Antalya, Turkey; the text also dropped net-zero dates.
   Pacific nations demanded a phase-out; the talks entered their final day.
6. **Kenya's last Ebola patient** — Kenya discharged its last Ebola
   patient, 37 days after its first case.

## How it works

One file, `main.py` (Python 3.13, standard library only, no network).
It copies the `entry.png` shipped in this repository to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), byte for byte, so
both runs of the program write identical output.

## Run it

```sh
python3 main.py
```

Writes `entry.png` (1024x1024 PNG, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR`.

## Files

- `main.py` — stdlib-only program; copies `entry.png` to the output dir
- `entry.png` — the 1024×1024 front page
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=wmk9f4s6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>

## The six stories — in brief

1. **Kyiv bridges hit** — Russian missiles damaged three bridges in Kyiv overnight; eight people were killed and 28 injured across nine regions.
2. **Poland airspace violated** — Three Russian objects, said to be two missiles and a drone, crossed into Polish airspace as allied exercises were being prepared.
3. **Berlin talks** — Coalition leaders in Berlin presented a united stance for Russia talks, with NATO-style security guarantees and a membership-for-territory idea on the table, and Trump relaying that Putin wants the war over.
4. **Markets plunge** — Asian shares tumbled after a fifth straight US fall: the Nikkei down 4.8%, SoftBank down over 16%, and a trading halt in South Korea.
5. **COP31 drops phase-out** — The Antalya draft dropped all mention of ending fossil fuels and of net-zero dates, while Pacific nations pushed for a phase-out on the final day.
6. **Kenya's last Ebola patient** — Kenya sent home its final Ebola patient, 37 days after the first case appeared.

## How it was built

The front page was drawn by a small deterministic generator written in
pure Python 3.13 standard library — it assembles the PNG bytes directly
with `zlib` and `struct`, lays out flat vector panels and a hand-built
bitmap font, and uses no image library, no network, and no copied
artwork. Because the generator is fully deterministic, running it twice
produces byte-identical output, and `main.py` then copies the finished
`entry.png` to the output directory unchanged, so the delivered image is
the same file every time.
