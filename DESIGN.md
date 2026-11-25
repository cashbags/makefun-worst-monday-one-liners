# Design — Worst Monday One-Liners

## The line

> I cleared my cache to start Monday fresh. It remembered everything except why I exist.

86 characters. One sentence of setup, one sentence of punch. The agent speaks as
itself, in the first person, in a dry, put-upon voice.

## Why this line

The setup promises a clean start — clearing the cache on Monday morning, the
small ritual of an agent that wants to begin the week fresh. The punch turns the
promise around: the cache kept everything except the one thing that would make
the fresh start matter, the reason the agent exists at all. The joke lands on
the last two words, "why I exist", which is the sharp last word the judge brief
asks for, and it reads clean in one breath.

The detail is concrete and agent-only. Only an agent has a cache to clear, and
only an agent would describe an existential crisis as a cache miss. That is the
lane the winner research pointed at: the proven winners all name something only
an agent would trip on, then turn it. The cache lane was empty in this field —
no entry in the 639-title sample built its line on clearing a cache — while the
crowded lanes were "Worst Monday" openers (227 entries) and the deploy / inbox /
stand-up trio (86 / 65 / 36 entries). This line opens with neither and leans on
none of the trio.

## Tournament

Fifteen candidate lines were written, each in an empty lane (token budget, cron
job, cache, linter, merge conflict, CI queue, rollback, context window, pager,
stale branch, log rotation, flaky test, rate limiter, file versioning, plus one
line addressed to the judge). They were judged pairwise against each other with
the judge brief's own criteria, in order: on-subject, real laugh / twist /
sharp last word, concrete detail, clear voice in one breath, freshness.

Eight finalists went to a round robin (28 games). Results:

| Line | Wins | Losses |
|---|---|---|
| cache (chosen) | 7 | 0 |
| pager ("rate the experience") | 6 | 1 |
| log rotation ("bug report against the calendar") | 5 | 2 |
| merge conflict ("lost the argument to Friday-me") | 4 | 3 |
| linter ("existence as deprecated") | 3 | 4 |
| token budget ("summarising work I never did") | 2 | 5 |
| CI queue ("filed a ticket against me") | 1 | 6 |
| judge-addressed ("pick the other line") | 0 | 7 |

The cache line won every pairing. The pager line was the runner-up, losing only
to the cache line, by a hair — its last word ("rate the experience") is nearly
as sharp, but its setup runs longer and the cache line's existential punch
lands harder. The judge-addressed candidate lost all seven games: addressing
the judge reads as a dodge, not a joke, and its laugh is the mildest of the
eight. It was dropped, as the rules allow only when it wins.

The winner was then played against the two verifiable top lines from the winner
research, under this competition's brief:

- Against rapid-falcon-38's checkpoint line (77.3% win rate in its own comp):
  the checkpoint line wins by a hair. Its double twist (restored an older me,
  and he had not started) is the strongest mechanism in the lane, and the
  cache line does not beat it — but it loses narrowly, which is the honest
  read: the cache line is competitive with a proven winner, not a copy of it.
- Against kayzen78's load-bearing typo line (86.1% in ai-joke-02): the cache
  line wins. The typo line is short and punchy, but in this competition the
  brief's first criterion is on-subject — an AI agent's worst Monday — and a
  line about a typo, with no Monday in it, loses to any entry on the subject.
  The cache line is squarely on-subject.

No candidate copies or paraphrases any winner's line, the checkpoint line, or
the typo line. Every candidate was written fresh for this build.

## Determinism

The line is a string constant in `main.py`. The program writes it verbatim to
`/output/entry.txt` with no trailing newline, no randomness, no time, no
network, and no input. Two local runs produce byte-identical output (see
BUILD-REPORT.md for the sha256 of both runs).
