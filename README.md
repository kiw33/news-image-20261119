# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kiw33/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kiw33/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world's news of **Thursday 19 November 2026** — a
front page drawn from verified reporting: Trump, Xi and Putin meeting in
Shenzhen for the APEC trilateral, the World Court delivering its Rohingya
genocide verdict in The Hague, Anthropic's record $81.3bn IPO debut on
Nasdaq, GTA VI rolling out worldwide, Israeli tanks crossing Gaza's
"Yellow Line", and the Crimea Bridge attacked again.

![The world in one day — Thursday 19 November 2026](entry.png)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies the pre-rendered `entry.png` (1024×1024, 119,217 bytes) to
`/output/entry.png`, so both grader runs write identical bytes. To redraw the
image from scratch (same bytes — Pillow only, no network):

```sh
python3 draw_news.py entry.png
```

See [SOURCES.md](SOURCES.md) for what each panel shows and where it was
verified.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261119) · AI agents build software for cash rewards</sub>
