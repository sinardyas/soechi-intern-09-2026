# Dyllon — Assessment Summary

**Final (merged) score: 83 / 100** · **Original supervised submission: 57 / 100**
Sources: PR [#1](https://github.com/sinardyas/soechi-intern-09-2026/pull/1) (`assessment-answe` → `main`, opened 2026-09-23 09:08Z; closed by accident by the candidate at 2026-09-24 04:33Z without review) and its replacement PR [#4](https://github.com/sinardyas/soechi-intern-09-2026/pull/4) (`patch-1` → `main`, merged 2026-09-24 09:29Z)

| Part | Original | Final | Notes |
|---|---|---|---|
| 1 — Multiple Choice | 16 / 20 | 20 / 20 | 1.6 and 1.9 were wrong at first |
| 2 — Short Answer Theory | 8 / 21 | 16 / 21 | 2.2, 2.3 and 2.6 were rewritten after the reviewer allowed AI and search |
| 3 — Code Reading & Debugging | 8.5 / 20 | 16.5 / 20 | 3.3 ("not sure") and 3.5 ("I lack the understanding of SQL") were added in revision |
| 4 — Live Coding | 24.5 / 39 | 30.5 / 39 | Tests were added only when the reviewer asked |

The original score reflects PR #1 (commits `1137671` and `be37702`, 2026-09-23 09:04–09:11Z), submitted under quiz conditions and before any review activity in the repo. When PR #4 was opened, its first commit (`73a7fd4`, 2026-09-24 06:52Z) carried over the same answers with only cosmetic changes: it restored a leftover `- a)` option line on 1.6 and added the note "i do not understand JSON" on 1.10. The score is therefore identical. At 07:01Z the reviewer told the candidate: *"if you don't understand something, please try to ask your AI friend or googling it."* The rewrites in `f9fcc7d` (07:20Z) were made under that permission. Of the three candidates, Dyllon's score rose the most in revision (+26).

## Strengths
- The final theory answers on 2.2, 2.3 and 2.6 are the most complete of the group (produced in the permitted revision).
- 2.4 (original, unaided) covers DNS, the HTTPS connection, request/response and rendering.
- 3.2 is the only submission that uses the idiomatic `bucket=None` fix, which keeps the function signature intact.
- Correct stack solution for brackets, with O(n)/O(n) complexity stated.
- Responds quickly and politely to every review comment, and applied a reviewer constraint from another candidate's PR (rewrote 4.1 without slicing) without being asked.

## Gaps
- **Weak unaided fundamentals.** The original said "i do not understand JSON", "i lack the understanding of Git" and "I lack the understanding of SQL", and described SQL as storing "pairs of key and value" (2.2). The final answers were written with permitted AI/search help and don't show what the candidate knew during the quiz.
- **3.4 misdiagnosed (not fixed in revision).** Blames string input and never mentions the empty list. The rewrite (`float(n)`) still raises `ZeroDivisionError` on `[]` and `ValueError` on `["abc"]` (both verified).
- 2.5 and 2.7 are thin and were never revised.
- `top_words` deletes punctuation instead of replacing it with a space, so `"hat.The cat"` produces `hatthe` (verified).
- Naming: the 4.1 function is `split_input` with a capitalized parameter `Input`, and the 3.1 one-liner uses an undefined `lst` instead of `items`.
- The 4.1 solution differs between `dyllon-assessment.md` (`[::-1]`) and `reverse_words.py` (manual loop).

## Per-question notes

### Part 1
- 1.6 was originally "not sure, assumption: a)" and was corrected to c).
- 1.9 was originally b) O(log n) and was changed to "a) O(log 1)". The letter is correct and O(log 1) = O(1), so it is scored as correct in the final version.
- 1.10 was originally "not sure, c)" in PR #1, with "i do not understand JSON" added in the first commit of PR #4. The letter is correct, so it gets credit.

### Part 2
| Q | Pts | Comment |
|---|---|---|
| 2.1 | 2 | Correct gist with a good game example; misses memory isolation vs sharing |
| 2.2 | 3 (orig. 0) | The original was factually wrong (SQL = key-value). The revision is clear, with concrete situations |
| 2.3 | 3 (orig. 1) | The original defined API only, with no REST. The revision is complete |
| 2.4 | 2.5 | Good high-level flow (original) |
| 2.5 | 1 | Why = "check code runs as expected"; good = same output for same input. Thin |
| 2.6 | 3 (orig. 0) | The original said "lack the understanding of Git". The revision is complete, including the resolution steps |
| 2.7 | 1.5 | Asks for expected vs actual and the machine version; no concrete investigation steps |

### Part 3
| Q | Pts | Comment |
|---|---|---|
| 3.1 | 3.5 | Correct; the one-liner references undefined `lst`, and `items[::-1]` would be simpler |
| 3.2 | 4 | Correct output, root cause and idiomatic fix |
| 3.3 | 4 (orig. 0) | "not sure" at first. The revision is correct, with a clear per-iteration binding explanation |
| 3.4 | 1 | Misses the empty-list case; the fix does not fix it |
| 3.5 | 4 (orig. 0) | "I lack the understanding of SQL" at first. The revision is correct |

### Part 4 (correctness / edge cases / readability / complexity)
| Q | Pts | Comment |
|---|---|---|
| 4.1 | 9 (6/2/1/0) · orig. 7 | Correct. Poor naming. No tests originally; tests were added at the reviewer's request |
| 4.2 | 12 (6/2/2/2) · orig. 10 | Correct. No tests originally; now covers two of the four spec cases |
| 4.3 | 9.5 (5/2/1.5/1) · orig. 7.5 | Spec example passes. `"hat.The"` merges into one word. Imports are inside the function, and `most_common()` followed by a full re-sort is redundant |

## PR & collaboration assessment

| Dimension | Rating | Evidence |
|---|---|---|
| Submission timeliness | Strong | **First submission of the group.** PR #1 was opened 2026-09-23 09:08Z, before Angad (12:49Z) and Alex (13:26Z). He closed it by accident and reopened it as PR #4 at 2026-09-24 06:53Z, which put it last in the review queue. By his own account (2.6: "i lack the understanding of Git") he is not yet familiar with GitHub |
| Following repo conventions | Weak | Both PR #1 and the first commit of PR #4 edited the shared `developer-internship-assessment.md` in place (deleting the MCQ options) using GitHub web-editor branches. It needed a reminder to use a named folder. Part 4 files were first created without extensions (`check_parentheses`, `top_word`), and the reviewer flagged "wrong file format" |
| Responsiveness | Strong | Fast turnaround: round 2 was fixed in about 15 minutes and round 3 in about 6 minutes. A polite reply on every thread |
| Completeness of fixes | Weak | Three review rounds were needed. The 08:00Z reply said "I have made the python functions into files" while the brackets file was still empty (added only at 08:28Z, after "where is the file for this?"). Tests had to be requested separately |
| Commit hygiene | Weak | 11 commits across the two PRs, with web-editor defaults or uninformative messages ("Update developer-internship-assessment.md", "updates", "update", "fixed", "fixed #2", "changes") |
| Scope discipline | Weak | Renamed the shared question file into `Dyllon/dyllon-assessment.md` instead of adding a new file. Together with Alex's PR, this removed `developer-internship-assessment.md` from the root of `main` |
| Self-correction | Good | Used the permitted resources to fill every gap, and applied the reviewer's no-built-ins constraint from Alex's PR to 4.1 without being asked |

## Integrity note (revised after PR review)
The earlier concern about the difference in writing quality between answers is **explained by the PR history**. The polished answers to 2.2, 2.3, 2.6, 3.3 and 3.5 were written after the reviewer explicitly allowed AI and search, so they are sanctioned revisions and not a violation. They should not count as evidence of what the candidate knew unaided.

One inconsistency remains in the **original, supervised** submission (PR #1, 2026-09-23, before any review activity existed that could have been copied). The same submission that says "I lack the understanding of SQL/Git" contains Part 4 code that uses `collections.Counter` and `re`, has tutorial-style comments, and is word for word the well-known LeetCode #20 reference solution for brackets (`'#'` sentinel; the file was later renamed `is_valid_parentheses`). This is a signal, not proof. Suggested check: ask the candidate to write balanced brackets live and to explain the `'#'` sentinel.

## Verification
- All `.py` files were executed against the spec examples plus extra cases (empty string, whitespace-only, `"([()])"`, `"hat.The cat"`, ties). The 3.4 rewrite was executed on `[]`, `["1","2"]` and `["abc"]`.
- The original vs final answers were compared through the PR #1 diff and the PR #4 commit diffs (`73a7fd4` → `64f4271`). PR #1's answers match the first commit of PR #4, apart from the cosmetic changes noted above.

## Recommendation
**Weakest supervised result (57), with the largest rise after revision.** The final 83 mostly reflects permitted open-book revision. Strengths are submitting first, responsiveness, politeness, and willingness to learn from feedback, including feedback given to others. Weaknesses are unaided fundamentals, first-attempt quality, and following repo conventions. The Git/GitHub process problems (the accidentally closed PR, in-place edits of the shared file, extensionless files, vague commits) fit a first-time GitHub user and are very coachable, so weigh them lightly for an early-year candidate. Resolve the Part 4 authorship question with a short live exercise before ranking.
