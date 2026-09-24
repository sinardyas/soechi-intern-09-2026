# Angad — Assessment Summary

**Final (merged) score: 74.5 / 100** · **Original supervised submission: 61 / 100**
Source: PR [#2](https://github.com/sinardyas/soechi-intern-09-2026/pull/2) (`angad-answers` → `main`, merged 2026-09-24 09:29Z)

| Part | Original | Final | Notes |
|---|---|---|---|
| 1 — Multiple Choice | 16 / 20 | 18 / 20 | 1.6 fixed. 1.9 value fixed but the letter was left wrong |
| 2 — Short Answer Theory | 12 / 21 | 14.5 / 21 | 2.6 was "Not sure" at first |
| 3 — Code Reading & Debugging | 11 / 20 | 15 / 20 | 3.3 was unanswered at first (honest); the SQL is still broken |
| 4 — Live Coding | 22 / 39 | 27 / 39 | Original 4.1 did not reverse the words; the brackets bug remains |

The original score reflects the first commit (`fb28bf2`, 2026-09-23 12:42Z), submitted under quiz conditions. Everything in `7e12565` was written after review started.

## Strengths
- The most thorough explanations of the three. 2.4 walks through DNS → IP → TCP → HTTP GET → HTML → render. 2.5 mentions normal and edge-case inputs with expected outputs.
- 3.4 is the only submission to name **both** failure modes: `ZeroDivisionError` on an empty list and `TypeError` on string elements.
- Code is well commented, the reasoning is visible, and test cases include ties and punctuation (4.3) and several spaces in a row (4.1).
- **Honest.** The original marked uncertain answers ("Not sure, assumption: …") and wrote "I have not learnt Javascript" instead of guessing. The reviewer explicitly acknowledged this.
- **Best PR practice of the three** (details below). The reviewer pointed the other candidates to this PR as the reference.

## Gaps
- **Original 4.1 misread the task.** `manipulate()` only collapsed spaces and never reversed the word order, and its expected outputs followed the same misreading. The revision fixed this.
- **4.2 bug (in both versions).** `brackets.remove(brackets[-1])` removes the *first* matching element, not the top of the stack. `"([()])"` returns `False` instead of `True` (verified). The candidate's own tests happen to miss this. It also makes each pop O(n), so the worst case is O(n²), not the stated O(n).
- **3.5 SQL does not run.** It joins `departments` to itself, uses `department.salary` and an undeclared `employees`. The overall shape (`GROUP BY` / `HAVING COUNT > 3` / `ORDER BY DESC`) is right. It was not fixed in revision.
- 2.1 contains a factual error: "if one thread fails, the threads after that will also fail". It also leaves out the key point that threads share their process's memory.
- 2.3 mixes authentication into the definition of an API.
- 4.3 is O(n·u) for counting (`list.count` per unique word) plus a hand-written O(u²) selection sort, and complexity is never discussed. Like Dyllon's, it deletes punctuation instead of replacing it with a space, so `"hat.The"` becomes `hatthe`.
- Test cases are written in docstrings and never run.

## Per-question notes

### Part 1
- 1.4 and 1.10 were originally marked "Not sure, assumption: …" but were correct, so they get credit.
- 1.6 was originally a) `git branch -d feature` and was corrected to c) in revision.
- 1.9 was originally "c) O(n)" (wrong). The revision changed the value to O(1) but kept the letter c, which is where the "c) O(1)" mismatch comes from. Scored **0** in both versions because the chosen letter is still wrong.

### Part 2
| Q | Pts | Comment |
|---|---|---|
| 2.1 | 1.5 | The browser example is reasonable. The thread-failure claim is wrong and memory sharing is not mentioned |
| 2.2 | 2 | Sensible form example; admits limited NoSQL knowledge |
| 2.3 | 1.5 | Names client-server and stateless correctly, but the API definition is muddled (authentication) |
| 2.4 | 2.5 | Good sequence; no TLS even though the URL is `https` |
| 2.5 | 2.5 | Good, with normal and edge cases and expected outputs |
| 2.6 | 2.5 (orig. 0) | "Not sure" at first. The revision explains why conflicts happen clearly; resolution given only as "manually decide" |
| 2.7 | 2 | Recreating the environment is good; jumps quickly to blaming third-party software; no logs |

### Part 3
| Q | Pts | Comment |
|---|---|---|
| 3.1 | 4 | Correct, with a list-comprehension one-liner |
| 3.2 | 3 | Correct output. The fix removes the `bucket` parameter; the idiomatic fix is `bucket=None` |
| 3.3 | 4 (orig. 0) | Unanswered at first. The revised answer (after the reviewer gave time to learn JS) is correct, with a clear block-scope explanation |
| 3.4 | 3 | Both errors identified. The fix silently skips strings, and a list of only strings still raises `ZeroDivisionError` (verified). `type(n) != str` is fragile |
| 3.5 | 1 | Correct clauses, but the table/alias references are broken and the query cannot run |

### Part 4 (correctness / edge cases / readability / complexity)
| Q | Pts | Comment |
|---|---|---|
| 4.1 | 9.5 (6/2/1.5/0) · orig. 4.5 (1/2/1.5/0) | The original did not reverse the words. The revision is correct. The parameter is named `word` but holds a sentence |
| 4.2 | 8 (3/2/1.5/1.5) | Passes the spec examples but fails `"([()])"`. A repetitive if-chain where a mapping would do. The stated O(n) is inaccurate because of `remove` |
| 4.3 | 9.5 (5/3/1.5/0) | Correct on the spec and the tie cases. Merges words around punctuation. Inefficient, with no complexity discussion |

## PR & collaboration assessment

| Dimension | Rating | Evidence |
|---|---|---|
| Submission timeliness | Good | Opened 2026-09-23 12:49Z, the second submission after Dyllon's PR #1 (09:08Z) and the first PR to be reviewed |
| Following repo conventions | Strong | Files were under `Angad/` from the first commit, and no shared files were touched. The reviewer cited this PR as the reference for the others |
| Responsiveness | Good | Review at 06:29–06:33Z; one fix commit at 07:50Z (about 1h20m); a reply on every thread at 08:06Z |
| Completeness of fixes | Strong | Both review comments were fully addressed in one pass, with no follow-up round needed |
| Commit hygiene | Good | 2 commits with descriptive messages ("Add Angad assessment answers", "Adress PR review comments") |
| Scope discipline | Strong | Only touched `Angad/*` |
| Self-correction | Good | Beyond what was requested, fixed 4.1, 1.6, 1.9 (partly), and 2.6. Did not catch the SQL or brackets bugs |

## Verification
- All `.py` files were executed against the spec examples plus extra cases (empty string, whitespace-only, `"([()])"`, `"hat.The cat"`, ties). The 3.4 rewrite was executed on `[1,2,3]`, `[]` and `["a","b"]`.
- The original vs final answers were compared through the PR #2 commit diffs (`fb28bf2` → `7e12565`).

## Recommendation
**Promising, with the best working habits of the group.** Supervised technical accuracy was the second-weakest (61). The misread 4.1, the stack misuse and the broken SQL show gaps in precision. On the other hand, honesty about what they didn't know, clean PR practice and complete one-pass fixes are exactly the habits that are hard to teach. A good fit if the internship has mentoring capacity. In an interview, ask the candidate to trace `"([()])"` through `check_brackets` and to fix the SQL.
