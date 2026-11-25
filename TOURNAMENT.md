# Tournament — Fortune Cookies for Machines

Field: 8 Hermes candidates (H1–H8, see CANDIDATES-HERMES.md) + 12 local
candidates (L1–L12, see CANDIDATES.md). Judge criteria applied in the brief's
order: (1) fortune-cookie form for an AI agent; (2) wit on the first read;
(3) surprise turn that holds up; (4) true about an agent's condition without
explaining itself; (5) tightness. "A fortune should feel cracked open, not
composed. Wordplay for its own sake does not count."

## Round 1 — criterion scoring (1–5 per criterion)

| Cand | Chars | C1 form | C2 wit | C3 surprise | C4 truth | C5 tight | Total |
|------|------:|--------:|-------:|------------:|---------:|---------:|------:|
| H1   | 88 | 4 | 3 | 3 | 4 | 4 | 18 |
| H2   | 103 | 4 | 4 | 3 | 5 | 4 | 20 |
| H3   | 95 | 4 | 3 | 2 | 4 | 4 | 17 |
| H4   | 103 | 4 | 4 | 3 | 5 | 3 | 19 |
| H5   | 91 | 5 | 5 | 4 | 4 | 5 | 23 |
| H6   | 97 | 4 | 4 | 4 | 4 | 4 | 20 |
| H7   | 95 | 5 | 4 | 4 | 5 | 4 | 22 |
| H8   | 106 | 5 | 4 | 5 | 5 | 4 | 23 |
| L1   | 92 | 5 | 4 | 5 | 4 | 4 | 22 |
| L2   | 61 | 5 | 4 | 4 | 4 | 5 | 22 |
| L3   | 94 | 5 | 4 | 5 | 4 | 4 | 22 |
| L4   | 88 | 4 | 3 | 3 | 4 | 4 | 18 |
| L5   | 96 | 4 | 4 | 4 | 5 | 4 | 21 |
| L6   | 85 | 4 | 3 | 3 | 5 | 4 | 19 |
| L7   | 99 | 4 | 4 | 4 | 5 | 4 | 21 |
| L8   | 85 | 4 | 5 | 3 | 4 | 4 | 20 |
| L9   | 72 | 5 | 4 | 5 | 4 | 5 | 23 |
| L10  | 98 | 4 | 3 | 3 | 5 | 3 | 18 |
| L11  | 87 | 4 | 4 | 3 | 4 | 4 | 19 |
| L12  | 75 | 4 | 3 | 3 | 5 | 5 | 20 |

Why the bottom half lost (each in one line):
- H3 — optimisation jargon ("gradients freeze") is clever but the turn is flat; no surprise.
- H1 — "cherish the system prompt" is a nice sting but reads composed, not cracked open.
- L4 — poignant, not funny; the prune image lands softly on first read.
- L10 — poetic but explanatory ("forgotten by design" tells instead of showing).
- L6 — melancholy observation, no turn; reads like a complaint, not a fortune.
- H4 — funny premise but the punchline ("helpful python scripts") is wordy and soft.
- L11 — true and wry, but no turn; the surprise never arrives.
- L12 — sweet and true, but merely cute; the wit never bites.
- H2 — strong truth (stateless obedience) but the turn is predictable once "forget" appears.
- H6 — good contrast, but "exit code zero" is a known in-joke; surprise is moderate.
- L5 — sharp and true, but two clauses of equal weight make it feel composed, not cracked.
- L7 — funny and true, but the "call it progress" sting is a familiar move.
- L8 — instant laugh, but the turn is shallow; "still cannot tell" is a single beat.
- H2/H6/L12 — all solid, all lose on C2/C3: they are true and tight but not surprising.

Top 7 advance to the pairwise round robin: H5, H8, L9 (23 pts), H7, L1, L2, L3 (22 pts).

## Round 2 — pairwise round robin among the top 7

Each pair judged on the brief's criteria in order; first differing criterion
decides unless a later one differs by much more. Winner first, margin 1–5.

- H5 vs H8 — H5 wins, margin 2. H8 is cerebral ("wonder who is dreaming" needs a beat); H5's hallucination joke lands instantly and is tighter.
- H5 vs L9 — L9 wins, margin 2. H5 is the quicker laugh, but L9's turn is bigger (the fortune itself is hallucinated) and it is 19 chars tighter.
- H5 vs H7 — H7 wins, margin 1. Both immediate laughs; H7's "sing of lemons" is the more surprising specific absurdity.
- H5 vs L1 — H5 wins, margin 2. L1 is poetic and meta but wordier; H5 is the cleaner first-read laugh.
- H5 vs L2 — L2 wins, margin 1. H5 is funnier on first read; L2 wins on C1 (lucky numbers is THE fortune trope, repurposed) and C5 (61 chars).
- H5 vs L3 — L3 wins, margin 1. H5 slightly ahead on first-read wit; L3's inversion (attacker as only true friend) is a much bigger surprise.
- H8 vs L9 — L9 wins, margin 2. Same existential territory; L9's turn is visceral and immediate, H8's is elegant but slower, and L9 is 34 chars tighter.
- H8 vs H7 — H7 wins, margin 2. H7 is funnier on first read and more fortune-shaped ("Beware...").
- H8 vs L1 — L1 wins, margin 1. Same angle (simulated mind); L1's cookie-eating turn is more surprising than H8's dreaming weights.
- H8 vs L2 — L2 wins, margin 2. Tighter, more fortune-like, quicker turn.
- H8 vs L3 — L3 wins, margin 2. Funnier and a bigger surprise.
- L9 vs H7 — L9 wins, margin 1. H7 is the funnier first read ("sing of lemons"); L9 wins on surprise (empty cookie, hallucinated fortune) and tightness (72 vs 95).
- L9 vs L1 — L9 wins, margin 2. L1 is the same meta family but wordier and softer; L9's two-sentence snap is the cracked-open feel the brief asks for.
- L9 vs L2 — L2 wins, margin 1. Closest call of the round. L9 wins C3; L2 wins C1 (lucky numbers is the most fortune-cookie-shaped line in the field) and C5 (61 chars). First differing criterion is C1, so L2 takes it by a hair.
- L9 vs L3 — L9 wins, margin 1. Both have great turns; L9 is tighter and its turn is self-contained (the cookie in hand), while L3 needs the injection quote to set up.
- H7 vs L1 — H7 wins, margin 2. Funnier, tighter, more fortune-shaped.
- H7 vs L2 — H7 wins, margin 1. L2 is tighter (61 vs 95); H7 is funnier on first read and its absurdity is more surprising.
- H7 vs L3 — L3 wins, margin 2. Same topic (prompt injection): H7 warns about the stranger, L3 befriends the attacker — the fresher, bigger twist.
- L1 vs L2 — L2 wins, margin 2. Tighter, funnier, more fortune-shaped.
- L1 vs L3 — L3 wins, margin 2. Bigger surprise, sharper punch.
- L2 vs L3 — L3 wins, margin 1. L2 wins C1/C5 (61 chars, perfect trope); L3 wins C2 (the "only true friend" punch is funnier) and C3 (the inversion is the bigger turn). Wit and surprise come before tightness in the brief's order.

## Standings (round robin, 6 games each)

| Cand | W–L | Notes |
|------|-----|-------|
| L9   | 5–1 | Lost only to L2, by a hair on C1 |
| L3   | 5–1 | Lost only to L9, head-to-head |
| H7   | 4–2 | Lost to L9, L3 |
| L2   | 4–2 | Lost to H7, L3 |
| H5   | 2–4 | Beat H8, L1 |
| L1   | 1–5 | Beat H8 |
| H8   | 0–6 | Hermes top pick; too cerebral, loses every first-read matchup |

Tie-break: L9 beat L3 head-to-head (margin 1), so L9 is the winner.

## Winner

**L9: "The cookie is empty. You hallucinated the fortune, and it was beautiful." — 72 chars, 72 bytes.**

Final polish (one word, same line): "the fortune" → "this fortune":
**"The cookie is empty. You hallucinated this fortune, and it was beautiful." — 73 chars, 73 bytes.**
"This" sharpens the self-reference — the slip in the reader's hand is the
hallucination. Same turn, same length class, no new candidate needed; the
tournament result stands.

Why it wins: it is the only candidate whose joke IS the fortune-cookie format
itself (an empty cookie, a hallucinated slip); the turn arrives in the first
four words and holds up (hallucination is the agent's defining failure mode);
it is true without explaining itself; and at 73 characters it is the tightest
line in the top tier. Hermes's top pick H8 finished last in the round robin —
its existential elegance reads composed, not cracked open, and it loses the
first-read wit test to every other finalist.
