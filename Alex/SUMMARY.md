# Alex — Assessment Summary

**Final (merged) score: 85.5 / 100** · **Original supervised submission: 78.5 / 100**
Source: PR [#3](https://github.com/sinardyas/soechi-intern-09-2026/pull/3) (`alexander-nathanael-chung` → `main`, merged 2026-09-24 09:29Z)

| Part | Original | Final | Notes |
|---|---|---|---|
| 1 — Multiple Choice | 16 / 20 | 20 / 20 | 1.6 and 1.9 were wrong at first and fixed in revision |
| 2 — Short Answer Theory | 14.5 / 21 | 14.5 / 21 | Unchanged across revisions; correct but often shallow |
| 3 — Code Reading & Debugging | 14.5 / 20 | 18 / 20 | 3.3 was "N/A" at first and answered in revision |
| 4 — Live Coding | 33.5 / 39 | 33 / 39 | All three work; complexity barely discussed |

The original score reflects the first commit (`6c2aabd`, 2026-09-23 13:23Z), submitted under quiz conditions. Everything after that was written after review started, outside supervision.

## Strengths
- The strongest supervised result of the three candidates. All Part 4 code and the SQL were correct on the first submission.
- Correct SQL (`JOIN` + `GROUP BY` + `HAVING` + `ORDER BY`) and a clean, idiomatic stack solution for brackets, with complexity stated.
- `top_words` replaces punctuation with a **space** instead of deleting it, so `"hat.The"` is split into `hat` and `the`. This is the only submission that handles that case.
- Includes a tie-breaking test case (`apple`/`banana`) for 4.3.

## Gaps
- Theory answers are thin. 2.4 (browser request) leaves out DNS, TCP/TLS and rendering. 2.5 defines a "good" unit test only as "tests one thing". None of these improved during revision.
- The Part 4 answers show no complexity awareness outside 4.2.
- **4.1 rework is bloated.** The reviewer asked for no `reversed()`, only basic methods and data types. The replacement in `alex-reverse_words.py` is 45 lines. Its second and third passes (trim, then collapse spaces) do nothing, because the first pass already builds clean output. `alex-answers.md` still shows the old `reversed()` version, so the two files disagree. In both versions the function is named `f`.

## Per-question notes

### Part 1
- 1.6 originally a) `git branch -d feature` and 1.9 originally c) O(n). Both were corrected in commit `8dcc2a9` without the reviewer asking.

### Part 2
| Q | Pts | Comment |
|---|---|---|
| 2.1 | 3 | Correct: separate vs shared memory, threads run concurrently inside a process |
| 2.2 | 2 | Correct contrast; the "situations" are generic (structured vs unstructured) rather than concrete |
| 2.3 | 2.5 | Good API definition. Names client-server and stateless. "All data processed by the server" is slightly off |
| 2.4 | 1 | Only request → HTML → display. No DNS, TCP/TLS or rendering |
| 2.5 | 1.5 | Explains why unit tests exist; the "good test" criteria are minimal |
| 2.6 | 2 | Explains what a conflict is and why it happens; "manual review" is vague on how to resolve it |
| 2.7 | 2.5 | Good: collect device/conditions and crash logs, then recreate. Calling it a "false positive" is questionable |

### Part 3
| Q | Pts | Comment |
|---|---|---|
| 3.1 | 4 | `[3, 2, 1]`; `list(reversed(items))` |
| 3.2 | 3 | Correct output and root cause. The fix removes the `bucket` parameter, which changes the API; the idiomatic fix is `bucket=None` |
| 3.3 | 3.5 (orig. 0) | "N/A" at first. Revised to `3 3 3` and `var` → `let`, but describes `var` as "global" when it is function-scoped |
| 3.4 | 3.5 | Spots the empty-list division by zero but doesn't name `ZeroDivisionError`. Returning `0` is a defensible choice |
| 3.5 | 4 | Correct and complete |

### Part 4 (correctness / edge cases / readability / complexity)
| Q | Pts | Comment |
|---|---|---|
| 4.1 | 9 (6/2/1/0) · orig. 9.5 | Correct in both versions. The original one-liner was cleaner; the rework has dead passes. Two tests, neither for empty input |
| 4.2 | 12 (6/2/2/2) | Correct and clean. Only two of the four spec cases are tested |
| 4.3 | 12 (6/3/2/1) | Correct, including tie-breaking and punctuation between words. Complexity not stated |

## PR & collaboration assessment

| Dimension | Rating | Evidence |
|---|---|---|
| Submission timeliness | Good | PR opened 2026-09-23 13:26Z, the same day as Angad's |
| Following repo conventions | Weak | First commit put files at the repo root, left behind a stray `testing.py`, and edited the shared `developer-internship-assessment.md`. It took two reminders (06:44Z and 09:05Z) to move everything under `Alex/` |
| Responsiveness | Good | Round 1 was addressed about 1 hour after review, with a reply on each thread. Round 2 (no `reversed()`) was addressed in about 30 minutes |
| Completeness of fixes | Adequate | Removed `testing.py` and split Part 4 into files, but missed the folder request in the first pass |
| Commit hygiene | Weak | 5 commits with vague messages ("Intern Test", "Alex Assessment Answers 2", "Update alex-answers.md") |
| Scope discipline | Weak | The final commit `8051c31` moved the shared question file into `Alex/`. After the merge, `main` no longer has `developer-internship-assessment.md` at the root; it only exists as `Alex/developer-internship-assessment.md`. The reviewer did not catch this |
| Self-correction | Adequate | Fixed 1.6, 1.9 and 3.3 without being asked. Did not revisit the weak theory answers |

**Repo action needed:** restore `developer-internship-assessment.md` at the repo root on `main` and delete `Alex/developer-internship-assessment.md`.

## Verification
- All `.py` files were executed against the spec examples plus extra cases (empty string, whitespace-only, `"([()])"`, `"hat.The cat"`, ties). Every submitted function returned the expected result.
- The original vs final answers were compared through the PR #3 commit diffs (`6c2aabd` → `8051c31`).

## Recommendation
**Strong candidate. Top of the group on supervised performance (78.5).** Reliable at practical coding, with gaps in explaining systems concepts and in repository discipline: files in the wrong place, a shared file moved, and vague commit messages. In an interview, probe web and networking fundamentals. Ask why the reworked 4.1 has three passes over the data, and explain why touching shared files in a PR is a problem.
