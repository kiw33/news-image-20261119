# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kiw33/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kiw33/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world's news of Thursday 19 November 2026:
Trump, Xi and Putin meet at APEC in Shenzhen; the World Court rules on the
Rohingya genocide case; Anthropic debuts in the biggest IPO ever; GTA VI
rolls out worldwide; Israeli tanks cross Gaza's "Yellow Line"; and the
Crimean Bridge is attacked again — plus the day's other headlines in a
ticker. Drawn from scratch with Pillow, no network, fully deterministic.

## Run it

```sh
python3 main.py
```

This writes `entry.png` (1024 x 1024, under 1 MiB) in the repository root.
Run it twice and the bytes are identical. Sources for every fact in the
image are listed in `SOURCES.md`.

## What's inside

- `main.py` — entrypoint; renders and verifies `entry.png`.
- `draw_news.py` — all layout, text wrapping and pictograms (Pillow only).
- `SOURCES.md` — the 19 November 2026 reporting behind every panel.
- `entry.png` — the rendered front page.

---

<sub>Entered on [make.fun](https://make.fun/?ref=sc95sygb&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
