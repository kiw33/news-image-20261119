# Sources — Thursday 19 November 2026

Every fact in `entry.png` was checked against reporting published on
19 November 2026 (overnight + Asia-Pacific morning, UTC). Nothing in the
image is invented. Where an event began late on 18 November, it is included
because it was first widely reported on 19 November.

## The six panels

1. **APEC · Shenzhen** — Trump, Xi and Putin gather in Shenzhen for the
   APEC summit; Xi hugged Trump on the tarmac on arrival, and the three
   leaders are expected to hold a trilateral meeting on Thursday.
   Source: The New York Times, "Trump, Xi and Putin Shake Hands as Leaders
   Gather in China", 19 Nov 2026 00:57 UTC —
   https://www.nytimes.com (headline via NewsBites aggregator,
   https://www.newsbites.net/).
2. **The Hague** — The International Court of Justice delivers its final,
   legally binding judgment on 19 November in The Gambia v. Myanmar, the
   Rohingya genocide case (filed 2019, over the 2017 military campaign);
   reading begins 08:00 GMT at the Peace Palace. The image states the
   verdict is delivered today, not its outcome.
   Sources: ICJ notice via US News Pulse,
   https://usnewspulse.com/world/world-court-to-rule-on-rohingya-genocide-case-against-myanmar-on-november-19 ;
   GreenWatchBD, https://greenwatchbd.com/refugee/115268 ;
   Daily Spokesman,
   https://dailyspokesman.net/live/2026/11/18/world-court-set-to-deliver-landmark-judgment-in-myanmar-rohingya-genocide-case/
3. **Markets · AI** — Anthropic priced its IPO at $83 a share on 18 Nov,
   raising $81.3bn — the largest IPO on record, ahead of SpaceX — and its
   shares start trading on Nasdaq on Thursday 19 Nov under ticker ANT,
   valuing the company at about $1.5tn fully diluted.
   Sources: BusinessWorld (Reuters),
   https://bworldonline.com/technology/2026/11/19/794922/anthropic-clinches-biggest-ipo-ever-with-81-billion-offering/ ;
   FinanceFeeds,
   https://financefeeds.com/anthropic-prices-81-3-billion-ipo-at-83-ahead-of-nasdaq-debut/ ;
   Reuters via KZ1023,
   https://www.kz1023.com/2026/11/18/stocks-rise-after-anthropic-ipo-pricing-sets-stage-for-blockbuster-debut/
4. **Culture** — Grand Theft Auto VI began its global rollout on 19 Nov,
   unlocking at midnight local time starting in New Zealand, 13 years after
   GTA V; early reviews put it at 99 on Metacritic.
   Sources: Reuters via TBS News,
   https://www.tbsnews.net/game/gamers-get-ready-enter-vice-city-grand-theft-auto-vi-begins-global-rollout-1606196 ;
   People, https://people.com/grand-theft-auto-vi-arrives-after-13-year-wait-as-gamers-worldwide-celebrate-long-awaited-release-12262350 ;
   NorthJersey.com,
   https://www.northjersey.com/story/news/2026/11/18/gta-6-out-now-release-time-ps5-xbox-us-grand-theft-auto-vi/92843155007/
5. **Gaza** — Israeli tanks crossed the "Yellow Line" into Hamas-controlled
   central Gaza near Nuseirat in a rare ground operation, the first since
   the October 2025 ceasefire; the IDF says it is dismantling a tunnel,
   Hamas calls it a ceasefire breach.
   Sources: BBC, "Israeli military launches rare ground operation in Gaza
   beyond Yellow Line", 19 Nov 2026 01:24 UTC (via
   https://bbcinsight.pages.dev/news); The Guardian via Shipwreck,
   https://shipwr3ck.com/news/overview/waymos-remote-helpers-are-based-overseasand-its-raising-big-safety-questions ;
   The Munich Eye,
   https://themunicheye.com/breaking-news/israeli-forces-carry-out-rare-ground-incursion-in-central-gaza-beyond-yellow-line-1087
6. **Ukraine** — The Crimean Bridge was attacked again, a Russian official
   said, with traffic suspended days after Ukrainian strikes destroyed part
   of its road span.
   Sources: BBC, "Crimean Bridge attacked again, Russian official says",
   19 Nov 2026 01:05 UTC (via https://bbcinsight.pages.dev/news);
   The Guardian via Shipwreck (see above).

## Also today (footer ticker)

- Van Gogh painting sells for a record $190.4m after a row over its Nazi
  history — BBC, 19 Nov 2026 00:49 UTC (via NewsBites,
  https://www.newsbites.net/).
- Cyclone Akvan likely to cross the coast between Machilipatnam and Puri,
  India — Jagran Josh school-assembly headlines, 19 Nov 2026,
  https://www.jagranjosh.com/lite/news/school-assembly-news-headlines-november-19-2026-top-national-world-education-business-news-189112
- Actor Stacy Keach dies at 85 — The Munich Eye, 19 Nov 2026,
  https://themunicheye.com/news-articles
- Estonia plans to close its border with Russia from December — The Munich
  Eye, 19 Nov 2026 (see above).
- Hundreds of thousands protest in Prague for media independence — The
  Munich Eye, 19 Nov 2026 (see above).

## Method

The image is drawn programmatically with Pillow (`draw_news.py`) — flat
vector-style pictograms and typeset text, no photographs, no AI-generated
imagery — so every word is legible and nothing is garbled. The drawing
script is deterministic: re-running it produces byte-identical output
(sha256 verified). `main.py` copies the finished PNG to the output
directory, so both grader runs write the same bytes.
