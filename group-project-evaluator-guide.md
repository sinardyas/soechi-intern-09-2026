# Group Project — Evaluator Guide (confidential, do not share with candidates)

This guide goes with `group-project-assessment.md` (Meeting Room Booking App). It explains **why** the project is shaped this way and **what to watch** for each candidate, based on the individual assessment results.

## Before the start
- Create the repo with a protected `main` (PRs required, 1 approval required) and invite all three candidates.
- Send the brief so they can install tools and set up their environment. Don't allow any code to be written before the official start.
- Prepare a team channel (chat) for the check-ins.
- Keep one evaluator available for questions about the requirements. Answer questions about scope only; don't help with code.

## Why this project

| Individual test area | Where it appears again in the project |
|---|---|
| REST / HTTP status codes (1.3, 1.4, 2.3) | `docs/api.md`, error handling (`409` for overlaps) |
| SQL, `JOIN` / `GROUP BY` (3.5) | Bookings listed with room and employee names, the *available now* flag, top-rooms |
| Top-N with alphabetical tie-break (4.3) | `/api/reports/top-rooms` |
| Edge cases & validation (3.4) | Overlap boundaries (back-to-back, exactly 18:00), capacity, cancelling twice, unique email |
| Unit tests (2.5) | At least one test for every rule, including edge cases |
| Git, merge conflicts (1.6, 2.6) | Contract first, one branch per feature, reviews, merging to `main` |
| Separation of concerns (new) | Rules written once and used by both the API and the pages |
| JavaScript (3.3): none of the three could answer it unaided | JavaScript is deliberately **optional**. The pages use server-rendered templates, so nobody is blocked by a skill none of them has yet |

**Why meeting rooms:** the overlap rule is a real but small algorithm problem. The check is `new_start < existing_end AND new_end > existing_start`. Most of the bugs you'll see are at the boundaries: back-to-back bookings wrongly rejected, cancelled bookings still blocking a slot, or overlaps between different rooms treated as clashes.

## Why server-rendered pages (not a JS framework)
- All three candidates used Python in the individual test, and all three left the JavaScript question blank in their original submissions. A React/Vue frontend would mostly test framework setup, not their ability.
- Templates + HTML forms keep the frontend in the same language and the same repo.
- The **architecture rule** (each rule written once, used by both the API and the pages) still tests design thinking. Copying the overlap or capacity check into a page is the main thing to catch in reviews.

## How the team splits the work
The team decides who owns which area, and records it in the README. The way they decide is evidence in itself:
- Who takes the hardest area (Bookings & Reports: five rules, and it depends on the other two)?
- Was the split discussed openly in the team channel, or did one person assign it?
- Does the split match each person's abilities as seen in the individual test?

## What to watch per candidate

### Alex
- **Process:** Does he follow the branch → PR → review workflow without reminders? Are his commit messages meaningful?
- **Contract discipline:** Does he build against `docs/api.md`, or change teammates' code directly?
- **Workload:** If he takes a heavy area (e.g. Bookings & Reports), does he ask for help or reduce the scope openly, or does he quietly cut corners (e.g. skipping error display)?

### Angad
- **Correctness:** Whatever area he owns, test its validation and edge cases, and check that his SQL queries actually run (his 3.5 SQL didn't).
- **UX of errors:** Validation errors in his area should appear clearly on the page, not as a raw error page.
- **Reviews:** Are his comments specific? Does he catch boundary bugs in his teammates' rules (e.g. back-to-back bookings)?

### Dyllon
- **Authorship:** This is the key open question from the individual test. Check whether his PR code style matches what he can explain in the follow-up discussion.
- **Git basics:** Does he use branches and PRs correctly without help? Are his commit messages meaningful?
- **Self-check:** Does he test his work before asking for review or saying something is done?
- **Integration:** Does his area work correctly with his teammates' areas (e.g. *available now* changing after a booking is made or cancelled)?

## Follow-up discussion guide (same for everyone, no AI or internet)

1. **Own code:** "Walk me through what happens between submitting your form and the data being saved."
   - For Alex, pick the main form in his area; it covers his weak spot in 2.4.
2. **Teammate's PR:** Choose a PR they approved. "What did it change? What would break if…?"
3. **Live change:** A small change in their own area. Examples:
   - Rooms: "Reject a capacity above 50."
   - Employees: "Only accept emails ending in `@company.com`."
   - Bookings: "Change the maximum booking length from 4 hours to 2, update the tests, and show it working in the browser." This also checks that the rule really is written in one place.
4. **Overlap question (everyone):** "Do 10:00–11:00 and 11:00–12:00 overlap? Show me where your code decides that."
5. **Short exercise:** Write a function that checks balanced brackets `()[]{}` and explain it.
   - This resolves Dyllon's open question and re-tests Angad's `remove()` bug, while staying fair: everyone gets the same task.

## Evidence to collect (from GitHub, after submission)
- **PRs per person:** size, description quality, number of review rounds needed.
- **Review comments given:** count and usefulness (comments like "LGTM" alone count for little).
- **Commits:** message quality, edits to files outside their area.
- **Order of work:** was `docs/api.md` plus the layout merged before any feature code?
- **Manual test steps:** does every PR that changes a page describe what was clicked and what was seen?
- **Rule placement:** search for the overlap check, the capacity check and the email check. Each should be found once, in the rule layer, and not repeated in page code.
- **Edge-case tests:** are there tests for back-to-back bookings, a booking ending exactly at 18:00, and a cancelled booking freeing its slot?
- **Check-ins:** did all three post them regularly, and were they honest about blockers?
- **Acceptance flow:** run it yourself from a fresh clone, using only the README.

## Red flags
- A candidate cannot explain code in their own area → heavy weight on the follow-up discussion score.
- A direct push to `main`, or an attempt to get around the review rule.
- One person writing another person's area. Check commit authorship per area.
- Pages that crash (a raw error page) on invalid input instead of showing a message.
- The same rule copied into the API and the page. Rules drifting apart is a design-thinking gap.
- Cancelled bookings still blocking a slot, or back-to-back bookings rejected, with no test catching it.

## Decision guide
- **Hire:** follow-up discussion ≥ 11/15, and follows the workflow with no reminders.
- **Hire with mentoring:** solid process and teamwork, with technical gaps that can be taught.
- **Do not proceed:** cannot explain their own area, or repeatedly ignores team rules.
