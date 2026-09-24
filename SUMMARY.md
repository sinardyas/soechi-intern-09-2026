# Internship Assessment — Summary

The **original** score is each candidate's first submission, written under quiz conditions. The **final** score is the merged PR, after edits made during review with AI and search allowed. Full detail is in each candidate's `SUMMARY.md`.

| Candidate | Original | Final | PR process | Verdict |
|---|---|---|---|---|
| **Alex** | **78.5** | 85.5 | Weak | Strongest technically |
| **Angad** | 61 | 74.5 | Strong | Best working habits |
| **Dyllon** | 57 | 83 | Weak (new to Git) | Most growth; needs verification |

## Alex — 78.5 → 85.5
- **Strengths:** All three coding answers and the SQL were correct on the first try. His word counter is the only one that handles punctuation between words (`"hat.The"`).
- **Weaknesses:** Theory answers are shallow (how a web request works, unit testing). He rarely discusses complexity. His reworked 4.1 has two extra passes that do nothing.
- **PR process:** Files were in the wrong place, he needed two reminders to use his folder, and his commit messages are vague. He also moved the shared questions file into `Alex/`.
- **Interview:** Probe web and networking fundamentals.

## Angad — 61 → 74.5
- **Strengths:** He writes the most thorough explanations. He was the only one to find both bugs in 3.4. He was honest about gaps ("not sure") instead of guessing.
- **Weaknesses:** His brackets solution has a bug and returns the wrong result for `"([()])"`. His SQL doesn't run. His first 4.1 answer didn't reverse the words. He has some conceptual errors about threads and APIs.
- **PR process:** The best of the group: correct folder from the start, one fix commit, clear commit messages, and a reply to every comment. The reviewer used his PR as the example for the others.
- **Interview:** Have him walk through `"([()])"` in his brackets code and fix the SQL.

## Dyllon — 57 → 83
- **Strengths:** He submitted first (PR #1, which he closed by accident). He replies quickly and politely, and he learns from feedback, including feedback given to others.
- **Weaknesses:** His unaided fundamentals are weak: he wrote "I lack the understanding of SQL/Git" and got SQL vs NoSQL wrong. He misdiagnosed the bug in 3.4. Most of his score increase came from edits made after AI was allowed.
- **PR process:** Three review rounds, files without extensions, a fix he said was done before it was, and 11 vague commits. These are typical first-time GitHub mistakes and easy to coach.
- **Needs checking:** His first submission already contained a word-for-word copy of a well-known LeetCode solution, while he said he didn't know the basics. Do a short live coding exercise before ranking him.

## Recommendation
1. **Alex:** hire on technical strength; coach Git discipline.
2. **Angad:** a strong fit if mentoring is available; his habits make up for gaps in precision.
3. **Dyllon:** decide after a live coding check.

## Repo action
Restore `developer-internship-assessment.md` to the root of `main`. The PRs from Alex and Dyllon moved or renamed it.
